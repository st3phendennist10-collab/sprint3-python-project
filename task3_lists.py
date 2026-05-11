#a) Game names extraction
game_names=[]
for game in video_game_sales:
    game_names.append(game[NAME])
print(game_names)

#b) Append new game entry
video_game_sales.append([21, 'Animal Crossing: New Horizons', 'NS', 2020, 'Simulation', 'Nintendo', 7.45, 5.21, 7.37, 31.18])
print(len(video_game_sales))

#c) Create Tuple
dataset_info=(21,10,'Video Game Sales')
print(dataset_info)
#A tuple is useful for immutable data; data that shouldn't change. Data that will be referenced throughout.
