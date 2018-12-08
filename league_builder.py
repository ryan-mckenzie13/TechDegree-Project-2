#Project #2 Build a Soccer League, trying to exceed expectations!

import csv

if __name__ == "__main__":
    
    exp_players=[]
    reg_players=[]
    
    #opens the soccer_players.csv
    with open('soccer_players.csv', newline='') as csvfile:
        file_reader = csv.DictReader(csvfile, delimiter=',')
        players= list(file_reader)
    
    #creates the exp_player and reg_player lists.  
    for player in players:
            if player['Soccer Experience'] =='YES':
                exp_players.append(player)
            if player['Soccer Experience'] =='NO':
                reg_players.append(player)
    
    #divides teams up with exp and non exp players, puts them into lists
    sharks=exp_players[:3] + reg_players[:3]
    dragons=exp_players[3:6] + reg_players[3:6] 
    raptors=exp_players[6:] + reg_players[6:]
    
    #dicitionary with team being the key and roster being the value
    teams={'SHARKS':sharks,'DRAGONS':dragons,'RAPTORS':raptors}
    
    #Writing txt file with Teams
    file = open('teams.txt', 'a')
    # loop through the teams
    for team, roster in teams.items():
        # Write's the team name on own line
        file.write(team + "\n")
        # loop through players and write player info
        for player in roster:
            player_name = player['Name']
            exp_level = player['Soccer Experience']
            guardians = player['Guardian Name(s)']
            file.write("{}, {}, {}\n".format(player_name, exp_level, guardians))
        file.write("\n")
        
    #Date and Time of first practice for all teams
    
    date = "Monday December 3rd"
    time = "5pm"
    
    #Writing Welcome Letter to each Guardian(s)
    for team, roster in teams.items():
        for player in roster:
            player_name=player['Name']
            exp_level = player['Soccer Experience']
            guardians = player['Guardian Name(s)']
            #changes player names to lowercase with undercore in between
            welcome_letter=player_name.lower()
            welcome_letter=welcome_letter.replace(" ","_")
            file=open('{}.txt'.format(welcome_letter),'w')
            file.write("Dear {},\n" 
                       "Congratulations! {} is on the {}!\n"
                       "The first practice will be on {} at {}!\n"
                       "We look forward to seeing you there.\n" 
                       "Thanks,\n" 
                       "Coach Ryan".format(guardians,player_name, team, date, time))

    