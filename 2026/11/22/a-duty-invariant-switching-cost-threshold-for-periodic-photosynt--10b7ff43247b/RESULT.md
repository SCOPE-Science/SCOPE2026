# A duty-invariant switching-cost threshold for periodic photosynthetic repair

## Finding
Consider an idealized active photosynthetic-unit fraction \(x(t)\) driven by repeated light/dark periods. For each period \(T>0\), with fixed illuminated fraction \(0<f<1\), the system follows
\[
\dot x=u-(u+d)x\quad(0\le t<fT),\qquad
\dot x=v(1-x)\quad(fT\le t<T),
\]
where \(u,v,d>0\). The light-phase output is the integral of \(x(t)\); the dark-phase output is zero. At the unique attracting periodic state, subtract a dimensionally consistent positive cost \(c/T\) per unit time for one light/dark switching cycle, where \(c\ge0\) is the fixed cost per period expressed in output-time units.

Put \(k=u+d\), \(p=kf\), \(q=v(1-f)\), \(K=d/k^2\), and
\[
\Phi(T)=\frac{(1-e^{-pT})(1-e^{-qT})}{1-e^{-(p+q)T}}.
\]
The exact net productivity is
\[
J_c(T)=\frac{fu}{k}+\frac{K\Phi(T)-c}{T}.
\]
Its global optimization over \(T>0\) has precisely three regimes:

