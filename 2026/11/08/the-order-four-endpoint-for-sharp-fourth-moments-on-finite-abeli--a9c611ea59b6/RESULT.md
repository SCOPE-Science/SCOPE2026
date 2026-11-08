# The order-four endpoint for sharp fourth moments on finite abelian coordinate crosses

## Finding
Let \(H\) be any finite abelian group of order \(q\), let \(d\ge2\), and let \(\Omega_{H,d}\subset H^d\) be the union of its \(d\) coordinate subgroups, with their common identity counted once. For coefficients \(a:\Omega_{H,d}\to\mathbb C\), let
\[
F(\boldsymbol\chi)=\sum_{h\in\Omega_{H,d}}a(h)\boldsymbol\chi(h),\qquad
S=\sum_{h\in\Omega_{H,d}}|a(h)|^2,
\]
where \(\boldsymbol\chi\in\widehat H^d\), equipped with uniform probability measure.

**Sharp order-four threshold and rigidity.** For every integer \(d\ge2\) and every finite abelian group of order \(q\ge4\),
\[
\boxed{\mathbb E_{\boldsymbol\chi}|F(\boldsymbol\chi)|^4\le qS^2.}
\]
Equality for nonzero coefficients holds **if and only if** there are an axis \(j\), a character \(\eta\in\widehat H\), and a nonzero \(C\in\mathbb C\) such that \(a(h)=C\eta(h_j)\) at every point of that entire axis and \(a(h)=0\) at all points off it. Thus the optimal fourth-power constant is \(q\), independent of the number of axes and of the isomorphism type of \(H\).

The group-order threshold is best possible for a uniform statement over all nontrivial finite abelian groups: the all-ones data on two axes gives fourth-moment ratios \(7/3>2\) at \(q=2\) and \(77/25>3\) at \(q=3\). These counterexamples embed in any \(d\ge2\).

Moreover, for \(q\ge5\), writing \(X_j\) for the energy of the nonidentity coefficients on axis \(j\), the theorem gives the quantitative concentration remainder
\[
qS^2-\mathbb E|F|^4\ge 2\left(q-5+\frac1{q-1}\right)\sum_{i<j}X_iX_j.
\]

## Assumptions and scope
All character groups and all integrals are finite. We use the **unnormalized** Fourier synthesis \(F\) and uniform probability on the dual group. In particular, Parseval gives \(\mathbb E|F|^2=S\). The coordinate subgroups intersect only at the identity; it is a single frequency, not one duplicated frequency per axis. The main assertion holds for both abelian groups of order four (cyclic and Klein-four), for arbitrary finite abelian groups of larger cardinality, and for any finite number of axes. Only fourth moments are considered.

## Proof
Write \(a_0=a(0)\). Because the coordinate subgroups share only their identity, orthogonality of characters gives an independent-variable decomposition
\[
F=a_0+\sum_{j=1}^d U_j(\chi_j),\qquad
\mathbb E U_j=0,\quad X_j=\mathbb E|U_j|^2,
\quad T=\sum_jX_j,\quad S=|a_0|^2+T.
\]
Each \(U_j\) is a complex-valued function on a uniform set of exactly \(q\) points.

