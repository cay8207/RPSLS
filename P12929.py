from RPSLS_player import RPSLS_player

class P12929(RPSLS_player):
  def __init__(self):
    self.last_shot = "paper"
    self.last_result = "win"

  def shoot(self):
    if self.last_result == "win":
      return self.last_shot

    else:
      if self.last_shot == "scissors":
        return "spock"
      elif self.last_shot == "spock":
        return "lizard"
      elif self.last_shot == "lizard":
        return "rock"
      elif self.last_shot == "rock":
        return "paper"
      else:
        return "scissors"

  def update(self, result: str, competitor_shot: str):
    self.last_shot = competitor_shot
    self.last_result = result