# A universal logarithmic support-edge law for a heavy-tailed confined run-and-tumble particle

## Finding

Let a one-dimensional athermal run-and-tumble particle obey
\[
\dot X_t=-\kappa X_t+v\sigma_t,\qquad \kappa>0,\quad v>0,
\]
where the orientation \(\sigma_t\in\{-1,+1\}\) alternates at renewal times separated by independent, identically distributed positive waiting times \(T\). Write \(m=\mathbb E T\), \(B=v/\kappa\), and \(\overline G(t)=\Pr(T>t)\). For a stationary process, define the integrated survival function
\[
H(t)=\int_t^\infty\overline G(u)\,du.
\]
Suppose, for some \(\alpha>1\), a positive slowly varying function \(L\), and some constants \(C,\beta,u_0>0\),
\[
\overline G(t)\sim t^{-\alpha}L(t)\quad(t\to\infty),\qquad
\Pr(T\le u)\le C u^\beta\quad(0<u<u_0).
\]
Then the stationary position \(X_*\) is supported in \([-B,B]\), and with
\[
s_\varepsilon=\kappa^{-1}\log\frac{2B}{\varepsilon}
\]
one has the exact-equivalent edge law
\[
\boxed{\Pr(X_*>B-\varepsilon)\sim\frac{H(s_\varepsilon)}{2m}
\sim\frac{s_\varepsilon\,\overline G(s_\varepsilon)}{2m(\alpha-1)}}
\qquad(\varepsilon\downarrow0).
\]
The same law holds for \(\Pr(X_*<-B+\varepsilon)\). In particular, the exponent of the hidden tumbling-time tail is spatially identifiable:
\[
\lim_{\varepsilon\downarrow0}\frac{-\log\Pr(X_*>B-\varepsilon)}{\log\log(2B/\varepsilon)}=\alpha-1.
\]

For the half-\(t\) duration density studied by Farago and Smith,
\[
g(t)=\frac{\tau^2}{(t^2+\tau^2)^{3/2}},\qquad t>0,\quad \tau>0,
\]
the mean is \(m=\tau\) and the stationary harmonic-trap edge mass is explicitly
\[
\boxed{\Pr(X_*>B-\varepsilon)
=\frac{\kappa\tau}{4\log(2B/\varepsilon)}
\left[1+O\!\left(\frac{\log\log(2B/\varepsilon)}{\log(2B/\varepsilon)}\right)\right].}
\]
This is an inverse-logarithmic edge concentration, rather than the algebraic support-edge law of exponentially distributed run times.

## Assumptions and scope

The waiting durations are independent, strictly positive, identically distributed, absolutely continuous if desired, and have finite mean. The two orientation states have identical duration laws and flip deterministically at each renewal. The small-time assumption is a bound on the distribution function, not a restriction on large waiting times. Thermal translational noise is absent. The limit is the stationary position law followed by \(\varepsilon\downarrow0\), for fixed \(v,\kappa\) and a fixed run-time distribution. The origin of position is the harmonic trap center.

The stationary alternating-renewal orientation is obtained by choosing the sign with probability one half and taking an equilibrium-length-biased current renewal interval. The stationary position exists uniquely as the stable linear filter
\[
X_t=v\int_{-\infty}^t e^{-\kappa(t-u)}\sigma_u\,du.
\]
Any finite initial position is forgotten exponentially. All statements concern the stationary version, not a process started at a tumble at time zero.

## Proof

**1. Renewal age.** Conditional on either present orientation, the time \(A\) elapsed since the last flip has density \(\overline G(a)/m\), so
\[
\Pr(A>s\mid\sigma_0=+1)=\Pr(A>s\mid\sigma_0=-1)=\frac{H(s)}m.
\]
The current interval's duration and age are independent of all completed preceding interval lengths. Each sign has stationary probability one half.

**2. Boundary-deficit dynamics.** Put \(Z=(B-X)/(2B)\in[0,1]\). In a positive run of age \(A\), with entry deficit \(Z_0\),
\[
Z=Z_0e^{-\kappa A}.
\]
The immediately preceding run was negative and lasted a fresh ordinary renewal time \(U\) with law \(T\). During that run, the deficit moves toward one; hence, regardless of the earlier past,
\[
Z_0=1-e^{-\kappa U}+e^{-\kappa U}Z_{\mathrm{old}}
\ge1-e^{-\kappa U}.
\]
In a negative current run, the deficit satisfies
\[
Z=1-e^{-\kappa A}+e^{-\kappa A}Z_0\ge1-e^{-\kappa A}.
\]

**3. Upper and lower edge bounds.** Fix \(0<\theta<1\), let \(s=s_\varepsilon\), and write \(\delta=e^{-\kappa s}=\varepsilon/(2B)\). A present positive run older than \(s\) necessarily yields \(Z<\delta\). This gives, for every sufficiently small \(\varepsilon\),
\[
\Pr(Z<\delta)\ge\frac{H(s)}{2m}.
\]
Conversely, if the current run is positive, \(Z<\delta\), and \(A\le(1-\theta)s\), then \(Z_0<e^{-\kappa\theta s}\). The entry inequality forces
\[
U<-\kappa^{-1}\log(1-e^{-\kappa\theta s})=O(e^{-\kappa\theta s}).
\]
By the small-time waiting-time bound, the probability of this exceptional entry is \(O(e^{-\beta\kappa\theta s})\). In the negative state, \(Z<\delta\) requires \(A<-\kappa^{-1}\log(1-\delta)=O(\delta)\). Its probability is \(O(\delta)\), since the equilibrium-age density is bounded by \(1/m\). Combining the two signs gives
\[
\frac{H(s)}{2m}\le\Pr(Z<e^{-\kappa s})
\le\frac{H((1-\theta)s)}{2m}
+O(e^{-\beta\kappa\theta s})+O(e^{-\kappa s}).
\]
Every constant may depend on the fixed model parameters and \(\theta\), not on \(s\).

