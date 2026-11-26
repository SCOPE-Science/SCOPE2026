# Independent mathematical audit

## correctness

PASS

Anchor the cyclic gap list at a specified sampled point, not at the first point after a fixed coordinate cut. Conditional on its angle the other n-1 rotated angles are independent uniform, so their order-statistic spacings are Dirichlet(1,...,1). This anchoring leaves the cyclic statistic unchanged. Outside the half-circle tie null set, original containment means every gap is <1/2, and deleting a vertex merges its two adjacent gaps. Pivotality therefore requires the merged pair to sum to >1/2. Two disjoint pairs cannot both do this, and any three edges of a cycle of length n>=4 include a disjoint pair. The Beta(2,n-2) tail of an adjacent sum at 1/2 is n/2^(n-1); removing the two disjoint cases with an individual long gap gives per-gap-edge probability (n-2)/2^(n-1). In an adjacent joint event with common gap x<1/2, subtract 1/2-x from each neighboring gap; the residual simplex has total x, so the original neighbors are automatically <1/2 and the remaining gaps are at most x. The joint probability is (n-1) integral_0^(1/2) x^(n-2) dx=2^(-(n-1)). The n joint events are disjoint and exhaust K=2; the expectation and normalization then give K=1 and K=0. Wendel noncontainment is n/2^(n-1), and must be subtracted from K=0 before conditioning on containment. This gives conditional robustness zero at n=4 and 1/11 at n=5. Positive radial scaling does not change any of the containment predicates. The prior-law derivation in the originality assessment independently reproduces the probability algebra.

## originality

FAIL

The mathematical law is correct but is covered by the classical Hodges–Ajne exact semicircle tail together with an elementary first-moment and support calculation. In particular the robustness probability is a direct substitution, and the entire three-mass pivotal spectrum follows, not just one of its entries. This is demonstrated prior implication, not rejection for unavailable papers or an assertion that Hodges used the same pivotal-count wording.

## value

FAIL

Deletion resilience of a random hull is a natural question, and distinguishing one from two pivotal vertices is interpretable. But for this frozen setting the robustness part just changes the threshold in a classical exact scan statistic, and the remaining masses follow from a first-moment subtraction and an elementary cycle observation. The standalone support observation does not establish a genuinely distinct valuable remainder for repair under the exact-invariant standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
