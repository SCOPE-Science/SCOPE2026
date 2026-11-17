# Independent mathematical audit

## correctness

PASS

The binary greedy-arch index equals number of shortest prefixes containing 0 and 1. The one-sided forbidden contiguous factor 1^(r+1) is tracked with E_j,Z,O_j states and one-run length j<=r; eliminating states gives exactly F_r(z,u)=(1+z-z^(r+1)-u z^(r+2))/(1-z-2u z²+u z^(r+2)+u² z^(r+3)). The constant-universality layer is 1 empty, 1+1_(n<=r) for n>=1. Minimal j-universal length=2j, with k+1 witnesses for r=1 and 2^k for r>=2. Simple dominant root at u=1 gives mu_r via Q_u/(rho Q_z) for fixed r; rho_r is the unique root Σ_{j=1}^{r+1}rho^j=1, and mu_r->1/3. Independently brute-enumerated all legal strings up to n=10 for r=1..5, checked literal subsequence index and coefficient recurrence; C PASS for all fixed integer r>=1 by finite-state and analytic proof.

## originality

PASS

2026-10-25 and 2026-11-02 complete Resultary theorems count the different language in which BOTH 0 and 1 runs are capped. The present language only forbids long 1-runs while allowing arbitrarily many consecutive zeros. Their distributions and rates cannot be specialized to this language by setting the same cap or changing variable names. 2023 regular-language algorithms can compute each fixed automaton instance, but give no inspected parameter-uniform one-sided full bivariate formula and explicit mu_r. O PASS best of knowledge, retaining generic algorithm/unindexed transfer literature risk.

## value

PASS

A one-sided homopolymer run constraint is a natural non-symmetric regular language; the full universality index profile, sharp discontinuity at r=1 for minimal witnesses and explicit nonmonotone typical-rate phenomenon mu_2>mu_infinity=1/3 give a motivated all-parameter structural theorem. A closed rational family and its asymptotic consequence are independently useful and not a small arbitrary finite slice. V PASS.

The dated certificate retains the supplied scientific assessment, sources and limitations.
