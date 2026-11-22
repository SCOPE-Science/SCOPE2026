# Sharp resolution-gauge limit classification for positive gain–loss time steps

## Finding

**Theorem (complete resolution-gauge phase diagram).** Let \(d\ge1\), \(T>0\), \(\kappa_i>0\), and \(a_i>0\) for \(i=1,\dots,d\). Fix any positive denominator function \(\phi(h)=h+O(h^2)\) as \(h\downarrow0\). For every \(N\in\mathbb N\), take \(h=T/N\) and arbitrary nonnegative constants \(\alpha_{i,h}\), which may depend on the resolution. Define the gain and loss functions
\[
G_{i,h}(x)=\alpha_{i,h}x_i,\qquad L_{i,h}(x)=\kappa_i+\alpha_{i,h}.
\]
They are nonnegative on the positive cone, and *at every resolution* define exactly the same diagonal physical differential equation \(\dot x_i=G_{i,h}(x)-L_{i,h}(x)x_i=-\kappa_i x_i\) with \(x_i(0)=a_i\).

Apply the nonstandard positive update
\[
X_{i,n+1}=\frac{X_{i,n}+\phi(h)G_{i,h}(X_n)}{1+\phi(h)L_{i,h}(X_n)},\quad X_{i,0}=a_i.
\]
Let
\[
q_{i,h}=\frac1{1+h\alpha_{i,h}}\in(0,1].
\]
There are constants \(C_i\) independent of *all* offsets \(\alpha_{i,h}\) and of \(N\), such that for sufficiently small \(h\)
\[
\max_{0\le n\le N}\left|X_{i,n}-a_i e^{-\kappa_i q_{i,h}nh}\right|\le C_i h.
\]
Thus the piecewise-constant trajectories (using the left mesh value on each half-open cell and the computed endpoint at \(T\)) have precisely the subsequential uniform limits
\[
x_i^{(\theta)}(t)=a_i e^{-\kappa_i\theta_i t},\qquad \theta=(\theta_1,\ldots,\theta_d)\in[0,1]^d,
\]
where \(\theta\) ranges over accumulation points of the vector \((q_{1,h},\ldots,q_{d,h})\) as \(h=T/N\downarrow0\). **Every** \(\theta\in[0,1]^d\) is realizable by nonnegative resolution-dependent gain–loss functions encoding the exact same ODE.

For any fixed \(T>0\), convergence to the true physical solution \(x_i(t)=a_ie^{-\kappa_i t}\) for all coordinates is therefore **equivalent** to the sharp condition
\[
\boxed{\ h\alpha_{i,h}\longrightarrow0\quad\text{for every }i\ }. 
\]
In particular, keeping the physical vector field exactly correct and maintaining strict numerical positivity at every step do not ensure consistency under resolution-dependent representations. At the scalar choice \(\kappa=a=T=1\), \(\phi(h)=h\), the gauges \(\alpha_h=h^{-1}\) and \(\alpha_h=h^{-2}\) give limiting trajectories \(e^{-t/2}\) and \(1\), respectively, instead of \(e^{-t}\).

## Assumptions and scope

The result is for exact arithmetic, positive initial data, positive fixed diagonal decay rates, integer-mesh steps \(h=T/N\), and nonnegative gain–loss offsets constant in time and state *apart from the linear gain dependence* on \(x_i\). The constant in \(\phi(h)=h+O(h^2)\) is fixed independently of the offsets. No boundedness of the offsets as \(h\to0\) is required. All limits are taken along \(N\to\infty\), and each discrete trajectory is compared at its mesh times; piecewise-constant interpolation differs from its exponential shadow by at most \(O(h)\) because all effective rates are bounded. The theorem is not a claim about every general nonlinear learned flow, coupled equation, or training procedure.

## Proof

**Exact update reduction.** Since the same nonnegative \(\alpha_{i,h}X_{i,n}\) appears as a gain and as part of the loss, the stated update reduces to
\[
X_{i,n+1}=\frac{1+\phi(h)\alpha_{i,h}}{1+\phi(h)(\kappa_i+\alpha_{i,h})}X_{i,n}=\frac{X_{i,n}}{1+\kappa_i h v_{i,h}},\qquad v_{i,h}=\frac{\phi(h)/h}{1+\phi(h)\alpha_{i,h}}.
\]
This makes every multiplier strictly between zero and one, independent of the size of the offset. Set \(z_h=\phi(h)/h=1+O(h)\) and \(u_{i,h}=h\alpha_{i,h}\ge0\). Then the *exact* algebraic identity
\[
v_{i,h}-q_{i,h}=\frac{z_h-1}{(1+z_hu_{i,h})(1+u_{i,h})}
\]
shows \(|v_{i,h}-q_{i,h}|\le |z_h-1|=O(h)\) uniformly for all offsets. For all sufficiently small steps \(0<v_{i,h}\le2\).

