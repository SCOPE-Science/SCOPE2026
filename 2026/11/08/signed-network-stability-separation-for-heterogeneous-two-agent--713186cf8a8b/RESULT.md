# Signed-network stability separation for heterogeneous two-agent gradient tracking

## Finding
Fix a relative curvature disparity \(0<\eta<1\) and consider the two-node constant-step quadratic gradient-tracking recurrence defined below. Let \(B_+(\sigma,\eta)\) and \(B_-(\sigma,\eta)\) be the suprema of strictly Schur-stable normalized stepsizes for two symmetric stochastic networks with respective nontrivial eigenvalues \(+\sigma\) and \(-\sigma\), but identical essential spectral radius \(0<\sigma<1\) and curvature dispersion \(\eta\). Then
\[
\lim_{\sigma\uparrow1}B_+(\sigma,\eta)=\frac{2}{1+\eta},\qquad
\lim_{\sigma\uparrow1}\frac{B_-(\sigma,\eta)}{1-\sigma}=2.
\]
In particular, their admissible stepsize ceilings have an unbounded ratio:
\[
\frac{B_+(\sigma,\eta)}{B_-(\sigma,\eta)}\sim\frac{1}{(1+\eta)(1-\sigma)}.
\]
This is a sharp necessary scale for a stabilizing rule that knows only network essential spectral radius and curvature dispersion: it must obey the smaller near-bipartite ceiling, even when the corresponding positive-eigenvalue network admits a stepsize bounded away from zero. We also give the exact necessary-and-sufficient three-dimensional Schur test and a finite, rational stable/unstable pair at the same descriptors.

## Assumptions and scope
For \(-1<\nu<1\) define
\[
 W_\nu=\frac12\begin{pmatrix}1+\nu&1-\nu\\1-\nu&1+\nu\end{pmatrix},\qquad
 H_\eta=\operatorname{diag}(1+\eta,1-\eta).
\]
These are positive-entry symmetric doubly stochastic mixing matrices and strictly positive local scalar curvatures with mean one. The optimization objective is the average of the two centered costs \(f_i(x)=\tfrac12(H_\eta)_{ii}x^2\), with unique minimizer zero. For a common normalized constant stepsize \(\beta>0\), use precisely the update
\[
 x_{j+1}=W_\nu(x_j-\beta y_j),\qquad
 y_{j+1}=W_\nu y_j+H_\eta(x_{j+1}-x_j),\qquad y_0=H_\eta x_0.
\]
The tracker is **not** mixed after adding the gradient difference; that alternative changes the method under heterogeneous curvatures. In the orthonormal consensus/disagreement coordinates, after removing the invariant unit eigenvalue, the remaining transition on the scaled tracker average, position disagreement, and scaled tracker disagreement is
\[
 A_{\nu,\eta}(\beta)=
 \begin{pmatrix}
 1-\beta&\beta\eta(\nu-1)&-\beta\eta\nu\\
 0&\nu&-\nu\\
 -\beta\eta&\beta(\nu-1)&(1-\beta)\nu
 \end{pmatrix}.
\]
Define \(\mathcal{S}_{\nu,\eta}=\{\beta>0:\rho(A_{\nu,\eta}(\beta))<1\}\) and \(B_\pm(\sigma,\eta)=\sup\mathcal{S}_{\pm\sigma,\eta}\). These are upper endpoints as suprema; no assertion that the complete stability set is an interval is needed. The statements concern exact-arithmetic constant-step linear convergence, not optimal convergence rates or time-varying steps.

## Proof
**1. Characteristic polynomial and exact Schur test.** Direct determinant expansion gives \(Q(z)=\det(zI-A)=z^3+a z^2+b z+c\), where
\[
\begin{aligned}
 a&=\beta(1+\nu)-1-2\nu,\\
 b&=\nu^2+2\nu-4\beta\nu+\beta^2\nu(1-\eta^2),\\
 c&=-\nu^2+\beta\nu(1+\nu)-\beta^2\nu(1-\eta^2).
\end{aligned}
\]
The real monic cubic is strictly Schur stable if and only if
\[
|c|<1,\quad 1+a+b+c>0,\quad1-a+b-c>0,\quad1-b+ac-c^2>0.
\]
This is the classical cubic Jury/Schur test, and \(1+a+b+c=\beta(1-\nu)^2>0\). These explicit polynomial inequalities are a complete finite-parameter stability classification.

