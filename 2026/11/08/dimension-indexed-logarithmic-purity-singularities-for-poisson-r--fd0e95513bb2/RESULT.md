# Dimension-indexed logarithmic purity singularities for Poisson-reset quantum lattice walks

## Finding
Let \(d\ge1\) be a fixed integer, \(\kappa>0\), and \(r>0\). For the continuous-time nearest-neighbor quantum walk on \(\mathbb Z^d\) fully reset to the origin at independent Poisson times of rate \(r\), the stationary ensemble state has exact purity
\[
P_d(r):=\operatorname{Tr}(\rho_r^2)
=r\int_0^\infty e^{-rt}J_0(2\kappa t)^{2d}\,dt.
\]
Put
\[
a_d=\frac{\binom{2d}{d}}{4^d(\pi\kappa)^d},\qquad
\mu_{j,d}=\int_0^\infty t^jJ_0(2\kappa t)^{2d}\,dt
\quad (0\le j\le d-2).
\]
The indicated moments are finite. For every fixed \(d\ge1\), \(\kappa>0\), as \(r\downarrow0\),
\[
\boxed{P_d(r)=\sum_{j=0}^{d-2}\frac{(-1)^j\mu_{j,d}}{j!}r^{j+1}
+\frac{(-1)^{d-1}a_d}{(d-1)!}r^d\log(\kappa/r)+O_{d,\kappa}(r^d).}
\]
The sum is empty for \(d=1\). In particular, the first nonanalytic weak-reset term occurs **at order \(r^d\log(1/r)\)** for every dimension, with an explicit nonzero alternating coefficient:
\[
\begin{aligned}
P_1(r)&=\frac{r}{2\pi\kappa}\log(\kappa/r)+O(r),\\
P_2(r)&=\mu_{0,2}r-\frac{3}{8\pi^2\kappa^2}r^2\log(\kappa/r)+O(r^2),\\
P_3(r)&=\mu_{0,3}r-\mu_{1,3}r^2+\frac{5}{32\pi^3\kappa^3}r^3\log(\kappa/r)+O(r^3).
\end{aligned}
\]
For \(d=1\), a standard Bessel-transform identity gives the additional *exact* formula
\[
P_1(r)=\frac{2r}{\pi\sqrt{r^2+16\kappa^2}}\,
K\!\left(\frac{4\kappa}{\sqrt{r^2+16\kappa^2}}\right),
\qquad K(k)=\int_0^{\pi/2}\frac{d\theta}{\sqrt{1-k^2\sin^2\theta}},
\]
and hence the sharper equivalent \(P_1(r)\sim\frac{r}{2\pi\kappa}\log(16\kappa/r)\).
The stationary second Rényi entropy \(S_{2,d}=-\log P_d\) satisfies
\[
S_{2,1}(r)=\log(\kappa/r)-\log\log(\kappa/r)+\log(2\pi)+o(1),
\]
whereas for each \(d\ge2\),
\[
S_{2,d}(r)=\log(\kappa/r)-\log(\kappa\mu_{0,d})+o(1).
\]
For completeness, the independent strong-reset expansion is
\[
P_d(r)=1-\frac{4d\kappa^2}{r^2}+\frac{12d(4d-1)\kappa^4}{r^4}+O_{d,\kappa}(r^{-6})
\qquad (r\to\infty).
\]

## Assumptions and scope
Work in \(\mathcal H=\ell^2(\mathbb Z^d)\), with unit lattice spacing, \(\hbar=1\), origin vector \(\lvert0\rangle\), and the bounded self-adjoint tight-binding Hamiltonian
\[
H=-\kappa\sum_{j=1}^{d}(S_j+S_j^*),
\]
where \(S_j\) translates one lattice step in coordinate \(j\). A complete reset instantaneously replaces the entire density matrix by \(\lvert0\rangle\langle0\rvert\) independently of the state just before resetting. Reset times form a homogeneous Poisson process of rate \(r\), independent of the coherent evolution. Define the stationary ensemble state using the equilibrium exponential age distribution; the same state is reached in trace norm from a reset initial state as time tends to infinity. The limit \(r\downarrow0\) is taken at fixed integer \(d\) and fixed \(\kappa>0\); neither a thermodynamic finite-torus limit exchanged with \(r\to0\) nor a joint large-dimensional limit is asserted.

