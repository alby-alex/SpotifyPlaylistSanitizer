import tekore as tk

conf = tk.config_from_file('tekore.cfg', return_refresh=True)
user_token = tk.refresh_user_token(*conf[:2], conf[3])

spotify = tk.Spotify(user_token)



playlist = spotify.playlist("4TEfGWKFu6u9b7pwZNd2oM")

new_playlist = spotify.playlist_create(spotify.current_user().id, "{} (clean)".format(playlist.name)).id

for i in playlist.tracks.items:
    if not i.track.explicit:
        spotify.playlist_add(new_playlist, [i.track.uri])
    # print(i.track)