**2. Negative spectral endpoint.** Put \(\nu=-1+\delta\), with \(\delta=1-\sigma\downarrow0\), and take \(\beta=k\delta\) for fixed \(k>0\). The remaining necessary Schur expressions have expansions
\[
\begin{aligned}
1-a+b-c&=4k\delta+O(\delta^2),\\
1+c&=2\delta+O(\delta^2),\qquad1-c=2+O(\delta),\\
1-b+ac-c^2&=(8-4k)\delta+O(\delta^2).
\end{aligned}
\]
The already-positive expression \(1+a+b+c\) equals \(4k\delta+O(\delta^2)\). Thus every \(0<k<2\) gives a strictly stable step for all sufficiently small \(\delta>0\), proving \(\liminf B_-/\delta\ge2\).

For the matching upper bound, any stable step has \(|c|<1\). Since
\[
c=-(1-\delta)^2-\beta\delta(1-\delta)+\beta^2(1-\delta)(1-\eta^2),
\]
with fixed \(0<\eta<1\), the condition \(c<1\) bounds all stable \(\beta\) uniformly as \(\delta\downarrow0\). If a stable sequence had a positive limit \(\beta_0\), its limiting fourth Schur expression would have to be nonnegative, whereas at \(\nu=-1\) it is exactly
\[
1-b+ac-c^2=-\beta\big[(1-\eta^2)^2\beta^3-4(1-\eta^2)\beta+4\big]<0
\]
for every \(\beta>0\). Indeed, writing \(h=1-\eta^2\in(0,1)\) and \(u=\sqrt h\,\beta\), the bracket is \(4+\sqrt h(u^3-4u)\), strictly positive because \(u^3-4u\ge-16/(3\sqrt3)>-4\). Therefore every stable sequence has \(\beta\to0\). Taylor expansion near \((\delta,\beta)=(0,0)\) now gives
\[
1-b+ac-c^2=8\delta-4\beta+O((\delta+\beta)^2).
\]
Positivity forces \(\beta\le(2+o(1))\delta\) for every stable choice, proving \(\limsup B_-/\delta\le2\).

**3. Positive spectral endpoint.** Put \(\nu=1-\delta\). At the limiting, disconnected matrix \(\nu=1\) one has the exact factorization
\[
Q(z)=(z-1)[z-1+\beta(1+\eta)][z-1+\beta(1-\eta)].
\]
For every fixed \(0<\beta<2/(1+\eta)\), all Schur inequalities other than \(1+a+b+c>0\) are strictly satisfied at \(\nu=1\); the exceptional expression is exactly \(\beta\delta^2>0\) for each \(\delta>0\). Continuity consequently gives strict stability for all sufficiently small positive \(\delta\), whence \(\liminf B_+\ge 2/(1+\eta)\).

Conversely, if the roots are strictly inside the unit disk, the monic cubic coefficient obeys \(|a|<3\); near \(\nu=1\), this bounds \(\beta\), since \(a=\beta(1+\nu)-1-2\nu\). Any accumulation point \(\beta_0\) of stable choices must give a limiting polynomial whose three roots lie in the closed disk. Its explicit limiting root \(1-\beta_0(1+\eta)\) therefore has modulus at most one, so \(\beta_0\le2/(1+\eta)\). This proves \(\limsup B_+\le2/(1+\eta)\), and the ratio follows.