## Proof
**1. Stationary state and overlap reduction.** Between resets, put \(\psi_t=e^{-iHt}\lvert0\rangle\). Since a Poisson reset age at stationarity is exponential, the Bochner trace-class integral
\[
\rho_r=r\int_0^\infty e^{-rt}\lvert\psi_t\rangle\langle\psi_t\rvert\,dt
\]
converges in trace norm, is positive, and has trace one. For a process started in the reset state, the missing no-reset contribution has total trace norm at most twice \(e^{-rt}\), proving convergence. By rank-one projector multiplication,
\[
P_d(r)=r^2\int_0^\infty\!\int_0^\infty e^{-r(t+s)}
\lvert\langle\psi_s,\psi_t\rangle\rvert^2\,dt\,ds.
\]
Fourier diagonalization of \(H\) on \(\mathbb T^d\) gives
\[
\langle0\rvert e^{-iuH}\lvert0\rangle
=\prod_{j=1}^d\frac1{2\pi}\int_{-\pi}^{\pi}e^{2i\kappa u\cos q_j}\,dq_j
=J_0(2\kappa u)^d.
\]
The identity \(\int_0^\infty\!\int_0^\infty r^2e^{-r(s+t)}F(|t-s|)\,dt\,ds=r\int_0^\infty e^{-ru}F(u)\,du\) (integrate first along the difference and then along the minimum) establishes the exact purity formula.

**2. Long-time return kernel.** The standard fixed-argument large-time Bessel expansion yields
\[
J_0(2\kappa t)=(\pi\kappa t)^{-1/2}
\left[\cos(2\kappa t-\pi/4)+O_{\kappa}(t^{-1})\right].
\]
Consequently, as \(t\to\infty\),
\[
f_d(t):=J_0(2\kappa t)^{2d}
=t^{-d}\bigl(a_d+g_d(t)\bigr)+O_{d,\kappa}(t^{-d-1}),
\]
where \(g_d\) is a finite trigonometric polynomial of nonzero frequencies. Its zero average follows from
\[
\frac1{2\pi}\int_0^{2\pi}\cos^{2d}\theta\,d\theta=\binom{2d}{d}4^{-d},
\]
and its primitive is bounded. The positive mean term \(a_dt^{-d}\) proves \(\mu_{j,d}<\infty\) precisely when \(j\le d-2\): for \(j\ge d-1\), nonnegativity and positive periodic mean force divergence.

**3. Extracting the first logarithm, with its remainder.** For \(m=d-2\), where an empty Taylor sum is understood when \(d=1\), introduce
\[
R_m(z)=e^{-z}-\sum_{j=0}^{m}\frac{(-z)^j}{j!}.
\]
The difference between the Laplace transform of \(f_d\) and its finite Taylor moments is \(\int_0^\infty f_d(t)R_{d-2}(rt)\,dt\). For fixed \(d\), on \(0\le z\le1\),
\[
R_{d-2}(z)=\frac{(-z)^{d-1}}{(d-1)!}+O_d(z^d),
\]
including the case \(d=1\), when \(R_{-1}(z)=e^{-z}\). Split the integral into \([0,1]\), \([1,r^{-1}]\), and \([r^{-1},\infty)\), for sufficiently small \(r\). The bounded first interval and the far tail are \(O_{d,\kappa}(r^{d-1})\). The positive mean term on the middle interval gives
\[
\int_1^{1/r}a_dt^{-d}R_{d-2}(rt)\,dt
=\frac{(-1)^{d-1}a_d}{(d-1)!}
 r^{d-1}\log(1/r)+O_{d,\kappa}(r^{d-1}).
\]
For the oscillatory term, the leading Taylor remainder produces \(r^{d-1}\int_1^{1/r}g_d(t)t^{-1}\,dt\), which is \(O(r^{d-1})\) because \(g_d\) has a bounded primitive. The extra Taylor remainder and the \(O(t^{-d-1})\) Bessel error are likewise \(O(r^{d-1})\), by direct integration; replacing \(\log(1/r)\) by \(\log(\kappa/r)\) only changes the bounded remainder constant. Finally multiply the resulting Laplace expansion by \(r\). This proves the claimed general expansion with its nonzero coefficient for each fixed \(d\).

**4. Closed one-dimensional identity and entropies.** The classical Bessel product identity
\[
J_0(2\kappa t)^2=\frac2\pi\int_0^{\pi/2}J_0(4\kappa t\cos\theta)\,d\theta
\]
and \(\int_0^\infty e^{-rt}J_0(bt)\,dt=(r^2+b^2)^{-1/2}\) yield the stated complete-elliptic expression. The standard logarithmic singularity of \(K(k)\) at \(k\uparrow1\) supplies \(\log(16\kappa/r)\) and its coefficient. Taking negative logarithms proves the stated Rényi entropies: the one-dimensional case has the extra \(-\log\log(\kappa/r)\), whereas \(\mu_{0,d}>0\) is finite for \(d\ge2\).

