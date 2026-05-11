#a) Total Sales NA, EU, JP function
def calculate_total_sales(game):
    return game[6] + game[7] + game[8]
result=calculate_total_sales(video_game_sales[0])
print(result)

#b Filter by Genre Function
def filter_by_genre(data, genre='Platform'):
    result = []
    for game in data:
        if game[GENRE] == genre:
            result.append(game)
    return result

filtered_game = filter_by_genre(video_game_sales, 'Sports')
print(filtered_game)

#c) Game Summary Function
def get_summary(game):
    return f"{game[NAME]} ({game[YEAR]}) - {game[GENRE]} - ${game[GLOBAL_SALES]}M"

for game in video_game_sales:
    summary= get_summary(game)
    print(summary)
