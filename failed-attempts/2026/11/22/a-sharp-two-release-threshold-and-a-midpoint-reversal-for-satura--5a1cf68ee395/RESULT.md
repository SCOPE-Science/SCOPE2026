# A sharp two-release threshold and a midpoint reversal for saturating sterile-mating pressure

## Finding

A two-release intervention with exponentially surviving sterile males and a saturating mating-response law admits an **exact, unique, finite-horizon optimal waiting time**. There are two qualitatively distinct changes. First, at one sharp horizon the two releases change from simultaneous to staggered. Second, when the first release is sufficiently large relative to the second, the optimal second release crosses from **before** to **after** the midpoint of the intervention horizon. The latter crossing is not possible for equal-sized releases.

For positive normalized release sizes \(a,b\), mortality \(\mu\), horizon \(T\), and \(q=e^{-\mu T}\), define
\[
 T_c=\frac1\mu\log\left(2+\frac{b+1}{a}\right),\qquad
 y_*(T)=q+\sqrt{q^2+\frac{q(b+1)}a}.
\]
Then the unique second-release time maximizing cumulative sterile-mating pressure is
\[
 \boxed{\tau_*(T)=\begin{cases}
 0,&T\le T_c,\\[2mm]
 -\mu^{-1}\log y_*(T),&T>T_c.
 \end{cases}}
\]
When \(T>T_c\), the optimizer is strictly inside \((0,T)\), strictly increases with the horizon, and has derivative strictly between \(1/2\) and \(1\). If \(a\le b+1\), it occurs strictly before \(T/2\). If \(a>b+1\), there is a second sharp horizon
\[
 \boxed{T_m=\frac2\mu\log\frac{2a}{a-b-1}>T_c}
\]
at which \(\tau_*(T_m)=T_m/2\). The optimizer is before the midpoint for \(T_c<T<T_m\) and after it for \(T>T_m\). In particular,
\[
 \boxed{\tau_*(T)=\frac T2-\frac1{2\mu}\log\frac{b+1}{a}+o(1)\quad (T\to\infty).}
\]
These statements include every positive choice of the model parameters, with equality cases at the two critical horizons as indicated.

## Assumptions and scope

Let \(A,B,K,\mu,T>0\). Two instantaneous additions of sterile males are fixed in size at \(A\) and \(B\), the first at time \(0\), the second at a controllable time \(\tau\in[0,T]\). Sterile males do not reproduce and die independently at a constant per-capita rate \(\mu\). Thus their deterministic mean abundance is
\[
 S_\tau(t)=A e^{-\mu t}+B\,\mathbf{1}_{\{t\ge\tau\}}e^{-\mu(t-\tau)},\quad 0\le t\le T.
\]
With a fixed effective wild-male competition pool \(K>0\), the instantaneous sterile-mating fraction is \(S_\tau(t)/(K+S_\tau(t))\). We maximize the **time-integrated proxy**
\[
 J_T(\tau)=\int_0^T\frac{S_\tau(t)}{K+S_\tau(t)}\,dt.
\]
The wild-male pool, mating opportunities per unit time, and competitiveness are held constant; the fraction is a proxy, **not** the endpoint number of wild adults, human infections, or extinction probability. Set \(a=A/K\), \(b=B/K\), and \(q=e^{-\mu T}\). Simultaneous releases at \(\tau=0\) are permissible. A release at \(\tau=T\) contributes zero duration to the integral. If different physical units are used, \(A\), \(B\), and \(K\) must have the same units and \(\mu T\) must be dimensionless.

## Proof

