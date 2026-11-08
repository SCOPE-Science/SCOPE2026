"""Exact finite-attractor census for Stewart's finite morphic words.

Requires samcov.py and sufcov.py in the same directory, stdlib Python only.
"""
from samcov import word, covers
from sufcov import suffix_tree_masks

EXPECTED = {1:(2,2,2), 2:(2,1,5), 3:(3,55,10), 4:(3,110,17),
            5:(3,160,25), 6:(3,210,33), 7:(3,260,41), 8:(3,310,49)}

def pair_count(masks,n):
    allpos=(1<<n)-1
    ans=0
    for i in range(n):
        missed=[m for m in masks if not ((m>>i)&1)]
        for j in range(i+1,n):
            eligible=allpos
            for m in missed:
                if not ((m>>j)&1):
                    eligible &= m
                    if eligible==0:break
            ans += (eligible>>(j+1)).bit_count()
    return ans

def pair_exists(masks,n):
    for i in range(n):
        for j in range(i+1,n):
            if all(((m>>i)&1) or ((m>>j)&1) for m in masks):
                return True
    return False

def run():
    rows=[]
    for k in range(1,9):
        w=word(k)
        masks,_,_=covers(w)
        independent,_=suffix_tree_masks(w)
        assert set(masks)==set(independent),(k,'algorithms disagree')
        gamma,count,minmasks=EXPECTED[k]
        assert len(masks)==minmasks,(k,len(masks))
        if gamma==2:
            size2=sum(all(((m>>i)&1) or ((m>>j)&1) for m in masks)
                      for i in range(len(w)) for j in range(i+1,len(w)))
            assert size2==count,(k,size2)
            assert not any(all((m>>i)&1 for m in masks) for i in range(len(w)))
            witness=''
        else:
            if k==3: assert not pair_exists(masks,len(w)),(k,'pair witness')
            size3=pair_count(masks,len(w))
            assert size3==count,(k,size3)
            n=len(w)
            positions=(n//3,(n-1)//2,(5*n-3)//6)
            assert all(any((m>>i)&1 for i in positions) for m in masks),(k,positions)
            witness=','.join(map(str,positions))
        rows.append((k,len(w),gamma,count,len(masks),witness))
        print('CHECK',*rows[-1],flush=True)
    print('STEWART_ATTRACTOR_CENSUS_VERIFY_OK',len(rows),flush=True)
    return rows
if __name__=='__main__':run()
