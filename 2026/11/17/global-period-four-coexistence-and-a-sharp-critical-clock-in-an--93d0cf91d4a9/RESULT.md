# Global period-four coexistence and a sharp critical clock in an alternating implicit cubic map

## Finding
For the alternating implicit cubic recurrence given below, the global dynamics admit an exact two-parameter orbit census and basin partition. In the bistable region, a repelling primitive four-cycle separates the attracting persistent two-cycle from an attracting four-cycle; the separating fold and both amplitudes are explicit algebraic functions of the parameters. At the codimension-two critical point the convergence clock is \(n^-0.25\), with a sharp constant.

## Assumptions and scope
Use the alternating scalar relations of Oliveira (2026), Section 8.3, starting at phase zero:
\[
F_0(u,v)=(v-1)+(v-1)^3-u=0,\qquad
F_1(u,v)=v+v^3+(1+\mu)(u-1)+(2+\nu)(u-1)^3=0.
\]
The sequence uses \(F_0\) on even time indices and \(F_1\) on odd indices. Assume \(\mu>-1\), \(\nu>-2\), and an arbitrary real initial \(u_0\). Both implicit equations determine unique real forward states in this entire parameter domain. Define \(T(z)=z+z^3\), a strictly increasing bijection of the real line, and
\[
b=T^{-1}(a),\qquad f(a)=T^{-1}\big((1+\mu)b+(2+\nu)b^3\big),\quad a\ge0.
\]
Here \(a\) denotes the nonnegative amplitude of the even-time state. With \(a_n=|u_{2n}|\), one has \(a_{n+1}=f(a_n)\); for nonzero initial state the signed even-time states alternate. Define
\[
H(t)=t^4+3t^3+3t^2-\nu t-\mu,\quad t\ge0.
\]
Every strictly positive root \(t\) gives exactly one distinct primitive four-cycle (up to cyclic phase), with ordered states
\[
(a,1+b,-a,1-b),\quad b=\sqrt t,\quad a=b+b^3.
\]
The persistent period-two solution is \((0,1)\).

For \(\nu>0\), let \(t_c\) be the unique positive root of \(4t_c^3+9t_c^2+6t_c=\nu\), and let \(\mu_c=-3t_c^2(1+t_c)^2<0\). All case statements below are intersected with the standing restriction \(\mu>-1\); for sufficiently large \(\nu\), the fold may lie outside that restriction.

If \(\nu\le0\), precisely one positive root exists for \(\mu>0\), none for \(\mu\le0\). If \(\nu>0\), there is precisely one for \(\mu\ge0\); for \(\mu<0\), there are two when \(\mu>\mu_c\), one double root when \(\mu=\mu_c\), and none when \(\mu<\mu_c\). Positive simple roots with \(H'(t)>0\) correspond to attracting four-cycles, and those with \(H'(t)<0\) to repelling four-cycles. The double-root four-cycle is attracting only from amplitudes above it.

Every orbit converges to one of the listed periodic orbits. In particular, for \(\mu_c<\mu<0\) and \(\nu>0\), let \(0<a_-<a_+\) be the amplitudes corresponding to the two positive roots. Initial \(0\le |u_0|<a_-\) converges to \((0,1)\), initial \(|u_0|=a_-\) lies on the repelling four-cycle, and initial \(|u_0|>a_-\) converges to the attracting four-cycle of amplitude \(a_+\). For \(\mu=\mu_c\), amplitudes below the sole positive root converge to zero, while amplitudes above converge to the semistable cycle. For \(\mu>0\), or \(\mu=0,\nu>0\), every nonzero initial state converges to the unique attracting four-cycle; all other strict regimes without a positive root converge to the persistent two-cycle.

At \(\mu=\nu=0\), every nonzero initial state satisfies the sharp critical asymptotic
\[
\lim_{n\to\infty} n |u_{2n}|^4=\frac1{12}.
\]
For the additional critical half-line \(\mu=0,-2<\nu<0\), the corresponding law is \(\lim_{n\to\infty}n|u_{2n}|^2=-1/(2\nu)\).

## Proof
1. **Reduction to an increasing amplitude map.** Since \(T\) is an odd increasing bijection and \(1+\mu>0,2+\nu>0\), the even-phase return map is \(P(u)=-T^{-1}((1+\mu)T^{-1}(u)+(2+\nu)T^{-1}(u)^3)\). It is a strictly decreasing odd homeomorphism. For \(a>0\), \(P(a)=-f(a)\), and \(f\) is a strictly increasing continuous map of \([0,\infty)\) to itself. One has \(f(a)=O(a^{1/3})\) as \(a\to\infty\), so \(f(a)<a\) for sufficiently large \(a\). For any \(a_0\ge0\), monotonicity of \(f\) implies that \((f^n(a_0))\) is monotone after comparing the first two terms. The iterates are bounded and thus converge to a fixed point of \(f\). For the signed return map \(P\), even steps alternate in sign and magnitudes tend to a fixed point of \(f\). No other periodic orbit can exist: periodic amplitudes of an increasing scalar map are fixed points.

