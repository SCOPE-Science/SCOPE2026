# A sharp isoperimetric depth transition for the odd-cycle stable-set cut

## Finding
For every odd integer \(n\ge5\), let \(C_n\) be the simple \(n\)-cycle with cyclic indices and let
\[
F_n=\{x\in\mathbb R^n:x_i\ge0,\ x_i+x_{i+1}\le1\text{ for all }i\}.
\]
For a normalized cutting-plane depth \(0\le s\le1\), define
\[
P_n(s)=F_n\cap\bigl\{x:\textstyle\sum_i x_i\le(n-s)/2\bigr\}.
\]
Thus \(P_n(0)=F_n\), while \(P_n(1)\) is the ordinary integral stable-set polytope of \(C_n\). Let \(E=E_{n-1}>0\) be the Euler secant number, equivalently the number of up-down permutations of \(n-1\) labels. Writing \(V\) for coordinate-Euclidean \(n\)-volume and \(S\) for Euclidean \((n-1)\)-dimensional boundary measure, the **complete cutting-depth formulas** are
\[
\begin{aligned}
V(P_n(s))&=\frac{E}{2(n-1)!}-\frac{s^n}{2n!},\\
S(P_n(s))&=\frac{nE(1+1/\sqrt2)}{(n-1)!}
-\frac{(n/\sqrt2-\sqrt n)s^{n-1}}{(n-1)!}.
\end{aligned}
\]
Define the scale-invariant Euclidean isoperimetric quotient
\[
I(P)=\frac{S(P)}{V(P)^{(n-1)/n}}.
\]
Set \(a=(1-\sqrt{2/n})/[(1+\sqrt2)E]\), \(b=1/(nE)\) and \(p=(n-1)/n\). Then
\[
\frac{I(P_n(s))}{I(P_n(0))}=
\frac{1-a s^{n-1}}{(1-b s^n)^p}.
\]
The unique minimum of this quotient for \(0\le s\le1\) is as follows:

- For \(n=5\), it occurs at the **strictly interior** depth
  \[
  s_*=\frac{5(1-\sqrt{2/5})}{1+\sqrt2}=0.761209517034\ldots.
  \]
  Moreover \(I(P_5(s_*))<I(P_5(0))<I(P_5(1))\): a partial cut improves the quotient, but the full integral cut makes it worse than the original fractional relaxation.
- For every odd \(n\ge7\), the quotient is strictly decreasing over \([0,1]\); its unique minimum is the **full integral cut** \(s=1\), and \(I(P_n(1))<I(P_n(0))\).

No tie occurs at any integer dimension in the asserted range. The relative full-cut improvement satisfies
\[
E_{n-1}\left(1-\frac{I(P_n(1))}{I(P_n(0))}\right)\longrightarrow\sqrt2-1
\]
along odd \(n\to\infty\). The former three-angle ridge spectrum of the stable-set polytope is not claimed as new here.

## Assumptions and scope
All bodies are full-dimensional subsets of the **fixed standard Euclidean coordinate space** \(\mathbb R^n\). Surface measure includes every facet at its actual Euclidean scale; it is not lattice-normalized boundary volume. No affine-invariance of these measurements is asserted. The cut ranges over the entire path \(0\le s\le1\), not just its endpoints; only odd \(n\ge5\) are included. A zero-depth new facet is interpreted as absent, with vanishing measure. The Euler numbers are positive by definition, with \(E_4=5\), \(E_6=61\), and generating function \(\sec t=\sum_{k\ge0}E_{2k}t^{2k}/(2k)!\).

