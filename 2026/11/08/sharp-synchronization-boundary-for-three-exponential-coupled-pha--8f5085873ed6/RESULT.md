# Sharp synchronization boundary for three exponential-coupled phase particles

## Finding
For three labelled particles on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), consider the unnormalized continuous-time system
\[
\dot\theta_i=-\sum_{j=1}^3 \sin(\theta_i-\theta_j)\exp\!\left[\beta\cos(\theta_i-\theta_j)\right].
\]
For every real \(\beta>-2/3\), Haar-almost every initial phase triple converges to synchronization. For \(\beta<-2/3\), the equilateral phase state with gaps \(2\pi/3\) is normally exponentially attracting and has a positive-volume basin. The latter lower-side obstruction was previously established; the new contribution is the global synchronization classification for exactly three particles throughout the previously untreated interval between \(-2/3\) and \(-0.16\). No claim is made at equality.

## Assumptions and scope
The coupling is complete, symmetric, unnormalized, with three equal-mass labelled particles; time is continuous. Almost every means Lebesgue measure on \(\mathbb T^3\). A common phase rotation is a neutral symmetry, and normal attraction is taken in the two-dimensional quotient. No statement is made about other particle numbers, normalized attention, or the equality parameter.

## Proof
Write \(f_\beta(s)=\sin s\,e^{\beta\cos s}\) and \(P_\beta(t)=\int_0^t e^{\beta q}\,dq\). The system is gradient ascent for the real-analytic potential
\[
E_\beta(\theta)=\sum_{1\le i<j\le3}P_\beta(\cos(\theta_i-\theta_j)).
\]
The analytic gradient-convergence theorem on compact manifolds implies every orbit converges to a critical point. The center-stable avoidance theorem (Lemma 2.2 of Polyanskiy–Rigollet–Yao, cited below) implies that the entire basin of critical points with at least one positive Hessian eigenvalue has measure zero; no finiteness assumption on critical points is necessary.

If two phases coincide at an equilibrium while the third differs, the third must be antipodal to the pair because its angular velocity is \(-2 f_\beta(\delta)\), and \(f_\beta(\delta)=0\) only when \(\delta=0\) or \(\pi\) modulo \(2\pi\). At the nonsynchronized antipodal collision, the angular eigenvector \((1,1,-2)\) has strictly positive growth eigenvalue \(3e^{-\beta}\).

For three distinct phases, list them in cyclic order and denote the positive circular gaps by \(u,v,w\), with \(u+v+w=2\pi\). Direct subtraction of phase velocities yields
\[
\dot u=-2f_\beta(u)+f_\beta(v)+f_\beta(w),\quad
\dot v=f_\beta(u)-2f_\beta(v)+f_\beta(w),\quad
\dot w=f_\beta(u)+f_\beta(v)-2f_\beta(w).
\]
Thus at an equilibrium all three gap forces agree. The common force is positive: if one gap were \(\ge\pi\), its force would be nonpositive, whereas another gap is in \((0,\pi)\) and has positive force. Thus all gaps lie strictly in \((0,\pi)\).

On this interval,
\[
f'_\beta(s)=e^{\beta\cos s}(\cos s-\beta\sin^2s).
\]
Its sign changes exactly once, from positive to negative. Indeed, for \(t=\cos s\) the factor is \(t-\beta(1-t^2)\), which takes values \(-1\) and \(1\) at the endpoints and has exactly one root in \((-1,1)\) (the second root, when present, lies outside). Hence each positive force level has at most two preimages: a rising-branch angle \(\alpha\) and a falling-branch angle \(\gamma\).

Either all three gaps agree, giving the equilateral triple, or at least two equal gaps occupy one of these branches. When two gaps equal a falling-branch angle \(\gamma\), varying them by \(+t\) and \(-t\) at fixed third gap gives potential second derivative \(-2f'_\beta(\gamma)>0\), hence a positive Hessian direction. In the remaining nonequilateral possibility two rising-branch gaps equal \(\alpha\) and the third falling-branch gap equals \(\gamma=2\pi-2\alpha\). They satisfy \(\pi/2<\alpha<2\pi/3\). Set \(t=-\cos\alpha\in(0,1/2)\). Elementary trigonometry gives
\[
\sin\gamma=2t\sin\alpha,\qquad \cos\alpha-\cos\gamma=(1-2t)(1+t).
\]
From the force equality \(f_\beta(\alpha)=f_\beta(\gamma)\),
\[
\beta=\frac{\log(2t)}{(1-2t)(1+t)}
< -\frac1{1+t}< -\frac23,
\]
where the strict first inequality follows from \(\log z<z-1\) for \(z\ne1\). Thus for \(\beta>-2/3\) this remaining type is impossible. All nonsynchronized critical points have positive Hessian directions, and gradient convergence plus center-stable avoidance give synchronization almost everywhere.

At equilateral gaps the exact derivative is
\[
f'_\beta(2\pi/3)=e^{-\beta/2}\left(-\frac12-\frac{3\beta}{4}\right).
\]
The three-angle Jacobian has a rotational zero eigenvalue and two quotient eigenvalues \(-3f'_\beta(2\pi/3)\). These are strictly negative whenever \(\beta<-2/3\), proving positive-volume local attraction (previously known) and sharpness of the open-range threshold.

## Verification
The standalone `verify.py` uses SymPy to check the trigonometric force identities and NumPy to check representative equilateral Jacobian signatures. It is finite supporting evidence; the all-parameter theorem is proved by the preceding analytic argument and the cited general gradient-flow theorems. Run `python verify.py` with Python 3, SymPy, NumPy installed.

## Relationship to prior work
Polyanskiy, Rigollet, and Yao (arXiv:2507.22857v1, first public 2025-07-30) prove synchronization for all particle counts when \(\beta\ge-0.16\), and the equilateral obstruction for \(\beta<-2/3\) when the particle count is divisible by three. Their analytic gradient convergence and center-stable avoidance theorem are reused and credited. They do not establish the new strict intermediate interval for exactly three particles. Criscitiello, Rebjock, McRae, and Boumal (arXiv:2405.18273v2) prove a related exponential circle theorem for positive \(\beta\), not the intermediate negative interval. Absence in indexed searches is not proof of historical priority.

## Limitations
Exactly three particles; continuous-time unnormalized complete coupling; no endpoint assertion, other particle counts, or normalized/discrete dynamics. The known attracting lower-side obstruction is not claimed as independently discovered. No independent audit or historical-priority certification has been performed.

## References
1. Y. Polyanskiy, P. Rigollet, A. Yao, *Synchronization of mean-field models on the circle*, arXiv:2507.22857v1 (2025), https://arxiv.org/html/2507.22857v1, especially Lemma 2.2, Corollaries 2.4–2.6, and Appendix C.6.
2. C. Criscitiello, Q. Rebjock, A. D. McRae, N. Boumal, *Synchronization on circles and spheres with nonlinear interactions*, arXiv:2405.18273v2 (2026 revision of 2024 preprint), https://arxiv.org/html/2405.18273v2.
3. S. Łojasiewicz, *Ensembles semi-analytiques* (1965), for analytic gradient convergence; M. Shub, *Global Stability of Dynamical Systems* (1987), for the center-stable manifold theorem (both cited in Reference 1).
