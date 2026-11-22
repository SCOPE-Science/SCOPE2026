"""Finite independent check: literal binary words vs closed gap formula."""
from itertools import combinations
from math import comb
from collections import Counter, defaultdict

# Return maximum r with a(ba)^r as a subsequence, via actual greedy string matching.
def maximal_anchored_alternations(word):
    best = 0
    if 'a' not in word:
        return 0
    for r in range(1, len(word)//2+1):
        pat='a'+'ba'*r
        k=0
        for x in word:
            if k<len(pat) and pat[k]==x:
                k+=1
        if k==len(pat): best=r
    return best

def formula(A,B):
    out=Counter()
    # gap counts x0,...,xA via recursion, not literal words
    def visit(i,left,C,j):
        if i==A:
            x=left
            out[(C+A*x,j)]+=1
            return
        for x in range(left+1):
            visit(i+1,left-x,C+i*x,j+(i>0 and x>0))
    visit(0,B,0,0)
    return out

case_count=0; word_count=0
for A in range(1,7):
    for B in range(0,7):
        observed=Counter()
        for aa in combinations(range(A+B),A):
            word=''.join('a' if i in aa else 'b' for i in range(A+B))
            C=sum(word[:k].count('a') for k,ch in enumerate(word) if ch=='b')
            j=maximal_anchored_alternations(word)
            observed[(C,j)]+=1
            word_count+=1
        expected=formula(A,B)
        assert observed==expected, (A,B,observed,expected)
        for r in range(1,7):
            avoid=sum(v for (c,j),v in observed.items() if j<r)
            target=sum(comb(A-1,j)*comb(B+1,j+1) for j in range(min(r-1,A-1,B)+1))
            assert avoid==target,(A,B,r,avoid,target)
        case_count+=1
print({'direct_cases':case_count,'literal_words_checked':word_count,'comparison':'PASS'})
