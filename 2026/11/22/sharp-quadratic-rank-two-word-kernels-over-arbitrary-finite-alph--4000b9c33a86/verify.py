"""Reproduce finite checks of the rank-two colour-profile kernel theorem.

Only Python's standard library is needed. Exhaustive finite tests are corroboration,
not a substitute for the unbounded mathematical proof.
"""
from itertools import product
from collections import defaultdict


def signature(word):
    n=len(word)
    return frozenset((word[i],frozenset(word[:i]),frozenset(word[i+1:])) for i in range(n))


def minimum_profile_subsequence(word):
    seen=set(); picked=[]
    for i in range(len(word)):
        p=(word[i],frozenset(word[:i]),frozenset(word[i+1:]))
        if p not in seen:
            seen.add(p);picked.append(word[i])
    return tuple(picked)


def extremizer(k):
    assert k>=1
    ans=[]
    for t in range(2*k):
        if t<k:
            ans.append(t)
        else:
            ans.append(t-k)
        active=[a for a in range(k) if a<=t and t<k+a]
        ans.extend(active)
    return tuple(ans)


def two_round_game_equiv(u,v):
    """Direct Duplicator 2-round test, with all ordered witness pairs."""
    if not u or not v: return not u and not v
    def can_reply(src,dst,i):
        for j in range(len(dst)):
            if src[i] != dst[j]: continue
            if all(any(src[k]==dst[l] and ((k<i)-(k>i))==((l<j)-(l>j))
                       for l in range(len(dst))) for k in range(len(src))):
                # Require that every possible second move in other structure
                # can also be matched (game is symmetric after first move).
                if all(any(src[k]==dst[l] and ((k<i)-(k>i))==((l<j)-(l>j))
                           for k in range(len(src))) for l in range(len(dst))):
                    return True
        return False
    return all(can_reply(u,v,i) for i in range(len(u))) and all(can_reply(v,u,j) for j in range(len(v)))


def main():
    count=0
    for k in range(1,10):
        w=extremizer(k)
        assert len(w)==k*(k+2), (k,w)
        assert len(signature(w))==len(w)
        assert set(w)==set(range(k))
        count+=1
    theory_min={}
    words=[]
    for n in range(0,12):
        for w in product((0,1),repeat=n):
            s=signature(w)
            comp=minimum_profile_subsequence(w)
            assert len(comp)==len(s)
            assert signature(comp)==s
            if s not in theory_min: theory_min[s]=n
            else: assert theory_min[s]<=n
            words.append((w,s))
            count+=1
    # Infinite-word completeness comes from the mathematical profile theorem;
    # the finite census below only tests the first twelve lengths.
    assert len(theory_min)==97
    assert max(theory_min.values())==8
    assert sum(1 for n in theory_min.values() if n==8)==4
    assert sum(1 for s in theory_min if s and all(t[0]==0 for t in s))==3
    assert sum(1 for s in theory_min if s and all(t[0]==1 for t in s))==3
    selected=[w for w,s in words if len(w)<=5]
    # Compare signatures with an independent two-round game implementation.
    for i in range(len(selected)):
        for j in range(i+1,len(selected)):
            u,v=selected[i],selected[j]
            assert (signature(u)==signature(v))==two_round_game_equiv(u,v), (u,v)
            count+=1
    print('VERIFY_OK',count,'binary_theories',len(theory_min),'sharp_binary_length',max(theory_min.values()))

if __name__=='__main__':main()
