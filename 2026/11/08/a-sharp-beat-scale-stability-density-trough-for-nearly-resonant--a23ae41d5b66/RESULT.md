# A sharp beat-scale stability-density trough for nearly resonant sampled oscillators

## Finding
Consider the two independent controlled planar rotation modes with angular frequencies \(1\) and \(1+\varepsilon\), subject to the same fixed uniform sampling duration \(h\) and per-mode zero-order-hold negative state feedback. Let \(P_\varepsilon(T)\) be the fraction (Lebesgue measure divided by \(T\)) of durations \(h\in(0,T)\) for which **both** sampled closed-loop modes are strictly Schur stable. For every fixed \(L>0\),
\[
P_\varepsilon(L/\varepsilon)=F(L)+O_L(\varepsilon)\qquad(\varepsilon\downarrow0),
\]
where \(a=\pi/2\), \(L=2\pi q+r\) with \(q=\lfloor L/(2\pi)\rfloor\) and \(0\le r<2\pi\), and
\[
F(L)=\frac{q a^2+J(r)}{2\pi L},\qquad
J(r)=\begin{cases}
ar-r^2/2,&0\le r\le a,\\
a^2/2,&a\le r\le 2\pi-a,\\
a^2/2+(r-2\pi+a)^2/2,&2\pi-a\le r<2\pi.
\end{cases}
\]
This **complete beat-scale density law** has a unique global minimum over all \(L>0\):
\[
L_*=\frac{\pi\sqrt{10}}2,\qquad
\min_{L>0}F(L)=\frac{\sqrt{10}-3}{4}=0.0405694150420948\ldots.
\]
In contrast, the exactly resonant system \(\varepsilon=0\) has long-horizon stable-duration density \(1/4\). For each fixed irrational \(\varepsilon>0\), the long-horizon density exists and equals \(\arctan(1+\varepsilon)/(4\pi)\), approaching \(1/16\) as \(\varepsilon\downarrow0\) through irrationals. Thus the near-resonant beat window exhibits a **strict undershoot below both limiting densities**, as well as noncommuting time/frequency limits.

## Assumptions and scope
Use the real planar complex-coordinate notation \(z_j\in\mathbb C\) for two independent physical two-component states. The plant has dynamics \(\dot z_j(t)=i\omega_j z_j(t)+u_j(t)\), with \(\omega_1=1\) and \(\omega_2=1+\varepsilon\), \(\varepsilon>0\). On every \([kh,(k+1)h)\), the held control is \(u_j(t)=-z_j(kh)\), with the same fixed \(h>0\) for both modes; the continuous-feedback system \(\dot z_j=(i\omega_j-1)z_j\) is exponentially stable. The sampled matrix is block diagonal in the two real planes. Stability means both real \(2\times2\) blocks have eigenvalues of modulus strictly below one, equivalently exponential decay for the fixed-period sample-and-hold closed loop. The set of admissible \(h\)'s is measured in Lebesgue measure, **not** a randomized control schedule: \(h\) is fixed after selection. Results on irrational detuning are only asserted for the long-horizon limit; the finite beat-scale law holds for every real \(\varepsilon\downarrow0\).

## Proof
**1. Exact one-mode sampled factor.** Integrating the forced rotation exactly over one holding interval gives the complex sampled multiplier
\[
m_\omega(h)=e^{i\omega h}-\int_0^h e^{i\omega s}\,ds
=\left(1+\frac{i}{\omega}\right)e^{i\omega h}-\frac{i}{\omega}.
\]
Its modulus satisfies
\[
|m_\omega(h)|^2
=1+\frac{2(1-\cos(\omega h))}{\omega^2}-\frac{2\sin(\omega h)}{\omega}.
\]
Writing \(\theta=\omega h\bmod2\pi\), the strict condition \(|m_\omega(h)|<1\) is \(1-\cos\theta<\omega\sin\theta\), which holds precisely for
\[
0<\theta<\beta_\omega,\qquad \beta_\omega=2\arctan\omega\in(0,\pi).
\]
Indeed the right-hand side is nonpositive on \([\pi,2\pi]\), and on \((0,\pi)\), division by \(2\sin(\theta/2)>0\) gives \(\tan(\theta/2)<\omega\). Hence the two-mode stable-duration set is exactly the intersection of the phase windows \(h\bmod2\pi\in(0,a)\) and \((1+\varepsilon)h\bmod2\pi\in(0,\beta_{1+\varepsilon})\), where \(a=\beta_1=\pi/2\).

**2. Two-scale averaging with an error bound.** Split positive durations into full fast periods \(h=2\pi k+s\) with \(s\in[0,2\pi)\). The second mode has phase \((1+\varepsilon)h\equiv s+2\pi\varepsilon k+\varepsilon s\pmod{2\pi}\). Uniformly in the slow phase \(\delta=2\pi\varepsilon k\), replacing \(\beta_{1+\varepsilon}\) by \(a\) and deleting \(\varepsilon s\) changes the \(s\)-measure of the intersection by \(O(\varepsilon)\): both affected intervals have at most two endpoints, and each endpoint shifts by \(O(\varepsilon)\). The limiting intersection length in one fast period is
\[
U(\delta)=\sum_{j\in\mathbb Z}(a-|\delta-2\pi j|)_+,
\qquad (x)_+=\max(x,0).
\]
Here \(U\) is periodic with period \(2\pi\) and is Lipschitz. For \(T=L/\varepsilon\), there are \(L/(2\pi\varepsilon)+O(1)\) full periods and at most one bounded remainder. Summation of the preceding uniform errors, followed by the Lipschitz Riemann-sum estimate for \(U\), yields
\[
\operatorname{Leb}\{0<h<T:\text{both stable}\}
=\frac{1}{2\pi\varepsilon}\int_0^L U(s)\,ds+O_L(1).
\]
Division by \(T=L/\varepsilon\) proves \(P_\varepsilon(T)=\frac1{2\pi L}\int_0^L U(s)\,ds+O_L(\varepsilon)\). Neither irrationality nor any stochastic assumption is required.

