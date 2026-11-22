# A sharp phase-sign threshold for shifted convex-splitting BDF2 on two Cahn–Hilliard cells

## Finding
Consider the two-cell zero-mean Cahn–Hilliard phase equation and the shifted convex-splitting BDF2 chemical-potential force of Gu and Wang. For any \(\beta>1\), define
\[
t_c(\beta)=\frac{\sqrt{1+4/(\beta-1)}-1}{4}.
\]
With the exact semidiscrete one-step starter, there is \(\delta(\beta,t)>0\) such that whenever \(0<a_0<\delta\), all numerical amplitudes converge to zero, and
\[
\begin{cases}
a_n>0\quad\text{for every }n\ge0,&0<t\le t_c(\beta),\\
a_n>0\text{ infinitely often and }a_n<0\text{ infinitely often},&t>t_c(\beta).
\end{cases}
\]
Here \(t=\lambda\tau>0\) is the dimensionless timestep and \(\beta=\varepsilon^2\lambda>1\). Above the threshold, the indefinite sign reversals persist for **every sufficiently small nonzero pair of starting amplitudes**. No sign reversals occur in the corresponding exact semidiscrete phase trajectory started at a positive amplitude. The theorem is a near-equilibrium threshold, not a classification of arbitrary large histories.

For two unit-spaced Neumann cells \(\lambda=2\). At \(\varepsilon^2=1\), the threshold is \(\tau_c=(\sqrt5-1)/8\); larger fixed timesteps create an indefinitely oscillatory, decaying phase component from arbitrarily small positive data, despite the method's modified-energy dissipation.

## Assumptions and scope
Let \(L\) be the two-cell Neumann graph Laplacian, with \(L(1,-1)^T=\lambda(1,-1)^T\), \(\lambda>0\). We examine the zero-mean phase-only (zero-transport) specialization of the published time-discrete Cahn–Hilliard scheme. Set \(\phi^n=(a_n,-a_n)\), \(\beta=\varepsilon^2\lambda>1\), \(k=\beta-1\), and \(t=\lambda\tau\). The semidiscrete initial-value problem is
\[
\dot a=-\lambda(ka+a^3),\qquad a(0)=a_0>0.
\]
It has the positive exact solution \(a(s)=a_0e^{-k\lambda s}/\sqrt{1+a_0^2(1-e^{-2k\lambda s})/k}\), and its energy, up to an additive constant, is \(ka^2+a^4/2\), strictly convex for \(k>0\). Initialize the multistep method with
\[
a_1=\frac{a_0e^{-kt}}{\sqrt{1+a_0^2(1-e^{-2kt})/k}}.
\]
The exact starter is used to isolate the time-discretization effect; it is not claimed to be the specific numerical startup adopted in every implementation of the source method.

Let \(\chi(v,w)=(v^2+w^2)(v+w)/4\), \(A=(3a_{n+1}-a_n)/2\), and \(B=(3a_n-a_{n-1})/2\). The **unique** numerical successor solves
\[
(3+2\beta t)a_{n+1}-(4+4t)a_n+(1+2t)a_{n-1}+2t\chi(A,B)=0.
\tag{1}
\]
This is the two-cell antiphase reduction of the phase and chemical-potential equations with the original shifted arguments; it is not generic unmodified BDF2 applied to a scalar decay equation.

## Proof
**Exact reduction and uniqueness.** In the published method, the chemical potential is \(\mu^{n+1}=\varepsilon^2L\phi^{n+1}+\chi(\phi^{\dagger,n+1},\phi^{\dagger,n})-\phi^{*,n+1}\), with \(\phi^{\dagger,n+1}=(3\phi^{n+1}-\phi^n)/2\), \(\phi^{\dagger,n}=(3\phi^n-\phi^{n-1})/2\) and \(\phi^{*,n+1}=2\phi^n-\phi^{n-1}\). The phase equation is \(D_{2\tau}\phi^{n+1}=-L\mu^{n+1}\). Oddness of \(\chi\) preserves the antiphase subspace, and multiplication by \(2\tau\) gives (1). With \(z=a_{n+1}\), the derivative of its left side is
\[
3+2\beta t+3t\,\frac{3A^2+2AB+B^2}{4}>0.
\]
The polynomial left side tends to opposite infinities as \(z\to\pm\infty\); hence every pair of real previous states has exactly one real successor. Analytic implicit-function theory gives an analytic, odd two-dimensional update \(T\) near the origin.

