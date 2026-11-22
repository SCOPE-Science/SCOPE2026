# Reentrant equilibrium-like covariance in a switching stable–inverted harmonic trap

## Finding
For a thermal Brownian particle whose harmonic stiffness switches between positive confinement and **repulsion**, the *entire stationary position covariance* is completely monotone in a sharply determined **bounded interval** of the rate of escape from the repulsive phase, and fails to be completely monotone on both sides of that interval. At its two endpoints the full covariance becomes exactly that of an equilibrium Ornstein–Uhlenbeck particle, even though the stationary position distribution remains heavy-tailed. Both endpoints can have **infinite fourth positional moment**, despite their finite exactly exponential covariance.

Precisely, fix confining strength \(k>0\), repulsive strength \(h>0\), thermal diffusivity \(D>0\), and confinement-to-repulsion switching rate \(\beta>0\). Let the repulsion-to-confinement rate \(\alpha>0\) vary. The stationary diffusion obeys
\[
 dX_t=-k_{S_t}X_t\,dt+\sqrt{2D}\,dW_t,\qquad k_+=k,\quad k_-=-h,
\]
where \(S_t\) is independent of the Brownian noise, jumps \(+\to-\) at rate \(\beta\), and jumps \(-\to+\) at rate \(\alpha\). We restrict throughout to the **finite stationary variance** domain
\[
 \alpha>L:=\frac{h(\beta+2k)}{k}.
\]
Write \(C(t)=\mathbb E[X_tX_0]\) for \(t\ge0\). For \(k>h\) put
\[
 \beta_c=\frac{(k-h)^2}{4(k+h)},\qquad
 \alpha_\pm=k+h-\beta\pm\sqrt{(k-h)^2-4\beta(k+h)}.
\]
If \(k>h\) and \(0<\beta<\beta_c\), then \(L<\alpha_-<\alpha_+\), and:

- \(C\) is completely monotone on \([0,\infty)\) exactly for \(\alpha\in[\alpha_-,\alpha_+]\).
- For \(\alpha\in(\alpha_-,\alpha_+)\), the covariance is a **strictly positive mixture of two distinct exponentials**; outside the closed interval its fast exponential has a **strictly negative** coefficient, although \(C(t)>0\) for every \(t\ge0\).
- At each endpoint the fast mode cancels *exactly* and
\[
 C(t)=\frac{2D}{\alpha+\beta}\exp\!\left(-\frac{\alpha+\beta}{2}t\right),\qquad t\ge0.
\]
The two endpoints have **different** effective relaxation rates \((\alpha_-+\beta)/2\) and \((\alpha_++\beta)/2\).

If \(k>h\) and \(\beta=\beta_c\), there is exactly one cancellation point \(\alpha=k+h-\beta\), with no open interval of completely monotone covariance. If \(k\le h\), or \(k>h\) and \(\beta>\beta_c\), the covariance is **never completely monotone** at any finite-variance-admissible \(\alpha\). Thus this is an exhaustive phase diagram, including its boundary.

An exact witness with an especially sharp distributional contrast is \(k=2\), \(h=1\), \(\beta=1/20\), \(D=1\). Its two cancellation rates are
\[
 \alpha_\pm=\frac{59}{20}\pm\sqrt{\frac25},\qquad
 \rho_\pm=\frac{3\pm\sqrt{2/5}}{2}.
\]
At each endpoint \(C(t)=\rho_\pm^{-1}e^{-\rho_\pm t}\). Yet **both stationary laws have infinite fourth moment**, because their known algebraic-tail moment cutoffs \(p_\pm=117/40\pm\sqrt{2/5}\) lie strictly between \(2\) and \(4\). The two measured OU-like covariances are not claims of Gaussian position distributions, Gaussian paths, equilibrium dynamics, or finite fourth-order statistics.

## Assumptions and scope
All four basic parameters \(k,h,D,\beta\) and the variable \(\alpha\) are strictly positive and finite. The two-state chain is stationary, irreducible, and exogenous. The diffusion has constant thermal noise in both switching states. A unique stationary causal solution exists when the mean restoring coefficient is positive, \(\alpha k>\beta h\); the theorem imposes the stronger condition \(\alpha k>\beta h+2kh\), which is necessary and sufficient for its stationary second moment to be finite. All complete-monotonicity derivatives are right derivatives at zero. The statement concerns one particle's *stationary two-time covariance*; neither a complete Gaussian process law nor an entropy-production identity is asserted.

