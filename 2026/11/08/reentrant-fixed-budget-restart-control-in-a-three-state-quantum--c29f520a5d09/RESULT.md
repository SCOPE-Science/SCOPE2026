# Reentrant fixed-budget restart control in a three-state quantum walk

## Finding

Consider the discrete-time lackadaisical Grover quantum walk on the integer lattice, with positive self-loop weight \(\ell\). At each renewal, both the walker and coin are restored to the origin with coin state \(s_\ell=(1,\sqrt{\ell},1)/\sqrt{\ell+2}\). Independently sampled restart intervals \(T\) take values in \(\{1,2,3,4\}\) and obey the fixed mean budget \(\mathbb E T=3\). Observe the system in its stationary renewal phase, and maximize the probability \(R_\ell\) that it is at the origin, with no intermediate detection.

Write three restart protocols:

- \(D\): \(\Pr(T=3)=1\).
- \(B\): \(\Pr(T=1)=1/3\), \(\Pr(T=4)=2/3\).
- \(C\): \(\Pr(T=2)=\Pr(T=4)=1/2\).

Let \(\alpha\) be the unique root in \((0.140,0.141)\) of
\[
P(\ell)=3\ell^4-8\ell^3-3\ell^2-28\ell+4=0,
\]
and let \(\beta\) be the unique positive root of
\[
Q(\ell)=3\ell^4+2\ell^3+3\ell^2-20\ell-4=0.
\]
Set \(\gamma=(7+\sqrt{41})/2\). Numerically, these are \(\alpha\approx0.140013679\), \(\beta\approx1.608554345\), and \(\gamma\approx6.701562119\).

**Theorem.** Among all such restart laws, the unique maximizer is \(D\) for \(0<\ell<\alpha\), \(B\) for \(\alpha<\ell<\beta\), \(C\) for \(\beta<\ell<\gamma\), and \(D\) for \(\ell>\gamma\). At each transition, precisely the two adjacent listed protocols (and their convex mixtures) are optimal. No other ties occur.

For the matching classical lazy walk, whose independent steps are \(-1\), \(0\), \(+1\) with probabilities \(1/(\ell+2)\), \(\ell/(\ell+2)\), \(1/(\ell+2)\), **the unique optimal law is \(D\) for every \(\ell>0\)** under the identical interval and mean constraints. Hence the intermediate preference for randomized restarting and its return to deterministic control at both parameter extremes are coherence-dependent.

At \(\ell=1\), the quantum optimum is \(R_1(B)=1471/2187\), compared with \(R_1(D)=5/9\); the matching classical optimum is also \(5/9\). The strict quantum protocol advantage is \(256/2187\).

## Assumptions and scope

The walker Hilbert space is \(\mathbb C^3\otimes\ell^2(\mathbb Z)\), with ordered coin states \((-1,0,+1)\). Define the normalized coin \(s_\ell\), reflection \(G_\ell=2s_\ell s_\ell^*-I_3\), and conditional translation \(S(|c\rangle\otimes|x\rangle)=|c\rangle\otimes|x+c\rangle\). One free step is \(U_\ell=S(G_\ell\otimes I)\). The free initial state is \(s_\ell\otimes|0\rangle\); every restart reconstructs exactly this state, and the independent clock does not depend on the walk state. The four allowed positive integer intervals represent a four-step maximum restart latency, while the mean-three constraint fixes the average renewal budget.

Let \(p_a(\ell)=\| (I_3\otimes\langle0|) U_\ell^a(s_\ell\otimes|0\rangle)\|^2\) for integer \(a\ge0\). A *stationary renewal-phase observation* uses the invariant age law \(\Pr(A=a)=\Pr(T>a)/\mathbb E T\), which exists for all finite supported intervals, including periodic clocks. This qualification is essential: starting a deterministic clock at age zero need not yield a pointwise-in-time limiting marginal because of periodicity. The theorem asserts the invariant-phase expectation (equivalently, the long-time Cesàro average), not convergence of every synchronized trajectory's marginal.

The classical comparator is not a repeatedly measured quantum state with persistent coin memory. It is the standard independent-increment lazy random walk matched to the quantum walk's one-step position probabilities, with the same complete restarts and stationarity convention.

The classification is exact within \(\operatorname{supp} T\subseteq\{1,2,3,4\}\) and \(\mathbb E T=3\). It makes no optimality claim over unrestricted longer intervals, other initial coin states, monitored first-detection objectives, or trajectories not observed at stationary phase.

## Proof

