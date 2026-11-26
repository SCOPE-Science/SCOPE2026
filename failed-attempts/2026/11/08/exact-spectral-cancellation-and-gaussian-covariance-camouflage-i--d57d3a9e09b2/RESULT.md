# Exact spectral cancellation and Gaussian-covariance camouflage in a two-rate intermittent harmonic trap

## Finding

**Theorem (stationary on/off harmonic diffusion).** Fix \(\alpha,\beta,\kappa,D>0\). Let \(S_t\in\{0,1\}\) be a continuous-time Markov chain, independently of a two-sided Brownian motion \(W\), switching from the unconfined state \(0\) to confined state \(1\) at rate \(\alpha\), and from \(1\) to \(0\) at rate \(\beta\). Let the stationary particle satisfy
\[
 dX_t=-\kappa S_tX_t\,dt+\sqrt{2D}\,dW_t.
\]
Set \(T=\alpha+\beta\), \(\lambda_\pm=(\kappa+T\pm\sqrt{(\kappa+T)^2-4\alpha\kappa})/2\), and \(V=\mathbb E X_t^2\). Then \(0<\lambda_-<\kappa<\lambda_+\), and the entire stationary covariance \(C(t)=\mathbb E[X_0X_t]\), \(t\ge0\), is
\[
 C(t)=A_-e^{-\lambda_-t}+A_+e^{-\lambda_+t},\qquad
 A_+=\frac{D-\lambda_-V}{\lambda_+-\lambda_-},\quad A_-=V-A_+>0,
\]
with \(V=D[T^2+2\beta\kappa]/(\alpha\kappa T)\). Write \(H=T^2+2\kappa(\beta-\alpha)\).

1. **Spectral-sign phase:** \(\operatorname{sgn}(A_+)=-\operatorname{sgn}(H)\). The covariance is completely monotone on \([0,\infty)\) exactly when \(H\le0\), which is possible precisely for \(\alpha>\beta\) and \(\kappa\ge T^2/[2(\alpha-\beta)]\). For \(H>0\), its fast spectral coefficient is strictly negative and sufficiently high right derivatives violate complete monotonicity.
2. **Curvature phase:** If \(\alpha<\beta\), then \(C''(0+)<0\) and \(C''(t)\) changes sign exactly once, becoming positive for all larger lags. If \(\alpha=\beta\), then \(C''(0+)=0\) and \(C''(t)>0\) for every \(t>0\). If \(\alpha>\beta\), then \(C''(t)>0\) for every \(t\ge0\).
3. **Exact second-order camouflage:** A single-exponential stationary covariance exists for finite strictly positive switching rates **if and only if** \(\alpha>\beta\) and
\[
 \kappa=\kappa_*=\frac{T^2}{2(\alpha-\beta)}.
\]
At this unique stiffness, \(C(t)=(2D/T)e^{-Tt/2}\) for all \(t\ge0\), exactly the covariance (and the same diffusivity) of an equilibrium Ornstein–Uhlenbeck particle with relaxation \(T/2\). Nevertheless the stationary distribution is strictly non-Gaussian: its fourth cumulant is
\[
 \kappa_4(X)=\mathbb E[X^4]-3V^2=\frac{36D^2\beta}{\alpha T^2}>0,
\]
and its conventional standardized excess kurtosis is \(\kappa_4(X)/V^2=9\beta/\alpha\).

The results concern the stationary position marginal and covariance, not equality of full process laws. In fact, the mismatch of fourth moments rules out equality with the equilibrium OU process.

## Assumptions and scope

The rates \(\alpha,\beta\), on-state relaxation \(\kappa\), and thermal diffusivity \(D\) are strictly positive and finite. Switches do not instantaneously alter position. The state chain is independent of the Brownian noise, with invariant probabilities \(\pi_0=\beta/T\) and \(\pi_1=\alpha/T\). The stationary solution exists uniquely and has moments of all finite polynomial orders. The theorem does not include the singular boundaries \(\alpha=0\), \(\beta=0\), or \(\kappa=0\).

## Proof

**Stationarity and moments.** For a two-sided stationary chain, the stochastic convolution
\[
 X_t=\sqrt{2D}\int_{-\infty}^t\exp\!\left(-\kappa\int_s^t S_u\,du\right)dW_s
\]
converges. Indeed, the on-state occupation of an irreducible two-state chain grows linearly almost surely; the finite-state killed-generator \(Q-2n\kappa\operatorname{diag}(0,1)\) has strictly negative spectral abscissa for every integer \(n\ge1\), so the Gaussian conditional variance has finite positive integer moments. Contractivity of two solutions driven by the same chain and noise gives uniqueness of the stationary law.

Let \(M_i=\mathbb E[X^2\mathbf 1_{\{S=i\}}]\). Applying the generator to \(X^2\mathbf 1_{\{S=i\}}\) yields
\[
 0=2D\pi_0-\alpha M_0+\beta M_1,\qquad
 0=2D\pi_1+\alpha M_0-(\beta+2\kappa)M_1.
\]
Consequently \(M_1=D/\kappa\), \(M_0=D\beta/(\alpha\kappa)+2D\beta/(\alpha T)\), and
\[
 V=M_0+M_1=\frac{D(T^2+2\beta\kappa)}{\alpha\kappa T}.
\]

