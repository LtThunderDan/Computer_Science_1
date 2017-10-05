print("Trip to the Amazon")
print("You and a group of tourists are taking a trip through the Amazon")
print("While trucking along your tire pops")
print("There is no spare tire!")
print("Your job is to survive")
choice = input("Do you STAY or LEAVE the bus: ")
if choice == "STAY":
    print("You stayed!")
    choice = input("Should you SCAVANGE for supplies, set up a \
CAMP,or WANDER: ")
# has three or more decisions
    if choice == "SCAVANGE":
        print("You find wood and return to the bus")
        wood = input("How much wood do you pick up? ")
        wood = int(wood)
        if wood > 10:
            print("The group thanks you.")
            print("The fire signals a chopper to pick you up!")
            print("THE END")
        elif wood > 5:
            print("The group pats you on the back.")
            print("The fire keeps you warm till help comes.")
            print("Everyone developed hypothermia.")
            print("THE END")
        else:
            print("The group uses you as firewood.")
            print("THE END")
# 3 possible consequences
# numeric comparison
    elif choice == "CAMP":
        print("You successfully set up a tent and start a fire")
        print("While sleeping the tent sets on fire and kills you.")
        print("THE END")
    elif choice == "WANDER":
        print("You wander into the woods and get killed by a venus fly trap")
        print("THE END!")
    else:
        print("Error, does not compute.")
elif choice == "LEAVE":
    print("You and a group of people look for help")
    print("You end up finding an Amazonian tribe!!")
    choice = input("Do you CONTINUE into the village or PASS the village by: ")
    if choice == "CONTINUE":
        print("The tribe is cannibalistic and you are roasted and eaten")
        print("THE END!")
    elif choice == "PASS":
        print("You stumble accross the town of Iquitos, Peru")
        choice = input("Do you TELL them about the others or \
get on a PLANE and leave: ")
        if choice == "TELL":
            print("They help and successfully retrieve the lost members")
            print("THE END!")
        elif choice == "PLANE":
            print("The decision haunts you and drives you insane")
            print("You die years late in an insane asylum")
            print("THE END")
        else:
            print("Error, does not compute.")
    else:
        print("You become a cannibal yourself!")
else:
    print("You can't even get the first question right")
    print("You die")
# all have atleast two decision points
