# A unique damping threshold for reentrant stationary kurtosis in a telegraph-driven oscillator

## Finding
Let \(a,z>0\). A stationary symmetric two-state process \(\sigma_t\in\{-1,1\}\) flips signs at rate \(a\), and a driven harmonic oscillator obeys
\[
\ddot x_t+2z\dot x_t+x_t=\sigma_t.
\]
In its unique stationary state define \(\kappa_4(a,z)=\mathbb E[x_t^4]-3(\mathbb E[x_t^2])^2\). Define the polynomial
\[
\begin{aligned}
P(a,z)={}&48a^5+384a^4z+1152a^3z^2+104a^3
+1632a^2z^3+448a^2z\\
&+1104az^4+476az^2-9a+288z^5+132z^3+12z.
\end{aligned}
\]
There exists exactly one \(z_c>0\), numerically \(z_c\approx0.04243926674427\), for which a positive \(a_c\) satisfies \(P(a_c,z_c)=\partial_aP(a_c,z_c)=0\). Numerically \(a_c\approx0.10961017659535\). The **complete fourth-cumulant sign classification** is:

1. If \(0<z<z_c\), there are exactly two positive rates \(0<a_-(z)<a_+(z)\) satisfying \(P(a_\pm(z),z)=0\), and \(\kappa_4>0\) exactly for \(a_-(z)<a<a_+(z)\); outside that interval \(\kappa_4<0\).
2. If \(z=z_c\), the fourth cumulant vanishes only at \(a=a_c\) and is negative at all other positive switching rates.
3. If \(z>z_c\), then \(\kappa_4<0\) for all \(a>0\).

Thus sufficiently weak damping produces a negative–positive–negative sign sequence as the telegraph switching rate increases, despite the forcing being symmetric and bounded. The threshold is mathematically unique, not merely a numerical crossing.

## Assumptions and scope
The oscillator has dimensionless natural frequency one, restoring coefficient one, damping coefficient \(2z\), and telegraph driving amplitude one. The sign process switches independently of position and velocity. Switching rate \(a\), damping \(z\), and time are physical dimensionless parameters. The stationary causal oscillator is well defined for every \(z>0\), because the deterministic impulse response decays exponentially. The joint stationary state \((x,v,\sigma)\), with \(v=\dot x\), is symmetric under \((x,v,\sigma)\mapsto(-x,-v,-\sigma)\), so odd position moments vanish. The fourth cumulant refers to an instantaneous stationary position, not an integrated-time displacement cumulant.

## Proof
**1. Exact stationary generator and moments.** The joint generator is
\[
\mathcal Lf=v\partial_xf+(-x-2zv+\sigma)\partial_vf
+a\bigl[f(x,v,-\sigma)-f(x,v,\sigma)\bigr].
\]
For \(M_{pqs}=\mathbb E[x^pv^q\sigma^s]\) with \(p,q\ge0\), \(s\in\{0,1\}\), stationarity yields
\[
\begin{split}
0={}&pM_{p-1,q+1,s}-qM_{p+1,q-1,s}-2zqM_{p,q,s}\\
&+qM_{p,q-1,1-s}-2asM_{p,q,s}.
\end{split}
\]
Terms with vanishing prefactors are omitted. Symmetry forces \(M_{pqs}=0\) whenever \(p+q+s\) is odd. For degrees one through four, these are finite nonsingular linear systems over the positive parameter quadrant. Successive exact solution gives
\[
\mathbb E[x^2]=\frac{a+z}{z(4a^2+4az+1)},
\]
and the fourth cumulant factors as
\[
\boxed{\displaystyle
\kappa_4(a,z)=-\frac{3P(a,z)}{D(a,z)},
}\]
where
\[
D(a,z)=2z(3z^2+1)(4a^2+4az+1)^2(4a^2+12az+9)(4a^2+12az+8z^2+1).
\]
All factors of \(D\) are strictly positive for \(a,z>0\). The complete exact recurrence and symbolic checks are reproducible by running `python verify.py` with SymPy.

