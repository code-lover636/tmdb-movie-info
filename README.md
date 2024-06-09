# TMDB Movie Information

This is a Streamlit application that fetches and displays information about movies from The Movie Database (TMDB). Users can search for movies by name and view details such as the movie poster, release date, rating, and overview.

## Features

- Search for movies by name
- Display movie poster, release date, rating, and overview
- Save search results to a JSON file

## Installation

Follow these steps to install and run the application:

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/code-lover636/tmdb-movie-info.git
    cd tmdb-movie-info
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your TMDB API key:**

    - Create a `.env` file in the project directory.
    - Add your TMDB API key to the `.env` file:

    ```env
    TMDB_API_KEY=your_tmdb_api_key_here
    ```

## Usage

1. **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

2. **Open your web browser**

3. **Enter the name of a movie in the input box and click "Search".**

    The application will display the movie poster, release date, rating, and overview for the searched movie.

## Example

To search for "Harry Potter" movies:

1. Enter "Harry Potter" in the search box.
2. Click the "Search" button.
3. The application will display a list of Harry Potter movies with their details.

## License

This project is licensed under the MIT License.
