#a)Pokemon name Extract
game_name = video_game_sales[4][NAME]
print(game_name[:7])

#b) Cleaned messy names
messy_names = ['  Wii Sports  ', 'TETRIS', '  mario kart WII']
for name in messy_names:
    print(name.strip().lower())

#c)print a formatted summary of the #1 game in the format
game = video_game_sales[0]
print(f"#1 Best Seller: {game[NAME]} ({game[YEAR]}) - ${game[GLOBAL_SALES]}M global sales")
