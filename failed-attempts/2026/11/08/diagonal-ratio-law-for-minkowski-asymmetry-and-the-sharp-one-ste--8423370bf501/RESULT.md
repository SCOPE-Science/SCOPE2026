# Diagonal-ratio law for Minkowski asymmetry and the sharp one-step \(\lambda\)-Steiner triangle profile

## Finding

For a full-dimensional planar convex body \(K\), define its *Minkowski asymmetry* by
\[
s(K)=\inf_{c\in\operatorname{int}K}\inf\{t\ge1:-(K-c)\subseteq t(K-c)\}.
\]
Let \(Q\) be any strictly convex quadrilateral. Its two diagonals intersect in an interior point, dividing each diagonal into two positive segments. Let \(\alpha,\beta\in(0,1/2]\) be the shorter-segment length divided by the *whole diagonal length* on each diagonal. Then the exact affine-invariant formula is
\[
\boxed{s(Q)=2-\frac{\min\{\alpha,\beta\}}{1-\max\{\alpha,\beta\}}.}
\tag{1}
\]
In particular, \(s(Q)=1\) exactly for parallelograms; a genuine non-parallelogram quadrilateral satisfies \(1<s(Q)<2\).

This gives a complete one-step profile for generalized Steiner symmetrization of triangles. Let \(T\) be any nondegenerate triangle in the Euclidean plane, let \(u\) be any unit direction, and let \(S_u^\lambda T\) be the \(\lambda\)-Steiner symmetral of Kipp--Sagmeister, with \(0\le\lambda\le1/2\). Project its vertices to the line perpendicular to \(u\), order those projected points from left to right, and let
\[
a=\frac{\text{distance from leftmost to middle projection}}{\text{distance from leftmost to rightmost projection}},
\qquad m=\min\{a,1-a\}.
\]
The extreme projected vertices are distinct because \(T\) has positive area. When two projected vertices coincide, the definition gives \(a=0\) or \(a=1\), as appropriate. Then
\[
\boxed{s(S_u^\lambda T)=2-\frac{\min\{m,\lambda\}}{1-\max\{m,\lambda\}}.}
\tag{2}
\]
For every fixed \(\lambda\in[0,1/2]\), the exact range over directions is
\[
\boxed{2-2\lambda\ \le s(S_u^\lambda T)\ \le2.}
\tag{3}
\]
For \(\lambda>0\), the minimum occurs exactly when the middle projected vertex is the midpoint of the outer two projections (\(a=1/2\)); the maximum occurs exactly when two vertices share a projection (\(a\in\{0,1\}\)). At \(\lambda=0\), every image is a triangle and has asymmetry \(2\). At \(\lambda=1/2\), the minimum is \(1\) and the minimizing image is a parallelogram. Every intermediate value in the stated range is attained as the direction varies.

## Assumptions and scope

All bodies are nondegenerate, compact, and convex in the Euclidean plane; affine maps are assumed invertible. The asymmetry definition uses a *single* common center for the reverse homothetic containment, rather than any area-based symmetry measure. The parameter \(\lambda\) is as in [1, Definition 1.1], with shaking at \(\lambda=0\) and ordinary Steiner symmetrization at \(\lambda=1/2\). Direction \(u\) determines parallel chords; the formula is insensitive to replacing \(u\) by \(-u\).

All strict quadrilaterals have positive diagonal-part ratios; the boundary values \(a=0\) or \(\lambda=0\) of the normalized model represent triangles and are included only in (2). Ratios \(a,\lambda\) are dimensionless. Formula (1) uses the shorter part of each of the *two* diagonals and is invariant under reorienting or swapping them. No claim is made about iterative stochastic convergence, other polytope classes, or higher-dimensional simplices.

## Proof

**Step 1: complete affine diagonal normal form.** For any strictly convex quadrilateral, send the intersection of the diagonals to \((a,0)\), the endpoints of one diagonal to \((0,0)\) and \((1,0)\), and the endpoints of the other diagonal to \((a,\lambda)\) and \((a,\lambda-1)\), by an invertible affine map. Here \(a,\lambda\in(0,1)\) are the fractions of the corresponding total diagonals. Reversing the endpoints on either diagonal replaces its fraction by its complement. Hence one may take \(0<a,\lambda\le1/2\), and the fractions then equal \(\alpha,\beta\). By affine invariance of the defining containment, it suffices to calculate asymmetry of
\[
Q_{a,\lambda}=\operatorname{conv}\{(0,0),(a,\lambda),(1,0),(a,\lambda-1)\}.
\tag{4}
\]
For the final triangular-limit argument allow \(0\le a,\lambda\le1/2\). The body remains a nondegenerate triangle at either zero endpoint, and the same facet inequalities (some redundant) remain valid.

