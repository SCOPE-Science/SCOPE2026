"""Identify the 5 Dodgson minors as monomials times det(K_{n-1})/det(K_{n-2}) for general a,n.
Conjecture: D11 = u1 * det(K_{n-1}), D22 = u2 * det(K_{n-1}), D12 = v * det(K_{n-2}), cross terms = small/zero?
Then recurrence: Z_n * v Z_{n-2} = u1 u2 Z_{n-1}^2 - cross1*cross2 → R = (u1u2 - cross/v...)/v.
Compute ratios for several (n,a) and guess monomials."""
import numpy as np
from kasteleyn import build_K
def Wlist(n): return [(i, j) for i in range(1, 2*n, 2) for j in range(0, 2*n+1, 2)]
def Blist(n): return [(i, j) for i in range(0, 2*n+1, 2) for j in range(1, 2*n, 2)]
def minor(n,a,delB,delW):
    K=build_K(n,a)
    B=Blist(n); W=Wlist(n)
    bi={b:k for k,b in enumerate(B)}; wi={w:k for k,w in enumerate(W)}
    R=[bi[b] for b in B if b not in set(delB)]; C=[wi[w] for w in W if w not in set(delW)]
    M=K[np.ix_(R,C)]
    assert M.shape[0]==M.shape[1]
    return np.linalg.det(M)
import math
for a in [0.3,0.5,0.7]:
    print(f"===== a={a} =====")
    for n in [3,4,5,6]:
        r1=(0,1); r2=(2*n,2*n-1); c1=(1,0); c2=(2*n-1,2*n)
        D=minor(n,a,[],[])
        D11=minor(n,a,[r1],[c1]); D22=minor(n,a,[r2],[c2])
        D12=minor(n,a,[r1,r2],[c1,c2])
        Dx1=minor(n,a,[r1],[c2]); Dx2=minor(n,a,[r2],[c1])
        Dm1=minor(n-1,a,[],[]); Dm2=minor(n-2,a,[],[]) if n>=3 else None
        print(f"n={n}: D11/Dm1={D11/Dm1:.6f} D22/Dm1={D22/Dm1:.6f} D12/Dm2={D12/Dm2:.6f} Dx1={Dx1:.6f} Dx2={Dx2:.6f} D={D:.6f}")
