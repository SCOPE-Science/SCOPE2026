# A sharp negative-parameter stability boundary and bistability wedge in a quadratic flow

## Finding
For the three-dimensional quadratic system
\[
\begin{aligned}
\dot x&=-2x-\rho y+yz,\\
\dot y&=x-y+\rho z-2xz,\\
\dot z&=\rho y-5z+xy,
\end{aligned}
\]
consider its previously unclassified **negative** parameter branch \(\rho\le0\). Set
\[
\begin{aligned}
P(\rho)={}&594\rho^8-2076\rho^7-5948\rho^6+20050\rho^5
 +25505\rho^4\\
&-66100\rho^3-63325\rho^2+77500\rho+75000.
\end{aligned}
\]
Let \(\rho_f\) be the unique zero of \(P\) in \((-1.308661,-1.308660)\), and let
\[
\rho_t=\frac{5-\sqrt{105}}4\in(-1.3118,-1.3117).
\]
Then \(\rho_t<\rho_f<0\), and:

1. For every \(\rho_f<\rho\le0\), the origin is **globally exponentially attracting** in \(\mathbb R^3\). This is the exact negative-parameter endpoint of that property; at \(\rho=\rho_f\) another equilibrium exists, and at every \(\rho<\rho_f\) the origin is not globally attracting.
2. For every \(\rho_t<\rho<\rho_f\), there are **exactly three real equilibria**: the origin (a hyperbolic sink), a nonzero hyperbolic saddle with one unstable dimension, and a nonzero hyperbolic sink. Both nonzero equilibria have strictly positive first and second coordinates and strictly negative third coordinate. Their first coordinates satisfy \(0<x_-<x_+<1/4\).
3. At \(\rho=\rho_f\), the two nonzero equilibria coalesce at a nondegenerate saddle-node with first coordinate \(0.1031672875757\ldots\). At \(\rho=\rho_t\), the smaller branch meets the origin at a simple zero eigenvalue (transcritical exchange), while the larger sink persists. In particular, the entire open interval \((\rho_t,\rho_f)\) is a sharply delimited bistable window with a codimension-one saddle separatrix locally.

The width of the open bistable window is \(\rho_f-\rho_t\approx0.0030771473984\). No basin-volume, global basin-boundary, or periodic-orbit classification is asserted.

## Assumptions and scope
The parameter is real and restricted to \(\rho\le0\); state variables are unrestricted real numbers. A hyperbolic sink has all Jacobian eigenvalues with negative real parts; a one-unstable saddle has exactly one eigenvalue with positive real part. “Globally exponentially attracting” means an estimate \(\|u(t)\|\le C e^{-ct}\|u(0)\|\) for constants \(C,c>0\) depending only on the fixed parameter. At the two indicated endpoints no assertion of exponential convergence to the nonhyperbolic equilibria is made.

## Proof
**1. Algebraic equilibrium reduction and certified ordering.** The two last stationary equations form a linear system for \(y,z\) at fixed \(x\), with determinant
\[
D(x,\rho)=2x^2+\rho x+5-\rho^2.
\]
If \(D\ne0\), they give \(y=5x/D\), \(z=x(\rho+x)/D\). Substitution into the first stationary equation gives exactly \(-xQ(x,\rho)/D^2\), with
\[
\begin{aligned}
Q(x,\rho)={}&8x^4+8\rho x^3+(-6\rho^2+10\rho+35)x^2\\
&+(-4\rho^3+5\rho^2+15\rho)x\\
&+(\rho^2-5)(2\rho^2-5\rho-10).
\end{aligned}
\]
The exact polynomial identity \(\operatorname{disc}_x Q=12000P(\rho)\) holds. A rational Sturm computation proves that \(P\) has exactly four real zeros, each simple, isolated respectively by
\[
(-2.011935,-2.011934),\quad(-1.308661,-1.308660),\quad
(2.188758,2.188759),\quad(3.355161,3.355162).
\]
At \(\rho=-1\), \(Q\) has no real roots. At \(\rho=-131/100\), it has precisely two real roots, both in \((0,1/4)\). Neither \(Q(1/4,\rho)\) nor \(Q(0,\rho)\) vanishes within the stated open bistability interval (the latter first vanishes at its left endpoint \(\rho_t\)). Thus the two positive roots persist throughout this interval. Here \(D>2.95\), so the reduction is valid. At \(\rho_f\) they collide; since the discriminant root is simple, the collision is a nondegenerate fold. Moreover \(Q_x(0,\rho_t)=(-375+35\sqrt{105})/8\ne0\), so the small branch crosses \(x=0\) nondegenerately at \(\rho_t\). The value \(\rho_t\) is the negative zero of \(2\rho^2-5\rho-10\). The special singular-reduction parameters \(\rho=\pm\sqrt5\) do not lie in the intervals under discussion.

