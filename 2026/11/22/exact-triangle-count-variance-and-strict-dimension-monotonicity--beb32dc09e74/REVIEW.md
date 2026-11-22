# Review of exact spherical hemisphere triangle-count variance

## Correctness — PASS

The proof uses the exact spherical wedge probability, conditional independence for two triangles sharing an edge, independence for zero- and one-vertex overlaps, and exact pair counting. A common Gaussian sequence provides an almost-sure strictly decreasing coupling of the absolute inner products as dimension grows. Beta moments yield a positive and exact leading high-dimensional term. Exhaustive sign words in the first dimension and exact angular identities in the second and third dimensions were checked by the standalone deterministic program. Finite checks are confirmatory, not an infinite proof.

## Originality — PASS, conditional on inspected literature

Bubeck–Ding–Eldan–Rácz analyze the same spherical model and uncentered triangle counts, but their Section 2 supplies expectation bounds, while the sparse-regime second-moment section supplies upper bounds based on overlap, not exact covariance or dimension monotonicity. Bok–Li–Yu analyze variance of *signed* triangle statistics in a planted local geometry model. Deka–Luo–Wu analyze complete-graph and atypical edge-count large deviations, not this variance invariant. The closest inspected related published findings concern *signed triangles with affine random links*, *acute Euclidean chord triangles*, and *extreme spherical side lengths* rather than ordinary hemisphere adjacency triangles. None of these statements implies the exact universal uncentered triangle variance law and its strict dimension ordering. Priority is not certified: inaccessible alternative sources or different terminology may still contain it.

## Value — PASS

Triangle counts are the canonical motif statistic for detecting the dependence hidden by pairwise-independent edges in geometric graphs. The theorem determines their *entire finite-sample variance*, makes the dependence on ambient dimension strictly ordered for every n, quantifies the sharp 1/sqrt(d) separation from the independent-edge benchmark, and exhibits exact low-dimensional constants. These facts calibrate motif noise, rather than merely re-evaluating a marginal probability or repeating asymptotic threshold results.

## Verification and limitations

The full analytic scope is all integer dimensions at hard edge density 1/2 and any fixed number of vertices n>=3. Numerical checks do not prove universal claims. No general nonzero edge threshold, simultaneous large-n limit, optimal detector, or priority certification is asserted.

Self-review: passed. Independent audit: not yet performed.
