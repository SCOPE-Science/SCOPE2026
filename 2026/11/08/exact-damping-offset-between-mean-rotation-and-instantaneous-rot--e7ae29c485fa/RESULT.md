# Exact damping offset between mean rotation and instantaneous rotation precision in a Brownian gyrator

## Finding

For the stable two-temperature inertial Brownian gyrator specified below, the friction/damping rate that maximizes the absolute mean angular momentum is **strictly lower** than the rate that maximizes its **one-time stationary signal-to-noise ratio**. The distinction holds for every unequal pair of positive bath temperatures and every strictly stable, nonzero harmonic coupling.

Put \(a=u/k\in(0,1)\), \(g=\Gamma\sqrt{m/k}\), \(H=T_h/T_0\), \(C=T_c/T_0\), \(S=H+C\), and \(J=H-C>0\), where \(T_0>0\) is an arbitrary temperature unit. For the dimensionless instantaneous specific angular momentum \(L=xv_y-yv_x\), define \(F(g)=(\mathbb E L)^2/\operatorname{Var}(L)\). Then

\[
F(g)=\frac{2J^2a^2(1-a^2)g^2}{(4HC+a^2J^2)g^4+a^2[2S^2+(1-a^2)J^2]g^2+S^2a^4}.
\]

This is strictly unimodal on \(g>0\). Its unique maximizer is

\[
g_{\mathrm{precision}}=a\left(\frac{S^2}{4HC+a^2J^2}\right)^{1/4},\qquad g_{\mathrm{mean}}=a.
\]

Equivalently, in physical parameters,

\[
\Gamma_{\mathrm{precision}}=\frac{u}{\sqrt{mk}}\left(\frac{(T_h+T_c)^2}{4T_hT_c+(u/k)^2(T_h-T_c)^2}\right)^{1/4}>\Gamma_{\mathrm{mean}}=\frac{u}{\sqrt{mk}}.
\]

The dimensionless ratio obeys the sharp uniform bounds

\[
1<\frac{\Gamma_{\mathrm{precision}}}{\Gamma_{\mathrm{mean}}}<\frac1{\sqrt a},
\]

and the upper limit is approached as \(T_c/T_h\to0\). The optimal squared signal-to-noise ratio is exactly

\[
\max_{g>0}F(g)=\frac{2J^2(1-a^2)}{2S^2+J^2(1-a^2)+2S\sqrt{4HC+a^2J^2}}.
\]

Here **instantaneous precision** means the mean divided by the standard deviation of \(L\) at a single stationary time. It does **not** mean the precision of a time-integrated current, the asymptotic variance of a time average, or a thermodynamic-uncertainty-relation bound.

## Assumptions and scope

Fix mass \(m>0\), isotropic base stiffness \(k>0\), coupling \(0<u<k\), damping rate \(\Gamma>0\), and thermal bath temperatures \(T_h>T_c>0\). Let \(k_B>0\) be Boltzmann's constant. The planar stochastic dynamics are

\[
d\mathbf r_t=\mathbf v_t\,dt,\qquad
 d\mathbf v_t=\left(-\Gamma\mathbf v_t-\frac1mK\mathbf r_t\right)dt+
\sqrt{\frac{2\Gamma k_B}{m}\operatorname{diag}(T_h,T_c)}\,d\mathbf W_t,
\qquad K=\begin{pmatrix}k&-u\\-u&k\end{pmatrix}.
\]

The driving Brownian components are independent. Since the eigenvalues of \(K\) are \(k-u\) and \(k+u\), both positive, and \(\Gamma>0\), the linear drift is Hurwitz. Thus there is one centered, nondegenerate stationary Gaussian law. The temperature scale \(T_0>0\) defines dimensionless coordinates \(\mathbf r/\sqrt{k_BT_0/k}\), velocities \(\mathbf v/\sqrt{k_BT_0/m}\), and time \(t\sqrt{k/m}\). The ratio \(F\) is unchanged by this scaling; hence the stated physical optimum is independent of \(k_B\) and \(T_0\).

