# Quadratic close-packing correlation length in an anchored hard-rod crystal

## Finding

For the one-dimensional anchored hard-rod crystal of [1], let the rod diameter be \(\sigma>0\), the accessible width of each well be \(0<\delta<\sigma\), and the lattice spacing be \(\ell=\sigma+d\) with \(d>0\). Assume precisely one rod per well, with nearest-neighbor nonoverlap and the thermodynamic limit taken at fixed \(d\) before \(d\downarrow0\). Let \(\lambda_0(d)>|\lambda_1(d)|\) be the two largest, in modulus, nonzero eigenvalues of the infinite-volume transfer operator

\[
(K_df)(x)=\int_0^\delta \mathbf 1_{\{y\ge x-d\}} f(y)\,dy,\qquad 0\le x\le\delta.
\]

Then the eigenvalues can be chosen positive near close packing and obey the **joint sharp asymptotics**

\[
\lambda_0(d)=ed\left[1-\frac{\pi^2}{2}\left(\frac d\delta\right)^2+o(d^2/\delta^2)\right],\quad
\lambda_1(d)=ed\left[1-2\pi^2\left(\frac d\delta\right)^2+o(d^2/\delta^2)\right].
\]

Consequently, the lattice-site correlation length defined by \(\xi(d)^{-1}=\log(\lambda_0(d)/|\lambda_1(d)|)\) has the **quadratic close-packing law**

\[
\boxed{\lim_{d\downarrow0}\left(\frac d\delta\right)^2\xi(d)=\frac{2}{3\pi^2}.}
\]

The configurational reduced free energy per particle also has the two-term correction

\[
-\log\lambda_0(d)=-1-\log d+\frac{\pi^2}{2}\left(\frac d\delta\right)^2+o(d^2/\delta^2),
\]

in units where the positional integration measure is measured in fixed length units. The conclusion is an infinite-volume, close-packing asymptotic, not a finite-chain mixing-time assertion.

## Assumptions and scope

Coordinates are measured relative to the left edge of each interval, so the hard-core constraint between consecutive rods is \(y\ge x-d\). Set \(\varepsilon=d/\delta\). The model is purely equilibrium configurational and its spectral correlation length is measured in numbers of lattice spacings. \(\delta\) is fixed while \(d\) tends to zero. The indicated coefficient is dimensionless. Every statement about eigenvalues concerns the compact integral operator on \(L^2([0,\delta])\), not an approximate finite-mesh matrix.

## Proof

**1. Exact reduction to a centered killed walk.** Rescale the interval to \([0,1]\). With \((S_\varepsilon g)(x)=e^{-x/\varepsilon}g(x)\), direct substitution gives

\[
\frac{S_\varepsilon^{-1}K_dS_\varepsilon}{ed}=P_\varepsilon,
\quad (P_\varepsilon g)(x)=\int_0^1 \frac{e^{-1-(y-x)/\varepsilon}}{\varepsilon}\mathbf1_{\{y\ge x-\varepsilon\}}g(y)\,dy.
\]

Here the rescaled version of \(K_d\) includes its Jacobian factor \(\delta\), and \(\delta\varepsilon=d\). The integral is exactly the one-step transition operator of a random walk with increments \(\varepsilon(E-1)\), \(E\sim\mathrm{Exp}(1)\), killed upon leaving \([0,1]\). Its increments have mean zero, variance \(\varepsilon^2\), and exponential moments near zero. The similarity is bounded and invertible for each fixed \(\varepsilon>0\), though not uniformly so as \(\varepsilon\to0\). Eigenvalue ratios therefore agree exactly.

