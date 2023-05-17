from src.channel import Channel


class TestChannel:
    def test_print_info(self, capsys):
        channel = Channel('UC_x5XG1OV2P6uZZ5FSM9Ttw')
        channel.print_info()
        captured = capsys.readouterr()
        assert captured.out.startswith('{\n  "kind": "youtube#channelListResponse",\n  "etag":')
