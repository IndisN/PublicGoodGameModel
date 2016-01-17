#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


class PublicGoodGame(object):
    @classmethod
    def play(cls, agents):
        """
        @type agents: Agent
        """
        players_number = len(agents)
        if players_number not in [2,3,4]: # range(2,5):
            # print >>sys.stderr, players_number, agents
            raise Exception('Количество игроков должно быть от 2 до 4!')

        total_game_sum = sum(agent.money_in_game for agent in agents)

        for agent in agents:
            agent.total_money += float(total_game_sum * 1.5) / players_number - agent.money_in_game
        return agents