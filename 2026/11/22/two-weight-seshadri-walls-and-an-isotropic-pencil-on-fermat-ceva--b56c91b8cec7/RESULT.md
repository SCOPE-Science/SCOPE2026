# Two-weight Seshadri walls and an isotropic pencil on Fermat–Ceva blow-ups

## Finding

Fix an integer \(m\geq2\). In \(\mathbb P^2_{\mathbb C}\), take the reduced Fermat–Ceva arrangement
\[
\mathcal A_m=V\bigl((X^m-Y^m)(Y^m-Z^m)(Z^m-X^m)\bigr).
\]
Let \(T\) be its \(m^2\) ordinary triple points, namely \(X^m=Y^m=Z^m\), and let \(V\) be the three coordinate vertices. For arbitrary real weights \(\alpha,\beta>0\), define
\[
\varepsilon_m(\alpha,\beta)
=\inf_{C}\frac{\deg C}{\alpha\sum_{P\in T}\operatorname{mult}_P(C)+\beta\sum_{P\in V}\operatorname{mult}_P(C)},
\]
where \(C\) ranges over reduced irreducible complex plane curves for which the denominator is positive. Then
\[
\boxed{\varepsilon_m(\alpha,\beta)=\frac{1}{\max\{m\alpha+\beta,\,2\beta\}}.}
\]
When \(\beta<m\alpha\), precisely the \(3m\) arrangement lines realize the infimum. When \(\beta>m\alpha\), precisely the three coordinate sides realize it. At \(\beta=m\alpha\), both families realize the infimum; the assertion does not exclude further curves on this wall.

The unique weight ratio at which this Seshadri constant attains the volume upper bound is \(\beta/\alpha=m\):
\[
\varepsilon_m(\alpha,\beta)\leq
(m^2\alpha^2+3\beta^2)^{-1/2},
\]
with equality if and only if \(\beta=m\alpha\). On \(S_m=\operatorname{Bl}_{T\cup V}\mathbb P^2\), the integral class
\[
D_m=2mH-\sum_{P\in T}E_P-m\sum_{P\in V}E_P
\]
is nef and isotropic: \(D_m^2=0\). It is base-point-free and defines a morphism \(S_m\to\mathbb P^1\) with a smooth geometrically integral generic fiber of genus
\[
g_m=\frac{(m-1)(m-2)}2.
\]
The morphism has \(m^2\) explicit exceptional sections and three explicitly reducible fibers. No exhaustive classification of its remaining singular fibers is asserted.

## Assumptions and scope

Everything is over \(\mathbb C\). All base points are ordinary proper points of \(\mathbb P^2\), with one blow-up at each. The three coordinate vertices are the points \([1:0:0]\), \([0:1:0]\), \([0:0:1]\); the grid \(T\) consists of \([\zeta^i:\zeta^j:1]\) for a primitive \(m\)-th root \(\zeta\) and \(0\leq i,j<m\). The \(3m\) component lines fall into three pencils, each through one coordinate vertex. Every arrangement line contains exactly \(m\) triple points and one coordinate vertex. Every coordinate side contains two vertices and no point of \(T\).

The weighted Seshadri invariant is equivalently the largest \(t\geq0\) for which the real divisor \(H-t(\alpha\sum_{T}E_P+\beta\sum_{V}E_P)\) is nef on \(S_m\). Weights are uniform within each of the two geometrically intrinsic point strata, but need not be rational.

## Proof

**1. The incidence and upper bounds.** The factorization of \(X^m-Y^m\), \(Y^m-Z^m\), and \(Z^m-X^m\) gives the stated incidence data, and all intersections of lines are among \(T\cup V\). An arrangement line has weighted multiplicity sum \(m\alpha+\beta\) and degree one. A coordinate side has weighted sum \(2\beta\) and degree one. Therefore \(\varepsilon_m\leq1/\max\{m\alpha+\beta,2\beta\}\).

**2. Two Bézout inequalities.** Let \(C\) be any irreducible plane curve of degree \(d\) that is neither an arrangement line nor a coordinate side. Write
\[
A=\sum_{P\in T}\operatorname{mult}_P(C),\qquad B=\sum_{P\in V}\operatorname{mult}_P(C).
\]
Apply Bézout to \(C\) and each of the \(3m\) arrangement lines, all different from \(C\). At a triple point three lines contribute; at a coordinate vertex \(m\) lines contribute. Since the local intersection of \(C\) with a smooth line through a point is at least the multiplicity of \(C\) at that point,
\[
3A+mB\leq3md.\tag{1}
\]
Likewise, \(C\) is different from the three coordinate sides. Each vertex lies on exactly two of these, hence
\[
2B\leq3d.\tag{2}
\]
Put \(u=m\alpha\). From (1),
\[
\alpha A+\beta B\leq ud+(\beta-u/3)B.\tag{3}
\]
If \(0<\beta\leq u/3\), the right side is at most \(ud<(u+\beta)d\). If \(u/3\leq\beta\leq u\), (2) and (3) give
\[
\alpha A+\beta B\leq(u/2+3\beta/2)d\leq(u+\beta)d.
\]
If \(\beta\geq u\), the same estimate is at most \(2\beta d\). Thus in every region
\[
\alpha A+\beta B\leq d\max\{u+\beta,2\beta\}.
\]
Together with the two types of line curves, this proves the exact formula. All inequalities are strict for non-line curves when \(\beta\ne u\). The two candidate line sums are distinct in that case, proving the stated exact list of minimizers off the wall.

