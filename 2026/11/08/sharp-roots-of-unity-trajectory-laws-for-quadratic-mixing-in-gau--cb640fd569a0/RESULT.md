# Sharp roots-of-unity trajectory laws for quadratic mixing in Gaussian Hamiltonian Monte Carlo

## Finding

For each integer \(K\ge 1\), consider ideal Hamiltonian Monte Carlo targeting the centered Gaussian whose independent modal frequencies are exactly \(1,2,\ldots,K\). Each transition refreshes all Gaussian momenta independently and uses a common fresh trajectory duration \(T\in[0,\pi]\), drawn independently from an arbitrary law \(\mu\) satisfying the expected-duration budget \(\mathbb E_\mu T=\pi/2\). For nonzero centered quadratic position observables, measure stationary integrated autocorrelation per HMC transition, taking the maximum over all such observables.

**Sharp minimax law.** The smallest possible worst-observable integrated autocorrelation is

\[
\boxed{\inf_{\mu:\,\mathbb E T=\pi/2}\ \sup_{g\in\mathcal Q\setminus\{0\}}\tau_\mu(g)=\frac{3K-1}{K+1}.}
\]

It is attained by putting probability \(1/K\) on each of the \(K\) durations

\[
T_m=\frac{m\pi}{K+1},\qquad m=1,\ldots,K.
\]

There is an exact classification of **all** minimizing distributions. Write \(N=K+1\). Every minimizer is supported on these \(K\) durations and has masses \(p_m=1/K+\delta_m\) satisfying

\[
\delta_{N-m}=-\delta_m,\qquad |\delta_m|\le\frac1K,\qquad
\sum_{1\le m<N/2}(N-2m)\delta_m=0.
\]

Conversely, each such mass vector is optimal. The uniform time law is the unique minimizer for \(K\le3\). For every \(K\ge4\), there is a continuum of nonuniform, generally asymmetric minimizing laws.

## Assumptions and scope

The target probability measure on \(\mathbb R^K\) is

\[
\pi(dx)\propto\exp\!\left(-\frac12\sum_{j=1}^Kj^2x_j^2\right)dx.
\]

The Hamiltonian is \(H(x,p)=\tfrac12\sum_{j=1}^K(j^2x_j^2+p_j^2)\). Its Hamiltonian evolution is integrated **exactly** (not by a finite-step numerical integrator). Each Markov transition draws a fresh momentum \(P\sim N(0,I_K)\) and a fresh duration \(T\sim\mu\), independently of the current position and of all earlier draws, evolves for time \(T\), and discards the momentum. The duration law is any Borel probability on \([0,\pi]\) with \(\mathbb E T=\pi/2\).

Let \(Y_j=jX_j\). Under the stationary target the \(Y_j\) are independent standard normals. The space \(\mathcal Q\) is all centered, real, degree-two polynomials of position, equivalently the span of \(Y_j^2-1\) and \(Y_iY_j\) for \(1\le i<j\le K\). For a stationary scalar observable \(g\) with nonzero variance define

\[
\tau_\mu(g)=1+2\sum_{\ell=1}^\infty
\frac{\operatorname{Cov}_\pi(g(X_0),g(X_\ell))}{\operatorname{Var}_\pi(g(X_0))},
\]

when the series converges; assign value \(+\infty\) to a mode with perfect persistence. Here the performance measure counts **transitions**, not gradient evaluations, wall-clock work, or physical integration time; the expected integration duration is fixed separately by the constraint.

## Proof

**Step 1: exact quadratic spectrum.** Hamiltonian evolution and full momentum refresh give the normalized coordinate update

\[
Y'_j=\cos(jT)Y_j+\sin(jT)\xi_j,\quad
\xi_1,\ldots,\xi_K\overset{\mathrm{iid}}\sim N(0,1).
\]

This preserves the independent standard-normal target, for every fixed duration and hence for every mixing law. Taking conditional expectation on the quadratic basis shows that the Markov operator acts diagonally on \(\mathcal Q\), with eigenvalues