**1. Four free return probabilities.** From \(G_\ell s_\ell=s_\ell\), the local amplitude recurrence is
\[
\psi_n(t+1)_c=(G_\ell\psi_{n-c}(t))_c,\qquad c\in\{-1,0,1\}.
\]
Applying this recurrence at each occupied site, and writing \(\psi_0(a)\) for the unnormalized coin vector at the origin, gives
\[
\begin{aligned}
\psi_0(0)&=\frac{(1,\sqrt\ell,1)}{\sqrt{\ell+2}},\\
\psi_0(1)&=\frac{(0,\sqrt\ell,0)}{\sqrt{\ell+2}},\\
\psi_0(2)&=\frac{(2,\sqrt\ell(\ell-2),2)}{(\ell+2)^{3/2}},\\
\psi_0(3)&=\frac{(8\ell,\sqrt\ell(\ell^2-4\ell+12),8\ell)}{(\ell+2)^{5/2}}.
\end{aligned}
\]
Thus, by direct squared norms,
\[
\begin{aligned}
p_0&=1,\\
p_1&=\frac{\ell}{\ell+2},\\
p_2&=\frac{\ell^3-4\ell^2+4\ell+8}{(\ell+2)^3},\\
p_3&=\frac{\ell(\ell^4-8\ell^3+40\ell^2+32\ell+144)}{(\ell+2)^5}.
\end{aligned}
\]
These are unconditional, unmonitored position probabilities; they are not first-detection probabilities.

**2. Stationary restart objective and complete feasible set.** Define \(F_j=\sum_{a=0}^{j-1}p_a\) for \(j=1,2,3,4\). The size-biased renewal-cycle identity gives
\[
R_\ell(T)=\sum_{a=0}^3\frac{\Pr(T>a)}{3}p_a
=\frac{\mathbb E F_T}{3}.
\]
The four probabilities \(x_j=\Pr(T=j)\) obey \(x_j\ge0\), \(\sum_{j=1}^4x_j=1\), and \(\sum_{j=1}^4j x_j=3\). Their polytope is exactly the triangle with vertices \(D,B,C\). Indeed a basic feasible point has at most two positive coordinates; any support bracketing mean three is one of \(\{1,4\}\), \(\{2,4\}\), or the singleton \(\{3\}\). Therefore maximizing the linear objective reduces *without approximation* to the three candidate values
\[
R_D=\frac{F_3}{3},\qquad
R_B=\frac{F_1+2F_4}{9},\qquad
R_C=\frac{F_2+F_4}{6}.
\]

**3. Exact phase diagram.** Subtracting these three values and substituting the free returns yields
\[
\begin{aligned}
R_B-R_D&=-\frac{8P(\ell)}{9(\ell+2)^5},\\
R_B-R_C&=-\frac{4Q(\ell)}{9(\ell+2)^5},\\
R_C-R_D&=-\frac{4(\ell^2-7\ell+2)(\ell^2+\ell+2)}{3(\ell+2)^5}.
\end{aligned}
\]
Descartes' rule gives at most two positive roots for \(P\) and at most one for \(Q\). Exact rational endpoint sign evaluations show that \(P\) has roots in \((0.140,0.141)\) and \((3.624,3.626)\), and that \(Q\) has a root in \((1.608,1.609)\). Consequently these brackets exhaust their positive roots. The positive zeros of \(\ell^2-7\ell+2\) are \((7-\sqrt{41})/2\approx0.298438\) and \(\gamma\approx6.701562\), and the factor \(\ell^2+\ell+2\) is strictly positive for every \(\ell>0\). The resulting strict order of comparison points is
\[
0<\alpha<\frac{7-\sqrt{41}}{2}<\beta<3.6248641\ldots<\gamma.
\]
The three displayed comparison signs now give, interval by interval, the stated winning protocol \(D,B,C,D\). At the three winning transitions exactly one pairwise difference vanishes while the third candidate lies strictly below; hence all optimal distributions there are precisely the convex mixtures of the two tied vertices. The other positive root of \(P\) is a crossing of two *nonwinning* candidates and causes no additional optimal transition.

**4. Coherent versus classical control.** For the independent-increment lazy walk with probabilities \(r=1/(\ell+2)\) and \(q=\ell/(\ell+2)\), elementary path counting gives
\[
p_0^{\mathrm{cl}}=1,\quad
p_1^{\mathrm{cl}}=q,\quad
p_2^{\mathrm{cl}}=q^2+2r^2,\quad
p_3^{\mathrm{cl}}=q^3+6qr^2.
\]
The same renewal-polytope reduction applies. Its decisive pairwise differences have numerators
\[
\begin{aligned}
2p_3^{\mathrm{cl}}-p_1^{\mathrm{cl}}-p_2^{\mathrm{cl}}&=-\frac{2(3\ell^2-3\ell+2)}{(\ell+2)^3}<0,\\
p_3^{\mathrm{cl}}-p_2^{\mathrm{cl}}&=-\frac{2(\ell^2-2\ell+2)}{(\ell+2)^3}<0.
\end{aligned}
\]
Both quadratics are positive for all real \(\ell\) by completing squares. Hence the classical \(R_B<R_D\) and \(R_C<R_D\) strictly for every positive \(\ell\), proving unique deterministic optimality. Finally, evaluating the quantum expressions at \(\ell=1\) gives \(R_D=5/9\), \(R_B=1471/2187\), and \(R_C=469/729\), with \(R_B-R_D=256/2187\), as claimed.

