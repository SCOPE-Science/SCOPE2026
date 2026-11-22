# A critical jitter-span law for periodic acoustic monitoring

## Finding

**Theorem (complete finite-effort and critical-window law).** Fix a period \(P>0\), an effective recording-window length \(0<\ell<P\), an integer number of attempts \(m\ge1\), and a randomization span \(0<W\le P\). Suppose a target produces one instantaneous detectable call at each time \(jP+\Theta\), for integer \(j\), where the unknown phase \(\Theta\) is uniform on \([0,P)\). On attempt \(j\) a recorder opens the interval \([jP+U_j,jP+U_j+\ell]\), where \(U_j\) are independent uniform draws on \([0,W]\), independent of \(\Theta\); an interval can extend into the next nominal period. Let \(Q_m(P,\ell,W)\) be the probability that **none** of the \(m\) recording intervals contains a target call. Define

\[
a=\max\{0,W+\ell-P\},\qquad b=\min\{W,\ell\}.\]

Then **for all these parameters**, with endpoints interpreted by continuity,

\[
\boxed{\begin{aligned}
P Q_m={}&|P-W-\ell|\left(1-\frac aW\right)^m
+|W-\ell|\left(1-\frac bW\right)^m\\
&+\frac{2W}{m+1}\left[\left(1-\frac aW\right)^{m+1}
-\left(1-\frac bW\right)^{m+1}\right].
\end{aligned}}
\]

Thus \(W_0=P-\ell\) is a sharp transition separating three distinct *phase-averaged* long-monitoring regimes at fixed \(P,\ell,W\):

\[
\begin{array}{ll}
0<W<W_0:& Q_m=\frac{P-W-\ell}{P}+\frac{2W}{Pm}+o(m^{-1});\\
W=W_0:& Q_m\sim\frac{2W_0}{Pm};\\
W_0<W<P:& Q_m\sim\frac{W+\ell-P}{P}\left(\frac{P-\ell}{W}\right)^m;\\
W=P:&Q_m=\left(1-\frac\ell P\right)^m.
\end{array}
\]

The worst-phase conditional miss probability equals \(1\) for \(W\le W_0\), and equals \(((P-\ell)/W)^m\) for \(W>W_0\). In particular, full phase-averaged eventual detection at \(W=W_0\) does *not* imply any positive worst-phase detection guarantee. For fixed \(m\ge2\), full-phase randomization \(W=P\) uniquely maximizes phase-averaged detection among these uniform-span designs; for \(m=1\) every span has detection probability \(\ell/P\).

There is an exact universal near-critical window: for each fixed real \(c\), with \(W_m=W_0+c/m\) (which is feasible for all sufficiently large \(m\)),

\[
\boxed{\lim_{m\to\infty}mQ_m(P,\ell,W_m)
=\frac{(2W_0+|c|)\exp(-\max\{c,0\}/W_0)}P.}
\]

These are properties of the specified stochastic observation model, **not** assertions that whale songs occur at perfectly deterministic periods.

## Assumptions and scope

- The true calling phase is shared across all attempts and is uniform only when averaging over an unknown phase; the worst-phase assertion allows every deterministic phase.
- There is exactly one, perfectly recognized point call per period. If a call occupies time \(d\) and must be entirely captured, \(\ell\) can be interpreted as the available start-time interval after subtracting \(d\) from physical listening duration, when positive.
- Recording starts are independently re-randomized between attempts. A common random offset is **not** equivalent. When a window wraps a period boundary or overlaps another window, detection uses the union, with no double credit for a call.
- No ecological inference is made from false detections, irregular calling, phase drift, imperfect classification or shared environmental conditions.

## Proof

**1. Conditional miss.** Fix \(\Theta=\theta\). A recording contains a call exactly when the modulo-\(P\) start \(U_j\) lies in the length-\(\ell\) circular arc ending at \(\theta\). Its intersection length with the uniform allowed-start arc \([0,W]\) is \(h(\theta)\). Therefore the conditional hit probability per independent attempt is \(h(\theta)/W\), and conditional miss over \(m\) attempts is \((1-h(\theta)/W)^m\). Consequently

\[Q_m=\frac1P\int_0^P\left(1-\frac{h(\theta)}W\right)^m\,d\theta.\]

**2. Complete overlap profile.** For two circular arcs of lengths \(W,\ell\) on a circumference \(P\), the intersection length as one arc translates has minimum \(a=\max\{0,W+\ell-P\}\) and maximum \(b=\min\{W,\ell\}\). When \(W+\ell\le P\), the arcs are disjoint for a phase set of length \(P-W-\ell\); when \(W+\ell>P\), applying the same disjoint-arc argument to their complements yields a minimum-intersection plateau of length \(W+\ell-P\). In both cases the maximal-intersection plateau has length \(|W-\ell|\), and the remaining two ramps are linear with slope \(+1\) or \(-1\), each lasting phase length \(b-a\). Indeed \(|P-W-\ell|+|W-\ell|+2(b-a)=P\). This also holds in the limit \(W=P\), when \(a=b=\ell\).

**3. Exact integration.** Integrating the two plateau contributions and the two linear ramps in the integral of step 1 gives

\[
P Q_m=|P-W-\ell|(1-a/W)^m+|W-\ell|(1-b/W)^m
+2\int_a^b(1-t/W)^m\,dt,
\]

and evaluating the integral establishes the boxed finite-\(m\) identity. This proves all boundary cases, including \(W=\ell\), \(W+\ell=P\), and \(W=P\), without exceptional limiting conventions for \(m\).

