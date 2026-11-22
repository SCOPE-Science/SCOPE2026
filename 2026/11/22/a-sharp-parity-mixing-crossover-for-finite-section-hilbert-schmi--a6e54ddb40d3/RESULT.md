# A sharp parity-mixing crossover for finite-section Hilbert–Schmidt quasicentral energy

## Finding

Let \(S e_j=e_{j+1}\) be the unilateral shift on \(H=\ell^2(\mathbb N_0)\), \(P_N\) the orthogonal projection onto the first \(N\) coordinates, and \(\|\cdot\|_2\) the Hilbert–Schmidt norm. For each even \(N\ge2\) and \(\varepsilon\ge0\) set
\[
\mathcal E_N(\varepsilon)=\min_{0\le R\le I,\ R=P_NRP_N,\ Re_0=e_0}\bigl(\|[S^2,R]\|_2^2+\varepsilon^2\|[S,R]\|_2^2\bigr).
\]
The minimizer is unique, positive and diagonal. For every fixed \(c\ge0\),
\[
\boxed{\lim_{N\to\infty\atop N\text{ even}}N\mathcal E_N(c/N)
=\Phi(c)=\frac{4c\coth c}{1+c\coth c}},\qquad \Phi(0):=2.
\]
The crossover function increases strictly from \(2\) to \(4\). In the more general simultaneous limit with \(\varepsilon_N\ge0\), \(\varepsilon_N\to0\), the normalized energy tends to \(2\) if \(N\varepsilon_N\to0\), and to \(4\) if \(N\varepsilon_N\to\infty\). At zero coupling the *finite* exact identity is \(\mathcal E_N(0)=2/N\).

The profile is also determined. With \(N=2L\), the even and odd diagonal entries \(d_{2k}\) and \(d_{2k+1}\), interpolated linearly at scaled positions \(t=k/L\), converge uniformly to
\[
 x_c(t)=u_c(t)+v_c(t),\quad y_c(t)=u_c(t)-v_c(t),\quad
 u_c(t)=\frac{\kappa}{1+\kappa}(1-t),\quad
 v_c(t)=\frac{\sinh(c(1-t))}{(1+\kappa)\sinh c},\quad\kappa=c\coth c.
\]
For \(c=0\), interpret \(\kappa=1\) and \(v_0(t)=(1-t)/2\), giving \(x_0(t)=1-t\) and \(y_0(t)=0\).

## Assumptions and scope

The operator tuple consists of *separate* commutators with \(S^2\) and \(\varepsilon S\) and their **squared-norm sum**; it is not the commutator with \(S^2+\varepsilon S\). The cutoff is supported inside the first \(N\) coordinate vectors and fixes \(e_0\). The asymptotic theorem is for even cutoffs, nonnegative real coupling and the two-generator Hilbert–Schmidt quadratic energy only. All stated minima exist because the feasible set is compact in its finite-dimensional support. The diagonal minimum need not be a projection.

## Proof

**1. Reduction to the scalar conductor network.** Let \(U_\theta e_j=e^{ij\theta}e_j\). Since \(U_\theta^*S^m U_\theta=e^{-im\theta}S^m\), conjugation by \(U_\theta\) preserves each commutator norm, the finite support, positivity, and the boundary condition. Integrating \(U_\theta R U_\theta^*\) over the circle and using convexity gives a diagonal competitor with no larger energy. If a finite-rank operator \(K\) commutes with \(S^2\), then \(K S^{2n}e_r=S^{2n}Ke_r\) for \(r=0,1\). Compactness of \(K\), applied to the weakly null sequences \(S^{2n}e_r\), forces \(Ke_r=0\), hence \(K=0\). Therefore the squared-commutator quadratic form is strictly convex on finite-rank operators; averaging can preserve the minimum only if the original minimizer already equals its diagonal average. This establishes uniqueness and diagonality even when \(\varepsilon=0\).