**Linear dynamics.** The cubic term is third-order in the two-state history. Thus the linearization at zero has characteristic polynomial
\[
P(r)=(3+2\beta t)r^2-(4+4t)r+(1+2t),
\]
with discriminant
\[
\Delta=4\bigl(1-2kt-4kt^2\bigr).
\]
The unique positive zero of \(\Delta\) is \(t_c(\beta)\). For all \(t>0\), both characteristic roots are strictly within the unit disk: if \(d=3+2\beta t\), the normalized recurrence has sum \(s=(4+4t)/d\) and product \(p=(1+2t)/d\) satisfying
\[
1-s+p=\frac{2kt}{d}>0,\qquad 1-p=\frac{2+2kt}{d}>0,\qquad 1+s+p>0.
\]
These are the strict quadratic Schur inequalities. Hence the nonlinear origin is locally exponentially attracting for every timestep, on both sides of the sign threshold.

**The real-root region including the double-root boundary.** When \(0<t\le t_c\), write \(\delta_1=kt\). The discriminant condition implies \(\delta_1(2+4t)\le1\), so \(0<\delta_1<1/2\). Let \(r_-\le r_+\) denote the positive real roots (both below one), and let \(s_0=e^{-\delta_1}\), the exact starter's derivative at zero. The root midpoint is \(2(1+t)/d\). Direct algebra gives
\[
(1-\delta_1)d-2(1+t)=1-\delta_1(1+2t)-2\delta_1^2>0,
\]
because \(\delta_1(1+2t)\le1/2\) and \(2\delta_1^2<1/2\). As \(s_0>1-\delta_1\), it follows that \(s_0>(r_-+r_+)/2\), and in particular \(s_0>r_-\). The linear solution initialized by \(b_0=1,b_1=s_0\) is, for distinct roots,
\[
b_n=A_0r_+^n+(1-A_0)r_-^n,\qquad A_0=\frac{s_0-r_-}{r_+-r_-}>0.
\]
Thus \(b_n\ge\min(1,A_0)r_+^n>0\) uniformly in \(n\). At the repeated root \(r=r_+=r_-\), the solution is
\[
b_n=r^n\left[1+n\left(\frac{s_0}{r}-1\right)\right],
\]
with \(s_0>r\), hence \(b_n\ge c(n+1)r^n\) for some \(c>0\).