**2. Strict convexity and monotonicity.** Differentiating the explicitly displayed polynomial shows
\[
\partial_a^2P(a,z)>0,\qquad\partial_zP(a,z)>0
\quad\text{for every }a,z>0.
\]
Indeed, every monomial of \(\partial_a^2P\) and \(\partial_zP\) has a positive coefficient; the only negative term in \(P\), namely \(-9a\), disappears under either of these derivatives except for its first \(a\)-derivative. Also
\[
P(0,z)=12z+132z^3+288z^5>0,
\quad\lim_{a\to\infty}P(a,z)=+\infty.
\]
Let \(m(z)=\min_{a\ge0}P(a,z)\). Coercivity makes this minimum attained and continuous in \(z>0\). It is strictly increasing: for \(z_2>z_1>0\), a minimizer \(a_2\) at \(z_2\) gives
\[
m(z_2)=P(a_2,z_2)>P(a_2,z_1)\ge m(z_1),
\]
including when \(a_2=0\), since \(\partial_zP>0\) also at \(a=0\). At zero damping the limiting polynomial factors as
\[
P(a,0)=48a\left(a^2-\frac1{12}\right)\left(a^2+\frac94\right),
\]
which is negative for any \(0<a<1/\sqrt{12}\). Hence \(m(z)<0\) for all sufficiently small \(z>0\). At \(z=1\), \(P(0,1)>0\) and \(\partial_aP(0,1)>0\), so strict convexity yields \(P(a,1)>0\) for every \(a\ge0\). Thus \(m(1)>0\). By continuity and strict monotonicity there is exactly one \(z_c\in(0,1)\) with \(m(z_c)=0\).

**3. Number of zero crossings.** At \(z_c\) the minimizer cannot occur at \(a=0\), because \(P(0,z_c)>0\), so \(a_c>0\), \(\partial_aP(a_c,z_c)=0\). Strict convexity makes \(a_c\) unique. For \(z<z_c\), \(P\) starts positive at zero, has a negative interior minimum, and diverges to positive infinity. Strict convexity implies precisely two positive zeros; \(P\) is negative precisely between them. For \(z>z_c\), \(P\) remains strictly positive. The sign of \(\kappa_4\) follows by the exact factorization in step 1. The quoted decimals are numerical solutions of the polynomial equations, not independent certificates of uniqueness.

## Verification
The standalone `verify.py` reconstructs the symmetric stationary moment equations through total degree four from the generator. It symbolically proves the variance and fourth-cumulant identities over formal positive parameters and separately solves the moment equations at four different rational parameter pairs, comparing exact rational results. It also checks the zero-damping factorization and an exact negative-polynomial witness. SymPy is the only nonstandard dependency; `requirements.txt` specifies it. Finite parameter checks corroborate but do not establish the infinite-parameter sign classification, which is proved by monotonicity and convexity above.

## Relationship to prior work
Pawula (1987) studied higher-order linear oscillators driven by random telegraph noise and derived a general moment representation. Its general moment methods are antecedents, not claimed as new. A full-text comparison could not be completed: the publication abstract was available but the complete paper was not accessible. Pawula (1987, later paper) developed moment-based distribution approximations and is similarly acknowledged.

Smith and Farago (2022) studied the exact same linear telegraph-forced oscillator in their model equation, with focus on the rapid-switching large-deviation stationary position distribution, support, and underdamped/overdamped geometry. Their article was inspected in the introduction, theoretical framework, asymptotic discussion, and the asymptotic discussion; no full-rate classification of fourth-cumulant signs or unique damping threshold was located. Their work supplies the direct model and a different limiting observable. Generic moment representations could imply the rational cumulant formula after algebra, but they do not by themselves state the unique sign-phase classification proved here. This distinction is the proposed contribution, subject to the documented full-text comparison risk.

## Limitations
The result concerns a *single*, *linear*, *stable* oscillator with strictly positive damping and symmetric Poisson telegraph forcing at fixed unit amplitude. It does not prove a phase transition in an infinite system, a claim about the full stationary density, or any universality under nonlinear forces, asymmetric noise, additional thermal Gaussian noise, or time-dependent parameters. The limit \(z\downarrow0\) is singular: no normalizable stationary oscillator state is claimed at zero damping. The general moment work of Pawula (1987) is a material unresolved originality comparison because its full text was inaccessible; independent bibliographic and scientific review has not been performed.

## References
1. R. F. Pawula, “Dichotomous-noise-driven oscillators,” *Physical Review A* **35**, 3102–3108 (1987), DOI: 10.1103/PhysRevA.35.3102; publicly dated 1987-04-01. Abstract inspected; full text unavailable.
2. R. F. Pawula, “Approximating distributions from moments,” *Physical Review A* **36**, 4996–5007 (1987), DOI: 10.1103/PhysRevA.36.4996. Abstract inspected; full text unavailable.
3. N. R. Smith and O. Farago, “Nonequilibrium steady state for harmonically-confined active particles,” arXiv:2208.06848 (2022), https://arxiv.org/abs/2208.06848. Article body inspected.