## Verification

The included `verify.py` uses only the Python standard library and can be run with `python3 verify.py`. It evolves full spatial coin amplitudes independently of the closed return formulas, enumerates the classical path probabilities, checks the three polynomial comparison identities at exact rational inputs, locates the three winning boundaries by bisection, checks strict phase regimes, and draws two thousand constrained renewal laws as convex mixtures of all three vertices. At the time of preparation it passed 8,307 bounded checks. Numerical diagnostics are consistency tests and do not establish universal optimality; that follows from the recurrence, the exact finite-dimensional feasible polytope, the polynomial identities, and the root-count proof above.

## Relationship to prior work

Das, *Restart and first detection in a lackadaisical quantum walk with flat-band localization* (arXiv:2609.08973v1, first posted 2026-09-08), establishes this weighted three-state quantum walk, the flat-band-active initial coin state, and the general unmonitored renewal identity for finite-mean restart (Sections II–III). The general stationary-age formula and the basic quantum-walk model are not new here. Das studies geometric and power-law unmonitored waiting times, and separately optimizes *monitored first detection* under sharp restart. The present theorem instead optimizes a mean-constrained, bounded-delay unmonitored restart clock for stationary return occupation and includes an exact parameter-dependent classical comparator.

Yin, Wang and Barkai, *Instability in the quantum restart problem* (arXiv:2301.06100; Physical Review E 109, 064150), analyzes monitored first-hitting times and sharp restart thresholds. Chełminiak, Wójcik and Wójcik, *Discrete-time walk on one-dimensional lattice under stochastic resetting: Advantage of quantum over classical scenario* (Physical Review E 111, 044143, 2025), compares mean absorption times with absorbing sites, not this stationary single-site residence criterion. General first-passage restart optimization and quantum detection laws do not determine the displayed three-policy phase diagram. Eule and Metzger (2016) and Wald et al. (2021) provide broader renewal and network-resetting frameworks, respectively; those frameworks are also acknowledged prior work. The particular finite-horizon optimization, root locations, reentrance, and classical dominance inequalities are additional claims requiring independent publication-priority checking.

## Limitations

The mean and maximum latency constraints are part of the theorem, not incidental numerical truncations. Longer-than-four-step restart intervals may change the optimum; no unrestricted optimality is asserted. A clock synchronized from time zero may have periodic marginals under deterministic or even-span interval distributions, so the invariant-phase mixture is necessary. No active monitoring occurs before observation, and the conclusion is not a first-passage theorem. The classical comparator has independent increments and is not a general decohered quantum channel. The source's general renewal theorem supplies much of the framework; a wider, presently unidentified fixed-budget optimal-restart theorem might subsume this specialization. No independent validation or publication-priority audit has been conducted.

## References

1. Debraj Das, *Restart and first detection in a lackadaisical quantum walk with flat-band localization*, arXiv:2609.08973v1 (2026-09-08), https://arxiv.org/html/2609.08973v1 .
2. Ruoyu Yin, Qingyuan Wang and Eli Barkai, *Instability in the quantum restart problem*, arXiv:2301.06100 (2023), https://arxiv.org/abs/2301.06100 ; Physical Review E 109, 064150 (2024), https://doi.org/10.1103/PhysRevE.109.064150 .
3. Przemysław Chełminiak, Jan Wójcik and Antoni Wójcik, *Discrete-time walk on one-dimensional lattice under stochastic resetting: Advantage of quantum over classical scenario*, Physical Review E 111, 044143 (2025), https://doi.org/10.1103/PhysRevE.111.044143 .
4. Debraj Das and Luca Giuggioli, *Discrete space-time resetting model: application to first-passage and transmission statistics*, Journal of Physics A 55, 424004 (2022), https://doi.org/10.1088/1751-8121/ac9765 .
5. Stephan Eule and Jakob J. Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting*, New Journal of Physics 18, 033006 (2016), https://doi.org/10.1088/1367-2630/18/3/033006 .
6. Sascha Wald et al., *From classical to quantum walks with stochastic resetting on networks*, Physical Review E 103, 012122 (2021), https://doi.org/10.1103/PhysRevE.103.012122 .
