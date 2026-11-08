# Exact stability-window staircase and unbounded reentrance in a delayed Holling-II predator-prey model

## Finding

Consider the Holling-II prey-maturation model with an instantaneous predator-conversion response (defined below). Suppose its positive coexistence equilibrium exists and that the linearization coefficients satisfy \(0<\alpha<\beta\) and \(\gamma>0\). Write
\[
\delta=\beta^2-\alpha^2,\quad
\theta=\arccos(\alpha/\beta),\quad
\omega_\pm=\frac{\sqrt{\delta+4\gamma}\pm\sqrt\delta}{2},
\quad T=\frac{\theta}{2\pi}\sqrt{1+4\gamma/\delta}.
\]
Define the two strictly increasing sequences of delays
\[
 A_n=\frac{\theta+2\pi n}{\omega_+},\qquad
 B_n=\frac{2\pi-\theta+2\pi n}{\omega_-},\qquad n=0,1,2,\ldots .
\]
**Theorem.** Every positive delay at which the characteristic equation has a purely imaginary root belongs to exactly the union of these sequences (allowing coincidences of one member of each sequence). Away from that union, the number of unstable complex-conjugate root pairs is exactly
\[
U(\tau)=\#\{n\ge0:A_n<\tau\}-\#\{n\ge0:B_n<\tau\}.
\]
The coexistence equilibrium is locally exponentially stable exactly on
\[
[0,A_0)\ \cup\ \bigcup_{\substack{n\ge0\\n+1<T}}(B_n,A_{n+1}),
\]
and is spectrally unstable for every other noncritical delay. At a critical delay it is not linearly exponentially stable, because it has imaginary characteristic roots. Thus the **exact number of reentrant stable open intervals** is
\[
 J=\max\{0,\lceil T\rceil-1\}.
\]
The strict inequality \(n+1<T\) includes the degenerate case in which a stabilizing and destabilizing crossing occur simultaneously: no positive-width interval appears at equality.

There is an explicit positive-parameter biological family with unboundedly many such intervals. Fix \((a,b,d,K,h)=(1,5/4,1,4,1/4)\), let the intrinsic growth rate \(r>0\) vary, and set the conversion delay to zero. With \(\theta_0=\arccos(3/5)\),
\[
J(r)=\max\left\{0,\left\lceil\frac{\theta_0}{2\pi}\sqrt{1+\frac{60}{r}}\right\rceil-1\right\},\qquad
\lim_{r\downarrow0}\sqrt r\,J(r)=\frac{\sqrt{15}\,\theta_0}{\pi}.
\]
In particular, for each integer \(m\ge1\), there are at least \(m\) reentrant stable intervals if and only if
\[
 0<r<\frac{60}{(2\pi m/\theta_0)^2-1}.
\]
The result is a spectral-stability statement about equilibria, not a statement about nonlinear Hopf criticality or the stability of periodic solutions.

## Assumptions and scope

The system is
\[
\begin{aligned}
\dot x(t)&=r x(t)\left(1-\frac{x(t-\tau)}{K}\right)-\frac{a x(t)y(t)}{1+h x(t)},\\
\dot y(t)&=y(t)\left(-d+\frac{b x(t)}{1+h x(t)}\right).
\end{aligned}
\]
The constants \(r,a,b,d,K,h\) are strictly positive, \(\tau\ge0\), \(b>dh\), and \(x_*=d/(b-dh)<K\). The unique positive coexistence equilibrium is
\[
 (x_*,y_*)=\left(\frac{d}{b-dh},\frac{1+hx_*}{a}r\left(1-\frac{x_*}{K}\right)\right).
\]
Define the coefficients, using \(\sigma=1+h x_*\), by
\[
\alpha=\frac{ahx_*y_*}{\sigma^2},\qquad
\beta=\frac{rx_*}{K},\qquad
\gamma=\frac{abx_*y_*}{\sigma^3}.
\]
The additional condition \(\beta>\alpha\) is explicit; it ensures the nondelayed equilibrium is linearly stable. With \(\tau_2=0\), the exact retarded characteristic equation is
\[
F(\lambda,\tau)=\lambda^2-\alpha\lambda+\beta\lambda e^{-\lambda\tau}+\gamma=0.
\]
A stable interval means all characteristic roots have strictly negative real parts, which implies local exponential asymptotic stability of this smooth retarded differential equation at its equilibrium. At noncritical unstable delays at least one conjugate pair has strictly positive real parts.

