# Critical cubic drift and sharp relaxation in a three-dimensional sine-delay map

## Finding
For real \(0<s<r<1\) and the three-dimensional map
\[
F_{r,s,b}(x,y,z)=(y,\sin z,rx+by-s\sin z),
\]
write \(b_*=1-r+s\), \(\varepsilon=b-b_*\), and \(D=2+r+s\). For each fixed \((r,s)\) there is \(\varepsilon_0>0\) such that all the following hold for \(|\varepsilon|<\varepsilon_0\).

If \(\varepsilon<0\), the origin is the only real fixed point and is a hyperbolic sink. At \(\varepsilon=0\) the origin remains locally asymptotically stable, but its generic convergence is algebraic: outside a local two-dimensional strong-stable manifold, every sufficiently small nonzero initial state has all coordinates eventually of the same sign and
\[
\lim_{n\to\infty}n x_n^2=\lim_{n\to\infty}n y_n^2=\lim_{n\to\infty}n z_n^2=3(2+r+s).
\]
On the strong-stable manifold convergence to zero is exponential. For \(0<\varepsilon<\varepsilon_0\), the map has exactly three real fixed points: a saddle origin with one unstable direction and two symmetry-related hyperbolic sinks
\[
P_\pm=(\sin z_\pm,\sin z_\pm,z_\pm),\qquad
z_\pm=\pm\sqrt{6\varepsilon}+O(\varepsilon^{3/2}).
\]
Their critical-direction multipliers, and that of the origin, are
\[
\lambda_\pm=1-\frac{2\varepsilon}{D}+O(\varepsilon^2),\qquad
\lambda_0=1+\frac{\varepsilon}{D}+O(\varepsilon^2).
\]
For \((r,s,b_*)=(1/2,1/4,3/4)\) the critical constant is \(33/4\).

## Assumptions and scope
The map is the displayed real three-dimensional iteration, sine is in radians, and all asymptotic limits refer to integer time \(n\to\infty\). The two-dimensional strong-stable manifold is local and passes through the critical origin. The convergence claims concern sufficiently small initial conditions, not arbitrary states in \(\mathbb R^3\). The number of real fixed points, by contrast, is global for the specified small detuning. The detuning radius and local neighborhood need not be uniform as \((r,s)\) approaches the boundary of the parameter wedge.

## Proof
**Complete fixed-point count.** Fixed points satisfy \(x=y=\sin z\) and \(z=(r+b-s)\sin z=(1+\varepsilon)\sin z\). Choose \(\varepsilon_0\) so that \(0<1+\varepsilon<\pi\). Every fixed point has \(|z|\le1+\varepsilon<\pi\); on \((0,\pi)\), \(\sin z/z\) strictly decreases from one to zero (its derivative has numerator \(z\cos z-\sin z<0\)). This yields exactly one root for \(\varepsilon\le0\) and three for \(\varepsilon>0\). Expanding the fixed-point equation gives \(z_\pm^2=6\varepsilon+O(\varepsilon^2)\).

