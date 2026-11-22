# A critical dimension for spatial collisions and hidden coherence in reset quantum walks

## Finding
For each integer \(d\ge1\), consider an origin-reset continuous-time nearest-neighbor quantum walk on \(\mathbb Z^d\) with hopping \(\kappa>0\) and independent complete Poisson resets at rate \(r>0\). Let \(\rho_r\) be its stationary ensemble density operator, \(p_{\mathbf n}(r)=\langle\mathbf n|\rho_r|\mathbf n\rangle\), and define the spatial collision probability and full quantum purity
\[
Q_d(r)=\sum_{\mathbf n\in\mathbb Z^d}p_{\mathbf n}(r)^2,
\qquad P_d(r)=\operatorname{Tr}(\rho_r^2).
\]
Then **the normalized weak-reset spatial collision coefficient is finite exactly in dimensions at least three**:
\[
\lim_{r\downarrow0}\frac{Q_d(r)}{r^2}
=\begin{cases}\infty,&d=1,2,\\
C_d\in(0,\infty),&d\ge3,
\end{cases}
\]
where the explicit nonnegative two-time integral
\[
C_d=\int_0^\infty\!\int_0^\infty
\left(\sum_{n\in\mathbb Z}J_n(2\kappa t)^2J_n(2\kappa s)^2\right)^d\,dt\,ds
\]
is finite for every integer \(d\ge3\). The one-dimensional case has the additional *exact* identity
\[
Q_1(r)=\frac{r}{\sqrt{r^2+16\kappa^2}}.
\]
At the critical dimension two, for all sufficiently small \(r/\kappa\), there are positive constants \(c,C\), independent of \(r\) and \(\kappa\), such that
\[
c\frac{r^2}{\kappa^2}\log\frac{\kappa}{r}
\le Q_2(r)\le
C\frac{r^2}{\kappa^2}\left(\log\frac{\kappa}{r}\right)^4.
\]
No exact two-dimensional logarithmic coefficient is asserted.

The spatial collision statistic does not exhaust stationary quantum coherence: \(P_d(r)>Q_d(r)\) strictly for all \(d\ge1\), \(r,\kappa>0\). In dimension one the gap has the exact ratio
\[
\frac{P_1(r)}{Q_1(r)}=\frac2\pi K\!\left(\frac{4\kappa}{\sqrt{r^2+16\kappa^2}}\right)
\sim\frac2\pi\log\frac{16\kappa}{r},
\]
where \(K(k)=\int_0^{\pi/2}(1-k^2\sin^2\theta)^{-1/2}\,d\theta\). In every fixed dimension \(d\ge3\), the ratio diverges faster:
\[
\frac{P_d(r)}{Q_d(r)}\sim \frac{M_d}{C_dr},\qquad
M_d=\int_0^\infty J_0(2\kappa t)^{2d}\,dt\in(0,\infty).
\]
The full-purity formula and its weak-reset asymptotic are prior results; the findings here concern the spatial collision coefficient and its contrast with that known purity.

## Assumptions and scope
The Hilbert space is \(\ell^2(\mathbb Z^d)\), with \(\hbar=1\). The Hamiltonian is the bounded self-adjoint operator \(H=-\kappa\sum_{j=1}^d(S_j+S_j^*)\). A complete reset maps every density operator to \(|\mathbf0\rangle\langle\mathbf0|\), with memoryless rate \(r\). The initial state is immaterial after stationary convergence. Every limit fixes integer \(d\) and \(\kappa>0\) and takes \(r\downarrow0\); no simultaneous finite-size or large-dimensional limit is addressed. The collision statistic is *measured-position inverse participation*, not eigenvector participation, temporal mean of trajectory purity, or entanglement entropy.

## Proof
**1. Renewal formula and positivity.** Between resets, \(\psi_t=e^{-iHt}|\mathbf0\rangle\) has site probabilities
\[
 f_t(\mathbf n)=|\langle\mathbf n|\psi_t\rangle|^2
 =\prod_{j=1}^d J_{n_j}(2\kappa t)^2.
\]
The exponential stationary reset age gives a trace-class state
\(\rho_r=r\int_0^\infty e^{-rt}|\psi_t\rangle\langle\psi_t|\,dt\), hence \(p_{\mathbf n}(r)=r\int_0^\infty e^{-rt}f_t(\mathbf n)dt\). Set \(g_d(\mathbf n)=\int_0^\infty f_t(\mathbf n)dt\), allowing infinity. By positivity, Tonelli, and monotone convergence,
\[
\lim_{r\downarrow0}\frac{Q_d(r)}{r^2}
=\sum_{\mathbf n}g_d(\mathbf n)^2
=\int_0^\infty\!\int_0^\infty S(t,s)^d\,dt\,ds,
\quad S(t,s)=\sum_{n\in\mathbb Z}J_n(2\kappa t)^2J_n(2\kappa s)^2.
\]
Thus the problem is exactly the square-summability of the free-walk occupation Green function.

