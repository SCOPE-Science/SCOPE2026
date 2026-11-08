# Complete zero-temperature Ising degeneracies of the icosidodecahedral cage

## Finding

Let \(D=GP(10,2)\) be the 20-vertex dodecahedral graph, whose 30 edges are indexed by \(e\). Its line graph \(L(D)\) is the 30-vertex icosidodecahedral graph. Place Ising spins \(\sigma_e\in\{-1,+1\}\) at the vertices of \(L(D)\). For uniform antiferromagnetic coupling \(J>0\) and longitudinal field \(h\in\mathbb R\), put
\[
H_{J,h}(\sigma)=J\!\sum_{\{e,f\}\in E(L(D))}\sigma_e\sigma_f-h\sum_{e\in E(D)}\sigma_e.
\]
At zero field, the ground energy is \(-20J\) and the *complete magnetization-resolved ground-state polynomial* is
\[
\begin{aligned}
\mathcal G_0(z)={}&1044828+762390(z^2+z^{-2})\\
 &+287370(z^4+z^{-4})+50265(z^6+z^{-6})\\
 &+3150(z^8+z^{-8})+36(z^{10}+z^{-10}).
\end{aligned}
\]
Thus there are exactly \(3{,}251{,}250\) labelled ground states at zero field, with residual entropy \(k_B\log(3{,}251{,}250)\). Here \(z\) grades the integer magnetization \(M=\sum_e\sigma_e\), and the labels on the graph are fixed (not symmetry-quotiented).

The exact zero-temperature field-dependent degeneracies are, with the negative-field cases obtained by spin reversal:

| Field | Ground energy | Ground states and magnetizations |
| --- | --- | --- |
| \(h=0\) | \(-20J\) | \(3{,}251{,}250\) states with polynomial \(\mathcal G_0\) above |
| \(0<h<4J\) | \(-20J-10h\) | \(36\) states, all \(M=10\) |
| \(h=4J\) | \(-60J\) | \(111{,}376\) states: \(\sum_{k=0}^{10}a_k z^{30-2k}\) |
| \(h>4J\) | \(60J-30h\) | one state, \(M=30\) |

At \(h=4J\), \(a_k\) is the exact number of \(k\)-edge matchings in \(D\):
\[
(a_0,\ldots,a_{10})=(1,30,375,2540,10155,24474,34805,27300,10260,1400,36).
\]
In particular \(\sum_{k=0}^{10}a_k=111376\). The \(36\) states in the strict intermediate-field plateau are the already-known perfect matchings; the full zero-field polynomial and saturation-field total are the additional exact enumeration addressed here.

## Assumptions and scope

The statement is about a *finite*, labelled, 30-spin, classical Ising system with uniform nearest-neighbour coupling and a uniform field. The positive coupling \(J\) and signed field \(h\) use the displayed Hamiltonian's normalization: the spins themselves take values \(\pm1\), not \(\pm\frac12\). There are no next-nearest-neighbour interactions, disorder, quantum transverse terms, temperature corrections, or boundary degrees of freedom. The graph is exactly \(L(GP(10,2))\), not an infinite kagome lattice.

## Proof

**1. Triangular decomposition and a sharp bound.** Each vertex \(v\) of the cubic graph \(D\) has three incident edges; their three line-graph vertices form a triangle \(T_v\). Because \(D\) is simple and triangle-free, these twenty triangles partition *all* sixty edges of \(L(D)\), and each spin belongs to exactly two such triangles. The Hamiltonian consequently splits exactly into twenty local terms,
\[
H_{J,h}=\sum_{v\in V(D)}\left[J(\sigma_{e_1}\sigma_{e_2}+\sigma_{e_1}\sigma_{e_3}+\sigma_{e_2}\sigma_{e_3})-\frac h2(\sigma_{e_1}+\sigma_{e_2}+\sigma_{e_3})\right],
\]
where \(e_1,e_2,e_3\) meet at \(v\). The four possible triangle types have energies (all up, two up, one up, all down)
\[
3J-\frac{3h}{2},\quad -J-\frac h2,\quad -J+\frac h2,\quad3J+\frac{3h}{2}.
\]
At \(h=0\), equality in the bound \(H\ge-20J\) holds exactly when every vertex of \(D\) sees both spin signs among its three incident edges. Such assignments exist: a perfect matching provides one minus edge and two plus edges at every vertex. Thus the bound is sharp, and the ground states are precisely the nonmonochromatic-at-every-vertex two-colourings of \(E(D)\).

For \(0<h<4J\), the unique locally minimizing triangle type is two up/one down, so the global minima correspond bijectively to perfect matchings formed by the minus edges. For \(h=4J\), both all-up and two-up/one-down triangles minimize simultaneously: the minus edges must form a matching of arbitrary size (possibly zero). For \(h>4J\), every triangle must be all up. All four lower bounds are attained, proving both the energy expressions and the precise state descriptions. Spin reversal treats negative fields.

