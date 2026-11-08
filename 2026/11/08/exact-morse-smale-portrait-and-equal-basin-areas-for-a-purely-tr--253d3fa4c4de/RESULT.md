# Exact Morse–Smale portrait and equal basin areas for a purely triadic oscillator triangle

## Finding
For three identical phase oscillators with only symmetric triadic coupling, every relative-phase trajectory converges to exactly one phase-locked state. The quotient dynamics on the phase-difference two-torus are Morse–Smale, with **exactly 18 hyperbolic equilibria: three sinks, nine saddles and six sources**, and no other nonwandering trajectories. Each sink has an attraction basin of *exactly one third* of the torus's flat area, namely \(4\pi^2/3\). The exceptional initial conditions are contained in the nine one-dimensional saddle stable manifolds and the six source equilibria.

## Assumptions and scope
Let \(\theta_i\in\mathbb T=\mathbb R/(2\pi\mathbb Z)\), with \(i\in\{1,2,3\}\), and let \(K>0\), \(\Omega\in\mathbb R\). The smooth autonomous system is
\[
\dot\theta_i=\Omega+K\sin(\theta_j+\theta_k-2\theta_i),\qquad\{i,j,k\}=\{1,2,3\}.
\]
The system has *no pairwise terms, no heterogeneous natural frequencies, and no other three-body harmonics*. Quotient the common rigid phase by the coordinates \(x=\theta_2-\theta_1\), \(y=\theta_3-\theta_1\), each modulo \(2\pi\). The induced flow is
\[
\dot x=-K[\sin(2x-y)+\sin(x+y)],\qquad
\dot y=-K[\sin(2y-x)+\sin(x+y)].
\]
A quotient equilibrium is a phase-locked solution in the original system; the three sink configurations, represented with \(\theta_1=0\), are \((0,0,0)\), \((0,2\pi/3,4\pi/3)\), and \((0,4\pi/3,2\pi/3)\). Basin area refers to the standard flat Lebesgue measure \(dx\,dy\) on \(\mathbb T^2\), of total mass \(4\pi^2\).

## Proof
**1. Strict potential.** Put \(\phi_1=-x-y\), \(\phi_2=2x-y\), \(\phi_3=2y-x\) modulo \(2\pi\), so \(\phi_1+\phi_2+\phi_3\equiv0\pmod{2\pi}\). With \(\bar s=\tfrac13\sum_i\sin\phi_i\), direct differentiation gives
\[
\dot\phi_i=-3K(\sin\phi_i-\bar s).
\]
The globally defined potential
\[
V=\sum_{i=1}^3(1-\cos\phi_i)
=3-\cos(x+y)-\cos(2x-y)-\cos(2y-x)
\]
satisfies the exact identity
\[
\dot V=-3K\sum_{i=1}^3(\sin\phi_i-\bar s)^2\le0.
\]
Equality holds precisely when all three sines agree, in which case all three relative angular velocities vanish. Thus the zero-dissipation set is precisely the quotient equilibrium set.

**2. Exhaustive critical-point census.** If three angles have the same sine, each is congruent to either \(a\) or \(\pi-a\). If all three are congruent, the zero-sum constraint gives \(3a\equiv0\pmod{2\pi}\), hence the three triples \((0,0,0)\), \((2\pi/3,2\pi/3,2\pi/3)\), and \((4\pi/3,4\pi/3,4\pi/3)\). If both sine branches occur, taking two copies of one branch and one copy of the other forces \(a\equiv0\) or \(\pi\); the resulting triples are exactly the three permutations of \((0,\pi,\pi)\). Therefore the \(\phi\)-torus contains exactly six equilibria. The map from \((x,y)\) to \((\phi_2,\phi_3)\) has integer matrix
\[
M=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\qquad \det M=3.
\]
It is a degree-three torus covering. Every one of the six equilibria has exactly three distinct lifts: **18 total**.

**3. Hyperbolic types and energy levels.** On the tangent plane \(\sum_i\delta\phi_i=0\), the Jacobian is \(-3K P\operatorname{diag}(\cos\phi_i)\), where \(P=I-\mathbf1\mathbf1^\top/3\). At the uniform zero triple its two eigenvalues are \(-3K,-3K\); at each nonzero uniform triple they are \(3K/2,3K/2\); and at each permutation of \((0,\pi,\pi)\) they are \(-K,3K\). The corresponding potential levels are, respectively, \(0\), \(9/2\), and \(4\). Lifting preserves these eigenvalues and yields three sinks, six sources and nine saddles, all hyperbolic.

