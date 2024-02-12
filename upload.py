import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Your credentials file (downloaded from the Google Cloud Console)
credentials_file = "yt-creds.json"

# YouTube Data API version
api_version = 'v3'

# Set up the OAuth2 flow for user authorization
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    credentials_file, ['https://www.googleapis.com/auth/youtube.upload'])
credentials = flow.run_local_server()

# Create a YouTube Data API client
youtube = build('youtube', api_version, credentials=credentials)

# Define the video metadata
request_body = {
    'snippet': {
        'title': 'Your Video Title',
        'description': 'Your Video Description',
        'tags': ['tag1', 'tag2'],
        'categoryId': '22',  # Category ID for entertainment
    },
    'status': {
        'privacyStatus': 'private',  # Set to 'public' for public videos
    },
}

# Upload the video
media = MediaFileUpload(video_file, chunksize=-1, resumable=True)
request = youtube.videos().insert(
    part=','.join(request_body.keys()),
    body=request_body,
    media_body=media
)
response = None
while response is None:
    status, response = request.next_chunk()
    if status:
        print(f'Uploaded {int(status.progress() * 100)}%')

print(f'Video uploaded! Video ID: {response["id"]}')

