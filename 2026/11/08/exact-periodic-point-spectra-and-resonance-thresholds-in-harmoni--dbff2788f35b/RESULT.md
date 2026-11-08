# Exact periodic-point spectra and resonance thresholds in harmonic outer billiards

## Finding
For every integer \(n\geq 6\) and parameter \(0<\varepsilon<n^{-2}\), consider the outer-billiard map of the strictly convex curve
\[
\gamma(t)=e^{it}+\varepsilon e^{int}.
\]
Put \(N=n-1\), \(\theta=2\pi/N\), \(c=\cos\theta\), and \(k=N/\gcd(N,2)\). Two explicitly symmetric families of outer-billiard points, at intersections of tangents to consecutive-by-two radial maxima and minima, each consist of \(\gcd(N,2)\) distinct primitive \(k\)-cycles.

Define
\[
\begin{aligned}
\tau_+(\varepsilon)&=2-\frac{4c^2N^2\varepsilon}{(1+\varepsilon)(1+n^2\varepsilon)},\\
\tau_-(\varepsilon)&=2+\frac{4c^2N^2\varepsilon}{(1-\varepsilon)(1-n^2\varepsilon)},\\
\phi(\varepsilon)&=\arccos(\tau_+(\varepsilon)/2),\\
\eta(\varepsilon)&=\operatorname{arcosh}(\tau_-(\varepsilon)/2).
\end{aligned}
\]
The exact multipliers of the primitive-period derivative are \(e^{\pm i k\phi}\) on every maximum-tangent cycle and \(e^{\pm k\eta}\) on every minimum-tangent cycle. In the entire stated convexity range, \(0<\tau_+<2<\tau_-\), so the first cycles are linearly elliptic or resonant, whereas the second are hyperbolic. Both \(\phi\) and \(\eta\) increase strictly with \(\varepsilon\).

The elliptic cycles have **scalar monodromy** \(DT^k=(-1)^j I\) at precisely the following complete finite list of parameters. Let
\[
\phi_*=\arccos\!\left(1-\frac{c^2N^2}{n^2+1}\right),\qquad
R_n=\left\lceil\frac{k\phi_*}{\pi}\right\rceil-1.
\]
For each integer \(1\leq j\leq R_n\), set \(A_j=1-\cos(j\pi/k)\) and \(B_j=2c^2N^2-(1+n^2)A_j\). Then there is exactly one resonance parameter,
\[
\boxed{\varepsilon_j=\frac{2A_j}{B_j+\sqrt{B_j^2-4n^2A_j^2}}},
\]
at which \(DT^k=(-1)^jI\). There are no other scalar-monodromy parameters in \((0,n^{-2})\). The \(\varepsilon_j\) increase strictly with \(j\). In particular, \(R_6=R_7=0\), \(R_8=1\), \(R_{10}=2\), and the number of such resonances grows with \(n\). These are linear resonance statements, not assertions about nonlinear stability or bifurcation.

The small-perturbation splitting is
\[
\phi(\varepsilon)\sim 2cN\sqrt\varepsilon,\qquad
\eta(\varepsilon)\sim2cN\sqrt\varepsilon\quad(\varepsilon\downarrow0).
\]
At the upper convexity boundary, with \(\delta=1-n^2\varepsilon\downarrow0\), the hyperbolic exponent diverges as
\[
\eta(\varepsilon)=-\log\delta+\log\!\left(\frac{4c^2(n-1)}{n+1}\right)+o(1).
\]

## Assumptions and scope
The plane is Euclidean and oriented counterclockwise. The **outer-billiard map** \(T\) sends a point \(A\) outside the curve to \(B\) when the midpoint of \([A,B]\) lies on \(\gamma\), the segment is tangent there, and the chosen tangent orientation goes from \(A\) toward \(B\). Thus \(A=\gamma(t)-\ell \mathcal T(t)\), \(B=\gamma(t)+\ell\mathcal T(t)\), where \(\mathcal T\) is the unit positively oriented tangent and \(\ell>0\). For a strictly convex table the corresponding branch is a well-defined local area-preserving diffeomorphism at all points used here. The cycle points are away from the table.

The assumptions \(n\geq6\), \(0<\varepsilon<n^{-2}\) give \(0<\theta<\pi/2\), \(c>0\), and strictly positive speed and curvature of \(\gamma\). Let the radial-extremum tangencies be
\[
P_j=(1+\varepsilon)e^{2\pi i j/N},\qquad Q_j=(1-\varepsilon)e^{i(2j+1)\pi/N},\quad j\in\mathbb Z/N\mathbb Z.
\]
Write \(E_j\) for the intersection of the tangent lines at \(P_j,P_{j+2}\), and \(H_j\) for the analogous intersection at \(Q_j,Q_{j+2}\). Only the dynamics, its derivative, and eigenvalues at these explicitly identified cycles are classified; no claim is made about all other periodic points.

