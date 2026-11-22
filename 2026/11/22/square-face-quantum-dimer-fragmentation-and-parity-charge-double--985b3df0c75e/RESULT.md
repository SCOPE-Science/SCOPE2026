# Square-face quantum-dimer fragmentation and parity-charge doublets on the rhombicuboctahedron

## Finding

Consider the 24-vertex small rhombicuboctahedral graph with the 18 square faces as the *only* allowed dimer resonances. Its 1,088 perfect matchings (an enumeration established in earlier literature) form an exact 2,616-edge resonance graph with **69 connected components**. The complete component-size distribution is

| Component order | Number of components | Matching states |
|---:|---:|---:|
| 594 | 1 | 594 |
| 16 | 6 | 96 |
| 14 | 24 | 336 |
| 2 | 24 | 48 |
| 1 | 14 | 14 |
| **Total** | **69** | **1,088** |

For any perfect matching \(M\), let \(\chi_M\in\mathbb F_2^{48}\) be its edge-incidence vector, and let \(B\) be the span of the binary boundary vectors of the 18 square faces. The face boundaries are independent, \(\dim B=18\), and each flip preserves the *linear charge* \([\chi_M]\in\mathbb F_2^{48}/B\). Nevertheless these charges are **not** a complete classification of dynamical connectivity. The 1,088 matchings occupy exactly 35 charge classes, distributed as follows:

| Charge-class order | Number of classes | Resonance components inside each class |
|---:|---:|---|
| 594 | 1 | One component of order 594 |
| 32 | 3 | Two components, each of order 16 |
| 28 | 12 | Two components, each of order 14 |
| 4 | 12 | Two components, each of order 2 |
| 2 | 7 | Two isolated states |

Thus **all 34 non-giant charge classes split into pairs of dynamically disconnected components** despite carrying identical binary face-boundary charges. The full 48-element octahedral group has six component-orbits, of types \((594,1)\), \((16,6)\), \((14,24)\), \((2,24)\), \((1,6)\), and \((1,8)\), where each ordered pair indicates component order and orbit size.

For the face-only uniform Rokhsar–Kivelson Hamiltonian \(H(t,v)\) defined below, the zero-energy ground-state degeneracy is **exactly 69** at \(v=t>0\), and is **exactly 14** when \(v>t>0\). In particular, the frozen states and the resonance-charge obstructions are physically different: many disconnected sectors remain mobile.

## Assumptions and scope

The labeled graph has vertex set \(V=\{(s,i):s\in\{0,1\}^3,\ i\in\{0,1,2\}\}\), where \(s\) is a three-bit word. There are edges between \((s,i)\) and \((s,j)\) for \(i\ne j\), and between \((s,i)\) and \((s\oplus e_j,i)\) for \(j\ne i\). This is the usual small rhombicuboctahedron: equivalently its 24 Euclidean vertices are permutations of \((\pm1,\pm1,\pm(1+\sqrt2))\) with edges of squared length four. It has 48 edges, eight triangular faces, and 18 square faces. A perfect matching comprises 12 graph edges covering each vertex exactly once.

The 18 allowed faces are specified without geometric ambiguity. Six are the cycles on \(\{(s,i):s_i=c\}\) for each coordinate \(i\) and bit \(c\). The other twelve are on \(\{(s,i),(s,j),(s\oplus e_k,i),(s\oplus e_k,j)\}\), where \(i<j\), \(k\) is the remaining coordinate, and the \(i\)- and \(j\)-bits of \(s\) are independently fixed. A move replaces the two occupied opposite edges of one square by its other two edges. There are no triangle moves or other-cycle moves.

Let \(\mathcal M\) denote all perfect matchings and \(\mathcal R\) their undirected face-flip graph. For real \(t>0\) and \(v\ge t\), define the physical Hilbert space with orthonormal basis \(\{|M\rangle:M\in\mathcal M\}\), and the uniform face-only Hamiltonian
\[
H(t,v)=\sum_{\{M,N\}\in E(\mathcal R)}\Big(v(|M\rangle\langle M|+|N\rangle\langle N|)-t(|M\rangle\langle N|+|N\rangle\langle M|)\Big).
\]
Each undirected flip is counted once. In the inequalities and energy assertions, zero means the bottom of this explicitly normalized positive-semidefinite Hamiltonian.

## Proof

**1. Exhaustive finite construction.** Every perfect matching appears once in the following recurrence: for a nonempty uncovered-vertex set \(S\), take its least vertex \(u\), select each available neighbor \(w\in S\) in turn, and recurse on \(S\setminus\{u,w\}\). The empty set has one empty matching. This is a bijection by induction because the partner of \(u\) is unique in each matching. Applying the recurrence to the 24-vertex adjacency described above produces precisely 1,088 distinct matchings, consistent with the previously published matching polynomial [3]. The two embedded programs implement this recurrence using different representations: vertex-pair tuples and 48-bit edge masks.

**2. Exact flip graph and components.** For each matching and each of the 18 expressly specified square faces, a flip exists if and only if symmetric difference with the four face edges is another perfect matching. Both exhaustive programs generate all such transitions, with 2,616 distinct unordered resonance edges. Breadth-first traversal or a disjoint-set computation over all 1,088 states gives the exact five-row component distribution in the Finding table. Because the recurrence exhausts all matchings and the face list exhausts all allowed faces, the result is a complete finite proof, not a sample of configurations. Applying all signed coordinate permutations to matching states and their components gives the six listed symmetry orbits.

