# Sharp fourth-distance-moment tomography for triangular perimeters

## Finding
Let \(T\) be any nondegenerate Euclidean triangle, with side lengths \(a,b,c>0\), perimeter \(P=a+b+c\), and area \(A>0\). Let \(X,Y\) be independent points chosen from the entire boundary of \(T\) according to normalized Euclidean arclength, and put \(m_{2j}=\mathbb E\|X-Y\|^{2j}\). Define \(p_1=a/P,p_2=b/P,p_3=c/P\) and \(e_2=p_1p_2+p_2p_3+p_3p_1\).

The exact moments are
\[
 m_2=\frac{P^2}{24}-\frac{2A^2}{P^2},\qquad
 m_4=\frac{P^4}{240}-A^2\left(1-\frac49e_2\right).
\]
The first identity is consistent with a previously published second-moment formula; the fourth-moment shape term and the following inverse and sharp-range consequences are the subject of this note.

**Inverse theorem.** Knowledge of \((P,m_2,m_4)\) determines the unordered triple of side lengths and hence \(T\) up to congruence. Explicitly, set
\[
 A^2=\frac{P^2}{2}\left(\frac{P^2}{24}-m_2\right),\quad
 e_2=\frac{9}{4A^2}\left(m_4-\frac{P^4}{240}+A^2\right),\quad
 e_3=\frac{m_2}{P^2}-\frac16+\frac{e_2}{2}.
\]
Then \(p_1,p_2,p_3\) are precisely the roots, including multiplicity, of \(z^3-z^2+e_2z-e_3=0\). The two initial even moments are minimal: \((P,m_2)\) alone does not distinguish all triangles.

**Sharp fixed-perimeter-and-area range.** Put \(K=16A^2/P^4\). For \(0<K<1/27\), let \(\alpha\in(0,1/3)\) and \(\beta\in(1/3,1/2)\) denote the unique solutions of \(x^2(1-2x)=K\) in those respective intervals. Define
\[
 E(x)=\frac{1+2x-3x^2}{4},\qquad
 B=\frac{P^4}{240}-A^2.
\]
Among all nondegenerate triangles with those prescribed \(P,A\), the **complete** range is
\[
 B+\frac49A^2E(\alpha)\ \le\ m_4\ \le\ B+\frac49A^2E(\beta).
\]
The lower and upper bounds are attained, respectively, by the two noncongruent isosceles triangles with normalized side lengths \(((1-\alpha)/2,(1-\alpha)/2,\alpha)\) and \(((1-\beta)/2,(1-\beta)/2,\beta)\). Every intermediate value is attained. At \(K=1/27\), only the equilateral triangle exists and the interval collapses to a point (\(\alpha=\beta=1/3\)).

## Assumptions and scope
Independence and **perimeter-uniform** arclength measure are essential: the endpoints are not sampled by invariant random lines and not sampled uniformly from the triangle's interior. The triangle is nondegenerate, so \(0<A^2\le P^4/432\); equality is equilateral. All expectations are exact population moments. The inverse theorem assumes that the numerical perimeter is separately known, and makes no claim about recovery of perimeter from two moments alone.

## Proof
**Step 1: exact polynomial integrations.** Label the three sides by \(\ell_1,\ell_2,\ell_3\). The probability that a boundary-uniform point lies on side \(i\) equals \(\ell_i/P\), and conditional position is uniform in the unit interval. If two points fall on the same side of length \(x\), then for \(j=1,2\)
\[
 \mathbb E[D^{2j}\mid\mathrm{same\ side}]=x^{2j}\frac{2}{(2j+1)(2j+2)},\qquad D=\|X-Y\|.
\]
If they lie on two distinct sides of lengths \(x,y\) meeting at an angle opposite the third side \(z\), let \(s,t\) be independent uniform variables on \([0,1]\). The cosine rule gives
\[
 D^2=x^2s^2+y^2t^2-(x^2+y^2-z^2)st.
\]
Set \(U=x^2, V=y^2, W=U+V-z^2\). Direct integration, using \(\mathbb E s^k=1/(k+1)\), gives
\[
 \mathbb E D^2=\frac{U+V}{3}-\frac W4,\qquad
 \mathbb E D^4=\frac{U^2+V^2}{5}+\frac{W^2+2UV}{9}-\frac{W(U+V)}4.
\]
These formulas hold at obtuse angles too: the cosine rule already handles the sign.

