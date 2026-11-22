# Integral two-sphere wedges from two-letter de Bruijn overlap graphs

## Finding

For every integer \(q\ge 2\), let \(A\) be an alphabet with \(|A|=q\). Define a **simple undirected** graph \(B_q\) whose vertices are the ordered two-letter words \((a,b)\in A^2\), and in which **distinct** words \((a,b)\) and \((c,d)\) are adjacent precisely when \(b=c\) or \(d=a\). Thus directed overlaps are symmetrized, self-loops are discarded, and any parallel edges are merged. Let \(X_q\) be the clique (flag) complex of this simple graph. Then

\[
X_q\simeq \bigvee^{\frac{(q-1)(q-2)(2q-3)}{6}}S^2.
\]

A wedge of zero spheres means a contractible space. In particular \(X_2\) is contractible, \(X_3\simeq S^2\), and every integral homology group is torsion-free. This is a full homotopy classification, not just a field-rank calculation.

## Assumptions and scope

The graph is the loopless undirected **simple** shadow of the order-three de Bruijn digraph (under a convention counting vertices as words of length two). Its vertices are **all** \(q^2\) words, including repeated-letter words. The result does not assert the same homotopy type for a directed flag complex, the original directed multigraph, higher word lengths, or a graph built from an observed subset of words.

## Proof

**1. Every flag simplex has dimension at most two.** Write \(v_{ab}\) for the word \((a,b)\), and \(h_a=v_{aa}\) for its diagonal word. The neighbors of \(h_a\) are precisely the \(2(q-1)\) words \(v_{xa}\) and \(v_{ay}\) with \(x,y\ne a\). No two distinct incoming words are adjacent, nor are two distinct outgoing words. Every incoming word is adjacent to every outgoing word. Hence all triangles containing \(h_a\) are exactly \(\{h_a,v_{xa},v_{ay}\}\) with \(x,y\ne a\), and there is no four-clique through \(h_a\).

Consider two distinct off-diagonal adjacent words \(v_{ab},v_{bc}\), with \(a\ne b\ne c\). If \(a\ne c\), their only common neighbors are \(h_b\) and \(v_{ca}\): this follows by resolving the two adjacency disjunctions \((x=b\text{ or }y=a)\) and \((x=c\text{ or }y=b)\). The two common neighbors are not adjacent. If \(a=c\), the pair is a two-cycle \(v_{ab},v_{ba}\); a common neighbor off the diagonal would have to coincide with one of these words, and its only distinct common neighbors are \(h_a,h_b\), which are not adjacent. Thus every triangle not containing a diagonal word is exactly a cyclic triple \(\{v_{ab},v_{bc},v_{ca}\}\) with \(a,b,c\) pairwise distinct, and no triangle extends to a four-clique. There are two such triangles for each unordered three-element alphabet subset.

**2. The diagonal-star subcomplex is the complete graph up to homotopy.** For each letter \(b\), let \(C_b\subset X_q\) consist of all triangles containing \(h_b\) and their faces, together with the cone point itself. It is the cone \(h_b * K_{q-1,q-1}\) (the complete bipartite graph here is regarded as a one-dimensional simplicial complex), so it is contractible. For distinct \(a,b\), the intersection \(C_a\cap C_b\) is exactly the single edge with endpoints \(v_{ab},v_{ba}\); no three distinct cone subcomplexes meet. The nerve theorem applied to \(U_q=\bigcup_{b\in A}C_b\) therefore gives

\[
U_q\simeq K_q,
\]

where the right side is the one-dimensional complete graph on the alphabet, not its filled clique complex. This applies also to \(q=2\).

**3. Each remaining triangle fills a fundamental triangle of that complete graph.** The full complex is obtained by attaching the \(2\binom q3\) external cyclic triangles to \(U_q\). For \(\tau_{abc}=\{v_{ab},v_{bc},v_{ca}\}\), its three boundary edges lie, respectively, in the cones \(C_b,C_c,C_a\), while its three vertices lie in pairwise cone intersections \(C_a\cap C_b\), \(C_b\cap C_c\), \(C_c\cap C_a\). Under the nerve equivalence, its attaching loop traverses the ordinary triangular loop \(a-b-c-a\) of \(K_q\). The reverse cyclic triple supplies another 2-cell on this same loop with opposite orientation. This identification can also be seen by connecting each intersection-edge midpoint to the corresponding cone center: each boundary edge contracts inside its containing cone to the two center-to-midpoint paths. Replacing the subcomplex \(U_q\) by its nerve in this homotopy pushout does not change the homotopy type of the resulting CW complex.

