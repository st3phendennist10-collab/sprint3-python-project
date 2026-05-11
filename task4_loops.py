# a)Games with over 25M global sales
for game in video_game_sales:
    if game[GLOBAL_SALES]>25:
        print(game[NAME],game[GLOBAL_SALES])

#b) Loop that counts games released before 2000
pre_2000_count=0
for game in video_game_sales:
    if game[YEAR]<2000:
        pre_2000_count=pre_2000_count+1

print(pre_2000_count)

#c) Loop that calculates NA sales and JP sales across games
total_na=0
total_jp=0
for game in video_game_sales:
    total_na = total_na + game[NA_SALES]
    total_jp = total_jp + game[JP_SALES]

print(f"Total NA sales: {total_na}")
print(f"Total JP sales: {total_jp}")
if total_na > total_jp:
    print('North America has higher sales')
elif total_jp > total_na:
    print('Japan had higher sales')
else:
    print("Both regions had equal sales")

#d) New list containing only Nintendo Titles
nintendo_games=[]
for game in video_game_sales:
    if game[PUBLISHER] == 'Nintendo':
        nintendo_games.append(game[NAME])

print(nintendo_games) 
print(len(nintendo_games))   
