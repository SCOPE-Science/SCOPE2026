# Independent mathematical audit

## correctness

PASS

Conditional on the best arriving at i, the earlier record indicators have independent probabilities 1/j. For i>b, a success with two choices uses either no record in (b,i), or one record j in (b,i) with none in (a,j) or (j,i). This gives the mass ratio in RESULT.md lines 62–67 after separate normalization. Positive mass on (a,b] excludes reverse order. The strictly increasing ratio on the common tail makes the CDF difference decrease and then increase to zero; the sign at N-1 is opposite to the last mass difference, which has the sign of Z. Thus Z=0 is ordered and Z>0 gives exactly one crossing in sign, allowing a zero plateau in discrete time. The largest optimal cutoffs can be justified independently of the cited rounding theorem. In backward record dynamic programming F_m(i) is optimal future success with m choices after i positions, and G_m=F_m−F_{m−1}; a record at i is accepted if i/N>G_m(i). The update F_m(i−1)=F_m(i)+(i/N−G_m(i))_+/i preserves 0≤G_2≤G_1 and makes both marginals nondecreasing backward. The reject-on-ties cutoffs are nested. The increments of N times success as b or a increases by one are S(b+1)−1 and V(a+1)+(S²−T)/2−1, respectively (holding b fixed for the latter). Expanding the two inequalities at consecutive maximizing integers gives the stated floors with O(1/N) perturbations and shifts (1−e^(−1))/2 and (1−e^(−1/2))/2. Direct substitution gives NZ=−1+2u/e^(−1)−v/e^(−3/2)+O(1/N). Lindemann–Weierstrass and Kronecker–Weyl make the shrinking bands around the rounding boundaries and sign line density zero. The subgraph of the straight sign line has the reported area. The relationship-to-prior-work paragraph calls this region curved; the proof and area formula correctly use a straight boundary.

## originality

PASS

The strongest available evidence places optimal policy, totals and integer rounding in prior work. Credit the separate conditional timing order, terminal-mass criterion and resulting arithmetic density, not the policy or rounding shifts. No distinct equivalent or stronger result was established by the searches; primary-text access remains limited.

## value

PASS

Separate success conditioning changes the timing question in a way total success and threshold optima cannot answer. The exact criterion covers all nondegenerate cutoffs, exposes a one-crossing mechanism, and shows that comparison fails on a positive limiting proportion of optimal integer horizons even though the continuum leading values coincide at the sign threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
