# A unique angular-sum optimizer for rectangular tetrahedra with a cube-root balancing law

## Finding

For any real anisotropy \(R>1\), consider the tetrahedra with one vertex incident to three mutually perpendicular edges and with the ratio of the longest to shortest of these three edges equal to \(R\). Their **total normalized vertex solid angle** has a unique minimizer up to similarity and permutation of the three orthogonal arms. Its intermediate arm length is neither the shortest nor the longest and obeys a cube-root balancing law when \(R\) is large.

Set \(t_R\) to be the unique root in \((1,R)\) of
\[
\frac{Rt_R}{\sqrt{1+t_R^2}}+\frac{t_R}{\sqrt{R^2+t_R^2}}=\sqrt{R^2+1}.
\]
The minimizing arm lengths, after rescaling the shortest to one, are precisely
\[
(1,b_R,R),\qquad b_R=\frac{R}{t_R}.
\]
Moreover,
\[
b_R\sim(2R)^{1/3}
\]
and the sharp minimum of the sum of normalized vertex solid angles is
\[
\Sigma_{\min}(R)=\frac14-\frac1{2\pi R}
+\frac{3}{2^{5/3}2\pi}R^{-5/3}+o(R^{-5/3}).
\]
For \(R=1\), the domain consists of the equal-arm tetrahedron and the assertion of a unique *interior* intermediate-arm optimizer is inapplicable.

## Assumptions and scope

The ambient space is Euclidean \(\mathbb R^3\), and all tetrahedra are nondegenerate. The family consists **only** of
\[
T(a,b,c)=\operatorname{conv}\{(0,0,0),(a,0,0),(0,b,0),(0,0,c)\},\qquad a,b,c>0.
\]
The three specified edges emanating from the origin are orthogonal. Their arm anisotropy is \(R=\max\{a,b,c\}/\min\{a,b,c\}\). This is not the ratio of the largest to smallest of *all six tetrahedron edge lengths*.

For each vertex \(v\), let \(\Omega_v(T)\) be the area in steradians of the spherical triangle obtained by intersecting the tangent cone at \(v\) with the unit sphere. Define
\[
\Sigma(T)=\frac{\sum_{v\in\operatorname{vert}(T)}\Omega_v(T)}{4\pi}.
\]
Because this functional is invariant under rigid motions, positive uniform scaling, and arm permutations, at fixed \(R>1\) we may use the complete parameterization
\[
(a,b,c)=(1,R/t,R),\qquad 1\le t\le R.
\]
The parameter \(t\) is the **reciprocal intermediate arm**, scaled by \(R\); it should not be confused with the intermediate arm length \(b=R/t\).

## Proof

**Step 1: an exact identity for the angular sum.** Write
\[
q=\sqrt{a^{-2}+b^{-2}+c^{-2}},\qquad
n_1=\frac{1/a}{q},\quad n_2=\frac{1/b}{q},\quad n_3=\frac{1/c}{q}.
\]
The inclined facet of \(T\) lies in the plane \(x/a+y/b+z/c=1\), with outward unit normal \((n_1,n_2,n_3)\). The other three outward facet normals are \(-e_1,-e_2,-e_3\). Along each edge incident to the origin, the interior dihedral angle is \(\pi/2\). Along the three remaining edges, the interior dihedral angles are respectively \(\arccos n_1\), \(\arccos n_2\), and \(\arccos n_3\).

The spherical triangle at each tetrahedron vertex has interior angles equal to the three interior dihedral angles along its incident edges. Its spherical area is their sum minus \(\pi\). Summing over all four vertices counts each of the six edge dihedral angles twice. Consequently
\[
\sum_v\Omega_v(T)=2\left(\frac{3\pi}{2}+\sum_{j=1}^3\arccos n_j\right)-4\pi,
\]
which simplifies to
\[
\boxed{\Sigma(T)=\frac12-\frac1{2\pi}\sum_{j=1}^3\arcsin n_j.}\tag{1}
\]
This normalization can be checked on the equal-arm case or directly against spherical-triangle areas: the angle at the origin alone is \(\pi/2\) steradians, hence \(1/8\) of the full sphere.

