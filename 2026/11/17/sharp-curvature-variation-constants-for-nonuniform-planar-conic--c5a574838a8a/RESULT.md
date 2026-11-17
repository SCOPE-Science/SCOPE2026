# Sharp curvature-variation constants for nonuniform planar conic-spline interpolation

## Finding
Fix an integer \(N\geq 2\). Let \(\mathcal F\) be a centrally symmetric fan of \(2N\) distinct rays of \(\mathbb R^2\), whose angles satisfy
\[
\theta_0<\theta_1<\cdots<\theta_{2N}=\theta_0+2\pi,
\qquad \theta_{j+N}=\theta_j+\pi.
\]
Put \(h_j=\theta_{j+1}-\theta_j\), and assume \(0<h_j<\pi\) for every \(j\). Set \(h_*=\max_jh_j\). For every continuous nonnegative absolutely homogeneous function \(q:\mathbb R^2\to[0,\infty)\) with angular profile \(\rho(\theta)=q(\cos\theta,\sin\theta)\) and finite measure \(\mu=(D_\theta^2+1)\rho\) on the circle, let \(q_{\mathcal F}\) be its nodal conic-spline interpolant. With \(M=|\mu|(\mathbb R/(2\pi\mathbb Z))\), the exact estimates are
\[
\boxed{\|q-q_{\mathcal F}\|_{L^\infty(S^1)}\leq \frac14\tan(h_*/2)\,M,}
\qquad
\boxed{\|q-q_{\mathcal F}\|_{L^1(S^1)}\leq (\sec(h_*/2)-1)\,M.}
\]
The \(L^1\) norm uses **un-normalized angular arc-length measure** \(d\theta\), not probability measure. For every such fan both constants are attained simultaneously by a rank-one seminorm. Therefore these coefficients are the exact operator-error norms even if the admissible functions are restricted to continuous seminorms.

Among all centrally symmetric fans with \(2N\) distinct rays satisfying the above gap condition, the unique minimizing fan for either sharp coefficient, up to rotation, has equally spaced rays. Its optimal coefficients are
\[
\boxed{C_\infty(N)=\tfrac14\tan\bigl(\tfrac\pi{2N}\bigr),\qquad
C_1(N)=\sec\bigl(\tfrac\pi{2N}\bigr)-1.}
\]
In particular, \(C_\infty(N)\sim\pi/(8N)\) and \(C_1(N)\sim\pi^2/(8N^2)\).

## Assumptions and scope
Absolute homogeneity means \(q(\lambda x)=|\lambda|q(x)\) for every real \(\lambda\) and vector \(x\). In particular \(\rho(\theta+\pi)=\rho(\theta)\). Neither convexity nor a positive-definite null space is assumed. The curvature distribution \(\mu=\rho''+\rho\) is a finite signed Radon measure, and its total variation is \(M\). The estimates are interpreted trivially at \(M=0\); in that case the profile must vanish because the only \(\pi\)-periodic solution of \(\rho''+\rho=0\) is zero.

On a sector \([\theta_j,\theta_{j+1}]\), writing \(s=\theta-\theta_j\) and \(h=h_j\), the interpolated profile is
\[
\rho_{\mathcal F}(\theta_j+s)=
\frac{\rho(\theta_j)\sin(h-s)+\rho(\theta_{j+1})\sin s}{\sin h},\quad 0\le s\le h.
\]
The positive sine weights make the extension a continuous nonnegative absolutely homogeneous conic spline, linear on each cone. Angles, curvature variation, and both error norms use the full \(2\pi\)-circle; none uses the half-circle normalization.

## Proof
**1. Local Green identity.** On a cell of length \(h<\pi\), the difference \(e=\rho-\rho_{\mathcal F}\) has zero boundary values and satisfies \((D^2+1)e=\mu\) distributionally in the cell interior. The Dirichlet Green kernel is
\[
G_h(s,t)=-\frac{\sin(\min\{s,t\})\sin(h-\max\{s,t\})}{\sin h},\qquad 0\le s,t\le h.
\]
It has nonpositive sign. The Green representation \(e(s)=\int_{(0,h)}G_h(s,t)\,d\mu(t)\) remains valid for finite measures, because the kernel is continuous and vanishes at the endpoints. Atoms of \(\mu\) on fan rays therefore do not alter cell errors. A direct maximization gives
\[
\max_{s,t\in[0,h]}|G_h(s,t)|=\frac{\sin^2(h/2)}{\sin h}=\frac12\tan(h/2).
\]
The maximum occurs at \(s=t=h/2\).

**2. Exact integrated kernel norm.** For fixed \(t\in(0,h)\), direct integration on either side of \(t\) gives
\[
\int_0^h|G_h(s,t)|\,ds
=\frac{\sin t+\sin(h-t)}{\sin h}-1
=\frac{\cos(t-h/2)}{\cos(h/2)}-1.
\]
It is nonnegative and bounded above by \(\sec(h/2)-1\), with equality at \(t=h/2\). This identity is the sharp local \(M\)-to-\(L^1\) error coefficient, rather than the cruder bound obtained by integrating the maximum of the kernel.

