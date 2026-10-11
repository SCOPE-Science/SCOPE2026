# Exact common-delay stability threshold for the delayed Beverton–Holt coexistence equilibrium

## Finding
For the interior equilibrium \(E^*\) of the delayed Beverton–Holt competition model studied by Huang, Long, and Shan, assume that \(E^*\) is hyperbolically stable when \(\tau_1=\tau_2=0\), and then set the two delays equal: \(\tau_1=\tau_2=\tau\ge0\). Write
\[
P=p_2+p_3>0,\qquad Q=q_4>0,\qquad \Delta=P^2-4Q,
\]
using the coefficients of the paper's characteristic equation. Then the stability boundary has a closed form:
\[
\tau_c=
\begin{cases}
\dfrac{\pi}{P+\sqrt{\Delta}},&\Delta\ge0,\\[6pt]
\dfrac{1}{\sqrt Q}\arcsin\!\left(\dfrac{P}{2\sqrt Q}\right),&\Delta<0.
\end{cases}
\]
The equilibrium is locally asymptotically stable exactly for \(0\le\tau<\tau_c\), nonhyperbolic at \(\tau=\tau_c\), and unstable for every \(\tau>\tau_c\). When \(\Delta\ne0\), the first imaginary pair is simple and crosses from left to right.

## Assumptions and scope
The model is system (6) of Huang, Long, and Shan. At an interior equilibrium \(E^*=(x_1^*,x_2^*)\), the paper reduces the characteristic equation to
\[
\lambda^2+p_2\lambda e^{-\lambda\tau_1}+p_3\lambda e^{-\lambda\tau_2}+q_4e^{-\lambda(\tau_1+\tau_2)}=0.
\]
For a common delay \(\tau_1=\tau_2=\tau\), define \(P=p_2+p_3\) and \(Q=q_4\). The hypothesis that the equilibrium is hyperbolically stable at zero delay implies \(P>0\) and \(Q>0\). No assumption is made about nonlinear Hopf coefficients or global attractivity.

## Proof
With equal delays, the characteristic equation is
\[
\chi(\lambda,\tau)=\lambda^2+P\lambda e^{-\lambda\tau}+Qe^{-2\lambda\tau}=0.
\]
Multiplying by \(e^{2\lambda\tau}\) gives
\[
(\lambda e^{\lambda\tau})^2+P(\lambda e^{\lambda\tau})+Q=0.
\]
Let
\[
z_\pm=\frac{-P\pm\sqrt{P^2-4Q}}{2}.
\]
Thus \(\chi(\lambda,\tau)=0\) if and only if \(\lambda e^{\lambda\tau}=z_+\) or \(\lambda e^{\lambda\tau}=z_-\). Equivalently, for \(\tau>0\),
\[
\lambda=\frac{1}{\tau}W_k(\tau z_\pm),\qquad k\in\mathbb Z.
\]
Because \(P,Q>0\), both quadratic roots have negative real part. For sufficiently small positive \(\tau\), the principal Lambert branches converge to \(z_\pm\), while every nonprincipal branch has real part tending to \(-\infty\); therefore all characteristic roots start in the open left half-plane.

A change of stability can occur only at an imaginary root. For one scalar factor, put \(\lambda=i\omega\), \(\omega>0\). Then
\[
i\omega e^{i\omega\tau}=z,
\]
so \(\omega=|z|\) and
\[
\arg z=\frac{\pi}{2}+\omega\tau\pmod{2\pi}.
\]
If \(\Delta\ge0\), write the two negative real roots as \(-\alpha_1\) and \(-\alpha_2\), with \(0<\alpha_1\le\alpha_2=(P+\sqrt\Delta)/2\). The first imaginary crossing among the two factors occurs for the larger magnitude root, at
\[
\tau_c=\frac{\pi}{2\alpha_2}=\frac{\pi}{P+\sqrt\Delta}.
\]
If \(\Delta<0\), the two quadratic roots are conjugate, each of modulus \(\sqrt Q\). The upper root has argument
\[
\arg z_+=\frac{\pi}{2}+\arcsin\!\left(\frac{P}{2\sqrt Q}\right),
\]
so its first positive crossing is
\[
\tau_c=\frac{1}{\sqrt Q}\arcsin\!\left(\frac{P}{2\sqrt Q}\right).
\]
The conjugate factor gives the conjugate imaginary root at the same delay.

