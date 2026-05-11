#a) Total Number of games in data set
total_games=len(video_game_sales)
print(f"Total Games:{total_games}")

#b) Average Global Sales
total_sales = 0
for game in video_game_sales:
    total_sales = total_sales + game[GLOBAL_SALES]

avg_global_sales = total_sales / total_games
print(f"Average Global Sales: {avg_global_sales}")

#c) Game share Wii Sports
top_game_share = (video_game_sales[0][GLOBAL_SALES] / total_sales) * 100
print(f"Top Game Share:{top_game_share}")
