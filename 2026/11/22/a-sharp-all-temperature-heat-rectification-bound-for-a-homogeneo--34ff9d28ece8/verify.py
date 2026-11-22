#!/usr/bin/env python3
"""Exact rational full-state check for homogeneous 3-spin kinetic Ising heat transport.

Run: python3 verify.py. Uses the Python standard library only.
"""
from fractions import Fraction as F
from itertools import product

STATES = list(product((-1, 1), repeat=3))
INDEX = {state: k for k, state in enumerate(STATES)}


def solve(A, b):
    n = len(A)
    X = [[F(v) for v in row] + [F(b[i])] for i, row in enumerate(A)]
    for i in range(n):
        p = next(k for k in range(i, n) if X[k][i])
        X[i], X[p] = X[p], X[i]
        piv = X[i][i]
        X[i] = [v / piv for v in X[i]]
        for k in range(n):
            if k != i:
                f = X[k][i]
                if f:
                    X[k] = [u - f * v for u, v in zip(X[k], X[i])]
    return [row[-1] for row in X]


def check(t, u):
    # t = tanh(beta_end J), u = tanh(beta_center J), both rational in [0,1).
    t, u = F(t), F(u)
    v = 2 * u / (1 + u * u)
    # Column-stochastic generator M: d p/dt = M p.
    M = [[F(0) for _ in STATES] for _ in STATES]
    heats = [[F(0) for _ in STATES] for _ in range(3)]
    for j, state in enumerate(STATES):
        for i in range(3):
            h = state[1] if i in (0,2) else state[0] + state[2]
            thermal_tanh = t*h if i in (0,2) else v*h/F(2)
            rate = (1 - state[i]*thermal_tanh)/2
            target = list(state)
            target[i] *= -1
            k = INDEX[tuple(target)]
            M[k][j] += rate
            M[j][j] -= rate
            heats[i][j] = rate * 2 * state[i]*h  # J=1
    A = [row[:] for row in M]
    A[-1] = [F(1) for _ in STATES]
    b = [F(0)]*7+[F(1)]
    p = solve(A,b)
    assert all(x>0 for x in p)
    assert sum(p)==1
    assert all(sum(M[i][j]*p[j] for j in range(8))==0 for i in range(8))
    measured = [sum(heats[i][j]*p[j] for j in range(8)) for i in range(3)]
    predicted = 2*(t-u)*(1-t*u)/(2*(1+u*u)-t*u)
    assert measured[1]==predicted, (t,u,measured[1],predicted)
    assert measured[0]==measured[2]==-predicted/2
    x = sum(state[0]*state[1]*p[j] for j,state in enumerate(STATES))
    z = sum(state[0]*state[2]*p[j] for j,state in enumerate(STATES))
    assert x==(2*t+v)/(4-v*t)
    assert z==t*x


def two_spin(t,u):
    # Full 4-state kinetic Ising generator stationary bond correlation.
    states=list(product((-1,1),repeat=2))
    ids={s:i for i,s in enumerate(states)}
    M=[[F(0)]*4 for _ in range(4)]
    for j,s in enumerate(states):
        for i,T in enumerate((t,u)):
            rate=(1-s[0]*s[1]*T)/2
            v=list(s);v[i]*=-1
            k=ids[tuple(v)]
            M[k][j]+=rate;M[j][j]-=rate
    A=[r[:] for r in M];A[-1]=[F(1)]*4
    p=solve(A,[F(0)]*3+[F(1)])
    correlation=sum(s[0]*s[1]*p[j] for j,s in enumerate(states))
    assert correlation==(t+u)/2
    Qleft=correlation-t
    assert Qleft==(u-t)/2


def main():
    vals=[F(0),F(1,10),F(1,7),F(1,4),F(1,3),F(1,2),F(2,3),F(3,4),F(4,5),F(9,10)]
    trials=0
    for t in vals:
        for u in vals:
            check(t,u)
            two_spin(t,u)
            trials+=1
    print('EXACT_THREE_SPIN_CURRENT_OK', trials)
    print('EXACT_TWO_SPIN_BASELINE_OK', trials)

if __name__=='__main__':main()
