# Independent mathematical audit

## correctness

PASS

With Ad nonsingular, B full row rank and H(S1)>0, S1 and S2 are accretive/invertible since H(S1^-1)=S1^-T H(S1) S1^-1>0 and H(S2)=B H(S1^-1) B^T>0. For mu=lambda_min H(S2)>0, the resolvent bound ||E||_2 <=alpha/(mu+alpha)<1 follows by the quadratic form. Exact multiplication of K and Q_alpha^-1 gives T=[[I,0,0],[X,-I,0],[0,E Z,I-E]]. Directly I-T^2 has last row [-E ZX,E^2 Z,E(2I-E)] and no other nonzero rows. Multiplying this row successively by I-T proves for every m>=2 the exact p_m(T) last row [-E^(m-1)ZX,E^m Z,E^(m-1)(2I-E)]. Since p_m(0)=1, it is a valid candidate in exact unrestarted right-preconditioned GMRES, and its norm yields ||r_m|| <= M_alpha [alpha/(mu+alpha)]^(m-1) ||r0||. Identical argument from each restarted-cycle residual gives the per-cycle factor, not a guarantee of one-cycle contraction for all m and alpha. Fixed matrices yield bounded M_alpha as alpha->0. The example d=v=p=1, Ad=As=B=1,G=0,r0=(1,1,1) has exact least-squares squared residual 2alpha^2/(1+alpha+alpha^2), hence sharp two-step alpha order. Independent random nonsymmetric accretive tests verified 576 matrix-polynomial identities for sizes 3–11 and m=2..7 with maximum Frobenius error 6.58e-14, plus exact symbolic scalar residual identity. Finite checks supplement, not replace, the all-m matrix induction.

## originality

PASS

Qualified best-of-knowledge PASS. Chao–Li (October 2026) explicitly supplies the exact KQ_alpha^-1 block and the Moebius Schur transform, not an analytic GMRES-rate theorem; it expressly cautions against inferring a nonnormal convergence rate from eigenvalues. The reviewed contribution is the concrete polynomial p_m=(1-t^2)(1-t)^(m-2), its exact last-row E^(m-1) expression and a Euclidean all-iteration and restarted-cycle bound with sharp two-step alpha order. Southworth–Sivas–Rhebergen supply general 2-by-2 Schur GMRES machinery but not the complete three-block specialized formula or lower witness. Greif–He and Beik–Benzi use different preconditioners. Search absence is not proof of novelty; a non-obvious generic 2-block theorem instantiation or unindexed paper remains a residual historical risk.

## value

PASS

The model-specific problem is natural: spectral clustering of the same nonnormal, fully coupled ideal Stokes–Darcy preconditioner does not control GMRES by itself, as its introducing paper explicitly observes. The exact residual-polynomial hierarchy supplies a usable quantitative all-iteration bound and a sufficient restarted-cycle contraction criterion, and the three-dimensional witness shows that the first alpha-order improvement after two steps is genuinely sharp. These establish a motivated finite-dimensional structural fact about algorithmic convergence beyond generic eigenvalue information, while transparently excluding mesh-uniform and inexact-preconditioner claims. The proof is short and uses standard algebra, but the exact model-dependent formula and sharp obstruction are not merely a renamed known table or an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
