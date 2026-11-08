# Self-review

## Correctness (PASS)

The first-step moment equations are checked with the walk stopped upon first hitting the external parent. Substituting the exact mean \(2s_v-1\) yields a finite recursive variance identity; expanding it establishes the weighted fringe-subtree sum without any appeal to finite enumeration. Discrete convexity of \(u(u-1)\) yields the unique balanced lower extremizer; strict increasing increments of \(F(u)=\frac83(u^3-u)\) yield the unique path-plus-leaves upper extremizer. Equality cases are valid also at the small boundary orders, and the attached exact-rational verifier independently checks all rooted shapes of orders two through eight. No claim of computer-proved infinite quantification is made.

## Originality (PASS, provisional)

The closest structural precedent is Aldous–Fill, §5.3, Theorem 5.20, which supplies a general formula for the variance of tree first-passage times, including an adjacent edge. That identity is acknowledged, and no new general variance formula is claimed. The assessed new conclusion instead solves the *optimization* at fixed starting-side component size and first-edge starting degree, including both sharp numerical bounds and all extremizing rooted shapes, and exhibits an unbounded same-local-data dispersion ratio. Chiclana (2026) proves tree variance lower bounds without this degree-conditioned exact extremal classification in the material examined. The published-literature searches identified no directly matching assertion. Source-access and priority risks are documented in `AUDIT.json`: in particular, a general exact-variance identity provides a strong starting point, while parts of a relevant recent preprint and an older thesis could not be inspected in full.

## Mathematical value (PASS)

Conditional first-passage variance is a natural measurement of dispersion in tree random walks, and a component-size-and-starting-degree constraint is a natural local-data comparison: the mean is fixed automatically by the component size, and the degree fixes the immediate branching. The result completely classifies the extreme variances under this information, identifies structurally different extremizers, and shows that even matching order, marked degrees and mean permit a variance ratio of linear order. This quantifies a genuine limitation of degree-based nonconcentration estimates, rather than a numerical improvement at arbitrary parameter values.

## Limitations and literature comparison

The variance is for a non-lazy simple random walk and a directed traversal of a tree edge, not a general graph or an arbitrary source-target pair. Known exact tree-variance identities must be distinguished from the new sharp fixed-degree optimization. The full texts of Meng Wang's honors project and the later portions of Chiclana's HTML were not accessible during inspection; the broad historical-priority conclusion is therefore provisional. Independent scientific assessment has not occurred.

Self-review: passed. Independent audit: not yet performed.
