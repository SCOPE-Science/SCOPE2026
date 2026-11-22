"""Finite test of dihedral fixed-space formulas for the 5-divisible partition graph.

Only the prime five case is enumerated. The all-prime statements require
and receive separate symbolic combinatorial proofs.
"""
from itertools import combinations
from math import comb

p=5; n=3*p; mask_all=(1<<n)-1
UP=[sum(1<<i for i in cb) for cb in combinations(range(n),p)]
UPSET=set(UP)
LO=[]
for a in UP:
    remaining=mask_all^a
    indices=[i for i in range(n) if remaining>>i&1]
    for cb in combinations(indices,p):
        b=sum(1<<i for i in cb); c=remaining^b
        if a<b<c:LO.append((a,b,c))
assert len(UP)==comb(3*p,p)==3003
assert len(LO)==126126

def action(mask,offset=0,reflection=False):
    value=0
    while mask:
        bit=mask&-mask; index=bit.bit_length()-1
        j=(offset-index)%n if reflection else (index+offset)%n
        value|=1<<j;mask-=bit
    return value

def fixed(generators):
    upper={u for u in UP if all(action(u,*g)==u for g in generators)}
    lower=[]
    incidences=0
    for triple in LO:
        if all(tuple(sorted(action(u,*g) for u in triple))==triple for g in generators):
            lower.append(triple)
            incidences+=sum(u in upper for u in triple)
    return len(upper),len(lower),incidences

M=comb(3*p,p)*(comb(2*p,p)//3-1)
u=comb((3*p-1)//2,(p-1)//2)
assert M==249249 and u==21
fixed_expected={(1,0):(3003,126126,378378),
                (1,1):(21,21*2**(p-1),21*2**(p-1)),
                (3,0):(0,3**(p-1),0),
                (3,1):(0,3**((p-1)//2),0),
                (p,0):(3,1,3),
                (p,1):(1,1,1),
                (3*p,0):(0,1,0),
                (3*p,1):(0,1,0)}
for h in (1,3,p,3*p):
    for refl in (0,1):
        gen=[] if h==1 else [(n//h,False)]
        if refl:gen.append((0,True))
        actual=fixed(gen)
        assert actual==fixed_expected[(h,refl)],(h,refl,actual,fixed_expected[(h,refl)])
        predicted=1+(M-(h-1)-2*(3**(p-1)-1 if h%3==0 else 0)-refl*h*u)//(h*(1+refl))
        assert (M-(h-1)-2*(3**(p-1)-1 if h%3==0 else 0)-refl*h*u)%(h*(1+refl))==0
        print('h',h,'reflection',refl,'fixed U,T,E',actual,'quotient first Betti',predicted)
print('SUCCESS: eight subgroup classes verified at prime five')
