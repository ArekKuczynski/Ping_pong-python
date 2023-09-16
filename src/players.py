import data

class Players():
    def __init__(self) -> None:
        self.data = data.Data()
        self.player_1 = "0"
        self.player_2 = "0"

        self.data.fonts()
        self.build_players()

    def build_players(self) -> None:
        self.player_1_surface = self.data.font_logo.render(self.player_1, True, "White")
        self.player_2_surface = self.data.font_logo.render(self.player_2, True, "White")

    def player_1_point(self) -> None:
        self.player_1 = str(int(self.player_1) + 1)
        self.build_players()

    def player_2_point(self) -> None:
        self.player_2 = str(int(self.player_2) + 1)
        self.build_players()

    def players_reset(self) -> None:
        self.player_1 = "0"
        self.player_2 = "0"
        self.build_players()
