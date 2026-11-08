from fractions import Fraction
from itertools import product
from math import comb

def formula_maws(a,b,c):
    assert a>=0 and b>=1 and c>=0
    A=max(a,b); B=max(b,c); L=max(a,b,c); K=min(A,B)
    r={'0'*(L+1)}
    r.update('1'+'0'*k+'1' for k in range(K+1) if k!=b)
    if L>A:r.add('0'*(A+1)+'1')
    if L>B:r.add('1'+'0'*(B+1))
    if a<b and c<b:r.add('0'*(a+1)+'1'+'0'*(c+1))
    if a>b and c>b:r.add('0'*(b+1)+'1'+'0'*(b+1))
    if a<b<=c:r.add('0'*(a+1)+'1'+'0'*b+'1')
    if c<b<=a:r.add('1'+'0'*b+'1'+'0'*(c+1))
    if a>=b and c>=b:r.add('1'+'0'*b+'1'+'0'*b+'1')
    return r

def direct_maws(s):
    f={''}
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):f.add(s[i:j])
    return {x+ch for x in f for ch in '01' if x+ch not in f and (x+ch)[1:] in f}

N=45
count=0
for n in range(3,N+1):
    for b in range(1,n-1):
        for a in range(n-b-1):
            c=n-b-a-2
            s='0'*a+'1'+'0'*b+'1'+'0'*c
            p=formula_maws(a,b,c)
            d=direct_maws(s)
            assert p==d,(n,a,b,c,p-d,d-p)
            count+=1
print('FORMULA_SET_ALL_PASS',count,'word parameters, n 3..',N)
# samples for random n 46..300, boundary / regime mixes
import random
rng=random.Random(1729)
for _ in range(1000):
    n=rng.randrange(46,301)
    b=rng.randrange(1,n-1)
    a=rng.randrange(0,n-b-1)
    c=n-b-a-2
    s='0'*a+'1'+'0'*b+'1'+'0'*c
    assert formula_maws(a,b,c)==direct_maws(s),(n,a,b,c)
print('SAMPLE_SET_PASS',1000)
# finite distribution moments for conditional two nonadjacent ones
for n in [10,30,100,300,700]:
    tot=0; tot2=0; nn=0
    for b in range(1,n-1):
        for a in range(n-b-1):
            c=n-b-a-2
            m=len(formula_maws(a,b,c))
            tot+=m;tot2+=m*m;nn+=1
    assert nn==comb(n-1,2)
    mean=Fraction(tot,nn)
    var=Fraction(tot2,nn)-mean**2
    print('n',n,'mean/n',float(mean/n),'var/n2',float(var/n**2))
print('LIMIT_EXPECT',float(Fraction(7,18)),'LIMIT_VAR',float(Fraction(25,648)))
