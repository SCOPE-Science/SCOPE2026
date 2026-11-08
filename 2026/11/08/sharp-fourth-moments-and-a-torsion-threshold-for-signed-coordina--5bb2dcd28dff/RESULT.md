# Sharp fourth moments and a torsion threshold for signed-coordinate Fourier crosses

## Finding
Fix integers \(d\ge 2\) and \(m\ge4\), let \(G=(\mathbb Z/m\mathbb Z)^d\), and give \(G\) normalized counting measure. Let \(\zeta_m=\exp(2\pi i/m)\), write \(z_j(x)=\zeta_m^{x_j}\), and consider the signed-coordinate Fourier spectrum
\[
E=\{0,e_1,-e_1,\ldots,e_d,-e_d\}.
\]
For arbitrary complex coefficients and
\[
f(x)=c+\sum_{j=1}^{d}\bigl(a_jz_j(x)+b_j\overline{z_j(x)}\bigr),\qquad
S=|c|^2+\sum_{j=1}^{d}(|a_j|^2+|b_j|^2),
\]
the exact sharp fourth-moment inequality is
\[
\boxed{\|f\|_{L^4(G)}^4\le K_{d,m}S^2,\qquad
K_{d,m}=\begin{cases}
\dfrac{6d+1}{2d+1},&m=4,\\[3pt]
\dfrac{3(4d+1)}{4d+3},&m\ge5.
\end{cases}}
\tag{1}
\]
Both constants are attained. Thus a genuine fourth-root-of-unity resonance persists in every dimension, while the sharp constant stabilizes at character order five.

The theorem includes complete equality conditions and a quantitative energy stability estimate. Define \(v_j=|a_j|^2+|b_j|^2\) and \(s=|c|^2\). Every polynomial satisfies
\[
K_{d,m}S^2-\|f\|_4^4\ge
\begin{cases}
2\left(s-\dfrac{S}{2d+1}\right)^2+
\displaystyle\sum_{j=1}^d\left(v_j-\dfrac{2S}{2d+1}\right)^2,&m=4,\\[8pt]
2\left(s-\dfrac{3S}{4d+3}\right)^2+
\dfrac32\displaystyle\sum_{j=1}^d\left(v_j-\dfrac{4S}{4d+3}\right)^2,&m\ge5.
\end{cases}
\tag{2}
\]
For \(S>0\), equality in (1) holds exactly when the appropriate squared coefficient energies agree with the centers in (2), every \(|a_j|=|b_j|>0\), and all products \(a_jb_j\overline c^{\,2}\) are positive real. When \(m=4\) there is one additional condition: all \(a_j^2\overline{b_j}^{\,2}\) are positive real. For \(m\ge5\), no further phase condition is required. Equality is invariant under an overall nonzero scalar multiple; the coefficient phases need not arise from translations by points of a finite group.

## Assumptions and scope
The positive integer \(d\) is at least two; the single-coordinate case is a known three-frequency problem and is not claimed as new. The integer \(m\) is at least four, so \(0,e_j,-e_j\) are distinct. There are no assumptions that the coefficients are real or of equal magnitude. The Fourier characters are unnormalized; \(L^p\) norms use the uniform probability measure on \(G\). In (2) the right side is homogeneous of degree four and vanishes at the zero polynomial. The same constant, equality classification, and second branch of (2) hold on the continuous torus \(\mathbb T^d\) with its independent Haar-uniform coordinate characters.

## Proof
**Step 1: the exact one-coordinate moments.** For independent uniformly distributed \(m\)-th roots of unity \(Z_j\), let
\[
Y_j=a_jZ_j+b_jZ_j^{-1},\qquad
v_j=|a_j|^2+|b_j|^2,\qquad w_j=2a_jb_j.
\]
Character orthogonality gives \(\mathbb E Y_j=0\), \(\mathbb E|Y_j|^2=v_j\), \(\mathbb E Y_j^2=w_j\), and \(\mathbb E(|Y_j|^2Y_j)=0\). The last identity uses only the absence of odd exponents \(\pm1,\pm3\) divisible by \(m\ge4\). Direct expansion gives
\[
\mathbb E|Y_j|^4=
\begin{cases}
v_j^2+2|a_jb_j|^2+2\operatorname{Re}(a_j^2\overline{b_j}^{\,2}),&m=4,\\
v_j^2+2|a_jb_j|^2,&m\ge5.
\end{cases}
\tag{3}
\]
The additional term occurs because the Fourier exponents \(4\) and \(-4\) alias to zero precisely at order four. As \(2|a_jb_j|\le v_j\), (3) implies
\[
\mathbb E|Y_j|^4\le\gamma v_j^2,
\quad \gamma=\begin{cases}2,&m=4,\\3/2,&m\ge5.\end{cases}
\tag{4}
\]
Equality in the second branch holds exactly when \(|a_j|=|b_j|\). In the first branch it also requires \(a_j^2\overline{b_j}^{\,2}>0\), provided \(v_j>0\).

