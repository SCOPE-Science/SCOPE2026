# Sharp identifiability and a rotation-blindness boundary for clonal Ornstein–Uhlenbeck covariance

## Finding

**Theorem (complete rotational identifiability dichotomy).** Fix an integer \(d\geq 2\) and a real symmetric positive-definite \(d\times d\) matrix \(S\). For every real skew-symmetric matrix \(\Omega\), consider a stationary Ornstein–Uhlenbeck diffusion with drift matrix \(A=S+\Omega\), diffusion matrix \(S\), and a pure-birth binary branching population with splitting rate one. Let \(Z(t)\) be the sum of all particle states, and let \(K_{\Omega}(t)=e^{-t}\operatorname{Cov}(Z(t))\) for \(t\geq0\), with the root sampled from the stationary law \(\mathcal N(0,I_d)\). Then

\[
K_{\Omega}(t)=I_d+2\int_0^t e^u e^{-(S+\Omega)u}e^{-(S-\Omega)u}\,du.
\]

The full covariance curve \(\Omega\mapsto(K_{\Omega}(t))_{t\geq0}\) is injective on real skew matrices **if and only if** \(S\) has pairwise distinct eigenvalues. In the simple-spectrum case, the derivatives of orders two and three at zero already determine both the damping matrix \(S\) and the complete antisymmetric drift \(\Omega\) by explicit formulas:

\[
S=\tfrac12I_d-\tfrac14K_{\Omega}''(0),\qquad
T=\tfrac12K_{\Omega}'''(0)-\bigl(\tfrac12K_{\Omega}''(0)\bigr)^2=2[\Omega,S],
\]
\[
(V^T\Omega V)_{ij}=\frac{(V^TTV)_{ij}}{2(s_j-s_i)}\quad(i\ne j),
\]

where \(V^TSV=\operatorname{diag}(s_1,\ldots,s_d)\) with distinct positive \(s_i\); the diagonal of \(V^T\Omega V\) is zero. No derivatives of order at most two detect \(\Omega\).

For two skew drifts \(\Omega,\widetilde\Omega\) with the same \(S\) and spectral gap \(\delta=\min_{i<j}|s_i-s_j|\), the optimal uniform Frobenius stability constant is

\[
\|\Omega-\widetilde\Omega\|_F
\leq \frac{\|K_{\Omega}'''(0)-K_{\widetilde\Omega}'''(0)\|_F}{4\delta}.
\]

This constant is attained by a perturbation supported in a closest eigenvalue pair. If \(S\) has a repeated eigenvalue, some \(\Omega\ne0\) is wholly invisible: \(K_{\Omega}(t)=K_0(t)\) for all \(t\geq0\), although its stationary entropy-production rate is strictly positive. The criterion extends, by stationary covariance whitening, to any multivariate Ornstein–Uhlenbeck model with positive-definite stationary covariance and diffusion: the relevant simple spectrum is that of the diffusion matrix in stationary-whitened coordinates.

## Assumptions and scope

All random variables are defined on the full real state space \(\mathbb R^d\). The single-particle stochastic differential equation is

\[
dX_t=-(S+\Omega)X_t\,dt+\sqrt{2S}\,dW_t,
\]

where \(S=S^T\succ0\), \(\Omega^T=-\Omega\), and \(W\) is standard \(d\)-dimensional Brownian motion. The positive-definite square root \(\sqrt{2S}\) is meant. The root state is independent of the population tree and sampled from \(\mathcal N(0,I_d)\). Each particle independently splits into exactly two daughters at exponential rate one. Both daughters inherit the mother’s instantaneous position and subsequently evolve with independent Brownian noises and independent branching clocks; there is no removal, immigration or resetting. Write \(N_t\) for the population size, \(Z(t)=\sum_{j=1}^{N_t}X_j(t)\), and \(\mathbb EN_t=e^t\). All covariances are unconditional across independent stationary-root population realizations, at the same population age \(t\). Because the stationary mean is zero, this covariance equals the intrinsic (population-count-conditioned, then averaged) covariance used in the foundational fluctuation-dissipation relation. The observable is the **entire matrix of population-sum covariances**, not merely scalar trace or a fixed projection.

The time origin and branching rate are known. The canonical theorem uses unit stationary covariance, while the general-coordinate stationary covariance is recovered as the value of the observation at zero age. The identifiability assertion concerns exact functional data and exact right derivatives at \(t=0\), not statistical consistency with finitely many clone measurements. No prior knowledge of \(S\) is required to recover it from the second derivative; the simple-spectrum condition is imposed on its recovered value. More generally, for drift \(B\), diffusion matrix \(D\succ0\), and stationary covariance \(\Sigma\succ0\), the transform \(X=\Sigma^{-1/2}Y\) produces the displayed canonical model with \(S=\Sigma^{-1/2}D\Sigma^{-1/2}\). The original covariance observable identifies \(\Sigma=K_Y(0)\) and \(D=\tfrac12\Sigma-\tfrac14K_Y''(0)\); whitening then yields the same rotational-identifiability criterion. This is an exact change of coordinates, not an extra assumption on physical diffusion.

## Proof

**Stationarity and pair decomposition.** Because \(A=S+\Omega\) has positive-definite symmetric part \(S\), it is exponentially stable. The stationary covariance \(\Sigma\) solves \(A\Sigma+\Sigma A^T=2S\); \(\Sigma=I_d\) solves it and is unique. The centered stationary Gaussian density is therefore \(p(x)=(2\pi)^{-d/2}e^{-\|x\|^2/2}\). For a single ancestor state \(x\), the conditional mean after \(u\) time is \(e^{-Au}x\). Thus two independently evolving descendants separated \(u\) time units ago have conditional product of means \(e^{-Au}xx^Te^{-A^Tu}\). Averaging the stationary ancestor gives \(H(u)=e^{-Au}e^{-A^Tu}\).

Every ordered pair of distinct extant particles has one most recent splitting event. The expected number of potential splitters at time \(t-u\) is \(e^{t-u}\). Each split creates two ordered daughter-subtree pair orientations, with independent expected descendant counts \(e^u\) and \(e^u\). Hence the expected ordered off-diagonal pair sum is \(2e^t\int_0^t e^u H(u)\,du\). The diagonal particle terms contribute exactly \(e^t I_d\) by stationarity. Since \(\mathbb EZ(t)=0\), division by \(\mathbb EN_t=e^t\) establishes the displayed formula for \(K_{\Omega}\). All expectations are finite at every finite \(t\) by the Yule process's finite second moment and Gaussian state moments.

**Short-time jet and recovery.** Differentiate the exact formula, obtaining \(K'=2e^tH\). With \(H(0)=I_d\), \(H'(0)=-(A+A^T)=-2S\), direct product differentiation yields

\[
H''(0)=A^2+2AA^T+(A^T)^2=4S^2+2(\Omega S-S\Omega).
\]

Consequently

\[
K_{\Omega}'(0)=2I_d,\quad
K_{\Omega}''(0)=2(I_d-2S),\quad
K_{\Omega}'''(0)=2\bigl((I_d-2S)^2+2[\Omega,S]\bigr).
\]