**Step 2: reduction to a one-variable strictly unimodal profile.** For the parametrization \((1,R/t,R)\) put \(Q=\sqrt{R^2+t^2+1}\). The normalized inverse arm lengths are the three positive numbers \(R/Q,t/Q,1/Q\), whose squares sum to one. Thus (1) becomes
\[
S_R(t)=\frac12-\frac1{2\pi}\left(\arcsin\frac RQ+\arcsin\frac tQ+\arcsin\frac1Q\right),\qquad t\in[1,R].\tag{2}
\]
Let \(A_R(t)\) be the parenthesized sum. Direct differentiation, with \(Q^2=R^2+t^2+1\), gives
\[
A_R'(t)=\frac1{Q^2}\left(\sqrt{R^2+1}-\frac{Rt}{\sqrt{t^2+1}}-\frac{t}{\sqrt{R^2+t^2}}\right).\tag{3}
\]
Introduce \(h_R(t)=Rt/\sqrt{t^2+1}+t/\sqrt{R^2+t^2}\). The derivative
\[
h_R'(t)=\frac{R}{(1+t^2)^{3/2}}+\frac{R^2}{(R^2+t^2)^{3/2}}>0\tag{4}
\]
is strictly positive for all \(t>0\). For \(R>1\), the endpoint comparisons are strict:
\[
h_R(1)=\frac R{\sqrt2}+\frac1{\sqrt{R^2+1}}<\sqrt{R^2+1},
\]
\[
h_R(R)=\frac{R^2}{\sqrt{R^2+1}}+\frac1{\sqrt2}>\sqrt{R^2+1}.
\]
The first inequality reduces to \(1/\sqrt2<R/\sqrt{R^2+1}\) and the second to \(1/\sqrt2>1/\sqrt{R^2+1}\), both equivalent to \(R>1\).

The intermediate value theorem and strict monotonicity (4) therefore provide a **unique** \(t_R\in(1,R)\) with \(h_R(t_R)=\sqrt{R^2+1}\). Equations (2)–(3) show that \(S_R'(t)<0\) below this root and \(S_R'(t)>0\) above it. This proves a unique global minimum and excludes any boundary minimizers, including for \(R\) arbitrarily close to one. Because \(t\mapsto R/t\) is bijective on \([1,R]\), the shape is unique up to arm permutation and scaling.

**Step 3: sharp large-anisotropy location.** We use the exact stationarity equation
\[
R\frac{t_R}{\sqrt{1+t_R^2}}+\frac{t_R}{\sqrt{R^2+t_R^2}}=\sqrt{R^2+1}.\tag{5}
\]
As \(R\to\infty\), the solution must satisfy \(t_R\to\infty\): otherwise the first term is at most \((1-\delta)R\) along a bounded subsequence, while the second remains bounded, contradicting the right side. Also \(t_R/R\to0\): if \(t_R\ge cR\) along a subsequence, the first term equals \(R+O(R^{-1})\) while the second is bounded below by a fixed positive constant, exceeding \(\sqrt{R^2+1}=R+O(R^{-1})\).

Rearranging (5) gives
\[
R\left(1-\frac{t_R}{\sqrt{1+t_R^2}}\right)
=\frac{t_R}{\sqrt{R^2+t_R^2}}-\left(\sqrt{R^2+1}-R\right).\tag{6}
\]
Using \(t_R\to\infty\) and \(t_R/R\to0\), the left side is asymptotic to \(R/(2t_R^2)\); the right side is asymptotic to \(t_R/R\), because \(\sqrt{R^2+1}-R\sim1/(2R)\) and \(t_R\to\infty\). Hence
\[
\frac{t_R^3}{R^2}\longrightarrow\frac12,
\qquad t_R\sim2^{-1/3}R^{2/3},\qquad b_R=R/t_R\sim(2R)^{1/3}.\tag{7}
\]