To transfer these bounds to the nonlinear trajectory, write the two-state map as \(T(v)=Jv+N(v)\) where \(N(v)=O(\|v\|^3)\). Since the spectral radius \(R<1\), choose \(q\) with \(R<q<\min(1,R^{1/3})\); a suitable equivalent norm gives \(\|v_n\|\le C a_0q^n\) for all sufficiently small \(a_0\). The exact nonlinear starter differs from \(a_0s_0\) by \(O(a_0^3)\). Duhamel's formula and the convergent geometric convolution \(\sum_{j\ge0}(q^3/R)^j\) give
\[
|a_n-a_0 b_n|\le C'a_0^3R^n
\]
for distinct roots, and \(\le C'a_0^3(n+1)R^n\) at the double root. The derived positive linear lower bounds therefore dominate the nonlinear error simultaneously for all \(n\) whenever \(a_0>0\) is small enough. This proves strict positivity for all time indices, including equality at the discriminant boundary.

**The complex-root region.** If \(t>t_c\), the eigenvalues of \(J\) are \(Re^{\pm i\theta}\) for some \(0<R<1\) and \(0<\theta<\pi/2\). A real linear coordinate change puts the nonlinear map in the form
\[
w_{n+1}=R\mathcal R_\theta w_n+O(\|w_n\|^3),
\]
where \(\mathcal R_\theta\) is planar rotation. For sufficiently small nonzero starting histories, the trajectory decays geometrically; local invertibility (\(\det J=R^2>0\)) ensures \(w_n\ne0\). Its unwrapped polar angle consequently satisfies
\[
\vartheta_n=n\theta+\vartheta_\infty+o(1),
\]
because each angle increment differs from \(\theta\) by \(O(\|w_n\|^2)\), a summable sequence. Every nonzero real linear coordinate, including \(a_n\), is a nonzero projection of \(w_n\). Rotation by \(0<\theta<\pi/2\), whether rational or irrational modulo \(2\pi\), enters each of the two open projection half-circles infinitely often; for a rational rotation its evenly spaced orbit has gaps strictly below \(\pi\), and for an irrational rotation the orbit is dense. The vanishing angular perturbation preserves infinitely many visits strictly inside both half-circles. Thus \(a_n\) has infinitely many positive and negative terms, while \(a_n\to0\). Exact semidiscrete starts with \(a_0>0\) are nonzero small histories, proving the claimed opposite-sign side of the threshold.

## Verification
The standalone `verify.py` checks the exact cubic reduction's Jacobian, its discriminant and oddness symbolically using SymPy. Numerical tests with SciPy solve the strictly monotone implicit step for five values of \(\beta\) and four relative timesteps per value, checking representative positive histories below and sign reversal above the predicted threshold. Execute `python verify.py` with Python, SymPy and SciPy installed. These finite checks validate algebra and illustrate behavior; the infinite-index classification comes from the analytic proof, not enumeration.

## Relationship to prior work
Gu and Wang [1] introduce the shifted convex-splitting BDF2 force and prove unique solvability, modified-energy dissipation and second-order convergence. Their scheme and cubic force are used unchanged in the two-cell phase specialization. Their inspected introduction, scheme, energy theorem, convergence section and numerical material do not give the present discriminant threshold or the nonlinear all-time sign trichotomy. Their modified energy remains nonincreasing; the sign phenomenon does not contradict their theorem.

Hundsdorfer, Ruuth and Spiteri [2] study monotonicity restrictions for classical linear multistep methods, including standard BDF2. A published calculation of the first negative iterate for standard backward-Euler-started scalar BDF2 [3] establishes a different threshold and phase delay. Here the linearized polynomial has different, shifted coefficients from the extrapolated concave term, and the result additionally handles an intrinsically nonlinear convex-splitting force and an exact phase-ODE starter for every time index. The general qualitative possibility of BDF sign oscillation is prior context, not claimed novel. Other convex-splitting BDF2 schemes [4,5] have distinct nonlinear forces and stability hypotheses; no equivalence establishing this exact threshold was found. This is a best-knowledge literature comparison, not a proof of historical priority.

## Limitations
The threshold concerns sufficiently small antiphase amplitudes in a two-cell Neumann phase subsystem, with fixed steps and the stated starter; it is not a universal maximum-principle threshold for the full PDE, arbitrary phase data, arbitrary velocity, or variable steps. The scheme remains locally stable above threshold, and energy dissipation concerns the **modified** BDF2 energy, not necessarily monotonicity of physical energy at each individual step. The equality case is established only for the specified semidiscrete starter, not every positive two-state history. Relevant earlier specialized BDF2 oscillation literature may contain related reductions not identified in the accessible sources; historical priority is not independently established.

## References
1. X. Gu and Q. Wang, *An Energy-Stable Implicit Convex-Splitting BDF2 Scheme for the Cahn–Hilliard–Navier–Stokes Equations*, arXiv:2606.04204v1, first publicly posted 2 June 2026. https://arxiv.org/abs/2606.04204
2. W. Hundsdorfer, S. J. Ruuth and R. J. Spiteri, *Monotonicity-Preserving Linear Multistep Methods*, CWI Report MAS-R0210 (2002), https://ir.cwi.nl/pub/4231/04231D.pdf, later SIAM J. Numer. Anal. 41 (2003), 605–623.
3. *Exact delayed sign loss just beyond BDF2's positivity boundary*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-delayed-sign-loss-just-beyond-bdf2-s-positivity-boundary--cf66315c5a14
4. W. Chen, X. Wang, Y. Yan and Z. Zhang, *A Second Order BDF Numerical Scheme with Variable Steps for the Cahn–Hilliard Equation*, SIAM J. Numer. Anal. 57 (2019), 495–525, https://doi.org/10.1137/18M1206084.
5. H.-L. Liao, B. Ji, L. Wang and Z. Zhang, *Mesh-robustness of an energy stable BDF2 scheme with variable steps for the Cahn-Hilliard model*, arXiv:2102.03731, 2021.
