from itertools import product

N=3
WORDS=tuple(range(1<<N))

def bits(x):
    return tuple((x>>i)&1 for i in range(N))

def sumword(a,b):
    aa,bb=bits(a),bits(b)
    return tuple(aa[i]+bb[i] for i in range(N))

def ud(A,B):
    seen=set()
    for a in A:
        for b in B:
            s=sumword(a,b)
            if s in seen:
                return False
            seen.add(s)
    return True

subs=[]
for mask in range(1,1<<(1<<N)):
    subs.append(tuple(w for w in WORDS if (mask>>w)&1))

best=0
ext=[]
for A in subs:
    for B in subs:
        p=len(A)*len(B)
        if p < best:
            continue
        if ud(A,B):
            if p>best:
                best=p; ext=[]
            if p==best:
                ext.append((A,B))

assert best==14
assert len(ext)==16
assert {(len(A),len(B)) for A,B in ext}=={(2,7),(7,2)}

# Exact structural classification.
def antipodal_pair(A):
    return len(A)==2 and (A[0]^A[1])==7
for A,B in ext:
    if len(A)==2:
        small,big=A,B
    else:
        small,big=B,A
    assert antipodal_pair(small)
    missing=set(WORDS)-set(big)
    assert len(missing)==1 and next(iter(missing)) in small

# Converse: every such pair is uniquely decodable and extremal.
expected=[]
for x in WORDS:
    y=x^7
    if x<y:
        small=(x,y)
        for z in small:
            big=tuple(w for w in WORDS if w!=z)
            assert ud(small,big)
            expected += [(small,big),(big,small)]
assert set(ext)==set(expected)

# Van Tilborg's distance-class count at n=3: for distance k there are
# at most C(3,k)*min(2^k,2^(3-k)) ordered pairs, hence 1+6+6+1=14.
from math import comb
bound=sum(comb(3,k)*min(2**k,2**(3-k)) for k in range(4))
assert bound==14

# A canonical witness.
A=(0,7)
B=tuple(range(7))
assert ud(A,B) and len(A)*len(B)==14

print('VERIFY_OK n=3 max_product=14 ordered_extremizers=16 size_profiles=2x7_or_7x2')
print('STRUCTURE small_code=antipodal_pair large_code=cube_minus_one_member_of_small_code')
print('BOUND distance_class_sum=1+6+6+1=14')
print('WITNESS A={000,111} B={000,001,010,011,100,101,110}')
