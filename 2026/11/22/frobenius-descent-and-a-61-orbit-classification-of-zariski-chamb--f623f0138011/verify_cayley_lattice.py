"""Exact intersection-lattice verification of the Cayley cubic chamber table.
No third-party packages. Python 3 standard library only.
"""
from itertools import combinations, permutations
from collections import Counter

V=range(4)
edges=list(combinations(V,2))
pairs=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
# A divisor class (degree, six multiplicities) denotes d H - sum m E.
classes=[]
for i in V:
    classes.append((1,[int(i in e) for e in edges]))
for e in edges:
    classes.append((0,[-int(e==f) for f in edges]))
for matching in pairs:
    classes.append((1,[int(e in matching) for e in edges]))
n=len(classes)
assert n==13
I=[[x[0]*y[0]-sum(a*b for a,b in zip(x[1],y[1]))
    for y in classes] for x in classes]
assert sorted(I[i][i] for i in range(n))==[-2]*4+[-1]*9
assert set(I[i][j] for i in range(n) for j in range(n) if i!=j)=={0,1}

def determinant(A):
    """Fraction-free exact elimination; a zero pivot is harmless (return 0)."""
    m=len(A)
    if m==0: return 1
    B=[list(map(int,r)) for r in A]
    sign=1; prev=1
    for k in range(m-1):
        if B[k][k]==0:
            j=next((j for j in range(k+1,m) if B[j][k]!=0),None)
            if j is None:return 0
            B[k],B[j]=B[j],B[k]
            sign=-sign
        pivot=B[k][k]
        for i in range(k+1,m):
            for j in range(k+1,m):
                num=B[i][j]*pivot-B[i][k]*B[k][j]
                assert num%prev==0
                B[i][j]=num//prev
        for i in range(k+1,m):B[i][k]=0
        prev=pivot
    return sign*B[-1][-1]

nd=[False]*(1<<n);nd[0]=True
for mask in range(1,1<<n):
    leading=mask.bit_length()-1
    old=mask ^ (1<<leading)
    if not nd[old]:continue
    idx=[i for i in range(n) if mask>>i&1]
    mat=[[I[i][j] for j in idx] for i in idx]
    nd[mask]=(-1)**len(idx)*determinant(mat)>0
valid={mask for mask in range(1<<n) if nd[mask]}
assert len(valid)==726
assert tuple(Counter(x.bit_count() for x in valid)[k] for k in range(7))==(1,13,69,186,260,168,29)

def cycle_type(p):
    vis=set();ls=[]
    for i in V:
        if i in vis:continue
        cur=i;z=0
        while cur not in vis:
            vis.add(cur);z+=1;cur=p[cur]
        ls.append(z)
    return tuple(sorted(ls,reverse=True))

expected={
 (1,1,1,1):(1,13,69,186,260,168,29),
 (2,1,1):(1,5,11,16,16,12,5),
 (2,2):(1,5,9,18,16,20,5),
 (3,1):(1,1,0,3,2,0,2),
 (4,):(1,1,1,0,2,2,1)}
counts=Counter()
for p in permutations(V):
    a=list(p)
    a.extend(4+edges.index(tuple(sorted((p[i],p[j])))) for i,j in edges)
    for matching in pairs:
        moved=tuple(sorted(tuple(sorted(p[i] for i in e)) for e in matching))
        a.append(10+next(i for i,m in enumerate(pairs) if tuple(sorted(m))==moved))
    assert sorted(a)==list(range(n))
    assert all(I[i][j]==I[a[i]][a[j]] for i in range(n) for j in range(n))
    fixed=Counter()
    for mask in valid:
        moved=sum(1<<a[i] for i in range(n) if mask>>i&1)
        if moved==mask: fixed[mask.bit_count()]+=1
    cy=cycle_type(p)
    assert tuple(fixed[i] for i in range(7))==expected[cy]
    counts[cy]+=1
assert counts=={(1,1,1,1):1,(2,1,1):6,(2,2):3,(3,1):8,(4,):6}
print('INTERSECTION_MATRIX_SUPPORTS',len(valid),'TOTAL_TYPES',dict(counts))
print('CAYLEY_CHAMBERS_LATTICE_EXACT_OK')
