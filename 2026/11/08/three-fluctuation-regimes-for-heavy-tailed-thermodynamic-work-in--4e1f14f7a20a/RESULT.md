# Three fluctuation regimes for heavy-tailed thermodynamic work in harmonic resetting

## Finding
Consider the work paid by switching a freely diffusing Brownian particle into a harmonic resetting trap and then restarting from an independently thermalized position. If independent exploration times have a power-law survival tail, the mean work rate stays finite, but its *physical-time* fluctuations have three sharply different limits.

Write \(\kappa>0\) for resetting-trap stiffness, \(D>0\) for diffusivity, \(\delta\geq0\) for the deterministic duration of the thermalizing return phase, and \(\sigma^2>0\) for the variance of the freshly thermalized position. Let the exploration duration \(T\) be positive and satisfy
\[
\Pr(T>u)\sim c u^{-q}\quad(u\to\infty),\qquad c>0,\quad q>1,
\]
with \(\mu=\mathbb ET\in(0,\infty)\) and \(m=\mu+\delta\). In each independent cycle, start with \(X\sim N(0,\sigma^2)\), diffuse freely for \(T\), then switch on \(V(x)=\kappa x^2/2\). The net pair-of-switches work is
\[
w=\frac{\kappa}{2}\big[(X+\sqrt{2DT}Z)^2-X^2\big],\qquad Z\sim N(0,1),
\]
where \(X,T,Z\) are independent across and within cycles. At the end of the return phase the position is **independently resampled** from the same thermal Gaussian. Define \(W(t)\) as the sum of the work of completed cycles by physical time \(t\), including return-phase durations in the clock. Its deterministic rate is
\[
v=\lim_{t\to\infty}\frac{W(t)}t=\frac{\kappa D\mu}{m}\quad\text{almost surely}.
\]

For an auxiliary standard normal \(Z\), set \(A=\kappa D Z^2-v\), and
\[
c_+=c\,\mathbb E[(A)_+^q],\qquad
c_-=c\,\mathbb E[(-A)_+^q].
\]
Both numbers are strictly positive for every finite \(\delta\geq0\).

**Stable regime.** For \(1<q<2\),
\[
\frac{W(t)-vt}{t^{1/q}}\ \Longrightarrow\ S_q,
\]
where \(S_q\) is the centered two-sided \(q\)-stable distribution with Lévy measure
\[
\nu(dx)=\frac q m\left[c_+\mathbf1_{\{x>0\}}x^{-q-1}+c_-\mathbf1_{\{x<0\}}|x|^{-q-1}\right]dx.
\]
In particular \(\log\mathbb E e^{iuS_q}=\int_{\mathbb R}(e^{iux}-1-iux)\,\nu(dx)\), which fixes every normalization without an unspecified scale convention.

**Critical regime.** For \(q=2\), define \(C=c\mathbb E[A^2]=c(3\kappa^2D^2-2\kappa Dv+v^2)\). Then
\[
\frac{W(t)-vt}{\sqrt{t\log t}}\ \Longrightarrow\ N\!\left(0,\frac C m\right).
\]

**Finite-variance regime.** For \(q>2\),
\[
\frac{W(t)-vt}{\sqrt t}\ \Longrightarrow\ N\!\left(0,\frac{\mathcal V}m\right),
\]
where the exact cycle-compensated variance is
\[
\mathcal V=2\kappa^2D^2\mathbb ET^2+2\kappa^2D\sigma^2\mu
+\left(\frac{\kappa D\delta}{m}\right)^2\!\operatorname{Var}(T).
\]
The dividing exponent \(q=2\) is sharp. For \(1<q\leq2\), the centered single-cycle reward has infinite second moment despite finite mean.

**A sign asymmetry created by the clock.** The uncentered work of one cycle obeys \(w\geq-\kappa X^2/2\), so its negative tail is at most exponentially small. Nevertheless the compensated reward \(w-v(T+\delta)\) has a negative power-law tail \(c_-u^{-q}\). Moreover increasing the deterministic return overhead \(\delta\) strictly increases \(c_+\) and strictly decreases \(c_-\), with \(c_-\downarrow0\) as \(\delta\to\infty\).