**2. Convergence in dimensions at least three.** Let \(B(t)=\sum_nJ_n(2\kappa t)^4\). Neumann's addition formula followed by Parseval gives
\[
 B(t)=\frac1{2\pi}\int_{-\pi}^{\pi}
 J_0\!\left(4\kappa t\sin\frac\theta2\right)^2\,d\theta.
\]
The classical uniform bound \(|J_0(x)|\le C(1+x)^{-1/2}\), \(x\ge0\), and \(\sin(\theta/2)\ge|\theta|/\pi\) for \(|\theta|\le\pi\) yield
\[
B(t)\le C\frac{1+\log(1+\kappa t)}{1+\kappa t}.
\]
Cauchy–Schwarz in the lattice index gives \(S(t,s)\le\sqrt{B(t)B(s)}\). Consequently,
\[
\int_0^\infty\!\int_0^\infty S(t,s)^d\,dt\,ds
\le\left[\int_0^\infty B(t)^{d/2}dt\right]^2<\infty
\quad(d>2).
\]
The last integral converges at infinity because its integrand is bounded by a constant times \(t^{-d/2}(\log t)^{d/2}\). Strict positivity follows from the positive integrand near \(t=s=0\).

**3. Divergence in dimension two (without unproved asymptotic extrapolation).** The one-coordinate free-walk random integer \(N_t\), with probabilities \(J_n(2\kappa t)^2\), has exact moments
\[
\mathbb E N_t^2=2\kappa^2t^2,\qquad
\mathbb E N_t^4=6\kappa^4t^4+2\kappa^2t^2.
\]
They follow by Taylor expansion of its exact characteristic function \(J_0(4\kappa t\sin(\theta/2))\). For \(\kappa t\ge1\), Cauchy–Schwarz applied to \(N_t^2\) above the threshold \(\kappa^2t^2\) gives
\[
\Pr(|N_t|\ge\kappa t)\ge
\frac{\kappa^4t^4}{6\kappa^4t^4+2\kappa^2t^2}\ge\frac18.
\]
For integer \(R\ge1\) define the two-dimensional annulus \(A_R=\{\mathbf n:R\le\|\mathbf n\|_\infty\le16R\}\). If \(t\in[R/\kappa,2R/\kappa]\), Chebyshev gives \(\Pr(|N_t|>16R)\le1/32\) for each coordinate. Taking the event \(|N_{t,1}|\ge\kappa t\) and excluding either coordinate's outer tail shows \(\Pr(\mathbf N_t\in A_R)\ge1/16\). Therefore
\[
\sum_{\mathbf n\in A_R}g_2(\mathbf n)\ge R/(16\kappa).
\]
Because \(|A_R|\le(33R)^2\), a second Cauchy–Schwarz estimate yields \(\sum_{\mathbf n\in A_R}g_2(\mathbf n)^2\ge1/(16^2 33^2\kappa^2)\). The annuli with \(R=32^j\), \(j\ge0\), are disjoint, so the sum diverges. Restricting to \(R\le\kappa/r\) and noting \(e^{-rt}\ge e^{-2}\) on each relevant time interval gives the stated positive \(r^2\log(\kappa/r)\) lower bound. The upper bound follows from
\[
\frac{Q_2(r)}{r^2}=\int\!\int e^{-r(t+s)} S(t,s)^2dt\,ds
\le\left[\int_0^\infty e^{-rt}B(t)dt\right]^2
=O\!\left(\kappa^{-2}\log^4(\kappa/r)\right).
\]
In dimension one the exact formula in the next step already implies divergence of \(Q_1(r)/r^2\).

