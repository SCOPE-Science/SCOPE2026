#!/usr/bin/env python3
"""Exact S6-equivariant negative-support enumeration on a one-nodal cubic resolution.
No external packages. Divisor coordinates in (H,E1,...,E6).
"""
from itertools import combinations, permutations
from collections import Counter,defaultdict
from math import lcm
import json,math

P=list(combinations(range(6),2))
# 22 negative curves: E0..E5, L_ij (indices 6..20), Q (index 21).
C=[]
for i in range(6):
    d=[0]*7;d[1+i]=1;C.append(tuple(d))
for i,j in P:
    d=[1]+[0]*6;d[1+i]=d[1+j]=-1;C.append(tuple(d))
C.append(tuple([2]+[-1]*6))
assert len(C)==22

def dot(a,b):return a[0]*b[0]-sum(a[k]*b[k] for k in range(1,7))
assert [dot(C[i],C[i]) for i in range(22)]==[-1]*21+[-2]
assert {dot(C[i],C[j]) for i,j in combinations(range(22),2)}=={0,1}

# Pairwise intersecting sets of edges of K6.
Ls=[s for k in range(6) for s in combinations(range(15),k)
    if all(set(P[i])&set(P[j]) for i,j in combinations(s,2))]
assert len(Ls)==192, len(Ls)  # pairwise-intersecting edge sets: 1,15,60,80,30,6.
# For each selected L_ij, allowed E's are precisely those not among line endpoints.
# Q may be present only if <= 1 exceptional E is selected.
S=[]
for lines in Ls:
    touched=set().union(*(set(P[k]) for k in lines)) if lines else set()
    free=sorted(set(range(6))-touched)
    for k in range(len(free)+1):
        for es in combinations(free,k):
            base=tuple(sorted(list(es)+[6+t for t in lines]))
            S.append(base)
            if len(es)<=1:S.append(tuple(sorted(base+(21,))))
S=sorted(set(S),key=lambda z:(len(z),z))
N=len(S);hist=[sum(len(s)==k for s in S) for k in range(7)]
print('CHAMBERS',N,'POLYNOMIAL',hist,flush=True)
assert hist==[1,22,156,490,725,447,57] and N==1898, (hist,N)
assert sum(21 in s for s in S)==648

# Exact Sylvester criterion: determinant sign (-1)^k for Gram leading principal kxk.
def det(M):
    n=len(M)
    if not n:return 1
    A=[list(map(int,r)) for r in M]
    prev=1;sign=1
    for k in range(n-1):
        if A[k][k]==0:
            j=next((j for j in range(k+1,n) if A[j][k]!=0),None)
            if j is None:return 0
            A[j],A[k]=A[k],A[j];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                assert num%prev==0
                A[i][j]=num//prev
        for i in range(k+1,n): A[i][k]=0
        prev=pivot
    return sign*A[-1][-1]
for s in S:
    for k in range(1,len(s)+1):
        d=det([[dot(C[i],C[j]) for j in s[:k]] for i in s[:k]])
        assert (-1)**k*d>0,(s,k,d)
print('SYLVESTER_ALL_SUPPORTS_OK',flush=True)

# S6 acts by reindexing exceptional points, L pairs, fixing Q.
index={p:i for i,p in enumerate(P)}
def action(sigma):return tuple(list(sigma)+[6+index[tuple(sorted((sigma[i],sigma[j])))] for i,j in P]+[21])
G=[tuple(p) for p in permutations(range(6))]
assert len(G)==720
Z=[sum(1<<i for i in s) for s in S]
Sindex={m:i for i,m in enumerate(Z)}
assert len(Sindex)==1898

def ctype(sigma):
    seen=set();cc=[]
    for i in range(6):
        if i in seen:continue
        j=i;k=0
        while j not in seen:seen.add(j);k+=1;j=sigma[j]
        cc.append(k)
    return tuple(sorted(cc,reverse=True))

def cycletype_action(pi):
    seen=set();cnt=Counter()
    for i in range(len(pi)):
        if i in seen:continue
        j=i;k=0
        while j not in seen:seen.add(j);k+=1;j=pi[j]
        cnt[k]+=1
    return dict(sorted(cnt.items()))
records=[]
for part in sorted(set(ctype(p) for p in G),key=lambda x:(len(x),x),reverse=True):
    p=next(p for p in G if ctype(p)==part)
    a=action(p)
    im=[Sindex[sum(1<<a[i] for i in s)] for s in S]
    orbitprof=cycletype_action(im)
    fixed=[s for idx,s in enumerate(S) if im[idx]==idx]
    counts=[sum(len(s)==k for s in fixed) for k in range(7)]
    qcounts=[sum(len(s)==k and 21 in s for s in fixed) for k in range(7)]
    records.append({'cycle_type':list(part),'class_size':sum(ctype(x)==part for x in G),
                    'order':math.lcm(*part),'representative':list(p),
                    'chamber_cycles':orbitprof,'fixed_chambers':len(fixed),
                    'fixed_support_size_profile':counts,'fixed_with_exceptional_minus_two':qcounts})
records.sort(key=lambda r:(r['order'],r['cycle_type']))
for r in records:print('CASE',r['cycle_type'],'size',r['class_size'],'fixed',r['fixed_chambers'],'sizes',r['fixed_support_size_profile'],'Q',r['fixed_with_exceptional_minus_two'],'orbits',r['chamber_cycles'])
assert len(records)==11
burnside=sum(r['class_size']*r['fixed_chambers'] for r in records)
assert burnside%720==0
print('BURNSIDE',burnside//720)
# Directly compute orbit partition under adjacent transpositions.
generators=[]
for i in range(5):
    p=list(range(6));p[i],p[i+1]=p[i+1],p[i];generators.append(action(p))
visited=set();orbits=[]
for idx in range(len(S)):
    if idx in visited:continue
    q=[idx];visited.add(idx)
    for vi in q:
        s=S[vi]
        for g in generators:
            ni=Sindex[sum(1<<g[i] for i in s)]
            if ni not in visited:visited.add(ni);q.append(ni)
    orbits.append(len(q))
assert len(orbits)==burnside//720
print('DIRECT_ORBITS',len(orbits),sorted(orbits))
with open('nodal_cubic_chambers_results.json','w') as f:
    json.dump({'negative_curves':22,'total':N,'support_polynomial':hist,'with_minus_two':648,
              'symmetry_group_order':720,'orbit_count':len(orbits),'orbit_sizes':sorted(orbits),
              'cases':records},f,indent=2)
print('NODAL_CUBIC_FROBENIUS_ZARISKI_CHAMBERS_EXACT_OK')