For \(D=\operatorname{diag}(d_0,\ldots,d_{N-1},0,\ldots)\), \(d_0=1\), the exact energy equals
\[
 \sum_{j=0}^{N-1}(d_j-d_{j+2})^2+\varepsilon^2\sum_{j=0}^{N-1}(d_j-d_{j+1})^2,\quad d_j=0\ (j\ge N).
\]
The unconstrained harmonic minimizer on this finite network has values between zero and one: if a free vertex attains a maximum strictly above one, or a minimum below zero, the discrete harmonic equation and connectivity to the grounded terminal vertices force the same extremum at a boundary, contradiction. The argument works separately on each parity component when \(\varepsilon=0\). Thus it is feasible for \(0\le D\le I\), so the scalar unconstrained and operator-constrained minima coincide.

**2. Two-chain representation.** Write \(N=2L\), \(x_k=d_{2k}\), \(y_k=d_{2k+1}\), and set \(x_L=y_L=0\). Then \(x_0=1\), while \(y_0\) is free, and the exact energy is
\[
 \mathcal F_{L,\varepsilon}(x,y)=\sum_{k=0}^{L-1}\bigl[(x_{k+1}-x_k)^2+(y_{k+1}-y_k)^2\bigr]+\varepsilon^2\sum_{k=0}^{L-1}\bigl[(y_k-x_k)^2+(x_{k+1}-y_k)^2\bigr].
\]
At \(\varepsilon=0\), minimization gives \(x_k=1-k/L\), \(y_k=0\), and \(\mathcal E_{2L}(0)=1/L=2/N\).

**3. Continuum limit with the critical scaling.** Fix \(c\ge0\), set \(\varepsilon=c/(2L)\), and let \(X_L,Y_L\) denote piecewise-linear interpolants on \([0,1]\) through the two sequences. A linear trial function yields a uniform bound on \(2L\mathcal F_{L,\varepsilon}\). Its nearest-neighbor-two energy implies uniform \(H^1(0,1)\) bounds; the scalar values lie in \([0,1]\). By one-dimensional compact embedding, subsequences converge uniformly and weakly in \(H^1\) to \(x,y\) with \(x(0)=1\), \(x(1)=y(1)=0\), and \(0\le x,y\le1\). Exactly,
\[
2L\sum(\Delta x_k)^2=2\int_0^1|X_L'|^2,\quad
2L\sum(\Delta y_k)^2=2\int_0^1|Y_L'|^2.
\]
Uniform convergence makes each weak first-neighbor term converge to the Riemann integral; the critical scaling gives
\[
 \liminf_{L\to\infty}(2L)\mathcal F_{L,c/(2L)}\ge
 \mathcal F_c(x,y):=2\int_0^1(x'^2+y'^2)\,dt+c^2\int_0^1(x-y)^2\,dt.
\]
Conversely sample any continuously differentiable admissible pair at the grid points (with the free value \(y_0\)) to obtain matching energy in the limit. The continuum minimum therefore equals the limit of the finite minima, and uniqueness of the continuum minimizer implies convergence of the whole sequence of interpolants, not merely subsequences.

**4. Explicit continuum solution.** Put \(u=(x+y)/2\), \(v=(x-y)/2\), so \(u(1)=v(1)=0\), \(u(0)+v(0)=1\), and
\[
 \mathcal F_c=4\int_0^1(u'^2+v'^2+c^2v^2)\,dt.
\]
For prescribed initial values \(u(0)=a\), \(v(0)=b\), the unique minimizing profiles are \(u(t)=a(1-t)\) and \(v(t)=b\sinh(c(1-t))/\sinh c\) for \(c>0\); at \(c=0\) both are linear. Integration by parts gives the minimal energy \(4[a^2+\kappa b^2]\), where \(\kappa=c\coth c\) (continuously \(\kappa(0)=1\)). Minimizing over \(a+b=1\) gives \(a=\kappa/(1+\kappa)\), \(b=1/(1+\kappa)\), and \(4\kappa/(1+\kappa)\). The profiles satisfy \(0\le y\le x\le1\): \(\kappa(1-t)\ge\sinh(c(1-t))/\sinh c\), because \(\sinh(ct)/t\) is increasing and \(\kappa\ge1\). Strict monotonicity of \(c\coth c\) follows from \(\sinh c\cosh c>c\) for \(c>0\).

