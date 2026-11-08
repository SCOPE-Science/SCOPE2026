#!/usr/bin/env python3
"""Exact characteristic-free combinatorial checks for 5-cycle del Pezzo boundaries."""
from itertools import combinations, permutations
from math import prod

# Picard basis (H,E1,E2,E3,E4), classes are dH-sum m_i E_i.
curves=[]
for i in range(4):
    v=[0]*5; v[i+1]=-1; curves.append((f'E{i+1}',tuple(v)))
for i,j in combinations(range(4),2):
    v=[1]+[0]*4; v[i+1]=v[j+1]=1
    curves.append((f'L{i+1}{j+1}',tuple(v)))

def pair(v,w): return v[0]*w[0]-sum(a*b for a,b in zip(v[1:],w[1:]))
def det(M):
    M=[list(row) for row in M]; n=len(M); out=1
    # Fraction-free Bareiss with pivot swaps.
    d=1
    for i in range(n-1):
        if M[i][i]==0:
            k=next((k for k in range(i+1,n) if M[k][i]),None)
            assert k is not None
            M[i],M[k]=M[k],M[i];out=-out
        pivot=M[i][i]
        for j in range(i+1,n):
            for k in range(i+1,n): M[j][k]=(M[j][k]*pivot-M[j][i]*M[i][k])//d
        for j in range(i+1,n):M[j][i]=0
        d=pivot
    return out*M[-1][-1]

assert all(pair(v,v)==-1 for _,v in curves)
P=[]
for start in range(10):
 for p in permutations([j for j in range(10) if j!=start],4):
    seq=(start,)+p
    if all(pair(curves[seq[i]][1],curves[seq[j]][1])==int((i-j)%5 in (1,4))
           for i in range(5) for j in range(i+1,5)):
        P.append(seq)
assert len(P)==120, len(P) # each of twelve pentagons with 10 orientations
assert len({frozenset(s) for s in P})==12
for s in P:
    B=[curves[i][1] for i in s]
    assert abs(det(B))==1
    assert [sum(v[i] for v in B) for i in range(5)]==[3,1,1,1,1] # -K=3H-sum E
print('PENTAGON_CYCLES=12; ALL_120_ORDERINGS_ARE_UNIMODULAR_AND_ANTICANONICAL')
print('EXAMPLE', [curves[j][0] for j in P[0]], 'DET',det([curves[j][1] for j in P[0]]))

def cycle_type(permutation):
    visited=set(); lengths=[]
    for i in range(5):
        if i not in visited:
            j=i; z=0
            while j not in visited:
                visited.add(j);z+=1;j=permutation[j]
            lengths.append(z)
    return tuple(sorted(lengths))

for a in range(5):
 for flip in (0,1):
    # rotations i->i+a, reflections i->a-i
    g=tuple((a-i if flip else a+i)%5 for i in range(5))
    assert (cycle_type(g)==(1,2,2) if flip else cycle_type(g) in ((5,), (1,1,1,1,1)))
    for m in range(1,21):
        gm=tuple(range(5))
        for _ in range(m): gm=tuple(g[gm[i]] for i in range(5))
        V=sum(gm[i]==i for i in range(5))
        edges={frozenset((i,(i+1)%5)):i for i in range(5)}
        EF=sum(frozenset((gm[i],gm[(i+1)%5])) in edges and
               edges[frozenset((gm[i],gm[(i+1)%5]))]==i for i in range(5))
        BF=sum(gm[i]==i and gm[(i+1)%5]==(i+1)%5 for i in range(5))*2
        sgn=(-1 if flip and m%2 else 1)
        for q in (2,3,5,7,11):
            Q=q**m
            y_count=Q*Q+1+Q*V
            d_count=V*(Q+1)-BF+EF
            assert y_count-d_count==Q*Q+sgn,(a,flip,m,q,y_count,d_count,sgn)
    if (a,flip) in ((0,0),(1,0),(2,0),(0,1)):
        print('FROBENIUS_TYPE',a,flip,'PERMUTATION_CYCLE_TYPE',cycle_type(g),
              'BOUNDARY_FIXED',[(sum(g[i]==i for i in range(5))),
              sum(frozenset((g[i],g[(i+1)%5]))==frozenset((i,(i+1)%5)) for i in range(5))],
              'SIGN',-1 if flip else 1)
print('ALL_DIhedral_FROBENIUS_AND_EXTENSIONS_CHECKED')

# Two independent checks of point counts: split blowup and reflection affine model.
for q in (2,3,5,7,11):
    # P^2 plus 4 exceptional P1 replacing four rational points; divide out 4 points.
    points=(q*q+q+1)+4*q
    boundary=5*(q+1)-5
    assert points-boundary==q*q+1
    print('SPLIT_BLOWUP',q,points,boundary,points-boundary)

for q,a in ((3,2),(5,2),(7,3),(11,2),(13,2)):
    assert pow(a,(q-1)//2,q)==q-1
    count=0
    for x in range(q):
     for y in range(q):
        c=(x*x-a*y*y)%q
        count+= (q if c==0 and y==1 else int(c!=0))
    assert count==q*q-1,(q,a,count)
    print('REFLECTION_AFFINE',q,'a',a,'COUNT',count)
print('VERIFY_OK')

# Purely formal scissor relations in K0(Var/F_q), with Z2, Z5 representing
# Spec(F_{q^2}), Spec(F_{q^5}) and L the affine line. No relations among
# formal generators are imposed.
def mono(n=0,z='1',c=1):return {(n,z):c}
def linear(*terms):
 out={}
 for sign,P in terms:
  for key,v in P.items():out[key]=out.get(key,0)+sign*v
 return {k:v for k,v in out.items() if v}
def scale(P,n=1,shift=0):return {(a+shift,z):n*c for (a,z),c in P.items() if n*c}
def add(*args):return linear(*[(1,a) for a in args])
def sub(a,b):return linear((1,a),(-1,b))
L=mono(1);ONE=mono();L2=mono(2);Z2=mono(0,'Z2');Z5=mono(0,'Z5')
P2=add(L2,L,ONE)
S_split=add(P2,scale(L,4));D_split=scale(L,5)
S_rot=sub(add(P2,scale(Z5,shift=1)),L)
D_rot=sub(add(scale(Z5,shift=1),Z5),Z5) # = L Z5
S_ref=add(P2,scale(Z2,2,1))
V=add(ONE,scale(Z2,2));E=V;B=scale(Z2,5)
D_ref=add(sub(add(V,scale(V,shift=1)),B),E)
assert sub(S_split,D_split)==add(L2,ONE)
assert sub(S_rot,D_rot)==add(L2,ONE)
assert sub(S_ref,D_ref)==add(L2,sub(Z2,ONE))
print('MOTIVIC_SCISSOR_IDENTITIES split=rotation=L^2+1; reflection=L^2-1+Z2')
print('ALL_TESTS_PASSED')
