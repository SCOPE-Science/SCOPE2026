# Fractional-memory stability staircase and inverse-square accumulation in the sine–cubic map

## Finding
For the commensurate Caputo-delta sinusoidal difference model below, the **complete number of linearly asymptotically stable real equilibria** is
\[
N_\alpha(c)=2\max\!\left\{0,\left\lceil\frac{D_\alpha}{2\pi\sqrt{c-1}}-\frac{\arctan\sqrt{c-1}}{\pi}\right\rceil\right\},\qquad c>1,\quad 0<\alpha\le1.
\]
Here \(D_\alpha\) is the unique solution \(D>1/4\) of
\[
\sqrt D=\left[2\cos\!\left(\frac{\arccos(-1/(2\sqrt D))-\pi}{2-\alpha}\right)\right]^\alpha.
\]
In particular \(D_1=1\), while \(D_\alpha>1\) for every \(0<\alpha<1\). As \(c\downarrow1\) with the order fixed,
\[
N_\alpha(c)=\frac{D_\alpha}{\pi\sqrt{c-1}}+O_\alpha(1).
\]
For each nonnegative integer \(m\), one symmetric equilibrium pair crosses the strict spectral-stability boundary at a unique \(c_m(\alpha)>1\). As \(m\to\infty\),
\[
c_m(\alpha)-1\sim\frac{D_\alpha^2}{4\pi^2m^2}.
\]
Thus the distinct spectral transitions form an inverse-square staircase accumulating at the degenerate parameter \(c=1\). At order \(\alpha=1/2\), \(D_\alpha=1.4476229868549\ldots\); at \(c=1.7\) there is one linearly stable pair, whereas the integer-order map has none. The claims concern linearized infinite-memory stability, not nonlinear basins or periodic-orbit bifurcations.

## Assumptions and scope
Let \(c>1\), \(0<\alpha\le1\), and let the state coordinates be real. Use the Caputo-like forward delta difference model of Liu, Tang and Hong (2022), with the same order in each coordinate and starting value at the origin of discrete time:
\[
{}^C\!\Delta_0^\alpha x(t)=\sin\bigl(\pi y(t+\alpha-1)\bigr)-x(t+\alpha-1),\qquad
{}^C\!\Delta_0^\alpha y(t)=\bigl[c(1-x(t+\alpha-1)^2)-1\bigr]y(t+\alpha-1).
\]
For \(0<\alpha<1\), the equivalent Volterra recurrence is \(u_n=u_0+\sum_{j=0}^{n-1}w_{n-1-j}f(u_j)\), where \(w_k=\Gamma(k+\alpha)/[\Gamma(\alpha)\Gamma(k+1)]\). At \(\alpha=1\), it is the ordinary integer-order map \(u_{n+1}=u_n+f(u_n)\). A stationary solution is *linearly asymptotically stable* if every solution of its linearized fractional Volterra system tends to zero. The strict boundary is excluded; the theorem does not classify nonlinear stability at nonhyperbolic equality cases.

## Proof
**1. Exact stationary-point census.** Put \(h=\sqrt{c-1}\), \(r=h/\sqrt{1+h^2}\), and \(\delta=\arctan h/\pi\in(0,1/2)\). The stationary equations are \(x=\sin(\pi y)\) and \([c(1-x^2)-1]y=0\). The origin is one solution. If \(y\ne0\), then \(x=\pm r\). Solving the sine equation on *all* real branches yields infinitely many isolated equilibria. Exactly the branches with positive Jacobian determinant occur in the symmetric pairs \(\pm P_m\), where
\[
P_m=\bigl(r,\,(-1)^m(m+\delta)\bigr),\qquad m=0,1,2,\ldots.
\]
Every remaining nonzero equilibrium has negative Jacobian determinant. The linearization at the origin has a positive eigenvalue \(c-1\); it is not linearly stable for \(c>1\). As a boundary observation, at \(c=1\) the stationary set is exactly \(\{(0,k):k\in\mathbb Z\}\), with a zero linearized eigenvalue at each point.

**2. Reduction to a scalar determinant.** At any nonzero equilibrium \((x,y)\), the Jacobian of the fractional vector field is
\[
M=\begin{pmatrix}-1&\pi\cos(\pi y)\\-2cxy&0\end{pmatrix},\quad
\operatorname{tr}M=-1,\quad\det M=2\pi cxy\cos(\pi y).
\]
At each \(\pm P_m\), \(\cos(\pi y)=(-1)^m/\sqrt c\), hence \(\det M=D_m=2\pi h(m+\delta)>0\). Both eigenvalues satisfy \(\mu^2+\mu+D_m=0\). A negative determinant instead produces a strictly positive real eigenvalue \(\mu\), which rules out linear asymptotic stability for any \(\alpha\in(0,1]\).

