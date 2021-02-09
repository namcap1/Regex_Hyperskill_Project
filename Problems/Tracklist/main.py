def tracklist(**music):
    for artist, dict_values in music.items():
        print(artist)
        for album, song in dict_values.items():
            print("ALBUM:", album, "TRACK:", song)