1. If \(c=0\), \(J_0\) is strictly decreasing. Its supremum \(f[fu+(1-f)v]/[kf+(1-f)v]\) is attained only as \(T\downarrow0\).
2. If \(0<c<K\), a unique finite global maximizer \(T_c>0\) exists and solves
\[
\Phi(T_c)-T_c\Phi'(T_c)=c/K.
\]
The optimum strictly improves on the long-cycle benchmark \(fu/k\), since \(J_c(T_c)-fu/k=K\Phi'(T_c)>0\). Also, \(T_c\) increases strictly with \(c\).
3. If \(c\ge K\), \(J_c\) is strictly increasing. Its supremum \(fu/k\) is reached only as \(T\to\infty\); no finite period maximizes net productivity.

Thus the sharp existence threshold \(c_*=d/(u+d)^2\) is independent of both the illumination duty fraction \(f\) and the dark-phase repair rate \(v\), as long as both phases have positive duration and \(v>0\). Near zero cost,
\[
T_c\sim\left(\frac{6(p+q)c}{Kp^2q^2}\right)^{1/3}\quad(c\downarrow0).
\]

## Assumptions and scope
The result concerns an exactly periodic scalar linear switching model with positive constant rates \(u\) (repair under light), \(v\) (repair in darkness), and \(d\) (light-induced deactivation), and fixed \(f\in(0,1)\). Production during illumination is proportional to the currently active fraction, with the proportionality normalized to one. The cost \(c\) is assessed once per complete light/dark cycle, including both switching events; its total effect per unit time is \(c/T\). The initial transient is discarded and the unique periodic attractor is evaluated. Arbitrary, unobserved biological acclimation, activation lags, photon saturation, electric lighting energy, constraints on admissible periods, and feedback control are not modeled. No claim is made for \(f=0\), \(f=1\), or \(v=0\).

## Proof
Set \(k=u+d\), \(a=u/k\), \(E=e^{-kfT}\), \(F=e^{-v(1-f)T}\). The illuminated flow sends any starting fraction \(x_0\) to \(x_1=a+(x_0-a)E\), and the subsequent dark flow sends \(x_1\) to \(1+(x_1-1)F\). This period map has derivative \(EF\in(0,1)\) and hence one globally attracting fixed point. Solving the fixed-point equation yields
\[
x_0-a=(1-a)\frac{1-F}{1-EF}.
\]
Integration through the illuminated phase gives the gross average output
\[
\frac1T\int_0^{fT}x(t)\,dt=fa+\frac{(1-a)(1-E)(1-F)}{kT(1-EF)}
=\frac{fu}{k}+\frac{d}{k^2T}\Phi(T).
\]
Subtracting the cycle cost proves the displayed formula for \(J_c\).

For all positive \(p,q,T\), set \(U(T)=\tanh(pT/2)\) and \(V(T)=\tanh(qT/2)\). Elementary hyperbolic identities give
\[
\Phi(T)=\frac{2U(T)V(T)}{U(T)+V(T)}.
\]
The harmonic-mean function \(h(x,y)=2xy/(x+y)\) for \(x,y>0\) has strictly positive first partial derivatives and negative-semidefinite Hessian
\[
D^2h(x,y)=-\frac4{(x+y)^3}
\begin{pmatrix}y^2&-xy\\-xy&x^2\end{pmatrix}.
\]
Both \(U\) and \(V\) are strictly increasing and strictly concave on \((0,\infty)\), so the chain rule implies \(\Phi'(T)>0\) and \(\Phi''(T)<0\) for every \(T>0\).

Define \(H(T)=\Phi(T)-T\Phi'(T)\). Then \(H'(T)=-T\Phi''(T)>0\). The expansions at zero and the exponential limits at infinity give
\[
\lim_{T\downarrow0}H(T)=0,\qquad \lim_{T\to\infty}H(T)=1,
\]
and hence \(H\) maps \((0,\infty)\) bijectively onto \((0,1)\). Differentiating the net productivity gives
\[
J_c'(T)=\frac{c-KH(T)}{T^2}.
\]
For \(c=0\), this is strictly negative; for \(c\ge K\), it is strictly positive at every finite period; and for \(0<c<K\), it changes sign exactly once, positive to negative, at the unique \(T_c\) with \(H(T_c)=c/K\). This establishes the complete global classification without relying on a finite search. Using \(c=K(\Phi(T_c)-T_c\Phi'(T_c))\) proves \(J_c(T_c)=fu/k+K\Phi'(T_c)\). Monotonicity of \(T_c\) follows by inverting the strictly increasing function \(H\).

Finally, the Taylor expansion
\[
\Phi(T)=\frac{pq}{p+q}T-\frac{p^2q^2}{12(p+q)}T^3+O(T^5)
\]
implies \(H(T)=p^2q^2T^3/[6(p+q)]+O(T^5)\), yielding the small-cost cubic-root law.

## Verification
The included standard-library file `checker.py` deterministically tests the stationary-orbit identity, the equivalent hyperbolic formula, the two productivity limits, the three cost regimes, the stationary maximum identity, and the small-cost asymptotic with independent light and dark repair rates. It completed 12,112 diagnostic assertions. The preceding proof covers all positive real parameters; the finite tests are regression checks only.

## Relationship to prior work
Sforza et al. (2012) experimentally studied the effects of pulsed-light frequencies and photoinhibition in algae; their qualitative response and frequency comparisons motivate separating biological cycling from switching costs, but they do not provide the stated exact price threshold for this scalar model. Grognard, Akhmetzhanov and Bernard (2012) optimized photobioreactor dilution under imposed day/night light using a biomass/light-attenuation model and different controls, not the choice of period with a fixed switching charge. Papadakis, Kotzabasis and Lika (2012) proposed a substantially richer photoinactivation-and-repair model; its accessible abstract does not settle this exact period-cost comparison, but full-text priority remains a limitation. Earlier frequency-dependent photosynthesis literature establishes parts of the broad biological motivation and does not, merely by describing frequency enhancement, imply the present algebraic three-regime classification.

## Limitations
The cost is stipulated per completed illumination cycle and may not equal actual mixing or actuator energy costs. The model omits nonlinear photochemistry, downstream carbon fixation, light intensity variation, start-up or hysteresis, ecological heterogeneity and finite planning horizons. The result is an exact theorem for a deliberately simplified kinetic model, not a universal law of algal growth or an experimentally calibrated operating rule. Bibliographic completeness and priority, particularly relative to full text unavailable for Papadakis et al. (2012), require further independent investigation.

## References
- Papadakis, I. A., Kotzabasis, K., and Lika, K. (2012), *Modeling the dynamic modulation of light energy in photosynthetic algae*, Journal of Theoretical Biology 300, 254–264, doi:10.1016/j.jtbi.2012.01.040 (available abstract, first electronic article date 2012-02-04).
- Grognard, F., Akhmetzhanov, A. R., and Bernard, O. (2012), *Periodic optimal control for biomass productivity maximization in a photobioreactor using natural light*, arXiv:1204.2906, first public preprint 2012-04-13.
- Sforza, E., Simionato, D., Giacometti, G. M., Bertucco, A., and Morosinotto, T. (2012), *Adjusted Light and Dark Cycles Can Optimize Photosynthetic Efficiency in Algae Growing in Photobioreactors*, PLOS ONE 7(6), e38975, doi:10.1371/journal.pone.0038975, published 2012-06-20.
- Vejrazka, C. (2012), *Microalgal photosynthesis under flashing light*, Wageningen University thesis, doi:10.18174/221726 (repository summary consulted; thesis complete text not inspected).
