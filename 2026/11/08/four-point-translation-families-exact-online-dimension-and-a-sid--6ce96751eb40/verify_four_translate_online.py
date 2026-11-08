"""Independent finite checks for four-point group-translate online dimension.
Uses standard-library exhaustive enumeration and exact binary-tree recursion.
"""
from itertools import combinations, product
from functools import lru_cache


def make_group(moduli):
    pts = list(product(*(range(m) for m in moduli)))
    index = {u: i for i, u in enumerate(pts)}
    add = [[index[tuple((a+b)%m for a,b,m in zip(u,v,moduli))]
            for v in pts] for u in pts]
    return pts,add


def ldim(hypotheses, n):
    H = tuple(sorted(set(hypotheses)))
    m = len(H)
    query_masks = tuple(sum(1<<i for i,h in enumerate(H) if (h>>q)&1)
                        for q in range(n))
    @lru_cache(None)
    def depth(version_space, d):
        if d == 0: return True
        if version_space.bit_count() < 1<<d: return False
        for query_mask in query_masks:
            left = version_space & query_mask
            right = version_space & ~query_mask
            if left.bit_count() >= 1<<(d-1) and right.bit_count() >= 1<<(d-1):
                if depth(left, d-1) and depth(right, d-1):
                    return True
        return False
    return max(d for d in range(m.bit_length()) if depth((1<<m)-1, d))


def predicted(A,add):
    n=len(add); B=set(A)
    H=sum(1 for t in range(n) if {add[t][x] for x in A}==B)
    corr=[len(B & {add[t][x] for x in A}) for t in range(1,n)]
    return (1 if H==4 else 3 if H==1 and 2 in corr else 2),H


def vc(hypotheses, n):
    H=set(hypotheses)
    for d in (3,2,1):
        for Q in combinations(range(n),d):
            traces={sum(((h>>q)&1)<<j for j,q in enumerate(Q)) for h in H}
            if len(traces)==1<<d: return d
    return 0


def run_group(moduli):
    elements, add=make_group(moduli)
    n=len(elements)
    counts={}; cases=0
    for A in combinations(range(n),4):
        translated=[sum(1<<add[t][x] for x in A) for t in range(n)]
        expected,h=predicted(A,add)
        observed=ldim(translated,n)
        assert expected==observed,(moduli,A,expected,observed,h)
        counts[observed]=counts.get(observed,0)+1
        cases+=1
    print('EXHAUSTIVE_GROUP_PASS',moduli,'sets',cases,'dimensions',counts,flush=True)
    return counts


def main():
    for n in range(8,17): run_group((n,))
    for moduli in ((2,2,2),(2,4),(3,3),(2,2,3),(2,2,2,2)):
        run_group(moduli)
    n=13
    one_diff=[]
    for a,b in combinations(range(2,n),2):
        A={0,1,a,b}
        diffs=[(u-v)%n for u in A for v in A if u!=v]
        if len(set(diffs))==12:
            one_diff.append((0,1,a,b))
    assert one_diff==[(0,1,3,9),(0,1,4,6),(0,1,5,11),(0,1,8,10)],one_diff
    counts=run_group((13,))
    assert counts=={2:52,3:663}
    _,add=make_group((13,))
    for A,expected in (((0,1,3,9),2),((0,1,2,3),3)):
        translated=[sum(1<<add[t][x] for x in A) for t in range(n)]
        assert ldim(translated,n)==expected
        assert vc(translated,n)==2
    print('N13_NORMALIZED_DIFFERENCE_SETS_PASS',one_diff,'count',52,flush=True)
    print('SAME_VC_DIFFERENT_ONLINE_DIMENSION_PASS',flush=True)
    print('ALL_FOUR_POINT_TRANSLATION_CHECKS_PASS',flush=True)

if __name__=='__main__':main()
