# Stratified extreme metric distortion on products of circles

## Finding
Let \(d\ge 2\), let \(r_1,\dots,r_d>0\), and equip the embedded flat product torus
\[
T_{\mathbf r}=S^1(r_1)\times\cdots\times S^1(r_d)\subset\mathbb R^{2d}
\]
with its induced intrinsic length metric. For two independent Riemannian-volume-uniform points \(X,Y\), set \(Z=d_T(X,Y)/\lVert X-Y\rVert\) (the null event \(X=Y\) is immaterial). Define, for any nonempty \(A\subseteq\{1,\dots,d\}\),
\[
S_A=\sum_{j\in A}r_j^2,\qquad
c_A=\frac{2^d S_A^{(d+|A|)/2}}{\pi^{|A|}\Gamma((d+|A|)/2+1)(\pi^2-4)^{(d-|A|)/2}
\prod_{j\in A}r_j^2\prod_{i\notin A}r_i}.
\]
The sharp essential maximum of \(Z\) is \(\pi/2\). As \(\varepsilon\downarrow0\), for every fixed positive radius vector,
\[
\Pr\{Z>\pi/2-\varepsilon\}
= C_1\varepsilon^{(d+1)/2}+C_2\varepsilon^{(d+2)/2}
+O_{d,\mathbf r}(\varepsilon^{(d+3)/2}),
\qquad C_k=\sum_{|A|=k}c_A\quad(k=1,2).
\]
In particular,
\[
C_1=\frac{2^d}{\pi\Gamma((d+3)/2)(\pi^2-4)^{(d-1)/2}}
\frac{\sum_{j=1}^d r_j^d}{\prod_{j=1}^d r_j}
\ge \frac{d\,2^d}{\pi\Gamma((d+3)/2)(\pi^2-4)^{(d-1)/2}},
\]
with equality **if and only if all radii coincide**. This singles out the balanced Clifford torus, including the minimal Clifford torus when \(d=2\) and the product lies in the unit three-sphere.

Conditioned on \(Z>\pi/2-\varepsilon\), with probability tending to one exactly one folded angular difference is near \(\pi\). Its index \(J\) converges to
\[
\Pr\{J=j\}=\frac{r_j^d}{\sum_i r_i^d}.
\]
Thus these labelled near-maximal-event proportions recover every ratio of radii; combining them with the ambient Euclidean diameter \(2\sqrt{\sum_i r_i^2}\) recovers all radii. Given \(J=j\), the normalized leading deficit contributions and slack jointly converge to \(\operatorname{Dirichlet}(1,\tfrac12,\ldots,\tfrac12,1)\), with \(d-1\) half-parameters (in the order antipodal-coordinate linear deficit, \(d-1\) coincident-coordinate quadratic deficits, and slack).

## Assumptions and scope
The integer \(d\ge2\) and every radius are held fixed as \(\varepsilon\downarrow0\). All points are independent and uniform for normalized intrinsic volume, not uniformly chosen from the ambient sphere. The random variable concerns the **intrinsic-to-ambient-Euclidean distance ratio**, not the intrinsic distance alone. The global essential maximum is approached on positive-measure neighborhoods; equality itself has probability zero. In dimension two, the two leading exponents are \(3/2\) and \(2\).

## Proof
**1. Exact angular representation.** Write the two points by their circle angles. Their independent wrapped angular differences have independent folded magnitudes \(U_j\) uniform on \([0,\pi]\). By orthogonal product geometry and the shortest circular arc formula,
\[
d_T(X,Y)^2=\sum_j r_j^2U_j^2,\qquad
\lVert X-Y\rVert^2=4\sum_j r_j^2\sin^2(U_j/2).
\]
Consequently
\[
Z(U)^2=\frac{\sum_j r_j^2 U_j^2}{4\sum_jr_j^2\sin^2(U_j/2)},\qquad
\Pr(Z>t)=\pi^{-d}\operatorname{vol}_d\{U\in[0,\pi]^d:Z(U)>t\}.
\]
This formula also gives a reproducible exact integral at every threshold.

**2. Complete maximizer classification.** For \(0<u\le\pi\), the strictly increasing function \(u/[2\sin(u/2)]\) lies in \((1,\pi/2]\), with equality at the upper endpoint alone. The displayed expression for \(Z^2\) is the weighted average of its squared values, with positive weights \(4r_j^2\sin^2(U_j/2)\) whenever \(U_j>0\). Therefore \(Z=\pi/2\) precisely at the \(2^d-1\) corners where each \(U_j\in\{0,\pi\}\) and at least one equals \(\pi\). At the remaining corner \(U=0\), the quotient extends continuously with limit \(1\). It is bounded strictly below \(\pi/2\) off disjoint fixed neighborhoods of these finitely many corners.

**3. Uniform local normal form.** Fix a nonempty antipodal index set \(A\), with \(k=|A|\). In its corner neighborhood put \(s_j=\pi-U_j\ge0\) for \(j\in A\) and \(y_i=U_i\ge0\) otherwise. Expanding both squared distances and then their square-root quotient gives
\[
\frac\pi2-Z=\sum_{j\in A}\frac{r_j^2}{2S_A}s_j+
\sum_{i\notin A}\frac{(\pi^2-4)r_i^2}{16\pi S_A}y_i^2
+O\!\left((\sum_{j\in A}s_j+\sum_{i\notin A}y_i^2)^2\right).
\]
More strongly the deficit is real analytic in the nonnegative variables \((s_j,t_i)\) with \(t_i=y_i^2\), and has strictly positive linear partial derivatives there. This follows from the explicit cosine formula, the nonzero Euclidean chord at every such corner, and the analytic square root near a positive number. Write the leading coefficients as \(a_j=r_j^2/(2S_A)\) and \(b_i=(\pi^2-4)r_i^2/(16\pi S_A)\).