**5. Subcritical and supercritical coupling.** The minimum is nondecreasing in \(\varepsilon\). If \(N\varepsilon_N\to0\), compare for each fixed \(c>0\) to the value at \(c/N\) from above, and to the zero-coupling value from below; sending \(c\downarrow0\) gives normalized limit two. If \(N\varepsilon_N\to\infty\), the lower bound dominates each fixed \(c/N\), hence \(\liminf N\mathcal E_N\ge\sup_c\Phi(c)=4\). The trial diagonal \(d_j=1-j/N\) gives the exact bound
\[
 N\mathcal E_N(\varepsilon_N)\le4-\frac3N+\varepsilon_N^2,
\]
which tends to four when \(\varepsilon_N\to0\). This proves the second limit without requiring a uniform finite-size crossover estimate.

## Verification

The self-contained `verify.py` constructs and solves the exact finite Dirichlet network and checks the minimizer's Euler equations, positivity, the zero-coupling identity, the continuum profile, and convergence to \(\Phi(c)\) at sampled parameters. It requires Python 3 and NumPy; run `python verify.py` in the directory containing this file. The checked numeric instances cannot certify the limit or originality, which follow respectively from the preceding proof and the literature comparisons below.

## Relationship to prior work

Liu and Zhao (2026, arXiv:2611.15604) prove a qualitative vanishing result for Hilbert–Schmidt quasicentral modulus of a single almost-normal operator. The present finite-section, two-generator **sum-of-squares** energy is not the asymptotic quasicentral modulus and its critical finite cutoff is not implied by that vanishing theorem. Voiculescu (2022, arXiv:2107.11924) identifies quasicentral moduli of group shift tuples with discrete condenser capacities, including the conditional-expectation reduction to diagonal functions; this is an acknowledged structural precursor. Voiculescu (2024, DOI:10.4171/QT/208) gives general condenser properties and a bilateral *single-shift* example, not the weak-coupling \((S^2,\varepsilon S)\) critical scaling. Classical ladder-network resistance techniques may provide equivalent routes to the continuum formula. The claim is specifically the sharp operator finite-section crossover, explicit parity profiles and complete scale separation for this constrained two-generator energy, not the novelty of elementary continuum Dirichlet minimization in isolation.

## Limitations

The operator bound is for the stated supported positive contractions fixing one vector, not for arbitrary unconstrained approximants. This is a restricted finite-section energy; no claim is made that the standard infinite-cutoff quasicentral modulus is nonzero. The result uses the Hilbert–Schmidt quadratic sum and even cutoff size, and does not classify arbitrary tuples or norms. An older unindexed exact weak-coupling ladder calculation may overlap with the continuum scalar formula; the primary operator-tuple statement was not found in accessible sources. Independent mathematical validation has not been performed.

## References

1. Shiqi Liu and Hongyin Zhao, *Quasicentral modulus for almost normal operators*, arXiv:2611.15604v1 (first public 2026-11-11), https://arxiv.org/html/2611.15604v1.
2. Dan-Virgil Voiculescu, *Capacity and the quasicentral modulus*, arXiv:2107.11924v4 (2022), https://arxiv.org/pdf/2107.11924.
3. Dan-Virgil Voiculescu, *The condenser quasicentral modulus*, Quantum Topology 15 (2024), 419–448, DOI:10.4171/QT/208, https://ems.press/content/serial-article-files/48871?nt=1.
