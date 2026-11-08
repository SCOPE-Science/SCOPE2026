# Transitive bipartite symmetry forces discrete geometric matching-complex fixed spaces

## Finding
Let \(B=(X\sqcup Y,E)\) be a finite simple bipartite graph with nonempty disjoint shores \(X,Y\). Let a finite group \(G\) act on \(B\) by automorphisms preserving the shores and **transitively on each shore**. Write \(\mathcal M(B)\) for the simplicial matching complex: its vertices are edges of \(B\), and its simplices are collections of pairwise vertex-disjoint edges. The geometric pointwise fixed space \(|\mathcal M(B)|^G\) has the following complete classification.

Set
\[
\mathscr I_G(B)=\{f:X\longrightarrow Y:\ f\text{ is a bijection, } f(gx)=g f(x)\text{ for every }g\in G,x\in X,\text{ and }(x,f(x))\in E\text{ for every }x\in X\}.
\]
Then, naturally as a finite zero-dimensional PL space,
\[
|\mathcal M(B)|^G\cong_{\mathrm{PL}}\coprod_{f\in\mathscr I_G(B)}\{\mathrm{point}\}.
\]
The indexing point is the barycenter of the perfect matching \(\{(x,f(x)):x\in X\}\). In particular, the fixed space is empty for unequal shore sizes and for equal shore sizes when \(\mathscr I_G(B)\) is empty. If it has \(N\ge1\) points, its only nonzero reduced integral homology is \(\widetilde H_0\cong\mathbb Z^{N-1}\).

For the complete bipartite graph \(B=K_{n,n}\) with identical transitive label permutations on the two shores, \(\mathcal M(B)=\Delta_{n,n}\), the square chessboard complex, and
\[
|\Delta_{n,n}|^G\cong_{\mathrm{PL}}\coprod_{c\in C_{S_n}(G)}\{\mathrm{point}\}.
\]
The centralizer of a transitive permutation group is semiregular, so its cardinality is between \(1\) and \(n\). In particular, every regular action gives precisely \(n\) fixed points, whereas a two-transitive action of degree greater than two gives one fixed point.

## Assumptions and scope
The graph is finite, undirected, bipartite and simple, both shores are nonempty, and the group action is side-preserving and separately transitive. Neither connectedness nor faithfulness is required. We mean **fixed points of the geometric realization**; the complex on individually fixed edge-vertices generally gives the wrong answer. A zero-point space means the empty topological space, not a contractible space.

## Proof
1. **Invariant barycentric supports.** Each point of a simplicial realization has unique strictly positive barycentric coordinates on its support simplex. If the point is fixed by all of \(G\), its support is a \(G\)-invariant nonempty matching and its coefficients are constant on every edge-orbit. Conversely, a barycenter of any admissible edge-orbit is fixed.

2. **Size obstruction.** Let \(O\subseteq E\) be an edge-orbit under \(G\). By transitivity on both shores, the first and second coordinate projections of \(O\) are all of \(X\) and \(Y\). If \(O\) is a matching, its two projections are injective. Surjectivity and injectivity imply \(|O|=|X|=|Y|\). In particular unequal shore sizes prohibit every invariant nonempty matching, hence the fixed-point set is empty.

3. **Equivariant bijections.** If \(O\) is an admissible edge-orbit, define \(f(x)\) to be the unique \(y\) with \((x,y)\in O\). Invariance of \(O\) gives \(f(gx)=gf(x)\), so \(f\in\mathscr I_G(B)\). Conversely, the graph of any \(f\in\mathscr I_G(B)\) is a matching and is a **single** orbit: given \(x,x'\), transitivity sends \((x,f(x))\) to \((x',f(x'))\).

4. **No higher-dimensional fixed cells.** Every admissible edge-orbit uses every vertex on both shores. Two distinct such orbits cannot coexist in a matching. Consequently, every invariant nonempty matching is exactly one admissible orbit, and its fixed barycentric point is its uniform barycenter. The fixed set is precisely the indicated finite collection of isolated points; the orbit-barycenter model identifies the zero-dimensional PL structures.

5. **Centralizer specialization.** On two identically labeled complete shores, a \(G\)-equivariant bijection is exactly a permutation commuting with every element of \(G\). If \(c\) centralizes a transitive \(G\) and fixes one label \(x\), then for every \(y=gx\) it fixes \(y\), hence \(c=1\). Thus the centralizer acts freely on labels and has order at most \(n\). The identity provides one fixed point, and the homology formula follows from the integral homology of a finite set. For a two-transitive action of degree greater than two, a nonidentity commuting permutation cannot exist: such a permutation would pair each \(x\) with \(cx\neq x\), providing a nontrivial invariant orbital of size \(n\), contrary to two-transitivity of ordered distinct pairs (which have cardinality \(n(n-1)>n\)).

These arguments apply to all finite parameters, not only the cases enumerated by the verifier.

## Verification
The standalone standard-library program `verify.py` generates 28 small shore-transitive group actions (including unequal shores, cyclic actions, full symmetric actions, a regular Klein-four action, and a dihedral action). It checks all 226 invariant bipartite edge sets available in these actions, enumerates **actual invariant rook matchings**, and compares them to admissible edge-orbits and equivariant perfect matchings. There are 421 observed admissible edge-orbits. Separately it checks the centralizer formula through degree six. The exact replay reports `ALL_VERIFY_OK` and `CENTRALIZER_VERIFY_OK`. This is finite corroboration; the all-dimensional proof is above.

## Relationship to prior work
Limonchenko and Yu (2026) give broad homotopy and torsion results for chessboard complexes, including torsion in ordinary square chessboard complexes. The present theorem concerns geometric fixed spaces of separately transitive symmetry groups, which are discrete even when the ambient complex has complicated topology. Lesh, Schreiner, and Wahl (2025) study doubling and connectivity for related matching complexes, but not these transitive fixed spaces. Bate, Everitt, Ford, and Ramos (2023 preprint; published 2026) compute integral symmetric-group representations for matching complexes of complete hypergraphs, a different invariant and complex. Standard orbit-counting or group-centralizer facts alone do not compute geometric fixed spaces until admissible invariant simplices and their intersections are analyzed.

## Limitations
The theorem requires shore-wise transitivity and a side-preserving action. For nontransitive actions, distinct invariant edge-orbits can coexist and fixed spaces can have positive dimension. Actions interchanging the shores are not covered. The theorem does not determine the homotopy type or torsion of the ambient matching complex, nor the homology representations of individual elements.

## References
- I. Limonchenko and S. Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, arXiv:2610.37827v1 (first public 2026-10-27), https://arxiv.org/html/2610.37827v1.
- K. Lesh, B. Schreiner, and N. Wahl, *The double of a simplicial complex*, arXiv:2506.10436 (first public 2025-06-12), https://arxiv.org/html/2506.10436v2.
- M. Bate, B. Everitt, S. Ford, and E. Ramos, *Homology of matching complexes and representations of symmetric groups*, arXiv:2312.13750 (first public 2023-12-21), https://arxiv.org/html/2312.13750v3.