2. **Exact polynomial and its sign.** For \(a=T(b)=b+b^3\), set \(t=b^2\). Direct expansion gives
\[
(1+\mu)b+(2+\nu)b^3-T(a)=-bH(t).
\]
Since \(T\) is increasing, \(\operatorname{sgn}(f(a)-a)=-\operatorname{sgn}H(t)\). Thus positive fixed amplitudes are precisely positive roots of \(H\), with their four-cycle states as displayed. Moreover \(H''(t)=12t^2+18t+6>0\), and \(H(0)=-\mu\), \(H'(0)=-\nu\). These facts and \(H(t)\to+\infty\) establish the complete root counts. When \(\nu>0\), the unique positive minimizer satisfies \(H'(t_c)=0\); substituting \(\nu=4t_c^3+9t_c^2+6t_c\) gives \(H(t_c)=\mu_c-\mu\) with \(\mu_c=-3t_c^2(1+t_c)^2\). Therefore the claimed curve is an exact global fold, not just a local normal-form approximation.

3. **Stability and basin boundaries.** At a positive fixed amplitude, the derivative is
\[
f'(a)=\frac{1+\mu+3(2+\nu)t}{(1+3t)(1+3a^2)}.
\]
Substituting \(\mu=t((1+t)^3-1-\nu)\) yields
\[
1-f'(a)=\frac{2tH'(t)}{(1+3t)(1+3a^2)}.
\]
Every derivative is strictly positive. Hence the smaller simple positive root in the two-root case is repelling, and the larger is attracting. The period-four multiplier of the signed return is \(f'(a)^2\). On the double-root curve, \(H(t)\ge0\) on \([0,\infty)\) and is strictly positive except at the double root, so \(f(a)<a\) elsewhere: approach to the double root is possible only from above. At the persistent two-cycle, the return multiplier is \(P'(0)=-(1+\mu)\), establishing hyperbolic attraction for \(-1<\mu<0\) and repulsion for \(\mu>0\); the sign of \(H\) gives the neutral cases when \(\mu=0\). Combining these signs with monotonic convergence from Step 1 proves all global basins.

4. **Critical clock.** At \(\mu=\nu=0\), the exact identity in Step 2 implies by Taylor expansion of \(T^{-1}\) that \(f(a)=a-3a^5+O(a^7)\) as \(a\to0^+\). The root classification gives \(a_n\downarrow0\) for every \(a_0>0\). Therefore \(a_{n+1}^{-4}-a_n^{-4}\to12\); summing and dividing by \(n\) yields the limit \(n a_n^4\to1/12\). For \(\mu=0,-2<\nu<0\), similarly \(f(a)=a+\nu a^3+O(a^5)\), so \(a_{n+1}^{-2}-a_n^{-2}\to-2\nu\), proving the second limit.

## Verification
The companion `CHECK.py` is a standalone Python 3 checker (standard library only). Execute `python3 CHECK.py`. It checks exact rational identities at 35 parameter choices, verifies representative algebraic root counts and derivative signs, tests basin separation in five cases, and checks the two asymptotic constants against long numerical orbits. Expected output is a single line beginning `VERIFY_OK`. Finite tests supplement the proof; they cannot establish the all-real-parameter theorem by themselves.

## Relationship to prior work
Oliveira's 2026 paper, Section 8.3, introduced this alternating implicit system as a *local* degenerate flip example and established its fifth-order reduced coefficient and nearby period-four bifurcating solutions. We use exactly its defining equations, without claiming those reductions or the existence of a local degenerate flip as new. The present result instead identifies the full globally defined return, an exact fold across the entire regular two-parameter region, all possible cycles and their basins, and the explicit global critical relaxation law. The source's local normal form does not specify those global claims.

Elaydi and Sacker (2005) established a general obstruction to a globally asymptotically stable orbit of least period not dividing the forcing period. There is no contradiction: here the forcing has period two and the persistent period-two orbit always remains, even in parameter regimes where nearly all *other* initial states converge to a primitive four-cycle. Their result does not give this model's exact parameter boundary or basins.

## Limitations
The theorem covers the stated globally monotone implicit region \(\mu>-1,\nu>-2\) and deterministic real scalar states. It does not classify parameter ranges in which the odd implicit step can be nonmonotone or multivalued, stochastic perturbations, or numerical branch-selection mechanisms. The source's reduced fifth-order degeneracy is established earlier work; the critical law given here is an explicit dynamical consequence in this system, not a general new normal-form theorem. The 2005 global-stability paper was accessible as a repository abstract, while its complete OA PDF was inaccessible; definitive historical-priority checking remains subject to that access limitation. The result has not received independent mathematical validation.

## References
- H. M. Oliveira, *Lyapunov–Schmidt reduction for periodic orbits of implicit discrete dynamical systems*, arXiv:2611.03336v1 (2026-11-02), especially Section 8.3, equations (100)–(105). https://arxiv.org/html/2611.03336v1
- S. Elaydi and R. J. Sacker, *Global stability of periodic orbits of non-autonomous difference equations and population biology*, Journal of Differential Equations **208** (2005), 258–273, DOI:10.1016/j.jde.2003.10.024. https://digitalcommons.trinity.edu/math_faculty/47/
