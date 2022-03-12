# Youtube Transcript Downloader

This is a package for retrieving transcripts from youtube

Developer by Edvinas Adomaitis (c) 2021

## Example of usage

replace placeholder [] with the desired youtube url
```
import youtube_transcript_downloader

url = "[your desired url]"
transcript = youtube_transcript_downloader.get_transcript(url)
```
the function returns a dictionary of { time : text }

printing out the transcript
```
for key, val in transcript.items():
        print(f"{key} : {val}")
```
output:
```
00:05 : text text text
00:10 : text text text
00:15 : text text text
00:20 : text text text
...
```