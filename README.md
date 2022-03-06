# touch-grass
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

4. Set the environment variable for your Google Cloud Credentials as the path to the json file with said credentials. You must use your own path to the required json.
   ```sh
   export GOOGLE_APPLICATION_CREDENTIALS=C:\Users\yourUser\credentials-file.json
   ```

5. Run the following commands in your terminal.
   ```sh
   export FLASK_ENV=‘development’
   flask run
   ```

6. Type "localhost:5000" into your browser's URL bar and press enter.
