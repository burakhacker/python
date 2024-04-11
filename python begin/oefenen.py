#dit is een variabel en hoe het werkt
#getal = 5
#print (getal)
#hier komt 5 uit
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#dit zijn de meest voorkomende datatypes
#int
#float
#string()
#boolean
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#print("   /|")
#print("  / |")
#print(" /  |")
#print("/_ _|")

#-------------------------------------------------------------------------------------------------------------------------------------------------------

#character_age = 33.213212
#character_name = "burak"
#is_male = True

#print("hallo ik ben " + character_name)
#print("en ik ben " + character_age + " jaar oud")

#character_name = "emir"
#print("ik houd van mij naam " + character_name)
#print("maar niet van mijn " + character_age + " jarige leeftijd")
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#werken met strings hier
#phrase = "Giraffe Academy"
#print(phrase.replace("Giraffe", "Elephant"))
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#werken met int dus cijfers
#from math import *
#my_num = 4.51
#print(floor(3.7)) 
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#input leren
#name = input("Enter your name: ")
#age = input("Enter your age: ")
#print("hello "+name + "! You are " + age)
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#simpel rekenmachine maken
#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = float(num1) + float(num2)

#print(result)
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#mad libs game?
#color = input("Enter a color: ")
#plural_noun = input("Enter a Plural Noun: ")
#celebrity = input("Enter a celebrity: ")

#print("roses are " + color)
#print(plural_noun + " are blue")
#print("I love " + celebrity)
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#mijn eigen mad libs game
#telefoon_merk = input("Zet hier je telefoon merk: ")
#kleur_telefoon = input("Zet hier je kleur van je telefoon: ")

#print(telefoon_merk + " is gaar en " + kleur_telefoon + " maakt het nog gaarder")
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#num1 = input("Enter a number: ")
#som = input(" select one of these 3 +  -  *  / : ")

#if som == '*':
    #num2 = input("Enter another number: ")
    #result = float(num1) * float(num2)
    #print(result)
#else:
    #num2 = input("Enter another number: ")
    #if som == '+':
        #result = float(num1) + float(num2)
    #elif som == '-':
        #result = float(num1) - float(num2)
    #elif som == '/':
        #result = float(num1) / float(num2)
    #else:
        #esult = print("Syantax Error")
        
    #if result is not None:
        #print("expectation", result)
        
        #print(result)
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#friends = ["Burak", "Emir", "drerrie"]
#print[1] = "mike"
#print(friends[1])

    
#luckt_numbers = [4, 8, 12, 16, 20, 24, 28]
#friends = ["Burak", "Emir", "Rhyan"]
#friends.extend(luckt_numbers)
#friends.append("Creed")
#friends.insert(1, "Bursko")
#print(friends)
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#dit is een tuple je kan het niet bewerken 
#coordinaten = (4, 5) (6, 7) (8, 9)
#coordinaten[1] = 10
#print(coordinaten[1])
#hier komt dus een error uit
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#functies 

#def zeg_hoi(name, age):
    #print("hello " + name + " you are " + (age)
    
#zeg_hoi("mike", "18")
#zeg_hoi("bravo", 30)
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#returnt statement
#def cube(num):
    #return num*num*num
#print("cube")

#result = cube(10)
#print(result)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#if statements

#is_male = False
#is_tall = True

#if is_male:
    #print("you are a male")
#else:
    #print("you are female   ")
#if is_tall:
    #print("you are tall")
#else:
    #print("you are short")
    
#dit is nog een manier----------------------------------------

#is_male = True
#is_tall = False

#if is_male or is_tall:
    #print("you are a male or tall or both")
#else:
    #print("you are neither")
    
#hier gebruik ik elif-----------------------------------------
    
#is_male = False
#is_tall = False

#if is_male and is_tall:
    #print("you are a tall male")
#elif is_male and not(is_tall):
    #print("You are a short male")
#elif not(is_male) and (is_tall):
    #print("You are not a male but tall")
#else:
    #print("you are neither male or tall")
    
#einde if statements
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#def max_num(num1, num2, num3):
    #if num1 >= num2 and num1 >= num3:
        #return num1
    #elif num2 >= num1 and num2 >= num3:
        #return num2
    #else:
        #return num3
    
    #print(max_num(3, 4, 5))
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#rekenmachine maken

#num1 = float(input("Voer een cijfer in: "))
#op = (input("Voer een som in : "))
#num2 = float(input("Voer een tweede cijfer in: "))
        
#if op == "+":
    #print(num1 + num2)
#elif op == "-":
    #print (num1 - num2)
#elif op == "/":
    #print (num1 / num2)
#elif op == "*":
    #print (num1 * num2)
#else:
    #print("Syntax error")
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#een dictionaries maken

#monthConversions = {
    #"Jan": "January",
    #"feb": "Febuary",
    #"mar": "March",
#}
   
#print(monthConversions["Jan"]) 
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#while loops

#i = 1
#while i <= 10:
    #print(i)
    #i += 2

#print("Done with looping")
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#gues game
#geheime_woord = "burak"
#gok_cijfer = 0
#gok_limit = 3
#Geen_gok_meer = False

#gok = ""

#while gok != geheime_woord and not (Geen_gok_meer):
    #if gok_cijfer < gok_limit:
        #gok = input("Gok maar: ")
        #gok_cijfer += 1
    #else:
        #Geen_gok_meer = True
        
#if Geen_gok_meer:
    #print("Je hebt verloren")  
#else:      
    #print("je hebt gewonnen! ")
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#def raise_to_power(base_num, pow_num):
    #result = 1
    #for index in range(pow_num):
        #result = result * base_num
    #return result

#print(raise_to_power(3, 4))
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Burak vertaling
#def translate(phrase):
    #translation = ""
    #for letter in phrase:
        #if letter in "AEIOUaeiou":
            #translation = translation + "g"
        #else:
            #translation = translation + letter
    #return translation

#print(translate(input("Enter a Phrase: ")))
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#try:
    #Number = int(input("Enter a Number: "))
    #print(Number)
#except:
    #print("Invalid Input")
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#datatype gemaakt (Zie student.py)-----------------------------------------------
#class student:
    
    #def __init__(self, name, major, gpa, is_on_probation):
        #self.name = name
        #self.major = major
        #self.gpa = gpa
        #self.is_on_probation = is_on_probation   
#------------------------------------------------------------------------------------------------------------------------------------------------------- 
#leuke quiz----------------------------------------------------------------------
#from vragen import vragen
#vragen_prompts = [
    #"hoe doe je een comment in python?\n(A) = //\n(B) = #\n(C) = $\n\n",
    #"hoe roep je een variable op in python?\n(A) = $\n(B) = # \n(C) = string\n\n",
    #"hoe schrijf je iets in een int in python?\n(A) = ,,\n(B) = '' \n(C) = str\n\n"
#]

#vraag = [
    #vragen(vragen_prompts[0], "B"),
    #vragen(vragen_prompts[1], "C"),
   # vragen(vragen_prompts[2], "C"),
#]

#def run_test(vraag):
    #score = 0
    #for question in vraag:
        #answer = input(question.prompt)
        #if answer == question.answer:
            #score += 1
    #print("Je hebt " + str(score) + "/" +str(len(vraag)) + " correct")

#run_test(vraag)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#chef maakt eten-----------------
#from chef import chef
#from chineseChef import chineseChef

#My_chef = chef()
#My_chef.make_special_dish()

#MychineseChef = chineseChef()
#MychineseChef.make_fried_rice()
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#klaar met de video 