**4. Exact one-dimensional collision and strict coherence witness.** Fourier transforming the one-dimensional stationary site probabilities and using Neumann's Bessel identity gives
\[
\widehat p(\theta)=r\int_0^\infty e^{-rt}J_0(4\kappa t\sin(\theta/2))dt
=\frac r{\sqrt{r^2+16\kappa^2\sin^2(\theta/2)}}.
\]
Parseval and the elementary trigonometric integral \(\frac1{2\pi}\int_{-\pi}^\pi(r^2+a^2\sin^2(\theta/2))^{-1}d\theta=[r\sqrt{r^2+a^2}]^{-1}\) prove \(Q_1\) exactly. The known all-dimensional purity identity follows from two independent exponential reset ages and the free return amplitude:
\[
P_d(r)=r\int_0^\infty e^{-rt}J_0(2\kappa t)^{2d}\,dt.
\]
For any \(d\), the absolute value of the stationary matrix element between the origin and one nearest neighbor is
\[
|\langle\mathbf0|\rho_r|\mathbf e_1\rangle|
=r\left|\int_0^\infty e^{-rt}J_0(2\kappa t)^{2d-1}J_1(2\kappa t)dt\right|
=\frac r{4d\kappa}(1-P_d(r))>0.
\]
The last equality is integration by parts of \(\partial_t J_0(2\kappa t)^{2d}=-4d\kappa J_0^{2d-1}J_1\); its strictness uses \(P_d(r)<1\). Since \(P_d(r)-Q_d(r)=\sum_{\mathbf m\ne\mathbf n}|\rho_r(\mathbf m,\mathbf n)|^2\), the quantum purity strictly exceeds the spatial collision probability. The standard complete-elliptic Bessel transform yields \(P_1(r)=\frac{2r}{\pi\sqrt{r^2+16\kappa^2}}K(4\kappa/\sqrt{r^2+16\kappa^2})\), proving the exact ratio and its logarithmic limit. For \(d\ge3\), dominated convergence in the known purity integral gives \(P_d(r)/r\to M_d\), while the first three steps give \(Q_d(r)/r^2\to C_d\), completing the ratio asymptotic.

## Verification
The accompanying `check_collision.py` implements 55 deterministic diagnostics: direct one-dimensional site-probability quadrature versus exact inverse participation, elliptic versus Bessel-Laplace purity, a closed nearest-neighbor coherence identity in five dimensions, and two independent two-dimensional collision representations. It also computes finite positive cutoffs of the convergent higher-dimensional integral. Run `python3 check_collision.py` with Python 3, NumPy and SciPy. The infinite-dimensional convergence/divergence is established by the estimates above, **not** by finite cutoffs or numerical tests.

## Relationship to prior work
Das–Dattagupta–Gupta and Acharya–Gupta derive stationary one-dimensional tight-binding site occupations under resetting (the latter primarily conditional resetting). General quantum-reset frameworks and the full stationary density operator predate this result. The published result *Dimension-indexed logarithmic purity singularities for Poisson-reset quantum lattice walks* explicitly determines \(P_d(r)\) and the dimension-dependent nonanalytic purity hierarchy, but does not state the separate positional inverse-participation classification for \(Q_d(r)\), its critical square-summability dimension, or the comparison via a stationary off-diagonal witness. Its purity formula is used as an established fact, not relabeled a new discovery. Dimension-one exact collision follows from published site profiles by a routine Parseval step and is not presented alone as the novel contribution. The assessed new statement is the all-dimension spatial collision/Green-function trichotomy and its measurable contrast with coherent purity. More general unlocated \(\ell^2\)-Green or dispersive theorems might imply this specialization; this is a priority risk.

## Limitations
The result proves the exact **threshold for a finite normalized spatial collision coefficient**, not the sharp leading coefficient of the logarithmic divergence in dimension two. The two-dimensional bounds intentionally leave logarithmic powers between one and four. No assertion is made for finite lattices, disorder, directional hopping imbalance, arbitrary reset distributions, conditional reset locations, or simultaneous large-dimension/rare-reset scaling. Publication priority remains subject to broader literature coverage.

## References
1. A. Acharya and S. Gupta, *Tight-binding model subject to conditional resets at random times*, first public preprint 27 August 2023, [arXiv:2308.14040](https://arxiv.org/abs/2308.14040).
2. S. Dattagupta, D. Das and S. Gupta, *Stochastic resets in the context of a tight-binding chain driven by an oscillating field*, [arXiv:2209.14117](https://arxiv.org/abs/2209.14117).
3. D. Das, S. Dattagupta and S. Gupta, *Quantum unitary evolution interspersed with repeated non-unitary interactions at random times*, [arXiv:2106.14181](https://arxiv.org/abs/2106.14181).
4. B. Mukherjee, K. Sengupta and S. N. Majumdar, *Quantum dynamics with stochastic reset*, [arXiv:1806.00019](https://arxiv.org/abs/1806.00019).
5. S. Wald and L. Böttcher, *From classical to quantum walks with stochastic resetting on networks*, [arXiv:2008.00510](https://arxiv.org/abs/2008.00510).
6. *Dimension-indexed logarithmic purity singularities for Poisson-reset quantum lattice walks*, published research record, [full result](https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-dimension-indexed-logarithmic-purity-singularities-for-poisson-r--fd0e95513bb2/RESULT.md).
7. NIST Digital Library of Mathematical Functions, [Bessel addition theorems, §10.23](https://dlmf.nist.gov/10.23), [asymptotics, §10.17](https://dlmf.nist.gov/10.17), and [elliptic integrals, §19.12](https://dlmf.nist.gov/19.12).
