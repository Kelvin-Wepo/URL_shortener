from flask import Flask, redirect, request
import string
import random

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'  # Change this to your domain name

url_map = {}

def generate_short_url():
    # Generate a short URL using 6 random characters
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(characters, k=6))
    return short_url

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle form submission
        long_url = request.form['url']
        short_url = generate_short_url()
        url_map[short_url] = long_url
        return f'Short URL: <a href="{short_url}">{short_url}</a>'
    else:
        # Show the home page with a form to submit a URL
        return '''
            <form method="post">
                <label for="url">Enter a URL:</label>
                <input type="text" id="url" name="url" required>
                <button type="submit">Shorten</button>
            </form>
        '''

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = url_map.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return 'Short URL not found'

if __name__ == '__main__':
    app.run(debug=True)
