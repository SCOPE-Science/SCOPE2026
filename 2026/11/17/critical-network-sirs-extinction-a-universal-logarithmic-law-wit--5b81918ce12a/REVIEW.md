# Independent mathematical audit

## correctness

PASS

Verified the exact invariant population triangle y_i>=0,z_i>=0,y_i+z_i<=1 and Perron identity at rho(Gamma^-1 W)=1 for irreducible W: A=W-Gamma has a simple zero eigenvalue v>0 and w>0, u=w^T y, u'=-w^T[(y+z)⊙Wy]<=0. Every positive-infection trajectory becomes strictly componentwise infected; LaSalle yields (y,z)->0. Relative slow variation u(t-r)/u(t)->1 and exponential stable semigroups yield y=vu+p u²+o(u²), z=h u+q u²+o(u²), h=Delta^-1 Gamma v, Ap=b-Kv on w^T p=0, q=Delta^-1(Gamma p+Kh), K=w^T[(v+h)⊙Wv]>0. Multiplication gives u'=-Ku²-Lu³+o(u³), so t y->v/K, t z->h/K and (u^-1-Kt)/log t->L/K (not necessarily O(1) remainder). Independently used symbolic matrix algebra on the exact specified W=[[3/4,1/4],[1/2,3/2]], Gamma=diag(1,2), Delta=dI: w=(2/3,1/3), v=(1,1), exact Ap projection, K=2(2d+3)/(3d), L/K=-(8d³+45d²+27d-54)/(9d²(2d+3)). Its cubic has strictly positive derivative on d>0, unique root 0.795652212912595; sign reverses. Finite symbolic checks corroborate but do not prove global critical trajectories.

## originality

PASS

Gatti–Como prove the disease-free spectral threshold and global attraction for finite deterministic network SIRS; they do not provide these two-scale Perron coefficients in inspected accessible material. The indexed 2026 SIRCm and adaptive SIS critical logarithm results concern different state variables/vector fields; their B sign parameter is feedback, whereas the present explicit sign reversal varies immunity-waning d in a directed irreducible 2-node SIRS. No inspected publication implies the exact p,q,L or this parameter-specific polynomial. Full text of potentially relevant Gatti–Como SIRS source was not retrievable during this run, so priority is best-of-knowledge with explicit residual risk, not an access-based automatic FAIL.

## value

PASS

The exact network SIRS threshold is a mathematically natural nonhyperbolic boundary where exponential stability no longer controls extinction rates. A universal directed-network spatial Perron profile, a computable second-order projected correction and a one-parameter sign reversal in that correction offer meaningful structural asymptotics beyond the original reproduction threshold; equations and coefficients are specific to the original epidemic flow.

The dated certificate retains the supplied scientific assessment, sources and limitations.
