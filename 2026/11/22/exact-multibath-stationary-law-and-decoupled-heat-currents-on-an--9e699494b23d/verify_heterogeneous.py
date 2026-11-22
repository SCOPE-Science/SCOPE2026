"""Exact master-equation checks of a heterogeneous hot-hub Ising star.

Standard-library only; run: python verify_heterogeneous.py
"""
from fractions import Fraction as F
from itertools import product


def moments(t, rates, hub_rate):
    n=len(t)
    A=[F(0)]*(1<<n); B=[F(0)]*(1<<n)
    A[0]=F(1)
    for S in range(1,1<<n):
        ii=[i for i in range(n) if S & (1<<i)]
        den=sum(rates[i] for i in ii)
        A[S]=sum(rates[i]*t[i]*B[S^(1<<i)] for i in ii)/den
        B[S]=sum(rates[i]*t[i]*A[S^(1<<i)] for i in ii)/(hub_rate+den)
    return A,B


def exact_law(t,rates,hub_rate):
    n=len(t)
    A,B=moments(t,rates,hub_rate)
    result={}
    for state in product((-1,1),repeat=n+1):
        c=state[0]; signs=state[1:]
        w=[F(1)]*(1<<n)
        for S in range(1,1<<n):
            lowbit=S & -S; i=lowbit.bit_length()-1
            w[S]=w[S^lowbit]*signs[i]
        result[state]=sum(w[S]*(A[S]+c*B[S]) for S in range(1<<n))/2**(n+1)
    return result, A,B


def flip(state,k):
    return state[:k]+(-state[k],)+state[k+1:]


def transition(state,k,t,rates,hub_rate):
    if k==0: return hub_rate/2
    i=k-1
    return rates[i]*(1-state[0]*state[k]*t[i])/2


def check(t,rates,hub_rate):
    n=len(t)
    P,A,B=exact_law(t,rates,hub_rate)
    assert sum(P.values())==1
    assert min(P.values())>0
    for state in P:
        balance=F(0)
        for k in range(n+1):
            flipped=flip(state,k)
            balance+=P[flipped]*transition(flipped,k,t,rates,hub_rate)
            balance-=P[state]*transition(state,k,t,rates,hub_rate)
        assert balance==0,(state,balance)
    for i in range(n):
        corr=sum(prob*state[0]*state[i+1] for state,prob in P.items())
        assert corr==rates[i]*t[i]/(hub_rate+rates[i])
        assert hub_rate*corr + rates[i]*(corr-t[i])==0
    if n>=2:
        for i in range(n):
            for j in range(i+1,n):
                cov=sum(prob*state[i+1]*state[j+1] for state,prob in P.items())
                implied=t[i]*t[j]*rates[i]*rates[j]/(rates[i]+rates[j])*(F(1)/(hub_rate+rates[i])+F(1)/(hub_rate+rates[j]))
                assert cov==implied
                ui=rates[i]*t[i]/(hub_rate+rates[i])
                uj=rates[j]*t[j]/(hub_rate+rates[j])
                assert cov==ui*uj*(1+2*hub_rate/(rates[i]+rates[j]))
    return len(P)


def beta_moment(k, alpha):
    if k%2: return F(0)
    z=F(1)
    for j in range(k//2): z*=F(2*j+1,2)/(alpha+F(2*j+1,2))
    return z


if __name__=='__main__':
    tests=states=0
    settings=[(F(1),[F(1,3),F(2,5),F(3,7),F(1,2)], [F(1),F(2),F(3,2),F(4,3)]),
              (F(3,2),[F(1,4),F(2,3),F(5,9),F(3,8)], [F(2),F(1,2),F(3,5),F(3)]),
              (F(2,3),[F(1,3),F(1,2),F(1,6),F(2,7)], [F(2,3),F(2,3),F(2,3),F(2,3)])]
    for n in range(1,8):
        for hub,pt,pr in settings:
            t=[pt[j%4] for j in range(n)]
            r=[pr[j%4] for j in range(n)]
            states+=check(t,r,hub);tests+=1
    for n in range(1,9):
        for c,l,t0 in ((F(1),F(1),F(2,5)),(F(3),F(2),F(1,4))):
            A,B=moments([t0]*n,[l]*n,c)
            alpha=c/(2*l)
            for mask in range(1<<n):
                k=mask.bit_count()
                assert A[mask]==t0**k*beta_moment(k,alpha)
                assert B[mask]==t0**k*beta_moment(k+1,alpha)
    print(f'HETEROGENEOUS_EXACT_STATIONARITY_OK cases={tests} state_checks={states}')
    print('HOMOGENEOUS_BETA_MOMENTS_OK sizes=1..8 two-rate-sets')
