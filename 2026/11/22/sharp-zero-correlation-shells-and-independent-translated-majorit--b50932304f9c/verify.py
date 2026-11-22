"""Finite check of translated majority correlation, exact overlap and triple-independence construction."""
from math import comb
from itertools import combinations

def overlap_formula(d,a):
    m=(d-1)//2
    return sum(comb(a,j)*comb(d-a,r) for j in range(a+1) for r in range(d-a+1) if j+r<=m and a-j+r<=m)

def verify():
    assertions=0
    for d in range(1,62,2):
        m=(d-1)//2
        K=[overlap_formula(d,a) for a in range(d+1)]
        assert K[0]==2**(d-1) and K[-1]==0; assertions+=2
        for a in range(d):
            expected=0 if a%2 else comb(a,a//2)*comb(d-a-1,m-a//2)
            assert K[a]-K[a+1]==expected; assertions+=1
            assert K[a]+K[d-a]==2**(d-1); assertions+=1
        central=[a for a,v in enumerate(K) if 4*v==2**d]
        if d%4==3: assert central==[(d-1)//2,(d+1)//2]
        else: assert central==[]
        assertions+=1
    for d in [1,3,5,7,9,11,13]:
        m=(d-1)//2
        K=[0]*(d+1)
        for a in range(d+1):
            mask=(1<<a)-1
            K[a]=sum((x.bit_count()<=m and (x^mask).bit_count()<=m) for x in range(1<<d))
            assert K[a]==overlap_formula(d,a); assertions+=1
    for k in range(4):
        d=4*k+3
        c=(1<<k)-1
        masks=[0]
        for i in range(3):
            A=((1<<(k+1))-1)<<(k+i*(k+1))
            masks.append(c|A)
        assert max(x.bit_length() for x in masks)<=d; assertions+=1
        for u,v in combinations(masks,2):
            assert (u^v).bit_count() in (2*k+1,2*k+2); assertions+=1
        for ids in combinations(range(4),3):
            tallies=[0]*8
            for x in range(1<<d):
                pat=sum(int((x^masks[j]).bit_count()<=2*k+1)<<a for a,j in enumerate(ids))
                tallies[pat]+=1
            assert tallies==[2**(d-3)]*8, (k,ids,tallies)
            assertions+=1
    print(f'passed {assertions} exact assertions; d=1..61, exhaustive d<=13, triple constructions d=3,7,11,15')
if __name__=='__main__':verify()
