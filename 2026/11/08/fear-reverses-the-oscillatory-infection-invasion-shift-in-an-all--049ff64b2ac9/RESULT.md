# Fear reverses the oscillatory infection-invasion shift in an Allee predator–prey model

## Finding
In the no-delay fear–Allee eco-epidemic model of Al Amri, Khan and Greenhalgh [1], the sign of the difference between infection-invasion exponents on a nearby ecological cycle and at the corresponding disease-free coexistence equilibrium can be reversed by changing *only the habituation floor* of the fear response, with all other parameters fixed. More precisely, the small-cycle predator-mean displacement has an exact signed leading coefficient. For the two positive rational fear floors below the coefficients have opposite signs:

\[
\begin{aligned}
\alpha&=\frac{26}{3125},\quad\theta=\frac15,\\
C\!\left(\frac{92}{225}\right)&=-\frac{72008352}{212226125}<0,\\
C\!\left(\frac1{100}\right)&=\frac{1645176}{6555125}>0.
\end{aligned}
\]

Thus sufficiently small disease-free oscillations can make invasion *easier* than the equilibrium-based prediction at the first fear floor, but *harder* at the second. This is an invasion statement for a rare infection, not a theorem asserting existence of endemic attractors.

## Assumptions and scope
Consider the nondimensional, no-delay model with susceptible prey \(x\), infected prey \(y\), and predators \(z\):

\[
\begin{aligned}
\dot x&=x(1-x-y)(x-\theta)f(z)-\frac{xy}{1+y}-xz,\\
\dot y&=y\left(\frac{x}{1+y}-\frac32z-\mu\right),\\
\dot z&=z\left(x+\frac65y-d\right),\\
f(z)&=\eta+\frac{\alpha(1-\eta)}{\alpha+z}.
\end{aligned}
\]

Here \(0<\theta<1\), \(0<\eta<1\), \(\alpha>0\), \(\mu>0\), and \(d>0\). This is exactly the parameter specialization \(a=b=\beta=c=\delta=1\), \(p=6/5\), \(g=3/2\), \(m=d\) in equation (2.2) of [1], with \(p>b\), \(p<g\), and \(b\le a\). The disease-free plane \(y=0\) is invariant, and its planar flow is

\[
\dot x=x\bigl(H(x)f(z)-z\bigr),\quad\dot z=z(x-d),
\qquad H(x)=(1-x)(x-\theta).
\]

Put \(d_0=(1+\theta)/2\), \(h=(1-\theta)^2/4\). There is a unique \(z_0>0\) satisfying \(z_0=h f(z_0)\). Define \(f_0=f(z_0)\), \(K=1-h f'(z_0)>0\), and

\[
C=\frac{2d_0}{K}\left(\frac{h f''(z_0)z_0}{2d_0K}-f_0\right).
\]

For sufficiently small \(\varepsilon=d_0-d>0\), write \(z_*(d)>0\) for the unique solution of \(z_*=H(d)f(z_*)\), \(\Gamma_\varepsilon\) for the locally attracting small ecological cycle, and \(\overline{\cdot}\) for its physical-time average over one period.

## Proof
**1. Existence and criticality of the ecological cycle.** The coexistence equilibrium is \((d,z_*(d))\), which exists uniquely for \(\theta<d<1\), since \(H(d)f(z)-z\) decreases strictly from positive to negative. Its Jacobian trace is \(dH'(d)f(z_*(d))\), and determinant is \(dz_*(d)[1-H(d)f'(z_*(d))]>0\). Therefore the trace crosses zero transversely at \(d=d_0\). Write

\[
\omega=\sqrt{d_0Kz_0},\qquad M=\sqrt{\frac{z_0}{d_0K}},
\qquad X=x-d_0,\quad Y=\frac{z-z_0}{M}.
\]

The transformed linear field is \(\dot X=-\omega Y\), \(\dot Y=\omega X\). At this point its nonlinear partial derivatives required for the planar first Lyapunov formula are

\[
\begin{gathered}
F_{XX}=-2d_0f_0,\quad F_{XY}=-\omega/d_0,\quad
F_{YY}=d_0h f''(z_0)M^2,\\
F_{XXX}=-6f_0,\quad F_{XYY}=h f''(z_0)M^2,\quad G_{XY}=1,\\
G_{XX}=G_{YY}=G_{XXY}=G_{YYY}=0.
\end{gathered}
\]

The standard planar Hopf cubic coefficient in these normalized coordinates is

\[
\ell_1=\frac{F_{XXX}+F_{XYY}}{16}
+\frac{F_{XY}(F_{XX}+F_{YY})}{16\omega}
=-\frac{f_0}{4}<0.
\]

The real part of the eigenvalues near \(d=d_0-\varepsilon\) is \(d_0f_0\varepsilon+O(\varepsilon^2)\). The nondegenerate supercritical Hopf theorem gives a unique nearby locally orbitally attracting positive cycle for all sufficiently small \(\varepsilon>0\), with squared leading \(x\)-amplitude \(4d_0\varepsilon+o(\varepsilon)\). Hence

\[
\operatorname{Var}_{\Gamma_\varepsilon}(x)=2d_0\varepsilon+o(\varepsilon),\qquad
\operatorname{Var}_{\Gamma_\varepsilon}(z)=\frac{z_0}{d_0K}\,2d_0\varepsilon+o(\varepsilon).
\]

