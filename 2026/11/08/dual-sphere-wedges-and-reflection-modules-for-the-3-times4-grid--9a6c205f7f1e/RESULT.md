# Dual sphere wedges and reflection modules for the \(3\times4\) grid at threshold four

## Finding
Let \(G=P_3\square P_4\), with vertex set \(V=\{(r,c):0\le r<3,0\le c<4\}\) and edges joining vertices at Manhattan distance one. Define the four-robust clique complex \(K=\mathsf{Cliq}_4(G)\) by declaring \(\sigma\subseteq V\) a face exactly when it contains no independent four-set of \(G\). Define the total four-cut complex \(T=\Delta_4^t(G)\) by declaring \(\sigma\) a face exactly when \(V\setminus\sigma\) contains an independent four-set. The latter is the Alexander dual of the former on the same twelve vertices.

There are integral homotopy equivalences
\[
K\simeq\bigvee^{20}S^5,\qquad T\simeq\bigvee^{20}S^4.
\]
Let \(R(r,c)=(2-r,c)\) and \(C(r,c)=(r,3-c)\). They generate the geometric reflection group \(H=\langle R,C\rangle\cong C_2\times C_2\). On the rational top homology of **each** complex, the character in the order \((1,R,C,RC)\) is
\[
\chi=(20,0,-4,0).
\]
Let \(\mathcal Q\) denote the six unit squares in the two-by-three array of elementary grid cells, and let \(\varepsilon_C\) be the one-dimensional character with \(\varepsilon_C(R)=+1\), \(\varepsilon_C(C)=-1\). As rational \(H\)-modules, both top-homology groups are isomorphic to
\[
\varepsilon_C\otimes_{\mathbb Q}\mathbb Q\!\left[{\mathcal Q\choose3}\right].
\]
Here the bracket means the rational permutation space on the twenty unordered triples of distinct unit squares; no geometrically canonical cycle basis is asserted. The four one-dimensional irreducibles \(\chi_{a,b}\), defined by \(\chi_{a,b}(R)=a\), \(\chi_{a,b}(C)=b\) for \(a,b\in\{+1,-1\}\), occur with multiplicities \(5-b\), independently of \(a\).

## Assumptions and scope
The grid is finite, unweighted, simple and contains exactly twelve vertices, numbered by \(v=4r+c\) in row-major order. All simplicial complexes are abstract and include the empty simplex; the finite checker enumerates only nonempty faces and explicitly adds the empty-chain contribution in Lefschetz calculations. The statement concerns ordinary integral homotopy equivalence and rational (not integral) representation isomorphisms. The square triples are indexed by the six unit **faces of the planar grid**, not vertices of \(G\).

## Proof
**Exact face generation.** Every independent four-set is one of the 61 four-subsets with no graph edge among its vertices. The checker enumerates these by iterating over all \(\binom{12}{4}\) possibilities and testing the six possible adjacency pairs. It next enumerates all \(2^{12}-1\) nonempty subsets. For \(K\) it retains exactly those masks containing no one of the 61 forbidden four-masks; for \(T\) it retains exactly those masks disjoint from at least one forbidden four-mask. This is an exhaustive application of the definitions, not sampling. The nonempty face vectors are
\[
(f_0,\dots,f_5)(K)=(12,66,220,434,466,217)
\]
and
\[
(f_0,\dots,f_7)(T)=(12,66,220,495,792,707,326,61).
\]
There are 1,415 and 2,679 nonempty faces, respectively; the program independently tests the Alexander-dual complement relation.

**Exact acyclic Morse matching.** In either face poset, start with all nonempty faces unmatched. For \(v=0,1,\ldots,11\) in order, pair every still-unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever both are still unmatched. Each pair differs in exactly one vertex; a face appears in at most one pair. The algorithm produces 697 pairs for \(K\) and 1,329 pairs for \(T\). The unpaired faces are exactly one vertex and 20 five-simplices for \(K\), and one vertex and 20 four-simplices for \(T\).

