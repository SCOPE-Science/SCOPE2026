# Independent mathematical audit

## correctness

PASS

The actual rational stability function is F(z)=(z²-6z+12)/(z²+6z+12). Since the SRG adjacency algebra is span(I,A,J), its Laplacian has eigenvalues 0,alpha,beta with alpha+beta=s, alpha beta=N mu. Exact spectral projector algebra gives nonedge entry 12alpha beta h²(6+sh)/(N D_alpha D_beta)>0 and edge entry 12h[12+6p h/N+p(s-N)h²/N]/(D_alpha D_beta). The diagonal is positive from F(h alpha), F(h beta)>0. The sign quadratic has a single positive root iff s<N; row/column sums equal one. I independently inverted the 10x10 Petersen rational matrix at h=4: diagonal 1783/4123, nonedge 408/4123, edge -36/4123, row sum 1. At h=0 offdiagonals vanish as required.

## originality

PASS

The exact same SRG classification was subsequently published as “Sharp Gauss–Legendre heat-step positivity on strongly regular graphs”; its Resultary commit is timestamped 2026-11-09T01:09:49Z while the assigned source package was imported 2026-11-08T22:34:30Z. This establishes mathematical equivalence and a later *observed publication commit*; it is not proof of research priority or independence. The older 2010 Padé positivity literature gives method-level conditions and directed counterexamples but not the full SRG adjacency/nonedge criterion. This PASS is chronology-qualified and requires human priority reconciliation if external publication dates emerge.

## value

PASS

The all-SRG, all-timestep positivity frontier is a natural exact spectral-integration property with an explicit sharp graph-parameter dichotomy and informative examples (Paley, Petersen, triangular graphs). It separates componentwise monotonicity from positive spectral stability; not merely routine application of absolute-monotonicity radius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
