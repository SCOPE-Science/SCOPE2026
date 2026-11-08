# Exact survival interval and an upper-density bottleneck crossover in the generalized Allee-logistic map

## Finding

For the generalized Allee-logistic map
\[
 f_r(x)=rx(1-x)(c+mx),\qquad c=1-m(1+h),
\]
consider the strong-Allee fold regime \(0<m\le1\), \(0\le h\le1\), and \(0<c<m\). Put
\[
 \rho=\frac{m-c}{2m}\in(0,\tfrac12),\qquad
 r_b=\frac{4m}{(m+c)^2},\qquad
 a=1-\rho,\qquad
 s=\frac{\rho+\sqrt{\rho^2+4a^2}}2.
\]
At the fold \(r=r_b\), the exact basin of the positive semistable fixed point \(\rho\) inside the physical density interval \([0,1]\) is \([\rho,s]\). Every other initial density in \([0,1]\) converges to zero. For every \(x_0\in(\rho,s)\),
\[
 \lim_{n\to\infty} n(x_n-\rho)=\frac{a^2}{\rho}.
\]

Now set \(r=(1-\varepsilon)r_b\), \(\varepsilon\in(0,1)\). Every physical-density trajectory becomes extinct. Fix any \(\eta\in(0,\rho)\) and define the first downward crossing
\[
 N_\eta(x_0,\varepsilon)=\min\{n\ge0:x_n\le\rho-\eta\}.
\]
The square-root-scaled extinction-delay limits are
\[
 \lim_{\varepsilon\downarrow0}\sqrt\varepsilon\,N_\eta(x_0,\varepsilon)
 =\begin{cases}
 \pi a/\rho,&\rho<x_0<s,\\
 \pi a/(2\rho),&x_0=s,\\
 0,&s<x_0\le1.
 \end{cases}
\]
More strongly, for each fixed \(\zeta\in\mathbb R\) and \(x_0(\varepsilon)=s+\zeta\sqrt\varepsilon\) (which belongs to \([0,1]\) for all sufficiently small \(\varepsilon\)), the entire threshold layer has the exact profile
\[
 \boxed{\lim_{\varepsilon\downarrow0}\sqrt\varepsilon\,
 N_\eta(s+\zeta\sqrt\varepsilon,\varepsilon)
 =\frac{a}{\rho}\left[\frac\pi2-
 \arctan\left(\frac{2-\rho/s}{a}\zeta\right)\right].}
\]
The profile distinguishes a full fold passage, a half passage, and immediate upper-density extinction, without asserting a new generic saddle-node exponent.

## Assumptions and scope

The domain is the full physical interval \(x_0\in[0,1]\); time is integer-valued \(n\ge0\). Parameters obey \(c=1-m(1+h)\) with \(0<m\le1\), \(0\le h\le1\), and \(0<c<m\). The derived \(\rho\) lies strictly between zero and one half, so \(\rho<s<1\). All limits hold at fixed admissible \(m,h,\eta\) and, in the layer statement, fixed real \(\zeta\). This is a deterministic statement, with neither stochastic extinction nor spatial migration.

## Proof

**Exact fold normalization.** Substitution gives the polynomial identity
\[
 F(x):=f_{r_b}(x)=x\left(1-\frac{(x-\rho)^2}{a^2}\right),\qquad
 F(x)-x=-\frac{x(x-\rho)^2}{a^2}.
\]
For \(0\le x\le1\), the factor in parentheses is nonnegative, and \(0\le F(x)\le x\le1\). The only fixed points are \(0\) and \(\rho\). A second exact identity is
\[
 F(x)-\rho=(x-\rho)
 \left(1-\frac{x(x-\rho)}{a^2}\right).
\]
For \(x>\rho\), the second factor changes sign once, at the unique positive root \(s\) of \(s(s-\rho)=a^2\). The root belongs to \((\rho,1)\) because \(\rho>0\) and \(1-\rho=a\). Therefore \(F((\rho,s))\subset(\rho,s)\) and its iterates decrease to \(\rho\), while \(F(s)=\rho\). For \(0\le x<\rho\), and for \(s<x\le1\) after one iterate, the monotone orbit stays below \(\rho\) and tends to zero. This proves the sharp basin boundary and excludes nontrivial periodic orbits at the fold.

**Parabolic rate.** For \(u_n=x_n-\rho>0\) along \(x_0\in(\rho,s)\),
\[
 u_{n+1}-u_n=-\frac{(\rho+u_n)u_n^2}{a^2}.
\]
Since \(u_n\downarrow0\), the reciprocal difference tends to \(\rho/a^2\), proving \(n u_n\to a^2/\rho\) by Stolz--Cesàro or summation of reciprocal increments.

**Below-fold extinction.** The perturbed map has the exact form
\[
 F_\varepsilon(x)=(1-\varepsilon)F(x),\quad
 F_\varepsilon(x)-x=-x\left[\varepsilon+
 (1-\varepsilon)\frac{(x-\rho)^2}{a^2}\right].
\]
Consequently \(0\le F_\varepsilon(x)\le(1-\varepsilon)x\) on \([0,1]\); all orbits tend to zero, and the downward crossing time is finite.

