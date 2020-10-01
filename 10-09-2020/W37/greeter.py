#!/usr/bin/env python3

import random

def simple_greeting(name):
    return "hello! " + name

def time_greeting(name):
    from datetime import datetime
    return f"It's {datetime.now()}, {name}"


greetings = [ simple_greeting
            , time_greeting
            ]

greeting = random.choice(greetings)
print(greeting("Christian"))

# 1. Add another greeting

# 2. Make all greetings take an name as input.


