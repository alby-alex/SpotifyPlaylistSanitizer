import tekore as tk

conf = tk.config_from_file('tekore.cfg', return_refresh=True)
user_token = tk.refresh_user_token(*conf[:2], conf[3])

spotify = tk.Spotify(user_token)



playlist = spotify.playlist("4TEfGWKFu6u9b7pwZNd2oM")



to_add_uris = []

#     for i in playlist.tracks.items:
#         if not i.track.explicit:
#             to_add_uris.append(i.track.uri)
#         else:
#             compare_artist = set()
#             for j in i.track.artists:
#                 compare_artist.add(j.name)
#             result = spotify.search("track:{}".format(i.track.name), types=['track'], limit = 20)
#             success = False
#             for j in result[0].items:
#                 if not j.explicit:
#                     temp = set()
#                     for k in j.artists:
#                         temp.add(k.name)
#                     if temp == compare_artist:
#                         # print("inital version: {} found version: {}".format(i.track.name, j.name))
#                         success = True
#                         break
#             if not success:
#                 print("Failed: {}".format(i.track.name))



# # result = spotify.search("track:No Brainer", types=['track'], limit = 5)
# # for i in result[0].items:
# #     print(i)
# new_playlist = spotify.playlist_create(spotify.current_user().id, "{} (clean)".format(playlist.name)).id

# spotify.playlist_add(new_playlist, to_add_uris)