**Step 2: exact facet constraints for a candidate center.** The outward facet normals and support values for (4), indexed from zero, can be chosen as
\[
\begin{array}{c|c|c}
i&n_i&b_i=h_{Q_{a,\lambda}}(n_i)\\\hline
0&(-\lambda,a)&0\\
1&(\lambda,1-a)&\lambda\\
2&(1-\lambda,a-1)&1-\lambda\\
3&(\lambda-1,-a)&0
\end{array}
\]
with the opposite support minima
\[
(m_0,m_1,m_2,m_3)
=\bigl(-\max\{a,\lambda\},\ a+\lambda-1,\ \min\{0,a-\lambda\},\ \lambda-1\bigr).
\tag{5}
\]
To test \(-(Q-c)\subseteq t(Q-c)\), put \(y=(t+1)c\). The containment is equivalent to
\[
n_i\cdot y\le t b_i+m_i\qquad(i=0,1,2,3).
\tag{6}
\]
This follows because \((t+1)c-Q\subseteq tQ\), and maximizing the functional \(n_i\cdot[(t+1)c-q]\) over \(q\in Q\) gives \(n_i\cdot y-m_i\). It is enough to check each facet of \(tQ\).

**Step 3: sharp obstruction by a positive dependence.** Define three nonnegative coefficients
\[
\beta_1=\frac{1-\lambda}{1-a},\qquad
\beta_2=\frac{1-a-\lambda}{1-a},\qquad
\beta_3=1.
\]
For \(0\le a,\lambda\le1/2\), they satisfy
\[
\beta_1n_1+\beta_2n_2+\beta_3n_3=0,\qquad
\beta_1b_1+\beta_2b_2+\beta_3b_3=1-\lambda>0.
\]
Multiplying three inequalities (6) by these coefficients and adding gives
\[
t\ge-\frac{\beta_1m_1+\beta_2m_2+\beta_3m_3}{1-\lambda}
=\begin{cases}
2-\dfrac{a}{1-\lambda},&a\le\lambda,\\[4pt]
2-\dfrac{\lambda}{1-a},&\lambda\le a.
\end{cases}
\tag{7}
\]
At equality of the two parameters either expression agrees. This proves the proposed lower bound with no optimization assumptions.

**Step 4: explicit feasible center proves the reverse bound.** Let \(t_*\) equal the corresponding right-hand side of (7). If \((a,\lambda)\ne(1/2,1/2)\), choose \(y\) as the unique solution of
\[
n_1\cdot y=t_*\lambda+a+\lambda-1,\qquad
n_3\cdot y=\lambda-1.
\tag{8}
\]
Its determinant is \(1-a-\lambda>0\). Direct substitution using (5) gives equality in inequalities \(i=1,2,3\), and gives the nonnegative *slack* in inequality \(i=0\) as
\[
(t_*b_0+m_0)-n_0\cdot y
=\begin{cases}
\dfrac{a(1-2\lambda)}{1-\lambda},&a\le\lambda,\\[4pt]
\dfrac{\lambda(1-2a)}{1-a},&\lambda\le a.
\end{cases}
\]
At \(a=\lambda=1/2\), take \(t_*=1\) and \(y=(1,0)\), which satisfies all four inequalities. Thus (6) holds at \(t_*\), so \(c=y/(t_*+1)\) is a suitable center and \(s(Q_{a,\lambda})=t_*\). Formula (1) follows. Its special cases follow immediately: \(s=1\) iff \(a=\lambda=1/2\), while positive fractions imply \(s<2\).

**Step 5: a triangle has a tent-shaped parallel-chord length.** Fix a triangle and a direction. When the three perpendicular projections are distinct, the length of the parallel sections is a nonnegative tent function \(\ell(x)\): it is affine from zero at the left extreme projection to its peak at the middle projected vertex, then affine back to zero at the right extreme projection. When two projections coincide, the chord length is instead a one-sided affine ramp whose nonzero endpoint is the coincident projection; it is exactly the \(a=0\) or \(a=1\) endpoint model, not a tent vanishing at both endpoints. After an invertible affine coordinate change, the projection interval is \([0,1]\), the peak lies at \(a\), and \(\ell(a)=1\).

