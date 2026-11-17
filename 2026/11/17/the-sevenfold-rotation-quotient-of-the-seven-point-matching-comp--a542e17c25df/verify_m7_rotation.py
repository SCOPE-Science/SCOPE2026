#!/usr/bin/env python3
"""Exact standard-library certificate for the sevenfold quotient of M(K_7).

Run: python3 verify_m7_rotation.py
This code constructs quotient cells, signed boundaries, a maximal tree,
and exact Tietze simplifications of the attaching-word presentation.
"""
from itertools import combinations
from collections import Counter
from fractions import Fraction

N = 7
EDGES = list(combinations(range(N), 2))
EDGE_NUMBER = {e:i for i,e in enumerate(EDGES)}


def rotate(face, k):
    rotated = [EDGE_NUMBER[tuple(sorted(((a+k) % N, (b+k) % N)))]
               for e in face for a,b in [EDGES[e]]]
    inversions = sum(rotated[i] > rotated[j]
                     for i in range(len(rotated))
                     for j in range(i+1, len(rotated)))
    return tuple(sorted(rotated)), (-1 if inversions & 1 else 1)


def canonical(face):
    options = [(rotate(face,k)[0], rotate(face,k)[1]) for k in range(N)]
    minimum = min(f for f,_ in options)
    matches = [(f,s) for f,s in options if f == minimum]
    assert len(matches) == 1, ('nonfree cell orbit',face)
    return matches[0]


def make_faces(k):
    return [f for f in combinations(range(len(EDGES)),k)
            if len({point for edge in f for point in EDGES[edge]}) == 2*k]

FACES={k:make_faces(k) for k in (1,2,3)}
REPS={k:sorted({canonical(f)[0] for f in FACES[k]}) for k in FACES}
assert [len(FACES[k]) for k in (1,2,3)] == [21,105,105]
assert [len(REPS[k]) for k in (1,2,3)] == [3,15,15]


def boundary(k):
    rownum={f:i for i,f in enumerate(REPS[k-1])}
    d=[[0]*len(REPS[k]) for _ in REPS[k-1]]
    for j,face in enumerate(REPS[k]):
        for t in range(k):
            rep,sgn=canonical(face[:t]+face[t+1:])
            d[rownum[rep]][j]+=(-1 if t%2 else 1)*sgn
    return d

D1=boundary(2)
D2=boundary(3)
assert all(sum(D1[i][k]*D2[k][j] for k in range(15)) == 0
           for i in range(3) for j in range(15))


def rank(matrix, p=None):
    A=[[Fraction(x) if p is None else x%p for x in row] for row in matrix]
    rows=len(A); cols=len(A[0]); r=0
    for j in range(cols):
        pivot=next((i for i in range(r,rows) if A[i][j]), None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        u=(1/A[r][j]) if p is None else pow(A[r][j],-1,p)
        A[r]=[(x*u if p is None else x*u%p) for x in A[r]]
        for i in range(rows):
            if i==r:continue
            c=A[i][j]
            if c:
                A[i]=[(a-c*b if p is None else (a-c*b)%p)
                      for a,b in zip(A[i],A[r])]
        r+=1
        if r==rows:break
    return r

assert rank(D1)==2 and rank(D2)==13
assert rank(D1,3)==2 and rank(D2,3)==12
assert rank(D1,7)==2 and rank(D2,7)==12
assert rank(D2,2)==13 and rank(D2,5)==13
TREE={1,2} # spanning tree in the quotient 1-skeleton
assert abs(D1[1][1]*D1[2][2]-D1[1][2]*D1[2][1])==1

EDGE_ORBIT={rep:i for i,rep in enumerate(REPS[2])}

def edge_word(a,b):
    rep,sgn=canonical(tuple(sorted((a,b))))
    index=EDGE_ORBIT[rep]
    if index in TREE:return []
    return [(index, sgn*(1 if a<b else -1))]


def reduce_word(word):
    word=list(word)
    while len(word)>1:
        for i in range(len(word)):
            a=word[i]; b=word[(i+1)%len(word)]
            if a[0]==b[0] and a[1]==-b[1]:
                if i==len(word)-1:word=word[1:-1]
                else:word=word[:i]+word[i+2:]
                break
        else:break
    return word

WORDS=[]
for a,b,c in REPS[3]:
    WORDS.append(reduce_word(edge_word(a,b)+edge_word(b,c)+edge_word(c,a)))
assert len(WORDS)==15
INITIAL_WORDS=[w[:] for w in WORDS]
# All attaching-word exponent sums agree with the cellular boundary.
for j,word in enumerate(WORDS):
    counts=Counter()
    for x,eps in word:counts[x]+=eps
    assert all(counts[i]==D2[i][j] for i in range(15) if i not in TREE)

# Each elimination uses a relator containing the chosen generator precisely once.
# Cyclically rotate relator so that it begins with that generator, solve for
# the generator and substitute into all remaining relators. These are exact
# Tietze moves, valid for the noncommutative fundamental group.
GENERATORS=set(range(15))-TREE
STEPS=[]
while True:
    choose=None
    for relator_id,word in enumerate(WORDS):
        count=Counter(a for a,_ in word)
        single=next((a for a,num in count.items() if num==1),None)
        if single is not None:
            choose=(relator_id,single,word)
            break
    if choose is None:break
    relator_id,x,word=choose
    position=next(i for i,(a,eps) in enumerate(word) if a==x)
    exponent=word[position][1]
    rest=word[position+1:]+word[:position]
    solution=[(a,-eps) for a,eps in reversed(rest)] if exponent==1 else rest
    def substitute(w):
        out=[]
        for a,eps in w:
            if a!=x:out.append((a,eps))
            elif eps==1:out.extend(solution)
            else:out.extend((a,-e) for a,e in reversed(solution))
        return reduce_word(out)
    WORDS=[substitute(w) for i,w in enumerate(WORDS) if i!=relator_id]
    GENERATORS.remove(x)
    STEPS.append(x)

assert STEPS==[4,0,8,9,3,13,10,6,12,7,5,14],STEPS
assert GENERATORS=={11},GENERATORS
powers=[]
for word in WORDS:
    assert all(g==11 for g,_ in word)
    powers.append(sum(e for _,e in word))
assert sorted(abs(z) for z in powers)==[0,21,42],powers

print('full face counts (vertices,edges,triangles):',*[len(FACES[k]) for k in (1,2,3)])
print('quotient face counts (vertices,edges,triangles):',*[len(REPS[k]) for k in (1,2,3)])
print('free orbit size for each nonempty face: 7')
print('chain boundary composition: zero')
print('ranks of d1 and d2 over Q:',rank(D1),rank(D2))
print('ranks d2 over F_3,F_7,F_2,F_5:',*[rank(D2,p) for p in (3,7,2,5)])
print('contracted tree edge indices:',*sorted(TREE))
print('Tietze eliminated generators:',*STEPS)
print('remaining generator and relator exponents:',*sorted(GENERATORS),powers)
print('fundamental group: C_21')
print('H0=Z, H1=Z/21, H2=Z^2, other homology=0')
print('M7_CYCLIC_QUOTIENT_PI1_HOMOLOGY_PASS')
