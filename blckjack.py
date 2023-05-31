import random
logo="""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
#main game function
def blackjack():
   print(logo)
   def deal_card():
     cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
     return random.choice(cards)
 #random drawing frist two cards for both computer and user
   user_cards = []
   comp_cards = []
   for i in range (0,2):
     user_cards.append(deal_card())
     comp_cards.append(deal_card())
   print(f"Your cards: {user_cards},current_score: {sum(user_cards)}")
   print(f"Computer's first card: {comp_cards[0]}")
 #score calculator function
   def calculate_score(user_cards,comp_cards):
     if (sum(user_cards) ==21 and len(user_cards)==2) or (sum(comp_cards)==21 and len(comp_cards)==2):
        return 0
     if sum(user_cards)>21 and 11 in user_cards:
       user_cards.remove(11)
       user_cards.append(1)
     elif sum(comp_cards)>21 and 11 in comp_cards:
       comp_cards.remove(11)
       comp_cards.append(1)
 #blackjack check
   calculate_score(user_cards,comp_cards)
   if sum(user_cards)==21 and len(user_cards)==2 and sum(comp_cards)!=21:
     print("You won with a black jack")
     should_continue=False
   elif sum(comp_cards)==21 and len(user_cards)==2:
     print("You won with a black jack")
     should_continue=False
   else:
     should_continue=True
 #game rules comparisons
   def compare():
     user_score=sum(user_cards)
     comp_score=sum(comp_cards)
     print(f"Your cards: {user_cards},final_score: {user_score}")
     print(f"Computer's first card: {comp_cards},final_score: {comp_score}")

     if user_score == comp_score:
       print("Its a draw")
     elif  user_score==21:
       print("You won")
     elif comp_score==21:
       print("Opponent won")
     elif user_score>21:
       print("You went over opponent won")
     elif comp_score>21:
       print("Opponent went over.You won")
     elif comp_score>user_score:
       print("Opponent won")
     else:
       print("You won")
 #user turn for drawing cards
   while should_continue==True and sum(user_cards)<=21:
     draw_card=input("Enter 'y' to draw a new card from the deck or 'n' to pass: ")
     if draw_card=="y":
       user_cards.append(deal_card())
       calculate_score(user_cards,comp_cards)
       print(f"Your cards: {user_cards},current_score: {sum(user_cards)}")
       print(f"Computer's first card: {comp_cards[0]}")
     if draw_card=="n":
      should_continue=False 
 #computer turn for drawing cards
   while sum(comp_cards)<17:
     comp_cards.append(deal_card())
     calculate_score(user_cards,comp_cards)
 #calling score function to compare score of both user and comp
   when_compare=calculate_score(user_cards,comp_cards)
   if when_compare!=0:
      compare()
#calling game function
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")=="y":
  blackjack()
  
