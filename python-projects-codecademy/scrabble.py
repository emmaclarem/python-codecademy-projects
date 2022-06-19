#Objective: In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
#updating lists to include lowercase letters
letters += [letter.lower() for letter in letters]
points += points

#making ordered pairs of letter values
letters_to_points = {key: value for key, value in zip(letters, points)}
letters_to_points[" "] = 0

#word scoring function
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letters_to_points.get(letter, 0)
  return point_total
  
#words played by each player
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

#empty dictionary for keeping players' scores
player_to_points = {}
#scoring each player's words and adding to the dictionary of total points 
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points

#function to take player and word and add it to the list of words they've played
def play_word(player, word):
  player_to_words[player].append(word)
  update_point_totals()

play_word("player1", "Code")
print(player_to_points)