## Proof
**1. The fractional volume and its facets.** The coordinate facets \(x_i=0\) are each isometric to the path fractional stable-set polytope on \(n-1\) coordinates. Complementing alternating even-position coordinates turns its inequalities into the alternating-order inequalities on \([0,1]^{n-1}\), so the standard permutation-chamber decomposition gives each such coordinate facet area \(E/(n-1)!\). The only other facets of \(F_n\) are the \(n\) cycle-edge inequalities \(x_i+x_{i+1}\le1\), all congruent, and all at perpendicular distance \(1/\sqrt2\) from the origin. Since the origin lies on every coordinate facet, the divergence/pyramid formula gives
\[
nV(F_n)=\frac n{\sqrt2}A_{\mathrm{edge}},
\qquad A_{\mathrm{edge}}=\sqrt2 V(F_n).
\]
For completeness, the exact fractional volume follows from the self-adjoint integral operator \((Tf)(u)=\int_0^{1-u}f(v)\,dv\): cyclic integration gives \(V(F_n)=\operatorname{tr}(T^n)\). Its complete cosine eigenbasis has eigenvalues \(2(-1)^j/[(2j+1)\pi]\), \(j\ge0\), so for odd \(n\) the standard Dirichlet-beta/secant identity yields \(V(F_n)=E/[2(n-1)!]\). Thus
\[
S(F_n)=n\frac{E}{(n-1)!}+n\sqrt2 V(F_n)
=\frac{nE(1+1/\sqrt2)}{(n-1)!}.
\]
The same fractional-volume identity and the basic simplex cap appear in the referenced prior study of the odd-cycle integrality cap; neither is independently claimed here.

**2. Exact geometry at every cut depth.** Define \(y_i=1-x_i-x_{i+1}\). The cyclic linear operator \(A=I+P\), with \(P\) the cyclic coordinate shift, satisfies \(|\det A|=2\) for odd \(n\) and
\[
\sum_i x_i=\frac{n-\sum_i y_i}{2}.
\]
In the removed region \(0\le\sum_i y_i<s\), one has \(y_i\ge0\). The inverse maps \(y=0\) to \(h=\mathbf1/2\) and maps \(y=e_i\) to the \(n\) distinct incidence vectors \(v_i\) of maximum stable sets; its columns have alternating entries of absolute value \(1/2\). Hence the whole simplex \(\{y\ge0,\sum_i y_i\le s\}\) maps inside \(F_n\) for \(0\le s\le1\). Its determinant gives removed volume \(s^n/(2n!)\).

The removed \(n\)-simplex has base in the new hyperplane \(\sum_i x_i=(n-s)/2\), at perpendicular distance \(s/(2\sqrt n)\) from its apex \(h\). Its base area therefore equals \(s^{n-1}\sqrt n/(n-1)!\). Each of the other \(n\) faces lies on an original cycle-edge facet and is at perpendicular distance \(s/\sqrt2\) from the opposite simplex vertex. Each removed old-facet area is \(s^{n-1}/[\sqrt2(n-1)!]\). Because this small simplex meets no coordinate-facet interior for \(s<1\), and meets those facets only in lower-dimensional sets at \(s=1\), the change in total boundary area is precisely **one added base minus \(n\) removed old-facet pieces**. This proves both exact formulas for every \(s\).

**3. Uniqueness and the dimension threshold.** After normalizing the formulas, the derivative of the logarithm of the isoperimetric quotient is
\[
\frac{d}{ds}\log I(P_n(s))=
\frac{(n-1)s^{n-2}(bs-a)}{(1-a s^{n-1})(1-b s^n)}
\quad(0<s<1).
\]
Both denominators are strictly positive because they are ratios of positive surface areas and volumes. Thus the derivative changes from negative to positive only at \(s_*=a/b=n(1-\sqrt{2/n})/(1+\sqrt2)\). For \(n=5\), elementary bounds \(\sqrt{2/5}>63/100\) and \(\sqrt2>7/5\) give \(s_*<1\), while clearly \(s_*>0\). For odd \(n\ge7\), the function \((1-\sqrt{2/n})/(1+\sqrt2)\) increases with \(n\); already at \(n=7\) it exceeds \(1/7\), since \(6>\sqrt{14}+\sqrt2\). Therefore \(s_*>1\) for all such dimensions. Strict monotonicity and uniqueness follow.

