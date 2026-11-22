# Two explicit, opposing basin certificates in a strong-Allee tipping model

## Finding

The frozen-carrying-capacity predator–prey model of Hennessy, Popović and Sattar admits *two simultaneous, computable sufficient tests* for opposite long-time outcomes, valid for **every** positive fast–slow parameter rather than only a singular limit. One test gives a positive, entropy-defined subset of the coexistence attraction basin; the other gives an explicit large-predator subset of the extinction attraction basin. The two certificates give different certified outcomes at an identical initial prey abundance that lies *below* the fast-nullcline fold. Neither certificate purports to locate the entire separating stable manifold.

## Assumptions and scope

Fix \(0<a<1\), \((2-a)^{-1}<\phi<1\), and \(\varepsilon>0\). Consider, for \(u(0)=u_0>0\), \(v(0)=v_0>0\), the autonomous system

\[
\varepsilon\dot u=u\bigl[(1-\phi u)(u-a)-v\bigr],\qquad
\dot v=v(u-1).
\]

Time is the slow time of the originating model, and \(\phi\) is held constant. Define

\[
f(u)=(1-\phi u)(u-a),\quad v_*=(1-a)(1-\phi),\quad
u_c=a+\phi^{-1}-1\in(a,1),
\]

\[
H(u,v)=\varepsilon(u-1-\log u)+v-v_*-v_*\log(v/v_*),\quad
B=\varepsilon(u_c-1-\log u_c)>0,
\]

and \(F=(1-a\phi)^2/(4\phi)>0\). Both \(O=(0,0)\) and \(S=(1,v_*)\) are locally asymptotically stable.

**Coexistence certificate.** For every strictly positive initial condition with \(H(u_0,v_0)<B\), the unique global solution remains strictly positive and converges to \(S\). Moreover \(B\) is the largest threshold such that the complete strict relative-entropy sublevel \(\{H<B\}\) is contained in the strict dissipative half-plane \(u>u_c\). This is sharp *only as a barrier for that particular entropy sublevel*, not as a description of the attraction basin.

**Extinction certificate.** For \(0<u_0\le a\), every positive \(v_0\) gives convergence to \(O\). For \(u_0>a\), put \(c=\varepsilon\log(u_0/a)\) and let \(T>0\) be the unique solution of

\[
e^T-1-T=c/F.\]

If

\[
v_0>V_{\rm ext}(u_0):=F e^T
=-F W_{-1}\!\left(-e^{-1-c/F}\right),\]

then the prey falls strictly below its Allee level \(a\) by time \(T\), and both populations converge to \(O\). The expression is the *optimal threshold within the stated global quadratic-growth and exponential-predator comparison*, not the exact basin boundary. The real Lambert branch \(W_{-1}\) is used.

For the exact parameters \(a=1/2\), \(\phi=4/5\), \(\varepsilon=1/10\), and \(u_0=4/5\), the data \(v_0=1/10\) are certified to approach \(S=(1,1/10)\), whereas \(v_0=1/4\) are certified to approach extinction. The initial prey value \(4/5\) lies below the singular prey-nullcline fold at \(7/8\).

## Proof

**Positivity and global existence.** The coordinate axes are invariant, so positive solutions remain positive for every finite existence time. The quadratic \(f\) has global maximum \(F\); hence \(\dot u\le Fu/\varepsilon\), giving finite prey bounds on each finite time interval. Then \(\dot v\le v\max_{[0,t]}(u-1)\), giving predator bounds. Thus solutions exist globally.

**Coexistence barrier and convergence.** Differentiate the explicitly defined function \(H\). The trophic terms cancel exactly:

\[
\dot H=(u-1)\bigl[f(u)-f(1)\bigr]
=-\phi(u-1)^2(u-u_c).\tag{1}
\]

The elementary function \(z-1-\log z\) is nonnegative for \(z>0\), vanishing only at \(z=1\). Therefore \(H\ge0\), its sublevels in the positive quadrant are compact, and \(H(u_c,v)\ge B\) for all \(v>0\), with equality only when \(v=v_*\). Since \(u_c<1\), the prey contribution to \(H\) is at least \(B\) for *all* \(u\le u_c\). Consequently \(H(u_0,v_0)<B\) implies \(u_0>u_c\). Before any first crossing of \(u_c\), equation (1) makes \(H\) nonincreasing. At the putative first crossing it would have to be at least \(B\), contradicting \(H(t)\le H(0)<B\). Thus \(u(t)>u_c\) for all \(t\), and the orbit stays in its positive compact initial sublevel. The largest invariant subset of \(\{u=1\}\) in this sublevel is \(\{(1,v_*)\}\): when \(u=1\), the prey derivative equals \((v_*-v)/\varepsilon\). LaSalle's invariance principle proves convergence. At any threshold strictly above \(B\), the complete entropy sublevel includes a point with \(u<u_c\), by continuity near \((u_c,v_*)\). This is the stated sharpness.

**Extinction comparison.** For \(u_0\le a\), \(f(u)\le0\) on \((0,a]\), and \(v>0\) ensures \(u\) falls below \(a\) (instantaneously when initially equal). Once below \(a\), \(f(u)<0\) so \(u\) decreases monotonically; it cannot approach a positive limit because its per-capita derivative is strictly negative on any compact subinterval of \((0,a)\). Hence \(u\to0\), and eventually \(\dot v\le-v/2\), giving \(v\to0\).

