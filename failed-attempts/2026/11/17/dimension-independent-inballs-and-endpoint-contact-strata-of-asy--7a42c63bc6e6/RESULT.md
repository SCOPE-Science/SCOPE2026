# Dimension-independent inballs and endpoint contact strata of asymmetric twinned chain polytopes

## Finding

Let \(I_d\) be the antichain on \([d]\), let \(C_d\) be the chain on \([d]\), and let \(\mathcal C(P)\) denote Stanley's chain polytope. Their asymmetric twinned chain polytope, in its canonical Euclidean coordinates, is
\[
K_d=\Gamma(\mathcal C(I_d),\mathcal C(C_d))
=\operatorname{conv}\bigl([0,1]^d\cup\{-e_1,\ldots,-e_d\}\bigr),\qquad d\ge2.
\]
Its Euclidean inradius is **independent of dimension**:
\[
\boxed{r_{\mathrm{in}}(K_d)=\frac1{\sqrt2}.}
\]
The complete set of centers of balls attaining this radius is the nondegenerate diagonal segment
\[
\boxed{\operatorname{Incenters}(K_d)=\{t\mathbf1:t\in[\ell_d,u]\},\quad
u=1-\frac1{\sqrt2},\qquad
\ell_d=\begin{cases}0,&d=2,\\\sqrt{\frac32}-1,&d\ge3.\end{cases}}
\]
Here \(\mathbf1=(1,\ldots,1)\). There are exactly \(1+d2^{d-1}\) facets. For \(d\ge3\), an inball at an interior point of the segment touches exactly \(d(d-1)\) facets; at the lower endpoint it touches
\[
\boxed{d(d-1)+d\binom{d-1}{2}}
\]
facets; and at the upper endpoint it touches \(d^2\) facets. For \(d=2\), the respective lower-endpoint/interior/upper-endpoint counts are \(3,2,4\). No other facets touch any radius-maximizing ball.

Thus the possible contact facets form a polynomially sized subset of an exponentially growing facet set. The lower endpoint is controlled by facets with three nonzero signed coefficients (except \(d=2\)), while the upper endpoint is controlled by coordinate facets.

## Assumptions and scope

The Euclidean structure is the usual \(\ell_2\) metric on \(\mathbb R^d\); the unit cube has vertices with coordinates zero or one, and the negative simplex has vertices \(-e_i\) together with the origin. The origin is an interior point of \(K_d\), not an extreme vertex. All statements quantify over **every integer \(d\ge2\)** and all centers of maximum-radius Euclidean balls. Facet contact means tangency of the closed inscribed ball to a genuine facet-supporting hyperplane, not mere contact with a lower-dimensional face. No claims are made under arbitrary nonorthogonal affine changes of coordinates.

## Proof

**1. Exact supporting facets.** As \(K_d\) is the convex hull of a cube and a negative simplex and contains the origin in its interior, its polar is
\[
K_d^\circ=\left\{y\in\mathbb R^d:
y_i\ge-1\ (1\le i\le d),\quad
\sum_{i=1}^d\max(y_i,0)\le1\right\}.
\]
The vertices of this polar are exactly
\[
-\mathbf1\quad\text{and}\quad
v_{i,J}=e_i-\sum_{j\in J}e_j,
\qquad i\in[d],\ J\subseteq[d]\setminus\{i\}.
\]
To check exhaustiveness, within any sign region with at least two strictly positive coordinates, one can perturb two positive coordinates in opposite directions and stay in the polar; hence such a point is not extreme. At a vertex with exactly one positive coordinate, that coordinate must be one, and every remaining coordinate must be either zero or minus one, since otherwise it can be perturbed. With no positive coordinates, every coordinate must be minus one to be extreme. Conversely, \(-\mathbf1\) is fixed by the \(d\) independent tight lower-coordinate constraints; for \(v_{i,J}\), the constraints \(y_j=-1\) for \(j\in J\), \(y_i=1\), and \(y_i+y_k=1\) for \(k\notin J\cup\{i\}\) are tight and independent. Thus each listed vector is extreme, proving the list. By polarity, these vectors are precisely the distinct outward facet normals, with support value one; their count is \(1+d2^{d-1}\). This also follows as a specialization of Tsuchiya's preexisting general facet theorem, which is not claimed here as new.

**2. Upper bound and all candidate centers.** For distinct \(i,j\), the list includes both normals \(e_i-e_j\) and \(e_j-e_i\). An inscribed ball of radius \(r\) with center \(c\) must satisfy
\[
|c_i-c_j|+r\sqrt2\le1.
\]
Consequently \(r\le1/\sqrt2\). Equality for every pair forces \(c_i=c_j\) for all \(i,j\); hence every optimal center must be \(t\mathbf1\). It remains to determine which values of \(t\) attain the upper bound.

