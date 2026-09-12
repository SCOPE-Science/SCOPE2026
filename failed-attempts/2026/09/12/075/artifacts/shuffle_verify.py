"""Verify one shuffle step explicitly: urban renewal on all n^2 faces of Aztec_n.
Implement: for each face (cell) with edge weights (a,b,c,d cyclic), factor Delta=ac+bd;
new smaller-face weights A=c/Delta etc. Then pendant removal + contraction + gauge → Aztec_{n-1}
with transformed weights. Track total prefactor. Do this SYMBOLICALLY-ish (numeric for generic a, then identify).
Actually simpler rigorous path for DRAFT: prove the SECOND-ORDER recurrence via Kuo condensation as stated in
Kuo, "Graphical condensation, I" (2004)? Let me instead verify the first-order shuffle factor numerically
by implementing the shuffle transformation on the Kasteleyn matrix and comparing det ratios.
But the shuffle changes weights (a,b) -> new pattern; need to track 2x2 fundamental domain evolution.
Alternative pragmatic approach: implement urban renewal at the *partition function* level via the
"reduced graph = Aztec_{n-1}"Dx: 
  Z_n(w) = (prod over faces Delta_face) * (gauge factor) * Z_{n-1}(w')
Compute prod Delta and gauge for our weight pattern symbolically in terms of counts of face types.
The weight pattern: faces alternate a/b in checkerboard fashion (period 2). Each face is a 4-cycle with edge weights?
In CJ convention, what are the 4 edge weights around face with center (2i+1,2j+1)? Edges connect B-W pairs...
Edges: B(x)-W(y) with weight depending on B class j and direction: e1-dir weight a(1-j)+bj; e2-dir i*(aj+b(1-j)).
Face (2i+1,2j+1): corners are B(2i,2j+1)? Let's enumerate: face center (2i+1,2j+1), vertices (2i,2j+1)B? (2i mod 2=0, 2j+1 odd → B ✓), (2i+2,2j+1)B, (2i+1,2j)W, (2i+1,2j+2)W.
Edges: B(2i,2j+1)-W(2i+1,2j): diff (1,-1) = -(−1,1) = -e2 → e2-dir weight i*(aj+b(1-j)) with j = class of B(2i,2j+1): (2i+2j+1)%4=1 iff (i+j) even → j_class=0 if i+j even else 1.
This is getting complicated but is FINITE casework (i+j parity × n parity). The shuffle orbit: after one shuffle, weights transform; Chhita-Young showed period 4 for (a,b) two-periodic.
For the DRAFT proof, we don't need to re-derive the shuffle from scratch: we can PRESENT the recurrence as a Lemma with proof via urban renewal counting (standard, following Elkies-Kuperberg-Larsen-Propp §X / Propp's "generalized domino shuffling" Theorem), computing the explicit factors for our pattern.
The KEY computations to verify NOW (numerically→symbolically):
  (i) # of a-faces and b-faces in Aztec_n (depends on n mod 2? mod 4?).
  (ii) Delta per face type, gauge exponents, pendant weights.
Let's just count faces by type for n=1..8 and see pattern.
Face type: (i+j) mod 2? or mod 4? CJ: face weights alternate product 1, b²/a², ... by (i+j)mod 4. With b=1: types by (i+j)%2: even→? Let's define face "a-face" if its 4 edges have weights involving a...
Simpler: compute Delta_face = ac+bd for each face directly from Kasteleyn matrix entries (edge weights = |K entries|), then tabulate by (i,j) parity.
"""
import numpy as np
from collections import defaultdict
def face_deltas(n,a,b=1.0):
    # vertices
    W = set((i, j) for i in range(1, 2*n, 2) for j in range(0, 2*n+1, 2))
    B = set((i, j) for i in range(0, 2*n+1, 2) for j in range(1, 2*n, 2))
    def wgt(bv, wv):
        # |K(b,w)| per CJ (2.3)
        (x1,x2)=bv; (y1,y2)=wv
        d=(y1-x1,y2-x1) if False else (y1-x1,y2-x2)
        s=(x1+x2)%4; j=0 if s==1 else 1
        if d==(1,1): return a*(1-j)+b*j
        if d==(-1,1): return a*j+b*(1-j)
        if d==(-1,-1): return a*j+b*(1-j)
        if d==(1,-1): return a*(1-j)+b*j
        return None
    out={}
    for i in range(0,n):
        for j in range(0,n):
            c=(2*i+1,2*j+1)
            vB1=(2*i,2*j+1); vB2=(2*i+2,2*j+1); vW1=(2*i+1,2*j); vW2=(2*i+1,2*j+2)
            e=[wgt(vB1,vW1),wgt(vB1,vW2),wgt(vB2,vW1),wgt(vB2,vW2)]
            # cyclic order around face: B1-W1, B2-W1? need adjacency: B1=(2i,2j+1): W1=(2i+1,2j): diff (1,-1) ✓ edge; W2=(2i+1,2j+2): diff (1,1) ✓.
            # B2=(2i+2,2j+1): W1: diff (-1,-1) ✓; W2: diff (-1,1) ✓. Cycle: B1-W1-B2-W2-B1. Opposite pairs: (B1W1,B2W2),(B1W2,B2W1).
            Delta=e[0]*e[3]+e[1]*e[2]
            out[(i,j)]=(tuple(e),Delta)
    return out

for n in [2,3,4]:
    fd=face_deltas(n,0.7)
    print(f"--- n={n} ---")
    by=defaultdict(list)
    for (i,j),(e,D) in fd.items():
        by[(i+j)%2].append(D)
    for p in sorted(by):
        print(f"  parity {p}: count={len(by[p])} deltas={sorted(set(round(d,9) for d in by[p]))}")
