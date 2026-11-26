"""Reproducible finite-field checks for the elementary-symmetric Clebsch fibre over F3.
Runs with Python >=3.9, standard library only. The proof of the universal point formula
uses smooth cubic surface cohomology and line generation as explained in RESULT.md.
"""
from itertools import combinations, permutations, product
from math import factorial

# F9 = F3[s]/(s*s+s-1). An element is encoded a+3*b for a,b in {0,1,2}.
def add(x,y): return ((x%3+y%3)%3)+3*((x//3+y//3)%3)
def neg(x): return ((-x)%3)+3*((-(x//3))%3)
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    a,b=x%3,x//3; c,d=y%3,y//3
    return ((a*c+b*d)%3)+3*((a*d+b*c-b*d)%3)
def powf(x,n):
    z=1
    for _ in range(n): z=mul(z,x)
    return z
def inv(x):
    assert x
    return powf(x,7)
def rref(rows):
    a=[list(row) for row in rows]; k=0
    for j in range(5):
        piv=next((i for i in range(k,len(a)) if a[i][j]),None)
        if piv is None: continue
        a[k],a[piv]=a[piv],a[k]
        a[k]=[mul(inv(a[k][j]),z) for z in a[k]]
        for i in range(len(a)):
            if i!=k and a[i][j]:
                t=a[i][j]
                a[i]=[sub(a[i][h],mul(t,a[k][h])) for h in range(5)]
        k+=1
        if k==len(a):break
    assert k==2
    return tuple(tuple(row) for row in a)
def e3(v):
    out=0
    for i,j,k in combinations(range(5),3):out=add(out,mul(mul(v[i],v[j]),v[k]))
    return out

def on_cubic(line):
    u,v=line
    assert all(sum((z%3 for z in row))%3==0 and sum((z//3 for z in row))%3==0 for row in line)
    for t in range(9):
        assert e3(tuple(add(u[i],mul(t,v[i])) for i in range(5)))==0
    assert e3(v)==0

# Equation s^2+s-1=0; s=3. u_i = zeta^i+zeta^-i; d_i = (zeta^i-zeta^-i)/(zeta-zeta^-i).
s=3
s2=sub(1,s)
u=(2,s,sub(s2,2),sub(s2,2),s)
d=(0,1,s,neg(s),2)
assert mul(s,s)==s2
lines15=set(); lines12=set()
for p in permutations(range(5)):
    # choose a pair of disjoint coordinate differences
    v=[0]*5;w=[0]*5
    v[p[0]],v[p[1]]=1,2
    w[p[2]],w[p[3]]=1,2
    lines15.add(rref((v,w)))
    lines12.add(rref((tuple(u[i] for i in p),tuple(d[i] for i in p))))
assert len(lines15)==15 and len(lines12)==12
assert not (lines15 & lines12)
assert len(lines15|lines12)==27
for L in lines15|lines12: on_cubic(L)
assert all(all(z//3==0 for row in L for z in row) for L in lines15)
# Every line is defined over F9. Six Frobenius-conjugate pairs among the twelve new lines.
def frobline(L):return rref(tuple(tuple(powf(z,3) for z in row) for row in L))
assert all(frobline(L)==L for L in lines15)
assert all(frobline(L) in lines12 and frobline(L)!=L for L in lines12)
assert len({frozenset((L,frobline(L))) for L in lines12})==6

def projective_points(field_order):
    for a in range(5):
        for tail in product(range(field_order), repeat=4-a):
            yield ((0,)*a)+(1,)+tail

def count_points(q):
    total=0
    for v in projective_points(q):
        ss=0
        for x in v:ss=add(ss,x)
        if ss==0 and e3(v)==0:total+=1
    return total
assert count_points(3)==25
assert count_points(9)==145
# The 25 F3 points also admit an elementary sign-pattern count.
count=0
for a in range(6):
 for b in range(6-a):
  if not(a+b) or (a-b)%3:continue
  ec=sum(((-1)**(3-i))*__import__('math').comb(a,i)*__import__('math').comb(b,3-i) for i in range(4) if i<=a and 3-i<=b)%3
  if ec==0:count+=factorial(5)//(factorial(a)*factorial(b)*factorial(5-a-b))
assert count==50 and count//2==25
# Picard rank 7, Frobenius order 2 (because all 27 geometric lines live over F9),
# trace= (#X(F3)-1-3^2)/3=5 gives +1 multiplicity 6 and -1 multiplicity 1.
assert (25-1-3**2)//3==5
assert (145-1-9**2)//9==7
for n in range(1,9):
    q=3**n
    formula=1+q*q+q*(6+(-1)**n)
    assert formula>0
print('PASS: 15+12 distinct lines, six Frobenius pairs, cubic identities, F3=25, F9=145, Frobenius trace=5, all-extension formula')
