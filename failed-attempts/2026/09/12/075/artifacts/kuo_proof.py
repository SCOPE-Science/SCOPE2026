"""Prove recurrence via Kuo condensation with EXPLICIT corner analysis.
Kuo (2003/2004) condensation for Aztec diamond with arbitrary edge weights:
We use the version: Let G = Aztec_n. Let a,b,c,d be the four "corner" vertices in cyclic order
(two black, two white alternating? or same color?). The identity:
  M(G) M(G - {a,b,c,d}) = M(G-{a,b}) M(G-{c,d}) + M(G-{a,d}) M(G-{b,c})
For Aztec: removing adjacent corner pairs forces edges, reducing to Aztec_{n-1} (times forced-edge weight);
removing all four corners reduces to Aztec_{n-2} (times forced weights).
The two terms on RHS: one corresponds to matching corners "straight" (giving Z_{n-1}^2 times weights),
the other to "cross" matching. For the Aztec region with our weights, one of the two terms VANISHES
or they combine to give R factor? In uniform case: M(G)M(G-4corners) = 2 M(G-2corners)^2? Hmm need both terms nonzero?
Actually for uniform Aztec: the identity gives Z_n * (2^{...} Z_{n-2}) hmm.
Let me just directly verify the combinatorial reduction numerically:
  G - {corners}: remove 4 extreme vertices; forced edges propagate; remaining graph = Aztec_{n-2} + forced weight.
Which 4 vertices? The extreme tips: e.g. W(1,0) [bottom], W(2n-1,2n)?? Hmm tips alternate colors.
Simplest: test all 4-corner removals and see which reduced determinants equal (monomial)*det(K_{n-2}).
"""
import numpy as np, itertools, math
from kasteleyn import build_K, logZ
def Wlist(n): return [(i, j) for i in range(1, 2*n, 2) for j in range(0, 2*n+1, 2)]
def Blist(n): return [(i, j) for i in range(0, 2*n+1, 2) for j in range(1, 2*n, 2)]
def ddet(n,a,delB,delW):
    K=build_K(n,a)
    B=Blist(n); W=Wlist(n)
    bi={b:k for k,b in enumerate(B)}; wi={w:k for k,w in enumerate(W)}
    keepR=[bi[b] for b in B if b not in set(delB)]
    keepC=[wi[w] for w in W if w not in set(delW)]
    M=K[np.ix_(keepR,keepC)]
    assert M.shape[0]==M.shape[1], (M.shape,)
    return np.linalg.det(M)

a=0.7; n=5
D5=ddet(n,a,[],[])
print("det5=",D5," Z5=",math.exp(logZ(5,a)))
# Candidate: remove bottom tip W(1,0) and top tip W(2n-1,2n)? These are both white; need balanced removal (equal B and W).
# Kuo corners for Aztec: two black + two white, one of each at each... Let's try: delB={(0,1),(2n,2n-1)}, delW={(1,0),(2n-1,2n)} (diagonal tips)
d=ddet(n,a,[(0,1),(2*n,2*n-1)],[(1,0),(2*n-1,2*n)])
D3=ddet(n-2,a,[],[])
print("4-corner minor=",d," det3=",D3," ratio=",d/D3)
# adjacent-pair removals
for delB,delW in [([(0,1)],[(1,0)]), ([(2*n,2*n-1)],[(2*n-1,2*n)]), ([(0,1),(0,2*n-1)],[(1,0),(1,2*n)])]:
    d2=ddet(n,a,delB,delW)
    D4=ddet(n-1,a,[],[])
    print(delB,delW,"minor=",d2," det4=",D4," ratio=",d2/D4)
