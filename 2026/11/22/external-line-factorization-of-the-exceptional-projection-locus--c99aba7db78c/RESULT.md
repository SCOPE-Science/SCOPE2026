# External-line factorization of the exceptional projection locus for Artin–Schreier conic configurations

## Finding

Let \(Q=p^e\ge2\) be any prime power, and let \(k=\overline{\mathbb F}_p\). The explicitly defined \(Q(Q+1)\)-point Artin–Schreier configuration in the next section has \(Q+1\) supporting lines. By the general geproci criterion, a **general** plane projection is not a complete intersection of type \((Q,Q+1)\). Nevertheless, the complete locus of *admissible exceptional projection centers* is a nonempty reduced arrangement of \(m=Q(Q-1)/2\) planes through the common supporting-line vertex, with an explicit arithmetic stratification.

Write a projection center as \(P=[a:u_0:u_1:u_2]\in\mathbb P^3_k\), and exclude centers for which two distinct supporting lines have the same projected image. On this open set, the projected \(Q(Q+1)\) points form a reduced plane complete intersection of degrees \(Q\) and \(Q+1\) **if and only if**

\[
G_Q(u_0,u_1,u_2)=0,\qquad
G_Q(U,V,W)=\prod_{\substack{b,c\in\mathbb F_Q\\ T^2+bT+c\ \mathrm{irreducible}\ \mathrm{over}\ \mathbb F_Q}}
(cU+bV+W).
\]

All factors are distinct, their number is \(m\), and the augmented-Vandermonde determinant defining the interpolation obstruction is a nonzero scalar multiple of \(G_Q\). Equivalently, its projectivized direction locus consists exactly of the \(\mathbb F_Q\)-external lines of the rational conic \(UW=V^2\) (lines meeting none of its \(Q+1\) rational points).

The admissible exceptional-center variety is noncanonically an \(\mathbb F_Q\)-isomorphic disjoint union

\[
E_Q^{\mathrm{good}}\cong\coprod_{j=1}^{m}\mathbb A^1\times\bigl(\mathbb A^1\setminus\mathbb F_Q\bigr).
\]

Here \(\mathbb A^1\setminus\mathbb F_Q\) means the affine line with its \(Q\) \(\mathbb F_Q\)-rational closed points removed. Consequently, for every integer \(r\ge1\),

\[
\#E_Q^{\mathrm{good}}(\mathbb F_{Q^r})=m Q^r(Q^r-Q),\qquad
Z(E_Q^{\mathrm{good}}/\mathbb F_Q,T)=\frac{(1-QT)^{mQ}}{(1-Q^2T)^m}.
\]

In particular there is **no admissible exceptional center over \(\mathbb F_Q\)**, but there are many over every proper finite extension.

The projectivized divisor's line-arrangement incidence is also exact. For odd \(Q\), its \(\mathbb F_Q\)-rational plane points comprise \(Q+1\) conic points on zero arrangement lines, \(Q(Q+1)/2\) off-conic points on \((Q-1)/2\) lines each, and \(Q(Q-1)/2\) other off-conic points on \((Q+1)/2\) lines each. For even \(Q\), the \(Q+1\) conic points and the conic nucleus lie on zero arrangement lines, while all remaining \(Q^2-1\) points lie on exactly \(Q/2\) arrangement lines. Every geometric multiple intersection of the arrangement is \(\mathbb F_Q\)-rational.

## Assumptions and scope

Use homogeneous coordinates \([a:x:y:z]\) on \(\mathbb P^3_k\), and put \(O=[1:0:0:0]\). For each \(t\in\mathbb F_Q\), define \(v_t=(1,t,t^2)\in\mathbb F_Q^3\), and let \(v_\infty=(0,0,1)\). The \(Q+1\) lines \(L_t=\mathbb P\langle O,[0:v_t]\rangle\) are distinct, concurrent at \(O\), and span \(\mathbb P^3\). Set

\[
Z_Q=\{[s:v_t]:s\in\mathbb F_Q,\ t\in\mathbb P^1(\mathbb F_Q)\},
\]

with \(v_t\) as above. These are \(Q(Q+1)\) distinct rational points, none equal to \(O\). The direction set \(\Gamma=\{[v_t]\}\) consists of all rational points on the nonsingular conic \(xz=y^2\) in \(\mathbb P^2\).

A center \(P=[a:u]\) is **admissible** if its direction \([u]\in\mathbb P^2_k\) does not belong to any of the \(\binom{Q+1}{2}\) secant lines joining two different points of \(\Gamma\). This excludes \(O\), all supporting lines and all projections with coinciding supporting-line images. On the admissible open locus, the projection of \(Z_Q\) consists of \(Q(Q+1)\) distinct points on \(Q+1\) distinct concurrent target-plane lines. A center is **exceptional** when this projection is a scheme-theoretic complete intersection of type \((Q,Q+1)\); the word does not assert the general geproci property.

