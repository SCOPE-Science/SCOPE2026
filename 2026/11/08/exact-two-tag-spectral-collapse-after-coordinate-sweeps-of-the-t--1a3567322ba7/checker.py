"""Independent finite-state checks for two labelled cards in binary coordinate sweeps."""
from collections import defaultdict
from fractions import Fraction

checks=0

def check(statement):
    global checks
    checks+=1
    assert statement

def sweep(d, initial):
    law={initial:Fraction(1)}
    for i in range(d):
        bit=1<<i
        new=defaultdict(Fraction)
        for (x,y),prob in law.items():
            if (x^y)==bit:
                new[x,y]+=prob/2
                new[x^bit,y^bit]+=prob/2
            else:
                for xx in (x,x^bit):
                    for yy in (y,y^bit):
                        new[xx,yy]+=prob/4
        law=dict(new)
    return law

def direct_step(d,law):
    out=defaultdict(Fraction)
    for state,p in law.items():
        for next_state,prob in sweep(d,state).items():
            out[next_state]+=p*prob
    return dict(out)

def predicted_one(d,j,x,y):
    n=1<<d
    z=x^y
    if z==0:return Fraction(0)
    if z&((1<<(j-1))-1):return Fraction(1,n*n)
    return Fraction(2,n*n) if z&(1<<(j-1)) else Fraction(0)

for d in range(1,6):
    n=1<<d
    for z in range(1,n):
        j=z.bit_length()
        law=sweep(d,(0,z))
        for x in range(n):
            for y in range(n):
                check(law.get((x,y),0)==predicted_one(d,j,x,y))
        for k in range(1,d+1):
            pk=sum((p for (x,y),p in law.items() if (x^y).bit_length()==k),Fraction(0))
            check(pk==Fraction((1<<(k-1))+(k==j),n))
        tv=sum((abs(law.get((x,y),0)-Fraction(1,n*(n-1))) for x in range(n) for y in range(n) if x!=y),Fraction(0))/2
        check(tv==Fraction(n-2,(1<<j)*(n-1)))
    print('One-sweep exact checks passed: dimension',d)

# Independently compose actual two-sweep transition laws for all starts, dimensions <=3.
for d in range(1,4):
    n=1<<d
    for x in range(n):
        for y in range(n):
            if x==y:continue
            j=(x^y).bit_length()
            first=sweep(d,(x,y))
            second=direct_step(d,first)
            for u in range(n):
                for v in range(n):
                    if u==v:continue
                    U=Fraction(1,n*(n-1))
                    want=U+(first.get((u,v),0)-U)/n
                    check(second.get((u,v),0)==want)
    print('Actual two-sweep Chapman-Kolmogorov checks passed: dimension',d)
print('PASS:',checks,'exact rational equalities')
