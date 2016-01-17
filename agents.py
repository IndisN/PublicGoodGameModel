#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
from interaction import PublicGoodGame


class Agent(object):
    def __init__(self, start_money, in_game_money_percent):
        self.total_money = start_money
        self.money_in_game = self.total_money * in_game_money_percent

    def __repr__(self):
        return 'Agent: total_money={0:.4f}, money_in_game={1:.3f}'.format(self.total_money, self.money_in_game)


class Society(object):
    def __init__(self, start_agents_number, start_agent_money):
        self.agents = [
            Agent(start_money=start_agent_money, in_game_money_percent=p)
            for p in [random.random() for i in range(start_agents_number)]
        ]

    def __iter__(self):
        for agent in self.agents:
            yield agent

    def play_once(self, agents_per_game):
        games_number = len(self.agents) // agents_per_game
        random.shuffle(self.agents)

        for i in range(games_number):
            self.agents[i*agents_per_game:i*agents_per_game+agents_per_game] = PublicGoodGame.play(self.agents[i*agents_per_game:i*agents_per_game+agents_per_game])

    def dying(self, dying_money_border):
        self.agents = [agent for agent in self.agents if agent.total_money >= dying_money_border]