#!/usr/bin/env python3
"""Exact rational evidence for a multi-nutrient coexistence entropy identity.
The analytical proof, not these finite checks, establishes all-size results.
"""
from fractions import Fraction as Q
from random import Random

S, M = 3, 2
beta, gamma = Q(1), Q(1)
th = [Q(1,2), Q(2,3), Q(3,4)]
a = [[Q(1,2), Q(1)], [Q(1), Q(2,3)], [Q(3,4), Q(1,3)]]
Ns, Rs = [Q(1), Q(2), Q(3)], [Q(2), Q(3)]
Ts = [[beta * Rs[j] / (beta + gamma * th[i] * a[i][j] * Ns[i]) for j in range(M)] for i in range(S)]
k = [sum(a[i][j] * ((1-th[i])*Rs[j]+th[i]*Ts[i][j]) for j in range(M)) for i in range(S)]
R0 = [Rs[j] + gamma * Rs[j] * sum((1-th[i])*a[i][j]*Ns[i] for i in range(S)) + beta * sum(Rs[j]-Ts[i][j] for i in range(S)) for j in range(M)]

def derivative(N, R, T):
    Nd = [N[i] * (sum(a[i][j]*((1-th[i])*R[j]+th[i]*T[i][j]) for j in range(M)) - k[i]) for i in range(S)]
    Rd = [R0[j]-R[j]-gamma*R[j]*sum((1-th[i])*a[i][j]*N[i] for i in range(S))-beta*sum(R[j]-T[i][j] for i in range(S)) for j in range(M)]
    Td = [[beta*(R[j]-T[i][j])-gamma*th[i]*a[i][j]*T[i][j]*N[i] for j in range(M)] for i in range(S)]
    return Nd,Rd,Td

def check(N, R, T):
    Nd,Rd,Td=derivative(N,R,T)
    actual=gamma*sum((1-Ns[i]/N[i])*Nd[i] for i in range(S))+sum((1-Rs[j]/R[j])*Rd[j] for j in range(M))+sum((1-Ts[i][j]/T[i][j])*Td[i][j] for i in range(S) for j in range(M))
    rhs=Q(0)
    for j in range(M):
        coeff=1+gamma*sum((1-th[i])*a[i][j]*Ns[i] for i in range(S))
        rhs-=coeff*(R[j]-Rs[j])**2/R[j]
        for i in range(S):
            u,v=R[j]/Rs[j],T[i][j]/Ts[i][j]
            t=Ts[i][j]/Rs[j]
            P=u*u+u*v*v-3*u*v+v
            rhs-=beta*Rs[j]/(u*v)*(t*(u-v)**2+(1-t)*P)
    assert actual == rhs, (actual, rhs)
    return actual

assert derivative(Ns,Rs,Ts)==([Q(0)]*S,[Q(0)]*M,[[Q(0)]*M for _ in range(S)])
assert check(Ns,Rs,Ts)==0
rng=Random(261100222)
for count in range(700):
    N=[Ns[i]*Q(rng.randint(1,11),rng.randint(1,11)) for i in range(S)]
    R=[Rs[j]*Q(rng.randint(1,11),rng.randint(1,11)) for j in range(M)]
    T=[[Ts[i][j]*Q(rng.randint(1,11),rng.randint(1,11)) for j in range(M)] for i in range(S)]
    result=check(N,R,T)
    # P >=0 from the analytical square decomposition; all other terms nonnegative.
    assert result<0
print('PASS: exact 3-species, 2-nutrient equilibrium and 700 statewise entropy identities, strict negative dissipation')