**Centered one-coordinate bound.** For \(q\ge4\), every centered complex random variable \(U\) on \(q\) equally likely values with \(X=\mathbb E|U|^2\) satisfies
\[
\mathbb E|U|^4\le c_qX^2,\quad
|\mathbb E(U|U|^2)|\le m_qX^{3/2},\qquad
c_q=q-2+\frac1{q-1},\quad m_q=\frac{q-2}{\sqrt{q-1}}.
\tag{1}
\]
For completeness, normalize \(\sum|z_i|^2=1\) and \(\sum z_i=0\). At an extremum of \(\sum|z_i|^4\), Lagrange multipliers give \((2|z_i|^2-\lambda)z_i=\mu\). If \(\mu=0\), all nonzero coordinates have equal modulus, yielding at most \(1/2\). If \(\mu\ne0\), all \(z_i\) lie on one real line after rotation and solve one cubic. Three distinct real roots would sum to zero. Perturbing one occurrence of each root while preserving the triple's sum and squared norm also preserves its fourth-power sum (the elementary identity \(a^4+b^4+c^4=(a^2+b^2+c^2)^2/2\) whenever \(a+b+c=0\)). Since \(q\ge4\), an untouched coordinate then yields four distinct roots at another extremum, impossible for a cubic. Thus only two values occur. With multiplicities \(r\) and \(q-r\), the fourth-power sum equals \(q/[r(q-r)]-3/q\), maximized at \(r=1\) or \(q-1\). The resulting uniform-probability constant is \(c_q\); its value exceeds the excluded \(1/2\) case when \(q\ge4\). Finally, the centered cubic bound follows from Cauchy–Schwarz applied to \(\mathbb E[U(|U|^2-X)]\) and \(\operatorname{Var}(|U|^2)\le(c_q-1)X^2\). This establishes (1).

**Independent-variable fourth moment.** Expanding the fourth power of the independent centered sum and using (1) and \(|\mathbb EU_j^2|\le X_j\) gives, with \(A=|a_0|\),
\[
\mathbb E|F|^4\le A^4+6A^2T+4m_q A\sum_jX_j^{3/2}
+c_q\sum_jX_j^2+6\sum_{i<j}X_iX_j. \tag{2}
\]
In this expansion the terms with \(\mathbb EU_i^2\overline{\mathbb EU_j^2}\) are bounded by \(2X_iX_j\), and the independent mixed \(|U_i|^2|U_j|^2\) terms contribute \(4X_iX_j\); no other mixed terms survive centering.

**Orders at least five.** Since \(c_q>3\) for \(q\ge5\), the inequalities \(\sum_jX_j^{3/2}\le T^{3/2}\) and \(\sum_jX_j^2=T^2-2\sum_{i<j}X_iX_j\) reduce (2) to
\[
\mathbb E|F|^4\le A^4+6A^2T+4m_qAT^{3/2}+c_qT^2
-2(c_q-3)\sum_{i<j}X_iX_j.\tag{3}
\]
When \(T>0\), set \(s=\sqrt{q-1}\) and \(t=A/\sqrt T\). The remaining scalar inequality is exactly
\[
q(t^2+1)^2-(t^4+6t^2+4m_qt+c_q)
=\frac{(st-1)^2(s^2t^2+2s^2+2st-1)}{s^2}\ge0.
\tag{4}
\]
This proves both the sharp inequality and the displayed concentration remainder for \(q\ge5\).

**The previously unresolved order four.** Here \(c_4=7/3<3\) and \(m_4=2/\sqrt3\), so the sign used in (3) reverses; that argument does not apply. Let \(T>0\), \(x_j=X_j/T\), \(B=\sum_jx_j^2\), \(t=A/\sqrt T\), and \(v=\sqrt B\in(0,1]\). Cauchy–Schwarz gives \(\sum_jx_j^{3/2}\le\sqrt{\sum_jx_j^2}=v\). Equation (2) now yields
\[
\frac{4S^2-\mathbb E|F|^4}{T^2}
\ge 3t^4+2t^2+1-\frac{8}{\sqrt3}tv+\frac23v^2.
\tag{5}
\]
The quadratic on the right, as a function of \(v\in[0,1]\), has its unconstrained minimum at \(v=2\sqrt3\,t\). If \(0\le t\le1/(2\sqrt3)\), its minimum is \(3t^4-6t^2+1\ge1/2>0\). Otherwise the minimum on \([0,1]\) occurs at \(v=1\), where (5) becomes
\[
\frac13(\sqrt3t-1)^2(3t^2+2\sqrt3t+5)\ge0.
\tag{6}
\]
Equality requires \(t=1/\sqrt3\) and \(v=1\). Since \(B=\sum x_j^2=1\), precisely one \(X_j\) is nonzero. This proves the order-four inequality and establishes **single-axis rigidity** there, despite the unfavorable sign of \(c_4-3\).