**Uniform finite-horizon shadow estimate.** For \(y\ge0\) we have \(0\le y-\log(1+y)\le y^2/2\). Therefore, for \(0\le n\le N\),
\[
\left|n\log(1+\kappa_i h v_{i,h})-n\kappa_i hq_{i,h}\right|
\le n\kappa_i h|v_{i,h}-q_{i,h}|+\frac n2\kappa_i^2h^2v_{i,h}^2
\le \left(T\kappa_i K+2T\kappa_i^2\right)h
\]
for a fixed \(K\ge\sup_{h\text{ small}}|z_h-1|/h\). Both negative exponents are nonpositive; the exponential map is 1-Lipschitz on the nonpositive half-line. Multiplying by \(a_i\) proves the asserted \(O(h)\) error bound with \(C_i=a_i(T\kappa_i K+2T\kappa_i^2)\). Linear interpolation or constant interpolation changes the exponential shadow by at most \(2a_i\kappa_i h\) on each mesh cell, so the convergence statement holds in the uniform norm on \([0,T]\).

**Completeness and sharp consistency criterion.** The vectors \(q_h\) lie in compact \([0,1]^d\). Along a convergent subsequence \(q_h\to\theta\), the uniform shadow bound and continuity of \(e^{-\kappa_i q_ht}\) give uniform convergence to the stated trajectory. Conversely, any uniformly convergent subsequence of numerical trajectories has a convergent sub-subsequence of \(q_h\), so it has exactly one of the stated limits. Every \(\theta_i\in(0,1]\) is realized by \(\alpha_{i,h}=(1-\theta_i)/(\theta_i h)\); \(\theta_i=0\) is realized by \(\alpha_{i,h}=h^{-2}\). Such coordinate choices are independent. The true solution is attained for the whole sequence if \(q_{i,h}\to1\), equivalently \(h\alpha_{i,h}\to0\). Conversely, if the numerical solution converges to the true solution at the positive terminal time \(T\), the shadow bound implies \(e^{-\kappa_iT q_{i,h}}\to e^{-\kappa_iT}\). Strict injectivity of the exponential on \(\mathbb R\) and \(\kappa_iT>0\) imply \(q_{i,h}\to1\), proving necessity.

## Verification

The standalone `checker.py` verifies the rational update and gauge identity using exact rational arithmetic and checks representative phase limits and strict positivity. A finite calculation cannot establish the infinite-resolution assertion; the proof supplies the uniform estimates and full cluster-point argument. Run with `python checker.py` using only Python's standard library.

## Relationship to prior work

Zinihi, Ehrhardt and Sidi Ammi introduce the positive gain–loss NSFD update, equation (3), and prove first-order consistency for a *fixed* smooth representation, not for resolution-dependent representations [1]. The present result concerns an independent mathematical question: exact identification of every limit when different gain–loss pairs realize the same physical vector field but grow with inverse resolution. The fixed-representation theorem is recovered as the case \(h\alpha_{i,h}\to0\); it does not imply the failure or classification outside this regime. The older general literature on positive nonstandard discretization supplies context, not this limit classification [2]. An analogous but mathematically distinct loss of representation invariance has been described for finite-correction Patankar deferred correction with large face-flux offsets at fixed step [3]. A separate split exponential–Euler two-time identification theorem concerns two observed time maps and two real reaction parameters [4], not the nonnegative gain–loss gauges and complete convergence phase diagram studied here.

## Limitations

The effect depends on allowing the decomposition to vary with resolution. It does **not** contradict the source's established first-order consistency at a fixed representation, nor assert the failure of training algorithms, arbitrary nonlinear flows, or uniformly bounded offset families. The classification applies to positive diagonal linear dynamics and the specified rational update, with a fixed admissible denominator function. General nonlinear gauge effects remain unresolved. Historical priority outside the inspected sources is not independently certified.

## References

1. A. Zinihi, M. Ehrhardt, M. R. Sidi Ammi, *Structure-Preserving Neural ODEs via Nonstandard Finite Difference Discretization*, arXiv:2607.10858v1 (first public 2026-07-12), https://arxiv.org/abs/2607.10858 .
2. R. E. Mickens, *Nonstandard finite difference schemes for differential equations*, Journal of Difference Equations and Applications (2002), https://doi.org/10.1080/1023619021000000807 .
3. *A flux-offset gauge-stalling law for finite-correction modified Patankar deferred correction*, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-flux-offset-gauge-stalling-law-for-finite-correction-modified--8a12fdc5c04c .
4. *Two-time aliases, a cubic third-time cusp, and opposite long-horizon signs for split exponential–Euler maps*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-two-time-aliases-a-cubic-third-time-cusp-and-opposite-long-horiz--723be3ffe5ad .
