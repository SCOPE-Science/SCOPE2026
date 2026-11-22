# Exact inverse-level density and a square-root edge law for an incommensurate two-sine map

## Finding
For the incommensurate two-sine real map of Ali et al., every output strictly between its two formal amplitude bounds has infinitely many distinct real predecessors. More sharply, writing the output as \(Ac\), with \(-2<c<2\), the number \(N_c(R)\) of real solutions of \(g(x)=Ac\) in \([-R,R]\) satisfies
\[
\lim_{R\to\infty}\frac{N_c(R)}{2R}=\nu_{\alpha,\beta}(c)>0,
\]
where \(\alpha,\beta>0\), \(\alpha/\beta\notin\mathbb Q\), and
\[
\nu_{\alpha,\beta}(c)=\frac1{\pi^2}\int_{\max(-1,c-1)}^{\min(1,c+1)}\max\!\left\{\frac{\alpha}{\sqrt{1-(c-s)^2}},\frac{\beta}{\sqrt{1-s^2}}\right\}\,ds.
\]
The integral is improper at any endpoint at which a denominator vanishes; all singularities are integrable. Its exact central value and sharp endpoint laws are
\[
\nu_{\alpha,\beta}(0)=\frac{\max(\alpha,\beta)}\pi,\qquad
\nu_{\alpha,\beta}(\pm(2-\delta))=\frac{\sqrt{2(\alpha^2+\beta^2)}}{\pi^2}\sqrt\delta+o(\sqrt\delta)
\quad(\delta\downarrow0).
\]
The image of \(g\) on the entire real line is exactly \((-2A,2A)\): neither endpoint is attained. These are one-step inverse counts, not assertions about admissible backward trajectories on a bounded forward attractor.

## Assumptions and scope
Define
\[
 g(x)=A\{\sin[\alpha(x-\varphi)]+\sin[\beta(x-\varphi)]\},
\qquad A>0,\quad\alpha>0,\quad\beta>0,\quad\varphi\in\mathbb R,
\quad\alpha/\beta\notin\mathbb Q.
\]
For each real \(c\), let \(N_c(R)\) count *distinct* real roots in the *closed* interval \([-R,R]\) of \(g(x)-Ac=0\). The interval endpoints contribute at most two roots and do not affect limits. Frequencies have units of inverse state; \(\nu\) is roots per unit input length. No distribution or randomness is assigned to iterates. The amplitude \(A\) and shift \(\varphi\) do not appear in the normalized inverse density.

## Proof
**1. Image and abundance.** The two phases \((\alpha(x-\varphi),\beta(x-\varphi))\bmod 2\pi\) trace a dense orbit on the two-torus by rational independence. Therefore the range is dense in \([-2A,2A]\). Because it is a continuous image of the connected real line it is an interval, and its intermediate values are all attained. Equality \(g(x)=2A\) would require both phase angles to equal \(\pi/2\bmod 2\pi\), making \(\alpha/\beta\) a rational ratio of integers congruent to \(1\bmod4\), impossible; likewise \(g(x)=-2A\). Thus the image is exactly \((-2A,2A)\).

**2. Deterministic crossing-flux lemma.** Let \(h(\theta,\psi)=\sin\theta+\sin\psi\), and let \(v=(\alpha,\beta)\). For fixed \(c\in(-2,2)\setminus\{0\}\), the level \(h^{-1}(c)\) is a compact analytic one-dimensional level curve, smooth except for no points (the only critical values of \(h\) are \(-2,0,2\)). The line-flow \(t\mapsto(\alpha t,\beta t)\bmod2\pi\) is uniquely ergodic. On each compact transversal arc where \(|v\cdot\nabla h|>0\), flow-box coordinates and uniform equidistribution show that the asymptotic intersections per unit time equal the uniform Haar measure of the corresponding crossed tube divided by its time thickness. Exhausting transversals and shrinking neighborhoods of the finitely many tangencies yields
\[
\nu(c)=\frac1{(2\pi)^2}\int_{\mathbb T^2}\delta(h(\theta,\psi)-c)\,|v\cdot\nabla h(\theta,\psi)|\,d\theta\,d\psi.
\]
For completeness, tangencies solve \(\sin\theta+\sin\psi=c\) and \(\alpha\cos\theta+\beta\cos\psi=0\); their common solutions are finite for \(c\ne0\), as follows by eliminating \(\psi\) and obtaining a nonidentically zero polynomial in \(\sin\theta\) with finitely many roots. Since the transverse flux has vanishing mass on shrinking neighborhoods of this finite set, it does not change the limiting intersection density. Possible *exact* tangential roots have zero asymptotic density (each fixed torus point lies on the irrational line orbit at most once). The same argument can equivalently be obtained by smoothing the counting delta function, applying unique ergodicity away from those neighborhoods, then taking the smoothing thickness to zero. Thus \(N_c(R)/(2R)\to\nu(c)\). This is an application of a standard deterministic form of level-crossing/coarea counting, rather than a claim of a new general ergodic theorem.

