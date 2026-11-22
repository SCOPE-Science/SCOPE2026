# The Wagner graph's complete induced-forest filtration and seven-dimensional dihedral homology

## Finding
Let \(W\) be the eight-vertex Wagner graph, also called the Möbius ladder \(M_8\), with vertices \(\mathbb Z/8\mathbb Z\), perimeter edges \(\{i,i+1\}\), and opposite edges \(\{i,i+4\}\), subscripts modulo eight. For \(d\geq 0\), let \(\mathcal F_d(W)\) be the abstract simplicial complex of vertex sets whose induced subgraph is acyclic and has maximum degree at most \(d\). There is a complete integral homotopy classification

\[
\mathcal F_0(W)\simeq S^1,\qquad
\mathcal F_1(W)\simeq S^2,\qquad
\mathcal F_2(W)\simeq \bigvee^7 S^3,\qquad
\mathcal F_d(W)\simeq S^4\quad(d\geq3).
\]

Every consecutive inclusion induces the zero map on positive-degree reduced integral homology. Thus the entire positive-degree integral persistence of the degree filtration has one class born and dying between levels zero and one, one between levels one and two, seven between levels two and three, and one persisting from level three onward, in degrees one, two, three and four respectively.

The dihedral group \(D_8=\langle r,s\mid r^8=s^2=1,\ srs=r^{-1}\rangle\) acts simplicially by \(r(i)=i+1\) and \(s(i)=-i\). On the new seven-dimensional group \(\widetilde H_3(\mathcal F_2(W);\mathbb Q)\), the rational character is the sum of the trivial character and the three distinct two-dimensional **real** irreducible characters:

\[
\chi=1+\chi_{\rho_1}+\chi_{\rho_2}+\chi_{\rho_3},
\]

where \(\chi_{\rho_j}(r^k)=2\cos(\pi jk/4)\) and every reflection has character zero in \(\rho_j\). More precisely as a rational representation this is \(\mathbb Q\oplus W_4\oplus W_2\), where the four-dimensional rational constituent \(W_4\) complexifies to \(\rho_1\oplus\rho_3\) and the two-dimensional rational constituent \(W_2\) complexifies to \(\rho_2\). The stage-three top homology is a one-dimensional character with \(r\) acting as \(-1\) and \(s\) acting as \(+1\). In particular the stage-two homology has precisely one rational class invariant under all dihedral symmetries; the stage-three class is not fully invariant.

## Assumptions and scope
The graph is the **specific** simple cubic graph on labeled vertices \(0,\ldots,7\) with the twelve undirected edges defined above. The empty face is present in every complex but is not counted as a nonempty cell in a discrete-Morse matching. The graph is cubic, so all stages with \(d\geq3\) equal the unrestricted induced-forest complex. Each homotopy equivalence is ordinary, not an equivariant homotopy equivalence. Dihedral statements classify rational homology characters, not integral representation lattices.

## Proof
**Exact face reconstruction.** For each nonempty bitmask \(b\) from \(1\) to \(255\), select exactly the vertices whose bits are set. List the induced graph edges. The subset is a face of \(\mathcal F_d\) exactly when a union-find scan of these edges never closes a cycle and each vertex's induced degree is at most \(d\). This is a finite exhaustive decision procedure on the precisely specified graph, without sampling. The resulting face vectors, starting at the empty face, are:

| Stage | Face vector \((f_{-1},f_0,\ldots)\) |
|---|---|
| \(d=0\) | \((1,8,16,8)\) |
| \(d=1\) | \((1,8,28,32,10)\) |
| \(d=2\) | \((1,8,28,56,58,16)\) |
| \(d=3\) | \((1,8,28,56,66,32)\) |

**Complete acyclic elementary-collapse certificates.** The four bundled JSON certificates each contain a finite ordered list of `collapse` and `critical` operations on the actual face poset. A `collapse` removes a codimension-one pair \((\sigma,\tau)\) in which \(\tau\) is maximal among currently retained faces and \(\sigma\) belongs to no retained face other than \(\tau\) that properly contains it. A `critical` operation removes one currently maximal face. Deleting a maximal face or an elementary-collapse pair preserves downward closure of the remaining face set. The verifier checks every operation against the actual complex and separately checks that the entire directed matched Hasse diagram is acyclic (matched edges upward, all others downward). The signatures of the remaining critical cells, by dimension, are:

\[
\begin{array}{c|c|c}
 d & \text{matched pairs} & \text{critical cells} \\
 0 & 15 & \{0:1,1:1\}\\
 1 & 38 & \{0:1,2:1\}\\
 2 & 79 & \{0:1,3:7\}\\
 3 & 94 & \{0:1,4:1\}
\end{array}
\]

