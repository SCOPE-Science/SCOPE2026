# A sharp moving-seed Poisson transition and exact first-hit law for parabolic stochastic dynamics

## Finding

**Theorem (moving initial-row seeds).** Fix \(\beta_0,\beta_1,\kappa>0\) and \(\rho\in(0,1)\). For every sufficiently large integer \(N\), take the same two-state nonlinear stochastic operator
\[
 W(1-s,s)=(1-h(s),h(s)),\qquad h(s)=\frac{s}{1+s},
\]
but choose initial row seeds \(s_{i,N}=\beta_iN^{-\kappa}\), for \(i\in\{0,1\}\). Define the associated length-\(N\) inhomogeneous Markov chain \(Z_0,\ldots,Z_N\) by \(\Pr(Z_0=1)=\rho\) and
\[
 \Pr(Z_n=1\mid Z_{n-1}=i)=\frac1{n+N^\kappa/\beta_i},
 \qquad 1\le n\le N.
\]
Write \(\mathsf P_N=\mathcal L(Z_1,\ldots,Z_N)\), and let \(\mathsf Q_N\) be the product law of independent Bernoulli coordinates with \(q_{n,N}=(n+N^\kappa/\beta_0)^{-1}\). The following statements hold.

**(i) Optimal whole-path decoupling.** For a finite constant depending only on the fixed parameters,
\[
 \|\mathsf P_N-\mathsf Q_N\|_{\rm TV}\le C N^{-\kappa}.
\]
When \(\beta_0\ne\beta_1\), this is an exact order bound:
\[
 \|\mathsf P_N-\mathsf Q_N\|_{\rm TV}
 \ge\rho\left|\frac1{1+N^\kappa/\beta_1}-\frac1{1+N^\kappa/\beta_0}\right|
 \sim\rho|\beta_1-\beta_0|N^{-\kappa}.
\]
For coinciding seeds the path is exactly independent and the total-variation distance vanishes.

**(ii) Sharp rare-visit phase diagram.** Let \(K_N=\sum_{n=1}^N\mathbf1_{\{Z_n=1\}}\), and \(\mu_N=\sum_{n=1}^Nq_{n,N}\).

* If \(0<\kappa<1\), then \(\mu_N=(1-\kappa)\log N+\log\beta_0+o(1)\), and
\[
 \frac{K_N-\mu_N}{\sqrt{\mu_N}}\Longrightarrow\mathcal N(0,1),
 \qquad\frac{K_N}{\log N}\longrightarrow1-\kappa
 \quad\text{in probability}.
\]
* If \(\kappa=1\), the random point measure \(\sum_{n=1}^N\mathbf1_{\{Z_n=1\}}\delta_{n/N}\) converges weakly on \([0,1]\) to the inhomogeneous Poisson point process with intensity
\[
 \lambda(t)\,dt=\frac{\beta_0}{1+\beta_0t}\,dt.
\]
In particular,
\[
 K_N\Longrightarrow\operatorname{Poisson}(\log(1+\beta_0)),
\qquad \|\mathcal L(K_N)-\operatorname{Poisson}(\log(1+\beta_0))\|_{\rm TV}=O(N^{-1}).
\]
* If \(\kappa>1\), then \(\Pr(K_N=0)\to1\).

**(iii) Exact first-hit law.** Set \(\tau=\inf\{n\ge1:Z_n=1\}\), with \(\tau=\infty\) if there is no such visit. Conditional on \(Z_0=0\), for every \(0\le m\le N\),
\[
 \Pr(\tau>m\mid Z_0=0)=\frac{N^\kappa/\beta_0}{N^\kappa/\beta_0+m}.
\]
Thus the first-hit clock, on the scale \(N^\kappa/\beta_0\) when \(0<\kappa<1\), tends to a Pareto-type survival function \((1+t)^{-1}\). At \(\kappa=1\), for \(0\le t\le1\), the survival at scaled time \(Nt\) tends to \((1+\beta_0t)^{-1}\), matching the Poisson no-point probability.

## Assumptions and scope

The parameters \(\beta_0,\beta_1,\kappa,\rho\) are fixed, strictly positive where stated, and \(N\to\infty\). The stipulation \(N\ge\max\{\beta_0^{1/\kappa},\beta_1^{1/\kappa}\}\) guarantees valid row seeds in \((0,1]\). The nonlinear operator \(W\) is independent of \(N\); the **initial row-seed data** vary with \(N\). This is a triangular family of finite experiments, not one chain with retroactively changed transitions. The original-time step is \(n\), not a return or accelerated time. Total variation is the supremum of the absolute probability difference over measurable events. The first-hit identity is conditional on the *initial Markov state*, not on a stationary distribution. The cited framework specifies the transition row at generation \(n\) as the \(n\)-fold iterate of its own initial seed; in particular, \(h^{\circ n}(s)=1/(n+1/s)\).

