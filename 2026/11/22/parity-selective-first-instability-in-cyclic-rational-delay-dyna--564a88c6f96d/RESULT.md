# Parity-selective first instability in cyclic rational-delay dynamical maps

## Finding

Consider a ring of \(k\ge2\) positive scalar states, with the indices interpreted modulo \(k\), governed by
\[
 x^{(i)}_{n+1}=1+t\frac{x^{(i+1)}_n}{(x^{(i+1)}_{n-1})^2},\qquad i=1,\ldots,k,\quad t>0.
\]
Its positive synchronous equilibrium has all coordinates \(s=(1+\sqrt{1+4t})/2\). Set \(a=t/s^2\in(0,1)\), so that \(t=a/(1-a)^2\). Define
\[
 c_k=\begin{cases}-1,&k\text{ even},\\-\cos(\pi/k),&k\text{ odd},\end{cases}
 \qquad H_k(a)=1-9a^2+4c_ka^3+12a^4.
\]
For every \(k\ge2\), \(H_k\) has exactly one root \(a_k\) in \((0,1/2)\). Write \(t_k=a_k/(1-a_k)^2\). The synchronous equilibrium is a hyperbolic sink for \(0<t<t_k\), has a unit-modulus multiplier at \(t=t_k\), and is linearly unstable for \(t>t_k\). At the boundary all remaining multipliers lie strictly in the unit disk; the critical multiplier or multipliers are simple and cross the unit circle outward with nonzero radial velocity.

The instability is sharply parity-dependent. For **every even** \(k\), one has \(a_k=1/3\), \(t_k=3/4\), and the sole critical multiplier is \(-1\), in the alternating spatial Fourier mode. For **every odd** \(k\ge3\), \(a_k>1/3\), \(t_k>3/4\), and the sole critical multipliers form a complex-conjugate nonreal pair in the two Fourier modes closest to spatial alternation. For odd \(k\to\infty\),
\[
 a_k=\frac13+\frac{\pi^2}{75k^2}+O(k^{-4}),\qquad
 t_k=\frac34+\frac{3\pi^2}{50k^2}+O(k^{-4}).
\]
In particular, for \(k=3\), \(a_3=0.348356193200759\ldots\), and \(t_3=0.820357195635835\ldots\). At this first crossing the scalar in-phase mode is still strictly contracting. The loss of stability is therefore caused by spatially nonuniform oscillations, not the ordinary in-phase scalar instability at \(t=2\).

## Assumptions and scope

The result holds for every integer \(k\ge2\) and every positive gain \(t\), for the autonomous smooth map of the open positive phase space \((0,\infty)^{2k}\) taking current and previous ring states to updated and current states. Claims of attraction and instability refer to the equilibrium of this finite-dimensional map. At a critical threshold, **nonlinear** stability and the existence, direction, or criticality of any nonlinear flip or Neimark–Sacker bifurcation are not asserted. The formula for \(t_k\) is an exact algebraic or trigonometric characterization and does not require any numerical approximation.

## Proof

**Equilibrium and Fourier decomposition.** The synchronous fixed-point condition \(s=1+t/s\) has the unique positive solution shown above. Since \(t=s(s-1)\), one has \(a=(s-1)/s\), and hence \(t=a/(1-a)^2\), strictly increasing in \(a\in(0,1)\). A first variation \(u^{(i)}_n\) satisfies
\[
 u^{(i)}_{n+1}=a\bigl(u^{(i+1)}_n-2u^{(i+1)}_{n-1}\bigr).
\]
Taking a spatial Fourier mode \(u^{(i)}_n=\lambda^n\omega^i\), where \(\omega^k=1\), gives the exact characteristic equation
\[
 Q_\omega(\lambda)=\lambda^2-a\omega\lambda+2a\omega=0.
\]
Thus the \(2k\) multipliers of the full real Jacobian are precisely the roots of these \(k\) quadratic equations, including algebraic multiplicity.

**Exact Schur test.** For a monic quadratic \(z^2+bz+c\) with complex coefficients, both roots lie in the open disk precisely when \(|c|<1\) and \(|b-\overline b c|<1-|c|^2\). Here \(b=-a\omega\), \(c=2a\omega\); the criterion becomes \(a<1/2\) and
\[
 a^2|2a-\omega|^2<(1-4a^2)^2,
\]
which, on writing \(u=\operatorname{Re}\omega\), is exactly
\[
 H(a,u):=1-9a^2+4ua^3+12a^4>0.
\]
For fixed \(a>0\), this expression increases strictly with \(u\). The minimum cosine among \(k\)-th roots of unity equals \(c_k\) from the finding: it occurs at the sole alternating mode \(\omega=-1\) when \(k\) is even, and at the two conjugate modes \(\exp(\pm i(\pi-\pi/k))\) when \(k\) is odd. It is therefore necessary and sufficient for stability to have \(a<1/2\) and \(H_k(a)>0\).

For \(0<a<1/2\),
\[
 \frac{\partial H}{\partial a}(a,u)=-6a(3-2ua-8a^2)<0
\]
for every \(-1\le u\le1\). Also \(H_k(0)=1\), and \(H_k(1/2)=(c_k-1)/2<0\). This proves existence and uniqueness of the root \(a_k\) and all strict-stability assertions. At equality, the Schur test with \(|c|=2a_k<1\) has exactly one root on the unit circle and one strictly inside for each critical mode. At all other modes the inequality remains strict. For \(a_k<a<1/2\), the critical quadratic is not Schur-stable and has no unit root because the equality occurs at the unique zero; therefore at least one root has modulus greater than one. For \(a\ge1/2\), the modulus of the product of the roots of every \(Q_\omega\) equals \(2a\ge1\), and the already-unstable critical branch cannot regain unit-disk stability. At \(a=1/2\), its strict Schur inequality is violated, so an expanding root still exists; for \(a>1/2\), its root-product modulus exceeds one. The equilibrium is thus linearly unstable for all \(a>a_k\).

