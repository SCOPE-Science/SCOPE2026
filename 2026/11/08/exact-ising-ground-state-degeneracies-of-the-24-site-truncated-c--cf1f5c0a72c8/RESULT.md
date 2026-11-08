# Exact Ising ground-state degeneracies of the 24-site truncated cube

## Finding

For the 24-site truncated-cube Ising antiferromagnet with distinct positive intratrimer coupling \(J\) and intertrimer coupling \(K\), the complete **labeled zero-temperature ground-state degeneracy** at nonnegative external field \(h\) is

\[
\Omega(h)=\begin{cases}
450,&0\le h<K,\\
11682,&h=K,\\
828,&K<h<K+2J,\\
26441,&h=K+2J,\\
1,&h>K+2J.
\end{cases}
\]

At the first critical field the individual counts by total magnetization \(M\) are \(450,2520,4572,3312,828\) at \(M=0,2,4,6,8\). At the second they are \(828,4272,8056,7632,4092,1296,240,24,1\) at \(M=8,10,12,14,16,18,20,22,24\). For negative \(h\), global spin reversal gives the same degeneracies and reverses all magnetizations.

The three energy branches, their breakpoints and the strict-region magnetizations are consequences of a more general triangle-expansion ground-state characterization and are **not claimed as new** here. The contribution is the exact, graph-specific degeneracy and critical-field magnetization-count classification, including its reproducible independent enumeration.

## Assumptions and scope

Let the cube graph be \(Q_3\) with vertex set \(\{0,1\}^3\). Replace every base vertex \(u\) by a triangle of three spin sites \((u,v)\), one for every cube neighbor \(v\). Connect sites within the same triangle (24 internal edges overall), and also join \((u,v)\) and \((v,u)\) for every base edge (12 external edges overall). This is the 24-vertex truncated-cube graph.

For every \(J,K>0\), \(h\in\mathbb R\), and spin assignment \(s_{u,v}\in\{-1,+1\}\), set
\[
H(s)=J\sum_{\rm internal\ edges} s_is_j+K\sum_{\rm external\ edges}s_is_j-h\sum_{i=1}^{24}s_i.
\]
The ground-state degeneracy counts distinct assignments of all 24 labeled spins, without quotienting by graph automorphisms or spin reversal. The statements concern an isolated finite classical cluster at zero temperature, not a thermodynamic transition or the quantum Heisenberg Hamiltonian of an experimental material.

## Proof

Write \(k\) for the number of plus spins, \(c_i\) for the number of unlike-spin internal edges, and \(c_e\) for the number of unlike-spin external edges. Directly from the graph's 24 internal and 12 external bonds,
\[
H=24J+12K-2Jc_i-2Kc_e-h(2k-24).
\]
The three-branch ground energy, already implied by the standard triangle-expansion characterization, is
\[
E_0(h)=\begin{cases}
-8J-12K,&0\le h\le K,\\
-8J-4K-8h,&K\le h\le K+2J,\\
24J+12K-24h,&h\ge K+2J.
\end{cases}
\]
For strict low field, each external edge is antialigned and every internal triangle contains both signs. Choosing which endpoint is plus on each of the 12 base-cube edges gives an orientation of that edge. The triangle condition is exactly that no cube vertex be a source or a sink. Checking all \(2^{12}=4096\) orientations gives precisely \(450\) valid ones. For strict intermediate field, each triangle has exactly one minus spin and no external edge has both endpoints minus. Thus the states are the choices of one of three ports at each cube vertex, excluding reciprocal port choices. An independent exhaustive search of \(3^8=6561\) choices gives \(828\).

At \(h=K\), each triangle has one or two minus spins and no external edge has two minus endpoints. These are the locally constrained choices from the six nonempty proper subsets of three ports. A \(6^8\)-choice integer enumeration with early pruning yields the counts \(450,2520,4572,3312,828\) at \(k=12,13,14,15,16\), respectively, whose sum is \(11682\).

At \(h=K+2J\), the minus spins form an independent set of the full 24-vertex graph, so each cube-vertex triangle has zero or one minus port and no external edge has two minus endpoints. An independent \(4^8\)-choice enumeration gives, for \(k=16,17,\ldots,24\), counts \(828,4272,8056,7632,4092,1296,240,24,1\); the sum is \(26441\). Above that field the all-plus state is uniquely optimal.

All counts are exact nonnegative integers. The independent, full-state enumeration described below verifies that no excluded configurations attain the ground-state energy for any of the five cases. The ground-energy envelope above follows from the triangle/link bond inequalities and realizability on the cube, and is used here only to locate the relevant equality manifolds; the graph-specific counting is the assessed statement.

## Verification

Two separate complete enumerations are provided. `scan2.cpp` iterates all \(2^{24}=16,777,216\) spin configurations with Gray-code updates and records the complete joint histogram of \((k,c_i,c_e)\) into `hist2.csv`. This table has 539 nonzero entries, its counts sum to \(16,777,216\), and direct minimization using the energy identity returns the stated degeneracies, including at \((J,K)=(1,1),(1,3),(3,1),(1,7)\).

`verify_degeneracies.py` does not use `hist2.csv`: it independently enumerates orientations and constrained local port choices for each ground-state manifold, reproducing the exact sector counts. To replay, compile and execute `scan2.cpp` with a C++17 compiler and run `python3 verify_degeneracies.py` with Python 3.8 or later. No randomized computation, floating-point tolerance, external network access or nonstandard library is necessary for the counting certificate.

## Relationship to prior work

Krawczyk and collaborators (first posted 20 December 2004) study Ising frustration on the infinite Archimedean \((3,12^2)\) lattice. Strečka, Karľová and Madaras (first posted 16 February 2015) study magnetic-field effects on Platonic-solid Ising graphs. Neither investigated the isolated truncated-cube graph's two-coupling critical-field degeneracy table. Dreier and collaborators (2018) report physical 24-spin truncated-cube clusters consisting of eight magnetic trimers in boleite, with a quantum Hamiltonian rather than the classical Ising counting problem; only its abstract and accessible contextual material, not its full article, were inspected.

The energy envelope and ground-manifold characterizations for triangle expansions of cubic graphs are not independently new. Moreover, the count at the upper critical field is also an evaluation of the truncated cube's independence polynomial, so any earlier explicit independence-set enumeration would already cover that component. The scope claimed here is the complete magnetization-resolved Ising degeneracy profile on this particular physically motivated finite graph.

## Limitations

This is an exact finite-cluster result, not an infinite-volume assertion. No quantum-spin conclusion, thermodynamic phase transition or experimental material parameter estimate is established. The general phase boundaries and characterization are prior structural information, not a novel theorem here. The original 2018 quantum-magnetism article was not available in full text for comparison, and additional unindexed exact tables may exist. No independent scientific audit has been performed.

## References

- M. J. Krawczyk et al., *Spin glass properties of an Ising antiferromagnet on the Archimedean \((3,12^2)\) lattice*, arXiv:cond-mat/0412545 (first posted 2004-12-20), https://arxiv.org/abs/cond-mat/0412545.
- J. Strečka, K. Karľová, A. Madaras, *Giant magnetocaloric effect, magnetization plateaux and jumps in frustrated antiferromagnetic Ising small spin clusters*, arXiv:1502.04449 (first posted 2015-02-16), https://arxiv.org/abs/1502.04449.
- E. S. Dreier et al., *24-spin clusters in the mineral boleite*, Phys. Rev. B **97**, 014416 (2018), https://doi.org/10.1103/PhysRevB.97.014416.
