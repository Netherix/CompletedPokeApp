class BattleGame:
    def __init__(self, player1_team, player2_team):
        self.player1_team = player1_team
        self.player2_team = player2_team

    def calculate_winner(self):
        player1_stats = self.calculate_team_stats(self.player1_team)
        player2_stats = self.calculate_team_stats(self.player2_team)

        if player1_stats > player2_stats:
            return self.player1_team[0].author.id
        elif player1_stats < player2_stats:
            return self.player2_team[0].author.id
        else:
            return None
        
    def calculate_team_stats(self, team):
        total_stats = 0

        for pokemon in team:
            total_stats += pokemon.attack + pokemon.defense + pokemon.hp

        return total_stats