**Linear and nonlinear critical modes.** At zero, the characteristic polynomial is
\[
p_\varepsilon(\lambda)=\lambda^3+s\lambda^2-(1-r+s+\varepsilon)\lambda-r.
\]
For \(\varepsilon=0\) it factors as
\[
(\lambda-1)(\lambda^2+(1+s)\lambda+r).
\]
The quadratic is strictly Schur-stable by \(r<1\), \(r-s>0\), and \(2+r+s>0\). The remaining unit multiplier is simple, with right eigenvector \(q=(1,1,1)\) and normalized left eigenvector \(p=(r,1+s,1)/D\). Implicit differentiation of the characteristic polynomial yields \(\lambda_0'(0)=1/D\).

Define \(W=z+rx+(1+s)y\). At the critical parameter direct substitution produces the **exact**, non-perturbative identity
\[
W(F_{r,s,b_*}(x,y,z))-W(x,y,z)=\sin z-z.
\]
In normalized center coordinate \(u=W/D=p\cdot(x,y,z)\), the odd symmetry of the map permits a symmetric \(C^5\) local center manifold \(X(u)=uq+O(u^3)\) with \(z(u)=u+O(u^3)\). The exact identity gives its scalar return map
\[
u_{n+1}=u_n-\frac{u_n^3}{6D}+O(u_n^5).
\]
The cubic coefficient is negative for every allowed pair. For all sufficiently small nonzero center points, \(u_n\) eventually preserves its sign and decreases in magnitude to zero; moreover,
\[
\frac1{u_{n+1}^2}-\frac1{u_n^2}=\frac1{3D}+O(u_n^2).
\]
Consequently \(n u_n^2\to3D\), and all three physical coordinates are \(u_n(1+O(u_n^2))\). Standard discrete center-manifold stability transfer and local strong-stable foliation give exponential tracking by a center orbit for every sufficiently small initial point. The single strong-stable leaf over the origin is two-dimensional and decays exponentially; every other leaf tracks a nonzero center orbit and has the same algebraic limit. This also proves local asymptotic stability at the nonhyperbolic threshold.

At a nonzero equilibrium the characteristic polynomial becomes
\[
P(\lambda;z,\varepsilon)=\lambda^3+s(\cos z)\lambda^2-(b_*+\varepsilon)(\cos z)\lambda-r\cos z.
\]
As \(\cos z_\pm=1-3\varepsilon+O(\varepsilon^2)\), one has \(P(1;z_\pm,\varepsilon)=2\varepsilon+O(\varepsilon^2)\) and \(\partial_\lambda P(1;0,0)=D\). Thus the multiplier near one is \(1-2\varepsilon/D+O(\varepsilon^2)\). The other two remain strictly Schur-stable by continuity; hence both new fixed points attract locally. The unit eigenvalue at the origin moves above one for positive detuning and below one for negative detuning, completing the three regimes.

## Verification
The accompanying `checker.py` is standalone Python 3 using only the standard library. It reproduces the exact characteristic factorization, left-right eigenvector and balance identities at rational parameters, checks Schur inequalities, computes finite-iteration critical limits, and independently computes a newborn equilibrium and its near-unit multiplier. Numerical tests are consistency checks rather than proofs of the quantified theorem. Run `python3 checker.py`.

## Relationship to prior work
Mammeri (2017) analyzed a fixed-sine-amplitude predecessor through boundedness, linear stability and bifurcation plots. Rajagopal et al. (2023) studied the more general sine map \((y,\sin z,\alpha+\beta x+\gamma y-\delta\sin z+\mu z)\), which contains the displayed family at \((\alpha,\mu)=(0,0)\). Almatroud et al. (2024) explicitly studied this symmetric zero-feedback sine map, emphasizing fixed-point stability, simulations and control. Their inspected results do not state the cubic center drift, strong-stable exception, exact critical coefficient, or the joint pitchfork theorem. The analysis uses standard center-manifold methods, whose general existence statements do not supply these object-specific coefficients. Unindexed equivalent literature remains possible.

## Limitations
The theorem is local in initial conditions and near the critical parameter; it does not claim global convergence, a complete global basin decomposition, chaos or any cryptographic property. The published systems admit wider parameter ranges not treated here. The finite checker cannot certify an infinite-time theorem. Independent mathematical audit has not been performed.

## References
1. M. Mammeri, *Symmetry and Periodic-Chaos in 3-D Sinusoid Discrete Maps*, Bulletin of Mathematical Analysis and Applications 9(1) (2017), 1–8. Public full text: https://www.researchgate.net/publication/317278288_SYMMETRY_AND_PERIODIC-CHAOS_IN_3-D_SINUSOID_DISCRETE_MAPS.
2. K. Rajagopal, S. Kanagaraj, C. Volos, A. Karthikeyan, *Influence of Parametric Symmetry on the Dynamics of 3D Sinusoidal Discrete Systems*, Symmetry 15 (2023), 780, https://doi.org/10.3390/sym15040780 (first published March 23, 2023).
3. O. A. Almatroud et al., *Multistability, Chaos, and Synchronization in Novel Symmetric Difference Equation*, Symmetry 16 (2024), 1093, https://doi.org/10.3390/sym16081093 (published August 22, 2024).
4. Y. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, third edition, Springer (2004): standard local center-manifold and invariant-foliation methods.
