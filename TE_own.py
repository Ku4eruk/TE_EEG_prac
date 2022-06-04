# I(y -> x) = S(y) - S(y / x)
# S(y / x) = - SUM(p(x)) * SUM(p(y / x) * log2(p(y / x))) = 
# = - SUM(p(x, y)* log2(p(y / x)))
# S(y) = - SUM(p(y) * log2(p(y)))
# p(y / x) joint probability = P(A and B) / P(B) 
from math import log2
import random
from pprint import pprint


# S(y) = - SUM(p(y) * log2(p(y)))
def S_one(sign: list) -> float:
    probabilities = prob_one(sign)
    sum_s = 0
    for value in sign:
        sum_s -= probabilities[value] * log2(probabilities[value])
    return sum_s 

# S(y / x) = - SUM(p(x)) * SUM(p(y / x) * log2(p(y / x))) = 
# = - SUM(p(x, y)* log2(p(y / x)))
def S_double(sign1: list, sign2: list) -> float: # sign1 - y, sign2 - x
    joint_probabilities = prob_double(sign1, sign2)
    prob_sign2 = prob_one(sign2)
    sum_s = 0
    for key1, value1 in joint_probabilities.items():
        for key2, value2 in prob_sign2.items():
            sum_s -= value2 * joint_probabilities[key1][key2]
    return sum_s
            


def prob_one(sign: list) -> dict:
    characters = {}
    length = len(sign)
    for value in sign:
        if value not in characters:
            characters[value] = 1 / length
        else:
            characters[value] += 1 / length
    return characters


# p(y / x) joint probability = P(A and B) / P(B) 
def prob_double(sign1: list, sign2: list) -> dict:
    prob_list_sign1_and_sign2 = prob_one(sign1 + sign2)
    prob_list_sign2 = prob_one(sign2)
    prob_list_mutual = {}
    for key1, value1 in prob_list_sign1_and_sign2.items():
        prob_list_mutual[key1] = {}
        for key2, value2 in prob_list_sign2.items():
            prob_list_mutual[key1][key2] = value1 / value2
    return prob_list_mutual


# I(y -> x) = S(y) - S(y / x)
def te_calc(sign1: list, sign2: list) -> float:
    return S_one(sign1) - S_double(sign1, sign2) 



# q = prob_double([1, 2, 2, 1, 3, 3], [1, 1, 1, 2, 2, 5, 5])
# print(q)