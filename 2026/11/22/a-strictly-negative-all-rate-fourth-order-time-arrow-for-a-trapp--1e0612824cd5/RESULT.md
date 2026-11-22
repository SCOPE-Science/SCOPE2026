# A strictly negative all-rate fourth-order time arrow for a trapped telegraph particle

## Finding
Let a one-dimensional run-and-tumble particle have constant propulsion speed magnitude and a symmetric Poisson-flipping heading while undergoing linear harmonic confinement and independent thermal diffusion. Its stationary position history is not reversible, and its first possible nonzero polynomial two-time arrow has **one strict sign at every lag and every positive switching/trap-rate ratio**, even in the presence of arbitrary independent thermal diffusion.

More precisely, for the stationary process defined below, write
\[
\mathcal A(t)=\mathbb E[X_0^3X_t]-\mathbb E[X_0X_t^3],\qquad t\geq0.
\]
For every \(k,g,v>0\), \(D\geq0\), and \(z>0\), its unilateral Laplace transform is
\[
\boxed{\widehat{\mathcal A}(z)=-\frac{24gv^4}{(2g+k)(2g+3k)(z+2g)(z+k)(z+3k)(z+2g+2k)}.}
\]
Consequently, writing \(h_a(t)=e^{-at}\mathbf1_{\{t\geq0\}}\) and \(*\) for convolution on the nonnegative half-line,
\[
\boxed{\mathcal A(t)=-\frac{24gv^4}{(2g+k)(2g+3k)}(h_{2g}*h_k*h_{3k}*h_{2g+2k})(t)<0\quad (t>0).}
\]
The formula holds without excluding coincident relaxation rates, and is **independent of \(D\)**. In particular,
\[
\mathcal A(t)=-\frac{4gv^4}{(2g+k)(2g+3k)}t^3+O(t^4),\qquad t\downarrow0.
\]
No lower-degree polynomial two-time antisymmetry survives stationary sign symmetry and symmetry of scalar covariance. Thus degree four is the first possible nonzero order.

## Assumptions and scope
Fix \(k,g,v>0\) and \(D\geq0\). The stationary sign \(S_t\in\{-1,+1\}\) changes sign at rate \(g\), so \(\mathbb E[S_0S_t]=e^{-2g|t|}\). Let \(B_t\) be a two-sided standard Brownian motion independent of \(S\), and define the unique stationary solution
\[
dX_t=(-kX_t+vS_t)\,dt+\sqrt{2D}\,dB_t.
\]
Equivalently, \(X_t=v\int_{-\infty}^te^{-k(t-s)}S_sds+\sqrt{2D}\int_{-\infty}^te^{-k(t-s)}dB_s\). The active part is bounded by \(v/k\), the Gaussian part has finite moments of all orders, and the process is stationary and globally sign symmetric. The observable uses a *positive forward lag*, and an antisymmetric expectation is defined from the position coordinate alone; it is not a trajectory-level entropy-production rate. In higher-dimensional isotropic-redraw notation, a one-dimensional redraw event at rate \(\gamma\) flips with rate \(g=\gamma/2\).

## Proof
**Stationary moment balances.** The generator on smooth polynomial functions \(f(x,s)\), \(s=\pm1\), is
\[
Lf(x,s)=(-kx+vs)\partial_xf+D\partial_x^2f+g[f(x,-s)-f(x,s)].
\]
Set \(c_1=\mathbb E[XS]\), \(m_2=\mathbb E[X^2]\), \(c_3=\mathbb E[X^3S]\), and \(m_4=\mathbb E[X^4]\) in the stationary law. Applying \(\mathbb ELf=0\) to the polynomials \(xs,x^2,x^3s,x^4\) yields in order
\[
 c_1=\frac{v}{k+2g},\quad m_2=\frac{vc_1+D}{k},\quad c_3=\frac{3vm_2+6Dc_1}{3k+2g},\quad m_4=\frac{vc_3+3Dm_2}{k}.
\]
These are exact finite generator identities, not moment-closure assumptions.

**Forward mixed-moment hierarchy.** Define
\[
f_0(t)=\mathbb E[X_0S_t],\quad f_1(t)=\mathbb E[X_0X_t],\quad f_2(t)=\mathbb E[X_0X_t^2S_t],\quad f_3(t)=\mathbb E[X_0X_t^3].
\]
The Markov generator gives the exact triangular system
\[
\begin{aligned}
f_0'&=-2gf_0,\\
f_1'&=-kf_1+vf_0,\\
f_2'&=-(2k+2g)f_2+2vf_1+2Df_0,\\
f_3'&=-3kf_3+3vf_2+6Df_1,
\end{aligned}
\]
with \((f_0,f_1,f_2,f_3)(0)=(c_1,m_2,c_3,m_4)\). Set \(a(t)=\mathbb E[X_0^3X_t]\). Conditional first moments of \(X_t\) and \(S_t\) imply
\[
\widehat a(z)=\frac{m_4+vc_3/(z+2g)}{z+k}.
\]
Writing \(M\) for the exact coefficient matrix of the four-dimensional system and \(m=(c_1,m_2,c_3,m_4)^\top\), \(\widehat f_3(z)=e_4^\top(zI-M)^{-1}m\). Successive triangular elimination gives the entirely explicit identity
\[
\frac{m_4+vc_3/(z+2g)}{z+k}-e_4^\top(zI-M)^{-1}m
=-\frac{24gv^4}{(2g+k)(2g+3k)(z+2g)(z+k)(z+3k)(z+2g+2k)}.
\]
The independence of \(D\) is an exact cancellation in this identity, verified also symbolically in the standalone checker. All Laplace transforms are valid for \(z>0\) because the mixed stationary moments are bounded in time.

