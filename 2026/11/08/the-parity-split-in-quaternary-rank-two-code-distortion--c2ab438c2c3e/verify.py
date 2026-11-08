"""Standalone exact checks for rank-two quaternary Hamming distortion."""
from itertools import product, permutations
from fractions import Fraction

def mul(a,b):
    p=0
    while b:
        if b&1: p^=a
        b>>=1
        a<<=1
        if a&4: a^=7
    return p

def det(A):
    a,b,c,d=A
    return mul(a,d)^mul(b,c)

V=((1,0),(0,1),(1,1),(1,2),(1,3))
def normalize(v):
    a,b=v
    assert a or b
    if a:
        inv=next(k for k in (1,2,3) if mul(k,a)==1)
    else:
        inv=next(k for k in (1,2,3) if mul(k,b)==1)
    return mul(inv,a),mul(inv,b)

def act(A,v):
    a,b,c,d=A
    x,y=v
    return normalize((mul(a,x)^mul(b,y),mul(c,x)^mul(d,y)))

def sgn(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

projective_perms=set()
for A in product(range(4),repeat=4):
    if det(A):
        p=tuple(V.index(act(A,v)) for v in V)
        projective_perms.add(p)
assert len(projective_perms)==60
assert all(sgn(p)==1 for p in projective_perms)
assert {p for p in permutations(range(5)) if sgn(p)==1}==projective_perms
frob=tuple(V.index((mul(v[0],v[0]),mul(v[1],v[1]))) for v in V)
assert frob==(0,1,2,4,3) and sgn(frob)==-1

# The five nonzero weight classes are indexed by their unique kernel directions.
def weights(counts):
    N=sum(counts)
    return tuple(N-v for v in counts)

def distortion(counts1, counts2):
    a=weights(counts1); b=weights(counts2)
    possibilities=[]
    for p in projective_perms:
        rs=[Fraction(b[p[i]],a[i]) for i in range(5)]
        possibilities.append(max(rs)/min(rs))
    return min(possibilities)

m=(0,1,2,3,4)
e=(1,0,2,3,4)
assert weights(m)==(10,9,8,7,6)
assert sorted(weights(m))==sorted(weights(e))
assert distortion(m,e)==Fraction(100,81)
# Exhaustive Hamming weight computation for actual length-ten generator matrices.
def codeword_weights(counts):
    generator=[v for v,c in zip(V,counts) for _ in range(c)]
    out=[]
    for u in product(range(4),repeat=2):
        if u==(0,0): continue
        out.append(sum((mul(u[0],v[0])^mul(u[1],v[1]))!=0 for v in generator))
    return sorted(out)
assert codeword_weights(m)==sorted(w for w in weights(m) for _ in range(3))
assert codeword_weights(e)==codeword_weights(m)

# Every full-support profile with up to 10 columns; weights identify its multiset of projective multiplicities.
# For <10, repeated multiplicities ensure the isospectral fiber is one PGL orbit.
num_profiles=0
for n in range(2,11):
    for m0 in range(n+1):
        for m1 in range(n-m0+1):
            for m2 in range(n-m0-m1+1):
                for m3 in range(n-m0-m1-m2+1):
                    m4=n-m0-m1-m2-m3
                    arr=(m0,m1,m2,m3,m4)
                    if sum(x>0 for x in arr)<2:continue
                    num_profiles+=1
                    # same sorted multiset is one orbit when a repetition occurs
                    if len(set(arr))<5:
                        if n<=7: # independent direct enumeration manageable
                            orbit={tuple(arr[p[i]] for i in range(5)) for p in projective_perms}
                            assert orbit==set(permutations(arr))
                    else:
                        assert n==10 and sorted(arr)==[0,1,2,3,4]
                        orbit={tuple(arr[p[i]] for i in range(5)) for p in projective_perms}
                        assert len(orbit)==60
assert distortion(m,m)==1
# Exact distortion theorem over a varied full-support finite family.
tested_distinct=0
for n in range(10,22):
    for a0 in range(n+1):
        for a1 in range(a0+1,n+1):
            for a2 in range(a1+1,n+1):
                for a3 in range(a2+1,n+1):
                    a4=n-a0-a1-a2-a3
                    if a4<=a3: continue
                    aa=(a0,a1,a2,a3,a4)
                    bb=(a1,a0,a2,a3,a4)
                    w=sorted(weights(aa))
                    delta=min(Fraction(w[i+1],w[i]) for i in range(4))
                    assert distortion(aa,bb)==delta*delta
                    tested_distinct+=1
assert tested_distinct>=30
print('CHECK_OK','distinct_profiles', tested_distinct, 'PGL_size',len(projective_perms),'profiles',num_profiles, 'minimal_nontrivial_length',10,'distortion',str(distortion(m,e)), 'weight_enumerator', sorted(codeword_weights(m)))