**Step 4: the fractional-power angular correction.** Since the three inverse-arm parameters satisfy \((R/Q)^2+(t/Q)^2+(1/Q)^2=1\), elementary inverse-trigonometric identities rewrite the sum in (2) as
\[
A_R(t)=\frac\pi2+\arctan\frac{t}{\sqrt{R^2+1}}+\arctan\frac1{\sqrt{R^2+t^2}}-\arctan\frac{\sqrt{1+t^2}}R.\tag{8}
\]
Write \(\alpha_R=t_R/R^{2/3}\to\alpha_0=2^{-1/3}\). Taylor expansion of the three elementary arctangents in (8), or the mean value theorem applied to the difference of the first and third, yields
\[
A_R(t_R)-\frac\pi2
=\frac1R-\frac1{2Rt_R}-\frac{t_R^2}{2R^3}+o(R^{-5/3}).\tag{9}
\]
Indeed, the first-minus-third term equals \(-1/(2Rt_R)+o(R^{-5/3})\), and the middle term equals \(1/R-t_R^2/(2R^3)+o(R^{-5/3})\); these estimates are valid because of (7). Therefore
\[
A_R(t_R)-\frac\pi2
=\frac1R-\left(\frac1{2\alpha_0}+\frac{\alpha_0^2}{2}\right)R^{-5/3}+o(R^{-5/3}),
\]
where \(1/(2\alpha_0)+\alpha_0^2/2=3\cdot2^{-5/3}\). Inserting into (2) proves the stated exact two-term asymptotic with the fractional-power correction. This completes the proof.

## Verification

The accompanying standalone file `verify.py` uses the standard library only. It evaluates the four individual normalized vertex solid angles using the three-vector determinant formula for a spherical trihedral, and independently evaluates (1) using the facet-normal expression. A fixed-seed run checked 4,000 arbitrary positive arm triples, the derivative-root characterization and uniqueness pattern for twelve different anisotropy ratios, and the fractional-power asymptotics at four large ratios. The checker printed `ANGLE_SUM_OK 5300`.

The checker is finite corroboration only. The universal uniqueness and asymptotic statements follow from the exact derivative inequalities and estimates (3)–(9). No finite grid, randomized test or numerical root finder is invoked as an infinite proof.

## Relationship to prior work

Licht, *On solid angles and simplex shape measures* (first posted October 5, 2026), introduces a dimension-general sharpness and regularity perspective for minimum solid angles; its Section 3 also recalls the classical angle-sum bound. The present theorem optimizes a **different invariant**—the sum of the four vertex solid angles—under a fixed, geometrically specified arm ratio.

Kabluchko and Schange, *Angles of orthocentric simplices* (first posted May 8, 2025), Theorem 8.5, compute internal and external angle formulas for rectangular orthocentric simplices of every dimension. In dimension three, their formulas could be used to evaluate the four angles at a prescribed shape. The present result is not an assertion that those individual-angle formulas are new: its contribution is the **unique constrained angular-sum optimizer**, the exact root characterization, and the asymptotic balancing law and noninteger-power term. The elementary Gram–Euler identity used in the proof is likewise classical.

Earlier literature on tetrahedral solid angles, including Liu and Joe's 1994 work, establishes individual-angle formulas and compares shape measures. It is not claimed that angular sum formulas or trirectangular tetrahedra were first discovered here. Historical priority of the constrained optimization is not independently certified.

## Limitations

The orthogonality of the three arm edges is essential. The result does not characterize extrema among arbitrary tetrahedra or under a bound on the ratio of *all* six edge lengths. It is an exact minimization, not a maximum classification. The asymptotic statement is for \(R\to\infty\); it is not claimed uniform in additional geometric parameters. The result does not re-establish any previously known formula for the individual smallest vertex angle. Independent mathematical review remains unperformed.

## References

1. Martin W. Licht, *On solid angles and simplex shape measures*, arXiv:2610.05883v1, submitted 2026-10-05; author's open preprint: https://martinlicht.github.io/pdf/preprint.solidangles.pdf.
2. Zakhar Kabluchko and Philipp Schange, *Angles of orthocentric simplices*, arXiv:2505.05048v1, submitted 2025-05-08; Section 8.3, Theorem 8.5: https://arxiv.org/pdf/2505.05048.
3. A. Liu and B. Joe, *Relationship between tetrahedron shape measures*, 1994; classical tetrahedral solid-angle and shape-measure comparisons.
4. Spherical excess and the Gram–Euler angle relation, classical formula for the solid-angle sum of a Euclidean tetrahedron (proved directly by spherical vertex triangles above).