\[
\rho_j=\mathbb E_\mu\cos^2(jT)\quad\text{on }Y_j^2-1,
\qquad
\gamma_{ij}=\mathbb E_\mu[\cos(iT)\cos(jT)]
\quad\text{on }Y_iY_j.
\]

Since \(|\gamma_{ij}|\le\sqrt{\rho_i\rho_j}\le\rho_*:=\max_j\rho_j\), the largest eigenvalue on \(\mathcal Q\) is exactly \(\rho_*\ge0\). When \(\rho_*<1\), each eigenmode with multiplier \(\lambda\) has integrated autocorrelation \((1+\lambda)/(1-\lambda)\); orthogonality of the Gaussian quadratic basis makes any observable's integrated autocorrelation a convex combination of those eigenmode values. The function is strictly increasing in \(\lambda<1\). Hence

\[
\sup_{g\in\mathcal Q\setminus\{0\}}\tau_\mu(g)
=\frac{1+\rho_*}{1-\rho_*}.
\]

If \(\rho_*=1\), the corresponding diagonal quadratic mode is invariant and the supremum is infinite. Consequently it suffices to minimize \(\rho_*\).

**Step 2: sharp universal lower bound.** Put \(c_j=\mathbb E_\mu\cos(2jT)=2\rho_j-1\), \(1\le j\le K\), and \(N=K+1\). The nonnegative Fejér-sum identity is

\[
0\le \mathbb E_\mu\!\left|\sum_{a=0}^{N-1}e^{2iaT}\right|^2
=N+2\sum_{j=1}^{K}(N-j)c_j
\le N+NK\max_{1\le j\le K}c_j.
\]

Therefore \(\max_jc_j\ge-1/K\) and

\[
\rho_*\ge\frac{K-1}{2K},\qquad
\sup_g\tau_\mu(g)\ge\frac{3K-1}{K+1}.
\]

The proof uses no assumption on the time law beyond being a probability; therefore it also applies under the mean-duration constraint.

**Step 3: attainable bound at the required cost.** Let \(\mu_*\) place equal masses on \(T_m=m\pi/N\), \(m=1,\ldots,N-1\). Its mean is \(\pi/2\), and the roots-of-unity identity gives, for every \(j=1,\ldots,N-1\),

\[
\mathbb E_{\mu_*}e^{2ijT}=\frac1K\sum_{m=1}^{N-1}e^{2\pi ijm/N}=-\frac1K.
\]

Thus every \(c_j=-1/K\) and every \(\rho_j=(K-1)/(2K)\), attaining the lower bound. The preceding spectral estimate also handles every mixed covariance observable.

**Step 4: classify all equality laws.** Because all Fejér weights \(N-j\) are positive, equality at \(\max_jc_j=-1/K\) forces \(c_j=-1/K\) for all \(j\), and the expected squared modulus in Step 2 is zero. The geometric sum \(\sum_{a=0}^{N-1}z^a\) vanishes precisely at the nontrivial \(N\)-th roots of unity. Since \(T\in[0,\pi]\), its zero set is exactly \(\{m\pi/N:1\le m\le N-1\}\). This proves that every minimizing law is supported on the stated grid.

For its masses \(p_m\), use the even symmetry \(q_m=(p_m+p_{N-m})/2\). Cosine moments of \(p\) are the full discrete Fourier coefficients of the symmetric vector \(q\). The conditions \(c_j=-1/K\) for all nonzero indices, together with normalization and \(q_0=0\), give by discrete Fourier inversion \(q_m=1/K\) for every \(m\ne0\). Equivalently, \(p_m=1/K+\delta_m\) with \(\delta_{N-m}=-\delta_m\); positivity of probabilities is exactly \(|\delta_m|\le1/K\). The budget \(\sum_mp_m m\pi/N=\pi/2\) then becomes

\[
\sum_{1\le m<N/2}(N-2m)\delta_m=0.
\]

Every listed condition is necessary; reversing the reasoning establishes sufficiency. For \(N\le4\) the one possible independent antisymmetric displacement (if any) is killed by the single nonzero mean constraint, so the optimum is unique. For \(N\ge5\) choose, with sufficiently small nonzero \(u\),

