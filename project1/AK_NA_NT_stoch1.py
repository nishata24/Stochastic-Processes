# Epic Question 1. Dice rolls and character creation. 
"""In Dungeons and Dragons, an ability score of 18 indicates the highest innate ability a human can have. To generate an
ability score, roll 3d6. A score of 3 is the lowest possible value a human can have, and a score of 18 is the highest. A
value of 9 is considered average. There are 6 ability scores (strength, dexterity, intelligence, wisdom, constitution
and charisma). The fun method for creating a character is to generate 3 values per ability score, and keep the highest
one. Answer the following questions."""

import random

def rollDie():
    # roll 1d6 and return the result
    return random.choice([1,2,3,4,5,6])


#1. a) What is the probability that any one roll of 3 dice, you generate an ability score of 18?

def roll_3d6_get_18(numTrials): # calculate probability of rolling a total of 18 on 3 six-sided dice
    yes = 0 # count the number of times the total is 18
    for rolls in range(numTrials): # roll 3 six-sided dice using rollDie()
        d1 = rollDie()
        d2 = rollDie()
        d3 = rollDie()
        if d1 + d2 + d3 == 18: # add up the results from the 3 rolls
            yes += 1 # if 3 rolls add up to 18, update yes
    print ('Probability of rolling 18 on any single roll =', yes/numTrials) # print probability of a sum of 18 from 3 rolls


#1. b) What is the probability, using the fun method of generating 3 scores and keeping the highest, that you generate an ability score of 18?

def roll_3d6x3_get_18(numTrials): # calculates probability of rolling a total of 18 on 3 rolls of 3 six-sided dice, where the highest of the three totals is the result
    yes = 0 # count number of times the highest total is 18
    for i in range(numTrials): 
        sumroll = []
        for rolls in range(0,3): # roll 3 six-sided dice 3 times
            d1 = rollDie()
            d2 = rollDie()
            d3 = rollDie()
            sumroll.append(d1 + d2 + d3)
        # print(sumroll)
        if max(sumroll) == 18: # check which of the 3 sums is the highest
            yes += 1 # if the highest sum is 18, update count
    print ('Probability of rolling 18 with special mode =', yes/numTrials)

#1. c) What is the probability using the fun method, you generate a character that is the most perfect form of human possible (i.e. a character not unlike Prof Fred Fontaine), that has 18’s in all ability scores?
# d) What is the probability using the fun method, you generate the most average, uninteresting character possible (i.e. a character remarkably similar to Prof. Keene), that has 9’s in all ability scores? Hint: there are 25 ways to roll a 9 with 3 dice.

def roll_six_consecutive_scores(numTrials, score): # calculates probability of rolling 6 consecutive scores of a specific value on 3 rolls of 3 six-sided dice
    yes = 0 # count number of times 6 consecutive scores of the specified value are rolled
    kept_sum = [] # emtpy list to store max score from each set of 3 rolls
    for i in range(numTrials):
        sumroll = [] 
        for rolls in range(0,3): # roll 3 six-sided dice 3 times
            d1 = rollDie()
            d2 = rollDie()
            d3 = rollDie()
            sumroll.append(d1 + d2 + d3)
        kept_sum.append(max(sumroll))

    #detect how many times score appears 6 times in a row
    for i in range(len(kept_sum)-5):
        if kept_sum[i] == score and kept_sum[i+1] == score and kept_sum[i+2] == score and kept_sum[i+3] == score and kept_sum[i+4] == score and kept_sum[i+5] == score:
            yes += 1
    print ('Probability of rolling ' + str(score) + ' 6 times in a row = ' + str(yes/numTrials))


N = 10000000
roll_3d6_get_18(N) # 1. a)
roll_3d6x3_get_18(N) # 1. b)
roll_six_consecutive_scores(N, 18) # 1. c)
roll_six_consecutive_scores(N, 9) # 1. d)

