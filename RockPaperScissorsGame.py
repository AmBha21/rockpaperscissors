#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:13:28 2022

@author: amolbhagavathi
"""
from random import randint
def rock_paper_scissors(user_input):
    user_input.lower()
    rock_paper_sciccors_list=["rock","paper","scissors"]
    computer_choice=rock_paper_sciccors_list[randint(0,len(rock_paper_sciccors_list)-1)]
    if user_input==computer_choice:
        return "It's a draw"
    if user_input=="rock" and computer_choice=="scissors" or user_input=="paper" and computer_choice=="rock" or user_input=="scissors" and computer_choice=="paper":
        return computer_choice,"You win"
    return computer_choice,"You lose"  