A finite simplicial complex with an acyclic face-poset matching is homotopy equivalent, by discrete Morse theory, to a CW complex with one cell for each critical face. In each case there is precisely one zero-cell and all other critical cells have a single common positive dimension. There are no intervening cells, so every positive cell is attached to a point; hence the resulting CW complex is the claimed wedge of spheres **over the integers and up to homotopy**, not merely mod-two homology. The two new stages require seven three-cells and one four-cell, respectively.

**Persistence.** Face tests are monotone in \(d\), so these are the genuine nested complexes. By the homotopy calculations, for each fixed positive degree, at most one of the four successive stages has nonzero reduced integral homology. Thus every inclusion-induced map in positive-degree reduced homology is zero, and the interval multiplicities asserted in the finding follow. This does not assert that every inclusion is nullhomotopic.

**Dihedral character.** Each of the sixteen displayed permutations preserves the edge set. For such a permutation \(g\), the simplicial Lefschetz number is the alternating sum over every setwise \(g\)-fixed nonempty face, weighted by the sign of its induced vertex permutation. With just one nontrivial positive homology degree \(j\), the trace on \(\widetilde H_j\) equals \((-1)^j(L(g)-1)\). Exhaustive integer signed counts produce, for \(k=0,1,\ldots,7\),

\[
\begin{aligned}
\chi_{\mathcal F_2}(r^k)&=(7,1,-1,1,-1,1,-1,1),\\
\chi_{\mathcal F_2}(sr^k)&=(1,1,1,1,1,1,1,1),\\
\chi_{\mathcal F_3}(r^k)&=(1,-1,1,-1,1,-1,1,-1),\\
\chi_{\mathcal F_3}(sr^k)&=(1,-1,1,-1,1,-1,1,-1).
\end{aligned}
\]

Character orthogonality gives exactly the trivial representation plus the three distinct two-dimensional dihedral irreducibles at degree three. The last two rows give the asserted one-dimensional degree-four character.

## Verification
All certificate files are standalone, use vertex bitmasks, and are bundled with the result: `certificates/stage_0.json` through `certificates/stage_3.json`, `verify.py`, and `verification_output.txt`. Execute `python3 verify.py` with Python 3's standard library. The verifier independently reconstructs the graph and all faces, verifies the complete ordered simplicial collapses and maximal critical removals, topologically sorts the entire directed Hasse diagram to check acyclicity, compares all four face vectors and critical signatures, verifies the nested face inclusions, and enumerates all sixteen signed Lefschetz traces. The supplied recorded output is reproduced by direct execution; it is not itself the proof without the instructions and certificates. The entire computation ranges over all \(2^8\) labeled vertex subsets, so the finite census is exhaustive.

## Relationship to prior work
Carnero Bravo, *The Forest Filtration of a Graph* (first publicly posted July 25, 2023), defines this filtration, studies its general properties, and determines families including cycles, cactus graphs, certain complete multipartite graphs and graph products. The accessible primary work does not classify the Wagner graph's degree-two and unrestricted forest stages. Earlier investigations of higher-independence complexes by Abdelmalek, Deshpande, Goyal, Roy and Singh address chordal graphs and trees, not these two stages of the nonchordal Wagner graph. A publicly available 2026 calculation of two-independence complexes of Möbius ladders already proves \(\mathcal F_1(W)\simeq S^2\) and its dihedral character. Those facts are included here only to make the complete filtration precise: **the new mathematical contributions are the stage-two and unrestricted homotopy types, their filtration consequences, and the dihedral characters of those two stages**. Known ordinary-independence computations are likewise not claimed as new.

## Limitations
This is a complete result for one natural eight-vertex graph, not an infinite-family formula for all Möbius ladders. The finite matching certificates prove integral ordinary homotopy types, but do not supply explicit homotopy equivalences compatible with group actions, nor any integral decomposition of the dihedral homology lattices. Character calculations apply to the explicitly displayed dihedral subgroup. Literature comparisons cannot rule out unindexed or inaccessible equivalent statements; a separate independent scientific audit has not been performed.

## References
1. Andrés Carnero Bravo, *The Forest Filtration of a Graph*, first arXiv version July 25, 2023, arXiv:2307.13271. https://arxiv.org/abs/2307.13271
2. Fred M. Abdelmalek, Priyavrat Deshpande, Shuchita Goyal, Amit Roy, Anurag Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, first arXiv version June 21, 2021, arXiv:2106.10863. https://arxiv.org/abs/2106.10863
3. *Five exact higher-independence homotopy types for Möbius ladders and their dihedral characters*, publicly indexed 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-five-exact-higher-independence-homotopy-types-for-m-bius-ladders--7339638cffe4
4. Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. https://doi.org/10.1006/aima.1997.1650
