# Independent mathematical audit

## correctness

PASS

The exact residual state has k pendant and k(k-1)/2 core edges, so first-step p_k=2/(k+1) and F_k=(2zF_{k-1}+(k-1)F_{k-2})/(k+1). Summing yields (1-t^2)J_t-2zJ=1 for J=tH; integration gives the PGF. Darboux transfer at t=1, with the t=-1 term lower order uniformly near z=1, gives mod-Poisson asymptotic F_n(z)=2^(z-1)n^(z-1)/Gamma(z+1)(1+O(1/n)); differentiating yields displayed moments and CLT. Parity and X=0 boundaries follow exactly. Independent recurrence/power-series checks through n=4, and n=7 normalized probabilities agree.

## originality

FAIL

A full earlier/same-day published theorem for precisely K_n with pendant leaves, weighted dimer adsorption, gives the complete finite recurrence at every rate w>0, in particular w=1, the exact means, the same logarithmic Gaussian law and matching parity. Thus the central distribution is already completely determined; solving the published recurrence into a hyperbolic generating function and extracting a variance constant is a routine refinement, not a distinct surviving original theorem. Publication dates are both November 8; ordering within day is unknown, so coverage is assessed without invented chronology.

## value

FAIL

The natural matching-loss phenomenon is valuable mathematically but already established for the larger weighted family with a stronger weak-channel Poisson crossover. Remaining closed-form OGF and routine cumulant constant do not amount to a motivated new independent mathematical fact beyond the exact known recurrence and Gaussian theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