## Proof

**1. Exact scalar dynamics.** The identity \(h(s)^{-1}=s^{-1}+1\) yields \(h^{\circ n}(s)=(n+s^{-1})^{-1}\) by induction. The operator satisfies the published \(F\)-stochastic definition with \(f=\varphi=g=h\) in simplex coordinate \(s\): \(h(0)=0\), \(h(s)>0\) for \(s>0\), and its iterates tend to zero. Set \(A=N^\kappa\), \(a_i=A/\beta_i\), and \(c=\min\{\beta_0^{-1},\beta_1^{-1}\}>0\).

**2. Full-path total-variation bound.** Let \(U_1,\ldots,U_N\) be independent uniforms and construct simultaneously
\[
 Z_n=\mathbf1_{\{U_n\le(n+a_{Z_{n-1}})^{-1}\}},\qquad
 B_n=\mathbf1_{\{U_n\le(n+a_0)^{-1}\}}.
\]
Choose \(Z_0\) independently with \(\Pr(Z_0=1)=\rho\). The vectors \((Z_n)_{1\le n\le N}\) and \((B_n)_{1\le n\le N}\) have laws \(\mathsf P_N\) and \(\mathsf Q_N\). Write
\[
 \Delta_n=\left|\frac1{n+a_1}-\frac1{n+a_0}\right|
 =\frac{A|\beta_1^{-1}-\beta_0^{-1}|}{(n+a_0)(n+a_1)}.
\]
The first disagreement probability is exactly \(\rho\Delta_1\). At subsequent times it is exactly \(\Delta_n\Pr(Z_{n-1}=1)\), because row zero has the reference threshold. Independently of the past,
\[
 \Pr(Z_{n-1}=1)\le\frac1{n-1+cA},\qquad
 \Delta_n\le\frac{A|\beta_1^{-1}-\beta_0^{-1}|}{(n+cA)^2}.
\]
Therefore
\[
 \begin{aligned}
 \|\mathsf P_N-\mathsf Q_N\|_{\rm TV}
 &\le \Pr\{(Z_1,\ldots,Z_N)\ne(B_1,\ldots,B_N)\}\\
 &\le \rho\Delta_1+C_1 A\sum_{n=2}^N(n+cA-1)^{-3}
 =O(A^{-1}).
 \end{aligned}
\]
The last bound is uniform over the full horizon: the infinite comparison sum is \(O(A^{-2})\). Conversely, projecting onto coordinate one and using its marginal gives
\[
 \|\mathsf P_N-\mathsf Q_N\|_{\rm TV}\ge\rho\Delta_1
 \sim\rho|\beta_1-\beta_0|A^{-1},
\]
so the exponent is optimal when the seeds differ.

**3. Independent count law and the subcritical Gaussian regime.** For \(S_N=\sum_{n=1}^NB_n\), an exact rising-factorial identity is
\[
 \mathbb E(z^{S_N})=
 \prod_{n=1}^N\left(1+\frac{z-1}{n+a_0}\right)
 =\frac{(a_0+z)_N}{(a_0+1)_N},
 \qquad (v)_N:=\prod_{j=0}^{N-1}(v+j).
\]
Monotone integral comparison gives
\[
 \mu_N=\log\left(1+\beta_0N^{1-\kappa}\right)+O(N^{-\kappa}),
 \qquad \sum_{n=1}^Nq_{n,N}^2\le C_2N^{-\kappa}.
\]
When \(0<\kappa<1\), the variance \(\sum q_{n,N}(1-q_{n,N})\sim\mu_N\to\infty\). Bounded independent Bernoulli increments satisfy Lindeberg's condition and yield the stated central limit theorem and law of large numbers for \(S_N\). The full-vector total-variation estimate transfers both limits to \(K_N\), including the centering by the specified deterministic \(\mu_N\).

**4. Critical rare-event point process.** If \(\kappa=1\), then
\[
 q_{n,N}=\frac1N\frac{\beta_0}{1+\beta_0 n/N}.
\]
For every continuous nonnegative test function \(f\) on \([0,1]\), independence yields the exact product Laplace functional
\[
 \mathbb E\exp\left(-\sum_{n=1}^Nf(n/N)B_n\right)
 =\prod_{n=1}^N\left[1-q_{n,N}(1-e^{-f(n/N)})\right].
\]
Since \(\max_nq_{n,N}=O(N^{-1})\), expanding the logarithm produces an error bounded by \(O(\sum_nq_{n,N}^2)=O(N^{-1})\); the linear term converges by Riemann sums to
\[
 -\int_0^1(1-e^{-f(t)})\frac{\beta_0}{1+\beta_0t}\,dt.
\]
This is the Laplace functional of the stated Poisson point process. The whole-vector coupling transfers the weak point-process convergence to \(Z\) since the associated point measures coincide with probability \(1-O(N^{-1})\). For the total count, Le Cam's elementary Bernoulli–Poisson bound \(\|\mathcal L(S_N)-\operatorname{Poisson}(\mu_N)\|_{\rm TV}\le\sum_nq_{n,N}^2\), together with \(\mu_N=\log(1+\beta_0)+O(N^{-1})\), gives the asserted \(O(N^{-1})\) count total variation after applying the coupling triangle inequality. The point measures are *not* claimed to converge in total variation: their supports are on a deterministic grid.

