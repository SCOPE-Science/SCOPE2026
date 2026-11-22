"""Direct matrix-overlap verification for optimal 3-by-3 cross-bibifix codes."""
from itertools import product
from collections import defaultdict
from math import comb


def squares(m):
    # An m is a flat 3x3 matrix in row-major order.
    return (m[0], m[1], m[3], m[4]), (m[4], m[5], m[7], m[8])


def compatible(c):
    pref1 = {m[0] for m in c}
    suff1 = {m[8] for m in c}
    if pref1 & suff1:
        return False
    p = [squares(m)[0] for m in c]
    s = [squares(m)[1] for m in c]
    return not(set(p) & set(s))


def group_structure(q, A, B):
    S = set(range(q))
    assert set(A).isdisjoint(B)
    data = [m for m in product(range(q), repeat=9) if m[0] in A and m[8] in B]
    left = defaultdict(list)
    right = defaultdict(list)
    neutral = []
    for m in data:
        center = m[4]
        if center in B:
            # prefix 2-square starts with a in A, ends with c in B
            left[squares(m)[0]].append(m)
        elif center in A:
            right[squares(m)[1]].append(m)
        else:
            neutral.append(m)
    assert set(left) == set(right)
    assert len(left) == len(A)*len(B)*q*q
    for k in left:
        assert len(left[k]) == len(B)*q**4, (q,A,B,k,len(left[k]))
        assert len(right[k]) == len(A)*q**4
        assert squares(left[k][0])[0] == squares(right[k][0])[1]
    # Full code chooses the larger side of each conflict component.
    code=neutral[:]
    for key in left:
        code.extend(max([left[key],right[key]],key=len))
    assert compatible(code)
    predicted=len(A)*len(B)*(q-min(len(A),len(B)))*q**6
    assert len(code)==predicted
    return len(data),len(neutral),len(left),len(code)


if __name__=='__main__':
    for q,A,B in ((2,{0},{1}),(3,{0,1},{2}),(3,{0},{1,2}),(4,{0,1,2},{3}),(4,{0,1},{2,3})):
        res=group_structure(q,A,B)
        print('q,A,B,data,neutral,components,max=',q,sorted(A),sorted(B),*res)
    print('DIRECT_PASSES')
    for q in range(2,501):
        b=(q+1)//3
        scores={t:t*(q-t)**2 for t in range(1,q//2+1)}
        assert max(scores.values())==scores[b]
        assert [t for t,v in scores.items() if v==scores[b]]==[b]
    print('INTEGER_MAXIMIZER_2_TO_500_PASSES')
