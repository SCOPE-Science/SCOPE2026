# Direction-dependent locking-band deformation in two travelling-wave characteristic flows

## Finding
Let \(m\in\mathbb Z\setminus\{1\}\), put \(k=m-1\), and consider the positive periodic characteristic speed
\[
f_{v,\varepsilon,m}(x,t)=2+\cos(x-vt)+\varepsilon\cos(x-mvt),\quad v>0,\quad |\varepsilon|<1.
\]
Spatial period is \(2\pi\) and temporal period \(T=2\pi/v\). A \((p,q)\) characteristic cycle obeys \(x(t+qT)=x(t)+2\pi p\); the pair \((p,q)\) is primitive when \(p,q\) are coprime positive integers. The \((1,1)\) locking region is the set of speeds \(v\) supporting a characteristic with \(x(t+T)=x(t)+2\pi\).

**Theorem.** For each fixed integer \(k\ne0\) there is \(\varepsilon_k>0\) such that, for \(0<|\varepsilon|<\varepsilon_k\), the positive-speed \((1,1)\) locking set is exactly the closed interval \([v_-(\varepsilon),v_+(\varepsilon)]\). Each endpoint carries exactly one nonhyperbolic locked characteristic. In the open interior there are exactly two \((1,1)\) characteristics modulo spatial translation, one attracting and one repelling, and their Floquet multipliers are exact reciprocals. The two endpoints are analytic even functions of \(\varepsilon\), with
\[
\begin{aligned}
v_-(\varepsilon)&=1+\left(\frac1{2k}+\frac1{4k^2}\right)\varepsilon^2+O_k(\varepsilon^4),\\
v_+(\varepsilon)&=3+\left(\frac1{6k}-\frac1{36k^2}\right)\varepsilon^2+O_k(\varepsilon^4),\\
v_+(\varepsilon)-v_-(\varepsilon)&=2-\frac{6k+5}{18k^2}\varepsilon^2+O_k(\varepsilon^4).
\end{aligned}
\]
Thus a faster co-propagating second grating (\(m\ge2\), so \(k\ge1\)) **narrows** the trapping-speed interval to second order; a stationary or counter-propagating grating (\(m\le0\), so \(k\le-1\)) **widens** it. For the specific two-speed perturbation \(m=2\), the width is \(2-11\varepsilon^2/18+O(\varepsilon^4)\); for a stationary second grating \(m=0\), it is \(2+\varepsilon^2/18+O(\varepsilon^4)\).

**Structural restriction.** For every \(v>0\) and every \(|\varepsilon|<1\), no characteristic has an *isolated attracting primitive* \((p,q)\) cycle with \(q>1\). Such a subharmonic cycle can only occur in a neutral family for which the appropriate iterate of the period map is the identity. This last restriction is the classical projective/Riccati obstruction specialized to the characteristic system; it is not claimed as a new general theorem about forced phase equations.

## Assumptions and scope
The medium is one-dimensional and impedance matched so that its right-going characteristics solve \(\dot x=f_{v,\varepsilon,m}(x,t)\). The period \(T\) is a valid forcing period even when the moving-frame forcing has a smaller fundamental period. The result is for fixed integer \(m\ne1\) and sufficiently small perturbation amplitude for the sharp expansions and global \((1,1)\) census; the projective obstruction holds at arbitrary amplitude \(|\varepsilon|<1\). The strict positivity \(f\ge1-|\varepsilon|>0\) is automatic. No result is asserted for fields with spatial harmonics beyond the first or for the full non-impedance-matched wave equation.

## Proof
Put \(y=x-vt\), so that
\[
\dot y=2-v+\cos y+\varepsilon\cos(y-kvt)=:F(y,t).
\]
The \((1,1)\) condition is precisely \(y(T)=y(0)\). Write \(z=\tan(y/2)\) in the projective real line. The identity \(\cos(y-kvt)=\cos y\cos(kvt)+\sin y\sin(kvt)\) turns the phase equation into the Riccati equation
\[
\dot z=\frac{3-v+\varepsilon\cos(kvt)}2+\varepsilon\sin(kvt)z+\frac{1-v-\varepsilon\cos(kvt)}2z^2.
\]
It is the projectivization \(z=U/V\) of
\[
\frac{d}{dt}\begin{pmatrix}U\\V\end{pmatrix}=
\frac12\begin{pmatrix}
\varepsilon\sin(kvt)&3-v+\varepsilon\cos(kvt)\\
v-1+\varepsilon\cos(kvt)&-\varepsilon\sin(kvt)
\end{pmatrix}\begin{pmatrix}U\\V\end{pmatrix}.
\]
This coefficient matrix has trace zero, so its period matrix has determinant one. The stroboscopic circle map is therefore an orientation-preserving real Möbius transformation. A nonidentity Möbius map has at most two fixed points. Classification of real Möbius transformations also shows that every periodic point of primitive period \(q>1\) belongs to an elliptic finite-order transformation, in which case its \(q\)-th iterate is the identity on the whole circle; hence such periodic points are not isolated attracting cycles. For a hyperbolic Möbius map the two fixed-point derivatives have product exactly one.

Reversal \((y,t)\mapsto(-y,-t)\) preserves the differential equation, since \(F(-y,-t)=F(y,t)\). If \(P\) is the period map and \(R(y)=-y\), then \(RPR=P^{-1}\). A unique parabolic fixed point must satisfy \(R(y)=y\pmod{2\pi}\), hence it must be at \(0\) or \(\pi\). At the unperturbed upper fold \(v=3\) that point is \(0\), and at the lower fold \(v=1\) it is \(\pi\). The signed displacement \(P(y)-y\), differentiated with respect to \(v\) at either unperturbed fold, has derivative \(-T\ne0\). Its second derivative in \(y\) is nonzero (negative at \(0\), positive at \(\pi\)). Analytic fold continuation therefore gives one unique nearby nondegenerate fold at each endpoint, with the same pinned initial phase.

