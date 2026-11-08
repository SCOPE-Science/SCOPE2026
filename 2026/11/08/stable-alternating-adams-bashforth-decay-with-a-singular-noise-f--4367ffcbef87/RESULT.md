# Stable alternating Adams–Bashforth decay with a singular noise floor

## Finding

For the *standard* variable-step, two-step Adams–Bashforth (AB2) discretization of the real scalar decay equation \(y'(t)=-\gamma y(t)\), \(\gamma>0\), suppose the positive step lengths alternate between \(a/\gamma\) and \(b/\gamma\), where \(a,b>0\). The exact strict asymptotic absolute-stability condition is

\[
\boxed{a+b<2.}
\]

Thus the negative-real-axis stability interval depends on the **period total**, not on the ratio \(a/b\). Nevertheless, stability does not give a ratio-independent bound on the response to locally injected noise. Add an independent zero-mean scalar perturbation of fixed variance \(\sigma^2>0\) to the updated value at *each* AB2 step. If \(0<a+b<2\), the resulting linear process has a unique asymptotic two-periodic covariance. Denote by \(V_{\mathrm{long}}(a,b)\) the variance at the end of the step of length \(b/\gamma\). For every fixed \(b\in(0,2)\),

\[
\boxed{\lim_{a\downarrow0}a^2 V_{\mathrm{long}}(a,b)=\frac{\sigma^2 b^4}{4\left[1-\left(1-b+\frac{b^2}{2}\right)^2\right]}.}
\]

The right-hand side is positive and finite. Hence the stationary variance diverges at the *sharp quadratic order* \(a^{-2}\), even though the deterministic period map has a limiting spectral radius strictly below one. The phase-reversed two-step matrix simultaneously has Euclidean operator norm asymptotic to \(b^2/a\).

In particular, at \(b=1\), \(\lim_{a\downarrow0}a^2V_{\mathrm{long}}(a,1)=\sigma^2/3\). By contrast, the ordinary constant-step AB2 method with normalized stepsize \(1/2\), and the same independent additive noise variance per step, has stationary scalar variance \(6\sigma^2/5\).

## Assumptions and scope

All statements concern exact arithmetic in the transfer coefficients for a scalar autonomous ODE with \(\gamma>0\); a noisy update is modeled by directly adding an independent random scalar to its newly calculated solution value. Noise variables have mean zero, common finite variance \(\sigma^2>0\), and are independent of the deterministic initial pair and of one another. They need not be Gaussian. The step pattern is exactly periodic: after each long step comes a short step and then a long step. The initial pair is any fixed finite real pair; its mean contribution decays precisely in the stated stability region. Variance is the infinite-update limit at the fixed end-of-long-step phase, and the small-\(a\) limit follows the infinite-time limit, not conversely.

For general real coefficients outside the negative axis, for nonperiodic step sequences, or for floating-point error whose magnitude depends on the evolving numerical solution, no stability or variance assertion is made. Noise here is an idealized *additive* local perturbation rather than a universal hardware roundoff model.

## Proof

**1. Exact variable-step transfer.** Linear interpolation of the two available derivatives over the next interval of normalized length \(h\), when the preceding interval has normalized length \(p\), gives

\[
y_{n+1}=y_n+h\left[\left(1+\frac{h}{2p}\right)f_n-\frac{h}{2p}f_{n-1}\right],
\qquad f_j=-y_j
\]

under the rescaled time \(\tau=\gamma t\). Hence for \(X_n=(y_n,y_{n-1})^{\mathsf T}\), the deterministic transfer is

\[
T(h,p)=\begin{pmatrix}1-h-\frac{h^2}{2p}&\frac{h^2}{2p}\\1&0\end{pmatrix},\qquad X_{n+1}=T(h,p)X_n.
\]

Define \(H=T(a,b)\) (short update), \(L=T(b,a)\) (long update), and \(M=LH\) (two-step map, observed immediately after each long step). Direct multiplication gives

\[
\operatorname{tr}M=1-(a+b)+\frac{(a+b)^2}{2}+\frac{ab}{4},\qquad \det M=\frac{ab}{4}.
\]

For the real quadratic \(\chi(\mu)=\mu^2-(\operatorname{tr}M)\mu+\det M\), its strict Schur/Jury conditions are \(1-\det M>0\), \(\chi(1)>0\), and \(\chi(-1)>0\). The identities

\[
\chi(1)=\frac{(a+b)(2-a-b)}2,\qquad
\chi(-1)=\frac{(a+b-1)^2+ab+3}2>0
\]

show that when \(a+b<2\), all three conditions hold (indeed \(ab/4<1/4\)). At equality, \(\chi(1)=0\), so the map has a unit eigenvalue. For \(a+b>2\), \(\chi(1)<0\) and the real monic characteristic polynomial has a root strictly greater than one. Thus strict asymptotic stability holds *if and only if* \(a+b<2\).

**2. Stationary covariance.** Put \(e_1=(1,0)^{\mathsf T}\). At each update, perturb the *new scalar value*: \(X_{n+1}=T(h,p)X_n+e_1\xi_n\). Observing the process after long steps and grouping the independent short- and long-step noises gives

\[
X_{k+1}^{\mathrm{long}}=M X_k^{\mathrm{long}}+L e_1\xi_{k,\mathrm{short}}+e_1\xi_{k,\mathrm{long}}.
\]

In the stable region its unique limiting covariance \(P(a,b)\) is the convergent positive-definite solution of

\[
P=MPM^{\mathsf T}+\sigma^2\left[(Le_1)(Le_1)^{\mathsf T}+e_1e_1^{\mathsf T}\right],
\quad
P=\sum_{j=0}^{\infty}M^j W(M^{\mathsf T})^j.
\]

The sum converges by \(\rho(M)<1\). It is strictly positive-definite because the two forcing directions \(e_1\) and \(Le_1=(1-b-b^2/(2a),1)^{\mathsf T}\) are linearly independent. The end-of-long-step scalar variance is \(V_{\mathrm{long}}=e_1^{\mathsf T}Pe_1\).

**3. Sharp singular coefficient.** Holding \(b\in(0,2)\) fixed and letting \(a\downarrow0\), direct inspection of the transfer matrices yields

\[
M\longrightarrow M_0=\begin{pmatrix}c&0\\1&0\end{pmatrix},
\quad c=1-b+\frac{b^2}{2}\in[1/2,1),
\quad aLe_1\longrightarrow\begin{pmatrix}-b^2/2\\0\end{pmatrix}.
\]

Consequently the rescaled forcing covariance satisfies

\[
a^2 W\longrightarrow\frac{\sigma^2b^4}{4}e_1e_1^{\mathsf T}.
\]

Since \(\rho(M_0)=c<1\), the inverse linear operator \(Z\mapsto Z-MZM^{\mathsf T}\) depends continuously on \(M\) near \(M_0\) and remains invertible. Therefore \(a^2P\) converges to the unique solution \(P_0\) of

\[
P_0=M_0P_0M_0^{\mathsf T}+\frac{\sigma^2b^4}{4}e_1e_1^{\mathsf T},\quad
P_0=\frac{\sigma^2b^4}{4(1-c^2)}\begin{pmatrix}1&c\\c&1\end{pmatrix}.
\]

Taking the first diagonal entry proves the asserted exact variance limit. The coefficient is neither zero nor infinite for fixed \(b\in(0,2)\), proving the claimed sharp order.

Finally, the opposite-phase two-step matrix is \(HL\). Direct multiplication shows

\[
aHL\longrightarrow\frac{b^2}{2}\begin{pmatrix}-1&1\\-1&1\end{pmatrix}.
\]

The limiting rank-one matrix has spectral norm \(b^2\); hence \(\lVert HL\rVert_2\sim b^2/a\). Although \(LH\) and \(HL\) have the same eigenvalues, their phase-specific nonnormal amplification is not uniformly bounded as the step ratio degenerates.

**4. Exact rational example.** For \(b=1\), solving the three independent entries of the Lyapunov equation gives

\[
\frac{V_{\mathrm{long}}(a,1)}{\sigma^2}=
\frac{a^7-4a^6-4a^5-8a^4+4a^3+16a^2+a+4}
{a^2(a-4)(a-1)(a+1)(a^2+a+3)},\qquad 0<a<1.
\]

Its \(a^2\)-scaled limit is \(1/3\). At \(a=1/10\), this ratio equals exactly \(42631561/1200771\), approximately \(35.50348984\). The corresponding fixed-step \(1/2\) variance \(6\sigma^2/5\) follows from the scalar stationary Yule–Walker equations for \(y_{n+1}=(y_n+y_{n-1})/4+\xi_n\).

## Verification

Run `python verify.py` with Python 3.10 or later and SymPy 1.14.0. The script checks the exact transfer trace/determinant, both Jury factorizations, two singular transfer limits, the limiting covariance matrix, the full rational expression at \(b=1\), its sharp coefficient, and twelve additional positive-definite rational covariance solutions by exact linear algebra. The recorded run returns PASS. Symbolic identities are independently visible in the proof; finite cases are regression checks, not replacements for the all-parameter argument.

## Relationship to prior work

The motivating paper by Throwe and Teukolsky (first public arXiv posting 2018-11-06) develops Adams–Bashforth-based integration with arbitrary varying steps for conservative multirate systems and explicitly discusses accuracy and conservation, but not this fixed-scalar two-periodic noisy covariance limit. López and Romay analyze preassigned step ratios for variable-step Adams implementations and practical efficiency, not the period-two stationary noise asymptotic. Tavakkol, Son, and Lynett develop an adaptive third-order Adams–Bashforth discretization for Boussinesq flows; their step control and experiments do not provide the exact AB2 result here. Earlier Nordsieck stability papers by Skeel–Jackson and by Calvo–Lisbona–Montijano concern step-ratio stability, and therefore pose the strongest possible precedent for the *deterministic* part; their accessible abstracts do not resolve the stochastic-response comparison. The independent driving-noise model and its singular coefficient are the specific contribution being assessed, not variable-step Adams methods themselves.

## Limitations

The claim is about the homogeneous scalar test equation, a fixed two-periodic grid, and additive independent local noise with a fixed variance. It does not bound deterministic local truncation error, physical error under a consistent startup, general stiff or oscillatory systems, genuinely floating-point relative roundoff, nonperiodic meshes, or multirate spatial discretizations. A stable Floquet spectrum alone is not claimed to imply a uniform noise gain. Specialist earlier stability or periodic-AR literature could contain an equivalent result; one closely related 1989 paper was available only in abstract form and could not be fully compared. The exact variance expression does not imply a practical stepsize design recommendation without a model of actual error magnitude.

## References

1. W. Throwe and S. A. Teukolsky, *A high-order, conservative integrator with local time-stepping*, arXiv:1811.02499, original public posting 2018-11-06. https://arxiv.org/abs/1811.02499
2. D. J. López and J. G. Romay, *Implementing Adams Methods with Preassigned Stepsize Ratios*, Mathematical Problems in Engineering (2010), DOI 10.1155/2010/765620. https://doi.org/10.1155/2010/765620
3. S. Tavakkol, S. Son and P. Lynett, *Adaptive Third Order Adams-Bashforth Time Stepping for Extended Boussinesq Equations*, arXiv:1909.04153, original public posting 2019-09-05. https://arxiv.org/abs/1909.04153
4. R. D. Skeel and L. W. Jackson, *The Stability of Variable-Stepsize Nordsieck Methods*, SIAM Journal on Numerical Analysis 20 (1983), 840–853, DOI 10.1137/0720056. https://doi.org/10.1137/0720056
5. M. Calvo, F. Lisbona and J. Montijano, *On the Stability of Interpolatory Variable-Stepsize Adams Methods in Nordsieck Form*, SIAM Journal on Numerical Analysis 26 (1989), 946–962, DOI 10.1137/0726052. https://doi.org/10.1137/0726052