No statement is made about centers on the excluded secant planes, about arbitrary (nonconic) direction sets, or about the full Weddle scheme of all degree-\(Q\) hypersurface relations.

## Proof

**1. Reduction to interpolation.** Fix an admissible center \(P=[a:u]\). Choose a vector-space complement \(W\) to \(ku\) in \(k^3\), and uniquely write \(v_t=\alpha_tu+w_t\), with \(w_t\in W\). Quotienting the four-dimensional homogeneous coordinate space by the center vector identifies the image of \([s:v_t]\) with \([s-a\alpha_t:w_t]\) in the target plane \(\mathbb P(k\oplus W)\). The \([w_t]\) are distinct by admissibility. On the corresponding target line, the \(Q\) projected points are the roots of

\[
\sigma^Q-\sigma+\beta_t^Q-\beta_t=0,\qquad \beta_t=a\alpha_t.
\]

Suppose that the projected set is a reduced complete intersection of degrees \((Q,Q+1)\). Its degree-\(Q\) equation \(F\) cannot contain any supporting target line: otherwise the degree-\((Q+1)\) equation would have to meet that line in a scheme of length \(Q+1\), whereas the desired intersection there has length \(Q\) and avoids the concurrency point. Since \(F\) restricts to a nonzero multiple of the displayed monic orbit polynomial on every line, the coefficient of \(\sigma^Q\) is common and nonzero. Scaling \(F\), the coefficient of \(\sigma\) is \(-1\) on all lines. Writing \(F=\sigma^Q+\sigma M(w)+H(w)\) with the sign incorporated into \(M\), this implies that the vector \((1,\ldots,1)\) belongs to the degree-\((Q-1)\) evaluation image on the \(Q+1\) distinct points \([w_t]\in\mathbb P(W)\).

Conversely, if a form \(M\) of degree \(Q-1\) satisfies \(M(w_t)=1\) for every \(t\), then degree-\(Q\) evaluation on \(Q+1\) distinct points of \(\mathbb P^1\) is surjective. Choose a degree-\(Q\) form \(H\) with \(H(w_t)=\beta_t^Q-\beta_t\). The degree-\(Q\) plane form \(F=\sigma^Q-\sigma M+H\) cuts precisely the required reduced \(Q\)-point orbit on every supporting line. The product of the \(Q+1\) supporting-line equations has no common component with \(F\), and Bézout's theorem gives their scheme-theoretic complete intersection as exactly the projected \(Z_Q\).

**2. The determinant and its degree.** Let \(D_Q(u)\) be the augmented homogeneous Vandermonde determinant for degree-\((Q-1)\) evaluation at the \(Q+1\) projected directions with the final column \((1,\ldots,1)\). Up to a nonzero factor independent of \(u\), it is

\[
D_Q(u)=\sum_{i=1}^{Q+1}(-1)^i\prod_{\substack{1\le j<k\le Q+1\\j,k\ne i}}\det(u,v_j,v_k).
\]

Each summand has total degree \(\binom Q2\) in \(u\). The determinant is nonzero: at \(u=v_i\), every term except the \(i\)-th vanishes, while the remaining product is nonzero because no three distinct points of a smooth conic are collinear. Thus \(D_Q\) is homogeneous of exact degree \(m=Q(Q-1)/2\).

**3. Every external line divides the determinant.** Let \(h\in(\mathbb F_Q^3)^*\setminus\{0\}\) have \(h(v_t)\ne0\) for all \(t\in\mathbb P^1(\mathbb F_Q)\). Along the projective line \(h(u)=0\), the functional \(h\) descends to \((k^3/ku)^*\), and its \((Q-1)\)-st power supplies the interpolation form:

\[
M(w_t)=h(w_t)^{Q-1}=h(v_t)^{Q-1}=1.
\]

Therefore \(D_Q(u)\) vanishes identically on the line \(h(u)=0\), so \(h(u)\) is a factor. Such \(\mathbb F_Q\)-lines are exactly the lines avoiding all rational points of the conic, hence the external lines. There are \(Q^2+Q+1\) rational projective lines altogether, of which \(Q+1\) are tangents and \(\binom{Q+1}{2}\) are secants. Thus exactly \(m=Q(Q-1)/2\) are external. Since these are distinct linear factors and \(D_Q\ne0\) has degree exactly \(m\), their product is \(D_Q\) up to a nonzero scalar, with no other factor or multiplicity. Writing an external line as \(h(U,V,W)=cU+bV+W\) gives precisely the irreducible quadratic \(T^2+bT+c\) stated in the finding; conversely every such quadratic avoids roots in \(\mathbb P^1(\mathbb F_Q)\). This proves the exact reduced factorization and the if-and-only-if criterion on admissible centers.

