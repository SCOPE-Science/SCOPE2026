# Exact geometric wave trains under monotone exponential transmission in a closed SIR model

## Finding

A closed susceptible-infectious-removed (SIR) epidemic with *strictly increasing, single-exponential transmission* can display an indefinitely long sequence of strict prevalence peaks and strict incidence peaks. The mechanism is exactly integrable. Its scaled susceptible and infectious coordinates move periodically on a classical Lotka–Volterra orbit; the unscaled epidemic observables inherit that oscillation with a rigorously geometric damping envelope.

More precisely, take the assumptions below and set \(b=\gamma-a\), \(v(t)=\beta(t)S(t)/N\), \(h(t)=\beta(t)I(t)/N\). Introduce the nonnegative energy

\[
F(v,h)=v-b-b\log(v/b)+h-a-a\log(h/a).
\]

Write \(E=F(v(0),h(0))\), and define the **prevalence threshold** \(E_I=F(\gamma,a)\). Let

\[
h_c=\frac{a-b+\sqrt{(a-b)^2+8ab}}{4}>0,
\qquad E_c=F(b+h_c,h_c).
\]

For \(E>0\), the scaled coordinates have a strictly positive period \(P(E)\). Prevalence has exactly one strict local maximum and one strict local minimum per period precisely when \(E>E_I\). Incidence has exactly one strict local maximum and one strict local minimum per period precisely when \(E>E_c\). At either equality the relevant observable has a tangential stationary point, not a new local extremum, and below threshold it is strictly decreasing apart from possible tangencies at equality. At the center \(E=0\), neither observable has peaks.

For \(J\) equal to prevalence \(I\) or incidence \(c\), the exact time-shift law is

\[
J(t+P(E))=e^{-aP(E)}J(t).
\]

Consequently, once a peak exists, its infinitely many successors are geometrically smaller with constant ratio \(e^{-aP(E)}\). This is a mathematical statement about strict local extrema; it does not assert that progressively tiny peaks remain epidemiologically meaningful or pass a fixed observational prominence filter.

## Assumptions and scope

For real time \(t\geq0\), let \(S,I,R\) be nonnegative population counts with fixed \(N=S+I+R>0\), and consider

\[
\dot S=-\beta(t)SI/N,\qquad
\dot I=\beta(t)SI/N-\gamma I,\qquad
\dot R=\gamma I,
\quad \beta(t)=\beta_0e^{at}.
\]

Assume \(\gamma>0\), \(\beta_0>0\), \(0<a<\gamma\), \(S(0)>0\), \(I(0)>0\), and \(R(0)\geq0\). Define latent incidence \(c(t)=\beta(t)S(t)I(t)/N\). All peak counts refer to strict local extrema at positive real times; there is no smoothing or minimum-amplitude selection. Every full period in the scaled coordinates contains exactly the asserted number of extrema, regardless of its starting phase.

The primary MSC2020 is \(92D30\), mathematical epidemiology.

## Proof

**1. Exact change of coordinates.** Since \(\dot\beta=a\beta\), differentiation gives

\[
\dot v=a v+\frac\beta N\dot S
=av-\frac{\beta^2SI}{N^2}=v(a-h),
\]

and similarly

\[
\dot h=ah+\frac\beta N\dot I
=ah+vh-\gamma h=h(v-b),\quad b=\gamma-a>0.
\]

This is the positive predator–prey Lotka–Volterra system. Conversely, any solution \((v,h)\) with the prescribed positive initial values reconstructs \(S=Nv/(\beta_0e^{at})\), \(I=Nh/(\beta_0e^{at})\), and \(R=N-S-I\). The reconstruction satisfies all three SIR differential equations. The given admissible initial condition ensures the reconstructed \(R\) stays nonnegative because \(\dot R=\gamma I>0\). Thus the transformation is an identity for the actual epidemic trajectory, not a substitute model.

**2. First integral and periodicity.** Define

\[
F(v,h)=[v-b-b\log(v/b)]+[h-a-a\log(h/a)].
\]

A direct derivative yields

\[
\dot F=(1-b/v)v(a-h)+(1-a/h)h(v-b)
=(v-b)(a-h)+(h-a)(v-b)=0.
\]

