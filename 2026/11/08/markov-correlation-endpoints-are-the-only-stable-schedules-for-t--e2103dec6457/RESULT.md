# Markov-correlation endpoints are the only stable schedules for two symplectic-Euler steps

## Finding

Let \(0<a<b<2\) and set
\[
M(h)=\begin{pmatrix}1-h^2&h\\-h&1\end{pmatrix}.
\]
At successive updates of the unit-frequency harmonic oscillator, a two-state time-step chain has probabilities \(\Pr(S_{n+1}=S_n)=s\) and \(\Pr(S_{n+1}\ne S_n)=1-s\). The phase-space state is updated by \(X_{n+1}=M(S_{n+1})X_n\). For every \(s\in(0,1)\), the mean-square growth exponent is **strictly positive**: there is a \(\rho(s)>1\), independent of initial data, such that
\[
\mathbb E\|X_n\|_2^2\sim c(X_0,S_0,s)\rho(s)^n,
\qquad c(X_0,S_0,s)>0
\]
for every nonzero deterministic \(X_0\) and either fixed initial mode. The two perfect-correlation endpoints can instead be bounded. At \(s=1\), the mode never changes and all trajectories are bounded. At \(s=0\), the modes alternate exactly, and all trajectories are bounded if
\[
\left|2-(a+b)^2+a^2b^2\right|<2.
\]
For \(a=1/2\), \(b=3/2\), the alternating two-step trace is exactly \(-23/16\), so **both** endpoints are bounded while **every** interior Markov correlation produces exponential expected-energy growth. In this pair the conditional second-moment operator has the polynomial identity
\[
\det(I-\mathcal L_s)=-\frac94s(1-s)^2.
\]

## Assumptions and scope

The physical system is \(\dot q=v,\ \dot v=-q\), with physical energy \(E=(q^2+v^2)/2\). At step \(n+1\), kick velocity by \(-S_{n+1}q_n\), then drift position by \(S_{n+1}v_{n+1}\). The resulting \(M(h)\) is symplectic with determinant one. The two positive step lengths \(a,b\) lie strictly between zero and the conventional individual-step elliptic boundary \(2\). The Markov chain is time homogeneous, stationary probabilities \((1/2,1/2)\), with transition matrix \(\begin{psmallmatrix}s&1-s\\1-s&s\end{psmallmatrix}\). No independence between consecutive step lengths is assumed. The initial step mode may be fixed; \(X_0\ne0\) is deterministic. The theorem concerns arbitrarily many numerical updates and **mean-square** growth, not almost-sure or physical-time Lyapunov exponents.

## Proof

**(1) The six-dimensional positive moment map.** For each mode \(j\in\{a,b\}\), let \(W_j(n)=\mathbb E[X_nX_n^{\mathsf T}\mathbf1_{\{S_n=j\}}]\), a positive-semidefinite symmetric matrix. For \(0<s<1\), the update is
\[
\begin{aligned}
W_a(n+1)&=M(a)[sW_a(n)+(1-s)W_b(n)]M(a)^{\mathsf T},\\
W_b(n+1)&=M(b)[(1-s)W_a(n)+sW_b(n)]M(b)^{\mathsf T}.
\end{aligned}
\]
This linear transformation on two symmetric \(2\times2\) matrices is \(\mathcal L_s\). The expected squared norm equals \(\operatorname{tr}(W_a(n)+W_b(n))\).

**(2) Strict positivity of its square.** If \(W_a+W_b\) is positive definite, both weighted sums in (1) are positive definite and remain so. Otherwise, every nonzero input is supported on one common real line spanned by some \(v\ne0\). After one update, the two nonzero mode blocks are supported on the lines \(M(a)v\) and \(M(b)v\). Those lines are distinct: since \(\det M(h)=1\), direct multiplication gives
\[
\operatorname{tr}(M(b)^{-1}M(a))=2-(a-b)^2\in(-2,2).
\]
Consequently \(M(b)^{-1}M(a)\) has no real eigenline. Both weighted sums in the next update are positive definite. Thus \(\mathcal L_s^2\) sends every nonzero element of the product positive-semidefinite cone into its interior. The finite-dimensional strong Perron–Frobenius theorem for a proper cone gives a simple strictly dominant real root \(\rho>0\), positive-definite right eigenblocks \((C_a,C_b)\), and strictly positive asymptotic growth coefficient for any nonzero positive-semidefinite initial block pair.