**4. Finite same-descriptor separation.** At \(\eta=1/2\), \(\sigma=1/2\), and \(\beta=6/5\), the two exact reduced characteristic polynomials are
\[
 Q_+(z)=z^3-\tfrac15z^2-\tfrac{61}{100}z+\tfrac{11}{100},\qquad
 Q_-(z)=z^3+\tfrac35z^2+\tfrac{111}{100}z-\tfrac1{100}.
\]
For \(Q_+\), the four Schur checks are strictly positive, including \(1-b+ac-c^2=15759/10000\). For \(Q_-\), that last expression is \(-1161/10000\), so it is not Schur. Its derivative is everywhere positive, and its values at \(z=0\) and \(z=1/100\) have opposite signs, so its sole real root \(r\) lies in \((0,1/100)\). Since the product of all three roots is \(1/100\), its conjugate pair has squared modulus \(1/(100r)>1\). Thus there is exponential instability in the negative-signed reduced recurrence and strict stability in the positive-signed one. The polynomial \(100Q_-\) has no root modulo \(7\), so its real root is irrational. Therefore even the valid rational initial position \(x_0=(1,-1)^\top\), with \(y_0=H_\eta x_0\), has a nonzero component in the unstable real two-dimensional eigenspace: its nonzero reduced coordinate vector is rational up to common normalization and cannot be an eigenvector of a rational matrix for an irrational eigenvalue. The unstable component necessarily appears in position, as the disagreement position equation has nonzero coupling to tracker disagreement for \(\nu\ne0\). Hence some actual local position iterates diverge exponentially.

## Verification
The standalone `verify_dgt.py` recomputes the full four-dimensional recurrence, factors out its invariant eigenvalue, reconstructs the cubic and exact Jury expressions, verifies both singular limiting factorizations and first-order asymptotic coefficients, checks the rational stable/unstable example and modulo-seven irreducibility, and evaluates additional rational Schur witnesses. It is supplementary to the analytic proof. Run with Python 3 and SymPy using `python verify_dgt.py`.

## Relationship to prior work
Wang, Ballotta, Carli, Iannelli, Cao and Schenato (arXiv:2608.03548v1) give the exact heterogeneous reduced matrix and a conservative spectral-radius certificate using only \((\sigma,\eta)\); their explicitly solved exact cases are complete networks and homogeneous curvature. The present exact two-node Schur conditions and the sharp, signed, heterogeneous *stability-ceiling asymptotics* are not derived there. In particular a sufficient certificate does not imply the upper bound for all stable steps.

A published analysis entitled *Exact sign-aware graph-specific tuning for homogeneous distributed gradient tracking* (published-finding corpus, October 2026) already proves the signed-endpoint optimal contraction tuning for **homogeneous** local curvatures. Sign sensitivity itself is therefore not asserted as new. That result concerns \(\eta=0\) and rate-optimal tuning rather than the present fixed \(\eta>0\) stability ceilings. Tian, Chai and Xu (arXiv:2607.23601v1) derive exact worst-case rates for DIGing and AugDGM over graph/function classes. Their displayed AugDGM update mixes the gradient difference inside the consensus operation; that differs from Wang et al.'s update here when \(H_\eta\) and \(W_\nu\) do not commute. Their full text does not state the present sharp two-node asymptotic law. The cubic Schur criterion itself is classical.

## Limitations
The exact formulas and asymptotics apply only to two nodes, centered scalar strongly convex quadratics, a symmetric positive mixing matrix, common constant stepsize, fixed positive disparity \(0<\eta<1\), and exact arithmetic. The result does not imply that the signed-edge effect is absent in homogeneous problems; the homogeneous rate-optimal sign effect was previously known. The asymptotic upper endpoint does not classify potentially disconnected stability regions. Nor does it quantify convergence with time-varying graph weights, multidimensional noncommuting Hessians, or independent local stepsizes. A broader prior result on robust graph-dependent stability might subsume the specialization; the comparisons below leave historical priority open to independent examination.

## References
1. Y. Wang, L. Ballotta, R. Carli, A. Iannelli, X. Cao and L. Schenato, *Adaptive Stepsizes With Certified Convergence in Distributed Gradient Tracking With Quadratic Costs*, arXiv:2608.03548v1, 4 August 2026, https://arxiv.org/abs/2608.03548.
2. Q. Tian, L. Chai and J. Xu, *Exact Worst-case Convergence Rates of Distributed Gradient Tracking Methods*, arXiv:2607.23601v1, 26 July 2026, https://arxiv.org/html/2607.23601v1.
3. *Exact sign-aware graph-specific tuning for homogeneous distributed gradient tracking*, published October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-sign-aware-graph-specific-tuning-for-homogeneous-distribut--4bef30512fd6.
4. E. I. Jury, *Inners and Stability of Dynamic Systems*, Wiley, 1974; standard cubic Jury/Schur stability test.