**Bottleneck clock.** For \(u_n=x_n-\rho\) write the exact recurrence
\[
 u_{n+1}-u_n=-(\rho+u_n)\left[
 \varepsilon+(1-\varepsilon)\frac{u_n^2}{a^2}\right].
\]
On the scale \(u_n=a\sqrt\varepsilon\,v_n\), the rescaled time increment is \(\Delta\tau=(\rho/a)\sqrt\varepsilon\), and the limiting differential equation on bounded \(v\) intervals is
\[
 \frac{dv}{d\tau}=-(1+v^2),\qquad
 \arctan v(\tau)=\arctan v(0)-\tau.
\]
This limit can also be justified directly without extending an Euler estimate to infinite \(v\): for any fixed sufficiently small \(\delta>0\), the integral identity for the arctangent increment shows, uniformly while \(|u_n|\le\delta\),
\[
 \arctan\frac{u_{n+1}}{a\sqrt\varepsilon}-
 \arctan\frac{u_n}{a\sqrt\varepsilon}
 =-\frac\rho a\sqrt\varepsilon\bigl(1+O(\delta)+o_\varepsilon(1)\bigr).
\]
Indeed the exact step changes \(u\) by at most \(O(\varepsilon+\delta^2)\) and changes its nonzero magnitude by relative \(O(\delta)\) away from the central \(O(\sqrt\varepsilon)\) layer; the central layer follows by uniform smooth Euler convergence. Outside \([\rho-\delta,\rho+\delta]\), the number of iterates to a fixed outer threshold is bounded as \(\varepsilon\downarrow0\), for each fixed \(\delta\), by monotone comparison with the fold map. Thus the rescaled outer contribution vanishes. Passing first \(\varepsilon\downarrow0\), then \(\delta\downarrow0\), gives the limiting arctangent passage time.

For fixed \(x_0\in(\rho,s)\), the fold orbit enters the upper side of this layer in finite time for every fixed \(\delta\), with scaled entrance coordinate tending to \(+\infty\). The lower exit coordinate tends to \(-\infty\), giving a total arctangent excursion \(\pi\). For fixed \(x_0>s\), already \(F(x_0)<\rho\) and the fold orbit reaches \(\rho-\eta\) in finitely many steps, so the scaled time vanishes.

**Upper-preimage crossover.** The exact fold derivative at the nontrivial preimage is
\[
 F'(s)=\frac\rho s-2<0.
\]
Taylor expansion of the first perturbed step gives
\[
 F_\varepsilon(s+\zeta\sqrt\varepsilon)
 =\rho+\left(\frac\rho s-2\right)\zeta\sqrt\varepsilon+O(\varepsilon),
\]
so the scaled coordinate after the first step tends to
\[
 v_1\longrightarrow-\frac{2-\rho/s}{a}\zeta.
\]
Its arctangent distance to the lower exit \(-\pi/2\) is \(\pi/2+\arctan(v_1)\), yielding the boxed law. Taking \(\zeta=0\) gives the half-passage value at \(s\), and taking fixed \(x_0\in(\rho,s)\) or \(x_0>s\) produces the other two cases. No uniformity in unbounded \(\zeta\) is asserted.

## Verification

The accompanying `verify.py` checks the fold polynomial identities exactly using SymPy, verifies the upper cutoff, and evaluates finite orbit passage times at three distinct fold densities. For \(\varepsilon=10^{-7}\), it compares nine scaled crossover times (three fold densities and three layer shifts), three full passage times, and three high-density immediate-extinction cases with their formulas. The finite computations corroborate but do not prove the limiting law; the proof above supplies the universal quantifiers.

## Relationship to prior work

Pires, Andrade, and Herrmann (2026) introduce the exact GAL map and determine the stationary-state fold \(r_b\), tricriticality and scaling at the *extinction* and tricritical thresholds. Their public complete article does not state a sharp fold-survival interval, the fold ghost passage clock, or the initial-density boundary layer at \(s\).

Classical local saddle-node bottleneck exponents and finite-time scaling functions are established, including Corral, Sardanyés, and Alsedà (2018) and Corral (2025). The \(\varepsilon^{-1/2}\) exponent or arctangent normal form alone is **not claimed as new**. The result here combines the exact global surviving interval of this particular cubic density map with its explicit high-density preimage and the preimage-scale crossover coefficient. Vortkamp, Schreiber, Hastings, and Hilker (2020) analyze survival basins and long transients for another Allee population map; their model and assumptions do not determine this cubic fold profile.

## Limitations

The statement concerns exactly the fold and its approach from below; it does not classify the bistable parameter interval above the fold, nonautonomous environmental forcing, noise, or population discreteness. Classical generic fold theory may subsume portions of the local slowing argument; the novelty claim is limited to the model-specific sharp basin and upper-preimage crossover. Priority outside the inspected primary sources and cited comparisons remains provisional. No independent scientific audit has been performed.

## References

1. M. A. Pires, J. S. Andrade Jr., H. J. Herrmann, *Tricriticality and chaos in a generalized Allee-logistic map* (2026), arXiv:2606.05351v1, https://arxiv.org/abs/2606.05351.
2. A. Corral, J. Sardanyés, L. Alsedà, *Finite-time scaling in local bifurcations*, Scientific Reports **8**, 11783 (2018), https://doi.org/10.1038/s41598-018-30136-y.
3. A. Corral, *Universal finite-time scaling in the transcritical, saddle-node, and pitchfork discrete and continuous bifurcations*, Chaos **35**, 013106 (2025), arXiv:2405.19947, https://arxiv.org/abs/2405.19947.
4. I. Vortkamp, S. J. Schreiber, A. Hastings, F. M. Hilker, *Multiple Attractors and Long Transients in Spatially Structured Populations with an Allee Effect*, Bulletin of Mathematical Biology **82**, 82 (2020), https://doi.org/10.1007/s11538-020-00750-x.
5. D. A. Martin, Q.-Y. Tang, D. R. Chialvo, *Finite-time scaling on low-dimensional map bifurcations*, Physical Review Research **7**, 043241 (2025), https://doi.org/10.1103/73cc-j6mx.