**Step 2: independent-coordinate expansion and sharp bound.** Put \(s=|c|^2\) and \(R=\sum_jv_j\). Independence and the moments above give the exact formula
\[
\begin{aligned}
\mathbb E\left|c+\sum_jY_j\right|^4
={}&s^2+4sR+2\operatorname{Re}\left(\overline c^{\,2}\sum_jw_j\right)
+\sum_j\mathbb E|Y_j|^4\\
&+\sum_{i<j}\left(4v_iv_j+2\operatorname{Re}(w_i\overline{w_j})\right).
\end{aligned}
\tag{5}
\]
By \(|w_j|\le v_j\), (4), and \(S=s+R\), equation (5) yields
\[
\mathbb E|f|^4\le s^2+6sR+\gamma\sum_jv_j^2
+6\sum_{i<j}v_iv_j
=3S^2-2s^2-(3-\gamma)\sum_jv_j^2.
\tag{6}
\]
The positive quadratic penalty in (6) has the exact square completion
\[
2s^2+(3-\gamma)\sum_jv_j^2
=\frac{2(3-\gamma)}{2d+3-\gamma}S^2
+2(s-s_*)^2+(3-\gamma)\sum_j(v_j-v_*)^2,
\tag{7}
\]
where
\[
s_*=\frac{3-\gamma}{2d+3-\gamma}S,\qquad
v_*=\frac{2}{2d+3-\gamma}S.
\]
This identity follows by expanding the squares and using \(s+\sum_jv_j=S\). Substitution of \(\gamma=2\) or \(\gamma=3/2\) proves (1) and (2), including the exact leading coefficients.

**Step 3: attainability and complete equality.** For \(m\ge5\), choose positive real coefficients proportional to
\[
c=\sqrt3,\qquad a_j=b_j=\sqrt2\quad(1\le j\le d).
\]
Then \(S=4d+3\) and all inequalities in (4)--(7) are equalities. For \(m=4\), choose \(c=a_j=b_j=1\), giving \(S=2d+1\) and again equality throughout. These witnesses establish optimality.

Conversely, equality in (1) forces equality in (7), which gives \(s=s_*>0\), \(v_j=v_*>0\). Equality in (5)--(6) forces \(|w_j|=v_j\), so each \(|a_j|=|b_j|>0\), and simultaneous phase alignment of \(\overline c^{\,2}w_j\) and \(w_i\overline{w_j}\). The first alignments are equivalent to \(a_jb_j\overline c^{\,2}>0\); they automatically imply the second alignments. At order four, equality in (4) imposes the additional squares-alignment conditions in the statement. Every displayed condition is sufficient, since it makes all the upper bounds equalities. This exhausts all nonzero extremizers. On \(\mathbb T^d\) the same character moments as \(m\ge5\) apply, completing the torus assertion.

## Verification
The standalone standard-library program `artifacts/checker.py` reconstructs all pair-sum convolution fibers in integer Gaussian arithmetic for \(m=4,5,6,7\) and \(d=1,2,3\). For 624 seeded complex-integer coefficient tests it checks exact equality between the convolution formula and the independent-moment identity, and checks (1) exactly using rational arithmetic. It evaluates all 12 prescribed real-phase equality witnesses directly on the finite groups, then independently compares 72 general-complex inputs using discrete Fourier sums with integer convolution. It additionally checks 96 general-complex energy-deficit inequalities and 72 non-real extremizers across dimensions two and three. It reports `SIGNED_COORDINATE_CROSS_L4_PASS cases=876 exact_integer_convolutions=624`. Execute from the folder containing this file with `python artifacts/checker.py`; it requires only Python's standard library. Finite tests are corroboration, not a substitute for the uniform proof above.

## Relationship to prior work
Neuwirth's analysis of metric unconditionality for Fourier subsets establishes how even Fourier moments detect additive relations, but does not state the signed-coordinate-cross sharp constants or the order-four threshold. Baernstein and Culverhouse study majorization and sharp Khinchin inequalities for sums of independent uniform sphere vectors with scalar weights; those theorems are relevant to fourth moments, but their stated hypotheses and conclusions do not provide the arbitrary complex-paired-frequency equality classification or order-four torsion jump here. The three-frequency classification in the published research corpus already gives the cases \(d=1\): \(7/3\) at order four and \(15/7\) at higher orders. That one-dimensional result is explicitly excluded from the new contribution.

Published results for complete two-axis Fourier extension on finite abelian products allow every point on either full axis, rather than two signed coordinate characters in each of arbitrarily many independent directions. A separate five-frequency Ferrers-aperture theorem treats a different collision pattern, with one midpoint collision and linked mixed-row collisions, not the two independent midpoint collisions of the signed-coordinate cross in dimension two. Consequently neither inspected result implies the all-dimensional bound, equality, or stability in (1)--(2) without further unproved reductions. The comparison is bounded: historical full priority and any implicit older Khintchine-type general theorem remain open.

## Limitations
The stated sharp constants rely on each coordinate character having order at least four; at orders two or three the frequency set aliases or has additional fourth-moment resonances. No sharp higher even moment, mixed-modulus formula, or growing-spectrum asymptotic is proved. The energy-deficit inequality (2) controls coefficient energies, not a complete optimal distance to the full phase-aligned extremizer manifold. The polynomial calculation is elementary but its exact dimension-dependent phase classification and order-four torsion threshold constitute the present mathematical claim. Independent verification and a comprehensive historical-priority review have not been performed.

## References
1. S. Neuwirth, *Metric unconditionality and Fourier analysis*, arXiv:math/9707211, first public 1997-07-28, https://arxiv.org/abs/math/9707211.
2. A. Baernstein II and R. C. Culverhouse, *Majorization of sequences, sharp vector Khinchin inequalities, and bisubharmonic functions*, Studia Math. 152 (2002), 231–248, https://doi.org/10.4064/sm152-3-3.
3. S. Neuwirth, *The Sidon constant of sets with three elements*, arXiv:math/0102145, first public 2001-02-19, https://arxiv.org/abs/math/0102145.
4. *Exact Lambda(4) constants for every three-character subset of a cyclic group*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-lambda-4-constants-for-every-three-character-subset-of-a-c--5562292e7127.
5. *Sharp fourth-moment extension and one-axis rigidity for finite abelian crosses*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-extension-and-one-axis-rigidity-for-finite-a--5b31463115dc.
6. *Sharp fourth moments for a five-point Ferrers Fourier spectrum*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moments-for-a-five-point-ferrers-fourier-spectrum--bb5fd3f72396.
