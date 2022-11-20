import os
import re

list_path = os.listdir()
list_srt = []
list_movie = []
for path in list_path:
    if path.endswith('.srt'):
        list_srt.append(path)
    elif path.endswith(('.mkv', '.mp4')):
        list_movie.append(path)

list_srt.sort()
list_movie.sort()

print('sous-titre: ' + str(list_srt))
print('movies :' + str(list_movie))
i = 0
if len(list_movie) <= 1:
    os.rename(list_srt[0], '{}.srt'.format(list_movie[0][:-4]))
else:
    for srt in list_srt:
        os.rename(srt, '{}.srt'.format(list_movie[i][:-4]))
        i += 1