## Assumptions and scope
The theorem concerns a one-dimensional overdamped Brownian exploration phase with zero exploration potential and a harmonic returning potential, in the **exact renewal idealization**. The return duration \(\delta\) is charged to the physical-time clock, but a return ends with a fresh Gaussian draw independent of all past states. Passive finite-duration harmonic relaxation without independent rethermalization is not claimed to produce this exact model. A thermal Boltzmann preparation has \(\sigma^2=k_{\mathrm B}\Theta/\kappa\), but only Gaussian preparation with finite positive variance is needed. Work is the sum of the two instantaneous switch contributions per *completed* cycle, not the separate heat during thermal relaxation. The final incomplete cycle is excluded from \(W(t)\); this convention is made explicit rather than hidden in a boundary term. No nonlattice assumption is required for the fluctuation limits: the renewal age is tight under the finite-mean assumption. The stated survival equivalence and independence are essential.

## Proof
**1. Work and rate.** Let \(T_i,X_i,Z_i\) be independent copies and put \(L_i=T_i+\delta\), \(S_n=\sum_{i=1}^nL_i\), \(N(t)=\max\{n:S_n\leq t\}\) and \(W(t)=\sum_{i=1}^{N(t)}w_i\). The free Brownian propagator gives the displayed work identity. Normal moments yield \(\mathbb E[w_i\mid T_i]=\kappa DT_i\) and
\[
\operatorname{Var}(w_i\mid T_i)=2\kappa^2D^2T_i^2+2\kappa^2D\sigma^2 T_i.
\]
For \(q>1\) the mean \(\mathbb E|w_i|\) is finite: the \(T_i\) term has finite mean and the cross term has finite \(\mathbb E\sqrt{T_i}\). Renewal-reward strong laws therefore give \(W(t)/t\to v=\mathbb Ew_i/\mathbb EL_i\).

**2. Tail of compensated work.** Let \(\xi_i=w_i-vL_i\), whose expectation is exactly zero. The decomposition
\[
\xi_i=T_iA_i+\kappa X_i\sqrt{2DT_i}\,Z_i-v\delta,
\qquad A_i=\kappa DZ_i^2-v,
\]
separates a regularly varying main term from a lower-order perturbation. For any \(p\) satisfying \(q<p<2q\), independence and Gaussian moments give
\[
\mathbb E\big|\kappa X_i\sqrt{2DT_i}\,Z_i\big|^p<\infty,
\]
because \(p/2<q\). Markov's inequality makes the perturbation \(o(u^{-q})\) in either tail. Conditioning on \(A_i\), the standard product-tail argument (domination by \(|A_i|^{q+\epsilon}\) for some \(\epsilon>0\)) gives
\[
\Pr(T_i A_i>u)\sim c_+u^{-q},\qquad
\Pr(T_i A_i<-u)\sim c_-u^{-q}.
\]
An \(\epsilon u\) sandwich transfers the same limits to \(\xi_i\). The Gaussian law assigns positive probability both to \(Z_i^2>v/(\kappa D)\) and to \(Z_i^2<v/(\kappa D)\); hence \(c_+,c_->0\) for finite \(\delta\).

**3. Stable and Gaussian domains of attraction.** For \(1<q<2\), the two tail equivalences with \(\mathbb E\xi_i=0\) imply the centered i.i.d. stable domain-of-attraction theorem. At deterministic index \(n\), the Lévy intensity of \(n^{-1/q}\sum_{i\le n}\xi_i\) has positive/negative tail masses \(c_+,c_-\). Since \(N(t)/t\to1/m\), the functional stable limit theorem and random time change give the claimed intensity divided by \(m\). For \(q=2\), the truncated variance instead satisfies
\[
\mathbb E[\xi_i^2\mathbf1_{\{|\xi_i|\le u\}}]\sim2(c_++c_-)\log u=2C\log u.
\]
The normal domain-of-attraction theorem then gives \(\sum_{i\le n}\xi_i/\sqrt{n\log n}\Longrightarrow N(0,C)\), followed by the same random time change. For \(q>2\), the ordinary i.i.d. central limit theorem applies and total-variance decomposition in step 1 yields \(\operatorname{Var}(\xi_i)=\mathcal V\).

**4. Complete-cycle clock correction.** Exactly,
\[
W(t)-vt=\sum_{i=1}^{N(t)}\xi_i-v\big(t-S_{N(t)}\big).
\]
For finite-mean positive renewal intervals the backward recurrence age \(t-S_{N(t)}\) is tight. In the nonlattice case it additionally converges to a proper equilibrium-age law, but that stronger statement is unnecessary here. Dividing by \(t^{1/q}\), \(\sqrt{t\log t}\), or \(\sqrt t\) makes this remainder vanish in probability. This completes all three limits without treating the random number of cycles as independent of their work.

