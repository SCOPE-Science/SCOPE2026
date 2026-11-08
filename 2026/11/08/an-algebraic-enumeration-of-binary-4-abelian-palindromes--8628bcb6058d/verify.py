"""Exact symbolic and independent finite checks for binary 4-abelian palindromes.
Run: python verify.py (requires SymPy)."""
from itertools import product
from collections import Counter
import sympy as sp

z,t=sp.symbols('z t')
states=[''.join(b) for b in product('01',repeat=3)]
M=sp.zeros(8)
for i,a in enumerate(states):
    for b in '01':
        four=a+b
        weight=t if four=='0011' else (1/t if four=='1100' else 1)
        M[i,states.index(four[1:])]=weight
B=sp.eye(8)-z*M
u=2-t-1/t
D=1-2*z+u*z**6
assert sp.factor(B.det()-D)==0
R=sum(B.inv(method='DM')[i,states.index(a[::-1])] for i,a in enumerate(states))
R_expected=(4-4*z-8*z**3-2*u*z**5+4*u*z**6)/D
assert sp.factor(R-R_expected)==0
G=2*z+4*z**3+(2*z**2-4*z**3+4*z**4-8*z**6)/sp.sqrt((1-2*z)*(1-2*z+4*z**6))
coeff=[int(sp.expand(sp.series(G,z,0,17).removeO()).coeff(z,n)) for n in range(1,17)]
assert coeff==[2,2,4,4,8,8,16,28,56,104,192,368,704,1356,2608,5032],coeff
num_checked=0
for n in range(1,17):
    total=0
    for tup in product('01',repeat=n):
        w=''.join(tup)
        rev=w[::-1]
        # Independently compute all factor frequencies of lengths <=4.
        is_pal=all(Counter(w[i:i+k] for i in range(n-k+1)) ==
                   Counter(rev[i:i+k] for i in range(n-k+1))
                   for k in range(1,min(4,n)+1))
        if n>=3:
            boundary=(w[:3]==rev[:3])
            imbalance=sum(w[i:i+4]=='0011' for i in range(n-3)) - sum(w[i:i+4]=='1100' for i in range(n-3))
            assert is_pal==(boundary and imbalance==0),(n,w,is_pal,boundary,imbalance)
        total+=is_pal
        num_checked+=1
    assert total==coeff[n-1],(n,total,coeff[n-1])
print('VERIFY_OK symbolic_det_trace_gf, finite_n=1..16, words=',num_checked,'coefs=',coeff)
