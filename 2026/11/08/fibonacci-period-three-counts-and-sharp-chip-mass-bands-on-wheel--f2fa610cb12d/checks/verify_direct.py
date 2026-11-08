#!/usr/bin/env python3
"""Independent direct update enumeration of bounded periodic chip states on wheels."""
import json
from itertools import product
from collections import Counter
from math import comb

def fib(t):
    a,b=0,1
    for _ in range(t): a,b=b,a+b
    return a

def predicted_total(n):
    return 3*n*(fib(2*n+1)+{0:3,1:-2,2:-1}[n%3])

def run(n):
    # Vertex 0 is the hub; vertices 1,...,n are the cyclic rim.
    nb=[list(range(1,n+1))]
    for i in range(n):
        nb.append([0,1+(i-1)%n,1+(i+1)%n])
    deg=[len(x) for x in nb]
    def step(x):
        fire=[int(x[i]>=deg[i]) for i in range(n+1)]
        return tuple(x[i]-deg[i]*fire[i]+sum(fire[j] for j in nb[i]) for i in range(n+1))
    mass=Counter(); states=0
    for x in product(*(range(2*d) for d in deg)):
        states+=1
        y=step(x)
        if y==x:continue
        if step(step(y))==x:mass[sum(x)]+=1
    assert sum(mass.values())==predicted_total(n),(n,dict(mass),predicted_total(n))
    return {"n":n,"states_checked":states,"period_three":sum(mass.values()),"mass_counts":sorted(mass.items())}

if __name__=='__main__':
    rows=[run(n) for n in range(3,7)]
    print(json.dumps({"status":"PASS","method":"independent full bounded state iteration","cases":rows},sort_keys=True,separators=(',',':')))