**3. Sharp inequalities on the diagonal.** For \(v_{i,J}\) with \(k=|J|\), the ball inclusion condition for \(r=1/\sqrt2\) is exactly
\[
1+(k-1)t\ge\sqrt{\frac{k+1}{2}}.
\]
For \(k=0\), this yields \(t\le u=1-1/\sqrt2\). For \(k=1\), equality holds at every \(t\). For each \(k\ge2\), the condition is
\[
t\ge a_k:=\frac{\sqrt{(k+1)/2}-1}{k-1}
=\frac1{2(1+\sqrt{(k+1)/2})}.
\]
The \(a_k\) strictly decrease with \(k\), so when \(d\ge3\) their strongest bound is the \(k=2\) bound \(t\ge\sqrt{3/2}-1\). When \(d=2\), there are no \(k\ge2\) normals. Finally, the remaining normal \(-\mathbf1\) imposes
\[
1+dt\ge\sqrt{d/2},\quad\text{i.e.}\quad
t\ge b_d:=\frac{\sqrt{d/2}-1}{d}.
\]
For \(d=2\), this is \(t\ge0\). For \(d\ge3\), writing \(z=\sqrt{d/2}\) shows
\[
b_d=\frac{z-1}{2z^2}\le\frac18<\sqrt{\frac32}-1.
\]
Thus the \(-\mathbf1\) constraint is redundant for \(d\ge3\). The intervals stated in the finding are precisely the feasible \(t\)-values. Since they are nonempty, they realize the upper-bound radius, and no other centers are possible.

**4. Exact tangent-facet stratification.** For a diagonal center and radius \(1/\sqrt2\), the \(k=1\) inequalities have equality for all \(t\), and there are \(d\binom{d-1}{1}=d(d-1)\) such facet normals. At \(t=u\), precisely the \(k=0\) inequalities also become tight, adding \(d\) facets. For \(d\ge3\), at \(t=\ell_d\), precisely the \(k=2\) inequalities also become tight, adding \(d\binom{d-1}{2}\) facets. Strict decrease of \(a_k\) excludes every \(k\ge3\) there. The all-negative inequality is strictly slack throughout the allowed interval when \(d\ge3\). When \(d=2\), that inequality is tight exactly at the lower endpoint \(t=0\), adding one facet; the coordinate inequalities add two facets at \(u\). This completes the exact classification.

## Verification

A standalone finite-dimensional checker (`verify_twinned_mixed.py`) constructs the indicated vertex set, computes its convex hull independently using Qhull, normalizes all recovered facet planes, and compares the resulting complete facet set to the analytic description. It separately solves an unconstrained-center Chebyshev-ball linear program and counts tight facets at both endpoints and an interior point. All checks passed in dimensions \(d=2,3,4,5,6\), and the analytic finite inequality checks passed through \(d=7\). The program prints `TWINS_CUBE_SIMPLEX_INBALL_PASS` when successful. Reproduce using Python with NumPy and SciPy installed: `python verify_twinned_mixed.py`. These finite tests corroborate but do not establish the infinite family; Steps 1–4 do.

## Relationship to prior work

Tsuchiya's 2015 preprint [1], Theorem 2.2, already characterizes the supporting facets of every twinned chain polytope and even computes the combinatorial volume for **exactly this antichain/chain pair** in Example 1.7. Both the construction and the facet classification are therefore prior results, not novelty claims. Ohsugi and Tsuchiya's 2019 paper [2], Section 5, proves Ehrhart-theoretic and \(\gamma\)-positivity properties for twinned chain polytopes, not the Euclidean ball-center geometry established here.

A separate published analysis of **symmetric** twinned chain polytopes of layered posets [3] determines centered radii and high-dimensional boxes of incenters for \(\Gamma(\mathcal C(P),\mathcal C(P))\). It explicitly excludes distinct poset pairs. The present body is the *asymmetric* pair \(\Gamma(\mathcal C(I_d),\mathcal C(C_d))\), and the symmetric theorem does not imply its sharp unequal endpoint bounds or contact counts. Its ideas are nevertheless closely related and historical priority under alternative metric terminology remains a risk.

## Limitations

Only the given canonical Euclidean metric and the specified asymmetric pair are covered. The polar/facet description is known in greater generality; the assessed assertion is the exact global inball-center locus and its full contact stratification, not a new combinatorial description of twinned chain polytopes. The review of historical priority is provisional; a yet-unindexed exact metric classification may exist. Independent mathematical validation has not been performed.

## References

1. A. Tsuchiya, *Volume, facets and dual polytopes of twinned chain polytopes*, arXiv:1512.08332, first posted 2015-12-28, Example 1.7 and Theorem 2.2. https://arxiv.org/abs/1512.08332
2. H. Ohsugi and A. Tsuchiya, *The h*-polynomials of locally anti-blocking lattice polytopes and their gamma-positivity*, arXiv:1906.04719, first posted 2019-06-11, Section 5. https://arxiv.org/abs/1906.04719
3. *Incenter boxes and contact strata of layered twinned chain polytopes*, publicly available `RESULT.md`, 2026-11-08. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-incenter-boxes-and-contact-strata-of-layered-twinned-chain-polyt--410962c86761/RESULT.md
