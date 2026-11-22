# Exact weak-seasonality phase law for bidirectional vector–host transmission

## Finding
For a vector–host disease-free linearization with two separately seasonal transmission directions, the second-order Floquet growth response has an explicit sinusoidal dependence on their relative phase. The maximizing phase is unique modulo a period; it is synchronized exactly when the two removal rates agree. At unequal removal rates a nonzero optimal phase lag exists, and different phase choices can put the *same* marginally critical unforced system on opposite sides of the invasion threshold for every sufficiently small nonzero forcing amplitude.

Put \(s=\sqrt{(d-a)^2/4+bc}\), \(r=(d-a)/(2s)\) and \(D=4s^2+\omega^2\). Define \(\Lambda_0=-(a+d)/2+s\). For every fixed \(\phi\in\mathbb R\), the principal continuous-time Floquet exponent satisfies
\[
\Lambda(\varepsilon,\phi)=\Lambda_0+\varepsilon^2 Q(\phi)+O(\varepsilon^4),\qquad
Q(\phi)=\frac{bc}{2D}\Big[s\big((1+r^2)\cos\phi-(1-r^2)\big)+\omega r\sin\phi\Big].
\]
The remainder is uniform in the relative phase. The unique maximizing phase modulo \(2\pi\) is
\[
\phi_*=\operatorname{atan2}(\omega r,s(1+r^2)),
\]
and the unique minimizing phase is \(\phi_*+\pi\) modulo \(2\pi\). Writing \(H=\sqrt{s^2(1+r^2)^2+\omega^2r^2}\), the exact sign law for the coefficient is
\[
Q(\phi)>0\quad\Longleftrightarrow\quad
\cos(\phi-\phi_*)>\frac{s(1-r^2)}{H}.
\]
For unequal removal rates, this specifies a nonempty open interval of enhancing phases and a nonempty open interval of suppressing phases. For equal removal rates, \(Q(\phi)\le0\), with equality only when \(\phi=0\) modulo \(2\pi\), and in that aligned case \(\Lambda(\varepsilon,0)=\Lambda_0\) exactly at every admissible amplitude.

At the marginal baseline parameters \((a,d,b,c,\omega)=(1,2,1,2,1)\),
\[
\Lambda_0=0,\qquad Q(\phi)=\frac{5\cos\phi+\sin\phi-4}{30}.
\]
In particular, \(Q(0)=1/30>0\), whereas \(Q(\pi)=-3/10<0\). Thus equal-mean, equal-amplitude, equal-frequency transmission histories give positive versus negative disease-free invasion exponents solely by changing the relative phase when sufficiently small nonzero \(\varepsilon\) is used.

## Assumptions and scope
Take any fixed \(a,d,b,c,\omega>0\), \(\phi\in\mathbb R\) and real \(|\varepsilon|<1\). The two infected-compartment vector \(x(t)=(x_H(t),x_V(t))^\top\) follows
\[
\frac{dx}{dt}=\begin{pmatrix}-a&b[1+\varepsilon\cos(\omega t)]\\c[1+\varepsilon\cos(\omega t+\phi)]&-d\end{pmatrix}x.
\]
Removal rates are constant, both transmission directions remain strictly positive, and there is no separate latent class or dynamic susceptible pool. The coefficient matrix has period \(T=2\pi/\omega\). The principal Floquet exponent is \(\Lambda=T^{-1}\log\rho(\Phi(T))\), where \(\Phi(0)=I\) is the fundamental matrix and \(\rho\) denotes spectral radius. The asymptotic statement is for \(\varepsilon\to0\) with all remaining parameters fixed. Invasion/decay conclusions are statements about this *linearized* rare-infection dynamics and not nonlinear endemic equilibria or outbreak probabilities.

## Proof
The strictly positive monodromy has a unique positive Perron eigenvector. Normalize the associated Floquet solution so that the ratio \(y=x_V/x_H\) is positive and periodic. Its Riccati equation is
\[
\dot y=c[1+\varepsilon\cos(\omega t+\phi)]+(a-d)y-b[1+\varepsilon\cos(\omega t)]y^2.
\]
At zero forcing its unique stable positive solution is \(y_0=(s+(a-d)/2)/b=s(1-r)/b\); its scalar linearization has slope \(-2s<0\). The implicit-function theorem for the periodic fixed point therefore gives a real-analytic periodic \(y(t;\varepsilon)\) near zero. Expand \(y=y_0+\varepsilon y_1+\varepsilon^2y_2+\cdots\). The first variational equation is
\[
\dot y_1+2sy_1=\operatorname{Re}(Fe^{i\omega t}),\qquad
F=c e^{i\phi}-by_0^2,
\]
so \(y_1=\operatorname{Re}(Fe^{i\omega t}/(2s+i\omega))\). The second equation is
\[
\dot y_2+2sy_2=-b y_1^2-2by_0y_1\cos(\omega t).
\]
With \(\langle\cdot\rangle\) denoting a period average, the first component gives the exact identity \(\Lambda=-a+b\langle(1+\varepsilon\cos\omega t)y\rangle\). Hence
\[
Q=b\langle y_2+\cos(\omega t)y_1\rangle
=-\frac{b^2|F|^2}{4sD}+\frac{br}{2}\operatorname{Re}\frac{F}{2s+i\omega}.
\]
Use \(bc=s^2(1-r^2)\) and \(by_0^2=c(1-r)/(1+r)\), expand real and imaginary components of \(F\), and collect terms. This yields precisely the displayed \(Q(\phi)\), with independent verification of the algebra in the standalone checker.