**2. Exact zero-field polynomial, without enumerating \(2^{30}\) candidate states.** Let \(A_v\) be the event that the three incident edge-spins at \(v\in V(D)\) are equal. For \(S\subseteq V(D)\), impose all events \(A_v\), \(v\in S\). They generate an equivalence relation \(\sim_S\) on the thirty edge variables by identifying the three edges meeting at every selected vertex. Let \(\mathscr C(S)\) be the resulting components. A component \(C\) must be monochromatic, so its possible contribution to the number of positive edge-spins is either zero or \(|C|\). Inclusion-exclusion therefore gives the *exact identity*
\[
F_D(t)=\sum_{S\subseteq V(D)}(-1)^{|S|}\prod_{C\in\mathscr C(S)}(1+t^{|C|}),
\]
where the coefficient of \(t^k\) counts zero-field ground states with exactly \(k\) positive edge-spins. Direct integer evaluation of these \(2^{20}\) terms yields
\[
F_D(t)=36(t^{10}+t^{20})+3150(t^{11}+t^{19})+50265(t^{12}+t^{18})+287370(t^{13}+t^{17})
+762390(t^{14}+t^{16})+1044828t^{15}.
\]
Since \(M=2k-30\), substitution \(\mathcal G_0(z)=z^{-30}F_D(z^2)\) gives the stated polynomial and total. The complete, bounded integer calculation is specified by the standalone `verify_inclusion_exclusion.cpp`, which constructs each equivalence class with disjoint-set union and multiplies the elementary factors by exact integer polynomial addition. The independent `verify_dfs.cpp` visits all admissible assignments using a local three-edge-completion pruning rule and obtains the *same entire coefficient array*. Neither computation samples; both exhaust the complete finite set. Their exact source and outputs are supplied below.

**3. Exact count at the saturation field.** The all-up or two-up-one-down condition at \(h=4J\) means the set of minus-labelled edges is a matching in \(D\). A matching of size \(k\) has magnetization \(M=30-2k\). A separate exact recursion chooses the least remaining vertex, either leaves it uncovered or pairs it with one of its remaining neighbours, counting every matching *once*. On the dodecahedral graph this yields \((a_0,\ldots,a_{10})\) above and the sum \(111376\), as implemented separately in `verify_inclusion_exclusion.cpp`. There can be no matching of size greater than ten on twenty vertices, proving the degree bound.

## Verification

Two standalone C++17 source files are included: `verify_dfs.cpp` generates \(GP(10,2)\) directly from its cyclic definition, while `verify_inclusion_exclusion.cpp` uses a second 30-edge labeling, verifies its explicit isomorphism to \(GP(10,2)\), evaluates all \(2^{20}\) inclusion-exclusion subsets, and separately recurses through all matchings. Each file verifies every coefficient against the claimed array and aborts on any mismatch. With a C++17 compiler, the commands are:

```
g++ -O2 -std=c++17 verify_dfs.cpp -o verify_dfs
./verify_dfs
g++ -O2 -std=c++17 verify_inclusion_exclusion.cpp -o verify_inclusion_exclusion
./verify_inclusion_exclusion
```

The expected summary lines are `VERIFY_DFS_OK zero_field=3251250 ...` and `VERIFY_IE_OK zero_field=3251250 saturation=111376`. The DFS and inclusion-exclusion procedures use distinct enumeration principles and separately constructed edge labelings. The exact graph identity, local-energy analysis and integer coefficients, rather than a runtime log alone, support the conclusion.

## Relationship to prior work

Rousochatzakis, Läuchli and Mila (2007, arXiv:0711.3231v1, Section III.2.2) identify and count the \(36\) up-up-down one-third-plateau configurations in the icosidodecahedral Ising limit, in bijection with dodecahedral perfect matchings. This known result is used and credited; it does not specify the \(h=0\) mixed-orientation magnetization polynomial or the \(h=4J\) sum over *all* dodecahedral matchings. The same paper primarily analyzes Heisenberg excitations, not the classical full zero-field Ising manifold. Strečka, Karlová and Madaras (2015) calculate uniform-field Ising properties on the five Platonic polyhedra, not the icosidodecahedron, while Žukovič and Bobák (2013) enumerate finite planar triangular clusters with free boundaries, not this spherical cage. Separately, the older dodecahedral proton-ice enumeration counts \(3{,}600{,}000\) admissible **orientations** of edges; edge orientations have opposite incidences at their endpoints and are not the undirected binary edge *labels* counted here. An unindexed exact Ising polynomial, table or equivalent graph-colouring enumeration remains possible.

## Limitations

This is an exact finite-cluster, zero-temperature classification. It does not claim a thermodynamic-limit phase transition, a finite-temperature partition function, a Heisenberg-model prediction, experimentally measurable noise thresholds, or immunity to nonuniform interactions. Counting labelled states differs from counting symmetry orbits. Independent external mathematical validation has not been performed.

## References

- I. Rousochatzakis, A. M. Läuchli and F. Mila, *Highly Frustrated Magnetic Clusters: The kagome on a sphere*, arXiv:0711.3231v1 (first submitted 20 November 2007), especially Sections I, III.2.2, and Appendix A. https://arxiv.org/abs/0711.3231
- J. Strečka, K. Karlová and T. Madaras, *Giant magnetocaloric effect, magnetization plateaux and jumps of the regular Ising polyhedra*, arXiv:1502.04449 (2015). https://arxiv.org/abs/1502.04449
- M. Žukovič and A. Bobák, *Entropy of spin clusters with frustrated geometry*, arXiv:1310.3298 (2013). https://arxiv.org/abs/1310.3298
- M. V. Kirov, *Atlas of Optimal Proton Configurations of Water Clusters in the Form of Gas Hydrate Cavities*, Journal of Structural Chemistry 43 (2002), 790–797, doi:10.1023/A:1022825324222 (for the mathematically distinct oriented-edge ice count).
