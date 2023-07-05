def roll_call_dwarves(dwarves=["Doc", "Dopey", "Bashful", "Grumpy"]):
    for i, name in enumerate(dwarves, start=1):
        print(f'{i}. {name}')


def summon_captain_planet(planeteer_calls=["earth", "wind", "fire", "water", "heart"]):
    return [f'{name.title()}!' for name in planeteer_calls]


def long_planeteer_calls(assorted_words=["axe", "earth", "wind", "fire"]):
    # for word in assorted_words:
    #     if(len(word) >= 4):
    #         return True
    # return False
    return any(len(word) > 4 for word in assorted_words)


def find_the_cheese(lst = ["crackers", "gouda", "thyme"] ):
    cheeses = ['gouda', 'cheddar', 'camembert' ]
    
    for food in lst:
        if food in cheeses: 
            return food 
    return None 
    


    