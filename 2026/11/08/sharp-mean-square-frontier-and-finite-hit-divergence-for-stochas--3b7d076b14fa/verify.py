#!/usr/bin/env python3
"""Exact-rational checks for scalar stochastic reflected-gradient moment geometry.
No external packages, data, network calls or state are needed.
The infinite statements follow from the written proof, not these finite checks.
"""
from fractions import Fraction as Q
from itertools import product
from math import sqrt

checks = 0

def check(condition):
    global checks
    assert condition
    checks += 1

def moment_matrix(h, m, v):
    return (
        (1 - 4*h*m + 4*h*h*v, h*h*v, 2*h*m - 4*h*h*v),
        (Q(1), Q(0), Q(0)),
        (1 - 2*h*m, Q(0), h*m),
    )

def det3(M):
    a,b,c = M[0]
    d,e,f = M[1]
    g,h,i = M[2]
    return a*(e*i-f*h) - b*(d*i-f*g) + c*(d*h-e*g)

def update(state, M):
    return tuple(sum(M[i][j]*state[j] for j in range(3)) for i in range(3))

def oracle_step(x, prev, z):
    # h = 1/(2m), and z = h U in {0,1}.
    return ((1-2*z)*x + z*prev, x)

# Check the characteristic-one determinant for many *exact* admissible moments.
for m in [Q(1,3), Q(2,3), Q(1), Q(5,2), Q(7)]:
    for ratio in [Q(1), Q(11,10), Q(3,2), Q(2), Q(7)]:
        v = ratio*m*m
        for h in [Q(1,100)/m, Q(1,5)/m, Q(1,2)/m,
                  Q(2,3)/m, Q(3,2)/m, Q(2)/m]:
            M = moment_matrix(h,m,v)
            I_minus_M = [[(Q(i==j)-M[i][j]) for j in range(3)] for i in range(3)]
            check(det3(I_minus_M) == h*(2*m-h*v-3*h*h*m*v))

# Exact finite-path enumeration against exact covariance propagation.
for x0, xm1 in [(Q(1),Q(0)), (Q(0),Q(1)),
                (Q(-2),Q(5,3)), (Q(3,7),Q(-1,4))]:
    M = moment_matrix(Q(1,2),Q(1),Q(2))
    state = (x0*x0, xm1*xm1, x0*xm1)
    for n in range(10):
        S=P=C=Q(0)
        for bits in product((0,1), repeat=n):
            x,prev = x0,xm1
            for bit in bits:
                x,prev = oracle_step(x,prev,bit)
            S += x*x
            P += prev*prev
            C += x*prev
        denom = 2**n
        check(state==(S/denom,P/denom,C/denom))
        state=update(state,M)

# The specific starting pair has zero lag covariance and a growing second moment.
M = moment_matrix(Q(1,2),Q(1),Q(2))
state=(Q(1),Q(0),Q(0))
s=[]
for n in range(46):
    s.append(state[0])
    check(state[2]==0)
    if n>=2:
        check(s[n]==s[n-1]+Q(1,2)*s[n-2])
    state=update(state,M)
check(s[45]>s[35]>s[25]>s[15]>s[5]>1)

# The three-draw reset word (0,1,0) annihilates *any* initial state.
for x0,xm1 in [(Q(a,3),Q(b,5)) for a in range(-7,8) for b in range(-7,8)]:
    x,prev=x0,xm1
    for bit in [0,1,0]:
        x,prev=oracle_step(x,prev,bit)
    check((x,prev)==(0,0))

# For all-active draws, the sample path consists of alternating Fibonacci numbers.
fib=[0,1]
for i in range(2,50):
    fib.append(fib[-1]+fib[-2])
x,prev=Q(1),Q(0)
for n in range(36):
    check(x==(-1)**n*fib[n+1])
    check(s[n]>=Q(fib[n+1]**2, 2**n))
    x,prev=oracle_step(x,prev,1)

print('VERIFY_OK exact_rational_checks=',checks)
print('example: moment recursion S[n+1]=S[n]+S[n-1]/2; growth base=(1+sqrt(3))/2=',(1+sqrt(3))/2)
print('example: relative moment threshold tcrit=(sqrt(13)-1)/6=',(sqrt(13)-1)/6)
print('a.s. absorbing word: sampled normalized curvatures (0,1,0), probability 1/8 per disjoint triple')
