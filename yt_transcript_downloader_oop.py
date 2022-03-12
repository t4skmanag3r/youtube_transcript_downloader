import requests as req
import json
import re
from typing import Dict, Optional, Tuple, Any


class YoutubeTranscriptDownloader:
    def __init__(self, url) -> None:
        self.url = url

    def _get_serialized_share_entity(self) -> Optional[str]:
        try:
            data = req.get(self.url)
        except Exception as e:
            raise e
        if data.status_code != 200:
            data.raise_for_status()

        search = re.search('"serializedShareEntity":"[A-Za-z0-9%]*"', str(data.content))
        if not search:
            return None
        param = (
            str(data.content)[search.start() : search.end()].split(":")[1].strip('"')
        )
        return param

    def _get_innertube_api_key(self) -> Optional[str]:
        try:
            data = req.get(self.url)
        except Exception as e:
            raise e
        if data.status_code != 200:
            data.raise_for_status()

        search = re.search('"innertubeApiKey":"[A-Za-z0-9_]*"', str(data.content))
        if not search:
            return None
        key = str(data.content)[search.start() : search.end()].split(":")[1].strip('"')
        return key

    def _get_transcript_json(self, param: str, key: str) -> Optional[Dict[Any, Any]]:
        PAYLOAD = {
            "context": {
                "client": {
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.70,gzip(gfe)",
                    "clientName": "WEB",
                    "clientVersion": "2.20220309.01.00",
                }
            },
            "params": f"{param}",
        }
        transcript_url = f"https://www.youtube.com/youtubei/v1/get_transcript?key={key}&prettyPrint=false"
        try:
            data = req.post(transcript_url, json=PAYLOAD)
        except Exception as e:
            raise e
        if data.status_code != 200:
            data.raise_for_status()

        if not data.content:
            return None

        data = json.loads(data.content)
        return data

    def __navigate_to_cuegroups(self, json: dict) -> Dict[Any, Any]:
        return json["actions"][0]["updateEngagementPanelAction"]["content"][
            "transcriptRenderer"
        ]["body"]["transcriptBodyRenderer"]["cueGroups"]

    def _parse_cuegroup(self, cue_group: dict) -> Tuple[str, str]:
        time = cue_group["transcriptCueGroupRenderer"]["formattedStartOffset"][
            "simpleText"
        ]
        text = cue_group["transcriptCueGroupRenderer"]["cues"][0][
            "transcriptCueRenderer"
        ]["cue"]["simpleText"]
        return time, text

    def _parse_transcript_json(self, json: dict):
        json = self.__navigate_to_cuegroups(json)

        transcript = {}
        for cue_group in json:
            time, text = self._parse_cuegroup(cue_group)
            transcript[time] = text
        return transcript

    def get_transcript(self) -> Optional[Dict[str, str]]:
        param = self._get_serialized_share_entity()
        key = self._get_innertube_api_key()
        if not param or not key:
            return None

        transcript_json = self._get_transcript_json(param, key)
        if not transcript_json:
            return None
        transcript = self._parse_transcript_json(transcript_json)
        return transcript


def get_transcript(url):
    downloader = YoutubeTranscriptDownloader(url)
    return downloader.get_transcript()


def main():
    url = "https://www.youtube.com/watch?v=Wo5dMEP_BbI"
    transcript = get_transcript(url)
    if not transcript:
        return

    for key, val in transcript.items():
        print(f"{key} : {val}")


if __name__ == "__main__":
    main()
