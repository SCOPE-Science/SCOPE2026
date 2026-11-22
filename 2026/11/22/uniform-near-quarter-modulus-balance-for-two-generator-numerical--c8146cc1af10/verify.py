"""Independent finite checks for modular gap-residue balance theorem.

Uses direct dynamic programming for the gap set and a separate cyclic recurrence.
The mathematical proof in RESULT.md applies for all parameters.
"""
from math import gcd, ceil
from itertools import product

def cyclic_histogram(a, b, m):
    assert a > 1 and b > 1 and m >= 2 and gcd(a,b)==1 and gcd(a*b,m)==1
    s, t = a%m, b%m
    ti=pow(t,-1,m)
    differences=[0]*m
    z=0
    for j in range(1,m):
        r=(j*s)%m
        z += (r<s) - ((ti*r)%m < s)
        differences[j]=z
    genus=(a-1)*(b-1)//2
    assert (genus-sum(differences))%m == 0
    baseline=(genus-sum(differences))//m
    hist=[0]*m
    for j in range(m): hist[(j*s)%m]=baseline+differences[j]
    return hist

def brute_histogram(a,b,m):
    F=a*b-a-b
    representable=bytearray(F+1)
    representable[0]=1
    for n in range(F+1):
        if representable[n]:
            if n+a<=F: representable[n+a]=1
            if n+b<=F: representable[n+b]=1
    hist=[0]*m
    for n in range(1,F+1):
        if not representable[n]:hist[n%m]+=1
    return hist

cases=0
for a in range(2,55):
 for b in range(a+1,65):
  if gcd(a,b)>1: continue
  for m in range(2,23):
   if gcd(a*b,m)>1: continue
   h=cyclic_histogram(a,b,m)
   assert h==brute_histogram(a,b,m),(a,b,m,h,brute_histogram(a,b,m))
   assert max(h)-min(h) <= (m+3)//4
   cases+=1

# Independently assess the finite cyclic-recurrence bound for all residue pairs,
# and the explicit diagonal construction across many moduli.
residue_cases=0
for m in range(2,181):
    units=[s for s in range(1,m) if gcd(s,m)==1]
    for s in units:
        first=[int((j*s)%m<s) for j in range(1,m+1)]
        for t in units:
            ti=pow(t,-1,m)
            z=lo=hi=0
            for j in range(1,m+1):
                z += first[j-1]-int((ti*s*j)%m<s)
                lo=min(lo,z);hi=max(hi,z)
            assert z==0
            assert hi-lo <= (m+3)//4
            residue_cases+=1
    # Valid lower-bound witness selection
    if m==2: s=1
    elif m==3: s=2
    elif m==4: s=3
    elif m==6: s=5
    elif m%2: s=(m-1)//2
    else: s=2*(m//4)-1
    assert gcd(s,m)==1,(m,s)
    expected= (m+1)//4
    actual=ceil((s-1)*(m-s)/m)
    assert actual==expected,(m,s,actual,expected)
    a,b=s+m,s+2*m
    h=cyclic_histogram(a,b,m)
    assert max(h)-min(h)==expected,(m,s,actual,h)

print('PASS: direct semigroup-versus-cyclic counts',cases)
print('PASS: residue pair tests',residue_cases)
print('PASS: diagonal witnesses for every modulus in [2,180]')