**3. Binary charges and their insufficiency.** Each square move changes \(\chi_M\) by the binary vector of that square boundary, so the quotient class modulo \(B\) is constant along every path of moves. Binary row reduction on the explicit 18 by 48 face-edge incidence matrix gives 18 nonzero pivots. Reducing each matching's incidence vector by this echelon basis, then grouping all 1,088 reduced representatives, produces exactly 35 classes with orders \(594,32,28,4,2\) and respective multiplicities \(1,3,12,12,7\). Cross-tabulating each class with the already proven flip components gives respectively \(594\), \(16+16\), \(14+14\), \(2+2\), and \(1+1\). These are exact integer operations on a fully enumerated finite set, reproduced in both standalone programs. The fact that two states share a quotient class means only that their incidence-vector difference is a *formal sum* of face boundaries; it does **not** guarantee a physically legal sequence of alternating face moves. This explains the precise gap between linear conserved charges and kinetic connectivity.

**4. Zero-temperature quantum interpretation.** At \(v=t>0\), each pair contribution is \(t(|M\rangle-|N\rangle)(\langle M|-\langle N|)\). Consequently \(H(t,t)=tL_{\mathcal R}\), the combinatorial graph Laplacian. A finite graph Laplacian has one independent zero vector constant on each connected component, so its zero eigenspace has dimension 69. At \(v>t>0\), every two-by-two edge contribution is positive definite on the span of its endpoint states, with eigenvalues \(v-t>0\) and \(v+t>0\). The common kernel therefore consists precisely of amplitudes supported on matching states of degree zero. There are 14 such frozen states. No claims about the nonzero spectrum or \(v<t\) follow from this argument.

## Verification

Execute `python3 verify_geometry.py` and `python3 verify_independent.py` with Python 3 and the standard library. The first program constructs graph edges, squares, matchings, all legal moves, connected components, all 48 graph automorphisms, and the binary quotient. The second starts from the exact algebraic Euclidean coordinates, reconstructs adjacency from squared distances, independently locates all 18 induced square cycles, and uses separately written matching enumeration, 48-bit transitions, disjoint-set connectivity, and binary elimination. Both programs assert every number claimed above and exit successfully when the checks pass. They supply the complete finite certificate; no numerical approximations or external input tables are used.

## Relationship to prior work

The RK construction and dimer Hilbert space are classical background [1,2]. The 1,088 matching count is present in [3] and is explicitly **not** presented as new. Tratnik and Ye [4] establish general properties of surface resonance graphs, and Wang and Kang [5] prove the general median-graph property of each component under proper sets of even faces. Neither general theorem gives the 69-component size distribution, the 35 linear charge classes, or their sharp pairwise splitting for this particular graph. In particular, the fact that components are median is not part of the originality claim. The full-length fullerene quantum-dimer analysis [6] involves different polyhedral graphs and different permitted moves; its full text was not accessible during this comparison, so it remains a limited historical-priority risk.

The specific contribution is the **full 24-site square-face kinetic sector classification, exact failure of linear charge completeness in 34 doublet classes, and the resulting two exact RK ground-state degeneracies**. These statements are not implied merely by the previously known matching count, nor by the general medianity or induced-cubical theorems.

## Limitations

This is an exact *finite-graph* result. The Hamiltonian is defined on perfectly packed dimers and uses exactly uniform square-face exchange amplitudes and the specified diagonal terms. It is not a derivation of this model from a particular microscopic spin Hamiltonian, nor an assertion about other Archimedean solids, additional plaquette flips, a thermodynamic limit, finite-temperature physics, or \(v<t\). An unindexed prior exact census could affect historical priority. No independent external scientific audit has been performed.

## References

[1] D. S. Rokhsar and S. A. Kivelson, “Superconductivity and the Quantum Hard-Core Dimer Gas,” *Physical Review Letters* **61**, 2376 (1988), https://doi.org/10.1103/PhysRevLett.61.2376.

[2] G. Misguich, D. Serban, and V. Pasquier, “Quantum dimer model with extensive ground-state entropy on the kagome lattice,” arXiv:cond-mat/0302152, first posted 2003-02-07, https://arxiv.org/abs/cond-mat/0302152.

[3] K. Balasubramanian, “Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions,” *Symmetry* **17**, 133 (2025), Table 2, https://doi.org/10.3390/sym17010133.

[4] N. Tratnik and D. Ye, “Resonance Graphs and Perfect Matchings of Graphs on Surfaces,” arXiv:1710.00761, https://arxiv.org/abs/1710.00761.

[5] C. Wang and H. Kang, “A Proof of the Tratnik–Ye Medianity Conjecture of Resonance Graphs on Surfaces,” arXiv:2609.12009, https://arxiv.org/abs/2609.12009.

[6] A. Prahlaadh and R. Ganesh, “Quantum dimer model on fullerenes: resonance, scarring and confinement,” arXiv:2204.01756, https://arxiv.org/abs/2204.01756.
