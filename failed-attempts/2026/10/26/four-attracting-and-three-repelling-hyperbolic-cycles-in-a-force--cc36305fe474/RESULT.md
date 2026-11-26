# Four attracting and three repelling hyperbolic cycles in a forced three-zone equation

## Finding
For the continuous scalar time-periodic differential equation
\[
\dot x=-9x+\frac{21}{2}\operatorname{sat}(x)+\frac{181363}{100000}\sin t,
\]
where \(\operatorname{sat}(x)=\max(-1,\min(x,1))\), there exist at least **seven distinct hyperbolic \(2\pi\)-periodic solutions**, **four attracting and three repelling**. In particular, these seven periodic solutions all persist, with the same respective stability types, for every sufficiently small variation of the three positive parameters in the family \(\dot x=-Ax+(A+B)\operatorname{sat}(x)+\mu\sin t\). For the three shooting intervals below there is exactly one periodic solution in each, not merely at least one.

The original seven-cycle construction establishes their existence and isolation but does not establish hyperbolicity of the six noncentral cycles. The new result classifies their linear stability and provides a rigorous quantitative separation of their Floquet multipliers from unity. No claim of global seven-cycle maximality is made.

## Assumptions and scope
Consider \(A=9\), \(B=3/2\), and \(\mu=181363/100000\). The Poincaré map \(P(y)=x(2\pi;y)\) takes initial condition \(x(0)=y\). Define the rational shooting intervals
\[
J_1=[-0.569204,-0.569203],\quad J_2=[-0.55677,-0.55675],\quad J_3=[-0.55517,-0.55514].
\]
All decimals in these intervals denote exact rational numbers. The source paper rigorously establishes transverse four-event itineraries on the broader interval \([-0.571,-0.567]\) containing \(J_1\), transverse four-event itineraries on \(J_2\), and transverse two-event itineraries on \(J_3\). Its central antisymmetric orbit lies below these shooting intervals. We use those established itinerary statements, not numerical assumptions about first-hitting events.

## Proof
Write \(D(y)=P(y)-y\). In a middle-zone segment \(|x|<1\), the scalar derivative of the vector field is \(B=3/2\); in exterior segments it is \(-A=-9\). Thus for any periodic solution on the certified transverse itineraries, if \(E\) is its **total exterior residence time** during a forcing period, the return multiplier obeys the exact identity
\[
P'(y)=\exp(3\pi-\tfrac{21}{2}E).
\]
It is therefore attracting precisely when \(E>2\pi/7\), and repelling precisely when \(E<2\pi/7\). The equality would be nonhyperbolic.

For each of the six rational shooting endpoints listed above, calculate the exact affine flow using
\[
\Phi_{c,d}(t;t_0,y_0)=e^{-c(t-t_0)}y_0-\frac{d}{c}(1-e^{-c(t-t_0)})+\frac{\mu}{1+c^2}\bigl[c\sin t-\cos t-e^{-c(t-t_0)}(c\sin t_0-\cos t_0)\bigr].
\]
The middle, lower and upper segments correspond respectively to \((c,d)=(-3/2,0)\), \((9,21/2)\), \((9,-21/2)\). The accompanying executable rigorous-interval witness `verify.py` brackets every switching time and establishes, in the order \(J_1,J_2,J_3\), the strict displacement-sign pairs \((+,-)\), \((-,+)\), and \((+,-)\). It uses outward-rounded intervals for the elementary functions, 80 decimal digits of interval precision, and verifies both the crossing-direction signs and the final displacement signs. Therefore at least one periodic solution exists in each interval.

There are two exterior visits along the four-event itineraries. Let \(s(y)\) and \(v(y)\) denote respectively the lower and upper exterior durations. Along each certified transverse itinerary, scalar order and the implicit crossing derivative show that **\(s(y)\) decreases strictly and \(v(y)\) increases strictly as \(y\) increases**. Indeed, increasing \(y\) delays the descending lower crossing but advances the ascending lower crossing, while it advances the ascending upper crossing and delays the descending upper crossing. On the two-event itinerary \(J_3\), the upper duration \(v(y)\) similarly increases.

