import unittest
import sys

sys.path.append("./")
import yt_transcript_downloader


class TestYtTranscriptsDowloader(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "https://www.youtube.com/watch?v=Wo5dMEP_BbI"

    def test__get_serialized_share_entity(self) -> None:
        param = yt_transcript_downloader._get_serialized_share_entity(self.url)
        self.assertIsNotNone(param)

    def test__get_innertube_api_key(self) -> None:
        key = yt_transcript_downloader._get_innertube_api_key(self.url)
        self.assertIsNotNone(key)

    def test_get_transcipt_wdata(self) -> None:
        param = yt_transcript_downloader._get_serialized_share_entity(self.url)
        key = yt_transcript_downloader._get_innertube_api_key(self.url)
        data = None
        if param and key:
            data = yt_transcript_downloader._get_transcript_json(param, key)
        self.assertIsNotNone(data)

    def test_get_transcript(self) -> None:
        self.assertIsNotNone(yt_transcript_downloader.get_transcript(self.url))


def main():
    unittest.main()


if __name__ == "__main__":
    main()
