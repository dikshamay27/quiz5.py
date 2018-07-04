#Question 1 :-    Write a Phython program to tell the  persinality of a person... (personality will be randomly generated,
use random module, term color for printed output)


#!/usr/bin/python
# William Thing
# March 29, 2015
# Personality Test
#
# The Keirsey test measures four independent dimensions of personality:
# Extrovert versus Introvert (E vs I): what energizes you
# Sensation versus iNtuition (S vs N): what you focus on
# Thinking versus Feeling (T vs F): how you interpret what you focus on
# Judging versus Perceiving (J vs P): how you approach life
# Individuals are categorized as being on one side or the other of each of these dimensions.  
# The corresponding letters are put together to form a personality type. 
# For example, if you are an extravert, intuitive, thinking, perceiving 
# person then you are referred to as an ENTP.
# This program will take people's Keirsey test answers to determine their
# personality type based on the four dimensions. Takes answer from given input
# file and writes results to a given output file.

# Returns number of times a specific answer was recorded in each
# of the four categories.
def sort_answers(answers, char):
   my_list = [0, 0, 0, 0];
   for i in range(10):
      if answers[i*7].upper() == char:
         my_list[0] += 1;
      for j in range(3):
         for k in range(1,3):
            if answers[i*7+j*2+k].upper() == char:
               my_list[j+1] += 1;
   return my_list;

# Returns percentage of B answers in the Keirsey test to determine a personality
# type
def percent_of_B(A_list, B_list):
   result = [];
   for i in range(len(B_list)):
      percentage = int(round(float(B_list[i]) / (A_list[i] 
                                         + B_list[i])*100));
      result.append(percentage);
   return result;

# Returns a person's personality type based on their responses
# 'X' signifies that a specific personality type for that dimension
# cannot be determined.
def extract_personality(B_list):
   result = ""
   # dimension one: Extrovert versus Introvert (E vs I): what energizes you
   if B_list[0] > 50:
      result += "I";
   elif B_list[0] < 50:
      result += "E";
   else:
      result += "X";
   # dimension two: Sensation versus iNtuition (S vs N): what you focus on   
   if B_list[1] < 50:
      result += "S";
   elif B_list[1] > 50:
      result += "N";
   else:
      result += "X";
   # dimension three: Thinking versus Feeling (T vs F): how you interpret what you focus on
   if B_list[2] < 50:
      result += "T";
   elif B_list[2] > 50:
      result += "F";
   else:
      result += "X";
   # dimension four: Judging versus Perceiving (J vs P): how you approach life 
   if B_list[3] < 50:
      result += "J";
   elif B_list[3] > 50:
      result += "P";
   else:
      result += "X";
      
   return result;

# Introduction to Personality Test Software
def intro():
   print("""This program processes a file of answers to the
Keirsey Temperament Personality Sorter. It converts
the various A and B answers for each person into
a sequence of B-percentages and then into a
four-letter personality type.""");

def main():
   intro();
   input_file = raw_input("input file name? ");
   output_file = raw_input("output file name? ");
   fo = open(input_file, "r");
   fw = open(output_file, "wb");
   content = fo.readlines();
   names = []
   personality_test = []
   for i in range(len(content)):
      if i % 2 != 0:
         personality_test.append(content[i].rstrip('\n'));
      else:
         names.append(content[i].rstrip('\n'));
   ppl_count = 0;
   while ppl_count < len(names):
      A_response = sort_answers(personality_test[ppl_count], 'A');
      B_response = sort_answers(personality_test[ppl_count], 'B');
      overall_B = percent_of_B(A_response, B_response);
      personality = extract_personality(overall_B);
      data = names[ppl_count] + ": " + str(overall_B) + " = " + personality  + "\n";
      fw.write(data);
      ppl_count+= 1;

   fo.close();
   
if __name__ == "__main__": main()


#Question 2 :-    Write a Phython program to implement Rock paper scissor game


rom random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]


#Question 4 :-      Write a program to generate cipher text( means secret text encrypted text)




  # Caesar Cipher

 

  MAX_KEY_SIZE = 26

 

  def getMode():

      while True:

          print('Do you wish to encrypt or decrypt a message?')

          mode = input().lower()

          if mode in 'encrypt e decrypt d'.split():

             return mode

         else:

             print('Enter either "encrypt" or "e" or "decrypt" or "d".')



 def getMessage():

     print('Enter your message:')

     return input()



 def getKey():

     key = 0

     while True:

         print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))

         key = int(input())

         if (key >= 1 and key <= MAX_KEY_SIZE):

             return key



 def getTranslatedMessage(mode, message, key):

     if mode[0] == 'd':

         key = -key

     translated = ''



     for symbol in message:

         if symbol.isalpha():

             num = ord(symbol)

             num += key



             if symbol.isupper():

                 if num > ord('Z'):

                     num -= 26

                 elif num < ord('A'):

                     num += 26

             elif symbol.islower():

                 if num > ord('z'):

                     num -= 26

                 elif num < ord('a'):

                     num += 26



             translated += chr(num)

         else:

             translated += symbol

     return translated



 mode = getMode()

 message = getMessage()

 key = getKey()



 print('Your translated text is:')

 print(getTranslatedMessage(mode, message, key))