**3. Global inequalities and antipodal factor.** For each cell \(I_j=(\theta_j,\theta_{j+1})\), the first kernel estimate yields
\[
\sup_{I_j}|e|\le\tfrac12\tan(h_j/2)|\mu|(I_j).
\]
Because \(\rho\) and hence \(\mu\) are invariant under translation by \(\pi\), one has \(|\mu|(I_{j+N})=|\mu|(I_j)\) and therefore \(|\mu|(I_j)\le M/2\). Taking the largest cell gives the stated \(L^\infty\) coefficient \(\tfrac14\tan(h_*/2)\). Fubini/Tonelli applied to the total-variation measure and the integrated kernel identity yields
\[
\begin{aligned}
\int_0^{2\pi}|e(\theta)|\,d\theta
&\le\sum_{j=0}^{2N-1}(\sec(h_j/2)-1)|\mu|(I_j)\\
&\le(\sec(h_*/2)-1)M.
\end{aligned}
\]
Both comparisons remain valid when the curvature measure has arbitrary signs or atomic components.

**4. Simultaneous equality by a seminorm.** Choose a cell of length \(h_*\), with midpoint angle \(\alpha\). Let \(v=(-\sin\alpha,\cos\alpha)\) and \(q(x)=|\langle v,x\rangle|\), so that \(\rho(\theta)=|\sin(\theta-\alpha)|\). In the sense of distributions,
\[
\mu=2\delta_\alpha+2\delta_{\alpha+\pi},\qquad M=4.
\]
The two support points lie at the midpoints of antipodal maximum-length cells. On the first cell, the only curvature atom is \(2\delta_\alpha\), and \(e(s)=2G_{h_*}(s,h_*/2)\); the opposite cell has the same error, and all other cells have zero error. Consequently
\[
\|q-q_{\mathcal F}\|_\infty=\tan(h_*/2),\qquad
\|q-q_{\mathcal F}\|_1=4(\sec(h_*/2)-1).
\]
Dividing by \(M=4\) proves simultaneous sharpness, including sharpness within ordinary seminorms.

**5. Optimal fan design.** The first \(N\) gaps satisfy \(\sum_{j=0}^{N-1}h_j=\pi\). Thus \(h_*\ge\pi/N\), with equality exactly when all \(N\) gaps are equal. The functions \(h\mapsto\tan(h/2)\) and \(h\mapsto\sec(h/2)-1\) are strictly increasing on \((0,\pi)\). The exact formulas and equality characterization give the unique optimal equally spaced fan, modulo global rotation. Taylor expansion at zero gives the displayed asymptotics.

## Verification
The local Green identity can be checked by its zero endpoint values and the unit derivative jump at \(s=t\). Its supremum follows from elementary sine-product monotonicity. The integral identity follows by separately integrating the two sine products. The symmetry and sharpness calculations use the full-circle curvature measure, preventing a factor-of-two normalization error.

The optional accompanying \`verify.py\` uses only Python's standard library and checks 372 deterministic finite identities/inequalities and numerical quadratures, including nonuniform meshes and the seminorm extremizer. It is a diagnostic rather than a proof of the infinite universal statements. Reproduce with \`python3 verify.py\`.

## Relationship to prior work
Michael Unser, *Quasi-norms on \(\mathbb R^d\): Characterization and Approximation by Conic Splines* (arXiv:2611.06212v1, publicly submitted November 4, 2026), Proposition 5.2, proves planar curvature-variation bounds on a uniform polar grid and explicitly displays the same Dirichlet Green kernel. The source provides the local \(L^\infty\) kernel estimate; its displayed global \(L^1\) coefficient is \(\tfrac12 h\tan(h/2)\) on a uniform grid, not the exact \(\sec(h/2)-1\). The present result extracts the exact kernel integral, uses antipodal measure symmetry for the global supremum coefficient, extends the inequalities to arbitrary centrally symmetric nonuniform fans, realizes equality with a rank-one seminorm, and determines the exact minimax fan. It does not claim the kernel construction, homogeneity characterization, or rate of convergence as new.

Unser, Fageot, and Ward, *Splines are Universal Solutions of Linear Inverse Problems with Generalized-TV Regularization* (arXiv:1603.01427), prove a representer theorem for generalized-TV inverse problems and nonuniform splines, not these precise node-interpolant worst-case constants. Classical trigonometric-spline work, including I. J. Schoenberg's 1964 article and Koch's 1984 L-spline collocation article, is related background; their historical scope motivates a residual priority risk for the underlying interval Green-operator norm. No claim of exhaustive historical priority verification is made.

## Limitations
The classification concerns the unit circle in two real dimensions, centrally symmetric sampling fans, angular gap strictly below \(\pi\), and finite \((D^2+1)\)-measure variation. It does not cover arbitrary non-antipodal knots, larger gaps, higher-dimensional spherical meshes, or nonlinear adaptive choices of the fan depending on \(q\). The minimax property concerns worst-case normalized errors over the entire stated class, not optimal sampling for a fixed particular function. Classical L-spline theory may independently contain equivalent local Green-operator norm formulas; the scientific comparison is against the explicitly identified modern conic-spline bounds and the accessible historical literature.

## References
1. M. Unser, *Quasi-norms on \(\mathbb R^d\): Characterization and Approximation by Conic Splines*, arXiv:2611.06212v1 (2026-11-04), https://arxiv.org/abs/2611.06212 ; especially Proposition 5.2 and its proof.
2. M. Unser, J. Fageot, J. P. Ward, *Splines are Universal Solutions of Linear Inverse Problems with Generalized-TV Regularization*, arXiv:1603.01427 (2016), https://arxiv.org/abs/1603.01427.
3. I. J. Schoenberg, *On trigonometric spline interpolation*, Journal of Mathematics and Mechanics 13 (1964), 795–825.
4. P. E. Koch, *Collocation by L-Splines at Transformed Gaussian Points*, SIAM Journal on Numerical Analysis 21 (1984), 1107–1114, https://doi.org/10.1137/0721068.
