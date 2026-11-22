# A unique quintic flip resonance and rational non-attainment in finite grazing returns

## Finding
For real \(0<a<1\), \(e>0\), and every integer \(M\ge2\), consider the continuous piecewise map
\[
f_\mu(x)=\begin{cases}
\nu x+e(\mu-x)^a,&x<\mu,\\
\nu x,&x\ge\mu,
\end{cases}\qquad \nu=(1+a)^{-1},\quad\mu>0.
\]
There is an explicitly defined primitive period-\(M\) orbit with exactly one nonlinear-branch visit whose multiplier is \(-1\). At its critical parameter, the **local flip type** obeys the sharp all-period dichotomy
\[
\boxed{\begin{array}{ll}
(1+a)^{M+1}<3(1-a):&\text{supercritical flip, critical cycle locally attracting},\\
(1+a)^{M+1}>3(1-a):&\text{subcritical flip, critical cycle locally repelling}.
\end{array}}
\]
For each \(M\ge2\) there is a unique real exponent \(a_M\in(0,1/2)\) solving
\[
\boxed{(1+a_M)^{M+1}=3(1-a_M).}
\]
Exactly there, the cubic term of the doubled return vanishes and its first nonzero nonlinear term is **negative quintic**. Nearby trajectories approach the critical period-\(M\) orbit at the sharp rate \(n^{-1/4}\) per doubled return, rather than the generic attracting rate \(n^{-1/2}\). Moreover, **no** rational exponent \(a=q/p\in(0,1)\) realizes equality: each genuine rational-degree case lies strictly on one side of the transition. For example, at \(a=1/4\), the primitive two-cycle flip is supercritical whereas the corresponding flips for every \(M\ge3\) are subcritical.

## Assumptions and scope
All dynamics are real. The map is evaluated locally around the explicitly constructed orbit, with \(0<a<1\), \(e>0\), \(\mu>0\), integer \(M\ge2\), and the constrained slope \(\nu=(1+a)^{-1}\). The power is taken only for positive \(\mu-x\). The theorem concerns an **exact, self-consistent one-nonlinear-visit itinerary**, not every period-\(M\) orbit or every basin. Values of \(\mu\) for small \(M\) need not be close to zero. The real-power extension admits the isolated degenerate exponent; the originating rational-degree family has rational \(a\) and hence never meets that equality.

Define
\[
\nu=(1+a)^{-1},\quad u=\nu^M,\quad
z_*={1+u\over 1+a+(1-a)u},\quad
K_*={1+u\over a}(1-z_*)^{1-a},\quad
\mu_* =\left({e\nu^{M-1}\over K_*}\right)^{1/(1-a)}.
\]
All these quantities are strictly positive, and \(\nu<z_*<1\). The physical critical cycle starts at \(x_0=\mu_*z_*\), takes its nonlinear branch once, then makes \(M-1\) linear steps and returns to \(x_0\). Its minimal period is exactly \(M\). The limiting statements below are for initial points sufficiently close to this orbit, within the same itinerary neighborhood.

