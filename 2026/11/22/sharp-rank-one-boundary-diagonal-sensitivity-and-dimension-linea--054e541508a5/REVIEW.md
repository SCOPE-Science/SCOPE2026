# Scientific review: rank-one-boundary semidefinite projection sensitivity

## Correctness — PASS

The projection is the spectral positive part. Malick–Sendov's separated-eigenspace divided difference yields exactly \(D\Pi(P-\eta Q)[H]=PHP+(PHQ+QHP)/(1+\eta)\), so the rank-one boundary derivative limit is legitimate without assuming differentiability at the singular limit. Expanding its first diagonal entry into independent real symmetric perturbation coordinates gives a sum of absolute coefficients. The Cauchy–Schwarz equality condition fixes the equal-magnitude complement, producing the exact one-parameter profile. The derivative's sign and strict curvature on the critical interval prove a unique maximizing mass for every \(n\ge3\); the complementary interval is excluded algebraically. Interior nonsingular finite-pair perturbations realize the limiting lower bound, while Frobenius nonexpansivity gives the global upper bound. The asymptotic expansion is obtained from the unique root. The included standard-library checker passed 2,843 supplementary assertions. Its finite numerical sampling does not replace the dimension-uniform proof.

## Originality — PASS, with historical-priority risk

The existing exact two-by-two projection result already supplies \(3/2\) and a dimension-independent higher-order embedding lower bound; its \(n=2\) case is excluded from the claim of novelty. The Malick–Sendov source contains the general positive-cone derivative, Ding–Sun–Sun–Toh contains spectral-map differentiability and Lipschitz transfer principles, and Goulart–Nakatsukasa–Rontsis studies projection-error estimates in Frobenius norm. These are important antecedents, but none of the inspected statements gives the optimized all-dimensional rank-one boundary diagonal coefficient or the conclusion \(\mathcal L_n=\Theta(n)\) in maximum-entry norm. The new result requires a distinct coordinatewise dual-norm extremization rather than merely restating the pre-existing Jacobian. Searches cannot establish universal publication priority, and an older or unindexed exact extremal calculation remains possible.

## Mathematical value — PASS

Projection onto positive semidefinite matrices is a standard matrix repair operation. Hilbert-space nonexpansivity alone offers no dimension-independent guarantee in a coordinate maximum norm. The finding calculates the sharp directional worst case on the natural low-rank boundary, classifies its extremizing eigenvector geometry, and resolves the previously unquantified dimensional order of unrestricted entrywise sensitivity: it grows linearly. This is a structural robustness boundary, not an arbitrarily chosen numerical parameter or a claim that the exact global coefficient is already known.

## Scope and limitations

The exact constant pertains to the stated limiting derivative class, not to all matrix pairs. The unrestricted global coefficient is bounded above and below but not exactly determined. The analysis is for real symmetric inputs, a Frobenius objective and the maximum absolute-entry perturbation norm. Existing exact two-dimensional results are acknowledged; historical priority remains subject to further literature discovery.

Self-review: passed. Independent audit: not yet performed.