Each bracket is nonnegative by \(z-1-\log z\geq0\) for \(z>0\), with equality only at the associated equilibrium. Hence \(F\) is strictly convex on the positive quadrant, its sublevel sets are compact and separated from both axes and infinity, and it has the unique minimizer \((b,a)\). For \(E>0\), the level set \(F=E\) is a smooth simple closed curve: its gradient vanishes only at the minimizer, and strict convexity makes the level the boundary of a compact convex disk. The vector field vanishes only at \((b,a)\), so on every such level it is continuous, tangent and nowhere zero. Each trajectory therefore runs around its level with some finite period \(P(E)>0\); uniqueness of solutions makes this period independent of the starting phase. The center level \(E=0\) is stationary.

**3. Original observables are a periodic positive factor times an exponential.** The inverse coordinates imply

\[
I(t)=\frac{N}{\beta_0}e^{-at}h(t),\qquad
c(t)=\frac{N}{\beta_0}e^{-at}v(t)h(t).
\]

Both periodic factors are positive and bounded above and below along a fixed level. Hence \(I,c\to0\), and because \(S=N e^{-at}v/\beta_0\to0\), the removed fraction tends to one. Periodicity gives the asserted exact shift identity. It also shows that each extrema's time translate by \(P(E)\) is of the same type and its magnitude is multiplied by \(e^{-aP(E)}\).

**4. Sharp prevalence threshold.** Since \(I>0\),

\[
\frac{\dot I}{I}=v-\gamma.
\]

