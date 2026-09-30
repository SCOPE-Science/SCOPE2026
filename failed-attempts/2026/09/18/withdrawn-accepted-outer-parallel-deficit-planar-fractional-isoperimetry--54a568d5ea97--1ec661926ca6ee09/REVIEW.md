# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The identity is a direct finite-interval integration of the published first-variation formula, followed by the published large-radius asymptotic. For
\[
H(r)=C_q(K+rB_1)-C_q(B_{R+r}),\qquad R=\operatorname{Per}(K)/(2\pi),
\]
Steiner's formula keeps the two bodies at equal perimeter and Proposition 3.8 of arXiv:2609.19052 gives
\[
H'(r)=2q\bigl[W_{1-q}(K+rB_1)-W_{1-q}(B_{R+r})\bigr].
\]
The source's fixed-perimeter fractional-Willmore inequality makes the derivative nonnegative, while its outer-parallel asymptotic gives \(H(r)\to0\). Hence
\[
-H(0)=\int_0^\infty H'(r)\,dr.
\]

The equality step was checked separately rather than inferred from the non-strict inequality in arXiv:2609.19052. Döhrer--Dohmen, arXiv:2604.02042, Theorem 1.3, prove unique disk minimization for all fractional Willmore energies among convex planar sets. At \(p=1\) their boundary kernel agrees, up to a positive normalization, with the integrated fractional mean-curvature quantity \(W_\alpha\) used by Lin et al.; the inward/outward normal conventions cancel exactly. Thus zero excess at any parallel radius forces \(K+rB_1\) to be a disk. Subtracting \(r\) from its support function forces \(K\) itself to be a disk.

Dimensional/scaling checks are consistent:
\[
C_q(\lambda K)=\lambda^{q+1}C_q(K),\qquad
W_{1-q}(\lambda K)=\lambda^qW_{1-q}(K),
\]
so the integrand times \(dr\) has the same homogeneity as the chord deficit. With \(q=1-s\), division by \(s(1-s)\) gives the coefficient \(2/s\) in the fractional-perimeter identity.

Potential failure modes checked include the perimeter matching under outer parallel addition, the translation freedom in the disk equality case, the sign convention for the nonlocal curvature, the convergence of the improper integral, and whether uniqueness of the Willmore minimizer was already known. The latter is prior art and is explicitly credited rather than claimed.

## Originality

**PASS, to the best of our knowledge.**

The following primary sources were inspected:

- Lin--Yang--Yang--Yuan--Zhang, arXiv:2609.19052v1. The paper proves the sharp planar fractional isoperimetric inequality, the convex chord inequality, the fractional-Willmore lower bound, the outer-parallel first-variation formula, and the asymptotic used to close the monotonicity argument. Its theorem states that equality is attained by the disk; the inspected version does not state the exact integrated deficit formula or an if-and-only-if equality characterization for the chord inequality.
- Döhrer--Dohmen, arXiv:2604.02042v1. Theorem 1.3 proves that disks uniquely minimize all fractional Willmore energies among convex planar sets of fixed perimeter. This rigidity theorem is prior art and is excluded from the originality claim.

Exact and synonymous searches combined terms such as fractional perimeter deficit, chord functional, outer parallel bodies, fractional Willmore, equality case, rigidity, and the two source identifiers. No earlier statement matching
\[
C_q(B_R)-C_q(K)
=
2q\int_0^\infty
\bigl[W_{1-q}(K+rB_1)-W_{1-q}(B_{R+r})\bigr]\,dr
\]
or its fractional-perimeter version was located. The current SCOPE archive was also searched by source identifier, object, and claim family without a matching record.

No highly relevant primary source identified in the search was inaccessible. The main residual originality risk is recency: the sharp planar inequality is a 2026 preprint and a simultaneous or not-yet-indexed observation could exist.

The originality claim is deliberately narrow: the new content is the exact outer-parallel deficit representation and its equality consequence for the newly proved sharp chord/fractional-perimeter inequality in the \(C^\infty_+\) convex class. The first variation, asymptotic, Willmore inequality, and Willmore rigidity are all credited prior ingredients.

## Value

**PASS.**

The identity upgrades a one-sided monotonicity proof into an exact representation of the full sharp deficit. It identifies the deficit as accumulated curvature-energy excess over all outer scales, and, by combining two recent results, closes the equality case for the smooth strictly convex subclass. This gives a reusable mechanism for future quantitative stability estimates: any lower control of the fractional-Willmore excess along the parallel flow can be integrated directly into a remainder term for the sharp chord or fractional-perimeter inequality.

## Limitations

The result is restricted to \(C^\infty_+\) convex bodies. It does not establish equality rigidity for arbitrary \(C^1\) domains or nonsmooth convex bodies, and it does not provide a quantitative geometric-distance remainder. Recency leaves residual originality risk.

No independent validation is asserted.