By [1, Definition 1.1] every such chord of \(S_u^\lambda T\) has the same length \(\ell(x)\) but has lower and upper endpoints \(-\lambda\ell(x)\) and \((1-\lambda)\ell(x)\) relative to a fixed perpendicular hyperplane. Reversing the vertical coordinate, if necessary, transforms the image into the four-point convex hull (4). Thus (7) computes (2) with the smaller first-diagonal fraction \(m=\min\{a,1-a\}\).

**Step 6: sharp range, equality, and continuity in direction.** For fixed \(0<\lambda\le1/2\), the quotient \(\min\{m,\lambda\}/(1-\max\{m,\lambda\})\) increases strictly with \(m\in[0,1/2]\): on \(m\le\lambda\) it equals \(m/(1-\lambda)\), and on \(m\ge\lambda\) it equals \(\lambda/(1-m)\). It rises from \(0\) to \(2\lambda\). Hence (3) and the stated equality cases hold. Given any side of \(T\), choosing \(u\) parallel to the line from the opposite vertex to the side midpoint makes the middle projected vertex a midpoint, attaining \(m=1/2\); choosing \(u\) parallel to a side makes two projections coincide, attaining \(m=0\). Continuous rotation between suitable such directions realizes all intermediate \(m\). When \(\lambda=0\), all chords are shaken against a common line and the resulting hull is a nondegenerate triangle, so \(s=2\) for all directions. This completes the theorem.

## Verification

The standalone `check_asymmetry.py` uses only Python's standard-library exact fractions, and can be run with `python check_asymmetry.py`. It reconstructs all four normal supports from the four vertices, constructs the center satisfying (8), verifies all supporting inequalities, and independently checks the positive-dependence certificate, over \(11{,}724\) rational pairs in the closed parameter square \([0,1/2]^2\). It separately checks five exact boundary and parameter-transition witnesses, including the singular parallelogram endpoint. Its tested output is:

```
EXACT_QUADRILATERAL_ASYMMETRY_CERTIFICATES_OK 11724
BOUNDARY_AND_SHARP_CASES_OK
```

These finite computations are corroboration only. The exact real-parameter proof is Steps 1–6; no numerical experiment is used to extend a sampled statement to all quadrilaterals. The display in (8) gives the explicit candidate witness for every parameter, and (7) gives the matching lower certificate.

## Relationship to prior work

Kipp and Sagmeister [1, Definition 1.1 and Theorem 1.8] introduce the parameterized operation and classify almost-sure convergence of planar random processes. Their work motivates understanding the geometry of an individual operation, but the global convergence criterion does not specify a quantitative one-step Minkowski-asymmetry profile for a triangle. Bakaev and Yehudayoff [2] study the general Minkowski symmetry functional and its stability near simplices. The classical bounds \(1\le s(K)\le2\), the central-symmetry endpoint, and the triangular endpoint are established background, not contributions claimed here. The calculation in (1) determines a full continuous two-parameter affine moduli family rather than just these endpoints; (2)–(3) specialize it to a natural recent operation.

Related published works treat an *area-centroid chord asymmetry* of quadrilaterals and Minkowski asymmetry of *parallel-opposite hexagons*, respectively. They use different invariants or different polygon classes: their results do not imply the formula in (1) or the direction profile in (2). A published result on preservation of central symmetry under intermediate generalized Steiner operations applies to originally centrally symmetric bodies, not a generic triangular input. The present result does not assert that a negative search establishes absolute historical priority.

## Limitations

The exact formula is proved only for planar strict quadrilaterals and the specified triangular limiting cases; the symmetrization conclusion concerns **one step**, not long-run stochastic convergence. The minimizing direction depends on the geometry of each triangle. This calculation does not give a closed form for arbitrary convex polygons or higher-dimensional simplices. A historically equivalent quadrilateral formula might appear in older work on Minkowski centers or affine moduli under different notation; broad priority remains provisional and requires specialist verification. The finite rational checker is not a substitute for the analytic proof. No independent mathematical validation is claimed.

## References

1. C. Kipp and Á. Sagmeister, *Random convergence of generalized Steiner processes*, arXiv:2610.05113v1, first publicly submitted 4 October 2026, Definition 1.1, Theorem 1.8, and Section 5. https://arxiv.org/html/2610.05113v1
2. E. Bakaev and A. Yehudayoff, *A simplex-based measure of symmetry*, arXiv:2607.03815v1, first publicly submitted 4 July 2026, Sections 1 and 3. https://arxiv.org/abs/2607.03815
3. T. Kobos and M. Varivoda, *On the Banach–Mazur Distance in Small Dimensions* (2024), for classical planar asymmetry properties and the uniqueness of the planar Minkowski center; the general background is not used as a new result.