**Step 1: exact integration.** On \([0,\tau)\), the normalized sterile abundance is \(a e^{-\mu t}\), while on \([\tau,T]\) it equals \(a e^{-\mu t}+b e^{-\mu(t-\tau)}\). Write \(y=e^{-\mu\tau}\), so \(q\le y\le1\). Direct use of \(\int \frac{c e^{-\mu t}}{1+c e^{-\mu t}}dt=-\mu^{-1}\log(1+c e^{-\mu t})\) gives
\[
 \mu J_T(\tau)=\log\frac{(1+a)(1+b+ay)y}{(1+ay)((1+aq)y+bq)}=:F_q(y).
\]
This identity is valid also at \(\tau=0\) and \(\tau=T\) by continuity; it gives, respectively, the response to one combined pulse and to the first pulse alone.

**Step 2: global—not merely stationary—optimization.** Differentiating the exact logarithm yields
\[
 F_q'(y)=\frac{-b\,g_q(y)}{y(1+ay)(1+b+ay)((1+aq)y+bq)},
 \qquad g_q(y)=ay^2-2aqy-q(b+1).
\]
Every denominator factor is strictly positive, and \(g_q'(y)=2a(y-q)\) is positive for \(y>q\). Moreover \(g_q(q)=-aq^2-q(b+1)<0\) and \(g_q(1)=a-q(2a+b+1)\).

If \(q\ge a/(2a+b+1)\), then \(g_q(y)<0\) for all \(q\le y<1\), so \(F_q\) strictly increases to its sole maximum at \(y=1\), even at equality. This is equivalent to \(T\le T_c\). If \(q<a/(2a+b+1)\), the strictly increasing quadratic \(g_q\) has exactly one zero in \((q,1)\); \(F_q\) increases before the zero and decreases after it. The sole global maximizer is therefore its positive root \(q+\sqrt{q^2+q(b+1)/a}\). Since \(\tau=-\mu^{-1}\log y\), the formula and uniqueness follow on the entire closed permissible interval, including boundaries.

**Step 3: monotonicity and limiting timing.** In the staggered regime set \(r=(b+1)/a>0\). The root equation becomes
\[
 q=\frac{y_*^2}{2y_*+r}.
\]
As \(q=e^{-\mu T}\) decreases strictly with \(T\) and the right side increases strictly with \(y_*>0\), the root \(y_*\) decreases and \(\tau_*\) increases. Implicit differentiation gives
\[
 \frac{d\tau_*}{dT}=\frac{2y_*+r}{2(y_*+r)},\qquad \frac12<\frac{d\tau_*}{dT}<1.
\]
Indeed this derivative decreases as \(T\) grows, giving strict concavity on \((T_c,\infty)\). From \(y_*=q+\sqrt{q^2+rq}\sim\sqrt{rq}\) as \(T\to\infty\), the stated additive midpoint asymptotic follows. The right derivative at onset is \((2+r)/(2(1+r))>0\), whereas the left derivative is zero: the simultaneous-to-staggered onset is a true kink.

**Step 4: the exact midpoint transition.** For \(T>T_c\), one has \(\tau_*<T/2\) precisely when \(y_*>\sqrt q\). Since \(g_q\) is strictly increasing on \([q,1]\), this is equivalent to
\[
 g_q(\sqrt q)=q\{a-b-1-2a\sqrt q\}<0.
\]
If \(a\le b+1\), this is always strict. For \(a>b+1\), the expression changes sign once when \(\sqrt q=(a-b-1)/(2a)\), yielding \(T_m\). To see this second transition occurs **after** the staggered onset, write \(r=(b+1)/a\in(0,1)\): its corresponding \(q_m=(1-r)^2/4\) is less than \(q_c=1/(2+r)\), since \((1-r)^2(2+r)<4\). Thus \(T_m>T_c\), and the strict-before/equal/strict-after statements follow with no omitted cases.

**An exact illustration.** Take \(a=4\), \(b=1\), \(\mu=1\). Then \(T_c=\log(5/2)\), \(T_m=\log16\), and at \(T_m\) the unique optimal second-release time is \(\log4=T_m/2\). At \(T=\log64\), the unique optimizer is
\[
 \tau_*=\log\frac{64}{1+\sqrt{33}}=2.2501464369\ldots>\frac{\log64}{2}.
\]
The integrated proxy is \(1.95084770295\ldots\), compared with \(1.71653604799\ldots\) for a simultaneous release. These numbers only illustrate the exact theorem and do not establish it.

## Verification

The standalone \(checker.py\) independently evaluates the integral by piecewise numerical quadrature, compares the closed expression with direct numerical integration, searches the full time interval numerically, tests both critical thresholds and the midpoint order, and checks the horizon derivative by finite differences. It passed 187,417 supplementary assertions under a deterministic random seed. The proof above, not the finite tests, establishes statements for all positive parameters. For reproduction with Python 3, execute \(python checker.py\) beside this document.

## Relationship to prior work

Almeida, Bellver-Arnau, Privat and Rebelo (first publicly posted July 21, 2023, arXiv:2307.11614; published 2024) model instantaneous sterile-mosquito releases and optimize epidemic outcomes in a coupled host-vector dynamical system. They establish general control sensitivities and study numerical allocations of multiple pulse times and quantities. The present theorem is intentionally **not a corollary of an epidemic objective**: it solves an exactly specified, different constant-wild-pool integrated mating-pressure proxy with the first release pinned and arbitrary unequal fixed release sizes.

Almeida, Duprez, Privat and Vauchelet (arXiv:2011.04449; later Journal of Differential Equations 2022) derive exact optimal controls for mosquito population systems with different state dynamics and objective functionals. Ramirez and Gordillo (2016) optimize pulsed sterile-male releases using stochastic search under population and cost constraints. Their results motivate studying pulse timing, but neither inspected statement gives this closed two-impulse response law. Wright, Winter and Duffull (2011) explain schedule dependence for saturating drug-response models, supplying a **cross-domain equivalence of mechanisms** and reducing any claim of complete conceptual novelty. Their inspected analysis does not give the above finite-horizon, pinned-first, unequal-impulse optimization and midpoint classification. The universal derivative and both exact thresholds are the mathematical contribution claimed here, not the familiar fact that nonlinear responses make timing important.

## Limitations

The contribution is a mathematical benchmark for a specified integral response, not a general optimal policy for suppressing real mosquito populations, a theorem about human incidence, or a prediction that fixed wild-male competition holds in the field. Wild adults, mating opportunities and sterile competitiveness may change in reality; release costs, stochastic survival, fitness delays, spatial effects and reproduction feedback are omitted. First-release time and both dose amounts are fixed. Other objectives can produce different schedules. Global historical priority has not been independently established; related older impulse and pharmacodynamic optimization may contain broader results not fully indexed or retrieved. No external independent mathematical validation has been performed.

## References

1. Almeida, L., Bellver-Arnau, J., Privat, Y., and Rebelo, C. *Vector-borne disease outbreak control via instant releases*. arXiv:2307.11614 (first version July 21, 2023); *Journal of Mathematical Biology* 89, 63 (2024). https://arxiv.org/abs/2307.11614 ; https://doi.org/10.1007/s00285-024-02159-9
2. Almeida, L., Duprez, M., Privat, Y., and Vauchelet, N. *Optimal control strategies for the sterile mosquitoes technique*. arXiv:2011.04449 (2020); *Journal of Differential Equations* 311 (2022), 229–266. https://arxiv.org/abs/2011.04449 ; https://doi.org/10.1016/j.jde.2021.12.002
3. Ramirez, S., and Gordillo, L. F. *Approximating Optimal Release in a Deterministic Model for the Sterile Insect Technique*. *International Journal of Agronomy* (2016), 8492107. https://doi.org/10.1155/2016/8492107
4. Wright, D. F. B., Winter, H. R., and Duffull, S. B. *Understanding the time course of pharmacological effect: a PKPD approach*. *British Journal of Clinical Pharmacology* 71 (2011), 815–823. https://doi.org/10.1111/j.1365-2125.2011.03925.x
