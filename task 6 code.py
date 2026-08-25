# a) Function to calculate the sum of regional sales for a single game row
def calculate_total_sales(game):
    return game[NA_SALES] + game[EU_SALES] + game[JP_SALES]

# Test calculate_total_sales on the first game
first_game_regional_sum = calculate_total_sales(video_game_sales[0])
print(f"Regional sales sum for {video_game_sales[0][NAME]}: {first_game_regional_sum:.2f}M")


# b) Function to filter the dataset by genre with a default value of 'Platform'
def filter_by_genre(data, genre='Platform'):
    filtered_games = []
    for game in data:
        if game[GENRE] == genre:
            filtered_games.append(game)
    return filtered_games

# Test filter_by_genre without specifying a genre (uses default 'Platform')
default_filtered = filter_by_genre(video_game_sales)
print(f"\nPlatform games found (default parameter): {len(default_filtered)}")

# Test filter_by_genre with an explicit genre specification
sports_filtered = filter_by_genre(video_game_sales, 'Sports')
print(f"Sports games found (explicit parameter): {len(sports_filtered)}")


# c) Function to return a formatted game summary string
def get_summary(game):
    return f"{game[NAME]} ({game[YEAR]}) - {game[GENRE]} - ${game[GLOBAL_SALES]}M"

# Loop through the full dataset to print summaries of all 20 games
print("\n--- Dataset Summary List ---")
for game in video_game_sales:
    print(get_summary(game))