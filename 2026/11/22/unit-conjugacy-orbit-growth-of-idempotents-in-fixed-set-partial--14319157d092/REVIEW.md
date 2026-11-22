# Scientific review: unit-conjugacy orbit growth of fixed-set partial idempotents

## Correctness — PASS

An idempotent partial map has each image point fixed and hence decomposes into rooted stars plus undefined vertices. The prescribed set can contain only fixed roots or undefined points. The unit group fixes that set pointwise and acts as every permutation on the remaining points. The proof classifies precisely the permissible decorated star multisets, derives the orbit stabilizer by explicit block permutations, and obtains both rank enumerators by independent choices of roots and labeled species. The asymptotic reduction to the Hardy–Ramanujan partition estimate is supplied in the proof, including treatment of the convolution tails. The standalone checker enumerates all parameter pairs with \(0\le a\le3\), \(0\le b\le4\), and verifies actual conjugacy orbits, ranks, stabilizers, and generating-function coefficients. These tests are supportive, not an infinite proof.

## Originality — PASS relative to inspected sources

The 2022 paper of Wijarajak and Chaiya establishes Green's relations and regularity for this precise partial fixed-point-set monoid, and its abstract does not state an orbit census. Their 2023 follow-up was inspected across its text, including its results about abundance, unit regularity, and coregularity; its unit group observation is credited. A 2016 full-transformation predecessor treats a different monoid and natural orders. Araújo and collaborators' general digraph-isomorphism criterion already yields the qualitative uncolored permutation-conjugacy framework; no novelty is claimed for that criterion. The present claim concerns the exact fixed-set decorated orbit sizes, rank-refined series, and fixed-distinguished-set partition asymptotic, which are not implied as explicit enumerative identities by the cited published results. Searches for these exact objects, aliases, and quantitative equivalences found no duplicate. The earlier 2022 article's full text was not obtained, and broad prior functional-digraph enumeration may hide an equivalent formulation; these remain genuine priority risks.

## Value — PASS

The complete classification is for every cardinality of each of two natural kinds of points and every idempotent, not a chosen slice. It makes the distinction between counting labeled elements and counting symmetry classes explicit, determines all orbit and stabilizer sizes, and shows a nontrivial partition-growth enhancement. The vanishing fraction of orbit types with any missing distinguished point is a further quantitative behavior of the symmetry quotient. This supplies a usable invariant and enumeration tool for a natural transformation-monoid family studied for regularity and structure.

## Limitations

This is a unit-conjugacy result for idempotents, not all semigroup conjugacies or all endomorphisms. The limiting assertion is for fixed \(a\); the 2022 paper was accessible at abstract level only. The partial map and unit-group cases \(a=0\) or \(b=0\) are included. Independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