The first two nontrivial jets have no rotational information, whereas the third gives the commutator \([\Omega,S]=\Omega S-S\Omega\). The commutator is symmetric, and orthogonal diagonalization of \(S\) gives \([V^T\Omega V,\operatorname{diag}(s_i)]_{ij}=(s_j-s_i)(V^T\Omega V)_{ij}\). If the eigenvalues are simple, every off-diagonal skew entry is uniquely recovered, proving injectivity from the third jet. The derivation also verifies the reconstruction formula for \(S\), which need not have been known beforehand.

**Sharp stability and degeneracy.** For any skew \(\Delta\Omega\), the third-jet difference at a fixed \(S\) is \(4[\Delta\Omega,S]\). In the eigenbasis,

\[
\|[\Delta\Omega,S]\|_F^2
=\sum_{i,j}(s_j-s_i)^2|(V^T\Delta\Omega V)_{ij}|^2
\geq\delta^2\|\Delta\Omega\|_F^2.
\]

Equality is achieved if \(\Delta\Omega\) has only the two opposite nonzero entries associated with a closest eigenvalue pair. This proves the sharp constant. If \(S\) has a repeated eigenvalue, choose a nonzero skew matrix supported on its multidimensional eigenspace. It commutes with \(S\), so

\[
H(u)=e^{-Su}e^{-\Omega u}e^{-Su}e^{\Omega u}=e^{-2Su},
\]

which is independent of \(\Omega\) at **every** time, not merely to a finite Taylor order. Thus repeated spectrum prevents global injectivity. These two cases prove the if-and-only-if statement. For a general stable Ornstein–Uhlenbeck process with stationary \(\Sigma\succ0\) and \(D\succ0\), the stationary Lyapunov equation yields \(B\Sigma+\Sigma B^T=2D\). Thus \(\Sigma^{-1/2}B\Sigma^{1/2}=S+\Omega\), with \(S=\Sigma^{-1/2}D\Sigma^{-1/2}\). The branching covariance transforms by congruence. The observed initial covariance and its second derivative determine \(\Sigma\) and \(D\), respectively, before the already-proved normal-form inverse is applied. This establishes the equivalent general-OU formulation.

