# Scientific review

## Correctness — PASS

The Laplacian has an explicit three-projector spectral resolution, which yields all three types of entries in the Radau IIA transition matrix. The same-part and cross-part off-diagonal entries are strictly positive for every positive step. The common diagonal is the quartic \(P_m\) over a strictly positive denominator. The sum-of-squares identity proves unconditional positivity at \(m=5\), and comparison with \(m=5\) proves it for all smaller sizes. For \(m\ge6\), a negative witness at scaled step \(x=8\), positive endpoints, and a two-sign-change coefficient sequence prove exactly two simple positive zeros and exactly one forbidden interval. All claims include the \(h=0\) boundary. The independent exact-rational matrix identity replayed successfully for 77 test cases with 9,680 checked entries; finite tests are not used as the infinite proof.

## Originality — PASS on the inspected evidence

Horváth (2005, DOI 10.1016/j.apnum.2004.08.026) provides general Runge--Kutta positivity-threshold work, but only an abstract was accessible. Horváth--Song--Terlaky (arXiv:1406.6755v1; journal DOI 10.3934/dcds.2015.35.2997) provide general sufficient rational-discretization invariance bounds. Their accessible full text (Section 3.2, Theorem 3.12, and accompanying discussion) does not state the precise \(K_{m,m}\) all-step classification; its absolute-monotonicity threshold is a sufficient first-bound principle and cannot by itself supply the second safe interval. Published research-record hits for \([2/2]\) Padé, Crank--Nicolson, and filtered Crank--Nicolson use different rational maps. The accessible previous research ledger similarly contains other graph families and Padé/RK methods, not this \([1/2]\) Radau IIA quartic. Residual risk: the full Horváth 2005 paper and specialist literature were not exhaustively accessible, so this is an evidence-bounded originality assessment rather than independent priority certification.

## Value — PASS

Graph diffusion end-step matrices must be nonnegative to preserve nonnegative temperature or probability vectors for every initial datum. L-stability alone does not guarantee that property. For an infinite, natural graph family, the exact classification unexpectedly has **two disjoint safe ranges**, with the onset fixed at the smallest balanced biclique with twelve vertices. It also provides a precise quartic to choose a safe timestep and a proof that negativity arises exclusively on the diagonal. This is a structural boundary and complete classification, not merely another evaluation of a matrix at one arbitrary size.

## Limits

Unweighted balanced complete bipartite combinatorial Laplacians only; endpoint positivity, not stagewise or nonlinear invariance; no independent mathematical audit. Full-text access to some older relevant papers remained limited.

Self-review: passed. Independent audit: not yet performed.
