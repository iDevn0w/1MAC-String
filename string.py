import random
import time

gift = [
   ["omra","haj","Quran"], #Dead man or woman(:
   ["PS4","disnyland","a kiss"], #kid
   ["a Car","going to Party","travle to sudan"],#young
   ["a perfume","make up","iphone XIIIXX","Samsung Galaxy S 1000"] #female
]
film = [
   ["old 1988", "The Messenger", "Gil"],
   ["spiderman", "batman", "spongbob"],
   ["Interstaller","Harry potter","Transformer","romero & juleit"]
]
rest = [
   ["old man coffe shop", "Tea xana", "1935 Resturant"],
   ["Disny Kid Resturant","park Resturant","Bazzar Resturant"],
   ["Macdonald's","mir a min in Dubia","shilton house Resturant"]
]

new_recomandtion = []
new_note = []
def age(old):
        if old < 16:
            print("you are just kid!")
        elif old <= 40:
            print("you are Young Man (:")
        elif old > 40:
            print("Oh, the Death near you! :( Pray to Allah") #hhhhh
            ########################################################
            # Gender                                               #
            ########################################################
        gen = input("what is you Gender for male enter M for Female enter F: ")
        gen1 = ("F", "M")
        while gen.upper() not in gen1:
            raw = input("Please Enter M for male, F for Female: ")
            if raw.upper() in gen1:
                print("ok! got it")
                break
            else:
                print("thank you!")
            ######################################################
            # Recommend                                          #
            ######################################################
        reco = input("""
        What would you like to recommend?
     
         1- A gift
         2- Restaurant
         3- Film

        Please Make a seletion : """)
        if reco == "1":
            if gen.upper() == "F":
                if old >= 16 and old <= 40:
                    print(random.choice(gift[3]))
                elif old > 40:
                    print(random.choice(gift[0]))
                elif old < 16:
                    print(random.choice(gift[1]))
            elif gen.upper() == "M":
                if old >= 16 and old <= 40:
                    print(random.choice(gift[2]))
                elif old > 40:
                    print(random.choice(gift[0]))
                elif old < 16:
                    print(random.choice(gift[1]))
        elif reco == "2":
            if old < 16:
                print(random.choice(rest[1]))
            elif old <= 40 or old >= 16:
                print(random.choice(rest[2]))
            elif old > 40:
                print(random.choice(rest[0]))
        elif reco == "3":
            if old < 16:
                print(random.choice(film[1]))
            elif old <= 40 or old >= 16:
                print(random.choice(film[2]))
            elif old > 40:
                print(random.choice(film[0]))
        else:
                time.sleep(1)
                print("Stupid. Not worth the program 😎\n What wrong with you man Run agian!")
                pass
            ######################################################
            #Recommandtions                                      #
            ######################################################
        cc = str(input("Would you like you add more recommendations? Enter y/n: "))
        if cc.lower() == "y":
            extra_info = input("Did you like add Specification?. yes/no: ")
            if extra_info.lower() == "yes":
                note = input("For Gender enter M or F or press C:  ") # we have Alien Too. Becuase of that You can Input X for Gender *_*
                note1 = input("Enter age or press C: ")
                if note.upper() == "M" or note.upper() == "F":
                    print("ok!")
                elif note.upper() == "C" or note1.upper() == "C":
                    pass
                out = int(input("how many recommendation to add : "))
                for i in range(out):
                    out1 = str(input("Enter Your Recommendation Please: "))
                    new_recomandtion.append(out1)
                    print(f'New List is added Now {new_recomandtion} for Gender {note} and age {note1}')
            elif extra_info.lower() == "no":
                pass
            print("Thank you for recommendation!, We respect your recommend! THANK YOU ")
        elif cc.lower() == "n":
            time.sleep(0.5)
            print("Enjoy!")

        

age(int(input("How Old are you: ")))

