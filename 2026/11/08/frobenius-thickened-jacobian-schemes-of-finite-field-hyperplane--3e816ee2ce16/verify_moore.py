#!/usr/bin/env python3
"""Exact finite-field checks for the singular-scheme theorem (stdlib only).

These finite checks corroborate, but do not replace, the general proof.
"""
import itertools
from math import prod

def plus(a,b,p):
    z = a.copy()
    for m,c in b.items():
        v = (z.get(m,0)+c)%p
        if v: z[m]=v
        elif m in z: del z[m]
    return z

def mul(a,b,p):
    o={}
    for m,c in a.items():
        for n,d in b.items():
            r=tuple(i+j for i,j in zip(m,n));v=(o.get(r,0)+c*d)%p
            if v:o[r]=v
            elif r in o:del o[r]
    return o

def determinant_power_matrix(cols,exponents,p,N):
    out={}
    for perm in itertools.permutations(range(len(cols))):
        inv=sum(perm[i]>perm[j] for i in range(len(cols)) for j in range(i+1,len(cols)))
        sign=(-1)**inv
        ex=[0]*N
        for row,colidx in enumerate(perm):ex[cols[colidx]]+=exponents[row]
        out=plus(out,{tuple(ex):sign%p},p)
    return out

def deriv(poly,k,p):
    out={}
    for m,c in poly.items():
        if m[k]%p:
            n=list(m);n[k]-=1
            out[tuple(n)]=c*(m[k]%p)%p
    return out

def factor_product(p,N):
    n=N
    a={(0,)*N:1}
    count=0
    for c in itertools.product(range(p),repeat=N):
        if not any(c):continue
        if c[next(i for i,z in enumerate(c) if z) ]!=1: continue
        linear={tuple(1 if j==i else 0 for j in range(n)):z for i,z in enumerate(c) if z}
        a=mul(a,linear,p);count+=1
    return a,count

def gauss2(N,q):
    return (q**N-1)*(q**(N-1)-1)//((q**2-1)*(q-1))

def local_tangent_check(N,p,D):
    # At [1:0:0], two Moore minors vanish simply, independently.
    if N!=3:return None
    grads=[]
    for poly in D:
        grads.append([poly.get(tuple([0,1,0]),0),poly.get(tuple([0,0,1]),0)])
    # The first coordinate has x0=1; terms with x0^a times x1/x2 also matter.
    grads=[]
    for poly in D:
        grads.append([sum(c for e,c in poly.items() if e[1]==1 and e[2]==0)%p,
                      sum(c for e,c in poly.items() if e[1]==0 and e[2]==1)%p])
    assert any((u[0]*v[1]-u[1]*v[0])%p for u,v in itertools.combinations(grads,2))
    return grads

for p,N in [(2,3),(3,3),(2,4)]:
    q=p;d=(q**(N-1)-1)//(q-1)
    F=determinant_power_matrix(list(range(N)),[q**j for j in range(N)],p,N)
    D=[determinant_power_matrix([j for j in range(N) if j!=i],[q**j for j in range(N-1)],p,N) for i in range(N)]
    for i in range(N):
        rhs={tuple(q*e for e in m): ((-1)**i*c)%p for m,c in D[i].items()}
        assert deriv(F,i,p)==rhs, (p,N,i)
    factors,k=factor_product(p,N)
    assert k==(q**N-1)//(q-1)
    # Moore determinant may be normalized by an invertible scalar.
    assert F==factors or F=={m:(-c)%p for m,c in factors.items()}
    degree_by_resolution=(d*d+sum(q**(2*j) for j in range(N-1)))//2
    assert degree_by_resolution==gauss2(N,q)
    deg_frob=q*q*degree_by_resolution
    tang=local_tangent_check(N,p,D)
    print(f"q={q}, N={N}: determinant identity, {k} hyperplane factors, {N} gradient/minor identities PASS")
    print(f"  reduced degree={degree_by_resolution}, Frobenius thickening degree={deg_frob}, tangent={tang}")
print('ALL_EXACT_CHECKS_PASSED')

def gf8mul(a,b):
    v=0
    while b:
        if b&1:v^=a
        b>>=1
        a<<=1
        if a&8:a^=0b1011
    return v

def gf8pow(a,n):
    z=1
    while n:
        if n&1:z=gf8mul(z,a)
        a=gf8mul(a,a);n>>=1
    return z

def geval(poly,coords):
    out=0
    for exp,c in poly.items():
        if c%2:
            z=1
            for x,e in zip(coords,exp):z=gf8mul(z,gf8pow(x,e))
            out^=z
    return out

def binary_rank(vals):
    basis=[]
    for v in vals:
        x=v
        for u in basis:x=min(x,x^u)
        if x:
            basis.append(x);basis.sort(reverse=True)
    # standard high-pivot elimination is simpler for n=3
    s={0}
    for v in vals:s|={x^v for x in list(s)}
    return (len(s)-1).bit_length()

p=2;N=4;q=2
D=[determinant_power_matrix([j for j in range(N) if j!=i],[q**j for j in range(N-1)],p,N) for i in range(N)]
counts={1:0,2:0,3:0}
for z in itertools.product(range(8),repeat=4):
    if z==(0,0,0,0):continue
    first=next(a for a in z if a)
    scale=gf8pow(first,6)
    v=tuple(gf8mul(scale,a) for a in z)
    if v!=z:continue
    rank=binary_rank(z)
    assert rank in counts
    counts[rank]+=1
    singular=all(geval(D[i],z)==0 for i in range(N))
    assert singular==(rank<=2), (z,rank,singular)
assert sum(counts.values())==(8**4-1)//7
# At rank-two point [1,alpha,0,0], the two transverse minor gradients are independent.
pt=(1,2,0,0)
G=[[geval(deriv(f,i,2),pt) for i in (2,3)] for f in D]
assert any(gf8mul(u[0],v[1])^gf8mul(u[1],v[0]) for u,v in itertools.combinations(G,2))
print(f'q=2, N=4 over F8: all 585 projective points checked; ranks {counts}; rank-two transverse gradients {G}')
print('ALL_EXTENDED_GEOMETRY_CHECKS_PASSED')