**Physical inequivalence of the blind family.** The steady-state probability current is \(j(x)=-\Omega x\,p(x)\). With diffusion matrix \(S\), the standard quadratic current definition gives entropy production

\[
\sigma_{\mathrm{EP}}=\int_{\mathbb R^d}\frac{j(x)^TS^{-1}j(x)}{p(x)}\,dx
=\operatorname{tr}(\Omega^TS^{-1}\Omega).
\]

It is positive whenever \(\Omega\ne0\). In two dimensions take \(S=sI_2\) with \(s>0\) and \(\Omega=\begin{pmatrix}0&-\omega\\\omega&0\end{pmatrix}\), \(\omega\ne0\). The covariance curve agrees identically with reversible \(\Omega=0\), while \(\sigma_{\mathrm{EP}}=2\omega^2/s>0\). Hence the blindness concerns genuinely different irreversible stationary processes.

## Verification

The accompanying standalone Python-standard-library script `verify.py` computes rational matrix-exponential Taylor coefficients, integrates the exact power series, checks all three covariance derivatives, reconstructs skew drift for diagonal simple-spectrum examples in dimensions two through five, and checks two non-diagonal damping matrices. It confirms the commuting-degeneracy identities to order twelve, positive dissipation for the blind rotations, and attainment of the stability constant in dimensions two through seven. It reports `VERIFY_OK exact_rational_checks=287`. These are exact finite algebraic checks, not exhaustive verification of the theorem for all real matrices or infinitely many times. The proof supplies those universal steps.

Run: `python3 verify.py` from the directory containing this file and the standalone script. No network connection or nonstandard Python package is required.

## Relationship to prior work

Michoel's 2026 branching fluctuation-dissipation relation, particularly Appendix B.1, equation (19), already gives the general clonal covariance integral and treats irreversible two-dimensional cases with cross-fluctuation or oscillatory behavior in Appendices B.2–B.3. The integral identity itself and qualitative nonequilibrium sensitivity are **not** new claims here. The present theorem instead resolves a distinct inverse question: which entire antisymmetric drift matrices are uniquely determined by a full age-resolved, same-time population-covariance observable, the minimum required jet order, the exact best sensitivity constant, and an all-time nullspace obstruction at spectral degeneracy. Those assertions are not stated in the inspected sections of the source.

Godrèche and Luck (2018) characterize stationary current, entropy production, response and two-time single-particle correlations of nonequilibrium Ornstein–Uhlenbeck processes. Their two-time correlations are not this branching population's same-time aggregate covariance, and they do not state the present identifiability dichotomy. Adamczak and Miłoś (2011) study central-limit regimes for branching Ornstein–Uhlenbeck sums, not inversion of rotational drift from a finite age jet. General system-identification literature can recover generators under different time-resolved observation assumptions and may contain mathematically stronger results that were not located; this is a remaining publication-priority risk.

## Limitations

The result assumes exact knowledge of the branch rate, a stationary Gaussian root distribution (with unit covariance only in canonical coordinates), a nondegenerate stationary covariance enabling whitening, independent daughter evolution, and availability of every entry of an age-resolved covariance matrix. It does not provide a finite-sample statistical estimator or a robustness bound for noisy numerical differentiation. The best Lipschitz constant diverges when two damping eigenvalues approach each other, and when eigenvalues collide the globally injective inverse ceases to exist; the theorem does not claim that *every* rotation is invisible in the degenerate case. Invisible rotations are precisely exhibited within repeated-eigenvalue blocks. Replacing the complete matrix with a scalar observable, changing the root law, allowing unknown or time-varying branching rate, or relaxing stationary Ornstein–Uhlenbeck dynamics requires separate analysis. Independent mathematical review and publication-priority verification have not been performed.

## References

1. Tom Michoel, *Fluctuation-dissipation relation in branching particle systems*, arXiv:2610.39624v1, first public 2026-10-29. https://arxiv.org/html/2610.39624v1 (especially Appendix B, equations (18)–(20)).
2. Claude Godrèche and Jean-Marc Luck, *Characterising the nonequilibrium stationary states of Ornstein-Uhlenbeck processes*, arXiv:1807.00694, first public 2018-07-02. https://arxiv.org/abs/1807.00694 (especially Sections 2.3–2.6).
3. Radosław Adamczak and Piotr Miłoś, *CLT for Ornstein-Uhlenbeck branching particle system*, arXiv:1111.4559, first public 2011-11-19. https://arxiv.org/abs/1111.4559.
4. Yue, Thunberg and Gonçalves, *Inverse Problems for Matrix Exponential in System Identification: System Aliasing*, arXiv:1605.06973. https://arxiv.org/abs/1605.06973 (related but different observation setting).
