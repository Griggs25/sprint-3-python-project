# a) Iterate and print games with global sales > 25 million
for game in video_game_sales:
    if game[GLOBAL_SALES] > 25.0:
        print(f"Name: {game[NAME]}, Global Sales: {game[GLOBAL_SALES]}M")

# b) Count games released before the year 2000
pre_2000_count = 0
for game in video_game_sales:
    if game[YEAR] < 2000:
        pre_2000_count += 1
print(f"Number of games released before 2000: {pre_2000_count}")

# c) Calculate and compare total sales between North America and Japan
total_na_sales = 0
total_jp_sales = 0

for game in video_game_sales:
    total_na_sales += game[NA_SALES]
    total_jp_sales += game[JP_SALES]

print(f"Total North America Sales: {total_na_sales:.2f}M")
print(f"Total Japan Sales: {total_jp_sales:.2f}M")

if total_na_sales > total_jp_sales:
    print("North America had higher sales.")
elif total_jp_sales > total_na_sales:
    print("Japan had higher sales.")
else:
    print("Both regions had equal sales.")

# d) Create a list of games published by 'Nintendo'
nintendo_games = []
for game in video_game_sales:
    if game[PUBLISHER] == 'Nintendo':
        nintendo_games.append(game[NAME])

print(f"Nintendo Games: {nintendo_games}")
print(f"Total Nintendo games: {len(nintendo_games)}")