**4. Exact corner-volume constants and error.** Rescale \(s_j=\varepsilon x_j\) and \(y_i=\sqrt\varepsilon z_i\). The leading volume is that of \(\sum_{j\in A}a_j x_j+\sum_{i\notin A}b_i z_i^2<1\), with nonnegative coordinates. On using \(v_i=b_i z_i^2\), its volume is
\[
\frac{\prod_{j\in A}a_j^{-1}\prod_{i\notin A}b_i^{-1/2}}{2^{d-k}}
\frac{\Gamma(1/2)^{d-k}}{\Gamma((d+k)/2+1)}.
\]
Multiplying by the uniform density \(\pi^{-d}\) yields exactly \(c_A\). The analytic implicit-function change of variables in the positive orthant and the weighted monomial density \(\prod v_i^{-1/2}\) show that each corner contributes
\[
c_A\varepsilon^{(d+k)/2}\bigl(1+O_{d,\mathbf r}(\varepsilon)\bigr).
\]
This is an integer relative-power expansion, not a presumed absence of a half-order term: it follows from analytic dependence on \(t_i=y_i^2\). Adding all corners, those with \(k=1\) contribute the first term; those with \(k=2\) contribute the second; all remaining corners and local corrections start at order \(\varepsilon^{(d+3)/2}\). This also treats \(d=2\), when no corners of order three exist.

**5. Rigidity, inverse data, and conditional laws.** For singleton \(A=\{j\}\), the formula reduces to \(c_{\{j\}}=K_d r_j^d/\prod_i r_i\), where \(K_d=2^d/[\pi\Gamma((d+3)/2)(\pi^2-4)^{(d-1)/2}]\). AM–GM gives \(\sum_jr_j^d\ge d\prod_j r_j\), with equality precisely at equal radii, proving the global sharp bound and uniqueness. The asymptotically disjoint singleton contributions yield the index probabilities. In each singleton corner, the normalized variables \((a_js_j, b_iy_i^2)/\varepsilon\), jointly with the remaining slack, converge by a Dirichlet integral to the stated distribution with parameters \(1\) for the linear coordinate, \(1/2\) for each quadratic coordinate, and \(1\) for slack. If the index proportions are labelled, \(r_i/r_j=(\Pr(J=i)/\Pr(J=j))^{1/d}\); the ambient chord diameter gives the remaining scale.

## Verification
The attached standalone `checks/verify_clifford_tail.py` implements the exact angle formula, the gamma-function constants, and independent deterministic numerical quadrature of the two-dimensional sublevel sets in disjoint corner neighborhoods. It tests three radius pairs, four deficit thresholds per pair, strict error decay toward the two-term expansion, higher-dimensional equal-radius rigidity, and angular pointwise bounds. Run with `python checks/verify_clifford_tail.py` using Python and SciPy. A successful replay prints `CLIFFORD_STRATIFIED_TAIL_CHECKS_OK 2436`. The proof above, not the numerical tests, supplies the all-dimensional asymptotic claim.

## Relationship to prior work
Brendle's 2012 Clifford-torus rigidity theorem [1] establishes the canonical balanced geometric object and minimality within the relevant class of embedded minimal tori in the three-sphere, but contains no uniform-pair distortion distribution. Tavernier and coauthors [2] explicitly distinguish intrinsic/geodesic from ambient Euclidean distances on products of circles and derive the Euclidean chord expression for orthogonal Clifford supercells; these are important *known input formulas*, not new claims here. Their application and conclusions concern Coulomb lattice sums rather than a stratified probability tail, a sharp radius-imbalance inequality, or a conditional defect distribution. Published research-record summaries concerning intrinsic distances on flat-torus inversion quotients and Clifford-torus spectral restriction also address different observables. The full research-record source pages were not independently accessible during this comparison, so absence of a historic equivalent theorem is not asserted as certified.

## Limitations
Asymptotics are for fixed strictly positive radii: no uniform control as a radius collapses or the number of factors grows is established. The statistic uses the flat product's intrinsic metric and the particular orthogonal product embedding, not an arbitrary isometric embedding of the same intrinsic torus. The conditional inverse statement requires labelled factors; unlabeled proportions recover only the radius multiset. Numerical quadratures are diagnostics, not infinite mathematical certificates. The literature comparison does not establish definitive historical priority, and no independent audit has been performed.

## References
[1] S. Brendle, *Embedded minimal tori in S^3 and the Lawson conjecture*, arXiv:1203.6597, version 1 publicly submitted 2012-03-29, https://arxiv.org/abs/1203.6597 .

[2] N. Tavernier, G. L. Bendazzoli, V. Brumas, S. Evangelisti and J. A. Berger, *Clifford Boundary Conditions for Periodic Systems: the Madelung Constant of Cubic Crystals in 1, 2 and 3 Dimensions*, arXiv:2107.04686v1, 2021-07-09, https://arxiv.org/html/2107.04686v1 .

[3] Published research-record summary, *Schur ordering and exact geodesic pair-distance laws on flat inversion orbifolds*, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-schur-ordering-and-exact-geodesic-pair-distance-laws-on-flat-inv--158649a31c2d (summary comparison only; full text unavailable).

[4] Published research-record summary, *Exact Clifford-torus harmonic trace spectrum and sharp exponential inverse instability*, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-clifford-torus-harmonic-trace-spectrum-and-sharp-exponenti--2d81ee89510d (summary comparison only; full text unavailable).