To compute their coefficients, set \(v=v_0+c\varepsilon^2+O(\varepsilon^3)\), \(y=y_0+\varepsilon y_1+\varepsilon^2y_2+\cdots\). At the upper fold \((v_0,y_0)=(3,0)\), the first-order periodic solution is \(y_1(t)=\sin(kv_0t)/(kv_0)\), and the second-order equation is
\[
\dot y_2=-c-\tfrac12y_1^2+y_1\sin(kv_0t).
\]
Integrating over one period yields \(c=1/(2kv_0)-1/(4k^2v_0^2)=1/(6k)-1/(36k^2)\). At the lower fold \((v_0,y_0)=(1,\pi)\), one has \(y_1(t)=-\sin(kv_0t)/(kv_0)\) and
\[
\dot y_2=-c+\tfrac12y_1^2-y_1\sin(kv_0t),
\]
so \(c=1/(2k)+1/(4k^2)\). Terms caused by the \(O(\varepsilon^2)\) shift of \(v\) in the temporal phase enter only at higher order.

The transformation \(t\mapsto t+\pi/(kv)\) changes the sign of \(\cos(y-kvt)\) without changing the autonomous part of the moving-frame equation. Thus the flows at \(\varepsilon\) and \(-\varepsilon\) are conjugate by a change of the temporal origin. Fold speed is invariant under this conjugacy, so both analytic endpoint functions are even, upgrading the remainders from cubic to \(O_k(\varepsilon^4)\).

At \(\varepsilon=0\), there are exactly two hyperbolic \((1,1)\) solutions for \(1<v<3\), one parabolic solution at each endpoint, and none elsewhere. Every \((1,1)\) solution for nonzero \(\varepsilon\) obeys the speed bound \(1-|\varepsilon|\le v\le3+|\varepsilon|\), since \(v\) equals the mean speed over one period. Compactness, hyperbolic continuation away from the two folds, the nondegenerate local fold normal forms, and the global two-fixed-point bound from the Möbius representation give exactly the asserted interval and counts, without additional remote \((1,1)\) branches. Subtracting the two endpoint expansions gives the width coefficient. Because \(6k+5>0\) for positive integers \(k\) and \(6k+5<0\) for negative integers \(k\), the directional sign reversal is strict.

## Verification
The standalone Python checker `check.py` symbolically verifies the Riccati coefficients and width identity, numerically obtains the two parabolic folds by shooting from their symmetry-pinned phases, tests twelve combinations of the secondary-wave index and perturbation amplitude, and verifies exact-reciprocity predictions numerically for four hyperbolic pairs. Run `python check.py` with NumPy, SciPy, and SymPy. Its successful terminal line is `VERIFY_OK symbolic_projective=1 quadratic_coefficients=1 fold_cases=12 reciprocal_pairs=4`. Finite numerical agreement supports, but does not replace, the analytic continuation and Möbius arguments.

## Relationship to prior work
Davies and Hiltunen, arXiv:2610.16847, investigate accumulation along characteristic limit cycles for travelling and superposed travelling modulations. Their displayed two-wave example has \(m=2\) and fixed secondary-wave strength \(1/2\); Section 4.3 establishes persistence of an already hyperbolic cycle under small perturbation. That argument assumes a nonzero Floquet exponent and does not locate the nonhyperbolic fold endpoints addressed here. The result above supplies a small-strength *boundary* calculation and its dependence on whether the second grating moves ahead of or against the first.

The forced Adler literature, including Gandhi–Knobloch–Beaume (2015), already studies phase-slip tongues and symmetric forcing; the projective obstruction to isolated subharmonic locking in first-spatial-harmonic systems is classical, also reflected in the integer-only locking of the single-harmonic RSJ equation discussed by Tsarev–Fominov (2025). The original contribution claimed here is the explicit two-wave, velocity-index-dependent **paired fold expansion and signed locking-band deformation** for the wave-characteristic model, together with its exact first-harmonic projective organization. General perturbative saddle-node theory is acknowledged; this is not a claim to invent that theory.

## Limitations
The exact coefficients depend on the normalization of the primary modulation, \(2+\cos(x-vt)\), the common spatial wavenumber, the integer secondary velocity ratio, and small secondary amplitude. The no-subharmonic assertion is a consequence of first spatial harmonic Riccati structure and can fail with additional spatial harmonics. The nonzero-amplitude fold curves away from their perturbative neighborhoods and nonlocal resonance bands of other integer windings are not classified. Historical priority of the explicit coefficients has not been independently certified. The periodic characteristic-flow conclusion does not prove wave-energy growth without the additional field hypotheses of the motivating paper.

## References
1. B. Davies and E. O. Hiltunen, *Limit cycles govern wave energy accumulation in space-time-varying materials*, arXiv:2610.16847v1, first public 2026-10-12, https://arxiv.org/abs/2610.16847.
2. P. Gandhi, E. Knobloch, and C. Beaume, *Dynamics of phase slips in systems with time-periodic modulation*, *Physical Review E* 92 (2015), 062914, arXiv:1509.03582, https://arxiv.org/html/1509.03582v2.
3. P. N. Tsarev and Ya. V. Fominov, *All fractional Shapiro steps in the RSJ model with two Josephson harmonics*, arXiv:2505.20502, https://arxiv.org/abs/2505.20502.