**4. Comparison of both endpoints.** With \(p=(n-1)/n\), the full-cut ratio is \((1-a)/(1-b)^p\). For \(n=5\), the bounds just cited give \(a<pb\), whence concavity yields \((1-b)^p\le1-pb<1-a\) and therefore \(I(P_5(1))>I(P_5(0))\). For \(n\ge7\), the strict inequality \(s_*=a/b>1\) gives \(a>b\), and \(1-a<1-b<(1-b)^p\); hence \(I(P_n(1))<I(P_n(0))\). Finally, \(E_{n-1}\to\infty\), \(aE_{n-1}\to1/(1+\sqrt2)\), and \(bE_{n-1}=1/n\). Expanding the exact ratio (with uniform second-order remainder) proves the stated scaled limit \(\sqrt2-1\).

## Verification
The standalone `verify_odd_cycle_cut.py` uses exact rational determinants and Gram matrices to verify the cut simplex and each facet-area value for odd dimensions \(3,5,7,9\), and enumerates alternating permutations for the corresponding Euler numbers. It also checks the critical-depth location. When NumPy and SciPy are installed it independently enumerates all stable-set vertices and computes the full convex-hull volumes and areas at the endpoints for dimensions \(3,5,7\). Recorded successful output: `ODD_CYCLE_CUT_GEOMETRY_PASS cases=4 exact_simplex_facets=28`. Exact finite calculations test normalizations but are **not** used as proof for arbitrary \(n\); that is supplied analytically above.

## Relationship to prior work
The odd-cycle inequality and the equivalence of the fully tightened relaxation with the stable-set polytope are established polyhedral theory, including the detailed convex-hull proof of Bärmann and Schneider. De Vries, Friedrich and Perscheid study extended formulations for odd-cycle and wheel inequalities. The published *Antiperiodic Brownian geometry of the odd-cycle integrality cap* already supplies the simplex description, removed volume and fractional volume, so these are prerequisites, not novelty claims. A separate previously recorded work establishes the complete ridge-angle spectrum and its odd-hole crossover, which is likewise excluded. The present contribution is the **full Euclidean boundary-area evolution and scale-invariant cutting-depth optimization**, including an interior optimum for the pentagon and a different all-higher-dimensions regime. No inspected stronger prior statement supplies this entire metric phase diagram.

## Limitations
All conclusions concern the standard Euclidean coordinate realization and the single symmetric cut family. The result does not compare arbitrary orientations or all possible valid cutting planes, nor establish an isoperimetric optimum among all bodies or all stable-set relaxations. Published sources and indexed searches cannot exclude every unindexed equivalent statement; in particular, the cap geometry makes the area formula accessible to a separate calculation, although the precise full-depth optimization was not found in the inspected material. Independent validation has not been performed.

## References
1. S. de Vries, U. Friedrich, B. Perscheid, *An extended formulation for the 1-wheel inequalities of the stable set polytope*, Networks 75 (2020), 86–94, first published 2019-10-17, https://doi.org/10.1002/net.21906 .
2. A. Bärmann, O. Schneider, *Set characterizations and convex extensions for geometric convex-hull proofs*, arXiv:2101.09267v1 (2021-01-22), Theorem 5, https://arxiv.org/abs/2101.09267 ; Mathematical Programming 195 (2022), 475–515.
3. *Antiperiodic Brownian geometry of the odd-cycle integrality cap*, publicly indexed scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-antiperiodic-brownian-geometry-of-the-odd-cycle-integrality-cap--826a819e0b80 .
4. S. Kafer, K. Pashkovich, L. Sanità, *On the Circuit Diameter of Some Combinatorial Polytopes*, arXiv:1709.09642 (2017-09-27), https://arxiv.org/abs/1709.09642 .