## Proof

**1. All imaginary roots and their true phases.** For \(\lambda=i\omega\), \(\omega>0\), separating real and imaginary parts gives
\[
\beta\cos(\omega\tau)=\alpha,\qquad
\beta\sin(\omega\tau)=\frac{\omega^2-\gamma}{\omega}.
\]
Squaring gives \(\omega^4-(\delta+2\gamma)\omega^2+\gamma^2=0\), whose only positive solutions are \(\omega_+\) and \(\omega_-\). Their product is \(\gamma\) and their difference is \(\sqrt\delta\), so \(\omega_+>\sqrt\gamma>\omega_-\). Hence the sine at the higher frequency is positive, while at the lower frequency it is negative. Since \(\cos\theta=\alpha/\beta>0\), the admissible phases are respectively \(\theta+2\pi n\) and \(2\pi-\theta+2\pi n\). These give precisely \(A_n\) and \(B_n\). The zero frequency never occurs because \(F(0,\tau)=\gamma>0\).

**2. Direction and simplicity of crossing.** At an imaginary characteristic root, implicit differentiation yields
\[
\frac{d\lambda}{d\tau}=\frac{\beta\lambda^2e^{-\lambda\tau}}{F_\lambda},\qquad
F_\lambda=2\lambda-\alpha+\beta e^{-\lambda\tau}(1-\lambda\tau).
\]
Using the two real/imaginary equations above,
\[
F_\lambda(i\omega,\tau)
=-\tau(\omega^2-\gamma)
+i\left(\frac{\omega^2+\gamma}{\omega}-\alpha\omega\tau\right),
\]
and direct multiplication gives the exact identity
\[
\operatorname{Re}\frac{d\lambda}{d\tau}
=\frac{\omega^4-\gamma^2}{|F_\lambda(i\omega,\tau)|^2}.
\]
Every critical delay is positive and \(\omega^2\ne\gamma\), so \(F_\lambda\ne0\). The high-frequency \(A_n\) crossings increase the unstable-pair count by one, while the low-frequency \(B_n\) crossings decrease it by one. If a pair of distinct frequencies crosses at one delay, their contributions are additive.

**3. Global root count and exact stable intervals.** At zero delay the characteristic polynomial is \(\lambda^2+(\beta-\alpha)\lambda+\gamma\), so it has no unstable roots. For any \(\operatorname{Re}\lambda\ge0\), the characteristic identity bounds
\[
|\lambda|^2\le(\alpha+\beta)|\lambda|+\gamma.
\]
Thus the roots in the closed right half-plane lie in a fixed bounded disk, for all delays. They can enter or exit that half-plane only at the explicit imaginary crossings; their number is finite. Continuity of the characteristic roots and the crossing directions prove the asserted formula for \(U(\tau)\) away from crossings.

Because \(\omega_+>\omega_-\) and \(0<\theta<\pi/2\), one has \(A_n<B_n\) for every \(n\). Immediately after the \(n\)-th low-frequency event \(B_n\), the unstable-pair count is zero exactly if \(B_n<A_{n+1}\). Indeed, if \(A_{n+1}\le B_n\), at least \(n+2\) high-frequency crossings have already occurred by then, compared with only \(n+1\) low-frequency crossings; if the inequality is strict in the other direction, the two counts agree until \(A_{n+1}\). Moreover,
\[
B_n<A_{n+1}
\iff
(n+1)(\omega_+-\omega_-)<\frac{\theta}{2\pi}(\omega_++\omega_-)
\iff n+1<T,
\]
where the intermediate display has the common factor \(2\pi\) divided from both sides (equivalently \(2\pi(n+1)(\omega_+-\omega_-)<\theta(\omega_++\omega_-)\)). The initial stable interval is \([0,A_0)\). Counting all strictly positive integers below \(T\) gives \(J=\max(0,\lceil T\rceil-1)\). Critical delays themselves carry imaginary roots and hence are excluded.