**4. Global convergence and Morse–Smale transversality.** Compactness of \(\mathbb T^2\) ensures global existence. The strict potential and the invariance principle imply that every omega-limit set lies in the finite equilibrium set. An omega-limit set of a continuous orbit on a compact space is connected, so it consists of a single equilibrium; in particular every quotient trajectory converges. The strict potential excludes nontrivial recurrent trajectories. No heteroclinic connection can join any two saddles, or a saddle to itself, since all saddles have equal potential \(4\), whereas potential decreases strictly along nonstationary trajectories. All other possible invariant-manifold intersections involve a source (whose unstable manifold is full two-dimensional) or a sink (whose stable manifold is full two-dimensional), hence are automatically transverse. The nonwandering set is therefore finite and hyperbolic and all stable/unstable intersections are transverse: the flow is Morse–Smale.

**5. Exact basin fractions.** Apart from the stable manifolds of nine saddles and the six source points, every initial condition converges to a sink. These exceptional sets have flat two-dimensional measure zero. The order-three translation
\[
(x,y)\longmapsto(x+4\pi/3,\ y+2\pi/3)\pmod{2\pi}
\]
leaves the vector field unchanged because it changes each \(\phi_i\) by an integer multiple of \(2\pi\), and it cyclically permutes the three sinks. Translation preserves flat area, so all three open sink basins have equal area. Their union has full area \(4\pi^2\); each therefore has area \(4\pi^2/3\).

## Verification
The accompanying standalone `verify.py` checks the quotient and covering identities, the exact 18 stationary lifts, all Jacobian spectra and potential levels, the threefold translation symmetry, and 24 illustrative numerical initial conditions. It prints `VERIFY_OK covering_degree=3 critical_points=18 sink=3 saddle=9 source=6 energy_levels=3 numerical_orbits=24`. Finite trajectory tests do **not** prove universal convergence, exhaustiveness or Morse–Smale transversality; the five analytic steps above do.

## Relationship to prior work
Dai and Kori (2025) introduce a larger three-oscillator model whose \(k_{21}\)-only, equal-frequency specialization is exactly the present differential equation. Their published analysis gives local Jacobian trace/determinant identities and numerically studies transitions and multistability with additional couplings and frequency mismatch; it does not give this exact 18-state global classification or three equal basin areas. Bick, Böhle and Kuehn (2022) develop a general many-oscillator/multi-population framework, primarily for invariant synchrony sets and their stability, rather than an exact finite-triangle Morse–Smale portrait. Wang et al. (2026) study heterogeneous frequencies in a triadically coupled ring and numerically compare basin stability; Kumpeerakij and Restrepo (2026) develop self-consistent approximations on general hypergraphs. Neither establishes these finite, identical-frequency equal-area basins. Nijholt et al. (2026) investigate a different resonant-frequency hyperlocking mechanism. Standard compact-gradient arguments are used and not claimed as new.

## Limitations
The claim is for exactly three oscillators and symmetric pure triadic sinusoidal coupling with identical intrinsic frequency and \(K>0\). It does not describe perturbed coupling, frequency mismatch, stochastic forcing, precise geometry of the basin boundaries, or the unquotiented common-phase drift. A literature search is not a proof of absolute historical priority, and no independent mathematical validation is claimed.

## References
1. Q. Dai and H. Kori, *Higher-order synchronization and multistability in higher-order Kuramoto phase oscillators*, Nonlinear Dynamics **113** (2025), 21801–21811. DOI: `10.1007/s11071-025-11274-1` (public May 31, 2025).
2. C. Bick, T. Böhle and C. Kuehn, *Multi-population phase oscillator networks with higher-order interactions*, NoDEA **29** (2022), article 64. DOI: `10.1007/s00030-022-00796-x`.
3. Z. Wang, J. Zhu, W. Qi and X. Liu, *Frequency Heterogeneity can Promote Order yet Undermine Stability in Kuramoto Networks with Higher-Order Interactions*, arXiv:`2603.14950` (March 16, 2026).
4. C. Kumpeerakij and J. G. Restrepo, *Self-consistent analysis of the Kuramoto model with higher-order interactions*, arXiv:`2605.24701` (May 23, 2026).
5. E. Nijholt et al., *Hypernetworks induce stable hyperlocking*, Nature Communications **17** (2026), article 7947. DOI: `10.1038/s41467-026-74556-1` (June 24, 2026).
