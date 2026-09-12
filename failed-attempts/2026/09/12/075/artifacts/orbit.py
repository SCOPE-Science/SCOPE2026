"""Work out the shuffle weight orbit.
Setup (Chhita-Young / Ruelle conventions): faces of Aztec_n carry face weights.
Urban renewal on face with edge weights (a,b,c,d) cyclic: Delta = ac+bd; new weights A=c/Delta, B=d/Delta, C=a/Delta, D=b/Delta (up to the exact labeling convention).
Our faces: two types. From numeric Deltas (a=.7,b=1): type0 (i+j even): Delta=2a^2=0.98; type1: Delta=2=1+b^2.
Find the actual edge 4-tuples: print them.
"""
from collections import defaultdict
def faces(n,a,b=1.0):
    W = set((i, j) for i in range(1, 2*n, 2) for j in range(0, 2*n+1, 2))
    B = set((i, j) for i in range(0, 2*n+1, 2) for j in range(1, 2*n, 2))
    def wgt(bv, wv):
        (x1,x2)=bv; (y1,y2)=wv
        d=(y1-x1,y2-x2)
        s=(x1+x2)%4; j=0 if s==1 else 1
        if d==(1,1): return a*(1-j)+b*j
        if d==(-1,1): return a*j+b*(1-j)
        if d==(-1,-1): return a*j+b*(1-j)
        if d==(1,-1): return a*(1-j)+b*j
        return None
    for i in range(n):
        for j in range(n):
            vB1=(2*i,2*j+1); vB2=(2*i+2,2*j+1); vW1=(2*i+1,2*j); vW2=(2*i+1,2*j+2)
            e00=wgt(vB1,vW1); e01=wgt(vB1,vW2); e10=wgt(vB2,vW1); e11=wgt(vB2,vW2)
            cyc=(e00,e01,e11,e10)  # cyclic order B1-W1? order: B1-W1 edge, then W1-B2 edge, B2-W2, W2-B1
            print(f"face({i},{j}) par={(i+j)%2}: cyc={cyc}")
faces(2,0.7)
