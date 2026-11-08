# A Robin critical window for numerical ranges of boundary-perturbed unilateral shifts

## Finding
Let \(S e_j=e_{j+1}\) be the unilateral shift on \(\ell^2(\mathbb N_0;\mathbb C)\), let \(P_0\) project onto \(e_0\), and let \(T_t=S+tP_0\), with \(t\ge0\). Its essential numerical range is always the closed unit disk, yet its ordinary numerical range undergoes an exact boundary transition at \(t=1/2\). For every angle \(\theta\in[-\pi,\pi]\), its support function is
\[
 h_t(\theta):=\sup_{z\in W(T_t)}\operatorname{Re}(e^{-i\theta}z)=
 \begin{cases}1,&t\cos\theta\le1/2,\\
 t\cos\theta+(4t\cos\theta)^{-1},&t\cos\theta>1/2.
 \end{cases}
\]
When \(0\le t\le1/2\), \(W(T_t)=\{z:|z|<1\}\). When \(t>1/2\), put \(\theta_0=\arccos((2t)^{-1})\). The closure is the compact convex body specified by \(h_t\); its boundary consists of the circular arc \(\{e^{i\theta}:\theta_0\le|\theta|\le\pi\}\) and the attached curved arc
\[
 z_t(\theta)=t(1-r_\theta^2)+r_\theta e^{i\theta},\qquad
 r_\theta=(2t\cos\theta)^{-1},\qquad |\theta|\le\theta_0.
\]
Exactly the curved arc with \(|\theta|<\theta_0\) belongs to the numerical range; the circular arc and the two junction points do not. Every interior point of the closure belongs to \(W(T_t)\). In particular, \(w(T_t)=1\) for \(t\le1/2\), whereas \(w(T_t)=t+(4t)^{-1}\) for \(t>1/2\).

Let \(T_{n,t}\) be the compression of \(T_t\) onto \(\operatorname{span}\{e_0,\ldots,e_{n-1}\}\), for each integer \(n\ge1\), and write \(w_n(t)=w(T_{n,t})\). There is an *exact finite-size crossing*:
\[
 w_n(t)\begin{cases}<1,&0\le t<(n+1)/(2n),\\
 =1,&t=(n+1)/(2n),\\
 >1,&t>(n+1)/(2n).
 \end{cases}
\]
The critical window is universal. For any fixed \(\alpha\in\mathbb R\), take \(t_n=1/2+\alpha/n\), which is nonnegative for sufficiently large \(n\). Then
\[
 \lim_{n\to\infty} n^2\bigl(w_n(t_n)-1\bigr)=F(\alpha),
\]
where
\[
 F(\alpha)=\begin{cases}
 -k(\alpha)^2/2,&\alpha<1/2,\quad k(\alpha)\in(0,\pi),\quad k(\alpha)\cot k(\alpha)=2\alpha,\\
 0,&\alpha=1/2,\\
 \kappa(\alpha)^2/2,&\alpha>1/2,\quad\kappa(\alpha)>0,\quad\kappa(\alpha)\coth\kappa(\alpha)=2\alpha.
 \end{cases}
\]
Both defining roots are unique. More generally, for every pair of fixed real parameters \(\alpha,\beta\), the finite-section supporting functions have the two-parameter angular boundary-layer law
\[
 \lim_{n\to\infty}n^2\left(h_{n,t_n}(\beta/\sqrt n)-1\right)
 =F(\alpha-\beta^2/4),
\]
where \(h_{n,t}(\theta)=\sup_{z\in W(T_{n,t})}\operatorname{Re}(e^{-i\theta}z)\). This distinguishes the critical angular scale \(n^{-1/2}\) from the radial scale \(n^{-2}\).

For fixed \(t\), the outer approximation also has three regimes:
\[
 1-w_n(t)\sim\frac{\pi^2}{2n^2}\quad(0\le t<1/2),\qquad
 1-w_n(1/2)\sim\frac{\pi^2}{8n^2},
\]
whereas for every fixed \(t>1/2\), with \(r=2t\),
\[
 w(T_t)-w_n(t)\sim\frac{(r^2-1)^2}{2r^3}\,r^{-2n}.
\]

