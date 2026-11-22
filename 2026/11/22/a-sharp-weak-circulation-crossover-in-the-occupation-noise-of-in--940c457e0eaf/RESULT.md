# A sharp weak-circulation crossover in the occupation noise of interacting Ehrenfest urn rings

## Finding

An interacting cyclic urn model can retain the same large-population **instantaneous** Gaussian fluctuations for every clockwise/counterclockwise bias while its **time-averaged** noise is strictly reduced by the magnitude of that bias. More precisely, the hydrodynamic limit of the time-average noise has an explicit nontrivial crossover at directional imbalance of order the reciprocal number of urns. The principal new statement is the finite-ring integrated-noise formula and its sharp hyperbolic-cotangent scaling limit, not the previously established static Gaussian approximation for three or four urns.

For any integer \(M\ge3\), repulsive interaction \(g\ge0\), and bias \(\delta=p-q\in(-1,1)\) with \(p,q>0\), \(p+q=1\), the limiting stationary central-limit field has diagonal lag covariance
\[
 C_M(t)=\frac{1}{M(M+g)}\sum_{k=1}^{M-1}e^{-\gamma_k t}\cos(\omega_k t),\qquad t\ge0,
\]
with
\[
 \gamma_k=\frac{M+g}{2M}\left[1-\cos\left(\frac{2\pi k}{M}\right)\right],\qquad
 \omega_k=\frac{\delta}{2}\sin\left(\frac{2\pi k}{M}\right).
\]
Its long-window sample-mean variance coefficient is
\[
 \mathcal A_M(g,\delta)=\lim_{T\to\infty}T\operatorname{Var}\left(\frac1T\int_0^T Z_i(t)\,dt\right)
 =\frac{2}{M(M+g)}\sum_{k=1}^{M-1}\frac{\gamma_k}{\gamma_k^2+\omega_k^2}.
\]
The coefficient is strictly decreasing as \(|\delta|\) increases in \([0,1)\); however, \(C_M(0)=(M-1)/[M(M+g)]\) does not depend on \(\delta\). In particular
\[
 \mathcal A_M(g,0)=\frac{2(M^2-1)}{3(M+g)^2}.
\]
If \(g_M/M\to\kappa\ge0\) and \(\delta_M=\zeta/M\) for fixed real \(\zeta\), then
\[
 \boxed{\lim_{M\to\infty}\mathcal A_M(g_M,\zeta/M)
 =\frac{2}{(1+\kappa)^2}\frac{u\coth(u)-1}{u^2},\quad
 u=\frac{|\zeta|}{1+\kappa},}
\]
with the right side interpreted continuously at \(u=0\), where it equals \(2/[3(1+\kappa)^2]\). At every fixed nonzero directional imbalance \(\delta\), the distinct asymptotic is
\[
 \mathcal A_M(g_M,\delta)\sim\frac{2}{|\delta|(M+g_M)}.
\]
Consequently, bias of order \(M^{-1}\) is precisely the crossover window between order-one time-average noise and order-\(M^{-1}\) noise in the sequential particle-number, observation-time, and urn-count limits described below.

## Assumptions and scope

Place \(N\ge1\) labeled particles in \(M\) urns arranged on a directed ring, with occupation counts \(n_i\), total \(\sum_i n_i=N\), and fractions \(x_i=n_i/N\). All indices are modulo \(M\). Each particle in urn \(i\) attempts clockwise and counterclockwise motion at respective rates \(p\) and \(q\). A move to neighboring urn \(j\) is accepted with logistic probability
\[
 T_g(x_i,x_j)=\frac{1}{1+\exp[g(x_j-x_i)]}.
\]
Thus the continuous-time chain has transition intensities \(Np x_iT_g(x_i,x_{i+1})\) and \(Nq x_iT_g(x_i,x_{i-1})\). This is an explicit finite-\(N\) Glauber-type discretization of the interacting mean-field urn ring; the closely related energy-difference rule replacing \(g(x_j-x_i)\) by \(g(x_j-x_i+1/N)\) has the same fixed-\(M\) Gaussian limit. Neither version involves transitions between non-neighboring urns.

For every fixed \((M,g,p,q)\), the finite-\(N\) process is irreducible and has a unique stationary distribution. Use the stationary central-limit scaling \(Z_i^{(N)}(t)=\sqrt N[x_i(t)-1/M]\). First let \(N\to\infty\), obtaining stationary \(Z(t)\); then, for this limiting Gaussian process, let the observation window \(T\to\infty\). Only after these two limits is \(M\to\infty\) taken. These statements do not assert a simultaneous uniform limit over \(N,T,M\), nor an exact finite-\(N\) covariance identity.