## Proof
**1. Strict convexity and tangent geometry.** Differentiate:
\[
\gamma'(t)=ie^{it}(1+n\varepsilon e^{iNt}),\qquad
\gamma''(t)=-e^{it}(1+n^2\varepsilon e^{iNt}).
\]
The signed curvature numerator satisfies
\[
[\gamma'(t),\gamma''(t)]=1+n^3\varepsilon^2+n(n+1)\varepsilon\cos Nt
\geq(1-n\varepsilon)(1-n^2\varepsilon)>0.
\]
Together with \(|\gamma'(t)|>0\) and the polar-angle derivative \(d\arg\gamma/dt>0\) for the stated range, this makes \(\gamma\) a strictly convex embedded closed curve. At an extremum of sign \(s\in\{+1,-1\}\), its radial distance, tangent speed, and curvature radius are
\[
R_s=1+s\varepsilon,\qquad v_s=1+sn\varepsilon,\qquad \rho_s=\frac{(1+sn\varepsilon)^2}{1+sn^2\varepsilon}.
\]
The tangent at an extremum is perpendicular to its radius. Elementary intersections of tangents to points at angular separation \(2\theta\) have center radius \(R_s/\cos\theta\) and half-chord tangent length \(\ell_s=R_s\tan\theta\). The outer map sends each such intersection to the one rotated by \(2\theta\): \(T(E_j)=E_{j+2}\) and \(T(H_j)=H_{j+2}\). The label advance by two has minimal period \(k=N/\gcd(N,2)\), with \(\gcd(N,2)\) cycles for either sign. Distinctness follows from their distinct polar angles.

**2. Exact derivative.** Work in the positively oriented orthonormal tangent/normal coordinates \((\mathcal T,\mathcal N)\) at an extremum. Differentiating \(A=\gamma(t)-\ell\mathcal T(t)\) and \(B=\gamma(t)+\ell\mathcal T(t)\) gives
\[
\delta A=(v\delta t-\delta\ell)\mathcal T-\ell(v/\rho)\delta t\,\mathcal N,
\quad
\delta B=(v\delta t+\delta\ell)\mathcal T+\ell(v/\rho)\delta t\,\mathcal N.
\]
Eliminating \(\delta t\) and \(\delta\ell\), the one-step Jacobian in this common fixed basis is
\[
S_s=\begin{pmatrix}-1&-2\rho_s/\ell_s\\0&-1\end{pmatrix},\qquad \det S_s=1.
\]
The next extremal tangent basis is rotated by \(2\theta\), so, after identifying consecutive frames by counter-rotation, the constant co-rotating Jacobian is \(K_s=R(-2\theta)S_s\). Its trace is
\[
\operatorname{tr}K_s=-2\cos(2\theta)+\frac{2\rho_s}{\ell_s}\sin(2\theta)
=2+4c^2\left(\frac{\rho_s}{R_s}-1\right).
\]
Direct factorization gives
\[
(1+sn\varepsilon)^2-(1+s\varepsilon)(1+sn^2\varepsilon)
=-s(n-1)^2\varepsilon,
\]
which yields the two stated rational traces. The physical-frame return derivative is conjugate to \(K_s^k\): because \(R(2k\theta)=I\), its eigenvalues agree with those of \(K_s^k\).

**3. Global elliptic/hyperbolic dichotomy.** Since \(\varepsilon<n^{-2}\), the denominator in each trace is positive. For the maximum family, \(\tau_+<2\), and its limiting decrement at \(\varepsilon=n^{-2}\) is \(2c^2N^2/(n^2+1)<2\), proving \(0<\tau_+<2\). The minimum family has \(\tau_->2\). Unit determinant gives the displayed phase and exponent and hence the return multipliers. Differentiation shows that \(\varepsilon/[(1+s\varepsilon)(1+sn^2\varepsilon)]\) is strictly increasing: its derivative is
\[
\frac{1-n^2\varepsilon^2}{(1+s\varepsilon)^2(1+sn^2\varepsilon)^2}>0.
\]
Therefore \(\phi\) and \(\eta\) are strictly increasing.

**4. Exhaustive scalar-monodromy resonances.** The phase \(\phi\) increases continuously from zero to \(\phi_*<\pi/2\). Since \(K_+\) has distinct unit-circle eigenvalues for \(\varepsilon>0\), \(K_+^k\) is a scalar \(\pm I\) exactly when \(k\phi=j\pi\) for some positive integer \(j\); this is possible precisely when \(j\pi/k<\phi_*\). The number of positive integers strictly below \(k\phi_*/\pi\) is \(R_n\). The resonance equation \(1-\tau_+/2=A_j\) is
\[
A_jn^2\varepsilon^2-\bigl(2c^2N^2-(1+n^2)A_j\bigr)\varepsilon+A_j=0.
\]
The unique root in \((0,n^{-2})\), guaranteed by monotonicity, is the smaller quadratic root, here written in rationalized form \(2A_j/(B_j+\sqrt{B_j^2-4n^2A_j^2})\). Both numerator and radicand are positive at admissible resonances. The other root lies outside the allowed range. Ordering of roots follows from strict increase of \(\phi\). This proves that the finite list is complete **within these two named orbit families**.

**5. Boundary laws.** The small-\(\varepsilon\) trace splitting is \(2-\tau_+=4c^2N^2\varepsilon+O(\varepsilon^2)\) and \(\tau_--2=4c^2N^2\varepsilon+O(\varepsilon^2)\); expansion of \(\cos\phi\) and \(\cosh\eta\) gives the square-root laws. At \(\delta=1-n^2\varepsilon\downarrow0\), \(\tau_--2\sim 4c^2N/(n+1)\,\delta^{-1}\). The identity \(\operatorname{arcosh}(u)=\log(2u)+o(1)\) as \(u\to\infty\) yields \(\eta=\log(\tau_-)+o(1)=-\log\delta+\log(4c^2N/(n+1))+o(1)\).

## Verification
The standalone standard-Python program `checker.py` reconstructs the actual outer-billiard step by solving the tangent equation with Newton iteration and compares finite-difference Jacobians in co-rotating frames to the closed traces and area-preserving determinant. It checks both cycle families for \(6\le n\le18\) at four admissible perturbations, comprising 104 comparisons; it also checks 2,070 algebraic resonance equations for \(6\le n<110\). Running `python3 checker.py` from the package directory prints a single `PASS` line. The derivation above establishes the infinitely many-parameter theorem; the code alone is neither an exhaustive check nor a substitute for proof.

## Relationship to prior work
Bialy, Mironov and Shalom (2018 preprint; journal 2021) introduce exactly this harmonic family and identify the symmetric periodic tangent intersections, illustrated as elliptic islands and hyperbolic periodic points (their Section 4). Their Section 2 constructs invariant curves with standard-shift dynamics. Their full text does not state the rational Floquet traces, primitive-period multipliers, scalar-monodromy parameter census, or the two exact boundary laws established here. These are not claims to invent the orbit families or generic area-preserving eigenvalue theory.

Ramírez-Ros (2006), Sections 1–5, develops Melnikov criteria for destruction of resonant invariant curves of perturbations of circular classical and dual billiards. That work studies resonance breakup of invariant curves, rather than this named finite collection of tangent-intersection periodic orbits and their exact all-parameter monodromy spectra. Nevertheless, classical outer-billiard Jacobian formulas and other unindexed discussions remain potential equivalence sources. No general novelty guarantee follows from an unsuccessful database search.

## Limitations
The theorem covers the two explicit symmetric families only, for integers \(n\ge6\) and strict convexity range \(0<\varepsilon<n^{-2}\). It does not count all periodic orbits, prove nonlinear KAM stability at nonresonant elliptic points, establish nonlinear bifurcations at scalar monodromy, or describe dynamics at or beyond the nonconvex boundary. The phase resonances are not asserted to correspond one-to-one to island creation or loss. Publication-priority comparisons cannot exclude equivalent formulas hidden in unindexed literature, and independent mathematical validation has not been performed.

## References
1. M. Bialy, A. E. Mironov, L. Shalom, *Outer billiards with the dynamics of a standard shift on a finite number of invariant curves*, arXiv:1811.04981v1, first public 2018-11-12; *Experimental Mathematics* 30 (2021), 469–474. https://arxiv.org/abs/1811.04981
2. R. Ramírez-Ros, *Break-up of resonant invariant curves in billiards and dual billiards associated to perturbed circular tables*, *Physica D* 214 (2006), 78–87, DOI 10.1016/j.physd.2005.12.007; open author PDF https://web.mat.upc.edu/rafael.ramirez/res/pdf/physicad06.pdf
