#!/usr/bin/env python3
'''
    This script merges the Marxist's Labour theoury of value with the theory of
    subjective preferences to find the most suitable flat in Munich.

    There are two key ideas to find the best flat in Munich:
    1. Describe your personal likelihood function for any parameter, such as
    "how far is my flat from my office", or "what is my preferable price".
    This is the neoclassical part of the script.
    2. Convert these parameters into your personal time. For more than one
    person the time weight might be calculated with some arbitrary weights.
    Then, the average convertion parameters are applied. It is necessary to
    normalize different dimensions of your problem into unit-less problem.
    This is the Marxist's part of the script.

    Copyleft: A. Rabusov <arabusov@gmail.com>

    License information:
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

    Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

    Everyone is permitted to copy and distribute verbatim or modified
    copies of this license document, and changing it is allowed as long
    as the name is changed.

           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

    0. You just DO WHAT THE FUCK YOU WANT TO.

'''
import numpy as np
import sys

class convertor_t:
    personal_weights = [1.]
    home_velocity = 3. # km/h
    walking_velocity = 3. # km/h
    money_weight = 1500./4./5./8. # 1500 money / month
    def flat_area (self, area):
        '''
            Area in m**2
        '''
        v = home_velocity / 1000.
        return area/v**2
    def walking_distance_km (self, distance):
        return distance/walking_velocity
    def walking_distance_m (self, distance):
        return self.walking_distance_km (distance/1000.)
    def money (self, money):
        return money / money_weight
    def __init__ (self, home_velocity=3., walking_velocity=3.,
            money_weight=1500./4./5./8.):
        """
            Standard conversion
            Must be also initialized with array-like parameters, but I'm lazy
        """
        self.home_velocity = 3. # km/h
        self.walking_velocity = 3. # km/h
        self.money_weight = 1500./4./5./8. # 1500 money / month

class likelihood_t:
    cnvr = convertor_t ()
    def price (self, cost):
    """
        Downfall exponent, of course
    """
        return np.exp (-cnvr.money (cost))
    def area (self, area):
        return np.exp (cnvr.flat_area (area))
    def walking_to_a_stop (self, distance):
        return np.exp (-cnvr.walking_distance_m (distance))
    def daily_public_transport_time (self, time)
        return np.exp (-time)
    def daily_public_transport_costs (self, costs):
        return np.exp (-cnvr.money (costs))
    def total (self)

if __name__ == "__main__":
    print ("Not ready")
