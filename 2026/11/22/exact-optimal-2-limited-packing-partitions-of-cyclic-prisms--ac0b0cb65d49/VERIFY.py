#!/usr/bin/env python3
"""Standalone exact certificate for closed-neighborhood 2-limited packing colorings of prisms."""
from itertools import product
from collections import Counter

K=3; columns=list(product(range(K),repeat=2)); m=len(columns)**2
edges=[[] for _ in range(m)]
for a, x in enumerate(columns):
    for b,y in enumerate(columns):
        for c,z in enumerate(columns):
            if all(max(Counter((x[r],y[r],y[1-r],z[r])).values())<=2 for r in (0,1)):
                edges[9*a+b].append(9*b+c)

def matrix_traces(upto):
    rows=[{i:1} for i in range(m)]
    traces=[]
    for step in range(1,upto+1):
        new=[]
        for row in rows:
            v={}
            for state,coef in row.items():
                for dest in edges[state]:v[dest]=v.get(dest,0)+coef
            new.append(v)
        rows=new
        traces.append(sum(rows[i].get(i,0) for i in range(m)))
    return traces

def poly_mul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return r

def poly_pow(p,n):
    r=[1]
    for _ in range(n):r=poly_mul(r,p)
    return r

# coefficient arrays are in descending powers of x
factors=[([1,0],39),([1,-1],6),([1,1],2),([1,0,1],1),
         ([1,2,-1],1),([1,1,0,1],2),([1,0,5,0,-4,0,1],2),
         ([1,-6,7,-6,2],1),([1,3,4,3,2],2)]
expected=[1]
for p,e in factors:expected=poly_mul(expected,poly_pow(p,e))
assert len(expected)==m+1
tr=matrix_traces(m)
coeffs=[1]
for k in range(1,m+1):
    s=sum(coeffs[k-j]*tr[j-1] for j in range(1,k+1))
    assert s%k==0
    coeffs.append(-s//k)
assert coeffs==expected,('characteristic polynomial disagrees',coeffs,expected)

def good(colors,n,num_colors):
    for i in range(n):
        for r in range(2):
            entries=[colors[2*i+r],colors[2*i+1-r],colors[2*((i-1)%n)+r],colors[2*((i+1)%n)+r]]
            if max(Counter(entries).values())>2:return False
    return True

for n in [3,4,5]:
    brute=sum(good(seq,n,3) for seq in product(range(3),repeat=2*n))
    assert brute==tr[n-1],(n,brute,tr[n-1])
for n in range(3,11):
    two=sum(good(seq,n,2) for seq in product(range(2),repeat=2*n))
    expected_two=6 if n%4==0 else (2 if n%2==0 else 0)
    assert two==expected_two,(n,two,expected_two)
print('PRISM_2LP_CERTIFICATE_OK',len(edges),sum(map(len,edges)),[(n,tr[n-1]) for n in range(3,12)])
