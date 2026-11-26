# Independent mathematical audit

## correctness

PASS

Recounting legal moves gives stationary weights (2,1,2m−2)/(2m+1) and rates (2m,2,4) for hub occupied, same blade and distinct blades. In particular the same-class marked rates are 1 and 2 in the first and third classes, not zero. In the tilted eigenvalue calculation stationarity gives πT=π diag(r), so the variance rate is μ+2⟨r−μ,h⟩ with −Qh=r−μ. The two leaf equations give h_B−h_A=(2−μ)/2 and h_C−h_A=(4−μ)/2. Substitution yields F=1+[π_B(2−μ)^2+π_C(4−μ)^2]/μ. Independent exact simplification in /workspace/review_checks.py confirms the rational formula and its consecutive difference; the difference is positive for m≥2, F_2=29/25 and the leading coefficients give 5/3. For fixed y=e^z>0 and T<∞ the fast variation-of-constants equation bounds u_A by a fixed constant times 1 plus the running suprema of u_B,u_C. The two slow equations then give a uniform Grönwall bound and u_C has a bounded derivative. The initial-layer term has L1 norm O(1/m), the u_B forcing contributes O(1/m), and the fast convolution differs in L1 by O(1/m) from y u_C (bounded derivative and decay of its kernel). Thus the last equation converges to u_C'=(2y²+2y−4)u_C, u_C(0)=1; π_C→1. This establishes convergence of the stationary MGF at every real z, and hence the asserted fixed-time law. It includes t=0 and does not assert path convergence or interchange the graph-size and long-time limits.

## originality

PASS

The graph-specific Fano factor and its sharp monotone limit, together with the fixed-time singleton/doublet law, are distinct in the inspected sources. The general non-Poisson verdict, stationary edge-count mean method and tilted activity machinery are not new. The exact two-token Laplacian result overlaps on the state graph but not on the dynamic counting invariant.

## value

PASS

A windmill separates ordinary peripheral jumps from rapid, counted hub excursions in a natural sparse interacting-particle model. The exact finite-size noise and monotone excess, and especially the fixed-time jump-size decomposition, resolve information that the generic non-Poisson classification doesn't give. The law explains why fast visits of vanishing stationary occupancy contribute a positive excess variance and gives a quantitative comparison point for other exclusion networks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
