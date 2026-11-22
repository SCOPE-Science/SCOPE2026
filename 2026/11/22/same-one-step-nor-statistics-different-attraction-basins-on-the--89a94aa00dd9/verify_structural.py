"""Separate structural verification via a side-specific bipartite-double isomorphism.
Run: python3 verify_structural.py
"""
from collections import Counter
from itertools import combinations

N=16
LEFT=[0,1,9,8,2,3,11,10,12,7,15,4,14,5,13,6]
RIGHT=[13,4,12,5,15,6,14,7,3,0,8,11,1,2,10,9]

def rows(kind):
    A=[]
    for i in range(N):
        x,y=divmod(i,4)
        cur=[]
        for j in range(N):
            a,b=divmod(j,4)
            if kind=='rook':
                hit = (i!=j) and ((x==a) or (y==b))
            else:
                hit=((a-x)%4,(b-y)%4) in ((1,0),(3,0),(0,1),(0,3),(1,1),(3,3))
            if hit:cur.append(j)
        A.append(tuple(cur))
    return A

R,H=rows('rook'),rows('shrikhande')
assert len(set(LEFT))==len(set(RIGHT))==16
for i in range(N):
    assert set(RIGHT[j] for j in R[i]) == set(H[LEFT[i]])

# Count one-step patterns by row-by-row insertion of rook placements; independent
# from the direct 65536-state orbit classification.
def rook_step(s):
    row=[(s>>(4*i))&15 for i in range(4)]
    col=[sum((row[i]>>j)&1 for i in range(4)) for j in range(4)]
    nxt=0
    for i in range(4):
        for j in range(4):
            # row/column counts exclude own occupied square
            self_bit=(row[i]>>j)&1
            if row[i].bit_count() + col[j] - 2*self_bit == 0:
                nxt |= 1<<(4*i+j)
    return nxt

fiber=Counter(rook_step(s) for s in range(1<<N))
assert Counter(fiber.values())==Counter({1:457,5:60,19:120,548:16,53731:1})
assert len(fiber)==654
assert Counter((y.bit_count(),w) for y,w in fiber.items()) == Counter({
(0,53731):1,(16,1):1,(1,548):16,(10,1):16,(2,19):120,
(6,1):120,(3,1):320,(4,5):60})

def translate(mask,perm):
    return sum((1<<perm[i]) for i in range(N) if mask>>i&1)

def shri_step(s):
    return sum(1<<i for i,neigh in enumerate(H) if all(not(s>>j&1) for j in neigh))

# Prove the two-sided relation for each state, not just the 16x16 adjacency certificate.
for s in range(1<<N):
    assert shri_step(translate(s,RIGHT))==translate(rook_step(s),LEFT)

# Classify fixed points separately, without using the orbit census or the previous rule.
for name,A in [('rook',R),('shrikhande',H)]:
    fixed=Counter()
    for k in (3,4):
        for indices in combinations(range(N),k):
            S=set(indices)
            independent=all(not any(j in S for j in A[i]) for i in S)
            dominates=all(i in S or any(j in S for j in A[i]) for i in range(N))
            if independent and dominates: fixed[k]+=1
    assert fixed==({'rook':Counter({4:24}),'shrikhande':Counter({3:32,4:16})}[name])
    print(name,'fixed_by_support',dict(fixed))

# In the image, image sizes are paired by support size as recorded by the rook
# test and by a separately generated Shrikhande image (not inferred by a graph theorem).
for name,step in [('rook',rook_step),('shrikhande',shri_step)]:
    image=set(step(s) for s in range(1<<N))
    pairs=Counter((y.bit_count(),step(y).bit_count()) for y in image)
    expect={(0,16):1,(16,0):1,(1,10):16,(10,1):16,
            (2,6):120,(6,2):120,(3,3):320,(4,4):60}
    assert pairs==expect
    assert all(step(step(y))==y for y in image)
    print(name,'support_transitions',sorted(pairs.items()))
print('SIDE_ISOMORPHISM_AND_FIXED_CLASSIFICATION_PASSED')