**4. Long-effort and worst-phase laws.** For \(W<W_0\), \(a=0\) and the minimum plateau has strictly positive length \(P-W-\ell\); all other factors involving \(1-b/W\) decay geometrically because \(b>0\). The ramp term equals \(2W/(P(m+1))+o(m^{-1})\). At \(W=W_0\) the minimum plateau vanishes, leaving the inverse-\(m\) ramp law. For \(W_0<W<P\), \(a>0\), the strictly positive minimum plateau dominates the ramp term by a factor of order \(m\), while \(1-b/W<1-a/W\); this yields the geometric law. At \(W=P\), every phase has hit probability \(\ell/P\). The least conditional hit probability over all phases is exactly \(a/W\), establishing the worst-phase formula, including zero-probability isolated phases at the critical point.

**5. Unique phase-averaged optimal span.** Fubini's theorem on the phase circle gives \(P^{-1}\int_0^P h(\theta)/W\,d\theta=\ell/P\). For \(m\ge2\), \(x\mapsto(1-x)^m\) is strictly convex on \((0,1)\) (and strictly convex on \([0,1]\) for these integer powers). Jensen's inequality gives \(Q_m\ge(1-\ell/P)^m\). Equality requires phase-constant \(h/W\), which occurs exactly when \(W=P\): for every \(W<P\) and \(0<\ell<P\), the overlap ramps have positive length. For \(m=1\), phase averaging gives \(Q_1=1-\ell/P\) for every \(W\).

**6. Near-critical crossover.** Put \(W_m=W_0+c/m\), and write \(c_+=\max\{c,0\}\). Then \(a=c_+/m\), the minimum plateau has length \(|c|/m\), and \((1-a/W_m)^m\to e^{-c_+/W_0}\). Because \(b\to\min\{W_0,\ell\}>0\), the maximal-plateau and high-end ramp terms are exponentially small. Multiplying the exact identity by \(m\) leaves \((|c|+2W_0)e^{-c_+/W_0}/P\), as asserted.

## Verification

The accompanying `check.py` uses an **independent** circular-interval intersection algorithm to evaluate the conditional hit function, then performs deterministic midpoint quadrature to compare its phase integral against the closed formula. It separately tests rational boundary inputs, Jensen's bound, and the two asymptotic regimes and crossover; it is supportive numerical evidence rather than a substitute for the proof. Run using `python3 check.py` in the directory containing `check.py`. No external package is needed.

For example, at \(P=60\) minutes, \(\ell=10\) minutes and \(W=40\) minutes, the undetectable-phase mass remains \((60-40-10)/60=1/6\), no matter how many independent recording cycles are attempted. The exact critical randomization span is \(W_0=50\) minutes; at this span, phase-averaged miss decays on the order of \(1/m\), while at \(W=55\) minutes it decays geometrically with base \(10/11\).

## Relationship to prior work

Michel et al. (2024) empirically examine how fixed duty cycles affect several blue-whale acoustic monitoring metrics; the source's methods compare fixed recurring listening periods and phases. Balantic and Donovan (2019) optimize wildlife acoustic sampling using modeled vocal-availability probabilities, and Rand et al. (2022) empirically compare duty-cycle protocols for killer whales. Their observed effects motivate the distinction between recording fractions and phase coverage. None of those read sections claims the exact independently re-randomized bounded-offset model or its critical exponent.

Classical random-circle coverage mathematics (for example Siegel and Holst 1982) treats arcs with *uniform locations over the whole circle* and asks different coverage and gap questions. The present observation model restricts every start to a proper phase arc and averages the non-detection of a **shared unknown target phase**. Standard independent-coverage conditioning supplies a starting identity; the contribution assessed here is the complete restricted-span finite formula and its sharp floor/polynomial/exponential phase boundary. The result is an analytic idealization, not a claim of exhaustive historical priority.

## Limitations

Perfect periodicity and a persistent phase are strong assumptions; biological call trains may drift or skip. The phase-averaged claim is different from a worst-case reliability guarantee. Recording overlap under jitter may reduce actual total powered-on time compared with nominal \(m\ell\); no fixed-energy optimality beyond equal window lengths and the specified randomization family is proved. Claims do not cover nonuniform jitter laws, changing call periods, or multiple acoustic populations. Historical comparison remains subject to incompletely indexed applied sampling literature and general circle-coverage results.

## References

1. Michel, M., Torterotot, M., Royer, J.-Y., and Samaran, F. (2024). *Effects of duty cycle on passive acoustic monitoring metrics: The case of blue whale songs*. Journal of the Acoustical Society of America 155, 2538–2548. First online 2024-04-09. https://doi.org/10.1121/10.0025545
2. Balantic, C., and Donovan, T. (2019). *Temporally adaptive acoustic sampling to maximize detection across a suite of focal wildlife species*. Ecology and Evolution 9, 10582–10600. https://doi.org/10.1002/ece3.5579
3. Rand, Z. R., Wood, J., and Oswald, J. (2022). *Effects of duty cycles on passive acoustic monitoring of southern resident killer whale occurrence and behavior*. Journal of the Acoustical Society of America 151, 1651–1660. https://doi.org/10.1121/10.0009752
4. Siegel, A. F., and Holst, L. (1982). *Covering the circle with random arcs of random sizes*. Journal of Applied Probability 19, 373–381. https://doi.org/10.2307/3213488