**Two-time generator and spectrum.** For \(t\ge0\) define \(z_i(t)=\mathbb E[X_tX_0\mathbf 1_{\{S_t=i\}}]\). Independence and the Markov generator give the exact linear system
\[
 \binom{z_0'}{z_1'}=
 \begin{pmatrix}-\alpha&\beta\\\alpha&-\beta-\kappa\end{pmatrix}
 \binom{z_0}{z_1},\qquad (z_0(0),z_1(0))=(M_0,M_1).
\]
The eigenvalues are \(-\lambda_\pm\), each simple and strictly negative. Summing components gives \(C(0)=V\) and \(C'(0+)=-\kappa M_1=-D\), whence the displayed spectral coefficients. The characteristic polynomial \(p(z)=z^2-(\kappa+T)z+\alpha\kappa\) satisfies \(p(0)>0\) and \(p(\kappa)=-\beta\kappa<0\), proving \(0<\lambda_-<\kappa<\lambda_+\). Since \(V>D/\kappa\), the ratio \(s=D/V\) satisfies \(s<\kappa<\lambda_+\), giving \(A_->0\).

A direct exact factorization yields
\[
 p(s)=\frac{\alpha\beta\kappa^2[T^2+2\kappa(\beta-\alpha)]}{(T^2+2\beta\kappa)^2}.
\]
Because \(p(s)=(s-\lambda_-)(s-\lambda_+)\) and \(s-\lambda_+<0\), the sign of \(A_+\) is minus the sign of \(H\). If \(A_+\ge0\), both weights are nonnegative and \((-1)^n C^{(n)}(t)\ge0\) for all integers \(n\ge0\) and \(t\ge0\). If \(A_+<0\), then \((-1)^n C^{(n)}(0+)=A_-\lambda_-^n+A_+\lambda_+^n<0\) for all sufficiently large \(n\), proving the converse.

**Curvature.** Reusing the matrix at lag zero gives
\[
 C''(0+)=D\kappa\frac{\alpha-\beta}{T}.
\]
If \(\alpha<\beta\), the fast coefficient is negative and \(C''(0+)<0\), while its positive slow term dominates as \(t\to\infty\). The ratio of its two exponential terms is strictly monotone, so the unique inflection lag is
\[
 t_{\rm inf}=\frac{1}{\lambda_+-\lambda_-}\log\!\left(\frac{-A_+\lambda_+^2}{A_-\lambda_-^2}\right)>0.
\]
If \(\alpha=\beta\), the initial curvature is zero and the rapidly decaying negative contribution thereafter has strictly smaller magnitude. If \(\alpha>\beta\), the initial curvature is positive and stays so: either both weights are nonnegative, or the negative fast contribution only decreases in relative magnitude as time increases.

**Camouflage and its limit.** The two distinct exponentials reduce to one exactly when \(A_+=0\), equivalently \(H=0\). This has a finite positive solution for \(\kappa\) exactly when \(\alpha>\beta\). Substitution gives \(\lambda_-=T/2\) and \(V=2D/T\), yielding the covariance equality. For \(N_i=\mathbb E[X^4\mathbf1_{\{S=i\}}]\), the generator yields
\[
 0=12DM_0-\alpha N_0+\beta N_1,\qquad
 0=12DM_1+\alpha N_0-(\beta+4\kappa)N_1.
\]
It follows that \(N_1=3DV/\kappa\) and that the *general* fourth cumulant is
\[
 \kappa_4(X)=\frac{6D^2\beta[T^2+2\kappa(2\alpha+\beta)]}{\alpha^2\kappa T^2}>0.
\]
Substituting \(\kappa=\kappa_*\) gives \(36D^2\beta/(\alpha T^2)\). A centered Gaussian with covariance \(C\) has fourth cumulant zero, so covariance equality is not equality in distribution.

## Verification

The proof is analytical. A standalone standard-library Python checker, `checker.py`, reconstructs the two-state generator independently of the exponential-residue formula, tests stationary second/fourth moment equations with exact rational arithmetic, verifies a sixth-order derivative recurrence, compares matrix-exponential and spectral representations at five nonnegative lags, and tests the exact cancellation and excess-kurtosis formulas on admissible rational boundaries. It reports 1,050 deterministic parameter cases passed. These finite tests supplement, not replace, the quantified proof.

## Relationship to prior work

Frydel's 2024 treatment of fluctuating on/off harmonic traps considers equal switching rates and determines stationary spatial laws and thermodynamic quantities; the present classification concerns unequal rates and the sign of temporal spectral weights, global curvature, and exact Gaussian-covariance matching. Huang, Jansen, Mandjes, Spreij, and De Turck (2014) give general Markov-modulated OU moment recursions and a matrix expression for autocovariances, a strong methodological precursor: the present model is a specialization of that framework. Their general matrix expressions do not themselves provide the explicit parameter-uniform spectral-sign phase, unique cancellation condition, or its positive standardized fourth cumulant. The general framework nonetheless creates residual priority risk for the interpretation of these formulas as implicit consequences. Guyon, Iovleff, and Yao (2004) establish broad stationary-switching diffusion facts, including conditional normality, rather than this covariance-cancellation classification.

## Limitations

No claim is made about finite-sample detectability or robustness of inference at the cancellation surface, equality of full process laws, or generalized non-Markov switching. The model has one-dimensional position and constant diffusion with an independent two-state Markov environment. The exact general covariance and moment methods have published predecessors, so originality attaches only to the parameter-uniform structural classification, not the matrix-exponential method or the on/off model. Independent validation remains to be performed.

## References

1. D. Frydel, "Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap," arXiv:2407.12213, first public version 2024-07-16, https://arxiv.org/abs/2407.12213 .
2. G. Huang, H. M. Jansen, M. Mandjes, P. Spreij, K. De Turck, "Markov-modulated Ornstein-Uhlenbeck processes," arXiv:1412.7952, first public version 2014-12-26, https://arxiv.org/abs/1412.7952 .
3. X. Guyon, S. Iovleff, J.-F. Yao, "Linear diffusion with stationary switching regime," ESAIM: Probability and Statistics 8 (2004), 25–35, https://doi.org/10.1051/ps:2003017 .
