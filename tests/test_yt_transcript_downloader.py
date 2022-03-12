import unittest
import sys

sys.path.append("./")
from youtube_transcript_downloader.yt_transcript_downloader import (
    YoutubeTranscriptDownloader,
    get_transcript,
)


class Test_YoutubeTranscriptDownloader(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "https://www.youtube.com/watch?v=Wo5dMEP_BbI"
        self.downloader = YoutubeTranscriptDownloader(self.url)

    def test__get_serialized_share_entity(self) -> None:
        param = self.downloader._get_serialized_share_entity()
        self.assertIsNotNone(param)

    def test__get_innertube_api_key(self) -> None:
        key = self.downloader._get_innertube_api_key()
        self.assertIsNotNone(key)

    def test_get_transcipt_wdata(self) -> None:
        param = self.downloader._get_serialized_share_entity()
        key = self.downloader._get_innertube_api_key()
        data = None
        if param and key:
            data = self.downloader._get_transcript_json(param, key)
        self.assertIsNotNone(data)

    def test_get_transcript(self) -> None:
        self.assertIsNotNone(self.downloader.get_transcript())


class Test_get_transcript(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "https://www.youtube.com/watch?v=Wo5dMEP_BbI"

    def test_get_transcript(self):
        self.assertIsNotNone(get_transcript(self.url))


def main():
    unittest.main()


if __name__ == "__main__":
    main()
