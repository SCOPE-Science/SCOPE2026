# A sharp single-optimum boundary for memory-assisted spin–phase synchronization

## Finding

Consider the nonmagnetic incoherent linear-stability threshold of the globally coupled Ising–Kuramoto model with independent Ornstein–Uhlenbeck phase forcing and endogenous Glauber spin flips, as defined below. For every \(D,\tau,\mu>0\), its critical coupling as a function of switching rate \(\gamma\geq0\) admits **at most one interior local extremum**, and any such extremum is the unique strict global minimum. More precisely, define
\[
G(t)=\exp\!\left[-D\bigl(t-\tau(1-e^{-t/\tau})\bigr)\right],\qquad
M_j(\gamma)=\int_0^\infty t^j e^{-\gamma t}G(t)\,dt,\quad j=0,1,2,
\]
\[
\beta_c=\mu\frac{M_1(0)}{M_0(0)},\qquad
L=2-\frac{M_0(0)M_2(0)}{M_1(0)^2}>0.
\]
For \(0\leq\beta_s\leq\beta_c\), the threshold \(K_c(\gamma)\) is strictly increasing on \(\gamma>0\); its infimum is attained at the continuous boundary \(\gamma=0\). For \(\beta_s>\beta_c\), there is exactly one finite minimizing rate \(\gamma_*(\beta_s)>0\), characterized by
\[
\frac{M_0(\gamma_*)}{M_1(\gamma_*)}-\gamma_*=\frac{\mu}{\beta_s}.
\]
The map \(\beta_s\mapsto\gamma_*(\beta_s)\) is strictly increasing from zero to infinity. Its two sharp endpoint laws are
\[
\gamma_*(\beta_s)=\frac{\mu}{\beta_c^2L}(\beta_s-\beta_c)
+O\bigl((\beta_s-\beta_c)^2\bigr)\quad(\beta_s\downarrow\beta_c),
\]
\[
\gamma_*(\beta_s)=\frac{2D}{\mu\tau}\,\beta_s+O(1)
\quad(\beta_s\to\infty).
\]
These assertions concern the linear instability threshold, not a proof of nonlinear ordered-state existence or finite-system synchronization.

## Assumptions and scope

Take independent particles with spin \(\sigma_i\in\{-1,1\}\), angle \(\theta_i\) and Gaussian OU driving \(\eta_i\), in the mean-field limit. With \(Z_m=N^{-1}\sum_i\sigma_i e^{i\theta_i}\), the phase and noise equations and the conditional spin flip rate are
\[
\dot\theta_i=\mu K\sigma_i\operatorname{Im}(Z_m e^{-i\theta_i})+\eta_i,
\qquad \tau\,d\eta_i=-\eta_i\,dt+\sqrt{2D}\,dW_i,
\]
\[
w_i(\sigma_i\to-\sigma_i)=\frac\gamma2
\left[1-\sigma_i\tanh\!\left(\beta_s K\operatorname{Re}(Z_m e^{-i\theta_i})\right)\right].
\]
Here \(D,\tau,\mu,K>0\), \(\beta_s,\gamma\geq0\); the direct phase coupling and pure Ising coupling are both set to zero. The \(\gamma=0\) value means the continuous extension from positive switching rates, since frozen spins need not define an ergodic background. Angles begin in the nonmagnetic incoherent reference state, OU forcing is stationary, and the instability is computed at its first harmonic. The underlying linear susceptibility is
\[
\chi_\gamma=\frac12M_0(\gamma),\qquad
K_c(\gamma)=\frac{2}{(\mu+\beta_s\gamma)M_0(\gamma)}.
\]
This threshold and the existence-only optimality criterion appeared in Hayashi (2026); the new claim is the **complete necessity/uniqueness classification** and the quantified onset and strong-response limits.

## Proof

**1. Linear-response reduction.** Free OU increments are centered Gaussian with variance \(2D[t-\tau(1-e^{-t/\tau})]\), so their first circular harmonic is exactly \(G(t)\). At zero field the symmetric Glauber spin has correlation \(e^{-\gamma t}\). To first order in a perturbation of \(Z_m\), the phase-drift response contributes the convolution kernel \(\mu e^{-\gamma t}G(t)/2\), and linearizing the spin master equation contributes \(\beta_s\gamma e^{-\gamma t}G(t)/2\). Their sum yields the stationary linear threshold above. For \(\gamma>0\), this is equivalent to the first-harmonic dispersion relation \(1=K(\mu+\beta_s\gamma)M_0(\gamma+s)/2\); positivity of the kernel makes the first attractive instability stationary.

**2. A strict moment inequality.** Fix \(\gamma\geq0\) and normalize \(f_\gamma(t)=e^{-\gamma t}G(t)/M_0(\gamma)\) as a density on \([0,\infty)\). Since
\[
\frac{d^2}{dt^2}\log f_\gamma(t)=-\frac D\tau e^{-t/\tau}<0,
\]
this density is strictly log-concave. Write its survival function \(S(t)=\int_t^\infty f_\gamma(u)\,du\). Its hazard is strictly increasing: indeed, the reciprocal hazard is
\[
\frac{S(t)}{f_\gamma(t)}=\int_0^\infty
\frac{f_\gamma(t+u)}{f_\gamma(t)}\,du,
\]
and for each \(u>0\) the integrand is strictly decreasing in \(t\), by strict concavity of \(\log f_\gamma\). Consequently \(S(s+t)<S(s)S(t)\) for all \(s,t>0\). Integrating over \(s,t\geq0\) gives
\[
\frac12\mathbb E[T_\gamma^2]=\int_0^\infty\!\int_0^\infty S(s+t)\,ds\,dt
<\left(\int_0^\infty S(s)\,ds\right)^2
=(\mathbb E[T_\gamma])^2.
\]
Since \(\mathbb E[T_\gamma]=M_1/M_0\), this is exactly
\[
M_0(\gamma)M_2(\gamma)<2M_1(\gamma)^2.
\]
The inequality is strict for all finite \(\gamma\geq0\).