\[
\delta_1=u,\quad\delta_2=-\frac{N-2}{N-4}u,\quad
\delta_{N-1}=-u,\quad\delta_{N-2}=\frac{N-2}{N-4}u,
\]

and all other \(\delta_m=0\). These are distinct nonuniform optimal laws, proving the claimed continuum.

## Verification

Run `python3 verify.py` using the Python standard library. The checker tests the exact rational mean constraint, the predicted cosine-square eigenvalues for \(K=1,\ldots,18\), all mixed quadratic multipliers within those sizes, the Fejér identity at 17 deterministic off-grid times per size, and explicit nonuniform equal-cost minimizers for \(K=4,\ldots,18\). The recorded output is in `verification_output.txt`. These finite checks are **not** a proof for all dimensions; Steps 1--4 supply the analytic universal argument.

In the simplest nontrivial case \(K=2\), the optimum uses times \(\pi/3,2\pi/3\) with equal probabilities; it has \(\rho_*=1/4\) and worst quadratic integrated autocorrelation \(5/3\). For \(K=4\), perturbing the four equal masses by \((u,-3u,3u,-u)\) for \(|u|<1/12\) gives nonuniform alternative optima.

## Relationship to prior work

The ideal harmonic-oscillator HMC coordinate update and the motivation for long randomized trajectory lengths appear in Apers, Gribling and Szilágyi (2022, arXiv:2209.12771v1), in particular their Sections 2.3 and 3. Their finite time-grid construction controls modal resonance and mixing/total-variation convergence rather than solving the fixed-mean, all-centered-quadratics stationary-autocorrelation minimax problem here. Hoffman, Radul and Sountsov (2021) use squared-state autocorrelations to motivate adaptive integration-length tuning but do not give this finite-frequency optimal-law classification. Wang and Wibisono (2022) optimize a deterministic, nonidentically distributed Chebyshev sequence for a different metric, not one iid trajectory-time law. Bou-Rabee and Sanz-Serna (2015 preprint) study exponentially randomized HMC durations rather than this budgeted extremum. The underlying Fejér nonnegativity identity and Fourier inversion are classical, not claimed as novel mathematical tools.

The specific contribution assessed here is their combination into a sharp full-quadratic HMC design theorem, its minimax value, complete equality cases and the uniqueness-to-nonuniqueness transition at four frequencies. Historical or unindexed exact overlap remains possible; no claim of priority or independent confirmation is made.

## Limitations

This is an exact-integrator result for the artificial but natural arithmetic Gaussian spectrum and full momentum refresh. It makes no statement about approximate symplectic integration, accept/reject, nonquadratic targets, general frequency sets, the total variation mixing time, nonquadratic observables, or gradient-evaluation efficiency. Although mean duration is fixed, full ideal integration is treated as an oracle; per-transition integrated autocorrelation is not a cost-normalized computational complexity guarantee. The probability laws described here are the complete minimizers **only within the stated duration interval and mean constraint**. Novelty relative to all possible historical research is not independently established.

## References

1. S. Apers, S. Gribling, and D. Szilágyi, *Hamiltonian Monte Carlo for efficient Gaussian sampling: long and random steps* (first arXiv version, 2022-09-26), https://arxiv.org/abs/2209.12771, Sections 2.3 and 3.
2. M. Hoffman, A. Radul, and P. Sountsov, *An Adaptive-MCMC Scheme for Setting Trajectory Lengths in Hamiltonian Monte Carlo*, AISTATS/PMLR 130 (2021), https://proceedings.mlr.press/v130/hoffman21a.html, Sections 2.1--2.2.
3. J.-K. Wang and A. Wibisono, *Accelerating Hamiltonian Monte Carlo via Chebyshev Integration Time* (arXiv first version, 2022-07-05), https://arxiv.org/abs/2207.02189.
4. N. Bou-Rabee and J. M. Sanz-Serna, *Randomized Hamiltonian Monte Carlo* (arXiv first version, 2015-11-30), https://arxiv.org/abs/1511.09382.
