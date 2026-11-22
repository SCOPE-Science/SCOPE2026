#!/usr/bin/env python3
"""Two independent exact joint-distribution recurrences and closed moments."""
from collections import defaultdict
from fractions import Fraction

def add_scaled(dst,poly,c,dt=0,da=0):
    for (t,a),v in poly.items():
        dst[t+dt,a+da]+=c*v

def recurrence(max_n):
    # Denominator: 1-2z+(1-uv)z^2-2u(v-1)z^3+u(v-1)z^4
    # Numerator: 1+u z^2-u v z^2.
    P=[]
    for n in range(max_n+1):
        out=defaultdict(int)
        if n==0:out[0,0]+=1
        if n==2:
            out[1,0]+=1;out[1,1]-=1
        if n>=1:add_scaled(out,P[n-1],2)
        if n>=2:
            add_scaled(out,P[n-2],-1)
            add_scaled(out,P[n-2],1,1,1)
        if n>=3:
            add_scaled(out,P[n-3],2,1,0)
            add_scaled(out,P[n-3],-2,1,1)
        if n>=4:
            add_scaled(out,P[n-4],-1,1,0)
            add_scaled(out,P[n-4],1,1,1)
        P.append({k:v for k,v in out.items() if v})
    return P

def automaton(max_n):
    # Tracks last three symbols only, independent of the rational run decomposition.
    state={('',0,0):1}
    out=[]
    for n in range(max_n+1):
        hist=defaultdict(int)
        for (tail,t,a),count in state.items():hist[t,a]+=count
        out.append(dict(hist))
        nxt=defaultdict(int)
        for (tail,t,a),count in state.items():
            for letter in '01':
                nt=t+(tail.endswith('0') and letter=='1')
                na=a+(tail.endswith('010') and letter=='1')
                nxt[(tail+letter)[-3:],nt,na]+=count
        state=nxt
    return out

def mean(n):
    return Fraction(0) if n<=1 else Fraction(1,4) if n==2 else Fraction(n*n+n+4,32)

def var(n):
    small={0:Fraction(0),1:Fraction(0),2:Fraction(3,16),3:Fraction(1,4),4:Fraction(5,16),5:Fraction(143,256)}
    return small[n] if n<6 else Fraction(2*n**3-5*n**2+45*n-60,512)

N=26
r=recurrence(N)
a=automaton(N)
for n in range(N+1):
    assert r[n]==a[n],(n,r[n],a[n])
    assert sum(r[n].values())==2**n,n
    moment1=sum((t*(t+1)//2-k)*v for (t,k),v in r[n].items())
    moment2=sum((t*(t+1)//2-k)**2*v for (t,k),v in r[n].items())
    assert Fraction(moment1,2**n)==mean(n),(n,'mean')
    assert Fraction(moment2,2**n)-mean(n)**2==var(n),(n,'variance')
    if n<=12 or n in (20,26):print(n,len(r[n]),str(mean(n)),str(var(n)))
print('PASS: rational-function and suffix-automaton exact distributions agree n=0..26')
