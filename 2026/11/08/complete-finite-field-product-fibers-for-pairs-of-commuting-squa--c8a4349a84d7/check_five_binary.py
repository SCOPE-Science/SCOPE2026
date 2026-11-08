#!/usr/bin/env python3
"""Direct original-identity verification of every rank-one nonzero fiber at n=5 over F2."""
from itertools import product
from check_product_fibers import mul,fiber

def dot(x,y):return sum(a*b for a,b in zip(x,y))%2

def main():
    one=[[0]*5 for _ in range(5)];one[0][4]=1
    zero=[[0]*5 for _ in range(5)]
    nonzero=[v for v in product(range(2),repeat=3) if any(v)]
    count=0
    for h in nonzero:
        for s in nonzero:
            if h==s:continue
            for P in product(range(2),repeat=3):
                if dot(P,h)!=1 or dot(P,s)!=0:continue
                for U in product(range(2),repeat=3):
                    if dot(U,h)!=0 or dot(U,s)!=1:continue
                    for Q,V in product(range(2),repeat=2):
                        B=[[0]*5 for _ in range(5)]
                        C=[[0]*5 for _ in range(5)]
                        for j in range(3):
                            B[0][j+1]=P[j];C[0][j+1]=U[j]
                            B[j+1][4]=s[j];C[j+1][4]=h[j]
                        B[0][4]=Q;C[0][4]=V
                        assert mul(B,B,2)==zero and mul(C,C,2)==zero
                        assert mul(B,C,2)==one and mul(C,B,2)==one
                        count+=1
    assert count==fiber(5,1,2),(count,fiber(5,1,2))
    print('DIRECT_5x5_BINARY_RANK_ONE_FIBER_OK',count)
if __name__=='__main__':main()