**4. Geometry and point counts of the admissible exceptional locus.** Distinct external \(\mathbb F_Q\)-lines meet in rational direction points. Every rational point on an external line lies on at least one rational secant of the conic. For odd \(Q\), off-conic points have either two or zero conic tangents, hence respectively \((Q-1)/2\) or \((Q+1)/2\) secants; for even \(Q\), apart from the nucleus every off-conic point has one tangent and \(Q/2\) secants. Thus removing all secants from any external line removes exactly that line's \(Q+1\) rational points. Distinct external-line components are disjoint after this removal.

Over each external direction line \(\ell\), the map \([a:u]\mapsto[u]\) from its center plane minus the vertex is an affine-line bundle. Over \(\ell\setminus\ell(\mathbb F_Q)\), choose a rational point of \(\ell\) to serve as infinity; the resulting nonvanishing coordinate on \(u\) trivializes the affine-line bundle. Hence each component is \(\mathbb A^1\times(\mathbb A^1\setminus\mathbb F_Q)\). The \(\mathbb F_{Q^r}\)-point count follows by multiplying \(Q^r\), \(Q^r-Q\), and \(m\); summing its logarithmic generating series yields the displayed zeta function.

**5. Incidence of the projectivized external-line arrangement.** For odd \(Q\), counting the \(Q+1\) conic points on lines through an off-conic rational point gives \((Q-1)/2\) external lines for a point on two tangents and \((Q+1)/2\) for a point on none. The numbers of these point types are respectively \(Q(Q+1)/2\) (double-count tangent-point incidences) and \(Q(Q-1)/2\). In even characteristic, all \(Q+1\) tangents pass through the nucleus; each of the remaining \(Q^2-1\) off-conic points lies on one tangent, \(Q/2\) secants and \(Q/2\) external lines. Distinct rational lines intersect in rational points, so this is also the complete geometric multiple-intersection profile.

## Verification

The standalone `verify.py` uses only the Python standard library. It constructs the exact augmented-Vandermonde polynomial and product of all external linear factors over \(\mathbb F_Q\), verifies equality up to a nonzero scalar, and exhaustively counts arrangement incidences over the base field for \(Q=2,3,4,5,7,8\), including quadratic and cubic binary extension fields. Run `python3 verify.py`; all six cases are expected to print `PASS`. These finite tests do not prove the assertions for arbitrary prime powers; Steps 1–5 supply that proof.

## Relationship to prior work

Chiantini, Farnik, Favacchio, Harbourne, Migliore, Szemberg and Szpond (2026) establish the Artin–Schreier interpolation criterion and prove that \(Q+1\) concurrent supporting lines are **not generically** \((Q,Q+1)\)-geproci. Their determinant argument supplies the general obstruction but does not identify its factorization or classify exceptional projection centers for the rational-conic, equal-orbit family. The result above determines that precise nongeneric stratum, its reduced components, incidence structure, extension-field points and zeta function.

The general Weddle-locus framework of Chiantini et al. (2026) and Ballico (2026) motivates studying special projection centers, but the inspected statements do not supply the characteristic-positive external-line identity for this family. The finite-geometry classification of conic external and internal points is classical; that incidence fact alone does not identify the complete-intersection projection locus or its determinant.

## Limitations

This is a theorem for the specified highly symmetric \(\mathbb F_Q\)-rational direction conic and identical Artin–Schreier orbits. It is not a classification for arbitrary concurrent-line orbits, projections from forbidden secant planes, or all degree-\(Q\) Weddle relations. The determinant defines the indicated interpolation obstruction, and the equivalent complete-intersection interpretation is asserted only on the admissible open locus. The finite-field experiments are supplementary. External literature may contain an unindexed equivalent special-projection computation; no independent mathematical audit is claimed.

## References

1. L. Chiantini, Ł. Farnik, G. Favacchio, B. Harbourne, J. Migliore, T. Szemberg, J. Szpond, *Artin–Schreier geproci configurations in projective spaces of arbitrary dimension*, arXiv:2609.03024v1, first submitted 2 September 2026, especially Proposition 2.3 and Theorem 3.4. https://arxiv.org/html/2609.03024
2. L. Chiantini, Ł. Farnik, G. Favacchio, B. Harbourne, J. Migliore, T. Szemberg, J. Szpond, *Weddle schemes*, arXiv:2606.25060v1, 23 June 2026, especially the introduction and Section 7.4. https://arxiv.org/abs/2606.25060
3. E. Ballico, *Generalized Weddle Loci*, Axioms 15 (2026), article 745, published 4 October 2026. https://doi.org/10.3390/axioms15100745
4. J. Kettinger, *The geproci property in positive characteristic*, Proceedings of the American Mathematical Society 152 (2024), 3229–3242. https://doi.org/10.1090/proc/16809