Weight the same-side integrals by \(\ell_i^2/P^2\) and the three unordered distinct-side integrals by \(2\ell_i\ell_j/P^2\). In particular,
\[
\begin{aligned}
P^2m_4={}&\sum_i\frac{\ell_i^6}{15}\\
&+2\sum_{\{i,j,k\}=\{1,2,3\},\ i<j}\ell_i\ell_j\left[
\frac{\ell_i^4+\ell_j^4}{5}
+\frac{(\ell_i^2+\ell_j^2-\ell_k^2)^2+2\ell_i^2\ell_j^2}{9}
-\frac{(\ell_i^2+\ell_j^2-\ell_k^2)(\ell_i^2+\ell_j^2)}4\right].
\end{aligned}
\]
The corresponding formula for \(m_2\) uses \(\ell_i^4/6\) and the quadratic conditional expectation above. Collecting symmetric monomials and applying Heron's identity
\[
16A^2=P(P-2a)(P-2b)(P-2c)
\]
yields exactly the two announced moment formulas. The standalone checker evaluates both independent expressions as exact rational numbers for several nonisosceles and isosceles triangles.

**Step 2: invert the moments.** Divide the first identity by \(P^2\) and solve for \(A^2\), which is strictly positive. Solve the second identity for \(e_2\). For \(e_3=p_1p_2p_3\), direct elementary-symmetric expansion of the first formula gives
\[
\frac{m_2}{P^2}=\frac16-\frac12e_2+e_3.
\]
Thus \(e_3\) is recovered. Vieta's formulas determine the unordered roots \(p_1,p_2,p_3\) uniquely and therefore the side-length multiset \(\{Pp_1,Pp_2,Pp_3\}\). The side-side-side congruence theorem completes the inverse claim, including repeated-root (isosceles) cases.

**Step 3: minimality.** At fixed \(P=1\) consider the two isosceles normalized side triples
\[
 \left(\frac14,\frac38,\frac38\right),\qquad
 \left(\frac{1+\sqrt5}{8},\frac{7-\sqrt5}{16},\frac{7-\sqrt5}{16}\right).
\]
They are noncongruent and satisfy the strict triangle inequalities. Their triangle-inequality slack triples \((1-2p_i)\) both have product \(1/32\). Therefore both have \(A^2=1/512\), hence both have \(m_2=29/768\). However their values of \(e_2\) are, respectively, \(21/64\) and \((31+5\sqrt5)/128\), which differ, so their \(m_4\) differ. One initial even moment is insufficient.

**Step 4: sharp fixed-\(P,A\) range.** Introduce positive normalized triangle-inequality slacks \(t_i=1-2p_i\). These satisfy
\[
 t_1+t_2+t_3=1,\quad t_1t_2t_3=K=\frac{16A^2}{P^4},\quad
 e_2=\frac{1+t_1t_2+t_2t_3+t_3t_1}{4}.
\]
By arithmetic-geometric mean, \(K\le1/27\), with equality only for \(t_1=t_2=t_3=1/3\). For \(0<K<1/27\), the level set \(\{t_i>0:\sum t_i=1,\prod t_i=K\}\) is compact and connected: it is the boundary, in the positive affine simplex, of the convex superlevel set of the strictly concave function \(\sum_i\log t_i\).