## Proof
**Existence and finite variance.** Let \(q=\alpha+\beta\), \(K=\operatorname{diag}(k,-h)\), \(\pi=(\alpha,\beta)^\mathsf T/q\), and
\[
 Q=\begin{pmatrix}-\beta&\alpha\\\beta&-\alpha\end{pmatrix}.
\]
The mean Lyapunov exponent for the homogeneous linear dynamics is \((\alpha k-\beta h)/q>0\), giving the stationary two-sided stochastic convolution. Its conditional variance is finite almost surely and the stationary law is unique by pathwise contraction under common switching and Brownian noise. The state-resolved stationary second-moment vector \(m=(\mathbb E[X_0^2\mathbf1_{\{S_0=+\}}],\mathbb E[X_0^2\mathbf1_{\{S_0=-\}}])^\mathsf T\) satisfies the exact Itô-generator equation
\[
 (2K-Q)m=2D\pi.
\]
The Metzler matrix \(Q-2K\) has negative spectral abscissa precisely when \(\alpha k>\beta h+2kh\). This is also the sharp second-moment integrability condition: positivity and irreducibility make the stationary Gaussian conditional-variance integral finite in mean exactly when the corresponding positive matrix semigroup is integrable. On this domain put \(H=\alpha k-\beta h-2kh>0\). Direct inversion gives
\[
 m_+=\frac{\alpha D(q-2h)}{qH}>0,\qquad
 m_-=\frac{\beta D(q+2k)}{qH}>0,
\]
\[
 V:=C(0)=\frac{D[q^2+2\beta k-2\alpha h]}{qH}>0.
\]
Stationarity of \(X^2\) implies \(\mathbb E[k_{S_0}X_0^2]=D\).