**4. Sharp asymptotic.** Karamata's tail integration theorem gives
\[
H(s)\sim\frac{s\overline G(s)}{\alpha-1}\in\mathrm{RV}_{1-\alpha}.
\]
The exponential errors in Step 3 are \(o(H(s))\). Therefore the ratio of the middle term to \(H(s)/(2m)\) has lower limit at least one and upper limit at most \((1-\theta)^{1-\alpha}\) for every fixed \(\theta\in(0,1)\). Taking \(\theta\downarrow0\) proves the first boxed equivalence. Reflection of the orientation and position gives the left edge. Slow variation then yields the logarithmic exponent identity.

**5. The half-\(t\) coefficient and error.** Direct differentiation establishes
\[
\overline G(t)=1-\frac{t}{\sqrt{t^2+\tau^2}},\qquad
H(t)=\sqrt{t^2+\tau^2}-t,\qquad m=\tau.
\]
Thus \(H(s)/(2m)=\tau/(4s)[1+O(s^{-2})]\). In Step 3, choose the upper-bound age window \((s-h,s]\) with \(h=2\kappa^{-1}\log(1+\kappa s)\). Then the exceptional-entry probability is \(O(s^{-2})\), the negative-state contribution is exponentially small, and \(H(s-h)=H(s)[1+O((\log s)/s)]\). Consequently
\[
\Pr(Z<e^{-\kappa s})=\frac{\tau}{4s}
\left[1+O\left(\frac{\log s}{s}\right)\right].
\]
Substitution of \(s=s_\varepsilon\) proves the second boxed law.

## Verification

The standalone file `verify_edge.py` checks the half-\(t\) density, survival integral, mean, residual-life tail and asymptotic coefficient symbolically. It independently samples the equilibrium age and 96 completed renewal runs to approximate stationary positions; the omitted earlier past is exponentially damped and no simulation is used in the proof. With a fixed random seed and 600000 stationary samples, the observed upper-edge probabilities at logarithmic thresholds \(6,10,16,24\) were respectively approximately \(0.045685,0.026100,0.016178,0.010620\); the corresponding leading theoretical values were approximately \(0.041381,0.024938,0.015610,0.010412\). The checker also verifies the valid deterministic finite-threshold bounds after accounting for sampling error. The universal theorem is proved analytically; Monte Carlo is diagnostic only.

## Relationship to prior work

Farago and Smith, *Confined run and tumble particles with non-Markovian tumbling statistics* (arXiv:2401.01576, first public January 3, 2024), formulate the general non-Markovian confined model, derive an integral-equation computational method and study a half-\(t\) waiting-time example. In their Section IV.3 the effective outward switching rate is observed to vanish at the support edge; the edge large-deviation prescription based on a nonzero limiting switching rate therefore ceases to apply. Their numerical half-\(t\) example uses a particular force whose derivative vanishes at the support boundary, unlike the harmonic force here. Their profiles and local-rate limits do not state the logarithmic stationary boundary-mass asymptotic or its coefficient proved here.

Dhar, Kundu, Majumdar, Sabhapandit and Schehr, *Run-and-tumble particle in one-dimensional confining potential: Steady state, relaxation and first passage properties* (arXiv:1811.03808, first public November 9, 2018), give exact stationary behavior for exponentially distributed run times. Their algebraic stationary support-edge phases do not cover non-Markovian regularly varying intervals.

The renewal-age identity is classical and is explicitly used rather than claimed as new. The claimed mathematical contribution is the sharp stationary support-edge equivalence, its general regular-variation coefficient, and the explicit half-\(t\) logarithmic law in the harmonic trap.

## Limitations

The result requires a finite-mean stationary renewal clock and a quantitative small-time probability bound; neither infinite-mean renewal dynamics nor arbitrary singular mass near zero is covered. The theorem concerns cumulative edge probability, not a pointwise asymptotic density or a finite-sample statistical estimator. It does not assert an edge formula for nonharmonic confining forces, orientation-dependent waiting-time distributions, additional Brownian noise, or a simultaneous limit in the trap and run-time parameters. Searches may miss unindexed general renewal-filter theorems; scientific priority is subject to independent literature review.

## References

1. O. Farago and N. R. Smith, *Confined run and tumble particles with non-Markovian tumbling statistics*, arXiv:2401.01576, first submitted January 3, 2024. https://arxiv.org/abs/2401.01576 ; complete accessible HTML https://arxiv.org/html/2401.01576 .
2. A. Dhar, A. Kundu, S. N. Majumdar, S. Sabhapandit and G. Schehr, *Run-and-tumble particle in one-dimensional confining potential: Steady state, relaxation and first passage properties*, arXiv:1811.03808, first submitted November 9, 2018. https://arxiv.org/abs/1811.03808 .
3. D. Heath, S. Resnick and G. Samorodnitsky, *Heavy tails and long range dependence in on/off processes and associated fluid models*, Mathematics of Operations Research 23 (1998), 145–165. https://doi.org/10.1287/moor.23.1.145 .
4. A. Sun, F. Ye and R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578, first submitted September 1, 2024. https://arxiv.org/abs/2409.00578 .