**2. Reality and positivity of the nonzero spectrum.** For any increasing sampled \(x_i\) and \(y_j\), each row of \(\mathbf1_{\{y_j\ge x_i-\varepsilon\}}\) is a terminal string of ones, and the row cutoffs are increasing. Every square minor is either zero or nonnegative (the nested-row/Ferrers-matrix determinant property). Multiplication by positive row and column factors retains total nonnegativity. Positive quadrature discretizations therefore give totally nonnegative finite matrices, whose eigenvalues are all nonnegative real. Their operators converge in Hilbert--Schmidt norm to \(P_\varepsilon\); isolation of each nonzero compact-operator spectral point implies every nonzero eigenvalue is real and nonnegative. The walk has a uniform positive probability of jumping beyond the right boundary in one step, so \(\|P_\varepsilon\|_{\infty}<1\); hence all eigenvalues lie in \([0,1)\).

**3. Diffusive trace limit.** Let \(m_\varepsilon=\lfloor t/\varepsilon^2\rfloor\) for any fixed \(t>0\), taking \(\varepsilon\) small enough that \(m_\varepsilon\ge2\). Its unrestricted \(m\)-step displacement is \(\varepsilon(\Gamma_m-m)\), where \(\Gamma_m\) has the gamma law of shape \(m\) and unit rate. The exact unrestricted return density is

\[
p_{m,\varepsilon}(0)=\frac{m^{m-1}e^{-m}}{\varepsilon\Gamma(m)}\longrightarrow (2\pi t)^{-1/2}.
\]