For rigorously checking **acyclicity**, form the complete nonempty simplicial Hasse diagram. Orient a cover \(\tau\supset\sigma\) downwards from \(\tau\) to \(\sigma\), except reverse each matched cover to orient upwards. The checker constructs every incidence—6,160 for \(K\) and 13,744 for \(T\)—and performs Kahn's topological-sort algorithm, visiting all 1,415, respectively 2,679, nodes. Therefore neither directed graph has a cycle; the matchings satisfy Forman's acyclic discrete Morse condition. Discrete Morse theory yields CW models with precisely the above critical cells. Since there are no critical positive-dimensional cells below the top dimension, the attaching maps of all top cells are constant into the sole zero-cell. These CW models are exactly wedges of twenty spheres in dimensions five and four, proving both integral homotopy statements. The displayed counts are verified from the package's own standalone program.

**Reflection traces and module.** Each geometric reflection permutes the twelve row-major vertex labels and preserves both complexes. On an invariant nonempty \(j\)-simplex, its signed contribution to the simplicial chain trace is the parity of the induced vertex permutation. The reduced Lefschetz number is
\[
\widetilde L(g)=-1+\sum_{\substack{\varnothing\ne\sigma\in K,\;g\sigma=\sigma}}(-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma),
\]
and similarly for \(T\). The leading \(-1\) is the augmented empty-chain contribution. The checker enumerates all invariant faces and evaluates these signs for each of \(1,R,C,RC\). Since the just-proved reduced homology is concentrated in dimension five for \(K\) and dimension four for \(T\), the homology trace equals \((-1)^5\widetilde L\) for \(K\) and \((-1)^4\widetilde L\) for \(T\). Both computations give \((20,0,-4,0)\).

Finally, the permutation module on unordered triples of the six grid squares has fixed-triple counts \((20,0,4,0)\) under \((1,R,C,RC)\): row reversal exchanges three square-pairs, while column reversal exchanges two pairs and fixes two squares. Twisting by \(\varepsilon_C\) gives \((20,0,-4,0)\). Rational representations of the finite abelian group \(C_2\times C_2\) are determined by their characters, establishing the asserted isomorphisms. The irreducible multiplicities follow by character orthogonality, as \((20-4b)/4=5-b\).

## Verification
Run `python3 verify_grid_robust.py`. It requires only the Python standard library and reconstructs the independent quartets, both complexes, all matched pairs, the entire oriented Hasse diagrams, full acyclicity tests, both face vectors, augmented signed Lefschetz traces and the twisted square-triple model. The package includes the output of the command as `verification_output.txt`. The terminal assertion is `ROBUST_3x4_EXACT_HOMOTOPY_AND_SYMMETRY_OK`. This is a complete *finite* exact verification; it does not assert an infinite-family result or replace the general validity of discrete Morse theory.

## Relationship to prior work
Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs* (first public arXiv version February 11, 2026), Theorem 1, classifies rectangular grids only for \(k=2,3\); Corollary 3 treats all \(k\) only for square sequences constructed solely by edge gluing. Its Conjecture 5 explicitly identifies \(k>3\) with corner gluing as unresolved. A \(3\times4\) grid uses corner gluing. Chandrakar–Hazra–Rout–Singh (arXiv first public August 14, 2024) classify total cut complexes for two-row grids with arbitrary \(k\), and for three-row grids only at \(k=3\); neither theorem gives the present total four-cut homotopy or reflections. Nearby finite calculations for the nine-vertex \(3\times3\) and sixteen-vertex \(4\times4\) grids do not logically imply the present twelve-vertex \(3\times4\) calculation. An equivalent unindexed computation remains possible.

## Limitations
This is a single naturally distinguished twelve-vertex case, not a proof of the conjecture for all grids or all square sequences. The Morse matchings need not be equivariant; rational character equality establishes a module isomorphism but does not construct a canonical integral homology basis or an equivariant homotopy equivalence. Independent verification has not been performed.

## References
1. M. Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365 (first public February 11, 2026), https://arxiv.org/abs/2602.11365. Theorem 1, Corollary 3, Conjecture 5, and the introduction's corner-gluing discussion.
2. H. Chandrakar, N. R. Hazra, D. Rout and A. Singh, *Topology of total cut complexes and cut complexes of grid graphs*, arXiv:2408.07646 (first public August 14, 2024), https://arxiv.org/abs/2408.07646. Theorem 1.1.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (standard discrete Morse theorem).