## Assumptions and scope
The Hilbert space is complex and countably infinite, and the finite sections have exactly \(n\) coordinates. The perturbation is the real nonnegative scalar multiple of the rank-one *diagonal* projection \(P_0\), not an exceptional shift weight. Numerical ranges use \(W(A)=\{\langle Ax,x\rangle:\|x\|=1\}\). The support function refers to the ordinary scalar numerical range, not the higher matrix ranges. The critical-window limits hold for fixed parameters as \(n\to\infty\); no uniformity over unbounded parameter sets is asserted. Complex perturbation scalars reduce to this real case by rotating the numerical range.

## Proof
**1. Supporting lines and the half-line Jacobi operator.** For any \(\theta\), the self-adjoint operator \(\operatorname{Re}(e^{-i\theta}T_t)\) is diagonally unitarily equivalent to
\[
 H_v=(S+S^*)/2+vP_0,\qquad v=t\cos\theta.
\]
Consequently \(h_t(\theta)=\sup\sigma(H_v)\). For each \(x=(x_j)\in\ell^2\), the elementary discrete-gradient identity gives
\[
 \langle H_vx,x\rangle=\|x\|^2-(1/2-v)|x_0|^2-\tfrac12\sum_{j\ge0}|x_{j+1}-x_j|^2.
\]
For \(v\le1/2\), this is at most \(\|x\|^2\), with equality impossible for a nonzero square-summable vector. Vectors nearly constant over long consecutive blocks show that the supremum is exactly \(1\).

When \(v>1/2\), put \(r=(2v)^{-1}<1\). The vector \((1,r,r^2,\ldots)\) is an eigenvector of \(H_v\) with eigenvalue \(v+(4v)^{-1}>1\). There is no larger eigenvalue: for any spectral value \(\lambda>1\), the interior recurrence forces a square-summable eigenvector proportional to \((1,r_\lambda,r_\lambda^2,\ldots)\), with \(\lambda=(r_\lambda+r_\lambda^{-1})/2\) and \(0<r_\lambda<1\); the first-coordinate equation then forces \(v=(2r_\lambda)^{-1}\). Above the essential band \([-1,1]\), all spectral points are eigenvalues because this is a rank-one perturbation. Hence the displayed support formula is exact.

**2. The complete ordinary numerical range.** For \(t\le1/2\), all supporting functions equal \(1\), so the closure is the closed unit disk. No circle point is attained, as attaining it would produce a top eigenvector of some \(H_v\) with \(v\le1/2\); thus the range is the open unit disk. For \(t>1/2\), the top eigenvector at an angle with \(|\theta|<\theta_0\) has normalized coordinates \(\sqrt{1-r_\theta^2}\,r_\theta^j e^{-ij\theta}\). Its numerical value is exactly \(z_t(\theta)\) above. At all other angles the top value is \(1\), not an eigenvalue, and therefore no corresponding boundary point is attained. The support formula and its continuous first derivative identify the two boundary arcs and their junctions. Convexity of the numerical range and the general fact that the interior of the closure of a convex subset of \(\mathbb R^2\) lies in that set complete the classification. Compact perturbation invariance of essential numerical range, together with the unilateral shift's essential numerical range, gives \(W_{\mathrm e}(T_t)=\overline{\mathbb D}\). Finally the maximum of the support function occurs at \(\theta=0\), yielding the numerical-radius formula.

