#!/usr/bin/env python3
"""Exact-rational checks for explicit one-sided LAB shape-limit formulas."""
from fractions import Fraction as Q

def sortmap(triple):
    a, b, c = sorted(triple, reverse=True)
    return b / a, c / a

def L(z):
    x, y = z
    return sortmap((Q(1,2), x, y+Q(1,2)))

def R(z):
    x, y = z
    return sortmap((Q(1,2), y, x+Q(1,2)))

def insideF(z):
    x, y = z
    return x >= Q(1,2) and y >= x-Q(1,2)

def insideG(z):
    return z[1] <= Q(1,2)

def PL(z):
    x,y=z
    if x >= Q(1,2):
        if y >= x-Q(1,2): t=Q(3)*x/(2*(1+y))
        else: t=Q(3)*(y+Q(1,2))/(2*x+1)
    elif 2*x+y >= Q(1,2):
        t=Q(3)/(4*(x+y+Q(1,2)))
    else: t=Q(3)*(2*x+y+Q(1,2))/(3+2*y)
    return t,Q(1,2)

def PR(z):
    x,y=z
    if y <= Q(1,2): t=Q(3)*y/(2*(1+x))
    else: t=Q(3)/(4*(x+y+Q(1,2)))
    return Q(1,2),t

def stable_L(z,m):
    x,y=z
    assert insideF(z)
    s=1+y
    a=Q(2,3)*s+Q(1-2*y,3)*(-Q(1,2))**m
    return x/a, s/a-1

def stable_R(z,m):
    x,y=z
    assert insideG(z)
    s=1+x
    a=Q(2,3)*s+Q(1-2*x,3)*(-Q(1,2))**m
    return s/a-1,y/a

def check(z):
    assert Q(0)<z[1]<=z[0]<=Q(1)
    assert insideF(L(L(z)))
    assert insideG(R(z))
    assert PL(L(z)) == PL(z) and PR(R(z)) == PR(z)
    assert PL(PL(z)) == PL(z) and PR(PR(z)) == PR(z)
    assert Q(1,2)<=PL(z)[0]<=1 and 0<PR(z)[1]<=Q(1,2)
    u=z
    for n in range(13):
        if n >= 2: assert u == stable_L(L(L(z)),n-2), ('L', z,n,u)
        u=L(u)
    u=z
    for n in range(13):
        if n>=1: assert u == stable_R(R(z),n-1), ('R',z,n,u)
        u=R(u)
    assert PL(z) == (Q(3)*L(L(z))[0]/(2*(1+L(L(z))[1])),Q(1,2))
    assert PR(z) == (Q(1,2), Q(3)*R(z)[1]/(2*(1+R(z)[0])))

n=0
for den in (7,11,17,31):
    for i in range(1,den+1):
        for j in range(1,i+1):
            check((Q(i,den),Q(j,den)))
            n+=1
# Nonempty sharp-burn-in witness chambers, and rate witness.
assert not insideF((Q(1,10),Q(1,10)))
assert not insideF(L((Q(1,10),Q(1,10))))
assert insideF(L(L((Q(1,10),Q(1,10)))))
assert not insideG((Q(4,5),Q(3,5))) and insideG(R((Q(4,5),Q(3,5))))
assert insideF((Q(3,4),Q(1,4)))
assert stable_L((Q(3,4),Q(1,4)),3) != PL((Q(3,4),Q(1,4)))
assert stable_R((Q(3,4),Q(1,4)),3) != PR((Q(3,4),Q(1,4)))
print('PASS:',n,'exact-rational initial states; both projection identities, entry thresholds, iterates 0..12, and sharpness witnesses')
