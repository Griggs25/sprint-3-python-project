# a) Calculate total global sales by genre using a dictionary
sales_by_genre = {}
for game in video_game_sales:
    genre = game[GENRE]
    global_sales = game[GLOBAL_SALES]
    if genre in sales_by_genre:
        sales_by_genre[genre] += global_sales
    else:
        sales_by_genre[genre] = global_sales
print(sales_by_genre)

# b) Count the number of games per publisher using a dictionary
games_per_publisher = {}
for game in video_game_sales:
    publisher = game[PUBLISHER]
    if publisher in games_per_publisher:
        games_per_publisher[publisher] += 1
    else:
        games_per_publisher[publisher] = 1
print(games_per_publisher)

# c) Create a dictionary for the #1 game and print its items using a loop
top_game_row = video_game_sales[0]  # #1 ranked game at index 0
top_game = {
    'name': top_game_row[NAME],
    'year': top_game_row[YEAR],
    'genre': top_game_row[GENRE],
    'publisher': top_game_row[PUBLISHER],
    'global_sales': top_game_row[GLOBAL_SALES]
}

for key, value in top_game.items():
    print(f"{key}: {value}")