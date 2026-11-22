# Sharp fourth-cumulant tomography of the hidden nematic coin in a chiral lattice walk

## Finding

Consider the four-heading, constant-step-length planar walk defined below, with a strictly positive circulant reorientation coin. Its one-step signed velocity correlation determines the persistence and chirality parameters \(p,c\), but every two-time velocity correlation and the full mean-squared-displacement curve is blind to the remaining nematic eigenvalue \(\eta\). That eigenvalue is nevertheless recovered uniquely from just **one long-time fourth-cumulant anisotropy**.

Let \(H_N=X_N/\ell\) and \(G_N=(X_N+Y_N)/(\sqrt2\ell)\). For the ordinary fourth cumulant \(\kappa_4(Z)=\mathbb E Z^4-3(\mathbb E Z^2)^2\), set
\[
K_{\rm ax}=\lim_{N\to\infty}\frac{\kappa_4(H_N)}{N},\quad
K_{\rm diag}=\lim_{N\to\infty}\frac{\kappa_4(G_N)}{N},\quad
\Delta=K_{\rm ax}-K_{\rm diag}.
\]
All three limits exist. With
\[
s=p^2+c^2,\qquad h=(1-p)^2+c^2,\qquad W=(1+p)^2+c^2,
\]
the complete inversion law is
\[
\boxed{\Delta=-\frac{s+6p+5}{4h}+\frac{3W}{2h(1-\eta)},\qquad
\eta=1-\frac{6W}{4h\Delta+s+6p+5}.}
\]
In particular, \(\partial\Delta/\partial\eta=3W/[2h(1-\eta)^2]>0\): no two distinct strictly positive reduced coins sharing \(p,c\) have the same anisotropy.

**Sharp realizability.** For any prescribed \(p,c\) with \(|p|+|c|<1\), the physically possible anisotropies are exactly the open interval
\[
\boxed{\Delta_{\min}<\Delta<\Delta_{\max},}
\]
where
\[
\Delta_{\min}=-\frac{s+6p+5}{4h}+\frac{3W}{4h(1-|p|)},
\quad
\Delta_{\max}=-\frac{s+6p+5}{4h}+\frac{3W}{4h|c|}
\]
and \(\Delta_{\max}=+\infty\) when \(c=0\). Every interior value corresponds to exactly one strictly positive four-weight coin; the endpoints are only boundary limits. The four weights are then
\[
\hat q_I=\frac{1+\eta+2p}{4},\quad
\hat q_B=\frac{1+\eta-2p}{4},\quad
\hat q_L=\frac{1-\eta+2c}{4},\quad
\hat q_R=\frac{1-\eta-2c}{4}.
\]
Thus two-point observations together with this single fourth-order contrast solve the full inverse problem **for the reduced coin**, not for a redundant decomposition into five elementary operations.

For example, at \(p=c=0\), all strictly positive coins have identical zero-lag and nonzero-lag second-order displacement statistics, while
\[
\Delta=\frac{1+5\eta}{4(1-\eta)},\quad -1<\eta<1,
\]
with a unique anisotropy sign change at \(\eta=-1/5\); the exact feasible range is \((-1/2,+\infty)\).

## Assumptions and scope

At each integer update, a heading \(J_n\in\{0,1,2,3\}\) is chosen from the preceding heading by the four-way stochastic circulant matrix
\[
C=\begin{pmatrix}
 a&r&b&l\\
 l&a&r&b\\
 b&l&a&r\\
 r&b&l&a
\end{pmatrix},\qquad
(a,b,l,r)=(\hat q_I,\hat q_B,\hat q_L,\hat q_R).
\]
It then performs one displacement of length \(\ell>0\) in the new heading \((\cos(\pi J_n/2),\sin(\pi J_n/2))\). The initial heading is uniform on all four states and the initial position is zero. The coin is strictly positive: \(a,b,l,r>0\), \(a+b+l+r=1\). Define its nontrivial Fourier eigenvalues by \(p=a-b\), \(c=l-r\), and \(\eta=a+b-l-r\). Equivalently its entire parameter domain is
\[
|p|+|c|<1,\qquad 2|p|-1<\eta<1-2|c|.
\]
There is no localization, translational Brownian component, hidden heading-dependent speed, or measurement noise. The two observables use normalized **projected displacement**, not radial displacement, and the limits concern ordinary cumulants per discrete step as \(N\to\infty\). The one-step complex velocity correlation is \(\mathbb E[\overline{U_n}U_{n+1}]=p+ic\), for \(U_n=e^{i\pi J_n/2}\), so the assumed knowledge of \(p,c\) can be obtained from consecutive position increments. All two-time correlations involve only that polar eigenvalue and its conjugate, not \(\eta\).