**Boundary multipliers and transversality.** At a unit root \(\lambda\) of \(Q_\omega\), the root is simple: a repeated root would require \(a\omega=8\), impossible for \(0<a<1/2\). Implicit differentiation followed by the root equation gives
\[
 \frac{\lambda'(a)}{\lambda(a)}=\frac{\lambda-2}{a(\lambda-4)}.
\]
Consequently, when \(|\lambda|=1\),
\[
 \frac{d}{da}\log|\lambda|=\frac{9-6\cos\theta}{a(17-8\cos\theta)}>0,
 \qquad \lambda=e^{i\theta}.
\]
Since \(da/dt>0\), every critical root moves outward transversely as \(t\) increases. A real unit root can only be \(+1\) or \(-1\). At \(+1\), the characteristic equation requires \(a\omega=-1\), impossible for \(a<1/2\); at \(-1\), it requires \(3a\omega=-1\), hence precisely \(a=1/3\), \(\omega=-1\). Therefore the even critical multiplier is the simple real \(-1\), whereas the odd critical multipliers are a nonreal conjugate pair. The angular location of the latter is characterized by \(\cos\theta=(5-a_k^{-2})/4\), from \(|\lambda-2|=1/a_k\).

**Exact parity and odd-ring asymptotics.** For even \(k\),
\[
 H_k(a)=(a-1)(2a+1)^2(3a-1),
\]
so the unique root in \((0,1/2)\) is \(1/3\), corresponding to \(t_k=3/4\). For odd \(k\), \(c_k=-\cos(\pi/k)>-1\) implies \(H_k(1/3)>0\), so \(a_k>1/3\). As \(k\to\infty\) through odd integers, \(c_k=-1+\pi^2/(2k^2)+O(k^{-4})\). At the limiting simple root \(a=1/3\),
\[
 \partial_aH=-50/9,\qquad \partial_uH=4/27.
\]
The implicit-function theorem yields \(a_k=1/3+\pi^2/(75k^2)+O(k^{-4})\). Differentiating \(t(a)=a/(1-a)^2\) gives \(t'(1/3)=9/2\), proving the stated threshold asymptotic. Finally, the in-phase \(\omega=1\) mode is governed by \(\lambda^2-a\lambda+2a=0\); its pair has modulus \(\sqrt{2a}\) throughout \(0<a<1/2\) and first becomes neutral at \(a=1/2\), i.e. \(t=2\), strictly after the full-ring first crossing.

## Verification

A standalone standard-library-only checker, `CHECKER.py`, evaluates the exact threshold polynomial and the explicit modal quadratic roots for fourteen ring sizes ranging from \(2\) to \(100\). It verifies the critical spectral radius and strictly smaller/larger spectral radii on the two sides, the even/odd threshold ordering, odd-ring asymptotic estimates, and the independent \(k=3\) numerical benchmark. Executing `python CHECKER.py` printed `PASS: 14 ring sizes, spectrum, parity, asymptotic, k=3 benchmark` in the reviewed package. These checks corroborate but do not replace the uniform proof for all integers \(k\).

## Relationship to prior work

Yazlık, Fidancı and Hassani introduced and studied the three-component cyclic rational-delay equations and their stability, including a sufficient local equilibrium criterion; their conclusion explicitly proposes larger cyclic dimensions as an open direction. At identical parameters, their sufficient stability condition becomes \(3a<1\), i.e. \(t<3/4\), which is exact only for even ring dimensions, while the three-component sharp threshold is larger. Bešo, Kalabušić, Mujić and Pilav studied the single-component recurrence and its separate scalar Neimark–Sacker threshold \(t=2\), but scalar dynamics cannot diagnose the earlier spatially nonuniform instability of a coupled ring. These are statements about different spectra, not competing numerical estimates for a common scalar mode. The present finding gives the all-dimension sharp **linearized** stability and parity law without claiming nonlinear bifurcation beyond the eigenvalue crossing.

## Limitations

This classification is restricted to uniform positive gain and the synchronous equilibrium. It makes no claim of global attraction for every positive initial state, the existence or stability of invariant circles or period-two orbits beyond the critical gain, the nonlinear behavior at the neutral threshold, or heterogeneous ring parameters. The critical odd-ring spectral pair is a necessary spectral condition for an oscillatory local bifurcation, not a proof of a nondegenerate Neimark–Sacker bifurcation. The finite numerical checker cannot independently certify infinitely many ring sizes or solve publication-priority uncertainty.

## References

1. Y. Yazlık, M. C. Fidancı, and M. K. Hassani, *Stability analysis of a three-dimensional system of difference equations with quadratic terms*, Journal of Applied Mathematics and Computing 70 (2024), 2521–2539. First publicly available April 6, 2024. https://doi.org/10.1007/s12190-024-02057-9 . Equations (8), (20)–(22), Theorem 4, and concluding open problem.
2. E. Bešo, S. Kalabušić, N. Mujić, and E. Pilav, *Boundedness of solutions and stability of certain second-order difference equation with quadratic term*, Advances in Difference Equations 2020, article 19, first published January 9, 2020. https://doi.org/10.1186/s13662-019-2490-9 . Scalar recurrence and bifurcation at its own threshold.
3. Standard complex quadratic Schur–Cohn stability criterion, used with an explicit substitution and independently proved parameter inequalities above.
