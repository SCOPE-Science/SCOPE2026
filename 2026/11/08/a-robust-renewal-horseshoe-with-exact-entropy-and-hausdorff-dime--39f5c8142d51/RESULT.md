# A robust renewal horseshoe with exact entropy and Hausdorff dimension in a boundary-Hopf return map

## Finding
For the continuous planar map
\[
F_{a,b}(x,y)=\begin{cases}
(ax+y-1,0),&x\le 0,\\
(bx+y-1,(1-b)x),&x\ge 0,
\end{cases}
\]
and every \(|a+2|\le10^{-3}\), \(|b-3/2|\le10^{-3}\), there exists the explicitly defined compact invariant Cantor set \(\Lambda_{a,b}\) on which \(F_{a,b}\) is topologically conjugate to the one-sided subshift of finite type with adjacency matrix
\[
A=\begin{pmatrix}1&1&0\\0&0&1\\1&0&0\end{pmatrix}.
\]
The entropy of this restricted system is exactly \(\log\lambda\), where \(\lambda>1\) is the unique root of \(\lambda^3-\lambda^2-1=0\); numerically \(\log\lambda\approx0.382245085840\). Its Hausdorff dimension is the unique positive solution of
\[
|a|^{-d}+|a[1+(a-1)b]|^{-d}=1.
\]
At the central parameter \((a,b)=(-2,3/2)\), the dimension is approximately \(0.573118339016\). These are invariants of the specific subsystem constructed below, not assertions about the full planar attractor.

## Assumptions and scope
All maps act on the real plane. The left and right formulas agree at \(x=0\), so \(F_{a,b}\) is continuous. All parameter bounds are inclusive. Let
\[
I=[-9/10,-1/100],\qquad k=1+(a-1)b,\qquad s=ak.
\]
For this parameter box, \(a<0\), \(k<0\), and \(s>1\). Define affine contractions on \(I\) by
\[
\phi_0(t)=\frac{t+1}{a},\qquad
\phi_1(t)=\frac{t+k+a+1}{ak}.
\]
Their unique nonempty compact invariant attractor \(K\subset I\) satisfies \(K=\phi_0(K)\sqcup\phi_1(K)\). Put
\[
S=K\times\{0\},\qquad E=\phi_1(K)\times\{0\},\qquad
\Lambda=S\cup F_{a,b}(E)\cup F_{a,b}^{2}(E).
\]
This definition of \(K\) is independent of the auxiliary interval \(I\) once its two affine maps are fixed: it is the unique compact IFS attractor.

## Proof
**1. Exact returns.** A point \((x,0)\) with \(x\in\phi_0(I)\) has \(x<0\) and makes one left iteration, returning to \((ax-1,0)\in I\). For \(x\in\phi_1(I)\), its first three iterates obey the strict signs \(x<0\), \(ax-1>0\), and \(b(ax-1)-1<0\). Thus the branch word is \(LRL\). Direct composition gives the third-step section map
\[
R_1(x)=a\{b(ax-1)-1\}+(1-b)(ax-1)-1
=akx-k-a-1.
\]
The one-step section map is \(R_0(x)=ax-1\). Consequently \(R_i\circ\phi_i=\operatorname{id}_I\) for \(i=0,1\).

**2. Uniform strict margins.** Exact rational interval arithmetic on the entire closed parameter box gives
\[
\begin{aligned}
-3.504501&\le k\le-3.495501,\\
6.987506499&\le s\le7.012506501,\\
\phi_0(I)&\subset(-1/2,-1/25),\\
\phi_1(I)&\subset(-4/5,-3/5).
\end{aligned}
\]
The two inverse images are disjoint and lie strictly inside \(I\). Moreover the first image of \(\phi_1(I)\times\{0\}\) has positive first coordinate, and the second has negative first coordinate and negative second coordinate, with strict bounds; the standalone rational checker provides all bounds. Thus both return itineraries are uniform across the parameter box. Since their contractions have respective ratios \(1/|a|<1\) and \(1/|s|<1\), there is a unique compact disjoint-branch attractor \(K\) with its standard unique one-sided two-symbol address.

