"""Exact certificate checker for a five-element semiring's free term functions.
Standard-library Python 3; no external services or files except free3_certificate.json.
Run: python verify.py
"""
import itertools
import json
from collections import Counter
from pathlib import Path

ADD = ((0,0,0,0,0), (0,1,0,0,1), (0,0,2,2,2),
       (0,0,2,3,3), (0,1,2,3,4))
MUL = ((0,0,0,0,0), (0,0,0,0,0), (0,0,2,2,4),
       (0,1,2,3,4), (4,4,4,4,4))

# Independently verify the finite source tables satisfy the stated semiring laws.
for a in range(5):
    assert ADD[a][a] == a
    for b in range(5):
        assert ADD[a][b] == ADD[b][a]
        for c in range(5):
            assert ADD[ADD[a][b]][c] == ADD[a][ADD[b][c]]
            assert MUL[MUL[a][b]][c] == MUL[a][MUL[b][c]]
            assert MUL[a][ADD[b][c]] == ADD[MUL[a][b]][MUL[a][c]]
            assert MUL[ADD[a][b]][c] == ADD[MUL[a][c]][MUL[b][c]]

def combine(a, b, table):
    assert len(a) == len(b)
    return bytes(table[x][y] for x, y in zip(a, b))

def evaluations(rank):
    return list(itertools.product(range(5), repeat=rank))

def word_value(word, tup):
    result = tup[ord(word[0])-ord('x')]
    for letter in word[1:]:
        result = MUL[result][tup[ord(letter)-ord('x')]]
    return result

def word_functions(rank):
    alphabet='xyz'[:rank]
    reps=[]
    for k in range(1, rank+1):
        for p in itertools.permutations(alphabet,k):
            w=''.join(p)
            reps.extend((w,w+p[0]))
    ev=evaluations(rank)
    vectors=[bytes(word_value(w,t) for t in ev) for w in reps]
    assert len(vectors)==len(set(vectors))
    assert len(vectors)==2*sum(len(list(itertools.permutations(alphabet,k)))
                                 for k in range(1,rank+1))
    vals=set(vectors)
    for a in vectors:
        for b in vectors:
            assert combine(a,b,MUL) in vals, 'word normal form incomplete'
    return reps,vectors

def additive_closure(words):
    # Systematically insert one word generator; each step exhausts subsets
    seen={}
    for i,w in enumerate(words):
        previous=list(seen.items())
        seen.setdefault(w,1<<i)
        for v,mask in previous:
            seen.setdefault(combine(v,w,ADD),mask | (1<<i))
    for a in seen:
        for w in words:
            assert combine(a,w,ADD) in seen, 'not closed under addition'
    return seen

def check_small(rank, target, support_counts):
    reps,words=word_functions(rank)
    vectors=additive_closure(words)
    assert len(vectors)==target, (rank,len(vectors),target)
    supports=Counter(len(set(''.join(reps[i] for i in range(len(reps))
                               if (mask>>i)&1))) for mask in vectors.values())
    assert dict(supports)==support_counts,(rank,supports)
    return reps,words,vectors

for r,num,counts in ((1,2,{1:2}),(2,21,{1:4,2:17}),
                     (3,778,{1:6,2:51,3:721})):
    check_small(r,num,counts)

words, word_vectors, all_vectors=check_small(3,778,{1:6,2:51,3:721})
cert=json.loads((Path(__file__).with_name('free3_certificate.json')).read_text('utf-8'))
assert cert['schema_version']==1 and cert['rank']==3
assert cert['word_representatives']==words
masks=cert['element_masks']
assert len(masks)==778 and len(set(masks))==778
assert all(isinstance(m,int) and 1<=m<2**len(words) for m in masks)

def evaluate_mask(m):
    indices=[i for i in range(len(words)) if (m>>i)&1]
    assert indices
    result=word_vectors[indices[0]]
    for i in indices[1:]: result=combine(result,word_vectors[i],ADD)
    return result
cert_vectors={evaluate_mask(m) for m in masks}
assert len(cert_vectors)==778
assert cert_vectors==set(all_vectors)
# Full algebra-closure check, independently verifying the stronger certificate claim.
for i,a in enumerate(cert_vectors):
    for b in cert_vectors:
        assert combine(a,b,MUL) in cert_vectors, ('mult',i)
        assert combine(a,b,ADD) in cert_vectors, ('add',i)
print('VERIFY_OK: free ranks 1,2,3 = 2,21,778; full-support counts 2,17,721; word ranks 2,8,30; 778-element explicit certificate closed under both operations')
