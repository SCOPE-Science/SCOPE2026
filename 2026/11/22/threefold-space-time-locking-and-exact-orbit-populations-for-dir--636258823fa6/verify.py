"""Exhaustive checker for dyadic directed Fibonacci cellular automata."""
from collections import Counter
from math import gcd

def rot_right(x,s,n):
    mask=(1<<n)-1
    s%=n
    return ((x>>s)|(x<<(n-s)))&mask

def step(u,v,s,n):
    return rot_right(u,s,n)^v,u

def period_spatial(u,v,s,n):
    x,y=u,v
    for t in range(1,n+1):
        x,y=rot_right(x,s,n),rot_right(y,s,n)
        if x==u and y==v: return t
    assert False

def formula(n,s):
    g=gcd(n,s)
    L=n//g
    m=L.bit_length()-1
    out={1:1,3:(1<<(2*g))-1}
    for j in range(1,m+1):
        out[3*(1<<j)]=(1<<(2*g*(1<<j)))-(1<<(2*g*(1<<(j-1))))
    return {k:v for k,v in out.items() if v>0}

def main():
    runs=0
    states=0
    for n in (1,2,4,8):
        for s in range(n):
            tally=Counter()
            max_t=3*n//gcd(n,s)
            for u in range(1<<n):
                for v in range(1<<n):
                    x,y=u,v
                    for t in range(1,max_t+1):
                        x,y=step(x,y,s,n)
                        if (x,y)==(u,v): break
                    else: raise AssertionError('missing return')
                    predicted=1 if not (u|v) else 3*period_spatial(u,v,s,n)
                    assert t==predicted, (n,s,u,v,t,predicted)
                    tally[t]+=1
                    states+=1
            assert dict(tally)==formula(n,s), (n,s,tally,formula(n,s))
            runs+=1
            print('n,s',n,s,'period population',dict(sorted(tally.items())))
    print(f'PASS: {runs} dyadic size/stride cases; {states} exhaustive states; space-time equality and cycle census')

if __name__=='__main__':main()