## Proof
**1. Exact return and its physical itinerary.** For \(x_0=\mu z\) with \(\nu<z<1\), one nonlinear step followed by \(M-1\) linear steps gives the normalized return
\[
P_{\mu,M}(z)=u z+e\nu^{M-1}\mu^{a-1}(1-z)^a.
\]
At \(\mu=\mu_*\) the second coefficient is \(K_*\). The equations \(P(z_*)=z_*\) and \(P'(z_*)=-1\) follow directly from the formulas above. The proposed physical intermediate points are \(x_j=\mu_*z_*\nu^{j-M}\) for \(1\le j\le M-1\). Since \(z_*>\nu\), every one exceeds \(\mu_*\), while \(x_0<\mu_*\). This proves the itinerary exactly and it persists in a neighborhood. The single nonlinear visit also proves minimal period \(M\).

**2. A transverse flip.** For any nearby parameter, a fixed point \(z(\mu)\) of this return satisfies
\[
K(\mu)(1-z)^a=(1-u)z,\qquad K(\mu)=e\nu^{M-1}\mu^{a-1}.
\]
Here \(P(z)-z\) strictly decreases with \(z\), so the fixed point is unique near \(z_*\) and moves strictly upwards with \(K\). Its multiplier is
\[
\rho=u-a(1-u){z\over1-z}.
\]
Consequently it decreases strictly with \(K\), and \(K\) decreases strictly with \(\mu\). The multiplier crosses \(-1\) transversely as \(\mu\) decreases through \(\mu_*\): the primitive orbit is attracting just above \(\mu_*\) and repelling just below it.

**3. Exact cubic and quintic coefficients.** Write \(h=z-z_*\), \(d=1-z_*>0\). At the critical parameter,
\[
P(z_*+h)-z_*=-h+b_2h^2+b_3h^3+b_4h^4+b_5h^5+O(h^6),
\]
where
\[
\begin{aligned}
b_2&={(1+u)(a-1)\over2d},&
b_3&=-{(1+u)(a-1)(a-2)\over6d^2},\\
b_4&={(1+u)(a-1)(a-2)(a-3)\over24d^3},&
b_5&=-{(1+u)(a-1)(a-2)(a-3)(a-4)\over120d^4}.
\end{aligned}
\]
The doubled return has the exact Taylor expansion
\[
P^2(z_*+h)-z_*=h+A h^3+B h^4+C h^5+O(h^6),
\]
with
\[
\begin{aligned}
A&=-2(b_2^2+b_3)={ (1-a)(1+u)[1+a-3(1-a)u]\over 6(1-z_*)^2},\\
B&=b_2(b_2^2+b_3)=-\tfrac12 b_2 A,\\
C&=-b_2^2b_3-6b_2b_4+3b_3^2-2b_5.
\end{aligned}
\]
Since \(u=(1+a)^{-M}\), the sign of \(A\) is precisely the sign of \((1+a)^{M+1}-3(1-a)\). If \(A<0\), the even return attracts on both sides; when the primitive orbit loses linear stability on decreasing \(\mu\), a locally attracting doubled-period orbit is born (supercritical flip). If \(A>0\), the critical return repels and a nearby repelling doubled-period orbit lies on the linearly stable side (subcritical flip). Both assertions follow also by dividing the local fixed-point equation for the doubled return by \(h\), applying the implicit-function theorem in \(h^2\), and checking the multiplier at the nonzero solutions.

**4. Unique quintic degeneration.** The function \(3(1-a)-(1+a)^{M+1}\) decreases strictly from \(2\) to a negative value over \((0,1)\), so it has a unique zero \(a_M\). For \(M\ge2\) this zero lies below \(1/2\). At equality \(u=(1+a)/[3(1-a)]\), hence \(A=B=0\). Substitution into the exact formula for \(C\) yields
\[
\boxed{\ C=-\kappa(a),\quad
\kappa(a)={16(2-a)^2(1-a)^4(1+a)^5\over405a^4(1-2a)^3}>0\quad(a=a_M).\ }
\]
Therefore \(P^2(z_*+h)-z_*=h-\kappa h^5+O(h^6)\). Positive and negative sufficiently small deviations contract in magnitude without changing sign under the doubled return. Summing the reciprocal-fourth increment, \(|h_{n+1}|^{-4}-|h_n|^{-4}=4\kappa+O(|h_n|)\), and applying Cesàro averaging proves
\[
\boxed{\ |P^{2n}(z)-z_*|\sim(4\kappa n)^{-1/4}\quad(z\ne z_*\text{ sufficiently close}).\ }
\]
For comparison, at \(A<0\) the same argument with reciprocal squares gives \(|P^{2n}(z)-z_*|\sim(2|A|n)^{-1/2}\). When \(A>0\), every sufficiently close nonfixed point exits a fixed small neighborhood after finitely many doubled returns, with the leading escape clock \(N_\delta(h)\sim (2A h^2)^{-1}\) as \(h\to0\) from either side. At the quintic point, the nearby doubled-cycle branch on the unstable side has the degenerate fourth-root amplitude scaling; this follows from the nonzero transverse multiplier crossing and negative quintic coefficient.

**5. Arithmetic non-attainment and examples.** If \(a=r/s\in(0,1)\) is reduced and equality holds, then
\[
(s+r)^{M+1}=3(s-r)s^M.
\]
Since \(\gcd(s+r,s)=1\), this forces \(s=1\), which contradicts \(0<r<s\). Thus rational exponents always have strict criticality. For \(a=1/4\), the inequality is \((5/4)^{M+1}\lessgtr9/4\); it is strictly below at \(M=2\) and strictly above for all \(M\ge3\). The unique continuous exponent at \(M=2\) is the root of \((1+a)^3=3(1-a)\), lying between \(1/4\) and \(1/3\).

## Verification
Run `python3 verify.py` with the versions bounded in `requirements.txt`. The checker verifies the symbolic cubic identity, quartic cancellation at the cubic-zero locus, exact quintic coefficient, rational examples on both sides, high-precision quintic limits for three return lengths, and direct branch-by-branch verification of sample original-map orbits. The observed success marker is `GRAZING_FLIP_PHASE_CHECK_OK`. The analytical steps above, not the finite sample checks, prove the arbitrary-length and arbitrary-exponent statements.

## Relationship to prior work
Lima and Perdigão (arXiv:2407.02782) introduced the rational-power grazing map, constructed the induced return, and classified strict bifurcation regimes using a leading-order return. Their source includes neither the sharp all-finite-return supercritical/subcritical inequality nor the isolated fifth-order degeneration and critical relaxation exponent shown here. An earlier indexed note, *Exponentially thin attracting-cycle windows at the critical grazing slope*, proves subcritical flips for sufficiently large return lengths and gives their thin physical-parameter windows. Its exact Schwarzian formula already implies the displayed **cubic sign threshold** when combined with generic flip theory; that implication is credited rather than claimed as independently new. The additional result is the **fifth-order coefficient and its strict negative sign on the complete zero-cubic locus**, the resulting precise fourth-root critical relaxation, and rational-exponent non-attainment. Generalized-flip normal-form theory supplies the method but not these model-specific fifth-order and arithmetic facts.

## Limitations
This is a local result for the specified one-nonlinear-visit primitive orbit. No global attractor or complete periodic-point census is claimed; other itineraries may coexist. The real-power degenerate exponent lies outside the strictly rational-degree subclass but within its natural continuous exponent extension. The map is considered as an exact mathematical recurrence, and no unproved conclusion for a physical impacting flow is inferred. The source's small-parameter grazing approximation should not be confused with the possibly finite \(\mu_*\) at short return lengths. Full publication-priority completeness remains subject to unindexed literature and independently performed review.

## References
1. M. F. S. Lima and T. R. Perdigão, *One-dimensional Piecewise Smooth Rational Degree Maps*, arXiv:2407.02782v1, first posted 2024-07-03, https://arxiv.org/abs/2407.02782, especially equations (4), (34), and Theorem 1.
2. *Exponentially thin attracting-cycle windows at the critical grazing slope*, public research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exponentially-thin-attracting-cycle-windows-at-the-critical-graz--7c4f97da14ac .
3. Yu. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, second edition, Springer, 1998, Chapter 4 (generic flip-normal-form background).
