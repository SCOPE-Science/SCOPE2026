"""Direct deletion-mask enumeration for permutation-power complement sets."""
from collections import Counter
from itertools import combinations, product
from math import comb

def direct(q,r):
    W=tuple(range(q))*(r+1)
    P=tuple(range(q))
    multiplicities=Counter()
    embedding_count=0
    for I in combinations(range(len(W)),q):
        if tuple(W[i] for i in I)!=P:
            continue
        S=set(I)
        rem=tuple(W[i] for i in range(len(W)) if i not in S)
        multiplicities[rem]+=1
        embedding_count+=1
    return multiplicities,embedding_count

def rotations(q):
    return [tuple(list(range(h,q))+list(range(h))) for h in range(q)]

def predicted(q,r):
    R=rotations(q)
    outs=set()
    for h in combinations(range(r+q+1),r):
        # Use monotone codes from 0..q, distinct values allowed repeatedly.
        pass
    from itertools import combinations_with_replacement
    for h in combinations_with_replacement(range(q+1),r):
        outs.add(tuple(x for z in h for x in R[z%q]))
    return outs

checked=0; literal_embeds=0; outputs=0
for q in range(2,8):
    for r in range(0,6):
        if comb(r+q,q)>1500: continue
        M,E=direct(q,r)
        L=predicted(q,r)
        assert set(M)==L,(q,r,'language')
        assert E==comb(r+q,q),(q,r,'embeddings')
        assert len(M)==comb(r+q,q)-r,(q,r,'count')
        special=tuple(range(q))*r
        assert M[special]==r+1,(q,r,'special')
        assert all(v==1 for k,v in M.items() if k!=special),(q,r,'uniqueness')
        checked+=1;literal_embeds+=E;outputs+=len(M)
print(f'POSITIONAL_VERIFY_OK cases={checked} embeddings={literal_embeds} distinct_outputs={outputs}')