**Equality cases at every order.** For \(q\ge5\) the positive remainder in (3) forces all but one \(X_j\) to vanish. The order-four case has just been treated. Thus \(F\) depends on one coordinate and its values form a \(q\)-tuple. Its fourth moment satisfies \(\mathbb E|F|^4\le q(\mathbb E|F|^2)^2\), with equality only when that \(q\)-tuple is supported at a single point. Fourier inversion gives precisely the scalar-character coefficient arrays described in the finding. Conversely those arrays attain equality. The case \(T=0\) gives a nonzero constant \(F\), strictly below \(qS^2\).

**Sharp lower threshold.** At \(q=2\), taking the constant coefficient and one nonidentity frequency from each of two axes all equal to one gives \(F=1+\chi_1+\chi_2\), \(S=3\), and \(\mathbb E|F|^4=21\), so the ratio is \(7/3>2\). At \(q=3\), using all five points of the two-axis cross with coefficient one gives \(S=5\), \(\mathbb E|F|^4=77\), and ratio \(77/25>3\). Both examples embed in any higher-dimensional cross. This concludes the sharp classification.

## Verification
The standalone Python checker `artifacts/verify_cross_axes.py` evaluates direct character sums on cyclic groups of orders four, five, six and seven and on the noncyclic Klein-four group, with two or three coordinate axes. It performed 480 deterministic randomized and full-axis equality comparisons and two exact pair-sum fourth-moment checks of the order-two/three counterexamples, reporting `CROSS_AXES_CHECK_PASS randomized_and_axis=480 exact_witnesses=2`. Run `python artifacts/verify_cross_axes.py` with the Python standard library; there are no additional dependencies. Finite tests corroborate the normalization and examples but are not proofs of the universal theorem, which follows from (1)–(6).

## Relationship to prior work
The 2026 publicly available result *Sharp fourth-moment extension and one-axis rigidity for finite abelian crosses* proves the two-axis statement for groups of order at least five, leaving order four unresolved and making no assertion for arbitrarily many axes. Its centered-moment argument is an antecedent to (1)–(4); the critical new step is the order-four estimate (5)–(6), where the earlier sign argument breaks down, together with uniform higher-axis rigidity. The 2018 work of Iosevich, Koh, Lee, Pham and Shen studies zero-radius spheres over finite fields, not crosses over arbitrary abelian groups of order four. González-Riquelme and Oliveira e Silva (2024) address sharp finite-field extension on smooth quadratic geometries and higher-dimensional cones, not this all-dimensions coordinate-cross endpoint. A general sharp product-space fourth-moment theorem not located in the searches could subsume the result; literature priority is therefore provisional.

## Limitations
This result concerns finite abelian direct-product coordinate subgroups, the fourth moment, and uniform dual probability. No best stability coefficient is asserted at order four; the quantitative energy-spread remainder is given only for orders at least five. The proof does not address all unions of affine subgroups, different coordinate group orders, or higher even moments. Sharpness in group order means the universal threshold, not that the exact constants for orders two and three have been determined here.

## References
1. *Sharp fourth-moment extension and one-axis rigidity for finite abelian crosses*, publicly available 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-extension-and-one-axis-rigidity-for-finite-a--5b31463115dc (especially the proof of the centered fourth-moment lemma and its two-axis limitation).
2. A. Iosevich, D. Koh, S. Lee, T. Pham and C.-Y. Shen, *On restriction estimates for the zero radius sphere over finite fields*, first public arXiv version 2018-06-29, https://arxiv.org/abs/1806.11387.
3. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, first public arXiv version 2024-05-26, https://arxiv.org/abs/2405.16647.
