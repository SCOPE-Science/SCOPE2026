# Two exact magnetic entropy spikes on the rhombicuboctahedral Ising antiferromagnet

## Finding
Let \(G\) be the 24-vertex, 48-edge graph of the convex *small rhombicuboctahedron* and put Ising spins \(\sigma_v\in\{-1,+1\}\) on its vertices. With unit antiferromagnetic exchange and a uniform real magnetic field \(h\), define
\[
\mathcal H_h(\sigma)=\sum_{uv\in E(G)}\sigma_u\sigma_v-h\sum_{v\in V(G)}\sigma_v.
\]
For \(h\ge0\), the exact ground energy is
\[
E_0(h)=\begin{cases}-32,&0\le h\le2,\\-16-8h,&2\le h\le4,\\48-24h,&h\ge4.\end{cases}
\]
The ground-state magnetization \(M=\sum_v\sigma_v\) is respectively \(0\), \(8\), and \(24\) in the three strict regions \(0\le h<2\), \(2<h<4\), and \(h>4\); the strict-region multiplicities are \(18,234,1\). At \(h=2\), the magnetizations are exactly \(0,2,4,6,8\), with a total of **1,392** ground states. More precisely, putting \(k=(24-M)/2\), the complete first-transition degeneracy polynomial is
\[
F_2(z)=234z^8+552z^9+444z^{10}+144z^{11}+18z^{12}
=6z^8(z+1)(3z^3+21z^2+53z+39).
\]
At \(h=4\), all independent sets of \(G\), considered as down-spin sets, are ground states. Their already-published independence polynomial gives \(13,875\) configurations. That previously tabulated polynomial and this derived high-field count are **not claimed as novel**. For negative fields, global spin reversal gives \(E_0(-h)=E_0(h)\) and reverses all magnetizations.

## Assumptions and scope
The graph has vertices \((p,\varepsilon)\) with \(p\in\{0,1,2\}\) and \(\varepsilon\in\{-1,1\}^3\). Two vertices are adjacent if (i) their signs agree and their indices differ, or (ii) their indices agree and their signs differ in exactly one coordinate other than that index. This is the graph obtained from all coordinate permutations and independent signs of \((1,1,1+\sqrt2)\), connecting pairs at Euclidean distance two. Case (i) gives eight vertex-disjoint triangles, each on the three vertices with fixed \(\varepsilon\); case (ii) gives six disjoint four-cycles, on which all other edges lie. The graph is four-regular. The Hamiltonian uses exchange coefficient \(+1\), *not* the \(-J\) ferromagnetic convention or spin variables \(\pm\tfrac12\). All numbers above are for finite 24 spins, zero temperature and equal couplings. An external field \(h\ge0\) favors plus spins.

## Proof
**Sector bound.** Let \(S=\{v:\sigma_v=-1\}\), \(k=|S|\), and \(e(S)\) be the number of edges induced by \(S\). Since \(G\) is four-regular,
\[
M=24-2k,\qquad E(\sigma):=\sum_{uv}\sigma_u\sigma_v=48-8k+4e(S).
\]
Write \(t_{\varepsilon}=|S\cap T_{\varepsilon}|\) for the eight disjoint triangles. Each induces \(\binom{t_{\varepsilon}}2\) edges. Therefore, for every \(S\),
\[
e(S)\ge\sum_{\varepsilon}\binom{t_{\varepsilon}}2\ge\sum_{\varepsilon}(t_{\varepsilon}-1)=k-8,
\qquad e(S)\ge0.
\]
**Sharpness in every nonnegative magnetization sector.** Set \(\chi(\varepsilon)=\varepsilon_0\varepsilon_1\varepsilon_2\) and \(\sigma_{(p,\varepsilon)}=\chi(\varepsilon)t_p\) with \((t_0,t_1,t_2)=(+1,+1,-1)\). Every nontriangle edge is antiparallel, and each triangle contains both signs. This is a \(k=12\) configuration, inducing exactly \(4\) down–down edges, all within its triangles. Choose one down vertex from each triangle to obtain an independent set of cardinality eight. Adding any subset of the four remaining down vertices produces for each \(8\le k\le12\) a set with exactly \(k-8\) induced triangle edges and no induced external edge. For \(0\le k\le8\), choose a subset of the eight-element independent set. Hence for \(0\le k\le12\),
\[
\min_{|S|=k}e(S)=\max(0,k-8),\quad
\min_{M\ge0\text{ fixed}}E=\begin{cases}-32+2M,&0\le M\le8,\\-48+4M,&8\le M\le24,\end{cases}
\]
where \(M\) ranges over even integers. For \(h>0\), a minimizer cannot have negative magnetization, by global spin reversal. Taking the lower envelope of the sector energies minus \(hM\) proves the stated thresholds and magnetizations. At \(h=0\), the sole minimizing magnetization is zero.

