# Independent mathematical audit

## correctness

PASS

With per-edge unit jump rates and killing at the two sites, the positive definite killed Laplacian yields the vector of lifetimes x by solving (L+D)x=1. If t and u are the trap rates times their local lifetimes, then t+u=n. Applying L^+ gives x=T*1-t L^+ e_a-u L^+ e_b for the uniform mean over all sites. Constant diagonal g and off-diagonal g-d give (1/kappa_a+d)t=(1/kappa_b+d)u, hence T/n=g+(1-d^2 P)/(K+2dP). For distinct sites d=R_eff/2>0; the derivative with respect to P is strictly negative at fixed K. AM–GM gives the unique equal split, at which T=n/K+ng-n R_eff/4, proving the placement and budget conclusions. For the 3-by-3 torus, using the zero and nonzero eigenspace projectors of the three-cycle in each factor gives Green diagonal 2/9 and Green off-diagonals 0 and -1/18 for adjacent and diagonal sites, respectively; the example follows. The supplied verify.py and VERIFICATION.md were inspected, not run. The sampled solves are corroboration, not proof of optimality over all graphs.

## originality

FAIL

The exact two-trap formula and its optimizer are direct specializations of a prior arbitrary-rate killed-resolvent formula in terms of the unkilled pseudoinverse, not just comparable to a one-perfect-trap result. In Jacobsen–Tien, sections 2.3 and 3.1–3.2, combine Theorems 4 and 5 at z=1. Write G=L^+, v=(kappa_a e_a+kappa_b e_b)/K, W=(I-1 v^T)G(I-v 1^T). The prior formula is (L+D)^(-1)=11^T/K+(I+WD)^(-1)W. If positivity of all rates is required, let positive rates at other sites tend to zero: L+D remains positive definite in the limit and I+WD stays nonsingular, as W is positive semidefinite and D is nonnegative. For alpha=kappa_a/K, beta=kappa_b/K and q=(beta,-alpha)^T, the trap block is W_SS=2d q q^T, W_S,: 1=-n d (alpha-beta)q, and 1^T W 1=n^2(g-2d alpha beta). Substituting these into the prior resolvent by the rank-one inverse formula gives T/n=1/K+g-2dP/K^2-d^2(1-4P/K^2)P/(K+2dP)=g+(1-d^2P)/(K+2dP). The claimed rate optimization is then immediate from monotonicity in P and AM–GM; at equal rates its resistance dependence is affine with negative slope, giving the placement rule. This is demonstrated prior implication, not a claim that the exact wording appears in the prior paper.

## value

FAIL

Placement and allocation of finite-rate traps are naturally motivated and the resistance form is a useful presentation. As a standalone scientific finding, however, the lifetime is mechanically obtained from the existing general absorption-resolvent theorem, and the two optimization statements reduce to strict monotonicity of one scalar rational function, AM–GM, and a linear ranking. The submitted record does not establish a distinct non-routine invariant or design principle beyond this specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