## Proof

**1. Spectral setup and existence.** For a real projection whose four possible unit increments are \(v_j\), the tilted transfer matrix is \(T(t)=\operatorname{diag}(e^{tv_0},\ldots,e^{tv_3})C\). Strict positivity makes its eigenvalue \(1\) simple and dominant at \(t=0\), with a simple analytic continuation \(\rho(t)\) for \(t\) near zero. The stationary initial distribution has nonzero projection on that eigenmode, so finite-dimensional spectral perturbation gives
\[
\log\mathbb E[e^{tZ_N}]=N\log\rho(t)+O(1)
\]
with the remainder analytic and derivatives through fourth order uniformly bounded near zero. Rotation by two headings changes the sign of projected increments but leaves the coin unchanged, hence the leading eigenvalue is even: \(\rho(t)=1+At^2+Bt^4+O(t^6)\). The asymptotic second- and fourth-cumulant slopes are \(2A\) and \(24(B-A^2/2)\), respectively.

**2. Two characteristic polynomials.** Put \(z\) for the spectral variable and define
\[
P_0(z)=(z-1)(z-\eta)((z-p)^2+c^2),\qquad s=p^2+c^2.
\]
For the axial projection \((1,0,-1,0)\), direct four-by-four determinant expansion gives
\[
P_A(z,t)=P_0(z)+(\cosh t-1)Q_A(z),
\]
\[
Q_A(z)=-\frac z2\big[(1+\eta+2p)z^2
-2(s+\eta p+\eta+p)z+(1+\eta)s+2\eta p\big].
\]
For the normalized diagonal projection \((1,1,-1,-1)/\sqrt2\), write \(u=\cosh(t/\sqrt2)\); then
\[
P_D(z,t)=P_0(z)+(u-1)Q_1(z)+(u^2-1)Q_2(z),
\]
\[
Q_1(z)=-z\big[(1+\eta)s+2\eta p+(1+\eta+2p)z^2\big],
\quad Q_2(z)=z^2(s+\eta p+\eta+p).
\]
These are exact polynomial identities, with no continuum or weak-turning approximation. Their determinants are independently checked in `CHECKER.py`.