**Complete critical manifolds.** The exact identities
\[
\mathcal H_{2}(S)=4(e(S)-k),\qquad \mathcal H_{4}(S)=-48+4e(S)
\]
show that \(h=4\) ground states are exactly independent sets. At \(h=2\), equality at energy \(-32\) holds exactly when every triangle has one or two vertices in \(S\) and no nontriangle edge has both endpoints in \(S\). Indeed, \(\binom t2=t-1\) only for \(t=1,2\). Because the six nontriangle four-cycles are vertex-disjoint, an independent set on this external-edge subgraph has at most 12 vertices, giving precisely \(8\le k\le12\) for the first-transition ground states.

**Exact multiplicity certificate.** Enumerate independently the \(6^8\) ways to choose one or two down vertices per triangle and reject choices occupying both ends of an external edge. Counting by \(k\) gives, in increasing order \(k=8,9,10,11,12\), exactly
\[
234,\ 552,\ 444,\ 144,\ 18.
\]
This finite set is explicitly exhaustive because every \(h=2\) ground state satisfies and is uniquely specified by one of these choices. At \(h=0\), every triangle must have one frustrated internal edge and every nontriangle edge must be antiparallel. The latter conditions force alternating spins on each of six disjoint external four-cycles, leaving \(2^6=64\) possibilities. Exactly 18 give nonmonochromatic spins on all eight triangles. The field-four independent sets are independently enumerable by at most one down vertex per triangle, namely \(4^8\) possibilities, producing the known size distribution \(1,24,228,1104,2940,4368,3536,1440,234\) for \(k=0,\ldots,8\). These are finite, complete combinatorial counts, not stochastic samples or extrapolations; accompanying code implements both the constrained counts and an independent exhaustive full-spin Hamiltonian check.

## Verification
Run `python3 verify.py` with Python 3.10 or later. It constructs the graph from sign-label adjacency, asserts its 24 vertices, 48 edges, eight triangles and 24 nontriangle edges, enumerates every admissible first-transition and independent-set state, and checks the zero-field signed-cycle count. For a separate unrestricted 24-spin enumeration, compile `full_spectrum.cpp` with a C++17 compiler and run the executable. That program constructs adjacency from the sign-label rule and traverses all \(2^{24}\) Ising states by Gray code, recording the minimum energy and its multiplicity in every magnetization sector. Its expected output is asserted internally rather than inferred from a Monte Carlo run. A replay from these two standalone files agrees on every claimed multiplicity.

## Relationship to prior work
Frustrated finite magnetic polyhedra and their field-dependent magnetization have been studied, for example, by Schmidt, Richter and Schnack (2005) for quantum Heisenberg spins on the cuboctahedron and icosidodecahedron. Timonin (2010) analyzes Ising field plateaux and entropy features on the infinite triangular Husimi lattice, and Yu (2016) studies two-dimensional Archimedean *tilings*. None of those specific results determines the finite four-regular rhombicuboctahedral Ising ground-state counts.

A previously published computation of the small rhombicuboctahedral **independence complex** lists all independent-set coefficients, exactly matching the field-four critical polynomial. Accordingly the high-field value \(13,875\) and the independence coefficients are prior knowledge, not the originality claim. The additional first-transition polynomial, zero-field multiplicity, and full nonnegative-field staircase require the separate mixed triangle/external-edge constraints proved here. Related exact Ising phase diagrams for triangle expansions of cubic graphs concern degree-three graphs with one external edge per triangle vertex; this graph has degree four and two external edges per triangle vertex, so those graph-specific theorems do not imply this critical counting result. Coincident threshold values after coupling substitution are not graph or ground-state equivalence.

## Limitations
The theorem concerns one canonical finite polyhedral graph, unit exchange and uniform longitudinal fields. It does not calculate finite-temperature thermodynamics, quantum Heisenberg energies, unequal-edge couplings or any thermodynamic-limit phase transition. The transition multiplicities are exact finite enumerations accompanying an analytic sector-minimum proof. Published independence-set counts already cover the field-four polynomial. Unindexed historical papers and other equivalent graph formulations may still affect priority; an independent scientific audit has not been performed.

## References
1. R. Schmidt, J. Richter and J. Schnack, *Frustration effects in magnetic molecules*, arXiv:cond-mat/0501376, first posted 2005-01-17, https://arxiv.org/abs/cond-mat/0501376.
2. P. N. Timonin, *Thermodynamics of strongly frustrated magnet in a field: Ising antiferromagnet on triangular Husimi lattice*, arXiv:1005.2650, first posted 2010-05-15, https://arxiv.org/abs/1005.2650.
3. U. Yu, *Ising antiferromagnet on the Archimedean lattices*, arXiv:1606.08191, first posted 2016-06-27, https://arxiv.org/abs/1606.08191 (two-dimensional tilings, not the finite solid).
4. *Integral sphere-wedge homotopy of the small rhombicuboctahedral independence complex*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-integral-sphere-wedge-homotopy-of-the-small-rhombicuboctahedral--babf3ae259ef. Its face counts already provide the graph's independence polynomial.
5. *Rhombicuboctahedron*, Polyhedra Viewer, https://polyhedra.tessera.li/rhombicuboctahedron/info (graph size and face incidences).
