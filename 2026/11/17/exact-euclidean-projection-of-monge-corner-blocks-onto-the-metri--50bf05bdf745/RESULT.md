# Exact Euclidean projection of Monge corner blocks onto the metric face

## Finding

For every integer \(n\ge3\), let \(\mathcal H_n\) be the normalized hollow symmetric Monge polytope: the nonnegative symmetric real \(n\)-by-\(n\) matrices \(C\) with zero diagonal, \(\sum_{i,j}C_{ij}=1\), and \(C_{ij}+C_{k\ell}\le C_{i\ell}+C_{kj}\) whenever \(i<k\) and \(j<\ell\). Equip its ambient matrix space with the Frobenius norm \(\|C\|_F^2=\sum_{i,j}C_{ij}^2\).

For positive integers \(a,b\) with \(a+b\le n\), define the corner-block matrix \(V_{a,b}\) to equal \(1/(2ab)\) on the upper-right \(a\)-by-\(b\) rectangle and its transposed lower-left rectangle, and zero elsewhere. The known vertex theorem says that these and only these are the vertices of \(\mathcal H_n\). For \(1\le k<n\), put \(F_k=V_{k,n-k}\) and \(\mathcal F_n=\operatorname{conv}\{F_1,\ldots,F_{n-1}\}\). This distinguished metric face is exactly the closure of the normalized genuine metric matrices inside \(\mathcal H_n\).

**Exact vertex projection.** For every admissible pair \((a,b)\), the unique Frobenius-nearest point of \(\mathcal F_n\) to \(V_{a,b}\) is
\[
\boxed{\Pi_{\mathcal F_n}(V_{a,b})=\frac{b}{a+b}F_a+\frac{a}{a+b}F_{n-b}.}
\]
When \(a+b=n\), both displayed cuts coincide and the expression means \(F_a\). Writing \(s=a+b\) and \(c=n-s\), the complete squared vertex-to-face distance spectrum is
\[
\boxed{\operatorname{dist}_F(V_{a,b},\mathcal F_n)^2
=\frac{c\bigl(ab+sc\bigr)}{2ab\,s\,(n-a)(n-b)}.}
\]

**Unique deepest nonmetric matrix.** The exact Euclidean Hausdorff distance between the entire hollow symmetric Monge simplex and its metric face is
\[
\boxed{d_H(\mathcal H_n,\mathcal F_n)^2
=\frac{(n-2)(2n-3)}{4(n-1)^2}.}
\]
The unique point of \(\mathcal H_n\) attaining this distance is \(V_{1,1}\), the normalized two-corner-entry matrix. Its unique closest metric-face point is \((F_1+F_{n-1})/2\). The squared gap increases from \(3/16\) at \(n=3\) and tends to \(1/2\), so the Hausdorff distance tends to \(1/\sqrt2\).

## Assumptions and scope

All statements are for every integer \(n\ge3\), every \(1\le a,b\) with \(a+b\le n\), and the **full-matrix** Frobenius norm, which counts each off-diagonal entry twice. The projection formula concerns the **closed metric face**, consisting of normalized path pseudometrics. Its relative interior consists of the genuine metrics, with all consecutive path distances positive. Distance to the (nonclosed) set of genuine metrics has the same infimum, but this infimum need not be attained: in particular, for the unique deepest point \(V_{1,1}\), its face projection is not a genuine metric when \(n\ge4\). No claim is made about projections from arbitrary interior points of \(\mathcal H_n\), or about nonsymmetric or nonhollow Monge matrices.

## Proof

**1. Inner products and support overlap.** Let \(X=V_{a,b}\), \(h=n-b\), \(s=a+b\) and \(c=n-s=h-a\ge0\). For \(1\le i,j<n\), counting the ordered pairs crossing both cuts gives the exact Gram entry
\[
\langle F_i,F_j\rangle_F=\frac1{2\max(i,j)\,(n-\min(i,j))}.
\]
The inner products with the corner block follow by counting the rectangle's entries that cross the cut:
\[
\langle X,F_k\rangle_F=
\begin{cases}
[2a(n-k)]^{-1},&k<a,\\
[2k(n-k)]^{-1},&a\le k\le h,\\
[2bk]^{-1},&k>h.
\end{cases}
\]
This is compatible at both endpoints. Also \(\|X\|_F^2=1/(2ab)\).

**2. Exact projection certificate.** Put
\[
Y=\frac b{s}F_a+\frac a{s}F_h,
\qquad g_k=\langle Y-X,F_k\rangle_F.
\]
For \(c>0\), direct substitution of the preceding inner products gives
\[
g_a=g_h=-\frac{c}{2s(n-a)(n-b)}=:g_*.
\]
For the other indices the exact nonnegative gaps are
\[
g_k-g_*=
\begin{cases}
\displaystyle \frac{c}{2s(n-b)}\left(\frac1{n-a}-\frac1{n-k}\right),&k<a,\\[6pt]
\displaystyle \frac{c(k-a)(h-k)}{2sk(n-k)(n-a)(n-b)},&a<k<h,\\[6pt]
\displaystyle \frac{c}{2s(n-a)}\left(\frac1{n-b}-\frac1k\right),&k>h.
\end{cases}
\]
Every displayed expression is strictly positive whenever its index range is nonempty. Thus \(\langle Y-X,F_k-Y\rangle_F\ge0\) for every vertex \(F_k\), with equality at the two vertices used in \(Y\). By convexity the same inequality holds for every \(Z\in\mathcal F_n\), and
\[
\|X-Z\|_F^2=\|X-Y\|_F^2+\|Z-Y\|_F^2+2\langle Y-X,Z-Y\rangle_F\ge\|X-Y\|_F^2.
\]
Equality forces \(Z=Y\); hence the projection is globally optimal and unique. When \(c=0\), \(X=F_a=F_h=Y\), so the statement is immediate.

