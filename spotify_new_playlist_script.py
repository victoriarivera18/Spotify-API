# terminal version
import json
import urllib3
import requests

# from secrets.py (for securtity reasons)
from secrets import spotify_user_id, spotify_token


# 1. write in list of playlists into text file
# 2. get searching information (artist and playlist name)
# 3. Check if info is valid -> yes - create new playlist with songs from given playlist by artist
#                              no - end program
# 4. after successful creation ask user if they want to add more songs to new playlist
# 5. end program when answer is no or  invalid information entered

# Make sure to fill in your spotify client_secret information

def get_playlists(): # prints out list of users public and non-collaborative playlists
    query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_user_id) # using secrets information
    response = requests.get(query, data=None, headers={ # from api documentation
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(spotify_token)
    })

    response_json = response.json()
    titles_list = []
    name_new = "Rosalia"
    y = 0

    # print(response_json["total"]) # total playlist count
    print("List of your playlist:: ")
    while y < response_json["total"]:
        try:
            if response_json["items"][y]["collaborative"] == False and response_json["items"][y]["public"] == True:  # get only your own public playlist
                print(response_json["items"][y]["name"])
        except IndexError:
            print()
        y = y + 1


def get_info():
    artist = input("Enter name of the artist you want to search for:: ")
    curr_playlist = input("Enter which playlist you want to search songs by artist:: ")

    info_tuple = (artist.lower(), curr_playlist.lower()) # make information all lowercase
    return info_tuple

# def make_new_playlist():
# def get_artist_songs():

def main():
    get_playlists()
    my_info = get_info()

main()