**5. Negative-tail mechanism and monotonicity.** Since \((X_i+\sqrt{2DT_i}Z_i)^2\ge0\), \(w_i\ge-\kappa X_i^2/2\), and the Gaussian square has an exponentially light tail. By contrast, subtracting the time-compensation \(v(T_i+\delta)\) makes the coefficient \(A_i\) negative on a nonempty interval of Gaussian values, yielding the negative \(u^{-q}\) tail. Since \(v=\kappa D\mu/(\mu+\delta)\) decreases strictly with \(\delta\), \(A_i\) increases pointwise: its positive-part \(q\)-moment increases strictly and its negative-part \(q\)-moment decreases strictly. Dominated convergence gives \(c_-\to0\).

## Verification
A standalone `check.py` reproduces the conditional-moment algebra independently, numerically integrates both positive and negative one-cycle tail constants for Lomax exploration clocks, verifies the \(q=2\) coefficient against the Gaussian fourth moment, checks the monotonicity with return overhead, and checks the pathwise lower bound for raw cycle work. Executing `python check.py` in a Python environment with SciPy and NumPy produces 87 passing checks. This verifies finite formulas only; the infinite-time distributional limits depend on the analytical renewal, regular-variation, and domain-of-attraction arguments above. For \(q=3/2\), \(\kappa=D=\mu=1\), \(\delta=1/2\), and the Lomax law with scale \(1/2\), the integrated coefficients are \(c_+\approx0.358840462559\), \(c_-\approx0.069992190507\). The thermal preparation variance does not enter either leading coefficient.

## Relationship to prior work
Olsen, Gupta, Mori and Krishnamurthy (arXiv:2310.11267, first posted 2023-10-17), give the general generating-function framework for work under finite-time potential-switching resets, including non-Poisson reset intervals. Their explicit harmonic work-fluctuation calculations use exponentially distributed exploration times; the paper explicitly identifies other waiting-time laws as a future question. The present statement isolates a free-exploration/harmonic-return specialization and determines non-Poisson **physical-time** limits, including the correlated clock-compensation effect. The general transform motivates the setup but does not itself state the stable intensity or critical normalization.

Gupta, Plata and Pal (arXiv:1909.08512) derive Gaussian work fluctuations under their Poisson restart protocol, explicitly assuming regular cycle-work variance. That regime cannot establish the heavy-tail limits here. Horii, Lefevere, Itami and Nemoto (arXiv:2203.08584) study anomalous renewal-reward fluctuations and a critical second-moment boundary for counting and Knudsen-gas models; their general theory is relevant and is credited, while the exact signed Brownian work-cycle compensation, the two-sided coefficients and the three explicit normalizations here concern a different observable. General stable-sum and renewal-reward theorems are used as established tools, not newly claimed results.

## Limitations
The result does not establish finite-time error bounds, stable-limit convergence rates, continuous relaxation dynamics during finite returns, or work statistics for nonquadratic reset traps. For \(1<q\le2\) the asymptotic law has infinite limiting variance; its finite-time cumulants need not follow by interchanging limits and expectations. The age correction is negligible on the displayed scales but can matter for finer asymptotics. The general renewal-reward theorems can potentially imply this specialization after nontrivial model-specific identification; priority against unindexed work remains uncertain. All scientific assessment here is self-review, not independent validation.

## References
1. K. S. Olsen, D. Gupta, F. Mori and S. Krishnamurthy, *Thermodynamic cost of finite-time stochastic resetting*, Phys. Rev. Research 6, 033343 (2024), arXiv:2310.11267, https://arxiv.org/html/2310.11267v5 (first public 2023-10-17).
2. D. Gupta, C. A. Plata and A. Pal, *Work fluctuations and Jarzynski equality in stochastic resetting*, Phys. Rev. Lett. 124, 110608 (2020), arXiv:1909.08512, https://arxiv.org/html/1909.08512v2.
3. H. Horii, R. Lefevere, M. Itami and T. Nemoto, *Anomalous fluctuations of renewal-reward processes with heavy-tailed distributions*, Phys. Rev. E 106, 034130 (2022), arXiv:2203.08584, https://arxiv.org/abs/2203.08584.
4. P. C. Bressloff, *Generalized Itô's lemma and the stochastic thermodynamics of diffusion with resetting*, J. Phys. A 57 (2024), https://doi.org/10.1088/1751-8121/ad8495 (context on switching potentials; not used as a limit theorem).
