# Exact above-threshold salt-mass excursion law for Poisson leaching with exponential marks

## Finding

Consider a salt-mass process with constant positive input and independently timed leaching, as specified below. Fix any threshold \(h>0\) and let \(\tau_h\) be the first downward crossing of \(h\) after an upward passage through \(h\). The *entire excursion-duration distribution* is characterized by the following explicit Laplace transform. For every \(s>0\), put

\[
A=\frac{as}{\lambda+s},\qquad z=\frac{(\lambda+s)h}{c}.
\]

Then

\[
\boxed{\quad\mathbb E_h[e^{-s\tau_h}]
=\frac{\lambda}{\lambda+s}
\frac{U(A,a,z)}{U(A,a,z)+A\,U(A+1,a+1,z)}\quad},
\]

where \(U(\cdot,\cdot,\cdot)\) is Tricomi's confluent hypergeometric function. The right side extends continuously to \(1\) at \(s=0\). Since Laplace transforms uniquely determine nonnegative probability distributions, this gives an exact full-duration law rather than a calibrated two-parameter surrogate.

There is also a finite-threshold stochastic approximation to the first leaching time \(E\sim\operatorname{Exp}(\lambda)\): a coupling exists with \(\tau_h\ge E\) almost surely and

\[
\boxed{\quad d_{\mathrm{TV}}\big(\mathcal L(\tau_h),\operatorname{Exp}(\lambda)\big)
\leq\Pr(\tau_h>E)
=\mathbb E\bigg[1-\Big(1+\frac{cE}{h}\Big)^{-a}\bigg]
\leq\min\Big\{1,\frac{ac}{\lambda h}\Big\}.\quad}
\]

In particular, high-threshold excursions converge in total variation to one exponential waiting time, and their exact first-jump-survival correction obeys \(\Pr(\tau_h>E)\sim ac/(\lambda h)\).

## Assumptions and scope

Let \(c,\lambda,a,h\) be arbitrary positive real numbers. The right-continuous Markov process \((X_t)_{t\ge0}\) starts at \(X_0=h\), grows deterministically at speed \(c\) between leaching events, and experiences leaching at an independent rate-\(\lambda\) Poisson clock. At each event, \(X_t=R X_{t-}\), where the factors \(R=V^{1/a}\), \(V\sim\operatorname{Uniform}(0,1)\), are independent between events and independent of the clock. Consequently \(\Pr(R\le r)=r^a\) for \(0\le r\le1\). Equivalently, \(-\log R\) is exponential with mean \(1/a\). This multiplicative-jump convention specifies the physical event update directly and avoids any ambiguity about stochastic-integration prescriptions.

Define the strictly downward hitting time

\[
\tau_h=\inf\{t>0:X_t<h\}\quad\text{under }X_0=h.
\]

The deterministic drift immediately moves the path above \(h\), and any downward crossing occurs at a leaching jump. A jump landing at exactly \(h\) has probability zero. The formula is for *salt mass*, not the moisture-dependent salt concentration, and assumes a fixed input rate, a constant leaching intensity, exponential independent leaching marks, no other loss mechanism, and no measurements or seasonal forcing. No stationarity assumption is required for the excursion-transform identity.

## Proof

**1. Generator and boundary condition.** For \(s>0\) and \(x\ge h\), define \(f(x)=\mathbb E_x[e^{-s\tau_h}]\), with the convention \(e^{-s\infty}=0\). Extend the value function as \(f(y)=1\) for \(0<y<h\), where termination is immediate. For \(x>h\), a first-step decomposition (or the backward equation for the piecewise-deterministic generator) gives

\[
c f'(x)-(\lambda+s)f(x)
+\lambda a x^{-a}\left(\int_0^h y^{a-1}\,dy
+\int_h^x y^{a-1}f(y)\,dy\right)=0.
\]

Set

\[
I(x)=\Big(\frac h x\Big)^a+a x^{-a}\int_h^x y^{a-1}f(y)\,dy.
\]

Then \(c f'=(\lambda+s)f-\lambda I\) and \(I'=a(f-I)/x\). In particular, \(I(h+)=1\), which fixes the *right-hand* boundary relation

\[
c f'(h+)=(\lambda+s)f(h)-\lambda.
\]

