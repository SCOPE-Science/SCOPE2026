#!/usr/bin/env python3
"""Exhaustive checks of cyclic trace masks and erasure formulas; no external dependencies."""
from itertools import combinations
from math import comb, factorial

PRIMITIVE={2:0b111,3:0b1011,4:0b10011,5:0b100101}

def mult(a,b,m,p):
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a&(1<<m):a^=p
    return z

def power_table(m):
    p=PRIMITIVE[m]; out=[1]
    for i in range(1,(1<<m)-1):out.append(mult(out[-1],2,m,p))
    assert len(set(out))==2**m-1
    return out

def trace(x,m,p):
    s=0;y=x
    for _ in range(m):s^=y; y=mult(y,y,m,p)
    assert s in (0,1)
    return s

def coefficient(m,D,shifts,indices,k):
    allpatterns=(1<<(1<<k))-1
    count=0
    for S in combinations(indices,k):
        observed=0
        for t,row in enumerate(shifts):
            if t in D:continue
            p=0
            for j,i in enumerate(S):p|=((row>>i)&1)<<j
            observed|=1<<p
            if observed==allpatterns:break
        if observed==allpatterns:count+=1
    return count

def rank(vs):
    vs=list(vs);r=0
    for bit in range(14,-1,-1):
        idx=next((j for j in range(r,len(vs)) if (vs[j]>>bit)&1),None)
        if idx is None:continue
        vs[r],vs[idx]=vs[idx],vs[r]
        for j in range(len(vs)):
            if j!=r and (vs[j]>>bit)&1:vs[j]^=vs[r]
        r+=1
    return r

def ind(m,k):
    a=1
    for i in range(k):a*=((1<<m)-(1<<i))
    return a//factorial(k)

def top_factor(m):return ind(m-1,m-1)

def lower_factor(m):return ind(m-2,m-2)

def expected(m,D):
    DD={D[i]^D[j] for i in range(len(D)) for j in range(i+1,len(D))}
    covered=set(D)|DD
    top=top_factor(m)*((1<<m)-1-len(covered))
    low=ind(m,m-2)
    if len(D)==3 and D[0]^D[1]^D[2]==0:low-=lower_factor(m)
    return top,low

def run():
    for m in range(2,6):
        powers=power_table(m);p=PRIMITIVE[m];L=len(powers)
        seq=[trace(x,m,p) for x in powers]
        shifts=[sum(seq[(t+i)%L]<<i for i in range(L)) for t in range(L)]
        samples=[(),(0,),(0,1),(0,1,2)]
        # guarantee dependent triple: alpha^u xor alpha^v is alpha^w
        third=powers.index(powers[0]^powers[1]);samples.append((0,1,third))
        print('degree',m,'period',L,'first',seq[:12],flush=True)
        for T in samples:
            if max(T,default=0)>=L:continue
            deleted=[powers[t] for t in T]
            observed_top=coefficient(m,set(T),shifts,range(L),m-1)
            predicted_top,predicted_lower=expected(m,deleted)
            assert observed_top==predicted_top,(m,T,observed_top,predicted_top)
            if len(T)==3 and m>=3:
                observed_lower=coefficient(m,set(T),shifts,range(L),m-2)
                assert observed_lower==predicted_lower,(m,T,observed_lower,predicted_lower)
                print(' ',T,'dependent' if rank(deleted)==2 else 'independent','top',observed_top,'low',observed_lower,flush=True)
            else:print(' ',T,'top',observed_top,flush=True)
    print('ALL EXHAUSTIVE TESTS PASSED')
if __name__=='__main__':run()