**3. Exact finite-section determinant and crossing.** Let \(H_{n,v}\) be the \(n\times n\) Jacobi matrix with diagonal \((v,0,\ldots,0)\) and adjacent entries \(1/2\). Positivity of the matrix entries of \(T_{n,t}\) implies
\[
 w_n(t)=\lambda_{\max}(H_{n,t}),\qquad h_{n,t}(\theta)=\lambda_{\max}(H_{n,t\cos\theta}).
\]
Indeed, replacing any test vector by its coordinatewise moduli never decreases the absolute quadratic-form estimate, and a nonnegative Perron eigenvector attains the symmetric-part maximum. Let \(U_j\) be Chebyshev polynomials of the second kind, normalized by \(U_j(\cos x)=\sin((j+1)x)/\sin x\), \(U_0=1\), and \(U_1(z)=2z\). The determinant recurrence yields the exact identity
\[
 \det(\lambda I-H_{n,t})=2^{-n}\bigl(U_n(\lambda)-2tU_{n-1}(\lambda)\bigr).
\]
At \(\lambda=1\), the polynomial vanishes precisely when \(t=(n+1)/(2n)\). In that case the positive eigenvector has coordinates proportional to \((n,n-1,\ldots,1)\), so \(1\) is the top eigenvalue; strict monotonicity in \(t\) follows from positivity of the leading normalized eigenvector's first coordinate. This proves the finite crossing and the angular crossing criterion \(h_{n,t}(\theta)>1\) exactly when \(t\cos\theta>(n+1)/(2n)\).

**4. Robin critical window.** Fix \(\alpha<1/2\). The top eigenvalue in the critical window is below \(1\) and may be written \(\cos\vartheta_n\), with \(0<\vartheta_n\le\pi/(n+1)\) for all sufficiently large \(n\). The determinant equation becomes
\[
 \sin((n+1)\vartheta_n)=(1+2\alpha/n)\sin(n\vartheta_n).
\]
Putting \(k_n=n\vartheta_n\), every accumulation point in \([0,\pi]\) satisfies \(k\cos k=2\alpha\sin k\). Zero cannot be a solution after dividing by \(k\), since \(\alpha<1/2\), and \(\pi\) cannot solve the undivided equation. The function \(k\cot k\) is strictly decreasing from \(1\) to \(-\infty\), so \(k_n\) converges to its unique solution \(k(\alpha)\); therefore \(n^2(\cos(k_n/n)-1)\to-k(\alpha)^2/2\).

For \(\alpha>1/2\), the top eigenvalue is greater than \(1\), and setting it equal to \(\cosh(\eta_n)\) changes the determinant equation into \(\sinh((n+1)\eta_n)=(1+2\alpha/n)\sinh(n\eta_n)\). The quantities \(n\eta_n\) remain bounded since \(\lambda_{\max}(H_{n,t_n})\le\sup\sigma(H_{t_n})=1+O_\alpha(n^{-2})\). Every limit solves \(\kappa\coth\kappa=2\alpha\), uniquely because the left side rises strictly from \(1\) to infinity. This gives the positive branch. For \(\alpha=1/2\), the finite crossing makes the scaled difference identically zero. Continuity of the two root branches at \(\alpha=1/2\) follows from the small-argument expansions of cotangent and hyperbolic cotangent.

For the angular law, put \(\theta_n=\beta/\sqrt n\). Then
\[
 n\left(t_n\cos\theta_n-\tfrac12\right)
 \longrightarrow\alpha-\beta^2/4.
\]
The preceding root argument holds also for varying critical-window parameters converging to a finite limit (including the junction), and the angular result follows. In particular, the exact angular set where the finite support exceeds one has half-width \(\arccos((n+1)/(2nt_n))\) if \(\alpha>1/2\); its leading value is \(\sqrt{4\alpha-2}\,n^{-1/2}\).

**5. Fixed-parameter finite-size asymptotics.** For fixed \(t<1/2\), the top finite eigenvalue is \(\cos\vartheta_n\) with \(n\vartheta_n\to\pi\), yielding the first inverse-square law. At \(t=1/2\), the Chebyshev equation reduces exactly to \(\vartheta_n=\pi/(2n+1)\), giving the second law. For fixed \(t>1/2\) and all sufficiently large \(n\), write the finite top eigenvalue \(\cosh\eta_n\) and put \(y_n=e^{\eta_n}\). The exact equation is
\[
 y_n\frac{1-y_n^{-2n-2}}{1-y_n^{-2n}}=r=2t.
\]
The increasing eigenvalue convergence implies \(y_n\to r>1\). Expanding this equation gives \(r-y_n=(r-r^{-1})r^{-2n}(1+o(1))\). Taking the difference between \((r+r^{-1})/2\) and \((y_n+y_n^{-1})/2\) yields the stated exponentially small asymptotic.