The statement applies to the fixed trap orientation in which \(K\) has the indicated entries, identical isotropic viscous damping along both axes, Gaussian white baths, and stationary single-time observations. Other trap orientations, non-Gaussian baths, ellipsoidal anisotropic drag, finite-window velocity estimation, and time-averaged uncertainty are not covered.

## Proof

**1. Stationary covariance.** Work in the dimensionless system with \(g>0\), \(a\in(0,1)\), and \(H,C>0\). Order the state as \(Z=(x,y,v_x,v_y)\). Its drift and noise covariance matrices are

\[
A=\begin{pmatrix}0&0&1&0\\0&0&0&1\\-1&a&-g&0\\a&-1&0&-g\end{pmatrix},\qquad
Q=\operatorname{diag}(0,0,2gH,2gC).
\]

The stationary covariance \(\Sigma=\mathbb E(ZZ^{\mathsf T})\) solves \(A\Sigma+\Sigma A^{\mathsf T}+Q=0\). Define

\[
V_x=\frac S2+\frac{Jg^2}{2(g^2+a^2)},\quad V_y=\frac S2-\frac{Jg^2}{2(g^2+a^2)},\quad P=\frac{aS}{2(1-a^2)},\quad z=\frac{gaJ}{2(g^2+a^2)}.
\]

Direct substitution into all entries of the Lyapunov equation gives

\[
\Sigma=\begin{pmatrix}
 V_x+aP&P&0&z\\P&V_y+aP&-z&0\\0&-z&V_x&0\\z&0&0&V_y
\end{pmatrix}.
\]

Uniqueness follows from the Hurwitz property. In particular \(\mathbb EL=\Sigma_{x,v_y}-\Sigma_{y,v_x}=2z=gaJ/(g^2+a^2)\). Its absolute value has derivative proportional to \(a^2-g^2\), so its unique maximizer is \(g_{\mathrm{mean}}=a\).

**2. One-time variance.** The stationary law is centered Gaussian. By the Gaussian fourth-moment (Isserlis/Wick) identity and the displayed zero covariances,

\[
\operatorname{Var}(L)=\Sigma_{xx}\Sigma_{v_yv_y}+\Sigma_{yy}\Sigma_{v_xv_x}+2z^2
=2V_xV_y+aP(V_x+V_y)+2z^2.
\]

Since \(V_x+V_y=S\), this simplifies exactly to

\[
\operatorname{Var}(L)=\frac{S^2}{2(1-a^2)}-\frac{J^2g^2(g^2-a^2)}{2(g^2+a^2)^2}.
\]

Combining this with \((\mathbb EL)^2=g^2a^2J^2/(g^2+a^2)^2\) and collecting powers of \(g^2\) proves the formula for \(F\). Every denominator coefficient is positive in the stated domain, because \(4HC+a^2J^2>0\), \(2S^2+(1-a^2)J^2>0\), and \(S^2a^4>0\).

**3. Unique damping optimum.** Write \(\alpha=4HC+a^2J^2\), \(\beta=a^2[2S^2+(1-a^2)J^2]\), and \(\gamma=S^2a^4\). Differentiation gives

\[
F'(g)=\frac{4J^2a^2(1-a^2)g(\gamma-\alpha g^4)}{(\alpha g^4+\beta g^2+\gamma)^2}.
\]

Because \(g>0\), its sign is positive strictly below \(g=(\gamma/\alpha)^{1/4}\) and negative strictly above. Furthermore \(F(g)\to0\) at both endpoints \(g\downarrow0\) and \(g\to\infty\), proving a unique global maximum. Substitution gives the claimed optimal precision and maximal squared signal-to-noise formula.

**4. Strict separation and sharp bound.** The identities \(S^2=4HC+J^2\) and \(\alpha=4HC+a^2J^2\) imply

