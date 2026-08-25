# a) Create a list of all game names using a loop
game_names = []
for game in video_game_sales:
    game_names.append(game[NAME])
print(game_names)

# b) Append the new game to the dataset and print the updated length
new_game = [21, 'Animal Crossing: New Horizons', 'NS', 2020, 'Simulation', 'Nintendo', 7.45, 5.21, 7.37, 31.18]
video_game_sales.append(new_game)
print(len(video_game_sales))

# c) Create a tuple for metadata and explain its choice
dataset_info = (len(video_game_sales), 10, 'Video Game Sales')
print(dataset_info)