The stationary-point locus for prevalence is the vertical half-line \(v=\gamma\). Along that line, \(h\mapsto F(\gamma,h)\) is strictly convex, tends to infinity at \(h=0\) and \(h=+\infty\), and has unique minimum at \(h=a\). Its minimum is \(E_I=F(\gamma,a)>0\), because \(\gamma>b\). If \(E<E_I\), no point of the level reaches \(v=\gamma\); since its center is at \(v=b<\gamma\), the entire orbit lies on the side \(v<\gamma\), so \(I\) decreases strictly. At \(E=E_I\), the orbit touches the line once at \((\gamma,a)\). This is the maximum of \(v\) on that orbit and \(I'\) has the same negative sign immediately before and after contact, so there is no strict peak. If \(E>E_I\), the energy level intersects the line at exactly two points with \(h<a\) and \(h>a\). At either crossing, \(\dot v=v(a-h)\ne0\), so \(v-\gamma\) changes sign. The two crossings alternate; the first has the prevalence growth sign changing negative-to-positive and the other positive-to-negative. Consequently there is exactly one strict minimum and one strict maximum of prevalence per full period, with infinitely many repeats.

**5. Sharp incidence threshold.** Directly differentiating incidence gives

\[
\frac{\dot c}{c}=
\frac{\dot\beta}{\beta}+\frac{\dot S}{S}+\frac{\dot I}{I}
=a-h+(v-\gamma)=v-h-b.
\]

Incidence stationary points lie on the positive ray \(v=b+h\), parameterized by \(h>0\). The energy restricted to this ray is

\[
\Phi(h)=F(b+h,h).
\]

It is strictly convex, with

\[
\Phi'(h)=2-\frac b{b+h}-\frac ah,
\qquad
\Phi''(h)=\frac b{(b+h)^2}+\frac a{h^2}>0.
\]

The unique critical point solves \(2h^2+(b-a)h-ab=0\), whose only positive root is the explicitly defined \(h_c\). This is the global minimum \(E_c>0\); \(\Phi(h)\to\infty\) at either endpoint. For \(E<E_c\), the entire orbit lies on the side \(v-h-b<0\), containing the center, so incidence decreases strictly. At \(E=E_c\), the orbit and ray are tangent once, and the growth sign is nonpositive on both sides: no strict extremum. For \(E>E_c\), the equation \(\Phi(h)=E\) has exactly two positive roots; the energy level intersects the ray transversally at those points, because the unique tangency along the ray is the minimum at \(h_c\). The growth sign changes at each crossing, giving exactly one strict local maximum and one strict local minimum per period.

**6. Two log-linear knots and an explicit witness.** On every finite interval \([0,T]\), \(\log\beta(t)=\log\beta_0+at\) is the linear interpolation of its values at the two endpoints. Thus the entire transmission trajectory has exactly the two-knot representation used in the motivating paper; no additional bends or forcing switches are introduced for further peaks. With \(N=\gamma=1\), \(a=1/2\), \(\beta_0=5/2\), \((S(0),I(0),R(0))=(4/5,1/5,0)\), the initial scaled point is \((v(0),h(0))=(2,1/2)\), while \(b=1/2\). Direct substitution gives

\[
E=\tfrac32-\tfrac12\log4\approx0.80685281944,
\quad E_I=\tfrac12-\tfrac12\log2\approx0.15342640972,
\quad E_c\approx0.11299357796.
\]

Both thresholds are exceeded. In this example, the peak pattern repeats indefinitely under the exponential geometric scaling, although later peaks are tiny. The numerical checker independently integrates the autonomous transformed system and verifies conserved energy and repeating peak timing. The theorem itself follows from the exact algebra and convex geometry above, not from finite numerical integration.

## Verification

The accompanying standard-library Python script `check.py` checks the exact coordinate equations and their conserved first integral numerically using fourth-order Runge–Kutta, checks both sharp thresholds for the stated rational example, and measures repeated maxima for both observables. Run it with `python check.py` (Python 3.9 or later). It is an illustrative finite check, not an exhaustive certificate for the universal theorem. The mathematical proof is independent of this computation.

## Relationship to prior work

Rabajante's 2026 paper develops peak conditions and a peak-preserving inference framework for time-varying SIR transmission, including two-knot linear interpolation of log-transmission. Its Proposition 2 states the general incidence stationary-point condition; it does not state the present fixed-one-slope exact integrability, sharp pair of energy thresholds, or the all-period geometric peak law. The present calculation specializes the transmission rate in a way that reveals additional structure; it does not dispute the paper's empirical minimal peak-preserving complexity, whose definition includes prominence, peak heights, timing, trough depth and whole-curve agreement.

The 2020/2021 CoSIR preprint of Shetty, Maheshwari, Bannur and Merugu is closer algebraically: it already maps an SIR system with an **adaptive state-dependent** transmission-control policy to Lotka–Volterra motion. Its underlying policy and transformed coordinates differ, and it studies potentially sustained infection cycles; it does not imply the exact exponentially prescribed transmission law here, the geometric decay of real prevalence and incidence, or the two stationary-locus energy thresholds. Periodic motion and the first integral of the classical predator–prey system are prior mathematics, not claimed as newly discovered. No exhaustive literature search can establish absolute uniqueness.

## Limitations

The model assumes fixed removal rate, closed population, deterministic homogeneous mixing, strictly positive initial susceptibles and infectives, and \(0<a<\gamma\). Transmission grows without bound as time increases, a deliberately mathematical limiting regime that is inappropriate as an unqualified long-horizon epidemiological forecast. The resulting infinite peaks have exponentially vanishing heights and therefore only finitely many can exceed any fixed positive measurement/prominence cutoff. The assertion of two-knot sufficiency refers to the count of unsmoothed strict local maxima on a chosen finite interval, not reproduction of arbitrary measured wave shapes or proof that an empirical optimal MPPC equals two. The claim is a self-reviewed mathematical finding, without independent audit.

## References

1. J. F. Rabajante, *How Simple Models Can Reproduce Multiple Epidemic Waves: Peak Topology, Minimal Dynamic Complexity, and Inference for Time-Varying Transmission*, arXiv:2610.05556v1 (first posted 4 October 2026), https://arxiv.org/abs/2610.05556 ; inspected full text: https://arxiv.t3mt.com/html/2610.05556v1 .
2. S. Shetty, H. Maheshwari, N. Bannur and S. Merugu, *CoSIR: Optimal control of SIR epidemic dynamics by mapping to Lotka-Volterra System*, medRxiv preprint, doi:10.1101/2020.11.10.20211995 (2020; v3 posted 6 October 2021), https://www.medrxiv.org/content/10.1101/2020.11.10.20211995v3.full.pdf .
3. S.-B. Hsu, *A remark on the period of the periodic solution in the Lotka-Volterra system*, Journal of Mathematical Analysis and Applications **95** (1983), 428–436. (Historical context for established Lotka–Volterra periodicity.)