**2. Strict quadratic global dissipation.** For \(0<a<2\), define
\[
V_a=\frac12\bigl(ax^2+y^2+(2-a)z^2\bigr).
\]
Its cubic derivative cancels identically, and \(\dot V_a=u^T M(a,\rho)u\), where
\[
M=\begin{pmatrix}
-2a&(1-a\rho)/2&0\\
(1-a\rho)/2&-1&\rho(3-a)/2\\
0&\rho(3-a)/2&5a-10
\end{pmatrix}.
\]
Permuting its rows/columns into the order \((z,x,y)\) shows via Sylvester's criterion that \(M\prec0\) if and only if \(F(a,\rho)>0\), where
\[
\begin{aligned}
F(a,\rho)={}&3a^3\rho^2+2a^2\rho^2-10a^2\rho-40a^2\\
&-18a\rho^2+20a\rho+85a-10,
\end{aligned}
\]
because \(\det M=-F/4\). The second exact discriminant identity is
\(\operatorname{disc}_aF=120P(\rho)\). Also \(F(0,\rho)=-10\) and \(F(2,\rho)=-4\rho^2\). Exact rational Sturm counts find two roots of \(F(\cdot,-1)\) in \((0,2)\), and no such roots at \(\rho=-3/2\). Since no discriminant or endpoint crossing occurs for \(\rho_f<\rho<0\), some \(a\in(0,2)\) has \(F(a,\rho)>0\) for every \(\rho\) in that interval; at \(\rho=0\), take \(a=1\). Thus \(M\prec0\) gives global existence and exponential decay. For \(\rho_t<\rho\le\rho_f\) a nonzero equilibrium prevents global attraction; for \(\rho<\rho_t\), the origin has an unstable eigenvalue by the characteristic polynomial in step 3. This establishes sharpness on the whole negative half-line.

**3. Exact stability in the narrow window.** The origin's characteristic polynomial is
\[
\lambda^3+8\lambda^2+(17+\rho-\rho^2)\lambda+(10+5\rho-2\rho^2).
\]
For \(\rho_t<\rho<\rho_f\), all Routh–Hurwitz inequalities are strict; hence the origin is a sink. For a nonzero root \(x\) in the window set \(y=5x/D\) and \(z=x(\rho+x)/D\). Its characteristic polynomial is \(\lambda^3+8\lambda^2+c_2\lambda+c_3\), with
\[
c_2=12+D+(\rho-z)(1-2z)-y^2,
\qquad c_3=\frac{xQ_x(x,\rho)}{D}.
\]
The determinant identity for \(c_3\) follows by reducing the exact Jacobian determinant modulo \(Q\). On the enclosing rational box \(-1.312<\rho<-1.308\), \(0<x<1/4\), one has \(D>2.95\), \(0<y<0.424\), \(|z|<0.112\), giving \(c_2>13\). Direct coefficient bounds imply \(|Q_x|<70\), hence \(|c_3|<6\). Since the quartic has exactly two simple real roots and positive leading coefficient, \(Q_x(x_-,\rho)<0<Q_x(x_+,\rho)\). The smaller root therefore has \(c_3<0\), yielding one positive eigenvalue and two with negative real parts. The larger has \(c_3>0\), and \(8c_2>c_3\); the cubic Routh–Hurwitz criterion gives a sink. Finally, the stable manifold theorem gives the stated two-dimensional local stable manifold of the saddle.

## Verification
The standalone `artifacts/verify_negative_etm.py` carries out exact symbolic reductions and rational Sturm counts for both discriminants and four real discriminant roots, checks the quartic root topology and coordinate barriers, verifies the origin and nonzero-equilibrium characteristic identities, and checks the Lyapunov determinant. Its output is in `artifacts/verification_output.txt`. Interval estimates in Step 3 are explicit rational inequalities; numerical displays of the endpoints only aid interpretation and are not the proof.

## Relationship to prior work
Khalili-Amirabadi and Jalaeian-Farimani, arXiv:2610.04768v1 (first public October 3, 2026), studied this same flow on \(\rho\ge0\). Their full-text Sections 2–9 provide energy-neutrality, an absorbing bound, and positive-parameter bifurcations; they explicitly leave the negative branch for future investigation. A related published note, “Exact global-stability threshold at the first ETM-3D saddle-node” (2026), establishes the **positive** global-stability boundary \(\rho\approx2.188759\) and the centered-quadratic mechanism. That note's discriminant polynomial and general method overlap with the present proof, but its statement does not cover \(\rho<0\), the distinct negative fold \(\rho_f\), the negative transcritical threshold \(\rho_t\), or the coexistence of two sinks separated by a saddle in \((\rho_t,\rho_f)\). The substantive additional result is the sharp negative **hysteresis/bistability classification**, not the discriminant or quadratic form by itself.

## Limitations
This is a real-state, deterministic equilibrium and global-stability result. The exact behavior at both nonhyperbolic endpoints is not fully classified, nor are global basins, periodic orbits, or chaotic dynamics for more negative parameters. The algebraic window is narrow, and the statement does not assert a uniform exponential rate as \(\rho\downarrow\rho_f\). Historical priority beyond the inspected papers and records remains open, and independent validation has not been performed.

## References
1. R. Khalili-Amirabadi and M. Jalaeian-Farimani, “ETM-3D: A One-Parameter Multistable Quadratic Flow with an Explicit Absorbing Set and Intermittent Chaos,” arXiv:2610.04768v1, October 3, 2026. https://arxiv.org/abs/2610.04768
2. “Exact global-stability threshold at the first ETM-3D saddle-node,” published mathematical research note, October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-global-stability-threshold-at-the-first-etm-3d-saddle-node--997f2098aca6