**3. Quartic coefficients and cancellation.** Since
\[
P_0'(1)=(1-\eta)h>0,\qquad
h=(1-p)^2+c^2,
\]
substituting \(z=1+At^2+Bt^4+O(t^6)\) and expanding the two determinants shows that the shared quadratic coefficient is
\[
A=-\frac{Q_A(1)}{2P_0'(1)}=\frac{1-s}{4h}.
\]
In particular, the two projected variance slopes coincide and equal \((1-s)/(2h)\). The respective quartic coefficients satisfy
\[
B_A=-\frac{\frac12P_0''(1)A^2+\frac12Q_A'(1)A+Q_A(1)/24}{P_0'(1)},
\]
\[
B_D=-\frac{\frac12P_0''(1)A^2+[Q_1'(1)/4+Q_2'(1)/2]A+Q_1(1)/96+Q_2(1)/12}{P_0'(1)}.
\]
Their difference eliminates the shared quadratic-log correction. Substituting the displayed polynomials and simplifying gives precisely
\[
24(B_A-B_D)=-\frac{s+6p+5}{4h}+\frac{3[(1+p)^2+c^2]}{2h(1-\eta)}.
\]
The expression is therefore the exact difference of fourth-cumulant slopes, rather than of uncentered fourth moments.

**4. Inversion and the sharp image.** Because \(|p|+|c|<1\), both \(h\) and \(W\) are positive. Hence the derivative in the Finding is strictly positive throughout the allowed open \(\eta\)-interval. Solving the displayed rational equality for \(\eta\) gives the explicit inverse. The nonnegativity of the four physical coin weights is exactly the pair of linear bounds \(2|p|-1\le\eta\le1-2|c|\); strict positivity makes them strict. The strictly increasing continuous map sends this interval bijectively onto the image between its two endpoint limits. Evaluating the rational function at the lower and upper endpoints gives \(\Delta_{\min}\) and \(\Delta_{\max}\). If \(c=0\), the upper endpoint is \(\eta=1\) and \(\Delta\to+\infty\); otherwise the upper bound is finite. Each interior \(\eta\) reconstructs exactly one positive quadruple via the four linear formulas. The special case \(p=c=0\) is immediate.

## Verification

Run `python CHECKER.py` with Python 3, SymPy, and NumPy. It symbolically verifies both exact determinant identities, the shared variance coefficient, both quartic coefficients, their difference, the derivative, and the inverse identity. It also compares the predicted long-time anisotropy with an independently implemented four-heading finite-step moment hierarchy for six positive, asymmetric and symmetric coins. All six numerical errors at \(N=3000\) steps were below \(0.01\). The finite calculations do not prove the infinite-time limit; that follows from the simple dominant eigenvalue and exact polynomial algebra above.

## Relationship to prior work

Sherf, Uhlig, Wójcik, Metzler, Roichman and Kalz (arXiv:2611.14446v1, first public 2026-11-10) introduced the active chiral square-lattice coin, explicitly described the redundant five-operation versus reduced four-weight parameterization, and established that first and second transport statistics depend on its polar mode \(p+ic\) rather than its nematic mode \(\eta\). That physical model, eigenmode decomposition, covariance invisibility, and low-order transport law are prior work. Their Fourier-space higher-gradient discussion highlights the nematic mode's possible role at higher order; it does not state this strictly monotone fourth-cumulant contrast, exact inverse, or sharp feasible anisotropy interval.

Sadjadi, Shaebani, Rieger and Santen (*Physical Review E* 91, 062715, 2015) provide a general persistent-random-walk forward Fourier-transform and fourth-moment framework, including explicit observation that a second angular Fourier moment affects fourth-order statistics even when the MSD is unchanged. The present result does not claim discovery of that principle or an original general moment formula; its claim is the exact **full reduced-coin inverse and attainability classification** for the discrete chiral four-heading specialization. Closest available related published research on continuous-time chiral four-heading walks or arbitrary Poisson turning laws derives fourth-cumulant signs and envelopes in different update dynamics rather than this discrete-time inverse. A general forward moment formula can algebraically imply the present special-case expression after calculation, so priority against implicit derivations remains a genuine limitation.

## Limitations

The strict inverse concerns ideal exact limiting cumulant coefficients and strictly positive reduced four-way coins. No finite-sample stability or noise tolerance is proved, and the formula is poorly conditioned near boundary regimes where the nematic eigenmode relaxes slowly. The initial headings are uniformly stationary, and each move has a constant known length. Zero transition weights and nonprimitive coins require separate boundary treatment. The original five operation probabilities are not separately identifiable because randomization is a linear combination of the four rotations. Fourth-order sensitivity of persistent walks to second angular moments is previously known; novelty of the more specialized strict inversion and sharp interval is not independently certified.

## References

1. N. Sherf, J. Uhlig, J. Wójcik, R. Metzler, Y. Roichman, and E. Kalz, *The active chiral random walk*, arXiv:2611.14446v1 (first public 2026-11-10), https://arxiv.org/abs/2611.14446. Sections 2.2–2.3 and angular-mode calculations.
2. Z. Sadjadi, M. R. Shaebani, H. Rieger, and L. Santen, *Persistent-random-walk approach to anomalous transport of self-propelled particles*, *Physical Review E* **91** (2015), 062715, https://doi.org/10.1103/PhysRevE.91.062715. General fourth-moment framework and higher angular-harmonic dependence.
3. *Directional fourth-cumulant phases and reentrant reversal effects in a chiral four-state walker*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-directional-fourth-cumulant-phases-and-reentrant-reversal-effect--ec488e19dc0f. Different continuous-time velocity-jump dynamics.
4. *Sharp fourth-cumulant envelopes at fixed persistence and chirality in planar run-and-tumble motion*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-fourth-cumulant-envelopes-at-fixed-persistence-and-chirali--0a534892a5b1. Continuous-time Poisson-tumbling sharp forward cumulant ranges.