At an extremum of \(t_1t_2+t_2t_3+t_3t_1\) on that level set, the Lagrange multiplier equations imply that each \(t_i\) solves one common quadratic equation. Thus at least two slacks are equal. Write the extremal triples, up to permutation, as \((x,x,1-2x)\). The product constraint becomes \(x^2(1-2x)=K\), whose two roots in \((0,1/2)\) are \(\alpha<1/3<\beta\). At either point \(e_2=E(x)\).

The relation \(\alpha^2(1-2\alpha)=\beta^2(1-2\beta)\) and \(\alpha\ne\beta\) implies \(\alpha+\beta=2(\alpha^2+\alpha\beta+\beta^2)\). Consequently \((\beta-\alpha)^2=(\alpha+\beta)(2-3(\alpha+\beta))>0\), so \(\alpha+\beta<2/3\). Hence
\[
 E(\beta)-E(\alpha)=\frac{(\beta-\alpha)(2-3(\alpha+\beta))}{4}>0.
\]
The fourth-moment formula increases strictly with \(e_2\) at fixed \(A\), so the stated two isosceles bounds, including equality cases, follow. Connectedness of the level set and continuity of \(m_4\) show that all intermediate values occur.

## Verification
Run `python3 verify.py` with Python 3. The checker independently evaluates the side-conditioned exact rational double integrals and the closed formulas for six triangles (including scalene, right, isosceles and near-degenerate cases), reconstructs their symmetric functions, evaluates 750 independent triangle instances against the analytic sharp envelope, and performs 170000 direct arclength endpoint pair simulations on a \(3\)-\(4\)-\(5\) triangle. The checked execution reports `VERIFY_OK exact_triangle_cases=6 reconstruct_checks=6 sharp_envelope_samples=750 random_pair_trials=170000`. Simulations are supplementary only; the proof is the symbolic integration and compactness argument above.

## Relationship to prior work
Bäsel (2012), sections 1–5, investigates motion-invariant-line random chords of **regular** polygons and distances between **interior-uniform** point pairs. In particular its probability measures are different from the independent boundary-arclength endpoint measure above, and the inspected paper gives neither this fourth moment nor the prescribed-\(P,A\) isosceles envelope. Tong, Ahmadi and Pan (2013), sections I–II of its available text, likewise explicitly sample points inside arbitrary triangles, rather than on their perimeters. A published second-moment boundary comparison establishes the first moment formula in a different normalization; the second-moment identity here is used as credited background, not claimed as new.

Gates (1982) proves triangle recognition from odd moments of a different invariant-line chord-length distribution; its full text was not accessible during this comparison. A known inverse theorem for the **full invariant-chord law** does not by itself supply the two-moment reconstruction, the specific boundary-endpoint probability model, or the fixed-\(P,A\) sharp fourth-moment interval. Unindexed earlier boundary-moment calculations remain a priority risk.

## Limitations
The result assumes a known perimeter and exact population moments; it does not assert that two distance moments without perimeter determine the absolute triangle, nor does it quantify statistical errors from a finite number of sampled endpoint pairs. At \(A\to0\) the inverse coefficient \(1/A^2\) becomes ill-conditioned. Historical priority is provisional, and the inaccessible Gates full text is a named comparison risk, not evidence of novelty. No independent validation has been performed.

## References
- U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first posted 2012-04-12, https://arxiv.org/abs/1204.2707 .
- F. Tong, M. Ahmadi, J. Pan, *Random Distances Associated with Arbitrary Triangles: A Systematic Approach between Two Random Points*, arXiv:1312.2498, first posted 2013-11-29, https://arxiv.org/abs/1312.2498 .
- J. Gates, *Recognition of triangles and quadrilaterals by chord length distribution*, J. Applied Probability 19 (1982), 873–879, https://doi.org/10.2307/3213843 .
- *Exact second-moment boundary gap for arbitrary Euclidean triangles*, published mathematical finding (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-second-moment-boundary-gap-for-arbitrary-euclidean-triangl--d886b40f95a8 . Its stated second-moment identity is credited, not claimed as new.
