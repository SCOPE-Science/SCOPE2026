#!/usr/bin/env python3
"""Independent modular-counter orbit, right-output, and binomial-period tests."""
from collections import deque
from math import comb
from itertools import combinations, product


def base_period(a,m):
    n=m; p=2; result=1
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0:n//=p;e+=1
            h=0;power=1
            while power*p<=a:power*=p;h+=1
            result*=p**(e+h)
        p+=1
    if n>1:
        p=n;power=1;h=0
        while power*p<=a:power*=p;h+=1
        result*=p**(1+h)
    return result

def trans(a,b,m,P,state,letter):
    r,Y=state
    if letter=='0':return ((r+1)%P,Y)
    bval=comb(r,a)%m
    tmp=[]
    prev=bval
    for v in Y:
        tmp.append((v+prev)%m)
        prev=v
    return (r,tuple(tmp))

def suffix_signature(a,b,m,r,Y):
    pat='0'*a+'1'*b
    vec=[1]+[comb(r,j)%m for j in range(1,a+1)]+list(Y)
    sig=[]
    for offset in range(a+b+1):
        u=vec.copy()
        for ch in pat[offset:]:
            old=u.copy()
            for k in range(1,a+b+1):
                if pat[k-1]==ch:u[k]=(old[k]+old[k-1])%m
        sig.append(u[-1])
    return tuple(sig)

cases=0;total_states=0;period_tests=0
for a in range(1,10):
 for m in range(2,10):
    P=base_period(a,m)
    for T in range(1,2*P+1):
        periodic=all((comb(n+T,a)-comb(n,a))%m==0 for n in range(0,a+T+2))
        assert periodic == (T%P==0),(a,m,T,P)
        period_tests+=1
    for b in range(1,6):
        if P*(m**b)>2400:continue
        start=(0,(0,)*b);seen={start};todo=[start]
        for s in todo:
            for c in '01':
                t=trans(a,b,m,P,s,c)
                if t not in seen:seen.add(t);todo.append(t)
        assert len(seen)==P*(m**b),(a,b,m,len(seen),P*m**b)
        signatures={suffix_signature(a,b,m,*s) for s in seen}
        assert len(signatures)==len(seen),(a,b,m,'non-distinct suffix outputs')
        total_states+=len(seen);cases+=1
literal_tests=0
for a in range(1,5):
 for b in range(1,5):
  for m in range(2,8):
   P=base_period(a,m);pat='0'*a+'1'*b
   for length in range(0,9):
    for chars in product('01',repeat=length):
     word=''.join(chars); state=(0,(0,)*b)
     for letter in word:state=trans(a,b,m,P,state,letter)
     exact=sum(1 for positions in combinations(range(length),a+b) if ''.join(word[i] for i in positions)==pat)
     assert state[1][-1]==exact%m,(a,b,m,word,state,exact)
     literal_tests+=1
print('PASS modular_cases=%d states=%d binomial_period_tests=%d literal_modular_checks=%d'% (cases,total_states,period_tests,literal_tests))