**Exact covariance and spectral coefficients.** Let \(M=Q-K\). A conditional Markov-semigroup argument yields the *independently checkable* identity
\[
 C(t)=\mathbf1^\mathsf T e^{Mt}m,\qquad \mathbf1=(1,1)^\mathsf T.
\]
The two decay rates \(0<\lambda_s<\lambda_f\) are
\[
 \lambda_{s,f}=\frac{q+k-h\mp\sqrt{(k+\beta-\alpha+h)^2+4\alpha\beta}}2.
\]
They are positive because \(\operatorname{tr}M=-(q+k-h)<0\) and \(\det M=\alpha k-\beta h-kh>0\), both consequences of \(H>0\). They are distinct since \(\alpha\beta>0\). Hence
\[
 C(t)=A_s e^{-\lambda_s t}+A_f e^{-\lambda_f t},\quad
 A_f=\frac{D-\lambda_sV}{\lambda_f-\lambda_s},\quad A_s=V-A_f.
\]
The strictly positive off-diagonal entries of \(M\) and \(m,\mathbf1>0\) imply \(A_s>0\) by the Perron–Frobenius spectral projection. The identity \(C'(0+)=-D\) fixes the second spectral coefficient; positivity of \(e^{Mt}\) also proves \(C(t)>0\).

**Sharp completely monotone classification.** Differentiating the exact matrix semigroup at zero and simplifying gives the *polynomial identity*
\[
 VC''(0+)-D^2=-\frac{\alpha\beta D^2(k+h)^2}{q^2H^2}\,F(\alpha),
\]
where
\[
 F(\alpha)=q^2-2(\alpha-\beta)(k+h)+4kh.
\]
On the other hand, the two-exponential representation gives
\[
 VC''(0+)-D^2=A_sA_f(\lambda_f-\lambda_s)^2.
\]
Since \(A_s>0\), the sign of \(A_f\) is the opposite of that of \(F\). A two-exponential covariance with positive slow coefficient is completely monotone **if and only if** its fast coefficient is nonnegative. Necessity follows because, when \(A_f<0\), the quantities \((-1)^nC^{(n)}(0+)=A_s\lambda_s^n+A_f\lambda_f^n\) become negative for every sufficiently large integer \(n\).

As a quadratic polynomial in \(\alpha\), \(F\) has vertex \(\alpha_0=k+h-\beta\), with
\[
 F(\alpha_0)=4\beta(k+h)-(k-h)^2,
 \quad F(L)=\frac{\beta(\beta+2k)(k+h)^2}{k^2}>0.
\]
If \(k\le h\), then \(\alpha_0\le L\), so \(F\) increases and stays positive on the admissible half-line. If \(k>h\), the vertex lies strictly above \(L\) whenever \(\beta\le\beta_c\): indeed \(\alpha_0-L=[k(k-h)-\beta(k+h)]/k>0\). For \(\beta<\beta_c\), the vertex value is negative; its two zeros \(\alpha_\pm\) therefore both lie strictly beyond \(L\), yielding the stated positive-mixture interval. At \(\beta=\beta_c\) its unique zero is the vertex. Above \(\beta_c\), \(F>0\) everywhere. This proves the complete parameter classification.

**Exact OU-like cancellation and heavy-tailed witness.** At \(F(\alpha)=0\), the variance formula simplifies to \(V=2D/q\). Thus \(A_f=0\) and the surviving exponent \(\lambda_s=D/V=q/2\), proving the all-lag identity. Equivalently, writing \(\rho=q/2\), all cancellation solutions can be parametrized as
\[
 \alpha=\frac{(\rho+h)(\rho+k)}{k+h},\qquad
 \beta=\frac{(k-\rho)(\rho-h)}{k+h},\qquad h<\rho<k.
\]
This parametrization also gives \(H=(\rho-h)(\rho+k)>0\), so the two candidate solutions never fall outside the second-moment domain. The stationary coordinate under positive/negative switching is a known nondegenerate Gaussian scale mixture with beta-prime variance law, whose absolute moment of order \(p>0\) is finite exactly when \(p<\alpha/h-\beta/k\) [de Saporta–Yao; the evaluated two-state beta-prime representation in the cited exact-variance study]. For the stated exact rational/radical witness this exponent equals \(117/40\pm\sqrt{2/5}\in(2,4)\), hence its second moments are finite but fourth moments infinite at both exact covariance-cancellation points. No fourth-moment formula is needed to establish the main spectral classification.

## Verification
The standalone `CHECK.py` reconstructs all symbolic moment, spectral, discriminant, and integrability-boundary identities directly with SymPy. Independently it solves the state-resolved second-moment linear system and evaluates the matrix exponential with SciPy on 210 diverse physical parameter sets, six lags each, for 2,540 total assertions/identity checks. It also tests the exact two-root finite-variance witness, its full exponential covariance at several lags, and the fourth-moment cutoffs. Run with Python 3, NumPy, SciPy, and SymPy installed: `python CHECK.py`. Finite tests corroborate; the all-parameter proof is the algebra and positivity argument above.

## Relationship to prior work
The random-switching harmonic model and its conditional Gaussian stationary laws are established. Biroli, Kulkarni, Majumdar, and Schehr (2023) analyze two **positive** stiffnesses with spatial correlations and stationary joint distributions; de Saporta and Yao (2005) establish heavy-tail criteria for positive/negative Markov-modulated drifts. The previously evaluated **two-component beta-prime mixture** and its moment threshold in the stable–inverted model are prior results, not claimed here. Huang and colleagues (2014) supply a general linear matrix-covariance method. Existing exact classifications of pure OU-like covariance for **positive** stiffnesses and of spectral-sign cancellation for **on/off** traps provide close algebraic predecessors, and their formulas were inspected. Neither theorem's assumptions include *negative stiffness*, and the on/off model has no heavy-tailed stationary fourth-moment divergence. The new assertion is the **complete finite-variance-domain zero/one/two cancellation diagram under repulsion** together with a two-solution example in which the stationary covariance matches a Gaussian equilibrium spectrum while the fourth moment diverges. This is qualified novelty, not an asserted uniqueness theorem across all literature: analytically extending earlier positive-stiffness formulas is a significant residual priority risk.

## Limitations
The result concerns only scalar overdamped harmonic drift, constant positive thermal diffusivity, and independent two-state exponential switching. It does not assert Gaussian finite-dimensional distributions, true thermal equilibrium, closeness in path-law distance, causal response equality, or finite-sample identifiability. The fourth-moment statement is an exact witness, not universal across all cancellation parameters. The stable–inverted heavy-tail exponent is established in prior literature rather than independently novel. The general covariance machinery and a positive-stiffness cancellation manifold are published, creating substantive implicit-coverage risk requiring independent scientific priority review; none has yet been performed.

## References
1. M. Biroli, M. Kulkarni, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570 (first public 2023-12-05), https://arxiv.org/abs/2312.02570 .
2. B. de Saporta, J.-F. Yao, *Tail of a linear diffusion with Markov switching*, arXiv:math/0503527 (2005), https://arxiv.org/abs/math/0503527 .
3. G. Huang, H. M. Jansen, M. Mandjes, P. Spreij, K. De Turck, *Markov-modulated Ornstein–Uhlenbeck processes*, arXiv:1412.7952 (2014), https://arxiv.org/abs/1412.7952 .
4. I. Santra, S. Das, S. K. Nath, *Brownian motion under intermittent harmonic potentials*, arXiv:2104.00609 (2021), https://arxiv.org/abs/2104.00609 .
5. *Exact beta-prime thermal variance and tail amplitude in a switching stable–inverted harmonic trap*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-beta-prime-thermal-variance-and-tail-amplitude-in-a-switch--93bb1b2e24d1 .
6. *A complete equilibrium-covariance camouflage manifold for a switching harmonic trap*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-complete-equilibrium-covariance-camouflage-manifold-for-a-swit--8f817ade8710 .
7. *Exact spectral cancellation and Gaussian-covariance camouflage in a two-rate intermittent harmonic trap*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-spectral-cancellation-and-gaussian-covariance-camouflage-i--d57d3a9e09b2 .
8. *A strictly signed fluctuation–response defect in a randomly switching harmonic trap*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-strictly-signed-fluctuation-response-defect-in-a-randomly-swit--91e29b772bb6 .