Write \(q_{m,\varepsilon}(x,y)\) for the density of the walk killed upon exiting the interval. Conditional on total displacement zero (equivalently \(\Gamma_m=m\)), the variables \(E_i/m\) have the exact Dirichlet-\((1,\ldots,1)\) distribution: their partial sums are the ordered statistics of \(m-1\) independent uniform points. Thus at time \(k\varepsilon^2\), the centered bridge is exactly \(\varepsilon(mU_{(k)}-k)\). The uniform quantile-process functional central limit theorem (or its direct derivation by inverting Donsker's empirical uniform process) shows that its linear interpolation converges to a standard Brownian bridge of duration \(t\), since \(m\varepsilon^2\to t\). This exact order-statistic representation supplies a direct bridge-invariance argument without assuming a killed local limit theorem. For each fixed \(x\in(0,1)\), the event that the translated bridge remains inside \((0,1)\) is a continuity set: the Brownian-bridge maximum and minimum have no atoms at either boundary. Therefore

\[
q_{m_\varepsilon,\varepsilon}(x,x)\longrightarrow p_D(t;x,x),
\]

where \(p_D\) is the heat kernel for \(\tfrac12\partial_x^2\) with Dirichlet boundary conditions on \((0,1)\). The diagonal is bounded above by the unrestricted return density \(p_{m_\varepsilon,\varepsilon}(0)\), uniformly in \(x\). Since \(P_\varepsilon\) is Hilbert--Schmidt, its powers of order at least two are trace class. Dominated convergence and the trace identity thus give

\[
\lim_{\varepsilon\to0}\operatorname{tr}(P_\varepsilon^{m_\varepsilon})
=\int_0^1p_D(t;x,x)\,dx
=\sum_{j=1}^\infty e^{-j^2\pi^2t/2}.
\tag{1}
\]

The bridge limit is not an assertion about survival of a *free* Brownian motion; it retains the killing at both endpoints. It is also independent of the half-open endpoint convention, since the walk increments are absolutely continuous.

**4. Extracting individual eigenvalues, including the second.** Enumerate the positive eigenvalues of \(P_\varepsilon\) in decreasing order as \(\mu_1(\varepsilon),\mu_2(\varepsilon),\ldots\), with any zero eigenvalues omitted, and set \(a_{j,\varepsilon}=-\varepsilon^{-2}\log\mu_j(\varepsilon)\). Total nonnegativity from step 2 makes these real and nonnegative. Equation (1) for every \(t>0\), together with the uniform unrestricted-return-density bound for its left side, gives convergence of the Laplace transforms of the locally finite counting measures \(\sum_j\delta_{a_{j,\varepsilon}}\). The elementary Laplace uniqueness principle for positive locally finite measures follows by first restricting to a compact interval using the exponential transform bound, taking subsequential weak limits, and using uniqueness of finite-measure Laplace transforms after multiplying by \(e^{-t_0a}\). The unique limit has exactly one atom at each \(j^2\pi^2/2\). Hence, for each fixed \(j\ge1\),

\[
-\varepsilon^{-2}\log\mu_j(\varepsilon)\longrightarrow\frac{j^2\pi^2}{2}.
\tag{2}
\]

In particular \(\mu_1=1-\pi^2\varepsilon^2/2+o(\varepsilon^2)\) and \(\mu_2=1-2\pi^2\varepsilon^2+o(\varepsilon^2)\). Both exist for all sufficiently small \(\varepsilon\), since their limiting Laplace atoms have positive mass.

**5. Return to thermodynamics.** The exact similarity yields \(\lambda_0=ed\mu_1\) and \(\lambda_1=ed\mu_2\). Therefore

\[
\log(\lambda_0/\lambda_1)=\frac{3\pi^2}{2}\left(\frac d\delta\right)^2+o(d^2/\delta^2).
\]

Taking its reciprocal proves the claimed correlation-length constant. Expanding \(-\log(ed\mu_1)\) proves the free-energy formula. This completes the proof for fixed \(\delta\) and \(\sigma\) under the stated limits.

## Verification

The accompanying `check.py` independently constructs the **killed, centered-exponential** transition matrix by analytically integrating its transition density over spatial cells; it does not use the source paper's polynomial root formula. It computes the top two eigenvalues at several approach-to-packing ratios and compares \(\xi/(\delta/d)^2\) with \(2/(3\pi^2)\). It also verifies the exact centered-gamma return-density formula. These finite-dimensional checks test arithmetic and normalization only: step 3 (the conditioned-bridge convergence) and step 4 (individual spectral recovery) supply the infinite-dimensional proof, not numerical extrapolation.

## Relationship to prior work

[1] derives the exact hard-rod transfer kernel, its finite-regime polynomial eigenvalue formulas, the site correlation-length definition, and the local cosine-squared profile at close packing. Its explicit correlation-length asymptotic concerns the *low-density interaction onset*; the present result instead quantifies the opposite, close-packing endpoint by a new killed-random-walk spectral limit. [2] and [3] provide related conditional random-walk limit-theorem context, but neither concerns the hard-rod transfer spectrum or its sharp coefficient. The statement is a specialization of standard diffusion spectral behavior only **after** the non-obvious exponential similarity, killing boundary treatment, and identification of the first two eigenvalues of the non-selfadjoint transfer operator. The searched literature did not locate an equivalent sharp constant for this anchored model.

## Limitations

The result is for a one-dimensional crystal with exactly one rod per well, no hopping between wells, fixed well width, nearest-neighbor hard core, and the thermodynamic limit taken first. It does not cover vacancies, soft potentials, changing well width, or arbitrary thermodynamic limit ordering. The leading constant is not a statement of finite-\(d\) error bounds. Numerical discretization is only a supplementary check. Full novelty priority is subject to unindexed and implicit prior coverage; independent external review has not been performed.

## References

[1] S. Mizani, S. Varga, M. Oettel and P. Gurin, *An infinite sequence of higher order Ehrenfest transitions in a one-dimensional crystal* (HTML manuscript title *From second to infinite order: Ehrenfest transitions in a one-dimensional hard-sphere crystal under compression*), arXiv:2610.26371v1 (first submitted 19 October 2026). https://arxiv.org/abs/2610.26371 ; https://arxiv.org/html/2610.26371v1

[2] F. Caravenna and L. Chaumont, *An invariance principle for random walk bridges conditioned to stay positive*, Electronic Journal of Probability 18 (2013), no. 60. https://arxiv.org/abs/1204.6148

[3] I. Grama and H. Xiao, *Conditioned local limit theorems for random walks on the real line*, arXiv:2110.05123 (2021). https://arxiv.org/abs/2110.05123