Note that incorrectly setting \(f(h)=1\) would force the wrong boundary condition: a path beginning at \(h\) is not yet below it.

**2. Differential equation and behavior at infinity.** Differentiate the equations and eliminate \(I\). The result is

\[
cx f''(x)+\big(ac-(\lambda+s)x\big)f'(x)-as f(x)=0,
\qquad x>h.
\]

With \(z=(\lambda+s)x/c\) and \(A=as/(\lambda+s)>0\), this becomes Kummer's equation

\[
z F''(z)+(a-z)F'(z)-A F(z)=0.
\]

For completeness, the probabilistic solution tends to zero as \(x\to\infty\). For fixed \(T<\infty\), before time \(T\) the trajectory is bounded below by \(x\prod_{j=1}^{N_T}R_j\), whose strictly positive random product does not depend on \(x\); therefore \(\Pr_x(\tau_h\le T)\to0\). As \(0\le f(x)\le\Pr_x(\tau_h\le T)+e^{-sT}\), first let \(x\to\infty\), then \(T\to\infty\). The Kummer solution \(M(A,a,z)={}_1F_1(A;a;z)\) grows exponentially for \(A>0\), whereas \(U(A,a,z)\sim z^{-A}\). Hence the unique decaying solution is \(f(x)=K U(A,a,(\lambda+s)x/c)\).

**3. Normalization and reconstruction.** The standard identity \(\partial_z U(A,a,z)=-A U(A+1,a+1,z)\) and the right boundary relation yield

\[
K\left((\lambda+s)U(A,a,z)-c\,\frac{\lambda+s}{c}\partial_z U(A,a,z)\right)=\lambda,
\]

or, after simplification,

\[
K=\frac{\lambda}{(\lambda+s)\{U(A,a,z)-\partial_z U(A,a,z)\}}
\]

with \(z=(\lambda+s)h/c\). Thus \(f(h)\) is the claimed transform. All factors in the denominator are positive because \(U(A,a,z)>0\) and \(-\partial_z U(A,a,z)>0\) for positive parameters (for example by the positive integral representation of Tricomi \(U\)). To confirm that the second-order reduction did not introduce a spurious solution, define \(I\) by its integral above and \(Q=cf'-(\lambda+s)f+\lambda I\). The second-order equation implies \(Q'=-(a/x)Q\); the right boundary relation implies \(Q(h+)=0\), hence \(Q=0\) everywhere. Bounded-solution uniqueness of the original stopped backward equation follows from the bounded martingale \(e^{-s(t\wedge\tau_h)}f(X_{t\wedge\tau_h})\) and letting \(t\to\infty\). This proves the exact transform.

**4. High-threshold comparison.** Construct \(E\) as the first Poisson leaching time and use the *same* event clock and jump factor for \(\tau_h\). Since the path increases until \(E\), \(\tau_h\ge E\) almost surely. At time \(E\), the salt mass is \(R(h+cE)\). Conditional on \(E\), the first event ends the excursion exactly with probability \((h/(h+cE))^a\). Therefore

\[
\Pr(\tau_h>E)=\mathbb E\left[1-(1+cE/h)^{-a}\right].
\]

The elementary inequality \(0\le1-(1+u)^{-a}\le au\) for \(u\ge0\) gives the bound \(ac/(\lambda h)\), while the common coupling bounds total variation distance. Dominated convergence applied to \(h[1-(1+cE/h)^{-a}]\), dominated by \(acE\), gives the first-order equivalence.

**5. Consistency check (known mean formula, not claimed new).** The stationary gamma density for this salt-mass process, already derived in the motivating model, has shape \(a+1\) and rate \(\lambda/c\). Combining its stationary tail with the continuous upward flux \(c\,p(h)\) yields the standard upcrossing/occupation expression

\[
\mathbb E\tau_h
=\frac{e^x\Gamma(a+1,x)}{\lambda x^a}
=\frac1\lambda\int_0^\infty e^{-t}(1+t/x)^a\,dt,
\qquad x=\frac{\lambda h}{c}.
\]

This mean decreases strictly toward \(1/\lambda\) as \(h\to\infty\), agreeing with the transform and coupling. It is included as a verification identity and as explicitly established background, not as the originality basis.