Consequently \(X_q\) is homotopy equivalent to a CW complex with the one-skeleton \(K_q\) and **two** 2-cells attached along the triangular boundary for each unordered triple of letters. Keeping one cell per triple yields the complete two-skeleton of the \((q-1)\)-simplex, so the CW complex is simply connected for \(q\ge3\). At \(q=2\) it is an interval and hence contractible. For \(q\ge3\), the integral cellular \(\partial_2\)-image equals the full cycle lattice \(\ker\partial_1\) of \(K_q\), because triangle boundaries through one fixed root span every integral graph cycle. This is a primitive lattice of rank \(\binom{q-1}{2}\). The free rank of \(C_2\) is \(2\binom q3\), giving

\[
\widetilde H_2(X_q;\mathbb Z)\cong
\mathbb Z^{2\binom q3-\binom{q-1}{2}}
=\mathbb Z^{\frac{(q-1)(q-2)(2q-3)}6}.
\]

All other reduced integral homology groups vanish, and the group above is torsion-free. A simply connected CW complex of dimension two is homotopy equivalent to a wedge of two-spheres: by Hurewicz, choose spherical representatives of a free integral basis of \(H_2\), form the corresponding wedge map, and apply Whitehead's theorem. This finishes the all-\(q\) homotopy proof.

## Verification

The separate `verify_debruijn.py` script constructs the overlap graph from its defining predicate, independently enumerates every clique through dimension four, partitions triangles into cone and cyclic classes, checks the exact face counts, and reduces both simplicial boundary matrices over \(\mathbb F_2\). For every \(2\le q\le8\), the observed mod-two Betti numbers are \((1,0,b(q))\). The computed face-vector formulas are

\[
(f_0,f_1,f_2)=\left(q^2,\frac{q(q-1)(2q+1)}2,\ q(q-1)^2+2\binom q3\right).
\]

No four-clique was found in these exhaustive finite checks. These computations independently corroborate the explicit algebraic argument; they are not used to infer the unbounded assertion or integral torsion-freeness.

Run `python3 verify_debruijn.py` with only the Python 3 standard library. Exact recorded output is in `verification_output.txt`.

## Relationship to prior work

Philippakis, Mallinar, Pandit and Belkin (arXiv:2410.07622; first public 2024-10-10) investigate the Laplacian and the ordinary **graph cycle space** of directed/undirected de Bruijn graphs, presenting word-space and graph-operator constructions. Their cycle-space dimension concerns the one-dimensional graph before triangle filling, whereas this result classifies the full homotopy of a specified **simple-graph flag complex**; the former does not determine \(\pi_1\), \(H_2\), or the homotopy type after filling every clique triangle. Their notation calls the length-two-vertex graph order three. Standard good-cover nerve theorems and cellular topology are used as proof tools, not claimed as new. Targeted searches located no earlier all-alphabet statement with the above exact simple-graph object and sphere multiplicity; this is not an assertion of exhaustive novelty.

## Limitations

The complete classification applies only to the loopless simple undirected two-letter overlap graph and its clique complex. It does not classify the chain complex retaining parallel directed arrows, the directed flag complex, or longer word-overlap graphs. Search-based novelty assessment cannot rule out unindexed equivalent literature. Finite verification covers only \(2\le q\le8\); the infinite and integral statements rest on the proof above.

## References

1. A. Philippakis, N. Mallinar, P. Pandit, M. Belkin, *Eigenvectors of the De Bruijn Graph Laplacian: A Natural Basis for the Cut and Cycle Space*, arXiv:2410.07622 (first public 2024-10-10), https://arxiv.org/abs/2410.07622.
2. Standard simplicial nerve theorem and the cellular Hurewicz–Whitehead method (background results, used in their classical forms).
