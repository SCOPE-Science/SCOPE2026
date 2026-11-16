"""Exact direct ternary-character certificate for order-four alternating-sign matrices.
No external packages: run `python3 verify_ternary_row.py`.
"""
from collections import Counter
from itertools import combinations, product
from math import prod

def matrices():
    rows=[]
    for width in (1,3):
        for cols in combinations(range(4),width):
            v=[0]*4
            for j,c in enumerate(cols):v[c]=1 if j%2==0 else -1
            rows.append(tuple(v))
    out=[]
    def recur(depth, columns, chosen):
        if depth==4:
            if columns==(1,1,1,1):out.append(tuple(chosen))
            return
        for row in rows:
            nextcols=tuple(columns[i]+row[i] for i in range(4))
            if all(z in (0,1) for z in nextcols):
                recur(depth+1,nextcols,chosen+[row])
    recur(0,(0,0,0,0),[])
    return out

def squared_spectrum():
    mats=matrices();assert len(mats)==42
    assert len({tuple(x for row in mat for x in row) for mat in mats})==42
    points=[tuple(mat[i][j]%3 for i in range(3) for j in range(3)) for mat in mats]
    histogram=Counter();minimum=100000;nullity=0
    for k in range(3**9):
        digits=[];x=k
        for _ in range(9):digits.append(x%3);x//=3
        count=[0,0,0]
        for p in points:
            count[sum(v*w for v,w in zip(p,digits))%3]+=1
        a,b,c=count
        norm=a*a+b*b+c*c-a*b-a*c-b*c
        histogram[norm]+=1
        if norm:minimum=min(minimum,norm)
        else:nullity+=1
    assert nullity==734 and minimum==3
    assert len(histogram)==53
    assert sum(histogram.values())==19683
    assert sum(k*v for k,v in histogram.items())==42*19683
    assert histogram[1764]==1 and histogram[3]==3504
    # Every character with one or two nonzero matrix coordinates is tested,
    # including characters not represented by a sparse nine-coordinate frequency.
    zeros_by_weight={1:[],2:[]}
    for t in (1,2):
        for locations in combinations(range(16),t):
            for coefficients in product((1,2),repeat=t):
                ct=[0,0,0]
                for mat in mats:
                    residue=sum(coefficients[i]*mat[locations[i]//4][locations[i]%4] for i in range(t))%3
                    ct[residue]+=1
                if ct[0]==ct[1]==ct[2]:zeros_by_weight[t].append((locations,coefficients))
    expected_pairs={tuple(sorted((4*r+1,4*r+2))) for r in range(4)} | {tuple(sorted((4+c,8+c))) for c in range(4)}
    assert zeros_by_weight[1]==[]
    assert len(zeros_by_weight[2])==16
    assert set(pair for pair,coeff in zeros_by_weight[2])==expected_pairs
    assert all(c in ((1,2),(2,1)) for _,c in zeros_by_weight[2])
    print('PASS exact row recursion, 42 ASMs; 19,683 ternary Fourier norms; 16 and only 16 weight-two zeros')
    print('nonzero=',19683-nullity,'zeros=',nullity,'min squared magnitude=',minimum,'distinct levels=',len(histogram))
    return histogram

if __name__=='__main__':squared_spectrum()