**3. Global monotonicity and sharp bifurcation.** Set \(h(\gamma)=M_0(\gamma)/M_1(\gamma)-\gamma\). Differentiation under the integral yields \(M_j'=-M_{j+1}\) and therefore
\[
h'(\gamma)=\frac{M_0(\gamma)M_2(\gamma)}{M_1(\gamma)^2}-2<0.
\]
All moments are finite because \(G(t)\leq e^{D\tau}e^{-Dt}\). At the origin, \(h(0)=M_0(0)/M_1(0)>0\). At large rates, the Taylor expansion \(G(t)=1-Dt^2/(2\tau)+O(t^3)\) and elementary Laplace integration give
\[
M_0(\gamma)=\gamma^{-1}-\frac D\tau\gamma^{-3}+O(\gamma^{-4}),
\qquad M_1(\gamma)=\gamma^{-2}-\frac{3D}{\tau}\gamma^{-4}+O(\gamma^{-5}),
\]
whence \(h(\gamma)=2D/(\tau\gamma)+O(\gamma^{-2})\to0\). Thus \(h\) is a continuous strictly decreasing bijection from \([0,\infty)\) onto \((0,h(0)]\). For \(\beta_s>0\), differentiating the reciprocal coupling \(F(\gamma)=K_c(\gamma)^{-1}\) gives
\[
F'(\gamma)=\frac{\beta_sM_1(\gamma)}2
\left[h(\gamma)-\frac\mu{\beta_s}\right].
\]
If \(\beta_s\leq\beta_c=\mu/h(0)\), this derivative is negative at every \(\gamma>0\). If \(\beta_s>\beta_c\), it switches exactly once from positive to negative, so the unique zero is the strict global maximizer of \(F\) and the strict global minimizer of \(K_c\). For \(\beta_s=0\), \(F'= -\mu M_1/2<0\). The inverse of the decreasing function \(h\) also proves strict increase of \(\gamma_*\) with \(\beta_s\).

**4. Endpoint laws.** At \(\beta_s=\beta_c\), \(h'(0)=-L<0\). Taylor expansion of \(h(\gamma_*)=\mu/\beta_s\) and the inverse-function theorem produce
\[
\gamma_* =\frac{\mu(\beta_s-\beta_c)}{\beta_c^2L}
+O\bigl((\beta_s-\beta_c)^2\bigr).
\]
As \(\beta_s\to\infty\), the same equation with the large-rate expansion of \(h\) forces \(\gamma_*\to\infty\) and yields \(\gamma_*=(2D/\mu\tau)\beta_s+O(1)\). All remainders hold with fixed \(D,\tau,\mu>0\).

## Verification

The accompanying `verify.py` independently integrates the moments and checks the exact threshold, global derivative sign, strict moment inequality, onset coefficient and strong-response law for several parameter values. For \(D=\tau=\mu=1\) it obtains \(\beta_c\approx1.260202010789377\); at \(\beta_s=2\) it obtains \(\gamma_*\approx1.825828106869273\), consistent with the source's displayed rounded optimizer \(1.826\). Numerical checks corroborate but do not replace the strict analytical proof.

## Relationship to prior work

Hayashi (2026), especially Sections II.2–II.3 and Appendix A, derives the linear susceptibility, stationary threshold, and a sufficient criterion for the existence of at least one finite optimal switching rate. Its numerical optimization at three memory times does not give a uniqueness theorem or a necessary-and-sufficient condition for every positive parameter choice. The present result proves such a classification by a strict log-concave-tilt moment inequality, and adds endpoint asymptotics that are not stated there. Tönjes (2010) treats the colored-noise Kuramoto instability without the endogenous Glauber spin response; Zhang and Strogatz (2021) optimize temporal network structure under resource constraints rather than this internal spin-relaxation rate. Strict log-concavity/increasing-hazard estimates are classical probabilistic ingredients, not claimed as new in isolation.

## Limitations

The result is for the nonmagnetic incoherent **linear-response critical coupling**, with vanishing direct phase and Ising-only couplings. It does not establish nonlinear ordered branches, finite-population phase transition statistics, or optimality in a magnetized background. Finite \(\tau>0\) is essential; the white-noise limit \(\tau=0\) has a different monotone formula and cannot be substituted into the asymptotic statements. The result is not a claim of priority over inaccessible or unidentified literature and has not been independently externally validated.

## References

1. R. Hayashi, *Memory-induced optimal switching in a dynamic Ising–Kuramoto model*, arXiv:2609.35838v1, first posted 2026-09-24. https://arxiv.org/abs/2609.35838 ; full text https://arxiv.org/html/2609.35838 .
2. R. Tönjes, *Synchronization Transition in the Kuramoto Model with Colored Noise*, Physical Review E **81**, 055201(R) (2010); arXiv:1003.1549. https://arxiv.org/abs/1003.1549 .
3. Y. Zhang and S. H. Strogatz, *Designing temporal networks that synchronize under resource constraints*, Nature Communications **12**, 3273 (2021). https://doi.org/10.1038/s41467-021-23446-9 .
