"""Independent direct definition test of three-round extension rank.
No import from structural_census.py. Enumerates every 4-by-4 binary incidence matrix.
"""
from functools import lru_cache

# Enumerate all realizable single-point extension types using subsets, not pair cases.
def direct_rank_three(bits):
    adj=[0]*8
    for i in range(4):
        for j in range(4):
            if bits>>(4*i+j)&1:
                adj[i]|=1<<(j+4)
                adj[j+4]|=1<<i
    @lru_cache(None)
    def r(mask,depth):
        if depth==0: return True
        for side in (0,1):
            op=mask& (240 if side==0 else 15)
            vertices=range(4) if side==0 else range(4,8)
            options=set()
            # list every binary relation pattern to the marked opposite side
            occupied=[j for j in range(8) if op>>j&1]
            for pattern in range(1<<len(occupied)):
                target=sum((pattern>>q&1)<<occupied[q] for q in range(len(occupied)))
                if not any((not (mask>>v&1))
                           and (adj[v]&op)==target
                           and r(mask|(1<<v),depth-1) for v in vertices):
                    return False
        return True
    return r(0,3)


def main():
    count=0
    for bits in range(65536):
        if direct_rank_three(bits):count+=1
    assert count==9672,count
    print('INDEPENDENT_DIRECT_RECURSION_OK count='+str(count))

if __name__=='__main__': main()
