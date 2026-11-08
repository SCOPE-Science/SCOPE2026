# Exact fractional-broadening threshold for two equal Cole–Cole loss peaks

## Finding

For two equal-strength Cole–Cole dielectric relaxation processes with a common exponent \(0<\alpha\leq1\) and positive relaxation-time ratio \(r>1\), there is a unique, explicit threshold separating a single strict dielectric-loss peak from two strict peaks. Define
\[
 c=\cos\!\left(\frac{\pi\alpha}{2}\right),\qquad
 D=\frac{c+\sqrt{c^2+8}}{2},\qquad
 r_*(\alpha)=\exp\!\left(\frac{2\operatorname{arcosh}D}{\alpha}\right).
\]
For \(1<r\leq r_*(\alpha)\) the total positive-frequency loss has exactly one strict local (and global) maximum, at \(\omega\tau_0=1\). At equality this maximum is quartically flat, rather than splitting into three stationary extrema. For \(r>r_*(\alpha)\) the central point is a strict minimum and there are exactly two nondegenerate maxima, located explicitly as below. No other critical points occur at positive frequency.

The threshold decreases strictly as \(\alpha\) increases, from an exponentially large limit at small \(\alpha\) to the Debye endpoint
\[
 r_*(1)=3+2\sqrt2,\qquad
 \lim_{\alpha\downarrow0}\alpha\log r_*(\alpha)=2\operatorname{arcosh}2.
\]
Thus a two-process response that has two resolved loss maxima for a narrow Debye profile can have just one maximum when each process is fractionally broadened. This criterion concerns the number of exact mathematical peaks, not two-process identifiability from complete complex data or resolution under measurement noise.

## Assumptions and scope

Let \(\Delta\varepsilon>0\), \(\tau_0>0\), \(r>1\), and \(0<\alpha\leq1\). Use the principal complex power and the sign convention
\[
 \chi^*(\omega)=\Delta\varepsilon\sum_{\sigma\in\{-1,1\}}
 \frac{1}{1+(i\omega\tau_0r^{\sigma/2})^\alpha},\qquad
 L(\omega)=-\operatorname{Im}\chi^*(\omega),\qquad\omega>0.
\]
The two components have exactly the same positive strength and exponent and have relaxation times \(\tau_0/\sqrt r\) and \(\tau_0\sqrt r\). The exponent \(\alpha\) here is the exponent of the complex power; another common notation for Cole–Cole broadening is \(1-\alpha\). No conductivity background, instrumental convolution, or other relaxation process is included.

Write
\[
 \theta=\frac{\pi\alpha}{2},\quad c=\cos\theta,\quad
 s=\alpha\log(\omega\tau_0),\quad a=\frac{\alpha\log r}{2},\quad
 d=\cosh a,\quad y=\cosh s\geq1.
\]
For \(r>r_*(\alpha)\), put
\[
 y_*=\frac{\sqrt{(d^2-1)(d^2-c^2)}-c}{d}>1,\qquad
 \omega_{\pm}=\tau_0^{-1}\exp\!\left(\pm\frac{\operatorname{arcosh}(y_*)}{\alpha}\right).
\]
Then \(\omega_-\) and \(\omega_+\) are exactly the two maxima, and \(\tau_0^{-1}\) is the intervening strict minimum. The minimum is exactly
\[
 L(\tau_0^{-1})=\frac{\Delta\varepsilon\sin\theta}{d+c},
 \qquad L(\tau_0^{-1})\sim2\Delta\varepsilon\sin\theta\,r^{-\alpha/2}
 \quad(r\to\infty;\ \alpha\text{ fixed}).
\]

## Proof

**Reduction to one real variable.** For any \(z>0\), direct rationalization of \((1+(iz)^\alpha)^{-1}\) gives
\[
 -\operatorname{Im}\frac{1}{1+(iz)^\alpha}
 =\frac{\sin\theta}{2\{\cosh(\alpha\log z)+c\}}.
\]
Consequently
\[
 L(s)=\frac{\Delta\varepsilon\sin\theta}{2}
 \left(\frac{1}{\cosh(s-a)+c}+\frac{1}{\cosh(s+a)+c}\right).
\]
Using \(\cosh(s\pm a)=dy\pm\sinh s\sinh a\), and \(\cosh^2s-\sinh^2s=1\), obtain
\[
 L(s)=\Delta\varepsilon\sin\theta\,
 \frac{dy+c}{Q(y)},\quad
 Q(y)=y^2+2cdy+c^2+d^2-1.
\]
The original denominators are strictly positive, so \(Q(y)>0\) for \(y\geq1\). The variable \(y=\cosh s\) is strictly increasing for \(s>0\) and is even in \(s\).