**4. Biological realization and divergent staircase.** For the indicated positive family, the equilibrium and linear coefficients simplify exactly to
\[
x_*=1,\quad y_*=\frac{15r}{16},\quad
\alpha=\frac{3r}{20},\quad\beta=\frac r4,\quad
\gamma=\frac{3r}{5},\quad\delta=\frac{r^2}{25}.
\]
The equilibrium is feasible for every \(r>0\). Inserting these identities into the formula for \(T\) proves
\(T(r)=\theta_0\sqrt{1+60/r}/(2\pi)\), hence the exact integer staircase. The condition \(J(r)\ge m\) is equivalent to \(T(r)>m\); solving this strict inequality yields the displayed \(r\)-threshold. Finally, \(\lceil T\rceil-T\in[0,1)\) gives \(\sqrt r\,J(r)\to\sqrt{15}\theta_0/\pi\).

## Verification

Run `python CHECK.py` with Python 3, NumPy and SymPy. It performs exact rational parameter-to-coefficient reductions; checks eight imaginary-root identities and crossing derivatives; checks the strict staircase at four growth rates; and independently counts unstable roots by a finite numerical argument-principle contour at seven delays. Representative values for \(r=1\) are \(A_0\approx1.052518659644\), \(B_0\approx7.864454820395\), and \(A_1\approx8.184195443291\), giving one reentrant window. Exact counting for \(r\in\{1,0.1,0.01,0.001\}\) gives respectively \(1,3,11,36\) reentrant windows. These computations confirm selected cases and algebra; only the analytic argument proves the quantified theorem.

## Relationship to prior work

Alawfi (2026) introduced and studied this delayed Holling-II model, derived its characteristic equation and imaginary-frequency quartic, and numerically investigated several stability switches and periodic bifurcations at one baseline parameter set. That contribution is prior art. The present result concerns **all** delay values on the instantaneous-conversion slice, obtains the two sign-corrected phase branches, counts **every** stable interval exactly, and exhibits an explicit positive demographic family with arbitrarily many reentrant intervals and a sharp small-growth-rate law. These all-delay and unbounded-count conclusions were not located in the inspected paper. General delay-equation stability-switch machinery and previous predator–prey analyses provide related methods and phenomena but do not, on the inspected evidence, state this exact staircase for the specified family.

## Limitations

The theorem gives the local spectral classification of the positive coexistence equilibrium for exactly zero conversion delay, not a classification of global attractors, nonlinear criticality of crossing points, or periodic-orbit stability. It does not apply automatically to positive conversion delays or to parameter regimes with \(\beta\le\alpha\). Published general stability-switch criteria could subsume portions of the proof methodology; uninspected specialized works remain a historical-priority risk. Numerical contour checks are finite reproducibility tests, not proof of the infinite sequence.

## References

1. A. Alawfi, *Hopf bifurcations and period-doubling cascade in a two-delay predator–prey model with Holling type II response*, Scientific Reports **16**, 30850 (published 2026-10-04), https://doi.org/10.1038/s41598-026-74386-7.
2. H. I. Freedman and V. Sree Hari Rao, *Stability Criteria for a System Involving Two Time Delays*, SIAM Journal on Applied Mathematics **46** (1986), 552–560, https://doi.org/10.1137/0146037. (General background.)
3. L. Nunney, *The effect of long time delays in predator-prey systems*, Theoretical Population Biology **27** (1985), 202–221, https://doi.org/10.1016/0040-5809(85)90010-3. (Related ecological stability phenomena.)
