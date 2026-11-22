# Review of the four-site diagonal-loading condition-number theorem

**Correctness (PASS).** The global optimality proof first rules out every asymmetric allocation using strict Rayleigh--Ritz and positivity of the minimal eigenvector. Independent reflection-even/odd blocks produce exact extreme eigenvalues. A derivative with exactly one positive zero establishes the unique per-budget minimizer, and the activation equation has exactly one positive root below \(q=1/2\). Limit statements follow by direct asymptotic analysis. The standalone symbolic and numerical checks supplement this infinite-domain proof.

**Originality (PASS on inspected evidence, with qualification).** Lu and Pong (2011) solve general spectral condition-number optimization using convex programming, but the inspected primary full text does not contain this explicit four-site optimal allocation, strict asymmetry exclusion or active-set root. Torres and Roy (2015) and van den Driessche (1994) address dominant-eigenvalue perturbation, not the largest-to-smallest positive eigenvalue ratio. A prior condition-number loading classification on stars is not a four-site path classification; the two reflection parity blocks here require different arguments. A plausible diagonal-perturbation publication was accessible only as an abstract and literature equivalence is not conclusively excluded.

**Value (PASS).** Four sites are the first unweighted path not isomorphic to a star. The exact budget frontier shows when a controller must begin funding the interior nodes, despite endpoints receiving more gain at every finite budget. Complete optimizer uniqueness across arbitrary four-node asymmetric allocations makes this a usable design rule, not just a symmetric ansatz.

**Boundaries and reproducibility.** Equal edge conductances, common baseline \(\mu>0\), additive nonnegative diagonal gains and a single equal-price budget are essential. No arbitrary-network classification or external independent certification is claimed. `CHECKER.py` reproduces the exact symbolic identities and supplementary numerical comparisons.

Self-review: passed. Independent audit: not yet performed.