**3. Distance formula.** Expand \(\|X-Y\|_F^2\) using the Gram identities and the two weights. Straight simplification gives
\[
\|X-Y\|_F^2
=\frac{(n-a-b)\bigl(ab+(a+b)(n-a-b)\bigr)}{2ab(a+b)(n-a)(n-b)},
\]
including the boundary case \(a+b=n\) where both sides vanish.

**4. Hausdorff extremizer and its uniqueness.** Since \(\mathcal F_n\subset\mathcal H_n\), their Hausdorff distance is the maximum of the convex function \(X\mapsto\operatorname{dist}_F(X,\mathcal F_n)\) over \(\mathcal H_n\); it is enough to compare vertices. For \((a,b)=(1,1)\), the formula is \((n-2)(2n-3)/[4(n-1)^2]\). For every other vertex outside \(\mathcal F_n\), \(ab\ge2\). The particular face vertex \(F_a\) satisfies \(\langle V_{a,b},F_a\rangle_F=\|F_a\|_F^2\), and therefore
\[
\operatorname{dist}_F(V_{a,b},\mathcal F_n)^2
\le\|V_{a,b}-F_a\|_F^2
=\frac1{2ab}-\frac1{2a(n-a)}\le\frac14.
\]
The remaining face vertices have zero distance. When \(n\ge4\), the squared distance of \(V_{1,1}\) is strictly greater than \(1/4\): the difference is \([n^2-5n+5]/[4(n-1)^2]>0\) for integer \(n\ge4\). At \(n=3\), \(V_{1,1}\) is the sole vertex outside the metric face. Thus \(V_{1,1}\) is the unique farthest vertex in every order.

Finally any point \(X\ne V_{1,1}\) is a convex combination of the known vertices with positive total weight on other vertices. Convexity of squared distance to a closed convex set gives \(\operatorname{dist}_F(X,\mathcal F_n)^2\le\sum\lambda_{a,b}\operatorname{dist}_F(V_{a,b},\mathcal F_n)^2\), which is strictly less than the unique maximum. This rules out all nonvertex maximizers. The limiting squared distance follows immediately by expanding the displayed rational expression.

## Verification

Run `python3 check_projection.py` with the Python standard library. It checks the Frobenius Gram formulas by explicitly constructing the matrices in \(1{,}438\) cases through \(n=10\), then checks the exact rational projection optimality inequalities, distance formulas, and strict deepest-vertex inequalities in \(15{,}179\) cases through \(n=45\). The script reports `MONGE_METRIC_FACE_PROJECTION_PASS`. These are finite corroborations only; all-order conclusions rely on the preceding proof.

## Relationship to prior work

Erickson and Kretschmann's 2023 theorem supplies the normalized corner-block vertex set and proves that the consecutive-cut simplex is exactly the path-metric face. Their Sections 3--5 describe vertices, facets and volumes, not Frobenius projections from the other corner-block vertices. An earlier geometric study of this same metric face determines its intrinsic incenter, circumball, and volume; those are **within-face** invariants and do not give the distance from the surrounding Monge polytope. Two further related results study, respectively, Gaussian directional widths of the whole hollow symmetric Monge simplex and its intrinsic Frobenius incenter; neither determines the nearest metric-face points or this Hausdorff separation. A related computation of shortest **pairs of vertices** of the hollow symmetric Monge simplex concerns a different distance invariant and does not imply the metric-face projection law.

The classical metric-nearness literature supplies optimization methods for correcting arbitrary dissimilarity matrices, but does not establish the two-cut projection and complete spectrum for this specific normalized Monge family in the material located. The overlap checks and remaining bibliographic risks are documented in `AUDIT.json`.

## Limitations

The result concerns a canonical fixed normalization; it is not affine-invariant. It computes projections from all vertices, not a closed formula for the nearest metric-face point of an arbitrary interior Monge matrix. When the nearest point lies on the boundary of \(\mathcal F_n\), it is a pseudometric rather than a genuine metric, so no unattained nearest true metric is claimed. The maximum distance is an exact mathematical value, not a statistical or empirical estimate. Priority relative to all historical treatments of metric-nearness and cut-metric projection is not independently certified.

## References

1. W. Q. Erickson and J. Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522v1, first publicly posted 2023-11-13; see Propositions 4.1, 4.2 and 4.6. https://arxiv.org/abs/2311.07522
2. *Exact Euclidean centers and volume of the Monge metric face*, publicly indexed 2026-10-18, published-finding corpus record `2026/10/18/SCOPE-exact-euclidean-centers-and-volume-of-the-monge-metric-face--e4715e9d958a`.
3. *Angular condensation and a Gaussian-width limit for hollow symmetric Monge simplices*, published-finding corpus record `2026/10/25/SCOPE-angular-condensation-and-a-gaussian-width-limit-for-hollow-symme--a0ad17986dc6`.
4. *The Frobenius incenter of every hollow symmetric Monge simplex is Toeplitz and tends to quadratic cost*, published-finding corpus record `2026/11/8/SCOPE-the-frobenius-incenter-of-every-hollow-symmetric-monge-simplex-i--0902c4e4745e`.
5. J. Brickell, I. S. Dhillon, S. Sra, and J. A. Tropp, *The Metric Nearness Problem*, SIAM Journal on Matrix Analysis and Applications 30 (2008), 375--396, DOI:10.1137/060653391.
