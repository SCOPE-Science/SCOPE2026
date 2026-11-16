"""Exact checks for Walsh transforms of perfect matchings of cycle prisms.

Only the Python standard library is used; integer arithmetic throughout.
Run: python prism_walsh_verifier.py
"""
from itertools import product
from math import prod


def edges_and_matchings(n):
    assert n >= 3
    edges = [(j, (j + 1) % n) for j in range(n)]
    edges += [(n + j, n + (j + 1) % n) for j in range(n)]
    edges += [(j, n + j) for j in range(n)]
    assert len(set(tuple(sorted(e)) for e in edges)) == 3 * n
    incident = [[] for _ in range(2 * n)]
    for k, (u, v) in enumerate(edges):
        incident[u].append((k, v))
        incident[v].append((k, u))
    matchings = []
    complete = (1 << (2 * n)) - 1
    def search(used, mask):
        if used == complete:
            matchings.append(mask)
            return
        u = next(i for i in range(2 * n) if not ((used >> i) & 1))
        for k, v in incident[u]:
            if not ((used >> v) & 1):
                search(used | (1 << u) | (1 << v), mask | (1 << k))
    search(0, 0)
    return edges, matchings


def product2(A, B):
    a,b,c,d = A; e,f,g,h = B
    return (a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h)


def cycle_weight(y):
    p = (1, 0, 0, 1)
    for t in y:
        p = product2(p, (1, t, 1, 0))
    return p[0]+p[3]


def sum_prism_subfamily(y, flip=1):
    n = len(y)
    z = cycle_weight(y)
    if n % 2: return z
    return z + flip*(prod(y[::2])+prod(y[1::2]))


def frequency_from_y(y, flip=1):
    # Rung signs all +1; rail signs a_j and b_j=y_j*a_j.
    n = len(y)
    A = [1]*n
    if flip < 0: A[0] = -1
    B = [a*b for a,b in zip(A,y)]
    s = A+B+[1]*n
    return sum((1 << j) for j,t in enumerate(s) if t < 0)


def direct_weight(mask, matchings):
    return sum(1 if ((mask & m).bit_count() & 1) == 0 else -1 for m in matchings)


def all_walsh_matchings(n, matchings):
    a = [0] * (1 << (3*n))
    for mask in matchings:
        a[mask] = 1
    width = 1
    while width < len(a):
        for block in range(0, len(a), 2*width):
            for j in range(block, block+width):
                x,y = a[j],a[j+width]
                a[j],a[j+width]=x+y,x-y
        width *= 2
    return a


seed_positive={3:(1,1,-1),4:(1,1,-1,-1),5:(1,-1,1,-1,-1),
 6:(1,1,1,-1,1,-1),7:(1,1,1,-1,1,-1,-1),8:(1,1,1,1,-1,1,-1,-1)}
seed_flip={3:1,4:-1,5:1,6:-1,7:1,8:1}
seed_zero={3:(-1,-1,1),6:(-1,1,-1,-1,1,1)}
assert product2(product2((1,0,0,1),(1,-1,1,0)),(1,-1,1,0))==(0,-1,1,-1)
assert cycle_weight((-1,)*6)==2
p=(1,0,0,1)
for x in (-1,)*6:p=product2(p,(1,x,1,0))
assert p==(1,0,0,1)
identity_blocks = [tuple(1 if c=='+' else -1 for c in s)
                   for s in ('+--+--','-+--+-','--+--+','------')]
for block in identity_blocks:
    q=(1,0,0,1)
    for t in block:q=product2(q,(1,t,1,0))
    assert q==(1,0,0,1) and prod(block)==1
assert len(set(identity_blocks))==4
for n in range(3,9):
    y=seed_positive[n]
    val=sum_prism_subfamily(y,seed_flip[n])
    want=4 if n%6==0 else 2 if n%6==3 else 1
    assert abs(val)==want,(n,y,val,want)
for n,y in seed_zero.items():
    assert sum_prism_subfamily(y)==0
    assert cycle_weight(y)==0
    if n%2==0: assert prod(y)==-1
for n in range(3,12):
    # All signed cyclic matching sums, with a six-site identity extension.
    for y in product((-1,1),repeat=n):
        assert cycle_weight(y+(-1,)*6)==cycle_weight(y)
        if n%2==0:
            assert prod(y+(-1,)*6)==prod(y)
for n in range(3,8):
    E,matchings=edges_and_matchings(n)
    a=all_walsh_matchings(n,matchings)
    gap=min(abs(int(x)) for x in a if x != 0)
    want=4 if n%6==0 else 2 if n%6==3 else 1
    assert gap==want,(n,gap,want)
    assert (any(v==0 for v in a))==(n%3==0)
    for y in [seed_positive[n]]+([seed_zero[n]] if n in seed_zero else []):
        for flip in (1,-1):
            mask=frequency_from_y(y,flip)
            v=direct_weight(mask,matchings)
            assert v==sum_prism_subfamily(y,flip),(n,y,flip,v)
            assert v==int(a[mask])
    if n%6==0:
        assert all(v%4==0 for v in a)
    print('n=%d edges=%d matchings=%d zeros=%d gap=%d' % (n,len(E),len(matchings),a.count(0),gap))
# Verify the uniform sign parametrization: arbitrary rung signs r and upper-rail
# signs a, with lower signs b_i=y_i r_i r_{i+1} a_i, give the same
# common-dimer transfer value up to the sign product of r.
def full_frequency_from_y(y,r,a):
    n=len(y)
    b=[y[j]*r[j]*r[(j+1)%n]*a[j] for j in range(n)]
    signs=list(a)+b+list(r)
    return sum(1<<j for j,v in enumerate(signs) if v==-1)
for n in (3,6):
    _,matchings=edges_and_matchings(n)
    y=seed_zero[n]
    for r_bits in range(1<<n):
        r=[-1 if (r_bits>>j)&1 else 1 for j in range(n)]
        for a_bits in range(1<<n):
            a=[-1 if (a_bits>>j)&1 else 1 for j in range(n)]
            assert direct_weight(full_frequency_from_y(y,r,a),matchings)==0
for n in range(3,202):
    r=n%6
    base={3:3,4:4,5:5,0:6,1:7,2:8}[r]
    if n<base:continue
    y=seed_positive[base]+(-1,)*(n-base)
    flip=seed_flip[base]
    if n%2==0 and ((n-base)//6)%2:flip=-flip
    v=sum_prism_subfamily(y,flip)
    want=4 if n%6==0 else 2 if n%6==3 else 1
    assert abs(v)==want,(n,v,want)
    if n%3==0:
        b=3 if n%2 else 6
        z=seed_zero[b]+(-1,)*(n-b)
        assert sum_prism_subfamily(z)==0,(n,z)
print('PRISM_WALSH_EXACT_TESTS_PASS')
