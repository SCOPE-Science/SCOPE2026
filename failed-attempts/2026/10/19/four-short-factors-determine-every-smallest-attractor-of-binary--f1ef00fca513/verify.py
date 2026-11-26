"""Independent exhaustive factor-occurrence test of a binary run-period attractor theorem."""
from itertools import combinations

def all_minimal_pairs(a,b,m):
    word=('0'*a+'1'*b)*m
    N=len(word)
    masks={}
    for i in range(N):
        for j in range(i+1,N+1):
            f=word[i:j]
            masks[f]=masks.get(f,0) | (((1<<(j-i))-1)<<i)
    return {(i,j) for i,j in combinations(range(N),2) if all((mask & ((1<<i)|(1<<j))) for mask in masks.values())}

def predicted(a,b,m):
    p=a+b
    left={(i*p+a-1,(j+1)*p-1) for i in range(m) for j in range(m-1)}
    right={(j*p,i*p+a) for i in range(m) for j in range(1,m)}
    return {tuple(sorted(pair)) for pair in left|right}

cases=0
for a in range(2,6):
    for b in range(2,6):
        for m in range(2,6):
            expected=predicted(a,b,m)
            actual=all_minimal_pairs(a,b,m)
            assert actual==expected, (a,b,m,sorted(actual^expected))
            assert len(expected)==2*m*(m-1),(a,b,m,len(expected))
            cases+=1
for a,b,m in [(6,2,3),(2,6,3),(6,7,2),(7,6,2),(3,8,2),(8,3,2)]:
    assert all_minimal_pairs(a,b,m)==predicted(a,b,m),(a,b,m)
    cases+=1
print('EXACT FACTOR CHECKS PASSED')
print('complete parameter triples:',cases)
print('example a=2,b=2,m=3: smallest attractors =',len(all_minimal_pairs(2,2,3)))
