# python-plexapi-playlistcopy

This is a quick hack to copy a playlist from one user to another. Even works with Managed Users.

# Usage Example

```
docker build -t plex_playlistcopy .

docker run plex_playlistcopy <SOURCE_USER_AUTH_TOKEN> <DEST_USER_AUTH_TOKEN> <http://plex_server_ip:32400> <PLAYLIST_NAME>
``````