**Strict sign and boundaries.** Since \(\mathcal A(t)=a(t)-f_3(t)\), uniqueness of the Laplace transform and the Laplace convolution theorem give the four-exponential convolution displayed above. For any \(t>0\), its simplex integral is strictly positive because its integrand is a product of strictly positive exponentials over a simplex of positive volume. The prefactor is strictly negative when \(g,v>0\); this proves the inequality for all \(t>0\), including coincident rates where partial fractions would be singular. The four-fold convolution is \(t^3/3!+O(t^4)\) as \(t\downarrow0\), giving the stated cubic coefficient. Symmetry under \((X,S,B)\mapsto(-X,-S,-B)\) annihilates odd total-degree moments; stationary scalar covariance is symmetric under time reversal at degree two. Therefore fourth order is the first possible nonzero polynomial two-time arrow, and strictness here witnesses irreversibility of the observed stationary position history.

## Verification
Run `python checker.py` in this package with Python 3, SymPy, NumPy and SciPy. The checker independently constructs the polynomial generator matrix, computes the stationary moments, simplifies the exact Laplace transform difference to the asserted four-pole factorization and checks its first three time derivatives. It then compares the full six-state conditional-moment matrix exponential with a separate four-stage positive-convolution cascade for six parameter combinations, eight lags each, including the resonances \(2g=k\) and \(2g=3k\), zero thermal noise and large positive thermal noise. The packaged run passed 100 symbolic/numerical checks. Finite checks corroborate the exact argument; the proof of all-parameter strict sign comes from positivity of the convolution, not sampling.

## Relationship to prior work
Guéneau, Majumdar and Schehr [1] establish the stationary harmonic run-and-tumble laws and their Gaussian thermal convolution; Sevilla and Meléndez Mora [2] develop an independent one-dimensional convolution treatment and stationary fluctuation comparisons. Their one-time results are credited and do not by themselves give a signed two-time fourth moment. Sun, Ye and Chen [3] provide broad conditional moment techniques and explicit stationary-state constructions; the present finite generator calculation uses standard machinery, not a purported invention of it.

A published high-dimensional result [4] studies precisely \(\mathbb E[X_0^3X_t]-\mathbb E[X_0X_t^3]\) under isotropic redraws. It establishes a one-sign theorem for dimensions at most seven **at the fixed rate ratio \(\gamma/k=2\)**, including the one-dimensional case \(g=k\). It also gives arbitrary-rate short- and long-lag coefficients, but does not assert the all-lag, all-positive-rate one-dimensional sign law; its previously covered resonant case is expressly excluded from the claim of novelty. A separate published work [5] derives the four-time connected cumulant of a telegraph bath and its strict negative sign under positive filtering. Its negativity does **not** determine the difference between the two distinct time orderings of fourth moments; establishing that ordering needs the additional four-pole factorization. It gives important exact precursor information, not a direct bound of the desired ordering. Another prior work [6] finds sign reversal of a position-only fourth-order arrow for *resetting Brownian* rather than telegraphic forcing, underscoring the dynamical specificity of the strict sign.

The asserted extension is the **uniform-in-rate strict position-only fourth-order asymmetry**, its exact thermal-noise cancellation and positive-convolution representation. General published multi-time techniques may permit a rederivation; novelty is not certification of global priority.

## Limitations
This is an overdamped single-coordinate model with symmetric instantaneous sign flips, a linear trap, additive independent Gaussian thermal forcing and complete stationary initialization. The sign theorem does not extend here to biased flips, finite-duration tumbles, rotational diffusion, nonlinear trapping or inertia. Strictness vanishes in limiting degenerate cases with \(g=0\) or \(v=0\), excluded from the positive-parameter theorem. It does not estimate entropy production or a finite-data detection rate. The exact multi-time kernel available in [5] is a residual priority risk for the factorized inequality, and a broader previously unknown result could subsume the all-rate conclusion. No independent scientific audit has been performed.

## References
1. M. Guéneau, S. N. Majumdar and G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436v1, first public 2026-02-09, https://arxiv.org/abs/2602.08436.
2. F. J. Sevilla and J. A. Meléndez Mora, *Nonequilibrium statistics of harmonically trapped run-and-tumble particles: An exact convolution approach*, arXiv:2608.21781v1, first public 2026-08-22, https://arxiv.org/abs/2608.21781.
3. A. Sun, F. Ye and J. Z. Y. Chen, *Run-and-tumble particles in a harmonic external field: constructing the solution of the Fokker–Planck equation from the equations of motion*, arXiv:2610.24961v1, first public 2026-10-18, https://arxiv.org/abs/2610.24961.
4. *A sharp dimension-seven threshold for the quartic time arrow of trapped run-and-tumble motion*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-dimension-seven-threshold-for-the-quartic-time-arrow-of--0d6063747558.
5. *Four-time sign fingerprints of covariance-matched resetting, Gaussian, and telegraph baths*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-four-time-sign-fingerprints-of-covariance-matched-resetting-gaus--c69dc0d762a5.
6. *A fourth-order arrow of time and lag-sign reversal in a harmonically filtered resetting Brownian bath*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-fourth-order-arrow-of-time-and-lag-sign-reversal-in-a-harmonic--2d5b968bafd9.