The constant term in the bracket equals \(-s(1-r^2)\); the phase-dependent part is \(s(1+r^2)\cos\phi+\omega r\sin\phi=H\cos(\phi-\phi_*)\). Since \(s>0\), its maximizing and minimizing phases are unique modulo \(2\pi\). Moreover, \(H^2-s^2(1-r^2)^2=r^2(4s^2+\omega^2)\), which is strictly positive exactly when \(a\ne d\). This proves the strict positive/negative phase intervals when removal rates differ, and the equal-rate boundary otherwise. Since the coefficient has a fixed strict sign at any chosen interior phase, the corresponding Floquet exponent difference has that sign for sufficiently small nonzero \(\varepsilon\) if \(\Lambda_0=0\).

Finally, shifting time by half a period changes \(\varepsilon\) to \(-\varepsilon\) in *both* seasonal terms without changing the Floquet exponent. Its analytic expansion is therefore even, which improves the remainder from \(O(\varepsilon^3)\) to \(O(\varepsilon^4)\). If \(a=d\) and \(\phi=0\), every time-dependent coefficient matrix equals \(-aI+[1+\varepsilon\cos(\omega t)]J\) for one constant matrix \(J\). All commute, and integrating over a period gives \(\Phi(T)=\exp(T[-aI+J])\). Thus \(\Lambda=\Lambda_0\) exactly for every \(|\varepsilon|<1\).

## Verification
The accompanying `verify_phase.py` independently computes the quadratic coefficient from a Riccati Fourier response and from a directly integrated fundamental matrix using fourth-order Runge–Kutta integration. It checks five parameter configurations, eleven phases per configuration, maximizing-phase inequalities, the exact threshold witness, and aligned equal-rate invariance: 202 assertions passed. These finite computations corroborate but do not replace the analytic all-parameter argument above. Reproduce by running `python verify_phase.py` with Python 3 (standard library only).

## Relationship to prior work
Khong, Carmona and Gandon (2023) developed a second-order seasonal perturbation framework for vector-borne infection and distinguished vector-density from common-biting-rate forcing. Their examined forcing is driven by a shared seasonal function and does not supply the independently phased directional-transmission optimizer displayed here. Nipa and Allen (2021) explicitly used two separately periodic transmission directions, including synchronized and quarter-period-shifted examples, but treated these with numerical reproduction-number and stochastic-outbreak calculations, without the all-phase analytic optimum and sharp sign boundary stated here. Wang and Zhao (2008) supplied the general periodic-compartmental invasion-threshold framework; their general theorem does not state this explicit small-forcing phase classification. Generic Floquet and Riccati perturbation methods are pre-existing tools, not asserted as novel.

## Limitations
This is a perturbative small-amplitude result. At a phase where \(Q=0\), fourth-order terms may govern the actual sign, except for the exact equal-removal aligned case. Phase optimality concerns the leading nonzero perturbation coefficient, not a theorem of global optimality at every finite amplitude. No measured epidemiological rates, human outcomes, nonlinear epidemic persistence, control effectiveness or field calibration are claimed. The checked sources leave residual historical-priority uncertainty; the comparison is not a proof of novelty across all literature.

## References
1. V. H. Khong, P. Carmona, S. Gandon, “Seasonality and the persistence of vector-borne pathogens,” *Journal of the Royal Society Interface* 20 (2023), article 20230470, first public online 2023-12-13. https://doi.org/10.1098/rsif.2023.0470 ; full-text https://pmc.ncbi.nlm.nih.gov/articles/PMC10715918/
2. K. F. Nipa, L. J. S. Allen, “The Effect of Demographic Variability and Periodic Fluctuations on Disease Outbreaks in a Vector–Host Epidemic Model,” in *Infectious Diseases and Our Planet* (2021), pp. 15–39. https://doi.org/10.1007/978-3-030-50826-5_2
3. W. Wang, X.-Q. Zhao, “Threshold Dynamics for Compartmental Epidemic Models in Periodic Environments,” *Journal of Dynamics and Differential Equations* 20 (2008), 699–717. https://doi.org/10.1007/s10884-008-9111-8
