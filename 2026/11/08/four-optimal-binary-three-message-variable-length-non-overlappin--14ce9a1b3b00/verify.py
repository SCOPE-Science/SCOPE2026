"""Exhaustive small-candidate certificate for binary strong nonoverlapping codes.
Python 3 standard library; run `python3 verify.py`.
"""
from itertools import combinations, product
from collections import Counter


def words(n):
    # Every word may be complemented, so choose initial 0 and final 1.
    return ['0'+''.join(t)+'1' for t in product('01',repeat=n-2)
            if all(('0'+''.join(t)+'1')[:k] != ('0'+''.join(t)+'1')[-k:]
                   for k in range(1,n))]


def compatible(u,v):
    if u in v or v in u:
        return False
    for k in range(1, min(len(u),len(v))+1):
        if u[:k] == v[-k:] or v[:k] == u[-k:]:
            return False
    return True

A={n:words(n) for n in range(4,8)}
assert {n:len(v) for n,v in A.items()}=={4:3,5:6,6:10,7:20}
for u,v in combinations(A[4],2):
    assert not compatible(u,v)
assert {v for v in A[5] if compatible('0011',v)}=={'00101','01011'}
assert {v for v in A[6] if compatible('0011',v)}=={'000101','001011','010111'}
assert {v for v in A[7] if compatible('0011',v)}=={
    '0000101','0001011','0010101','0010111','0101011','0101111'}
assert all(not compatible(u,v) for u in A[4] if u!='0011'
           for k in (5,6,7) for v in A[k])

# All length profiles of total <=16 and maximum length <=7 are tested below.
# The only omitted profile (4,4,8) is ruled out by the pair test above.
profiles=[]
sol=[]
for a in range(4,8):
    for b in range(a,8):
        for c in range(b,8):
            if a+b+c>16: continue
            profiles.append((a,b,c))
            for u in A[a]:
                for v in A[b]:
                    if a==b and not(u<v): continue
                    if not compatible(u,v): continue
                    for w in A[c]:
                        if b==c and not(v<w): continue
                        if compatible(u,w) and compatible(v,w):
                            sol.append((u,v,w))
assert sorted(sol)==[
    ('00011','01011','010011'),
    ('00101','00111','001101'),
]
assert {tuple(map(len,t)) for t in sol}=={(5,5,6)}
assert len(profiles)==10
# Binary complement gives the other two labeled codes; reverse-complement
# exchanges the two starting-0 classes, so all four form one orbit.
allcodes = {frozenset(t) for t in sol}
allcodes |= {frozenset(''.join('1' if c=='0' else '0' for c in w)
                          for w in t) for t in sol}
assert len(allcodes)==4
for code in allcodes:
    assert len(code)==3 and sum(map(len,code))==16
    assert all(compatible(u,v) for u,v in combinations(sorted(code),2))
    assert frozenset(w[::-1] for w in code) in allcodes
rep=next(iter(allcodes))
def compl(code):
    return frozenset(''.join('1' if b=='0' else '0' for b in w)
                     for w in code)
def rev(code): return frozenset(w[::-1] for w in code)
assert {rep,compl(rep),rev(rep),compl(rev(rep))}==allcodes
print('PASS oriented_profile_count',len(profiles),'oriented_optima',len(sol),
      'labeled_optima',len(allcodes),'optimum_total_length',16)
