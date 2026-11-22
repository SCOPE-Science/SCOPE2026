#!/usr/bin/env python3
"""Exact reproducibility checks for the leaf-count odds transition.
Run: python3 check.py
Only Python standard-library arithmetic is used.
"""
from fractions import Fraction as F

checks = 0

def check(condition, label):
    global checks
    assert condition, label
    checks += 1


def add(u,v):
    w=[0]*max(len(u),len(v))
    for i,a in enumerate(u): w[i]+=a
    for i,a in enumerate(v): w[i]+=a
    return w

def mul(u,v):
    w=[0]*(len(u)+len(v)-1)
    for i,a in enumerate(u):
        for j,b in enumerate(v): w[i+j]+=a*b
    return w

def deriv(u):
    return [i*u[i] for i in range(1,len(u))] or [0]

def sub(u,v):
    return add(u,[-x for x in v])

# R_n(t)=S_n(t)/B_n(t); both S and B have integer coefficients.
S,B=[0],[1]
cert=[]
for n in range(3,14):
    Snew=add(mul([6*n,6],S),mul(mul([n-2,1],[2*n,3]),B))
    Bnew=mul([4*n,6],B)
    S,B=Snew,Bnew
    Q=sub(mul(deriv(S),B),mul(S,deriv(B)))
    if n+1<=12:
        check(all(c>0 for c in Q),f'positivity coefficient test at size {n+1}')
        cert.append((n+1,len(Q)-1,min(Q)))
    elif n+1==13:
        check(any(c<0 for c in Q), 'first failure has negative coefficient')
    # R_n rational positivity is unconditional since B has positive coefficients.
    check(all(v>=0 for v in B), 'B polynomial positivity')


def odds(n,a):
    t=F(2)/a
    R=F(0)
    for k in range(3,n):
        R=F(3)*(k+t)/(2*k+3*t)*R+(k-2+t)/2
    return R

check(odds(13,F(1,2))-odds(13,F(1))==F(-15421,26112),'13-vertex strict reversal witness')
check(odds(12,F(1,2))-odds(12,F(1))==F(518051,121856),'12-vertex comparison')

# One-sided derivative at t=0 and its persistence for every n>=14.
r=q=F(0)
for m in range(3,100):
    qnew=F(3,2)*q-F(3,4*m)*r+F(1,2)
    rnew=F(3,2)*r+F(m-2,2)
    r,q=rnew,qnew
    if m+1==7:check(r==F(131,16),'r7 lower-bound base')
    if m+1==14:check(q==F(-696574397,164003840),'q14 strict negative')
    if m+1>=14:check(q<0, 'sign persistence sample (analytic induction covers all n)')

# Exact distribution recursion and independent full attachment-tree enumeration.
def distribution(a,up_to):
    d={2:F(1)}
    out={3:d.copy()}
    for n in range(3,up_to):
        e={}
        for ell,prob in d.items():
            stay= a*ell/(ell+a*n)
            e[ell]=e.get(ell,F(0))+prob*stay
            e[ell+1]=e.get(ell+1,F(0))+prob*(1-stay)
        d=e
        out[n+1]=d.copy()
    return out

def exhaustive(a,max_n):
    states={( (1,), (0,) ):F(1)}  # n=2 vertices; each tuple is neighbors.
    out={}
    for n in range(2,max_n+1):
        counts={}
        for tree,weight in states.items():
            degrees=[len(z) for z in tree]
            leaves=[i for i,d in enumerate(degrees) if d==1]
            ell=len(leaves)
            counts[ell]=counts.get(ell,F(0))+weight
        out[n]=counts
        if n==max_n:break
        new_states={}
        for tree,weight in states.items():
            degrees=[len(z) for z in tree]
            leaves={i for i,d in enumerate(degrees) if d==1}
            rates=[F(sum(j in leaves for j in tree[i]))+a for i in range(n)]
            total=sum(rates)
            for i,rate in enumerate(rates):
                next_tree=list(tree)+[(i,)]
                next_tree[i]=tuple(sorted(tree[i]+(n,)))
                next_tree=tuple(next_tree)
                new_states[next_tree]=new_states.get(next_tree,F(0))+weight*rate/total
        states=new_states
    return out

for a in (F(1,2),F(1),F(2),F(7,3)):
    dp=distribution(a,7)
    ex=exhaustive(a,7)
    for n in range(3,8):
        check(dp[n]==ex[n],f'exhaustive tree history n={n} a={a}')
        check(sum(dp[n].values())==1,f'probability normalization n={n} a={a}')
    check(F(0)<odds(13,a),'positive odds')

# Parameterwise stochastic order: exact finite-grid cross-check (proof gives all a and n).
for n in range(4,21):
    d1=distribution(F(1,2),n)[n]
    d2=distribution(F(2),n)[n]
    for k in range(2,n):
        check(sum(v for ell,v in d1.items() if ell>=k)>=sum(v for ell,v in d2.items() if ell>=k),
              f'stochastic-order finite check n={n} threshold={k}')

print('Exact checks passed:',checks)
print('Derivative-certificate (size, degree, minimum integer coefficient):')
for x in cert:print(*x)
print('R_13(t=4)-R_13(t=2) =',odds(13,F(1,2))-odds(13,F(1)))
print('q_14 =',F(-696574397,164003840))
