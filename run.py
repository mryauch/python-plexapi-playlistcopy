#!/usr/bin/python

import argparse
import logging
import sys
from plexapi.server import PlexServer
from plexapi.playlist import Playlist

logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger(__name__)

def parse_args():
  parser = argparse.ArgumentParser(description='PlexAPI Playlist Copier')
  parser.add_argument('src_token', type=str,
                      help='Plex auth token for user with existing playlist.')
  parser.add_argument('dst_token', type=str,
                      help='Plex auth token for user that will receive the playlist.')
  parser.add_argument('baseurl', type=str,
                      help='Plex server base URL.')
  parser.add_argument('playlist', type=str,
                      help='Playlist to copy.')
  parser.add_argument('-v', '--verbose', action='count')
  args = parser.parse_args()
  if not (args.src_token and args.dst_token and args.baseurl and args.playlist):
    parser.error('Missing argument. All arguments are required.')
  return args

def main():
  args = parse_args()

  src_token = args.src_token
  dst_token = args.dst_token
  baseurl = args.baseurl
  playlist = args.playlist
    
  src_plex = PlexServer(baseurl, src_token)
  dst_plex = PlexServer(baseurl, dst_token)

  for src_playlist in src_plex.playlists():
    print(src_playlist.title)
    if src_playlist.title == playlist:
      print(f"Copying playlist {playlist}...")
      src_playlist.create(server=dst_plex, title=playlist, items=src_playlist.items())
      print("Done!")
      
  if not args.verbose:
    loglevel = logging.WARNING
  if args.verbose == 1:
    loglevel = logging.INFO
  if args.verbose == 2:
    loglevel = logging.DEBUG
  

if __name__ == "__main__":
  main()