**3. Fractional spectral region and its unique crossing.** For a scalar eigenmode \(v_n\) of eigenvalue \(\mu\), the generating function of the linearized Volterra equation is
\[
\sum_{n\ge0}v_nz^n=\frac{v_0(1-z)^{\alpha-1}}{(1-z)^\alpha-\mu z}.
\]
The established necessary-and-sufficient fractional-difference spectral criterion gives stability precisely for eigenvalues inside the open region with radial boundary
\[
|\mu|<\left[2\cos\left(\frac{|\arg\mu|-\pi}{2-\alpha}\right)\right]^\alpha,
\qquad |\arg\mu|>\frac{\alpha\pi}{2}.
\]
The criterion also follows by setting \(z=e^{i\omega}\) in the denominator and tracking the component containing small negative real \(\mu\). For \(0<D\le1/4\), the two roots of \(\mu^2+\mu+D=0\) lie in \((-1,0)\) (coinciding at \(D=1/4\)), and are stable for all orders. For \(D>1/4\), they have \(|\mu|=\sqrt D\) and phase magnitude \(\phi(D)=\arccos(-1/(2\sqrt D))\in(\pi/2,\pi)\). The angle restriction always holds. As \(D\) increases, \(\sqrt D\) strictly increases while the radial admissible bound strictly decreases, yielding the unique crossing \(D=D_\alpha\) specified above. Thus **strict linear asymptotic stability holds exactly when \(0<D_m<D_\alpha\)**. At \(\alpha=1\), direct substitution gives \(D_1=1\); at \(0<\alpha<1\), evaluation at \(D=1\) gives a strictly larger permissible radius, so \(D_\alpha>1\).

**4. Counts and accumulation.** There are exactly two equilibria for each integer \(m\ge0\) satisfying \(2\pi h(m+\delta)<D_\alpha\). The number of such integers is \(\max\{0,\lceil D_\alpha/(2\pi h)-\delta\rceil\}\), proving the exact formula including strict equality cases. Since \(\delta=O(h)\), the stated \(1/h\) asymptotic follows. The monotone function \(2\pi h(m+\arctan h/\pi)\) grows from zero to infinity as \(h\) grows, so it equals \(D_\alpha\) at one and only one \(h_m>0\), with \(c_m=1+h_m^2\). For \(m\to\infty\), \(h_m\sim D_\alpha/(2\pi m)\), proving the inverse-square law. In particular, the first-pair threshold solves \(2t\tan t=D_\alpha\), \(c_0=1+\tan^2t\), with \(t\in(0,\pi/2)\). Its strict increase with \(D_\alpha\) establishes an open fractional-only stability interval between the integer and fractional first-pair thresholds.

## Verification
The standalone `checker.py` replays scalar spectral bounds, direct stationary equations, Jacobian determinants, integer counts, the order-one versus half-order example, and the inverse-square scaling for large integer indices. It uses only Python's standard library. It prints `PASS` after completing these checks. This computational test is supplementary: the proof above handles all real parameters and all integer branches without finite extrapolation.

## Relationship to prior work
The 2013 paper of Bi, Zhang, Xiang and Wang introduced the integer-order sine–cubic map and analyzed its principal symmetric equilibria and local transitions. Liu, Tang and Hong (2022) introduced its Caputo-delta fractional version, gave a sufficient eigenvalue stability region, and focused on the principal equilibrium pair and numerical bifurcations. The present result is not a claim to discover either the map or the general fractional spectral criterion. It establishes the full real branch count, an exact **order-dependent** stationary spectral-stability census, and an inverse-square accumulation law not supplied by those works. Busłowicz and Ruszewski (2013) prove a general necessary-and-sufficient eigenvalue region for fractional discrete-time linear systems; their theorem is applied here to the specific nonlinear map's full equilibrium family.

## Limitations
The word *stable* refers throughout to the infinite-memory **linearized** equation. Equality at \(D_m=D_\alpha\) is not called stable; nonlinear attraction, resonance, bifurcation types, basin sizes and incommensurate fractional orders are not established. The large count near \(c=1\) comes from branches at increasing \(|y|\), and does not imply infinitely many sinks in a bounded phase-space window for a fixed \(c>1\). The original integer-order map dates to 2013; the fractional-order model used for the claimed order-dependent result was publicly introduced in 2022.

## References
1. X. Liu, D. Tang and L. Hong, *A Fractional-Order Sinusoidal Discrete Map*, Entropy 24 (2022), 320, first published 2022-02-23, https://doi.org/10.3390/e24030320 . See Sections 2–4, especially (7), (10), and the equilibrium discussion.
2. C. Bi, Q. Zhang, Y. Xiang and J.-M. Wang, *Bifurcation and attractor of two-dimensional sinusoidal discrete map*, Acta Phys. Sin. 62 (2013), 240503, https://doi.org/10.7498/aps.62.240503 . See Equations (1)–(9) and Section 2.
3. M. Busłowicz and A. Ruszewski, *Necessary and sufficient conditions for stability of fractional discrete-time linear state-space systems*, Bull. Pol. Acad. Sci. Tech. Sci. 61 (2013), 779–786, https://doi.org/10.2478/bpasts-2013-0084 . See Theorem 4 and the boundary formula (42).
