#!/usr/bin/env python3
from itertools import product

N=7
WORDS=[''.join(p) for p in product('01', repeat=N)]

def deletion_ball(w):
    return {w[:i]+w[i+1:] for i in range(len(w))}

BALLS=[deletion_ball(w) for w in WORDS]
ADJ=[0]*len(WORDS)
for i in range(len(WORDS)):
    for j in range(i+1,len(WORDS)):
        if len(BALLS[i] & BALLS[j]) < 2:
            ADJ[i] |= 1<<j
            ADJ[j] |= 1<<i

best=[]

def greedy_color_order(P):
    order=[]; bounds=[]; color=0; U=P
    while U:
        color += 1
        Q=U
        while Q:
            bit=Q & -Q
            v=bit.bit_length()-1
            order.append(v); bounds.append(color)
            U ^= bit
            Q ^= bit
            Q &= ~ADJ[v]
    return order,bounds

def expand(clique, P):
    global best
    if not P:
        if len(clique)>len(best): best=clique[:]
        return
    order,bounds=greedy_color_order(P)
    for k in range(len(order)-1,-1,-1):
        if len(clique)+bounds[k] <= len(best):
            return
        v=order[k]
        bit=1<<v
        if not (P & bit):
            continue
        clique.append(v)
        expand(clique, P & ADJ[v])
        clique.pop()
        P &= ~bit

expand([], (1<<len(WORDS))-1)
assert len(best)==70, len(best)
print('MAX=70')
print('WITNESS=' + ','.join(WORDS[i] for i in sorted(best)))
print('SEARCH_OK')
