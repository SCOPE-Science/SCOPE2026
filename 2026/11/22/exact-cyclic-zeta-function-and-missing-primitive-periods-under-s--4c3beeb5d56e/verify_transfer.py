"""Exact transfer-matrix verification for two tandem-square lengths.
Requires Python 3 and SymPy. Run: python verify_transfer.py
"""
from itertools import product
from math import gcd
from sympy import Matrix, Symbol, eye, factor, Poly, trace

words = [''.join(bits) for bits in product('01', repeat=5)]
def legal(s):
    return s[:2] != s[2:4] and s[1:3] != s[3:5] and s[:3] != s[3:6]
E = {(u,u[1:]+a) for u in words for a in '01' if legal(u+a)}

def reachable(u):
    reached={u}; queue=[u]
    for x in queue:
        for a,b in E:
            if a==x and b not in reached:
                reached.add(b); queue.append(b)
    return reached
reach={u:reachable(u) for u in words}
components=[]; unused=set(words)
while unused:
    u=min(unused)
    c={v for v in unused if v in reach[u] and u in reach[v]}
    components.append(c); unused-=c
assert sorted(map(len,components))==[1]*16+[16]
R=sorted(max(components,key=len))
assert R == ['00010','00011','00100','00110','00111','01000','01100','01110',
             '10001','10011','10111','11000','11001','11011','11100','11101']
M=Matrix(16,16,lambda i,j:int((R[i],R[j]) in E))
comp=lambda s: ''.join('1' if c=='0' else '0' for c in s)
reps=[x for x in R if x[0]=='0']; assert len(reps)==8
Bp=Matrix(8,8,lambda i,j:int((reps[i],reps[j]) in E)+int((reps[i],comp(reps[j])) in E))
Bm=Matrix(8,8,lambda i,j:int((reps[i],reps[j]) in E)-int((reps[i],comp(reps[j])) in E))
z=Symbol('z')
P=1-z**2-z**3-z**4+z**6
Q=1+z**2+z**3-z**4-z**6
assert factor((eye(8)-z*Bp).det(method='domain-ge')-P)==0
assert factor((eye(8)-z*Bm).det(method='domain-ge')-Q)==0
assert factor((eye(16)-z*M).det(method='domain-ge')-P*Q)==0
# Full 32-state construction has only the indicated nontrivial recurrent component.
# Complementary states give the two blocks above.
Powers=eye(16); vals={}
for n in range(1,31):
    Powers=Powers*M
    vals[n]=int(trace(Powers))
assert [vals[n] for n in range(1,19)]==[
    0,0,0,12,10,6,0,12,36,50,22,18,78,196,190,124,170,546]
def mobius(k):
    factors=0; p=2
    while p*p<=k:
        if k%p==0:
            k//=p; factors+=1
            if k%p==0:return 0
        p+=1
    if k>1:factors+=1
    return (-1)**factors
def divisors(n):return [d for d in range(1,n+1) if n%d==0]
N={n:sum(mobius(n//d)*vals[d] for d in divisors(n))//n for n in vals}
assert {n for n in range(1,31) if N[n]==0}=={1,2,3,7,8,12}
# An independent exact characteristic factorization; the Perron root is isolated.
x=Symbol('x')
f=Poly(x**6-x**4-x**3-x**2+1,x)
roots=f.nroots(n=40)
positive=[r for r in roots if abs(float(r.as_real_imag()[1]))<1e-25 and float(r.as_real_imag()[0])>1]
assert len(positive)==1 and abs(float(positive[0])-1.401268367939855)<1e-13
print('PASS: 32-state SCC, 16-state graph, 8-state sign factorization,')
print('exact determinant, first 30 marked-period counts, primitive-period gaps, Perron root.')
