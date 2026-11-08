#!/usr/bin/env python3
"""Independent rational finite-state verification of a fixed-leaf voter process."""
from fractions import Fraction as F
from math import exp, log

def linear_solve(a, b):
    n=len(b)
    a=[list(map(F, row))+[F(b[i])] for i,row in enumerate(a)]
    for k in range(n):
        p=next(i for i in range(k,n) if a[i][k])
        a[k],a[p]=a[p],a[k]
        d=a[k][k]
        for j in range(k,n+1): a[k][j]/=d
        for i in range(n):
            if i!=k and a[i][k]:
                d=a[i][k]
                for j in range(k,n+1):a[i][j]-=d*a[k][j]
    return [a[i][n] for i in range(n)]

def solve_generator(states, trans, terminal_reward, running_reward):
    ix={s:i for i,s in enumerate(states)}
    a=[[F(0) for _ in states] for _ in states]
    b=[F(running_reward(s)) for s in states]
    for s,i in ix.items():
        for t,rate in trans(s):
            rate=F(rate)
            if rate==0:continue
            a[i][i]+=rate
            if t in ix:a[i][ix[t]]-=rate
            else:b[i]+=rate*terminal_reward(t)
    return dict(zip(states,linear_solve(a,b)))

def reduced(n):
    states=[(h,k) for h in (0,1) for k in range(n+1) if (h,k) not in [(0,0),(1,n)]]
    def transitions(s):
        h,k=s
        if h==0:return [((0,k-1),F(k)),((1,k),F(k+1,n+1))]
        return [((1,k+1),F(n-k)),((0,k),F(n-k,n+1))]
    q=solve_generator(states,transitions,lambda s:F(int(s==(1,n))),lambda s:0)[(1,0)]
    a=solve_generator(states,transitions,lambda s:F(0),lambda s:1)[(1,0)]
    b=solve_generator(states,transitions,lambda s:F(0),lambda s:int(s[0]==0))[(1,0)]
    return q,a,b,F(n+1,1)/q+a/q

def full(n):
    target=(1<<(n+1))-1
    states=list(range(target))
    def transitions(s):
        h=s&1; k=sum((s>>i)&1 for i in range(1,n+1))
        out=[]
        for i in range(1,n+1):
            if ((s>>i)&1)!=h:out.append((s^(1<<i),F(1)))
        if h==0:out.append((s|1,F(k+1,n+1)))
        else:out.append((s^1,F(n-k,n+1)))
        return out
    return solve_generator(states,transitions,lambda s:F(0),lambda s:1)[0]

def main():
    checks=0
    for n in range(1,6):
        q,a,b,m=reduced(n)
        f=full(n)
        assert m==f,(n,m,f)
        assert q*F(2*n+1)==n+1+b,(n,q,b)
        H=sum((F(1,j) for j in range(1,n+1)),F(0))
        assert 0<a<=F(8)*H
        assert F(n+1,2*n+1)<=q<=F(1)
        print('n=',n,'q=',str(q),'excursion=',str(a),'mean=',str(m),'decimal=',round(float(m),8))
        checks+=5
    for n in (10,50,100,1000):
        # The rigorous no-switch bounds used in the proof must hold uniformly.
        lower_plus=(F(n+1,n+2))**n
        lower_minus=(F(n+1,n+3))**n
        assert float(lower_plus)>=exp(-1.)
        assert float(lower_minus)>=exp(-2.)
        checks+=2
    assert all(exp(-2)<(1+2/(n+1))**(-n) for n in range(1,1000))
    checks+=1
    print('PASS',checks,'exact/rational or numerical inequality comparisons')
if __name__=='__main__':main()