For \(u_0>a\), positive prey implies \(\dot v=v(u-1)\ge-v\), so \(v(t)\ge v_0e^{-t}\). As \(f(u)\le F\) everywhere, integration of the exact logarithmic prey equation yields

\[
\varepsilon\log\frac{u(t)}{u_0}\le Ft-v_0(1-e^{-t}).\tag{2}
\]

Write \(c=\varepsilon\log(u_0/a)>0\). The right-hand side of (2) is strictly less than \(-c\) whenever \(v_0>R(t):=(Ft+c)/(1-e^{-t})\). The function \(R(t)\) diverges at both ends of \((0,\infty)\). Its derivative has the sign of \(F(e^t-1-t)-c\); hence there is one unique minimizer \(T>0\) satisfying the displayed equation, and \(R(T)=Fe^T\). Under the certificate, (2) gives \(u(T)<a\), after which the preceding elementary extinction argument applies. Rearranging the equation for \(T\) gives the Lambert expression, with its lower real branch because \(e^T>1+c/F\). This proves all quantifiers and both certificates.

**Example inequalities.** Here \(u_c=3/4\), \(v_*=1/10\), and

\[
H(4/5,1/10)=\tfrac1{10}\bigl[\log(5/4)-1/5\bigr]
<\tfrac1{10}\bigl[\log(4/3)-1/4\bigr]=B.
\]

Also \(F=9/80\). Taking the rational comparison time \(t=4/5\), one checks

\[
\frac9{80}\frac45-\frac14(1-e^{-4/5})
<-\frac1{10}\log(8/5).
\]

Consequently \((u_0,v_0)=(4/5,1/4)\) falls below \(a=1/2\) by that time, without depending on numerical root finding. The certified extinction root is \(V_{\rm ext}(4/5)=0.2487838970931\ldots<1/4\), and the coexistence entropy values are \(0.0023143551314\ldots<B=0.0037682072452\ldots\).

## Verification

The standalone `checker.py` recomputes the polynomial cancellation in (1) with exact rational arithmetic at many rational parameter values, tests the sharp comparison identity and uniqueness of the scalar minimizer, and checks the strict example inequalities at high precision. It also includes two independent finite-time numerical integrations as *illustrations only*. The proof above, not numerical integration or sampling, supplies the universal statements.

To reproduce, run `python checker.py` using Python 3.10 or later, with only standard-library dependencies.

## Relationship to prior work

Hennessy, Popović and Sattar formulate the frozen model as their equation (3) and analyze a singularly perturbed bistable phase portrait and a three-variable parameter-ramping system using folded-canard geometry. Their analysis establishes tipping scenarios and approximate critical ramp speeds, but the examined model, geometric-analysis, and appendix material does not give the two explicit frozen-system initial-data certificates above, nor a two-sided example below the fast fold. This finding is *not* a formula for the nonautonomous critical ramp speed.

Wang, Shi and Wei (2010/2011) study a **broader class** of strongly Allee predator–prey flows containing this one after positive time, state and parameter rescalings. Their phase-portrait and heteroclinic results establish much of the existence and geometry of the general attraction-basin boundary; we do not claim novelty for bistability, a separating curve, or uniqueness of periodic orbits. Their inspected phase portrait (Section 2), global results (Sections 3–4) and special cases (Section 5) do not state the present explicit pair of computable entropy and high-predator comparison inequalities. Van Voorn et al. (2007) likewise study the strong-Allee Lotka–Volterra model and numerical continuation of global separatrices, but their inspected formulation and global-bifurcation analysis do not supply these explicit dual initial-data certificates. The logarithmic relative-entropy technique, comparison principle, LaSalle theorem, and Lambert \(W\) manipulation are classical; novelty, insofar as the checked literature supports it, is the *particular jointly sharp-for-their-method two-sided parameter-explicit basin tests for this frozen tipping model*, rather than any general theorem about Allee systems.

## Limitations

Neither inequality is necessary for its outcome; between the sufficient regions the true basin cannot be classified by these estimates. The entropy threshold is optimal only for sublevel containment in the dissipative half-plane, and the Lambert threshold only for a specified comparison bound. The coefficients are held fixed: these results do not prove tracking or failure under a time-dependent carrying capacity. No conclusion about stochastic extinction, spatial processes, finite-population effects, or global basin-separatrix location follows. Historical priority may depend on unindexed specialized formulae, especially from the older literature on the same polynomial Lotka–Volterra–Allee class. There has been no independent audit.

## References

1. B. Hennessy, N. Popović, Z. Sattar, *A minimal model for rate-induced tipping to extinction* (2026), arXiv:2610.12319v1, first public October 8, 2026. https://arxiv.org/abs/2610.12319
2. J. Wang, J. Shi, J. Wei, *Predator–prey system with strong Allee effect in prey*, Journal of Mathematical Biology 62, 291–331 (2011), online March 12, 2010. https://doi.org/10.1007/s00285-010-0332-1; lawful author manuscript https://jxshix.people.wm.edu/shi/11-wang-shi-wei-JMB.pdf
3. G. A. K. van Voorn, L. Hemerik, M. P. Boer, B. W. Kooi, *Heteroclinic orbits indicate overexploitation in predator–prey systems with a strong Allee effect*, Mathematical Biosciences 209, 451–469 (2007). https://doi.org/10.1016/j.mbs.2007.02.006; lawful author manuscript https://www.bio.vu.nl/thb/research/bib/VoorHeme2007.pdf