\[
0<a^2S^2<\alpha<S^2
\]

because \(H,C>0\), \(J>0\), and \(0<a<1\). Taking fourth roots of \(S^2/\alpha\) yields \(1<g_{\mathrm{precision}}/g_{\mathrm{mean}}<1/\sqrt a\). The upper bound is sharp in the limiting cold-bath regime \(C/H\downarrow0\). Returning to physical units proves the theorem.

## Verification

The standalone Python program `verify_gyrator.py` reconstructs the dimensionless covariance, checks all Lyapunov residual entries symbolically, derives the Wick variance, verifies the rational signal-to-noise identity and its derivative, checks the closed-form optimum, and runs independent exact-rational specializations across stable parameters. Execute `python verify_gyrator.py` with SymPy installed. Its recorded successful execution produced `PASS: 219 symbolic and rational checks`. Those checks do not replace the global domain and uniqueness arguments in the proof.

## Relationship to prior work

Martins, Ben-Yedder, Fontana and Rondin, arXiv:2603.18818 (first posted 2026-03-19), give the same inertial gyrator, its full stationary Gaussian covariance in Methods Eq. (7), the mean angular momentum in Eqs. (5)/(11), and the mean-current maximizing damping. Those ingredients are explicitly prior; the new claim is the exact **one-time mean-to-standard-deviation optimization**, its universal strict offset from the mean-current peak, and the sharp all-temperature ratio bound. The Methods and principal text were read in full available HTML, and the PDF was inspected.

Bae, Lee, Kim and Jeong, arXiv:2012.12713 (first posted 2020-12-23), previously derive mean angular momentum and **long-time integrated-current fluctuation** \(D_\theta\) (their Eqs. (14)-(16), Appendix C), and analyze its dependence on trap anisotropy and particle mass. The integral-current fluctuation is not the stationary instantaneous variance used here, and the cited work does not provide this damping optimum. Its PDF sections III, IV and appendices were examined.

Dutta and Saha, arXiv:2606.17554 (first posted 2026-06-16), study an inertial Brownian **ellipsoid** with orientation-dependent anisotropic friction and consider a mean-to-fluctuation performance ratio, including finite-inertia optimum phenomena. This is the closest conceptual precursor and limits any broad novelty claim about finite-inertia precision optima. Its full text was not accessible in this inspection; publicly available abstracts and summaries do not verify whether its spherical reduction includes the exact universal damping formula here. Consequently, publication priority for that particular reduction requires further examination.

## Limitations

This is a self-contained exact statement about one-time stationary angular momentum of a harmonic, linear, Gaussian model. It makes **no** assertion about the signal-to-noise of time averages, the optimal statistical precision per unit recording time, experimentally sampled finite differences, or thermodynamic uncertainty bounds. The strict optimum comparison excludes equilibrium equal temperatures and zero potential coupling, where the mean vanishes and the SNR objective becomes identically zero. The singular limits \(a\downarrow0\), \(a\uparrow1\), and \(T_c\downarrow0\) are limiting statements, not included boundary points. Wider publication priority remains subject to the unresolved ellipsoid-paper comparison; the self-contained algebraic proof does not itself certify literature novelty.

## References

1. T. T. Martins, I. Ben-Yedder, A. Fontana, and L. Rondin, *Role of inertia on the performance of Brownian gyrators*, arXiv:2603.18818 (first publicly posted 2026-03-19). https://arxiv.org/abs/2603.18818
2. Y. Bae, S. Lee, J. Kim, and H. Jeong, *Inertial effects on the Brownian gyrator*, arXiv:2012.12713 (first publicly posted 2020-12-23); *Physical Review E* 103, 032148 (2021). https://arxiv.org/abs/2012.12713
3. S. Dutta and A. Saha, *Brownian gyration of an inertial ellipsoid*, arXiv:2606.17554 (first publicly posted 2026-06-16). https://arxiv.org/abs/2606.17554