## Verification

The accompanying standalone `checker.py` independently computes the special-function transform, the gamma/incomplete-gamma mean, and an integral representation of the mean; it simulates \(30{,}000\) excursion paths for each of four dimensionally distinct parameter settings. All analytic-to-simulation comparisons passed their stated seven-standard-error margins, as did monotonic-mean tests and the first-jump probability bound. For example, at \((a,\lambda,c,h,s)=(1.8,1.5,0.6,12,2)\), the transform is approximately \(0.4223846030\), the exact mean is approximately \(0.7077264878\), and the coupling gives \(d_{\mathrm{TV}}\le0.06\). The checker uses stochastic finite-sample diagnostics, not an infinite-case proof; the proof above is analytic.

Reproduce with `python checker.py` using a Python environment with `scipy` installed. The random seeds are fixed in the script. There are no data files or other required package artifacts.

## Relationship to prior work

Suweis et al. (2012, arXiv:1207.2332) formulate the constant-deposition/Poisson-leaching soil-salt-mass model and derive its stationary gamma law and exceedance probabilities. Suweis et al. (2011, arXiv:1103.5890) explain how multiplicative jump prescriptions relate to the physical random-loss factors. These existing model definitions and stationary calculations are not claimed as new.

Tamea, Laio, Ridolfi and D'Odorico (2011) analyze generic Poisson-driven geophysical threshold crossings. They provide exact mean excursion times and infinitesimal-duration behavior, then *approximate* full excursion-duration densities by two-parameter fits (Sections 2–4); these statements do not supply this exact transform for every positive parameter.

Löpker and Stadje (2009), especially Section 4.2, study the same Beta-family jump factors in growth-collapse processes but give Kummer-\(M\) formulas for the *upward first hitting time starting below the target* (and general upward-hitting transforms). Here the initial state is exactly the threshold and the target is *downward passage by a jump*; its boundary at infinity and the selected Kummer-\(U\) solution differ. The classical Kummer equation and its special functions are used as established tools. Boxma, Perry, Stadje and Zacks (2005/2006) also study growth-collapse hitting times, defined as equality with a level reached by upward drift. Their accessible abstract does not resolve the downward-excursion comparison; the 2005 report could not be fully accessed here and remains a specific historical-priority risk. A broader exit/ruin identity might imply this result without matching wording; no universal novelty claim is made.

## Limitations

The model neglects random salt inputs, moisture/salt coupling, non-Poisson storms, variable leaching severity, and crop-specific toxicity; it describes soil salt *mass*, not direct soil-solution salinity. The exact transform is not an elementary-time-domain density; numerical inversion may be required for particular quantiles. The total-variation estimate is a rigorous upper bound, not a claimed sharp bound on that distance. No field calibration or independent audit has been performed. The literature comparison does not establish historical priority against every possible first-passage representation.

## References

- Suweis, S., Rinaldo, A., van der Zee, S. E. A. T. M., Daly, E., Maritan, A. and Porporato, A. *Stochastic Modeling of Soil Salinity*. arXiv:1207.2332 (initial public release 10 July 2012). https://arxiv.org/abs/1207.2332
- Suweis, S., Porporato, A., Rinaldo, A. and Maritan, A. *Prescription-induced jump distributions in multiplicative Poisson processes*. arXiv:1103.5890 (initial public release 30 March 2011). https://arxiv.org/abs/1103.5890
- Tamea, S., Laio, F., Ridolfi, L. and D'Odorico, P. *Crossing properties for geophysical systems forced by Poisson noise*. *Geophysical Research Letters* (online 30 September 2011), DOI:10.1029/2011GL049074. https://doi.org/10.1029/2011GL049074
- Löpker, A. H. and Stadje, W. *Hitting Times and the Running Maximum of Markovian Growth Collapse Processes*. EURANDOM Report 2009-011, May 2009, Section 4.2. https://pure.tue.nl/ws/files/3054232/643466.pdf
- Boxma, O. J., Perry, D., Stadje, W. and Zacks, S. *A Markovian Growth-Collapse Model*. EURANDOM Report 2005-033 / *Advances in Applied Probability* 38 (2006), 221–243. https://doi.org/10.1239/aap/1143936148
