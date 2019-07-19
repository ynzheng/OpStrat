"""
Created on Wed Jul 17 13:02:07 2019

@author: Atheesh Krishnan

A python library implementation of widely used Options Trading Strategies.
"""
# import libraries
import pandas as pd
import numpy as np

def synthetic_long_put(spot_price, long_call_strike_price, long_call_premium):
    sT = np.arange(0.7 * spot_price, 1.3 * spot_price, 1)
    
    # A function that calculates the payoff from buying a call option. 
    # The function takes sT which is a range of possible values of stock price at expiration, 
    # strike price of the call option and premium of the call option as input. 
    # It returns the call option payoff.
    def call_payoff(sT, strike_price, premium):
        return np.where(sT > strike_price, sT - strike_price, 0) - premium
    
    long_call_payoff = call_payoff(sT, long_call_strike_price, long_call_premium)
    
    stock_payoff = (sT - spot_price) * -1.0

    synthetic_long_put_payoff = long_call_payoff + stock_payoff  
    print("Maximum Profit: {}".format(max(synthetic_long_put_payoff)))
    print("Maximum Loss: {}".format(min(synthetic_long_put_payoff)))
    
def option_strangle(spot_price, long_put_strike_price, long_put_premium,\
                   long_call_strike_price, long_call_premium):
    
    sT = np.arange(0.7 * spot_price, 1.3 * spot_price, 1)
    
    def call_payoff(sT, strike_price, premium):
        return np.where(sT > strike_price, sT - strike_price, 0) - premium
    long_call_payoff = call_payoff(sT, long_call_strike_price, long_call_premium)
    
    def put_payoff(sT, strike_price, premium):
        return np.where(sT < strike_price, sT - strike_price, 0)- premium
    long_put_payoff = put_payoff(sT, long_put_strike_price, long_put_premium)
    
    strangle_payoff = long_call_payoff + long_put_payoff
    print("Maximum Profit: {}".format(max(strangle_payoff)))
    print("Maximum Loss: {}".format(min(strangle_payoff)))
    print("This strategy is suitable when the outlook on the stock is moderately bearish.")

def long_short_combo(spot_price, strike_price, premium_paid, premium_received):
    
    sT = np.arange(0.7*spot_price, 1.3*spot_price, 1)
    
    def long_call(sT, strike_price, premium_paid):
        return np.where(sT > strike_price, sT - strike_price, 0) - premium_paid
    long_call_payoff = long_call(sT, strike_price, premium_paid)
    
    def short_put(sT, strike_price, premium_received):
        return np.where(sT > strike_price, 0, sT - strike_price) + premium_received
    short_put_payoff = short_put(sT, strike_price, premium_received)
    
    ls_combo_payoff = long_call_payoff + short_put_payoff
    
    print("Maximum Profit: {}".format(max(ls_combo_payoff)))
    print("Maximum Loss: {}".format(min(ls_combo_payoff)))
    
def jade_lizard(spot_price, long_call_strike_price, long_call_premium, \
                short_call_strike_price, short_call_premium, \
                short_put_strike_price, short_put_premium):
    
    sT = np.arange(0.9*spot_price, 1.1*spot_price, 1)
    
    # payoff on purchase of call options
    def call_payoff(sT, strike_price, premium):
        return np.where(sT > strike_price, sT - strike_price, 0) - premium
    
    long_call_payoff = call_payoff(sT, long_call_strike_price, long_call_premium)
    short_call_payoff = call_payoff(sT, short_call_strike_price, short_call_premium) * -1.0
    
    # payoff on purchasing put options
    def put_payoff(sT, strike_price, premium):
        return np.where(sT < strike_price, strike_price - sT, 0) - premium
    
    short_put_payoff = put_payoff(sT, short_put_strike_price, short_put_premium) * -1.0
    
    jade_lizard_payoff = long_call_payoff + short_call_payoff + short_put_payoff
    
    print("Maximum Profit: {}".format(max(jade_lizard_payoff)))
    print("Maximum Loss: {}".format(min(jade_lizard_payoff)))
    
jade_lizard(688, 750, 4.3, 730, 6.8, 660, 7.85)