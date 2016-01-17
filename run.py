#!/usr/bin/python
# -*- coding: utf-8 -*-
from agents import Society

def main():
    society = Society(start_agent_money=100, start_agents_number=7)

    for i in range(5):
        society.play_once(agents_per_game=3)
        society.dying(dying_money_border=130)
    for agent in society:
        print agent

if __name__ == '__main__':
    main()