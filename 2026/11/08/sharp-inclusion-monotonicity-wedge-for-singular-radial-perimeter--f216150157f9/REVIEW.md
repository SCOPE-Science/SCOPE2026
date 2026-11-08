# Scientific review

## Correctness — PASS

The identity \(E_p=4(\int_0^b(a^2+y^2)^{p/2}dy+\int_0^a(b^2+x^2)^{p/2}dx)\) is exact. Differentiating in the positive half-sides and substituting \(y=at\) yields \(\partial_a E_p=4a^pG_p(b/a)\), with symmetric formula for \(b\). The derivative \(G_p'=p(1+r)(1+r^2)^{p/2-1}\), the equality \(G_p(1)=(p+1)\int_0^1(1+t^2)^{p/2}dt\), and the negative infinite-radius limit prove a unique root above one for \(-1<p<0\). The shape wedge is convex in its half-side parameters, so integration of the nonnegative gradient along an inclusion path proves a global, strict statement. Expanding the short side outside the wedge produces an actual reverse inequality for a nearby nested pair. Scaling and the explicit \(p=-1\) formula handle the remaining exponents. The implicit differentiation and dominated convergence arguments justify the phase monotonicity and endpoint asymptotics. The packaged Python 3 script completed 902 supplementary checks, including derivative finite differences and root-side tests; it is not substituted for the proof.

## Originality — PASS, historically provisional

The closest primary results are the weighted-perimeter shape optimization for fixed boundary length (arXiv:2608.19851, particularly Sections 1–3), inclusion monotonicity for increasing nonnegative radial weights (arXiv:2610.11677, introduction/Theorem 1.3), and global rigidity for weights monotone on every nested convex-body pair (Saracco–Stefani 2023/2024). Their statements neither state the exact negative-power rectangle eccentricity wedge nor imply the sharp inverse-exponent and endpoint classification. Targeted public-literature searches and matching published mathematical-record queries identified sharp Hausdorff regularity for negative radial perimeters and rectangle phenomena for unrelated invariants, but not the asserted inclusion-monotonicity phase. The full October preprint, including Section 3 and its counterexamples, was compared against the claim. Historical coverage is not certified.

## Mathematical value — PASS

The original motivation is an explicit sharpness gap in general inclusion-monotonicity theorems for singular radial weights. A restricted convex-body class may still be monotone even when global monotonicity fails; the exact largest aspect-bounded class is a natural complete classification, not an arbitrary sampled parameter. The strict/global statement and its sharp counterexamples expose the competition between short-side boundary contributions and long-side boundary contributions. Smooth parameter dependence, a bijective critical-exponent curve, and two boundary asymptotics give usable information for geometric shape comparisons beyond an isolated computation. No assertion of a general convex-body extension is made.

## Closest literature and residual risks

The 2026 fixed-perimeter problem and the 2026 global monotonicity paper concern different comparison classes; the former also computes some rectangle-based examples in its fixed-perimeter setting. The full latter paper, including its sharpness examples in Section 3, was inspected. Older specialist literature still creates residual historical-priority risk. The result is not independently audited.

Self-review: passed. Independent audit: not yet performed.