**(3) The determinant rigidity forcing \(\rho>1\).** The eigenblock equations are
\[
\rho C_a=M(a)[sC_a+(1-s)C_b]M(a)^{\mathsf T},
\quad \rho C_b=M(b)[(1-s)C_a+sC_b]M(b)^{\mathsf T}.
\]
Since \(\det M(a)=\det M(b)=1\), strict concavity of \(\log\det\) on positive-definite matrices yields
\[
2\log\rho+\log\det C_a\ge s\log\det C_a+(1-s)\log\det C_b
\]
and the corresponding inequality with \(a,b\) exchanged. Adding proves \(\rho\ge1\). If equality holds, equality in both strict concavity inequalities forces \(C_a=C_b=C\), and the eigenblock equations force simultaneous invariance \(M(a)CM(a)^{\mathsf T}=M(b)CM(b)^{\mathsf T}=C\). But for every \(h\in(0,2)\), the positive-definite solutions of \(M(h)CM(h)^{\mathsf T}=C\) are exactly the positive scalar multiples of
\[
C_h=\begin{pmatrix}1&h/2\\h/2&1\end{pmatrix}.
\]
Indeed, direct multiplication verifies this invariant, and the elliptic matrix \(M(h)\) is conjugate to a nontrivial planar rotation, for which the invariant symmetric forms are one-dimensional. The normalized off-diagonal coefficient \(h/2\) makes it impossible to have a common invariant when \(a\ne b\). Hence \(\rho>1\). The asymptotic formula in the finding now follows from step (2).

**(4) The two endpoints.** At \(s=1\) the step is forever fixed; each \(M(h)\) is conjugate to a rotation for \(h\in(0,2)\), so all its powers are uniformly bounded. At \(s=0\), steps alternate. A direct product calculation gives \(\operatorname{tr}(M(b)M(a))=2-(a+b)^2+a^2b^2\). An \(SL(2,\mathbb R)\) matrix with trace strictly between \(-2\) and \(2\) has uniformly bounded powers. For \(a=1/2\), \(b=3/2\), the trace is \(-23/16\). Thus both endpoint schedules are bounded.

**(5) An exact finite-dimensional certificate.** In coordinates \((W_{11},W_{12},W_{22})\), the one-step covariance map at length \(h\) is the matrix
\[
T(h)=\begin{pmatrix}(1-h^2)^2&2h(1-h^2)&h^2\\-h(1-h^2)&1-2h^2&h\\h^2&-2h&1\end{pmatrix}.
\]
For \(a=1/2,b=3/2\), the full \(6\times6\) transfer is
\[
\mathcal L_s=\begin{pmatrix}sT(a)&(1-s)T(a)\\(1-s)T(b)&sT(b)\end{pmatrix}.
\]
Exact rational elimination gives \(\det(I-\mathcal L_s)=-9s(1-s)^2/4\). For every \(0<s<1\), this is negative, independently certifying that the real characteristic polynomial has a root greater than one. This last certificate is not substituted for the general proof in steps (1)–(4).

## Verification

Run `python3 verify.py` with Python 3 and no third-party packages. Its 67 exact-rational assertions include symplectic determinants, the invariant covariance for seventeen admissible step lengths, the alternating trace, relative ellipticity, and seven evaluations of the \(6\times6\) determinant. Each determinant entry is affine in \(s\), so its determinant has degree at most six; agreement at seven distinct rational points proves the stated degree-six-bounded polynomial identity over all real \(s\). Computation is supplementary to the general infinite-time Perron–Frobenius argument.

## Relationship to prior work

Abdulle and Garegnani (first public January 4, 2018, arXiv:1801.01340) develop random physical time steps for geometric integrators, prove preservation of symplecticity, and establish finite-step/error and long-but-finite energy estimates under small-step scaling. These do not imply bounded energy for infinitely many random updates at a fixed nonzero step distribution. Sturman and Thiffeault (2018) bound generalized Lyapunov exponents for independent products of shears, not the two-state Markov symplectic-Euler family. General Markov-jump covariance criteria express stability through the spectrum of a lifted operator but do not themselves give the all-interior-instability theorem or the two bounded endpoints. Lie, Stahn and Sullivan (2022) analyze random additive perturbations of one-step operator evolution rather than the present correlated step selection. The novelty here is the exact failure of mean-square robustness to *every* nonzero stochastic deviation from a stable periodic timetable, not a new generic spectral-radius test.

## Limitations

The result is specific to one harmonic oscillator, the kick-then-drift symplectic Euler family, two step values strictly in the individually elliptic interval, and a symmetric two-state Markov chain. It gives a second-moment growth rate, not the almost-sure top Lyapunov exponent, and does not contradict finite-horizon energy estimates or imply numerical instability for a finite simulation of prescribed duration. Classical Markov-switching spectral theory may indirectly encompass the cone argument; specialist publication-precedence review is needed.

## References

- A. Abdulle and G. Garegnani, *Random time step probabilistic methods for uncertainty quantification in chaotic and geometric numerical integration*, arXiv:1801.01340 (first posted 2018-01-04), Sections 7.1–7.2. https://arxiv.org/abs/1801.01340
- R. Sturman and J.-L. Thiffeault, *Lyapunov Exponents for the Random Product of Two Shears*, Journal of Nonlinear Science 29 (2019), 593–620, online 2018. https://doi.org/10.1007/s00332-018-9497-3
- S. Zhou, X. Liu, B. Chen and H. Liu, *Stability Analysis for a Class of Discrete-Time Nonhomogeneous Markov Jump Systems with Multiplicative Noises*, Complexity (2018). https://doi.org/10.1155/2018/1586846
- H. C. Lie, M. Stahn and T. J. Sullivan, *Randomised one-step time integration methods for deterministic operator differential equations*, Calcolo 59 (2022). https://doi.org/10.1007/s10092-022-00457-6
