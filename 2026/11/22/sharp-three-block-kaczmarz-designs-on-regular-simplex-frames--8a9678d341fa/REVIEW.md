# Scientific review: sharp three-block regular-simplex Kaczmarz design

## Correctness — PASS
The exact one-step error reduction is the least eigenvalue of the probability-weighted sum of orthogonal row-block projectors. The proof verifies the block projection quadratic form for centered coordinate vectors, decomposes all directions into internal contrasts and a two-dimensional block-mean subspace, and computes the latter's determinant exactly. Every three-block size profile is covered: zero, one, or two singleton blocks. Two independent Rayleigh bounds certify the globally best profile, while strict determinant monotonicity certifies the one-singleton optimum and rules out all remaining alternatives. Equality conditions identify all optimal partitions and probabilities. The standalone exact checker passed 218 assertions (including symbolic identities and full rational characteristic polynomials). These finite computations are supplemental, not the infinite proof.

## Originality — PASS, with publication-priority qualification
Needell–Tropp (2012) introduce uniform-block randomized Kaczmarz and paving-based convergence bounds, but not joint optimization of a simplex-frame partition and its nonuniform block probabilities. Needell–Zhao–Zouzias (2014) extend related randomized block methods to inconsistent data, not this three-block min-eigenvalue optimizer. Gower–Richtárik (2015) explicitly provide the general expected-projection spectral objective and an optimal-probability semidefinite program for fixed candidate samples: their general problem includes this example, but the examined sections do not state or derive the present all-size-profile exact solution and equality classification. Indexed comparison results on simplex row-level probability sampling, block-size noise amplification, and regular-simplex reshuffling address distinct objectives or sampling families. The new contribution is an exact solution of a natural, sharply specified joint discrete-continuous design problem, not the underlying projection method or spectral formulation. Equivalent results in uninspected specialty literature are possible, and published comparison results accessible only through summaries were not treated as exhaustive full-text exclusions.

## Value — PASS
The theorem classifies the unique optimal *shape* of a three-block partition for every simplex size and gives exact best rates even when the size profile is constrained. It exposes a concrete and somewhat counterintuitive structural distinction between block conditioning-oriented balanced pavings and one-step minimax projection coverage: one large block and two singletons win over all balanced partitions for this objective. It also quantifies the gap, \(2/[3(3m-2)]\) relative to uniform three-block sampling. This is a motivated exact experimental-design benchmark for block randomized projection methods, not a claim of lower computational expense per iteration.

## Closest sources and limitations
- Needell and Tropp, *Paved with Good Intentions*, arXiv:1208.3805, 2012, relevant algorithm, theorem, proof and paving sections inspected.
- Needell, Zhao and Zouzias, *Randomized Block Kaczmarz Method with Projection for Solving Least Squares*, arXiv:1403.4192, 2014, relevant formulation and convergence sections inspected.
- Gower and Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296, 2015, especially Sections 3.5 and 5.1 inspected; general rate optimization is prior art.
- Relevant indexed related claims address row sampling on simplex frames, noisy size-based block sampling, and reshuffling, rather than the complete three-block partition optimization.

The result does not establish multi-step optimality, computing-time superiority, approximate-solve robustness, or precedence against all research literature. Verification is same-model only.

Self-review: passed. Independent audit: not yet performed.