**3. Sharpness of the volume bound.** Let \(W=\alpha\sum_T E_P+\beta\sum_V E_P\), with \(W^2=-(m^2\alpha^2+3\beta^2)\). Nefness of \(H-tW\) entails \((H-tW)^2\geq0\), yielding the standard volume upper bound. Write \(u=m\alpha\). When \(\beta<u\), the square of the exact denominator exceeds \(m^2\alpha^2+3\beta^2\) by \(2\beta(u-\beta)>0\). When \(\beta>u\), the excess is \(\beta^2-u^2>0\). At \(\beta=u\), equality holds. This proves uniqueness of the volume-saturating weight ratio and establishes \(D_m^2=4m^2-m^2-3m^2=0\) with nefness supplied by the exact Seshadri inequality.

**4. Pencil, resolution, and genus.** Consider the three degree-\(2m\) forms
\[
P=X^m(Y^m-Z^m),\quad Q=Y^m(Z^m-X^m),\quad R=Z^m(X^m-Y^m).
\]
They satisfy \(P+Q+R=0\), so \(\langle P,Q\rangle\) is a pencil with three explicit members \(P,Q,R\). Its proper base points are exactly \(T\cup V\). At each \(P_0\in T\), the two differences of \(m\)-th powers are independent local coordinates, and the pencil generators have independent linear initial terms: the base multiplicity is one and one blow-up removes the base point. At a coordinate vertex, for instance \(X=1\), the local generators have degree-\(m\) initial forms \(Y^m-Z^m\) and \(-Y^m\). They share no zero in the exceptional direction \([Y:Z]\), so one ordinary blow-up removes that base point too, with multiplicity \(m\). The resolved pencil is therefore a base-point-free pencil inside \(|D_m|\) and defines a morphism \(f_m:S_m\to\mathbb P^1\).

The three displayed reducible fibers have, respectively, \(m\) times a coordinate side and the \(m\) distinct lines of the opposite Fermat pencil, all taken as strict transforms; they carry the divisor class \(D_m\). Each exceptional curve over \(T\) intersects \(D_m\) once, and is therefore a section of \(f_m\). The existence of a section forces the Stein factor of \(f_m\) to be the identity: a finite cover of \(\mathbb P^1\) with a section is of degree one. Consequently its generic fiber is geometrically connected. Generic smoothness in characteristic zero and the smoothness of \(S_m\) imply that the general fiber is smooth, hence geometrically integral. Finally, \(K_{S_m}=-3H+\sum_T E_P+\sum_V E_P\), so
\[
D_m\cdot K_{S_m}=m^2-3m,\qquad p_a(D_m)=1+\frac{D_m^2+D_m\cdot K_{S_m}}2=\frac{(m-1)(m-2)}2.
\]
This is the genus of the smooth generic fiber.

## Verification

The standalone file `check.py` exhaustively checks the modular grid incidence rules for every \(2\leq m\leq40\), representative rational weight inequalities in all three regions, the two line equalities, the isotropic intersection formula and adjunction genus. Run `python3 check.py`; the observed output begins `PASS: exact grid incidences`. These finite tests corroborate the algebra and combinatorics but do not replace the uniform Bézout argument or the geometric proof of base-point freeness.

## Relationship to prior work

Pokora (arXiv:1711.09364, Example 3.4) and Janasz–Pokora (arXiv:2004.04043, Example 1.3) give the uniform-weight Fermat–Ceva value \(1/(m+1)\). Dumnicki and collaborators (arXiv:2611.03797, first posted 2 November 2026) prove the unweighted line-arrangement statement up to twelve lines and present a Bézout covering criterion. None of those statements determines the two-weight function or its change of minimizing curves. The weighted result uses two simultaneous incidence bounds, from the Fermat components and the coordinate triangle; the second family becomes extremal for \(\beta>m\alpha\).

Classical work on multinets and Ceva pencils (Falk–Yuzvinsky, arXiv:math/0603166) provides the general framework for pencils with several reducible fibers. The existence of a Ceva-type pencil is not presented as independently novel; here it explains the critical isotropic nef class and the occurrence of exact volume saturation.

## Limitations

The result concerns the specific Fermat–Ceva point configuration and uniform weights on each of its two natural singular strata, not arbitrary configurations or arbitrary point-by-point weights. No claim is made to classify all curves attaining the constant at the wall, every singular fiber of the pencil, or the full nef cone of the blown-up surface. The literature comparison is a best-knowledge priority assessment, not proof of uniqueness in the worldwide literature; an equivalent unindexed weighted computation may exist.

## References

- M. Dumnicki, Ł. Farnik, K. Hanumanthu, B. Harbourne, P. Pokora, J. Roé and H. Tutaj-Gasińska, *Seshadri constants of singular loci of line arrangements with at most twelve lines*, arXiv:2611.03797v1, 2 November 2026, https://arxiv.org/abs/2611.03797.
- P. Pokora, *Seshadri constants and special configurations of points in the projective plane*, arXiv:1711.09364, https://arxiv.org/abs/1711.09364.
- M. Janasz and P. Pokora, *On Seshadri constants and point-curve configurations*, arXiv:2004.04043, https://arxiv.org/abs/2004.04043.
- M. Falk and S. Yuzvinsky, *Multinets, resonance varieties, and pencils of plane curves*, arXiv:math/0603166, https://arxiv.org/abs/math/0603166.
