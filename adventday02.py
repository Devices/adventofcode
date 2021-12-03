import pandas as pd

#movement = open("Input/day2input.txt", "r")

movement = pd.read_csv("Input/day2input.txt", header=None)
movement[['Direction', 'Amount']] = movement[0].str.split(" ", expand=True)
movement = movement[['Direction', 'Amount']]
movement['Amount'] = movement['Amount'].astype(int)

forward = movement[movement['Direction'].str.contains("forward")]
tot_forward = forward['Amount'].sum()
up = movement[movement['Direction'].str.contains("up")]
down = movement[movement['Direction'].str.contains("down")]
horizontal = abs(up['Amount'].sum() - down['Amount'].sum())
print('Answer to 2a: ',horizontal*tot_forward)