## Proof

**1. Globally stable deterministic equilibrium.** At large particle number the deterministic flux from urn \(i\) to \(i+1\) is
\[
 J_i=p x_iT_g(x_i,x_{i+1})-q x_{i+1}T_g(x_{i+1},x_i),\qquad \dot x_i=J_{i-1}-J_i.
\]
Let \(u_i=1/M\), \(V(x)=\sum_i(x_i-u_i)^2\), and \(\Delta_i=x_{i+1}-x_i\). The identity \(2T_g(x_i,x_{i+1})=1-\tanh(g\Delta_i/2)\) gives the exact dissipation formula
\[
 \dot V=-\frac12\sum_i\Delta_i^2
 -\sum_i\Delta_i(p x_i+q x_{i+1})\tanh(g\Delta_i/2)
 \le-\frac12\sum_i\Delta_i^2.
\]
Since \(g\ge0\), each term in the second sum is nonnegative. The ring Poincaré inequality \(\sum_i\Delta_i^2\ge2[1-\cos(2\pi/M)]V\) proves global exponential attraction to \(u\), without assuming uniqueness of a near-uniform saddle. The finite chain's jump amplitudes imply \(\mathcal L_NV\le-[1-\cos(2\pi/M)]V+2/N\). Hence the stationary expectations satisfy \(\mathbb E_{\mathrm{ss}}V=O(N^{-1})\). Applying the generator to \(V^2\) and using \(|V(x+(e_j-e_i)/N)-V(x)|\le C\sqrt V/N+C/N^2\) yields \(\mathbb E_{\mathrm{ss}}V^2=O(N^{-2})\). This controls fourth moments of the centered field.

**2. Stationary Gaussian limit.** A Taylor expansion of the jump generator at \(u\), together with the above concentration and moment bounds, identifies the stationary fluctuation limit as an Ornstein–Uhlenbeck process on the zero-sum hyperplane \(\sum_i Z_i=0\). Its linear drift matrix and infinitesimal covariance are
\[
 H= a(S_- -I)+b(S_+ -I),\quad a=\frac p2+\frac{g}{4M},\quad b=\frac q2+\frac{g}{4M},\qquad
 Q=\frac{1}{2M}(2I-S_+-S_-),
\]
where the circular shifts are \((S_+z)_i=z_{i+1}\) and \((S_-z)_i=z_{i-1}\). The OU generator is \((Hz)\cdot\nabla+\tfrac12 Q:\nabla^2\). Every nonzero Fourier mode has strictly negative real drift part, so the limiting stationary law is unique. Convergence of stationary generators and bounded fourth moments yields the stationary finite-dimensional law and its covariance functions, rather than simply assuming a linear-noise approximation.

On Fourier mode \(k\), \(H\) has eigenvalue \(-\gamma_k-i\omega_k\) under one Fourier sign convention (the sign of \(\omega_k\) is immaterial to diagonal covariances), while \(Q\) has eigenvalue \([1-\cos(2\pi k/M)]/M\). The Lyapunov equation \(H\Sigma+\Sigma H^\top+Q=0\) therefore gives
\[
 \Sigma=\frac{1}{M+g}\left(I-\frac{\mathbf1\mathbf1^\top}{M}\right).
\]
This also shows why circulating motion changes temporal correlations while leaving equal-time Gaussian covariance unchanged. The latter observation is antecedent to, not the novelty of, this result: see the prior literature below.

**3. All-lag and time-integrated fluctuations.** For stationarity, \(\operatorname{Cov}(Z(t),Z(0))=e^{Ht}\Sigma\). Fourier inversion gives the stated \(C_M(t)\), and Fubini's theorem plus exponential decay yields
\[
 \lim_{T\to\infty}T\operatorname{Var}\left(T^{-1}\int_0^T Z_i(t)\,dt\right)
 =2\int_0^\infty C_M(t)\,dt=\mathcal A_M(g,\delta).
\]
Differentiating the summands with respect to \(\delta^2\) gives a negative derivative whenever \(\sin(2\pi k/M)\ne0\). For \(M\ge3\), at least one such mode exists; therefore \(\mathcal A_M\) is strictly decreasing in \(|\delta|\), including the strict inequality relative to zero bias. At zero bias use \(\sum_{k=1}^{M-1}\csc^2(\pi k/M)=(M^2-1)/3\) to obtain the stated exact rational expression.

