# Exact Floquet neutrality of the harmonic cycle in the Adjaï–Akande–Yehossou–Monsia family
## Finding
For every integer \(n\ge 0\), consider the planar form of the mixed Liénard equation
\[
\ddot x+x\left(\dot x^2+\dot x\sum_{\ell=0}^{n}x^{2\ell}+x^2-1\right)\dot x+x^{2n+3}=0.
\]
Writing \(y=\dot x\) and
\[
S_n(x)=\sum_{\ell=0}^{n}x^{2\ell},
\qquad
R=x^2+y^2-1,
\]
the exact harmonic orbit
\[
\gamma(t)=(\cos t,-\sin t),
\qquad 0\le t\le 2\pi,
\]
has both planar Floquet multipliers equal to \(1\). Equivalently, its nontrivial characteristic exponent is exactly zero for every \(n\ge0\).

More precisely, the full nonlinear system satisfies the exact normal-defect identity
\[
\dot R=-2xy\bigl(y+S_n(x)\bigr)R.
\]
Consequently the unit circle is invariant, and linearizing this scalar equation normally along \(\gamma\) gives a normal multiplier of one. Thus the harmonic cycle is nonhyperbolic for every member of the family and cannot be exponentially attracting or exponentially repelling.

This statement does not decide whether the periodic orbit is isolated, semistable, or contained in a larger periodic annulus; those questions require higher-order return-map information beyond the neutral first variation.

## Assumptions and scope
The result concerns equation (1.8) in the cited article exactly as printed, with integer \(n\ge0\), interpreted as the smooth planar autonomous system
\[
\dot x=y,
\qquad
\dot y=-x\left(y^2+yS_n(x)+x^2-1\right)y-x^{2n+3}.
\]
No perturbation, averaging approximation, or numerical trajectory is used. The term “Floquet multiplier” refers to the multipliers of the period-\(2\pi\) variational equation along the exact harmonic orbit. One multiplier is the standard tangential multiplier \(1\); the theorem identifies the transverse multiplier.

## Proof
First rewrite the damping factor by using \(R=x^2+y^2-1\):
\[
y^2+yS_n(x)+x^2-1=R+yS_n(x).
\]
Hence
\[
\dot y=-xR y-xy^2S_n(x)-x^{2n+3}.
\]
Differentiating \(R\) gives
\[
\dot R=2x\dot x+2y\dot y=2y(x+\dot y).
\]
The finite geometric-sum identity
\[
1-x^{2n+2}=(1-x^2)S_n(x)
\]
implies
\[
\begin{aligned}
x+\dot y
&=x-x^{2n+3}-xy^2S_n(x)-xRy\\
&=x\bigl(1-x^{2n+2}\bigr)-xy^2S_n(x)-xRy\\
&=x\bigl((1-x^2)-y^2\bigr)S_n(x)-xRy\\
&=-xR\bigl(S_n(x)+y\bigr).
\end{aligned}
\]
Therefore
\[
\dot R=-2xy\bigl(S_n(x)+y\bigr)R.
\]
On \(R=0\), the source's exact solution gives \(x=\cos t\), \(y=-\sin t\). The normal variational equation is therefore
\[
\dot \rho=-2x(t)y(t)\bigl(S_n(x(t))+y(t)\bigr)\rho.
\]
Its period exponent is
\[
I_n=-2\int_0^{2\pi}x yS_n(x)\,dt-2\int_0^{2\pi}xy^2\,dt.
\]
For the first term, \(dx=y\,dt\), so over the closed orbit
\[
\int_0^{2\pi}xyS_n(x)\,dt
=
\oint xS_n(x)\,dx=0.
\]
For the second term,
\[
\int_0^{2\pi}\cos t\,\sin^2t\,dt=0.
\]
Thus \(I_n=0\), and the transverse Floquet multiplier is \(e^{I_n}=1\). The tangential multiplier of an autonomous periodic orbit is also \(1\), proving the claim.

The same result follows from Liouville's planar formula. Along the unit circle the divergence is
\[
-2xy\bigl(y+S_n(x)\bigr),
\]
whose period integral is the same \(I_n=0\).

## Verification
The accompanying `verify.py` reconstructs the finite geometric identity and the exact defect factorization at the polynomial level for every \(0\le n\le64\), and checks the two zero-integral reductions used in the Floquet calculation. Its output is stored in `verification_output.txt`.

The finite replay is an implementation check, not the proof for arbitrary \(n\). The all-\(n\) argument is the symbolic geometric-series calculation above.

## Relationship to prior work
Adjaï, Akande, Yehossou, and Monsia introduce this exact family as equation (1.8), prove that \(x(t)=\cos t\) is an exact harmonic solution for every integer \(n\ge0\), and display phase portraits for \(n=0,1,2\). Their paper discusses exact periodic solutions and algebraic limit cycles but does not compute a characteristic exponent or Floquet multiplier for equation (1.8).

The broader generalized-Liénard literature contains standard stability criteria and examples of hyperbolic stable limit cycles. Those general results do not determine the multiplier of this specific constructed family. Evaluating the exact normal defect here shows that the harmonic orbit lies precisely at the neutral Floquet boundary for every \(n\), despite the increasingly high polynomial degree.

Focused searches by DOI, exact title, equation-family terms, Floquet terminology, characteristic-exponent terminology, and the radial-defect formulation did not locate a same-system statement implying this all-\(n\) neutrality result. The closest indexed results concern Floquet or volume identities in different dynamical systems.

## Limitations
The finding is a first-variation statement. A unit transverse multiplier does not by itself prove that the orbit is non-isolated or Lyapunov stable, and it does not determine a higher-order Poincaré return coefficient. Accordingly, no correction is asserted to the mere existence of the exact periodic orbit. The result only rules out hyperbolicity and exponential transverse attraction or repulsion for equation (1.8).

The earliest exact public date used here is the journal publication date, 16 June 2022. A separate public record labels the work “January 2022” but does not supply a complete calendar date, so it is not used as date-only evidence.

## References
1. K. K. D. Adjaï, J. Akande, A. V. R. Yehossou, M. D. Monsia, “Periodic solutions and limit cycles of mixed Lienard-type differential equations,” *AIMS Mathematics* 7 (2022), 15195–15211. DOI: 10.3934/math.2022833.
2. G. Villari, F. Zanolin, “On the Qualitative Behavior of a Class of Generalized Liénard Planar Systems,” *Journal of Dynamics and Differential Equations* 34 (2022), 179–207. DOI: 10.1007/s10884-021-09984-2.
