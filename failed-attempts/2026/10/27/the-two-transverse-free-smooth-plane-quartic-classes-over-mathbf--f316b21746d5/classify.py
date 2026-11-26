"""Exact finite-field classification of transverse-free smooth plane quartics over GF(2).
Python 3 standard library. No external data required.
"""
from itertools import product
from collections import Counter

M=[(i,j,4-i-j) for i in range(5) for j in range(5-i)]
P=[v for v in product((0,1), repeat=3) if any(v)]
L=[]
for n in P:
    basis=[p for p in P if sum(a*b for a,b in zip(n,p))%2==0]
    assert len(basis)==3
    L.append((n,basis[0],basis[1]))

def pmul(a,b):
    r=0
    for i in range(5):
        if a>>i&1:
            for j in range(5-i):
                if b>>j&1: r^=1<<(i+j)
    return r

def restrict_monomial(m, u, v):
    t=1
    for k,e in enumerate(m):
        for _ in range(e):t=pmul(t,u[k]|v[k]<<1)
    return t

R=[[restrict_monomial(m,u,v) for m in M] for n,u,v in L]

def poly_rem(a,b):
    while a and a.bit_length()>=b.bit_length():
        a ^= b<<(a.bit_length()-b.bit_length())
    return a

def poly_gcd(a,b):
    while b:
        a,b=b,poly_rem(a,b)
    return a

def transverse(binary):
    # binary coefficient j multiplies u^(4-j) v^j
    # t=u/v, so coefficient j is coefficient of t^(4-j).
    # polynomial ascending: bit i <- binary bit(4-i)
    a=sum(((binary>>j)&1) << (4-j) for j in range(5))
    # coefficient of t^3 and t determine derivative in char 2
    deriv=sum(((a>>i)&1) <<(i-1) for i in (1,3))
    # infinity has multiplicity 4-deg(a), so degree >=3 necessary
    return a.bit_length()>=4 and deriv!=0 and poly_gcd(a,deriv)==1

def restrict(mask, which):
    q=0
    for j,z in enumerate(R[which]):
        if mask>>j&1:q^=z
    return q

def evalmon(m, p):return int(all(v==1 or e==0 for v,e in zip(p,m)))
E=[sum(evalmon(m,p)<<i for i,m in enumerate(M)) for p in P]
G=[[sum(((m[k]%2)*evalmon(tuple(e-int(a==k) for a,e in enumerate(m)),p))<<i for i,m in enumerate(M)) for k in range(3)] for p in P]

def rat_smooth(mask):
    for value,gr in zip(E,G):
        if (mask&value).bit_count()%2==0 and all((mask&t).bit_count()%2==0 for t in gr):
            return False
    return True

def point_count(mask):return sum((mask&t).bit_count()%2==0 for t in E)

def mat_mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3))%2 for j in range(3)) for i in range(3))

def invertible(MAT):
    a=[list(row) for row in MAT]; r=0
    for c in range(3):
        piv=next((i for i in range(r,3) if a[i][c]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        for i in range(3):
            if i!=r and a[i][c]:a[i]=[x^y for x,y in zip(a[i],a[r])]
        r+=1
    return r==3

def mul3(f,g):
    ans=set()
    for p in f:
        for q in g:
            k=tuple(i+j for i,j in zip(p,q))
            if k in ans:ans.remove(k)
            else:ans.add(k)
    return ans

def change(mask,A):
    forms=[{tuple(int(k==j) for k in range(3)) for j in range(3) if A[i][j]} for i in range(3)]
    v={}
    for i,m in enumerate(M):
        if mask>>i&1:
            curr={(0,0,0)}
            for j,k in enumerate(m):
                for _ in range(k):curr=mul3(curr,forms[j])
            for key in curr:v[key]=1-v.get(key,0)
    return sum((v.get(m,0)<<i) for i,m in enumerate(M))

if __name__=='__main__':
    import json
    totals=Counter();rat=Counter();S=[]
    for m in range(1,32768):
        k=sum(transverse(restrict(m,i)) for i in range(7))
        totals[k]+=1
        if rat_smooth(m):
            rat[k]+=1
            if k==0:S.append(m)
    assert len(S)==25
    assert Counter(point_count(m) for m in S)=={7:24,0:1}
    matrices=[tuple(tuple((bits>>(3*i+j))&1 for j in range(3)) for i in range(3)) for bits in range(512)]
    GL=[m for m in matrices if invertible(m)]
    assert len(GL)==168
    seen=set();orbits=[]
    for m in S:
        if m in seen:continue
        orbit={change(m,g) for g in GL}
        assert orbit.issubset(S)
        orbits.append({'representative':m,'size':len(orbit),'point_count':point_count(m),'stabilizer':168//len(orbit)})
        seen.update(orbit)
    assert len(seen)==25 and sorted(o['size'] for o in orbits)==[1,24]
    print(json.dumps({'monomials':M,'raw_transverse_line_histogram':dict(sorted(totals.items())),
       'rationally_smooth_histogram':dict(sorted(rat.items())),'zero_transverse_candidates':sorted(S),
       'point_count_histogram':dict(Counter(point_count(m) for m in S)),'orbit_data':orbits,
       'special_restrictions':[restrict(20181,i) for i in range(7)]},indent=2))