**Exact critical-point count.** Differentiating with respect to \(y\) yields
\[
 \frac{dL}{dy}=\Delta\varepsilon\sin\theta\,
 \frac{P(y)}{Q(y)^2},\qquad
 P(y)=d(d^2-1-c^2)-2cy-dy^2.
\]
For all \(y\geq1\), \(P'(y)=-2c-2dy<0\), and \(P(y)\to-\infty\) as \(y\to\infty\). At the endpoint,
\[
 P(1)=(d+c)(d^2-cd-2).
\]
Since \(d>1\) and \(0\leq c<1\), the sign of \(P(1)\) is the sign of \(d-D\), where \(D\) is the unique positive root of \(d^2-cd-2=0\). If \(d<D\), \(dL/dy<0\) on \(y\geq1\), hence \(s=0\) is the unique strict maximum. If \(d=D\), the derivative vanishes only at \(y=1\), is negative for \(y>1\), and \(s=0\) remains the sole strict maximum. The expansion \(y-1=s^2/2+O(s^4)\) together with \(P'(1)<0\) gives the exact local form at the threshold,
\[
 L(s)=\frac{\Delta\varepsilon\sin\theta}{D+c}-\frac{\Delta\varepsilon\sin\theta}{4(D+c)^3}s^4+O(s^6).
\]
Thus the threshold point is quartically flat.

If \(d>D\), strict monotonicity of \(P\) gives one and only one zero \(y_*>1\). Solving \(P(y_*)=0\), and factoring its quadratic discriminant as \((d^2-1)(d^2-c^2)\), gives exactly the expression above. The sign of \(dL/dy\) is positive for \(1\leq y<y_*\) and negative for \(y>y_*\). The even \(s\)-dependence then gives a central strict minimum and precisely two nondegenerate strict maxima. Since \(L(\omega)\to0\) at both frequency endpoints, the maxima are global. The equivalence \(d>D\iff r>r_*(\alpha)\) finishes the mode classification.

**Dependence on broadening.** The map \(c\mapsto D(c)\) is strictly increasing, whereas \(c(\alpha)=\cos(\pi\alpha/2)\) strictly decreases. Hence \(A(\alpha)=\operatorname{arcosh}D(c(\alpha))\) is positive and strictly decreasing. Therefore \(2A(\alpha)/\alpha=\log r_*(\alpha)\) strictly decreases. At \(\alpha=1\), \(c=0\) and \(D=\sqrt2\), yielding \(r_*(1)=(\sqrt2+1)^2\). As \(\alpha\downarrow0\), \(c\to1\) and \(D\to2\), yielding the asserted limit.

**Critical and large-separation laws.** Let \(a_*=\operatorname{arcosh}D\) for fixed \(\alpha\), and let \(d\downarrow D\) from above. Implicit differentiation of \(P(y_*,d)=0\) at \((y_*,d)=(1,D)\) gives
\[
 y_*-1=\frac{2D-c}{2}(d-D)+O((d-D)^2),\quad
 \operatorname{arcosh}(y_*)\sim\sqrt{(2D-c)(d-D)}.
\]
In particular the outer peak displacement in logarithmic frequency grows with a positive square-root exponent at onset. Finally, \(L(0)=\Delta\varepsilon\sin\theta/(d+c)\), and \(d=\cosh(\alpha\log r/2)\sim r^{\alpha/2}/2\), proving the stated trough-height asymptotic.

## Verification

The standalone file `verify.py` evaluates the original unsimplified two-component fractional loss, differentiates those components independently, and compares them to the closed rational reduction, critical roots, peak-count sign changes, center values, Debye endpoint, broadening monotonicity, onset square-root scaling, and large-separation trough law. It uses only the Python standard library and reports `VERIFY_OK checks=1004`. The infinite-parameter theorem is proved by the algebra and monotonicity above; the finite numerical tests are supplementary checks, not an exhaustive or independent mathematical certification.

Reproduce with `python3 verify.py` in the extracted package directory. No external datasets are required.

## Relationship to prior work

Cole and Cole (1941) introduce the fractional dielectric susceptibility and its single-component loss broadening. Hilfer (2002) presents full analytical frequency-domain susceptibility formulas and width comparisons for individual Cole–Cole, Cole–Davidson and Havriliak–Negami forms. Chassagne et al. (2016) study overlapping dielectric relaxations and fitting sums of two Havriliak–Negami terms. Those models and general fitting methods do not themselves state the present necessary-and-sufficient two-equal-component modality boundary or the exact peak positions. Previous results on three and four equal Debye components involve different component counts and fix \(\alpha=1\); neither entails this two-component fractional-exponent phase diagram without a separate calculation.

No global priority claim is made beyond the specifically examined material. A potentially relevant older statistical treatment of equally shifted generalized hyperbolic-secant mixtures, possibly under a different parametrization, remains a residual historical-priority risk.

## Limitations

The criterion uses ideal, noise-free, exact loss-profile extrema. Equal component strengths and equal fractional exponents are essential hypotheses; unequal strengths or distinct exponents need not share the same threshold. A single observed peak does not mean only one physical relaxation is present. No experimental detection limit, parameter-estimation error, finite frequency window, or electrical-conduction loss is modeled. The singular limit \(\alpha\downarrow0\) is not included in the theorem, although the threshold asymptotic is given.

## References

- K. S. Cole and R. H. Cole, *Dispersion and Absorption in Dielectrics I. Alternating Current Characteristics*, Journal of Chemical Physics 9 (1941), 341–351. https://doi.org/10.1063/1.1750906 . The original source is dated April 1941.
- R. Hilfer, *H-function representations for stretched exponential relaxation and non-Debye susceptibilities in glassy systems*, Physical Review E 65 (2002), 061510, published 2002-06-28. https://doi.org/10.1103/PhysRevE.65.061510 . Author-hosted full text: https://www2.icp.uni-stuttgart.de/~hilfer/publikationen/html/PRE-2002-65-061510/PRE-2002-65-061510.Sx1.html .
- C. Chassagne, E. Dubois, M. L. Jiménez, J. P. M. van der Ploeg and J. van Turnhout, *Compensating for Electrode Polarization in Dielectric Spectroscopy Studies of Colloidal Suspensions: Theoretical Assessment of Existing Methods*, Frontiers in Chemistry 4 (2016), 30, published 2016-07-19. https://doi.org/10.3389/fchem.2016.00030 .
