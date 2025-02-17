
import random

#from constants import *
LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}


def draw_letters():
    letter_pool = LETTER_POOL.copy()
    letters=[]
    while len(letters) < 10:
        letter = random.choice(list(letter_pool))
        letters.append(letter)
        print(len(letters), letters)
        
        letter_pool[letter]-=1
        
        if letter_pool[letter] == 0:
            letter_pool.pop(letter)
            
        print (len(letter_pool), letter_pool)   
    return letters 
    


def uses_available_letters(word, letter_bank):
    counter = 0
    upper_word = word.upper()
    for i in upper_word: 
        counter += 1
        if upper_word.count(i) == letter_bank.count(i) and counter == len(upper_word):
            return True
            
        elif upper_word.count(i) > letter_bank.count(i) and counter == len(upper_word):
            return False


def score_word(word):
    
    score_dict = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
    }
#  allow user enter upper and lower case letters
    upper_word = word.upper()
    score = 0
    for letter in upper_word:
        score += score_dict[letter]
    if len(word) in range (7,11):
        score += 8
        
    return score



def get_highest_word_score(word_list):
    highest_score = 0
    best_word = ""
    
    for word in word_list:
        #Use of helper function
        total_scored = score_word(word) 
        if total_scored > highest_score:
            highest_score = total_scored 
            best_word= word 
        # conditionals with tie breaking logic below
        elif total_scored == highest_score:
            # Not mutable variable
            temp_word = best_word
            #From here highest rate is always the same as there is tie.
            if len(word) == 10:
                best_word = word    
            elif len(temp_word) == 10:
                best_word = best_word
            elif len(temp_word) > len(word):
               best_word = word

            if len(temp_word) == len(word):
                best_word = word_list[0]
    # then we will return the winning word as a tuple return tuple(best_word[0], highest_score)
    my_tuple = (best_word, highest_score)
    return my_tuple
           
            

        