**3. Three-state coding.** The points of \(S\) have disjoint alternatives: the cylinder \(\phi_0(K)\times\{0\}\) returns to \(S\) after one iteration, and the cylinder \(E\) first passes through \(F(E)\) and \(F^2(E)\) before returning after three iterations. The three geometric phases are disjoint: \(S\) lies on the negative horizontal axis, \(F(E)\) lies on the positive horizontal axis, and \(F^2(E)\) has negative second coordinate. The maps of the cylinders to their successor phases are continuous and one-to-one; the third step on \(F^2(E)\) is one-to-one since its induced return map has nonzero slope \(s\). Unique inverse-limit addresses therefore give a homeomorphism intertwining \(F|_\Lambda\) and the one-sided Markov shift with transitions \(0\to0\), \(0\to1\), \(1\to2\), \(2\to0\). Compactness and forward invariance follow immediately.

**4. Entropy.** The matrix is irreducible and primitive; its characteristic polynomial is \(z^3-z^2-1\). Perron--Frobenius theory and shift conjugacy yield \(h_{\mathrm{top}}(F|_\Lambda)=\log\rho(A)=\log\lambda\). In particular, the Artin--Mazur zeta function of this compact subsystem is \(1/(1-z-z^3)\).

**5. Dimension.** The two similarities \(\phi_0,\phi_1\) satisfy the strong separation condition inside \(I\). The self-similar dimension theorem therefore gives \(\dim_HK=d\), the unique root of \(|a|^{-d}+|ak|^{-d}=1\). The two additional phase sets \(F(E)\) and \(F^2(E)\) are affine injective images of the one-dimensional Cantor set \(\phi_1(K)\) with nonzero linear derivatives. Each is bi-Lipschitz to its source, so the dimension of their finite union with \(S\) is also \(d\).

## Verification
Run `python3 verify.py` using the accompanying standalone standard-library checker. It certifies the parameter box with rational interval operations, exact section-return equalities at rational boundary/central parameters, the strict intermediate itinerary signs, and the cubic adjacency-matrix identity. It also reports supplemental numerical approximations to entropy and dimension. The proof above establishes all real parameters in the box; the finite exact tests are not substituted for that general interval argument.

## Relationship to prior work
Simpson's 2026 boundary-Hopf study introduces exactly the displayed two-parameter map as equation (4.1) and discusses predominantly numerical chaotic attractors; it does not state this specified uniform renewal subsystem or its entropy and dimension. Simpson's separate 2026 study of one-dimensional first returns establishes Farey-ordered return structures in the repelling-focus regime \(\delta_R>1\) and \(\delta_R>\tau_R^2/4\). Here \(\delta_R=b-1\) lies near \(1/2\), outside those hypotheses. Classical theory of separated affine IFSs, Markov subshifts, and border-collision robust chaos supplies ingredients rather than the parameter-specific two-branch construction. Earlier broad zero-determinant studies remain a historical-priority risk because their complete texts were not accessible in this review.

## Limitations
Only the constructed compact Cantor subsystem is conjugate to the stated Markov shift; neither full-attractor conjugacy nor an exact entropy of the entire planar map is claimed. The Hausdorff dimension concerns \(\Lambda\), not its basin or an ambient attractor. The two inverse branches and the explicit parameter box are sufficient, not asserted optimal. All computations are subordinate to the analytic proof. Historical novelty beyond the inspected primary text is not independently established.

## References
1. D. J. W. Simpson, *Boundary Hopf bifurcations in three-dimensional Filippov systems*, arXiv:2604.06570 (first publicly available 2026-04-08), especially section 4 and equation (4.1). https://arxiv.org/abs/2604.06570
2. D. J. W. Simpson, *One-dimensional first return maps for the two-dimensional border-collision normal form with a zero determinant*, arXiv:2606.08901 (2026-06-08), especially theorem hypotheses in sections 1--2. https://arxiv.org/abs/2606.08901
3. D. J. W. Simpson, *The two-dimensional border-collision normal form with a zero determinant*, arXiv:2408.04790 (2024); complete text not accessed. https://arxiv.org/abs/2408.04790
4. P. A. Glendinning and D. J. W. Simpson, *A constructive approach to robust chaos using invariant manifolds and expanding cones*, Discrete and Continuous Dynamical Systems 41 (2021), 3367--3387. https://doi.org/10.3934/dcds.2020409
5. P. Kowalczyk, *Robust chaos and border-collision bifurcations in non-invertible piecewise-linear maps*, Nonlinearity 18 (2005), 485--504. https://doi.org/10.1088/0951-7715/18/2/002