**3. Exact phase integral.** On \([0,2\pi]\), the kernel is
\[
U(s)=\begin{cases}a-s,&0\le s\le a,\\0,&a\le s\le 2\pi-a,\\s-(2\pi-a),&2\pi-a\le s\le2\pi.\end{cases}
\]
Consequently \(\int_0^{2\pi}U(s)\,ds=a^2\), and integration of the three pieces on the final partial period gives \(J(r)\), establishing the asserted closed formula for every \(L>0\).

**4. Sharp global minimizer.** On \(0<L\le a\), \(F(L)=1/4-L/(4\pi)\) is strictly decreasing; on \(a\le L\le2\pi-a\), \(F(L)=\pi/(16L)\) is strictly decreasing. On \(2\pi-a\le L\le2\pi\),
\[
F(L)=\frac{a^2+(L-3a)^2}{4\pi L}
=\frac{L-6a+10a^2/L}{4\pi}.
\]
Its derivative has the sign of \(1-10a^2/L^2\), so it decreases then increases, with unique minimum at \(L_*=a\sqrt{10}\), strictly inside \((3a,4a)\). Its value is \((\sqrt{10}-3)/4<1/16\). For \(L=2\pi q+r\) with \(q\ge1\), the expression for \(F\) is a weighted average of the full-period mean \(a^2/(4\pi^2)=1/16\) and (when \(r>0\)) the initial-segment average \(F(r)\), each at least \(F(L_*)\) with the first strictly larger; hence no later-period minimum ties \(F(L_*)\). Uniqueness follows.

**5. Two distinct long-horizon limits.** At exact resonance, the two stability intervals coincide modulo \(2\pi\); their density is \(a/(2\pi)=1/4\). For fixed irrational \(\varepsilon>0\), the linear torus flow \(h\mapsto (h,(1+\varepsilon)h)\bmod2\pi\) is equidistributed, and the rectangle's boundary has measure zero. Therefore its visiting-time proportion tends to \(a\beta_{1+\varepsilon}/(2\pi)^2=\arctan(1+\varepsilon)/(4\pi)\), which tends to \(1/16\) at vanishing detuning. The limits do not commute because the exact-resonance long-horizon density remains \(1/4\).

## Verification
The included standalone `verify.py` independently constructs the closed-loop multipliers, measures finite stable-duration intersections by exact *interval geometry* (subject only to floating-point arithmetic), evaluates the piecewise phase law and its global minimizer, and tests the irrational-frequency long-horizon average. It reports `VERIFY_PASS` with deterministic tests. These computations check finite instances only. The quantifiers for every \(L>0\), the sharp global minimum and the irrational-horizon claim rely on the preceding analytic proofs.

## Relationship to prior work
The exact zero-order-hold map and small-sampling stabilization questions are classical. Osinenko, Beckenbach and Streif (2018) prove practical sample-and-hold stabilization for nonlinear systems under approximate control optimizers; their Theorem 1 is not a characterization of the **density of all possibly large stabilizing sampling durations**, and does not compute a near-resonant two-mode slow-window law. Osinenko and Yaremenko (2021) develop stochastic Lyapunov stabilization in the sample-and-hold sense; their Theorems 1–2 concern stochastic practical stability with sufficiently short holds and do not imply the present phase-density formula. Wakaiki (2021) treats strong stability for sampled infinite-dimensional Riesz-spectral systems under sufficiently fast sampling, not this finite-dimensional resonance-density classification. Classical Kronecker–Weyl equidistribution is acknowledged and used only for the fixed-irrational-detuning long-horizon corollary; the new beat-scale formula and its global undershoot are obtained from the explicit sampled map and finite-window averaging. No claim is made to invent the equidistribution theorem or the zero-order-hold formula.

## Limitations
The result concerns two *uncoupled*, undamped rotating modes with identical scalar state-feedback gain and a common deterministic uniform hold duration. It counts stability over candidate sample intervals; it does not assert robustness to jitter, arbitrary feedback matrices, more oscillators, or fast execution for larger hold durations. The displayed convergence estimate holds at fixed positive \(L\), not uniformly as \(L\to\infty\). For a fixed *rational* nonzero detuning, the long-horizon density can depend on arithmetic and is not asserted to equal the irrational formula. Publication-priority uncertainty persists for older specialized sampling-resonance literature not fully accessible.

## References
1. P. Osinenko, L. Beckenbach and S. Streif, *Practical sample-and-hold stabilization of nonlinear systems under approximate optimizers* (public preprint 6 March 2018), [arXiv:1803.02203](https://arxiv.org/abs/1803.02203), especially Theorem 1.
2. P. Osinenko and G. Yaremenko, *On stochastic stabilization of sampled systems* (public preprint 15 May 2021), [arXiv:2105.07152](https://arxiv.org/abs/2105.07152), especially Theorems 1 and 2.
3. M. Wakaiki, *Strong Stability of Sampled-Data Riesz-Spectral Systems*, SIAM Journal on Control and Optimization 59 (2021), DOI [10.1137/20M1356877](https://doi.org/10.1137/20M1356877); abstract and MSC 93D15 inspected.
4. Classical Kronecker–Weyl equidistribution for irrational linear flows on a torus; used as an acknowledged standard theorem.
