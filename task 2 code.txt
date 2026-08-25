# a) Extract the name of the 5th game and slice out just the word "Pokemon"
game_name = video_game_sales[4][NAME]
pokemon_word = game_name[:7]
print(pokemon_word)

# b) Clean the messy names by stripping whitespace and converting to lowercase
for name in messy_names:
    cleaned_name = name.strip().lower()
    print(cleaned_name)

# c) Use an f-string to print a formatted summary of the #1 game
best_seller = video_game_sales[0]
summary = f"#{best_seller[RANK]} Best Seller: {best_seller[NAME]} ({best_seller[YEAR]}) - ${best_seller[GLOBAL_SALES]}M global sales"
print(summary)