Rigorous endpoint interval evaluations using the same affine formula certify the following conservative inequalities; all times are expressed in the original forcing-time units:
\[
\begin{aligned}
E(y)&\ge s(-0.569203)+v(-0.569204)>0.8984045&& (y\in J_1),\\
E(y)&\le s(-0.55677)+v(-0.55675)<0.861155&& (y\in J_2),\\
E(y)&=v(y)\ge v(-0.55517)>1.000965&& (y\in J_3).
\end{aligned}
\]
The exact critical time satisfies \(0.8975979<2\pi/7<0.8975980\). It follows that \(0<P'(y)<1\) **throughout** \(J_1\) and \(J_3\), while \(P'(y)>1\) **throughout** \(J_2\). Consequently \(D'(y)\) has a fixed strict sign on each interval; the periodic orbit in each is therefore unique in its corresponding interval and hyperbolic, attracting on \(J_1,J_3\), repelling on \(J_2\).

The original source proves there is one antisymmetric periodic solution \(x_c(t+\pi)=-x_c(t)\) below these intervals, with half-period lower exterior duration \(s_c<\pi/7\). Its derivative is \(P'(y_c)=\exp(3\pi-21s_c)>1\), so it is hyperbolically repelling. Finally the symmetry \(x(t)\mapsto-x(t+\pi)\) gives a different companion to each of the three noncentral periodic solutions and preserves the multiplier. This yields four attracting and three repelling distinct hyperbolic periodic solutions. As each has multiplier distinct from one and all crossings are transverse, standard implicit-function continuation of the return-map fixed-point equation gives local persistence of each under small parameter perturbations.

## Verification
The executable `verify.py` implements the rigorous interval witnesses for all six rational shooting endpoints using `mpmath.iv` outward-rounded elementary functions. It verifies sign changes and transverse crossings, bounds the mixed endpoint residence times, and asserts strict separation from \(2\pi/7\). The certified coarse numerical inequalities stated above leave large margins relative to all enclosure widths. The source's original analytic and rational sign arguments establish validity of the complete switching itineraries throughout the three enclosing intervals and the antisymmetric central orbit. Executing the script should print `CERTIFIED_OK`.

## Relationship to prior work
Hu and Chen, *Seven Limit Cycles in a Periodically Forced Three-Zone Equation*, arXiv:2610.19586v1 (2026-10-14), Theorem 1 and Lemma 1 prove the existence of seven isolated periodic orbits and certify the three broad shooting intervals. Their equation (4) records the general residence-time multiplier identity; the new step is the **strict, interval-wide parameter-specific residence bounds** that force all six noncentral branches to be hyperbolic, identify their stability arrangement, and prove local uniqueness within three explicit rational brackets. Their own central-orbit multiplier bound is cited as prior work. General Floquet and implicit-function theorems are standard tools, not claimed as original.

## Limitations
The theorem establishes at least seven hyperbolic cycles, not that these exhaust all cycles globally; additional periodic orbits outside the selected intervals are not excluded. It concerns a specified rational parameter triple and a sufficiently small unspecified open neighborhood, not the entire positive-parameter family. It relies on the already-published, fully inspected rational itinerary certificates for the three enclosing intervals and the central orbit. Independent auditing has not been performed. Historical priority under other terminology cannot be categorically excluded by literature searches.

## References
- C. Hu and J. Chen, *Seven Limit Cycles in a Periodically Forced Three-Zone Equation*, arXiv:2610.19586v1, posted 14 October 2026. Theorem 1, Lemma 1, equations (3)–(4), Appendix A. https://arxiv.org/pdf/2610.19586
- Standard scalar ODE comparison, smooth dependence on transverse switching events, and implicit-function continuation of hyperbolic periodic solutions are used in their ordinary mathematical forms.
