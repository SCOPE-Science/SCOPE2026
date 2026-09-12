"""Dodgson condensation on Kasteleyn matrix: find 4-periodic recurrence.
Idea: K_n has a corner 2x2 block structure. Let b0 = corner black vertex (0,1), w0 = corner white (1,0).
Jacobi: det K_n * det K_n^{b0,w0} ... hmm K is rectangular-indexed (B x W). Dodgson needs square matrix with two deleted rows AND cols.
Take rows b_S=(0,1) [west tip black], b_E=(2n,1)? and cols w_S=(1,0), w_E=(2n-1,0)?
Actually Kuo's theorem for Aztec (Kuo 2004, "Applications of graphical condensation...", Theorem 2.1?):
  For Aztec diamond region with edge weights, with vertices w,x,y,z around... 
Standard corollary (uniform): M(A_n) M(A_{n-2}) = 2 M(A_{n-1})^2? Hmm factor 2.
Let me instead directly TEST candidate Dodgson identities on the numeric K matrices to discover the exact algebraic identity,
then the proof is just "expand determinant" (verifiable symbolically for general n by block structure).
Test: det(K_n) * det(K_n without rows {b1,b2} and cols {w1,w2}) vs det(K_n\b1,w1)*det(...) - det(...)*det(...).
Choose b1=(0,1),w1=(1,0) (west-bottom corner edge), b2=(2n,2n-1)?,w2=(2n-1,2n) (east-top corner edge)?
"""
import numpy as np
from kasteleyn import build_K
def Wlist(n): return [(i, j) for i in range(1, 2*n, 2) for j in range(0, 2*n+1, 2)]
def Blist(n): return [(i, j) for i in range(0, 2*n+1, 2) for j in range(1, 2*n, 2)]

def subdet(n,a,delB,delW):
    K=build_K(n,a)
    B=Blist(n); W=Wlist(n)
    bi={b:k for k,b in enumerate(B)}; wi={w:k for k,w in enumerate(W)}
    keepR=[bi[b] for b in B if b not in delB]
    keepC=[wi[w] for w in W if w not in delW]
    M=K[np.ix_(keepR,keepC)]
    if M.shape[0]!=M.shape[1]: return None, M.shape
    return np.linalg.det(M), M.shape

a=0.7; n=4
D,_=subdet(n,a,set(),set())
print("det K4 =",D)
# try deleting one corner pair: rows (0,1), cols (1,0)
for delB,delW in [({(0,1)},{(1,0)}), ({(0,1),(8,7)},{(1,0),(7,8)}), ({(0,1),(0,7)},{(1,0),(1,8)})]:
    d,sh=subdet(n,a,delB,delW)
    print(delB,delW,sh,d)
