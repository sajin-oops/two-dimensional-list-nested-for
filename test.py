groceories = [["apple","mango","orange"],["carrot","potato","onion"]
              ,["fish","chicken","beaf"]]

print(groceories)

#O/P -[['apple', 'mango', 'orange'], ['carrot', 'potato', 'onion'], ['fish', 'chicken', 'beaf']]

for collection in groceories:
    for food in collection:
        print(food, end =" ")
    print()
        
'''
O/P
apple mango orange
carrot potato onion
fish chicken beaf
 
'''