**5. Supercritical extinction of observations.** If \(\kappa>1\), then \(\mathbb E S_N=\mu_N\le\beta_0N^{1-\kappa}\to0\). Markov's inequality gives \(\Pr(S_N>0)\to0\), and whole-path total variation transfers the statement to \(K_N\).

**6. Exact first-hit clock.** On \(\{Z_0=0,\tau>n-1\}\), the previous state is zero. Thus the chance of remaining at zero at time \(n\) is \(1-1/(n+a_0)=(n+a_0-1)/(n+a_0)\). The product telescopes:
\[
 \Pr(\tau>m\mid Z_0=0)=\prod_{n=1}^m\frac{n+a_0-1}{n+a_0}=\frac{a_0}{a_0+m}.
\]
Scale \(m=\lfloor a_0t\rfloor\) for \(0<\kappa<1\), or \(m=\lfloor Nt\rfloor\) for \(\kappa=1\), to obtain the stated survival functions. The first-hit identity is exact at every finite admissible \(N\), not an approximation.

## Verification

The standalone `checker.py` uses only the Python standard library and can be run as `python checker.py`. It verifies the parabolic iteration identity with rational arithmetic, enumerates complete short-path probabilities and their sharp first-coordinate lower bounds, checks the rising-factorial generating function and exact first-hit product, and compares the three asymptotic regimes numerically. Successful execution prints `MOVING_SEED_PARABOLIC_POISSON_OK`.

All infinite-horizon limits, the total-variation estimates and process convergence are proved analytically above. Finite computational tests only corroborate the formulas.

## Relationship to prior work

Souissi–Mukhamedov (2024) introduced the \(F\)-stochastic class and the construction of nonhomogeneous Markov chains from iterated initial rows. Jamilov–Mukhamedov–Mukhamedova–Souissi (2024) investigated regularity and absolute-continuity criteria for the associated path measures. The subsequently published result *Parabolic stochastic dynamics: full path-measure classes and a critical rare-visit window* already proves exact iterates for the present \(h\), a finite-defect coupling and a path-law equivalence phase diagram for **fixed positive seeds**, plus a critical-window Gaussian law when the **exponent** varies with the horizon. Neither the old fixed-seed asymptotics nor the moving-exponent result supplies the present moving-**seed** entire-path estimate uniformly as its initial row values vanish, the optimal exponent, or the inhomogeneous Poisson startup transition and exact first-hit scaling. Classical independent Bernoulli Poisson approximation and the independent central limit theorem are standard tools, not claimed as new.

## Limitations

The theorem is limited to the stated parabolic two-state operator, fixed positive seed coefficients and initial mass, and its triangular family of experiments. Its \(O(N^{-\kappa})\) estimate and sharpness refer to the *length-\(N\) path excluding coordinate zero*, not equivalence of infinite-horizon laws across changing seeds. The Poisson point-process limit is weak, not total variation, whereas the finite count has a quantitative total-variation bound. This theorem does not settle arbitrary \(F\)-stochastic systems. No claim of mathematical novelty beyond the inspected literature is made, and no independent validation has been performed.

## References

1. A. Souissi and F. Mukhamedov, “Nonlinear Stochastic Operators and Associated Inhomogeneous Entangled Quantum Markov Chains,” *Journal of Nonlinear Mathematical Physics* **31** (2024), article 11, first public 2024-02-26, https://doi.org/10.1007/s44198-024-00172-6 .
2. U. Jamilov, F. Mukhamedov, F. Mukhamedova and A. Souissi, “Dynamics of nonlinear stochastic operators and associated Markov measures,” *Mathematical Methods in the Applied Sciences* **47** (2024), 13300–13312, first public 2024-05-16, https://doi.org/10.1002/mma.10191 .
3. “Parabolic stochastic dynamics: full path-measure classes and a critical rare-visit window” (public result, 2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-parabolic-stochastic-dynamics-full-path-measure-classes-and-a-cr--c3b72a8ef229/RESULT.md .
4. Classical Bernoulli-array central limit and Poisson law-of-small-numbers theorems; used as standard probability tools with the requisite estimates shown in the proof.
