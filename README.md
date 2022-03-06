# Touch - grass
GitHub repository for the Touch Grass project for MLH's "A Hack A Day" hackathon.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/abigailnacional/touch-grass.git
   ```
2. Navigate to the folder
   ```sh
   cd touch-grass
   ```
3. Run install.sh by dragging the file into your terminal.

4. Run the following command in your terminal.
   ```sh
   flask run
   ```

5. Type "localhost:5000" into your browser's URL bar and press enter.

# What it does
Users are given a daily challenge: they must go outside, take a picture of something in nature that fits a specific category, and then upload it to the app. If the item in the image falls into the correct category, then the user will get points that they can use to purchase a prize later.

# How we built it
We used Flask to create a basic web app, so we used Python and SQLAlchemy for the backend and HTML and CSS for the frontend.

We also used Google Cloud's Vision API in order to identify which categories images fell into.

# What we learned
We learned how to work quickly with Flask, as one of our members had not used it before. We also learned how to use Google Cloud's Vision API.
