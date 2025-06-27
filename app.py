from flask import Flask, render_template, request
import pickle
import numpy as np
import os

# Load data from pkl files
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(popular_df['Book-Title'].values),
        author=list(popular_df['Book-Author'].values),
        image=list(popular_df['Image-URL-M'].values),
        votes=list(popular_df['num_ratings'].values),
        rating=list(popular_df['avg_ratings'].values),
    )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    if not user_input:
        return render_template('recommend.html', data=[], not_found=True)

    user_input = user_input.strip().lower()

    # Normalize pt.index once before matching
    pt.index = pt.index.str.lower().str.strip()

    matching_indices = np.where(pt.index == user_input)[0]

    if matching_indices.size == 0:
        # No match found – return empty recommendations
        return render_template('recommend.html', data=[], not_found=True)

    index = matching_indices[0]

    similar_items = sorted(
        enumerate(similarity_scores[index]),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    data = []
    for i in similar_items:
        item = []

        # Match using normalized title
        title = pt.index[i[0]]
        temp_df = books[books['Book-Title'].str.lower().str.strip() == title]

        if temp_df.empty:
            continue

        # Use drop_duplicates to avoid repeats
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    print(data)  # Optional debug
    return render_template('recommend.html', data=data)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    # Use dynamic port on deployment platforms like Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