**3. Elementary reduction of the flux.** Under normalized torus Haar measure the variables \(s=\sin\theta\) and \(t=\sin\psi\) are independent, each with density \((\pi\sqrt{1-s^2})^{-1}\) on \((-1,1)\). Conditional on \(s,t\), the signs of the cosines are independently equiprobable, giving the identity
\[
\mathbb E\bigl[|\alpha\cos\theta+\beta\cos\psi|\mid s,t\bigr]
=\max\{\alpha\sqrt{1-s^2},\ \beta\sqrt{1-t^2}\}.
\]
Set \(t=c-s\) in the coarea integral. This is exactly the displayed one-dimensional formula, including its factor \(1/\pi^2\). The integrand is strictly positive in the nonempty open integration interval, so \(\nu(c)>0\) for all noncritical \(c\in(-2,2)\).

**4. The saddle level \(c=0\).** The exact factorization
\[
\sin(\alpha u)+\sin(\beta u)=2\sin\bigl((\alpha+\beta)u/2\bigr)\cos\bigl((\alpha-\beta)u/2\bigr),\qquad u=x-\varphi,
\]
shows that the zero set consists of the union of two arithmetic progressions with spacings \(2\pi/(\alpha+\beta)\) and \(2\pi/|\alpha-\beta|\). The two progressions are disjoint because any intersection would force \(\alpha/\beta\) rational. Counting their points in \([-R,R]\) gives
\[
 N_0(R)=\frac{2R\max(\alpha,\beta)}\pi+O(1).
\]
Substituting \(c=0\) in the integral gives the same value, since the integrand becomes \(\max(\alpha,\beta)/(\pi^2\sqrt{1-s^2})\) and integrates to \(\max(\alpha,\beta)/\pi\).

**5. Endpoint asymptotics.** At \(c=2-\delta\), write \(\theta=\pi/2+u\), \(\psi=\pi/2+w\). Then \(2-h=(u^2+w^2)/2+O((u^2+w^2)^2)\), and \(v\cdot\nabla h=-(\alpha u+\beta w)+O((|u|+|w|)^3)\). For sufficiently small \(\delta>0\), the level is contained in this single neighborhood. Applying polar coordinates \((u,w)=r(\cos t,\sin t)\) to the coarea flux gives
\[
\nu(2-\delta)=\frac{\sqrt{2\delta}}{4\pi^2}\int_0^{2\pi}|\alpha\cos t+\beta\sin t|\,dt+o(\sqrt\delta)
=\frac{\sqrt{2(\alpha^2+\beta^2)}}{\pi^2}\sqrt\delta+o(\sqrt\delta).
\]
Replacing phases by their negatives gives \(\nu(-c)=\nu(c)\). This proves both endpoint laws.

## Verification
`check.py` is a *finite numerical diagnostic*, not an infinite mathematical proof. It independently computes the arcsine-max integral at several interior levels and compares it with counted sign changes on long finite trajectories for \((\alpha,\beta)=(1,\sqrt2)\). It also checks the exact central constant and the leading endpoint asymptotic. The analytic proof above—not the finite samples—establishes every limit and all parameter quantifiers.

## Relationship to prior work
Ali et al. (2023), their Map (4), define the precise two-sine dynamical system, discuss irrational frequency ratios and study equilibrium stability and bifurcation diagrams. The present quantity is instead the asymptotic **one-step inverse-level count for arbitrary targets** over an expanding *unrestricted real input window*. A published mathematical finding on the same source computes a fixed-point count in the different limit \(A\to\infty\); that statement neither supplies the density at fixed \(A\) and fixed \(c\) as \(R\to\infty\), nor its edge law. Classical almost-periodic and crossing-flux theory motivates the method and gives the underlying general flux principle; the asserted specific result is its explicit arcsine-max reduction, exact central count, and sharp endpoint constant for this published irrational two-frequency model. There is no claim of an independent invention of Kac–Rice, coarea or Kronecker–Weyl theory.

## Limitations
The count concerns unrestricted real inputs and one iteration; it does not count complete backward histories inside a compact invariant set. A noninteger frequency ratio in isolation is not equivalent to chaos of all initial conditions, and no Lyapunov or cryptographic-security assertion is made. The asymptotic has an \(o(R)\) remainder; no uniform finite-window error bound is claimed for arbitrary irrational frequencies. Specific existing but unindexed special-function treatments could affect publication priority; independent mathematical review has not occurred.

## References
1. A. M. A. Ali, S. Sriram, H. Natiq, A. Ahmadi, K. Rajagopal, S. Jafari, “A novel multi-stable sinusoidal chaotic map with spectacular behaviors,” *Communications in Theoretical Physics* **75** (2023) 115001, first published 2023-09-29. https://doi.org/10.1088/1572-9494/acf307 . Full publisher article: https://ctp.itp.ac.cn/EN/10.1088/1572-9494/acf307 .
2. P. Kurasov, R. Suhr, “Asymptotically isospectral quantum graphs and generalised trigonometric polynomials,” *Journal of Mathematical Analysis and Applications* **488** (2020), 124049, https://doi.org/10.1016/j.jmaa.2020.124049 (zero-set rigidity for almost-periodic trigonometric polynomials; does not provide the level-density formula here).
3. Classical Kronecker–Weyl equidistribution and deterministic level-crossing/coarea identity (standard methods, not claimed as original).
