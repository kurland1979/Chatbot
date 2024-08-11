#פונקציה לקבלת המשתמש
def Acceptance_of_the_user():
    
    print("Welcome to the world of movies! ")
    print()
    name = input("Please introduce yourself, what is your name? ")
    print(f"Hello {name}, I hope you enjoy my recommendations, so I show you a menu and all you have to do is choose the genre that suits you! ")
    print()
#תפריט אופציות לז'אנרים עבור המשתמש
def Genres_menu():

    print("1. comedy")
    print("2. drama")
    print("3. action")
    print("4. horror ")

    choice = input("The choice is yours:")

    if choice.isdigit():
        choice_as_num = int(choice)
        if choice_as_num >= 1 and choice_as_num <= 4:
            return choice_as_num
        else:
            print("Error: Try again: 1 - 4" )
            return Genres_menu()
    else:
        print("Error")
        return Genres_menu()

#רשמית סרטים עבור כל ז'אנר
def List_of_movies():
    genre =  { "comedy" : ["Spy", "Focus", "Players", "Why Him?" ],
                "drama" : ["The Gambler", "Babylon", "A Man Called Otto", "If I Stay"],
                "action" : ["The Whale", "Fast X", "The Little Mermaid", "Killers of the Flower Moon"],
                "horror" : ["Longlegs", " Tarot", "The First Omen", "Abigail"] 
             }
    return genre

def print_movie_list(category):
    # מקבלים את המילון של הסרטים
    movie_dict = List_of_movies()
    
    # בדיקה אם הקטגוריה קיימת במילון
    if category in movie_dict:
        print(f"Movies in the {category.capitalize()} category:")
        for movie in movie_dict[category]:
            print(f"- {movie}")
    else:
        print("Invalid category.")


#סיום של צ'אטבוט עם המשתמש
def end_chat():
    print("Hope you enjoyed my recommendation and your choice!")
    

#בדיקת פלט מהמשתמש
def Output_test():
     
     while True:
         answer = input("Would you like to see more recommendations? y/n").strip().lower()

         if answer == "n":
             print("Thank you for enjoying my recommendations, hope we meet again")
             return False

             
         elif answer == "y":
             return True
         else:
             print("Error/ Try agein")
     
    

#פונקציה ראשית 
def Movie_chatbot():
    Acceptance_of_the_user()

    while True:
        num = Genres_menu()

        if num == 1:
            category = "comedy"
        elif num == 2:
            category = "drama"
        elif num == 3:
            category = "action"
        elif num == 4:
            category = "horror"
        
        print_movie_list(category)

        if not Output_test():
            break
    end_chat()
      
if __name__ == "__main__":
         Movie_chatbot()
      