**2. Exact prey mean and signed predator shift.** Integrating \(\dot z/z=x-d\) around the positive periodic orbit yields \(\bar x=d\) *exactly*. For \(\xi=x-d\), \(\zeta=z-z_*(d)\), integration of \(\dot x/x=H(x)f(z)-z\) and Taylor expansion at the equilibrium, using \(H'(d)=2\varepsilon\), gives

\[
0=-K\bar\zeta-f_0\overline{\xi^2}
+\frac{h f''(z_0)}{2}\overline{\zeta^2}+o(\varepsilon).
\]

As \(\bar\zeta=O(\varepsilon)\) and the variances are as above, substitution yields

\[
\boxed{\bar z-z_*(d)=C\varepsilon+o(\varepsilon).}
\]

This expansion is justified by the smooth local Hopf family, with all variables uniformly of order \(\sqrt\varepsilon\) about equilibrium. In particular, no finite numerical experiment is used to establish the asymptotic law.

**3. Exact rational sign reversal at fixed \(\alpha\).** Choose \(\theta=1/5\), \(\alpha=26/3125\). At \(\eta=92/225\), direct substitution yields

\[
z_0=\frac{234}{3125},\quad f_0=\frac{117}{250},\quad
K=\frac{1303}{1170},\quad C=-\frac{72008352}{212226125}.
\]

At \(\eta=1/100\), the corresponding exact values are

\[
z_0=\frac{104}{3125},\quad f_0=\frac{26}{125},\quad
K=\frac{229}{130},\quad C=\frac{1645176}{6555125}.
\]

All ecological parameters except \(\eta\) are identical. Both examples meet the positive-domain hypotheses and have a supercritical ecological cycle when \(\varepsilon>0\) is sufficiently small.

**4. Infection invasion.** Linearizing the infected-prey equation transverse to a disease-free state gives the scalar equation \(\dot y=[x(t)-(3/2)z(t)-\mu]y\). Thus its exact Floquet exponent on the cycle, compared with the exponent evaluated at the coexistence equilibrium, is

\[
\begin{aligned}
\lambda_{\rm cyc}&=d-\frac32\bar z-\mu,\\
\lambda_{\rm eq}&=d-\frac32 z_*(d)-\mu,\\
\boxed{\lambda_{\rm cyc}-\lambda_{\rm eq}&=-\frac32 C\varepsilon+o(\varepsilon).}
\end{aligned}
\]

For each rational fear-floor example and every sufficiently small positive \(\varepsilon\), there is a nonempty interval of *positive* \(\mu\) between the two critical values \(d-(3/2)\bar z\) and \(d-(3/2)z_*(d)\). Choosing \(\mu\) in this interval gives opposite signs for the cycle-based and equilibrium-based rare-infection exponents. Their order reverses between the two fear floors. The positive-\(\mu\) condition follows since \(d_0-(3/2)z_0>0\) for both explicit examples.

## Verification
The accompanying \(\texttt{verify.py}\) checks the canonical Hopf coefficient symbolically, evaluates both rational coefficient identities exactly, and integrates the ecological cycle numerically at \(\varepsilon=0.004\). Its final output is \(\texttt{VERIFY\_OK}\). The numerical one-period estimates of \((\bar z-z_*)/\varepsilon\) are approximately \(-0.331819378\) and \(0.243468503\), converging toward the proven coefficients \(-0.339300131\) and \(0.250975534\). Numerical validation illustrates the asymptotic signs but cannot establish the theorem for all sufficiently small \(\varepsilon\).

## Relationship to prior work
Al Amri, Khan and Greenhalgh [1] formulate the exact three-population fear–Allee model and prove an ecological Hopf crossing; their discussion does not supply the present exact negative cubic Hopf coefficient, signed small-cycle predator mean shift, or fixed-parameter infection-invasion reversal. Bate and Hilker [2] already establish the *general principle* that invasion thresholds on ecological oscillations depend on time averages, and show a prey-infection increase in a different Rosenzweig–MacArthur ecological model. This principle is not new. The distinctive result here is that in [1]'s model the prey mean equals the equilibrium value exactly, while fear curvature alone reverses the predator-mean displacement and hence the rare-infection shift, even when only one fear parameter changes. Related fear-driven eco-epidemic models such as [3] incorporate direct fear-dependent suppression of transmission; that different mechanism does not imply the present theorem.

## Limitations
The finding is confined to the specified no-delay, parameter-restricted model, locally near a nondegenerate ecological Hopf bifurcation. It proves local orbital attraction within the disease-free plane, not global ecological attraction, endemic equilibria, invasion persistence, effects of finite infected population, or a universal monotonic dependence on \(\eta\). The comparison equilibrium is ecologically unstable on the small-cycle side. An independent audit has not been carried out; equivalent unindexed model-specific results remain a literature-priority risk.

## References
1. K. Al Amri, Q. J. A. Khan, D. Greenhalgh, *Combined impact of fear and Allee effect in predator-prey interaction models on their growth*, Mathematical Biosciences and Engineering **21** (2024), 7211–7252, https://doi.org/10.3934/mbe.2024319. First publicly published 2024-10-08. Open full text: https://strathprints.strath.ac.uk/90792/7/Al-Amri-etal-MBE-Combined-impact-of-fear-and-Allee-effect-in-predator-prey-interaction-models-on-their-growth.pdf.
2. A. M. Bate, F. M. Hilker, *Predator–prey oscillations can shift when diseases become endemic*, Journal of Theoretical Biology **316** (2013), 1–8, https://doi.org/10.1016/j.jtbi.2012.09.013. Open full text: https://www.usf.uni-osnabrueck.de/fileadmin/DE/Institut/Mitarbeiter/Hilker/papers/BateHilker-JTheorBiol-2013.pdf.
3. *Backward bifurcation, oscillations and chaos in an eco-epidemiological model with fear effect*, Journal of Biological Dynamics (2019), https://doi.org/10.1080/17513758.2019.1593525.
