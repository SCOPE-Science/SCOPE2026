# Scientific review: power-stabilization index for chain contractions

## Correctness — PASS

The fixed interval is nonempty because the displacement is nonincreasing and changes by at most one; exterior displacements have strict signs. Conditional on a fixed interval, every free exterior adjacent increment is independently and uniformly chosen from zero and one. Distance-to-interval evolution is therefore the *same-word* Bernoulli-prefix recursion \(h\mapsto S_{h-1}\), rather than an unjustified fresh-binomial approximation at each iteration. Uniform Hoeffding bounds for all sufficiently long prefixes, followed by upper and lower geometric-time comparisons, prove the claimed sharp \(\log_2 t\) normalization uniformly over the interval. Previously established fixed-point enumerations imply that the complement is of size \(n-o_{\mathbb P}(n)\) for the unconditional model. Direct map composition agrees with the tail recurrence for every size up to ten in the executable verifier. No finite computation is used as an infinite proof.

## Originality — PASS relative to inspected literature

The 2013 Adeshola–Umar paper, arXiv:1303.7428v2, Proposition 2.3 and Corollaries 2.4/2.9, **already contains the exact joint image-rank/fixed-point enumeration**. That enumeration and its obvious geometric limiting fixed-point distribution are not claimed. The 2021 Fernandes–Paulista paper, arXiv:2112.13427v1, establishes the directed-path weak-endomorphism identification, cardinalities, idempotents, regularity and generator rank. The 2022 Zubairu–Umar–Aliyu paper, arXiv:2205.00438v1, addresses regular/idempotent contraction subsemigroups. Their inspected material does not give asymptotic times until powers stabilize. Two maps of the same image rank and fixed-point count have distinct stabilization indices, so those counts do not imply the new invariant. Targeted research-record searches identified no covering statement. A broader, unlocated random-map iteration theorem remains a residual priority risk; lack of a search hit is not a novelty proof.

## Mathematical value — PASS

The number of powers required to reach an idempotent is a natural invariant of a finite transformation semigroup, directly measuring eventual dynamics beyond static image-rank information. A general worst-case linear bound contrasts with the sharp typical logarithmic law. The statement remains uniform even when the entire fixed interval is prescribed arbitrarily and grows or moves with the chain length. It gives a precise, mathematically motivated asymptotic answer not determined by the previously tabulated rank/fixed-point strata. No additive fluctuation law or publication-priority certification is claimed.

## Evidence and remaining risks

The main scientific evidence is the direct, uniform prefix-sum proof in `RESULT.md` and the independently implemented finite verification in `verify.py`. Close references are arXiv:1303.7428v2, arXiv:2112.13427v1 and arXiv:2205.00438v1. Main risks are a potentially unlocated theorem on iteration depths for this exact random-monotone-map model and the absence of independent mathematical audit. The result is not extended to order-reversing contractions or arbitrary monotone transformations.

Self-review: passed. Independent audit: not yet performed.