Finally, differentiating \(\lambda e^{\lambda\tau}=z\) along a simple characteristic branch yields
\[
\frac{d\lambda}{d\tau}=-\frac{\lambda^2}{1+\lambda\tau}.
\]
At \(\lambda=i\omega\),
\[
\operatorname{Re}\frac{d\lambda}{d\tau}=
\frac{\omega^2}{1+\omega^2\tau^2}>0.
\]
Thus every simple imaginary crossing is from left to right. There is no earlier crossing by the phase calculation above, so stability holds exactly before \(\tau_c\) and is lost permanently after it. When \(\Delta=0\), the scalar factor is repeated; the same threshold remains exact, but the critical pair is algebraically multiple rather than simple.

## Verification
For the paper's Figure 2 parameters
\[
m_1=\frac12,\qquad b=\frac65,\qquad m_2=\frac35,\qquad c_1=\frac25,\qquad c_2=\frac12,
\]
the positive equilibrium is
\[
x_1^*=\frac{-9+\sqrt{201}}{10},\qquad
x_2^*=\frac{-11+\sqrt{201}}{8}.
\]
Substitution gives
\[
P\approx0.468913836285099,\qquad
Q\approx0.013748352003386,
\]
with \(\Delta>0\), hence
\[
\tau_c\approx3.590488585197299.
\]
The source reports convergence at \(\tau=2\) and oscillatory behavior at \(\tau=4\), consistent with the exact threshold. The accompanying `verify.py` checks the equilibrium equations, the factorization, both branches of the threshold formula on representative coefficients, the imaginary-root residual at the threshold, the positive crossing direction, and the Figure 2 numerical value.

## Relationship to prior work
Huang, Long, and Shan derive the common-delay characteristic equation and give Theorem 2.9 in terms of positive roots of a transcendental frequency equation that still contains \(\tau\). The factorization above removes that implicit frequency search and gives a closed threshold directly from \(P\) and \(Q\). General Lambert-\(W\) methods for single-delay equations are classical, and Nishiguchi analyzes stability of a first-order scalar delay equation with complex coefficients. Those general results support the scalar-factor step, but the exact quadratic reduction and the two-case threshold formula above are specialized to the common-delay coexistence linearization of this Beverton–Holt model.

## Limitations
The result is local and linear. It does not prove existence, direction, or orbital stability of nonlinear periodic solutions; it does not cover unequal delays \(\tau_1\ne\tau_2\); and it does not establish global coexistence or exclusion outcomes. At \(\Delta=0\), the critical characteristic pair is multiple, so a standard simple-pair Hopf conclusion cannot be inferred from this threshold formula alone.

## References
1. Q. Huang, Q. Long, and C. Shan, “The effects of two discrete delays on the competition outcomes in a Beverton-Holt competition model,” *Discrete and Continuous Dynamical Systems - B* 30 (2025), 4674–4690. DOI: 10.3934/dcdsb.2025075.
2. J. Nishiguchi, “On parameter dependence of exponential stability of equilibrium solutions in differential equations with a single constant delay,” *Discrete and Continuous Dynamical Systems* 36 (2016), 5657–5679. DOI: 10.3934/dcds.2016048.
3. R. M. Corless, G. H. Gonnet, D. E. G. Hare, D. J. Jeffrey, and D. E. Knuth, “On the Lambert W function,” *Advances in Computational Mathematics* 5 (1996), 329–359. DOI: 10.1007/BF02124750.