## Verification
The standalone file `checker.py` uses exact rational polynomial arithmetic to verify the determinant/Chebyshev identity and the \(\lambda=1\) crossing for several dimensions and rational parameters. It also compares finite tridiagonal eigenvalues with the critical and exponential asymptotics. Running `python checker.py` in an environment with NumPy and SciPy prints `CHECKS_PASSED 261`. These finite diagnostics do not prove the general theorem; the analytic proof above handles all dimensions, parameters and limits. Reproducibility requires only this file and NumPy/SciPy.

## Relationship to prior work
Audeh, Kittaneh and Moradi study integral representations and exact numerical radii of alternating block shift paths (arXiv:2610.15242v1); this supplies the contemporary numerical-radius motivation but not rank-one *diagonal* defects or critical finite-section scaling. Farenick, Li and Singla investigate essential matrix ranges and their operator-system lifting geometry (arXiv:2510.08322, 2026 publication), whereas the present result explicitly compares one scalar essential numerical range with its boundary-perturbed ordinary numerical range and its finite compressions. Chien and Sheu's 2013 and Vandanjav and Undrakh's 2014 weighted-shift papers address off-diagonal weighted shift matrices/operators, which differ from the diagonal perturbation here. Ko and Lee (2011) analyze general rank-one perturbations of the unilateral shift, but their theorems concern point spectrum, hyponormality, and commutants; their complete public author text does not derive the numerical range, the finite-section threshold, or the Robin crossover. The half-line Jacobi recurrence, Chebyshev polynomials and Robin spectral limits are standard tools; their general machinery is not claimed as new. No claim is made concerning the general Smith–Ward problem or the higher-level matrix ranges.

## Limitations
The family is a single rank-one diagonal defect of the free unilateral shift; the result is not a classification of arbitrary finite-rank perturbations, arbitrary Toeplitz symbols or operator-valued defects. The asymptotic statements concern fixed parameters and do not give a uniform error estimate on an unbounded parameter set. General Jacobi/Robin boundary-scaling literature may contain an equivalent or stronger result stated without the numerical-range terminology; this is a residual originality risk. The related 2014 weighted-shift article could not be inspected in full from the available source, but its accessible theorem concerns off-diagonal modifications. Independent mathematical verification and publication-priority assessment remain outstanding.

## References
1. W. Audeh, F. Kittaneh, H. R. Moradi, *Integral Representations and Sharp Numerical Radius Inequalities for Hilbert Space Operators*, arXiv:2610.15242v1, first submitted 2026-10-11, https://arxiv.org/abs/2610.15242.
2. D. Farenick, C.-K. Li, S. Singla, *Geometry of essential matrix ranges and the Smith–Ward problem for operator systems*, arXiv:2510.08322; *Bulletin of the London Mathematical Society* 58 (2026), e70481, https://doi.org/10.1112/blms.70481.
3. M.-T. Chien, H.-A. Sheu, *The numerical radii of weighted shift matrices and operators*, *Operators and Matrices* 7 (2013), https://doi.org/10.7153/OAM-07-11.
4. A. Vandanjav and B. Undrakh, *On the numerical range of some weighted shift matrices and operators*, *Linear Algebra and its Applications* (2014), https://doi.org/10.1016/j.laa.2014.02.018.
5. E. Ko and J. E. Lee, *On rank one perturbations of the unilateral shift*, *Communications of the Korean Mathematical Society* 26 (2011), 79–88, https://doi.org/10.4134/CKMS.2011.26.1.079.
