import requests, os, json, streamlit as st
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image

load_dotenv()

API_KEY = os.getenv('TMDB_API_KEY')
SEARCH_URL = 'https://api.themoviedb.org/3/search/movie'


def fetch_movie_data(url, name):
    params = {
        'api_key': API_KEY,
        'query': name
    }
    
    response = requests.get(url, params=params)
    
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        
        return {"error": f"Failed to fetch data: {response.status_code}"}
    
def display_movie_card(movie):
    poster_url = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
    response = requests.get(poster_url)
    try:
        img = Image.open(BytesIO(response.content))
    except:
        response = requests.get("https://via.placeholder.com/150")
        img = Image.open(BytesIO(response.content))

    st.image(img, width=150)
    st.subheader(movie['title'])
    st.text(f"Release Date: {movie['release_date']}")
    st.text(f"Rating: {movie['vote_average']}")
    st.write(f"Overview: {movie['overview']}")

    # print(movie['title'])
    # print(f"Release Date: {movie['release_date']}")
    # print(f"Rating: {movie['vote_average']}")
    # print(f"Overview: {movie['overview']}")

    # print("\n=======================================================================================================\n")

if __name__ == "__main__":
    st.title("TMDB Movie Information")
    movie_name = st.text_input("Enter Movie Name", "Harry Potter") 
          
    if st.button("Search"):  
        movie_data = fetch_movie_data(SEARCH_URL, movie_name)
        
        if "error" in movie_data:
            st.error(movie_data["error"])
        else:
            for movie in movie_data['results']:
                with st.container():
                    display_movie_card(movie)
                    st.markdown("---")
            with open("data.json", "w") as f:
                json.dump(movie_data, f, indent=4)
            # st.success("Data written to data.json")

