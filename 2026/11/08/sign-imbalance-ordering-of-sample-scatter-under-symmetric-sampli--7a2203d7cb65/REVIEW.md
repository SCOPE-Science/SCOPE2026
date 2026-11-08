# Self-review

## Correctness — PASS

The theorem is an identity under the specified assumptions: independent identically distributed symmetric, nonzero observations with finite fourth moment. Independent fair signs separate from magnitudes. Conditional cumulants, the mixed term \(\operatorname{Cov}(T,S^2)\), and the unconditional fourth-moment identity yield the two conditional formulas. The positive coefficient \(B\) is justified by a strictly positive independent-copy representation whenever magnitudes are nonconstant. The explained-variance identity follows from the binomial fourth moment. A standalone exact-rational checker reproduces 516 independent assertions for finite-support distributions. The infinite statements rest on the analytic proof, not enumeration.

## Originality — PASS, qualified

Searches for conditional sample variance given the sign count, symmetric-sample scatter versus positive-minus-negative imbalance, sign-test and variance dependence, and related quadratic-form representations found no matching full statement. Dixon–Mood (1946) treats the sign test; Ekström–Jammalamadaka (2007, first available online in 2006) treats a different spacing-based symmetry statistic and its asymptotic dispersion. Full sections and appendix of the latter author's hosted manuscript were inspected. Standard half-normal moment references supply moments, not the conditional variance monotonicity or explained fraction. The formula may nevertheless be implicit in general quadratic-form moment identities; historical priority is not exhaustively established. Inaccessible older sources are not asserted to exclude the theorem.

## Value — PASS

The sign test uses only whether observations cross a fixed center, while sample scatter is a magnitude-and-sign statistic. Zero ordinary correlation between their raw statistics could misleadingly suggest absence of dependence. The exact nonlinear regression and a **universal** conditional-variance ordering separate these notions, quantify how much scatter is predictable from signs, and identify the finite-sample Gaussian benchmark \(4/(\pi^2n)\). The same theorem handles arbitrary continuous or discrete symmetric magnitude laws with finite fourth moment, including a deterministic-magnitude equality boundary. This is more than a moment-table substitution, though no new test optimality is claimed.

## Closest references and limitations

Dixon and Mood, *The Statistical Sign Test*, 1946, DOI 10.1080/01621459.1946.10501898; Ekström and Jammalamadaka, *An asymptotically distribution-free test of symmetry*, 2007, DOI 10.1016/j.jspi.2006.06.009; Byers, *Half-Normal Distribution*, 2014, DOI 10.1002/9781118445112.stat05864. The standard general quadratic-form literature may give equivalent consequences. No assertion of all-order stochastic dominance or applicability without symmetry and finite fourth moment is made.

Self-review: passed. Independent audit: not yet performed.