**4. Weak-bias hydrodynamic crossover.** Write \(\alpha_M=(M+g_M)/M\to1+\kappa\) and \(\delta_M=\zeta/M\). For every fixed positive mode \(k\), the two end modes \(k\) and \(M-k\) have limits
\[
 \frac{2}{M(M+g_M)}\frac{\gamma_k}{\gamma_k^2+\omega_k^2}
 \longrightarrow\frac{2}{\alpha^2\pi^2 k^2+\zeta^2},\qquad \alpha=1+\kappa.
\]
A uniform upper bound of a constant times \([\min(k,M-k)]^{-2}\), using \(\gamma_k\ge c\min(k,M-k)^2/M^2\), permits dominated convergence after pairing the modes. Hence
\[
 \lim\mathcal A_M(g_M,\zeta/M)
 =\frac{4}{\alpha^2}\sum_{k\ge1}\frac{1}{\pi^2 k^2+(\zeta/\alpha)^2}.
\]
The classical partial-fraction identity \(\sum_{k\ge1}(\pi^2 k^2+u^2)^{-1}=[u\coth u-1]/(2u^2)\) proves the crossover. For fixed \(\delta\ne0\), the summand in the finite exact expression is a bounded continuous function of angular frequency, and its angular mean is
\[
 \frac1{2\pi}\int_0^{2\pi}\frac{\alpha(1-\cos\theta)/2}{[\alpha(1-\cos\theta)/2]^2+[\delta\sin\theta/2]^2}\,d\theta=\frac1{|\delta|}.
\]
Riemann-sum convergence now gives the strong-bias asymptotic. This proves both asymptotic sides and the intervening \(M^{-1}\) scale.

## Verification

Run `python check.py` with Python, NumPy and SciPy installed. The checker constructs independent circulant drift/noise matrices and solves the continuous Lyapunov and Poisson equations without using the Fourier sum as its matrix input. It tests the all-lag covariance and integrated coefficient over multiple ring sizes, interactions, biases and lags, verifies the exact zero-bias identity, and compares finite-size values with the hyperbolic-cotangent limit. The matrix and limiting formulas passed 1,554 assertions in the supplied check. These numerical checks support reproducibility; they are not substitutes for the all-parameter analytic arguments above.

## Relationship to prior work

Cheng and Lai, *Non-equilibrium thermodynamics and phase transition of Ehrenfest urns with interactions* (arXiv:2106.00915, publicly released 2021-06-02), already give the microscopic ring model, the three-urn stationary Gaussian fluctuation matrix and oscillatory relaxation eigenvalues. Cheng and Lai, *Non-equilibrium dynamics and phase transitions in Potts model and interacting Ehrenfest urn model* (arXiv:2401.02632, 2024-01-05), identify the Potts mapping and mean-field dynamics. Cheng and Lai, *Coexistence of distinct non-uniform non-equilibrium steady states in Ehrenfest multi-urn model on a ring* (arXiv:2403.15708, 2024-03-23), explicitly compute the four-urn stationary Gaussian covariance and discuss thermodynamic stability. These static and small-system deductions are not claimed here as original. The assessed contribution is an explicit all-urn temporal occupation-noise formula with strict bias monotonicity and the large-ring \(M^{-1}\)-bias hyperbolic-cotangent crossover. General OU/Poisson-equation methods are known; the model-specific large-ring classification has not been identified in the checked sources.

## Limitations

The result is for repulsive or zero interaction \(g\ge0\), finite positive forward and reverse rates, and the sequential limits of particle count, observation time and ring length. No uniform joint three-parameter theorem is asserted. Equal-time Gaussian covariance invariance and small-ring oscillatory linear modes are known, not independently novel. The crossover formula concerns occupation-time variance and does not establish optimal transport, total entropy production, or finite-particle exact stationary laws. A general published Markov-chain Fourier theorem could subsume a component of the temporal calculation; publication priority requires independent external review.

## References

1. C.-H. Cheng and P.-Y. Lai, *Non-equilibrium thermodynamics and phase transition of Ehrenfest urns with interactions* (2021), https://arxiv.org/abs/2106.00915.
2. C.-H. Cheng and P.-Y. Lai, *Non-equilibrium dynamics and phase transitions in Potts model and interacting Ehrenfest urn model* (2024), https://arxiv.org/abs/2401.02632.
3. C.-H. Cheng and P.-Y. Lai, *Coexistence of distinct non-uniform non-equilibrium steady states in Ehrenfest multi-urn model on a ring* (2024), https://arxiv.org/abs/2403.15708.
