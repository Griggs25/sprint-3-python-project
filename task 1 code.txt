# a) Store the total number of games in the dataset
total_games = len(video_game_sales)
print(f"Total number of games in the dataset: {total_games}")

# b) Calculate the average global sales across all 20 games
total_global_sales = sum(game[GLOBAL_SALES] for game in video_game_sales)
avg_global_sales = total_global_sales / total_games
print(f"The average global sales across all games is: {avg_global_sales:.2f} million units")

# c) Calculate the percentage of total global sales represented by Wii Sports
wii_sports_sales = video_game_sales[0][GLOBAL_SALES]
top_game_share = (wii_sports_sales / total_global_sales) * 100
print(f"Wii Sports accounts for {top_game_share:.2f}% of the total global sales in this dataset.")