**5. Strong resetting.** At small time, \(J_0(2\kappa t)=1-\kappa^2t^2+\kappa^4t^4/4+O(t^6)\), hence
\[
f_d(t)=1-2d\kappa^2t^2+\frac{d(4d-1)}2\kappa^4t^4+O(t^6).
\]
Termwise Laplace integration over a small-time cutoff, plus an exponentially small remaining tail, gives the displayed large-\(r\) expansion using \(r\int_0^\infty e^{-rt}t^n\,dt=n!/r^n\).

## Verification
The accompanying standalone `check_purity.py` (Python 3; NumPy/SciPy) performs 34 finite assertions: independent one-dimensional Bessel-Laplace versus elliptic evaluations, finite-cycle spectral sums versus their infinite-lattice values, positivity and monotonicity across several \(d\), strong-reset coefficients, the elliptic weak-reset logarithm, and central-binomial trigonometric averages. Reproduction: `python3 check_purity.py`. These checks diagnose normalization and numerical consistency; the all-dimensional asymptotic assertion is proved analytically above and is **not** inferred from finite numerical verification.

## Relationship to prior work
The stationary renewal density-matrix formula and stochastic quantum-reset framework were developed by Mukherjee–Sengupta–Majumdar, Rose–Touchette–Lesanovsky–Garrahan, and related authors. Wald–Böttcher analyze stationary quantum-walk occupations on networks. Das–Dattagupta–Gupta give exact stationary site occupations and weak-reset spatial spreading for a one-dimensional tight-binding chain. Dattagupta–Das–Gupta also investigate the driven chain; Acharya–Gupta analyze conditional rather than unconditional resets. These results supply the dynamical setting and sometimes exact single-site return transforms but do **not** state the fixed-\(d\) sequence of first nonanalytic *ensemble-purity* terms \(r^d\log(\kappa/r)\), with their coefficients, nor the consequent dimension-specific Rényi entropy behavior. The one-dimensional elliptic integral and Bessel asymptotics are classical special-function identities, not claimed original; the distinct statement here is their all-dimensional stationary ensemble-purity synthesis and the hierarchy of logarithmic thresholds.

## Limitations
The claim concerns stationary *ensemble-state* purity, not mean purity of pure reset trajectories (which would be one), and not entanglement entropy across a subsystem partition. It assumes complete, state-independent Poisson reset to the origin and an exactly homogeneous infinite cubic lattice. There is no claimed uniformity in \(d\) or in \(\kappa\) as either changes with \(r\). Stronger abstract spectral Abelian theorems may imply the asymptotic mechanism without this explicit quantum-lattice formulation; a missed published specialization remains a provenance and priority risk. 

## References
1. B. Mukherjee, K. Sengupta and S. N. Majumdar, *Quantum dynamics with stochastic reset*, initial preprint 31 May 2018, [arXiv:1806.00019](https://arxiv.org/abs/1806.00019).
2. D. C. Rose, H. Touchette, I. Lesanovsky and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, 2018, [arXiv:1806.01298](https://arxiv.org/abs/1806.01298).
3. S. Wald and L. Böttcher, *From classical to quantum walks with stochastic resetting on networks*, 2020 preprint, [arXiv:2008.00510](https://arxiv.org/abs/2008.00510).
4. D. Das, S. Dattagupta and S. Gupta, *Quantum unitary evolution interspersed with repeated non-unitary interactions at random times*, initial preprint 27 June 2021, [arXiv:2106.14181](https://arxiv.org/abs/2106.14181).
5. S. Dattagupta, D. Das and S. Gupta, *Stochastic resets in context of tight-binding chain driven by oscillating field*, 2022, [arXiv:2209.14117](https://arxiv.org/abs/2209.14117).
6. A. Acharya and S. Gupta, *Tight-binding model subject to conditional resets at random times*, 2023, [arXiv:2308.14040](https://arxiv.org/abs/2308.14040).
7. NIST Digital Library of Mathematical Functions, [§10.17 Bessel large-argument expansions](https://dlmf.nist.gov/10.17) and [§19.12 complete elliptic integrals near singularities](https://dlmf.nist.gov/19.12).
