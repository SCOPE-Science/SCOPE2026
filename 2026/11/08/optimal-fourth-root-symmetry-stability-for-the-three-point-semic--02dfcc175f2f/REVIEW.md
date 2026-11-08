# Scientific review

## Correctness — PASS
The core assertion is quantitatively verified from the anchored-semicycle formula, the exact centering identity, a Fourier coefficient calculation, Parseval, and an integration-by-parts interpolation inequality. Every constant has been reconstructed: in particular \(\|u\|_2^2=8\pi\sum_{k\,\mathrm{odd}}|\widehat f(k)|^2/k^2\) and \(\|h'\|_2\le 2L\sqrt{2\pi}\), yielding exactly \(3m/(2\pi^3L^2)\). The bounded-Lipschitz sharpness family satisfies the stated lower density bound, and its exact deficit and TV distance scale as the fourth and first powers of frequency respectively. The standalone verifier performed exact-integration tests and 280,000 sampled triples. These experiments supplement rather than replace the proof.

## Originality — PASS, with explicit historical limits
Wendel (1962) proves the zero-deficit probability for centered distributions. Crucially, Wagner and Welzl (2001) already prove the extremal bound and characterize balanced equality: **neither is claimed as original**. The present claim is an explicit quantitative inverse modulus, a frequency-resolved deficit estimate, and an optimal Hölder exponent. Searches in published research records and readable primary comparisons found no covering statement with these conclusions. The 2022 spindle-convex adaptation concerns a different hull operation. More general historical stability literature could cover the incremental theorem; priority remains provisional.

## Value — PASS
The fourth-root exponent is a concrete geometric-statistical rigidity boundary: small excess semicircle probability forces nearly antipodal angular sampling only under regularity, while high frequency creates optimal ill-conditioning. This addresses a motivated question left open by a qualitative extremum and includes a sharpness obstruction, not a routine restatement of Wendel.

## Limitations
The exact numerical coefficient in the TV inequality is not asserted optimal. The theorem concerns the distance to antipodal symmetry, not to uniform angular law, and does not treat estimation from finitely many samples. No independent audit or priority certification has been performed.

Self-review: passed. Independent audit: not yet performed.
