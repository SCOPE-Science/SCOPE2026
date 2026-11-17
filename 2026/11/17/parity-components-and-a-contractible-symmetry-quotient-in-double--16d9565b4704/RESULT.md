# Parity components and a contractible symmetry quotient in doubles of joined polygon boundaries

## Finding
For every pair of integers \(m,n\ge4\), let \(C_m\) and \(C_n\) be **unfilled** simplicial cycles, and let \(X_{m,n}=C_m*C_n\) be their abstract simplicial join. Thus \(|X_{m,n}|\cong S^3\). Let \(D^2(X_{m,n})\) be the simplicial double: its vertices are the two-element faces of \(X_{m,n}\), and two such vertices are adjacent if they are disjoint and their union is a face of \(X_{m,n}\). The double has no faces of dimension greater than one.

There is a natural **graph isomorphism**
\[
\boxed{D^2(X_{m,n})\cong K_{m,n}\;\sqcup\;(C_m\times C_n),}
\]
where \(\times\) is the **categorical/direct graph product**, not the Cartesian product. The first component is complete bipartite. The second is a connected graph when at least one of \(m,n\) is odd, and consists of exactly two connected graphs when both are even.

In particular, if at least one parameter is odd, the complete **integral homotopy type** is
\[
\boxed{|D^2(X_{m,n})|\simeq
 \left(\bigvee^{(m-1)(n-1)}S^1\right)
 \sqcup\left(\bigvee^{mn+1}S^1\right).}
\]
If both parameters are even, it is
\[
\boxed{|D^2(X_{m,n})|\simeq
 \left(\bigvee^{(m-1)(n-1)}S^1\right)
 \sqcup\left(\bigvee^{mn/2+1}S^1\right)
 \sqcup\left(\bigvee^{mn/2+1}S^1\right).}
\]
The first Betti number is \(2mn-m-n+2\) in the first case and \(2mn-m-n+3\) in the second. The corresponding reduced zeroth Betti numbers are respectively one and two. All integral homology is torsion-free and vanishes in dimensions at least two.

Let \(G=D_m\times D_n\), with each dihedral group acting by rotations and reflections on its corresponding cyclic factor and therefore on the double. The **actual geometric quotient**, not merely the orbit graph obtained by forgetting edge inversions, satisfies
\[
\boxed{|D^2(X_{m,n})|/G\ \cong\ [0,1]\sqcup[0,1].}
\]
In particular its two components are contractible for all \(m,n\ge4\), even though the double has arbitrarily large first Betti number.

## Assumptions and scope
An unfilled \(C_k\) is the one-dimensional simplicial complex on \(\mathbb Z/k\mathbb Z\) with edges \(\{i,i+1\}\), indices taken modulo \(k\), and **no filled triangular face**. The vertex sets of the two cycles are disjoint. A face of their join is a union of a face of each. The double uses the Lesh–Schreiner–Wahl definition with pairwise disjoint edges whose union is a simplex. Write \(K_{m,n}\) for the complete bipartite graph with shores of sizes \(m,n\), and let the categorical product have vertices \((i,j)\) and edges \((i,j)\sim(i',j')\) exactly when \(i\sim i'\) in \(C_m\) and \(j\sim j'\) in \(C_n\). Graphs are regarded as one-dimensional CW complexes. The full automorphism group of \(X_{m,n}\) is **not** asserted to equal \(G\); only the specified factor-preserving action and its quotient are classified.

## Proof
**1. Exact double graph.** Label the first cycle by \(i\in\mathbb Z/m\mathbb Z\) and the second by \(j\in\mathbb Z/n\mathbb Z\). Every edge of the join belongs to exactly one of three classes: one of the \(m\) cycle edges in the first factor, one of the \(n\) cycle edges in the second, or a cross edge \(\{i,j\}\), where the two labels lie in different factors. Hence the double has \(m+n+mn\) vertices. Each tetrahedral facet of the join consists of an edge \(\{i,i+1\}\) and an edge \(\{j,j+1\}\) from the other factor. Its three partitions into two disjoint pairs produce exactly the following double edges: (a) an edge between its two within-factor cycle edges; (b) an edge from cross pair \((i,j)\) to \((i+1,j+1)\); (c) an edge from \((i,j+1)\) to \((i+1,j)\). There are no other double edges, because any union of two disjoint edges that is a simplex must be one of these tetrahedra. Thus the first class is \(K_{m,n}\), the cross-pair class is exactly \(C_m\times C_n\), and they have no edges between them. The tetrahedra and their three partitions are all distinct, so the double has \(3mn\) edges. Its dimension is one because a three-element face would require six distinct vertices in a simplex of the three-dimensional join.

**2. Connected components.** The complete bipartite graph is connected. The direct product is the graph of simultaneous unit steps on the two cycles and is \(4\)-regular on \(mn\) vertices, hence has \(2mn\) edges. If both cycles are even, their bipartition colors \(i\bmod2\) and \(j\bmod2\) are defined, and the parity \(i+j\bmod2\) is unchanged by any simultaneous step. Both parity classes are nonempty, each with \(mn/2\) vertices. Conversely, within either class, take paths between prescribed endpoints in each cycle. Their lengths have the same parity; inserting backtracks of length two makes them equal, yielding a path in the direct product. Thus exactly two components occur. If at least one cycle is odd, a path between any two vertices in that cycle can be replaced by one of opposite parity by traversing its odd circuit. Backtracks then equalize the lengths of paths in the two factors, so **any two product vertices** are connected. Thus the product has one component in this case.

**3. Integral homotopy.** A connected finite graph with \(v\) vertices and \(e\) edges has homotopy type \(\bigvee^{e-v+1}S^1\), by contracting any spanning tree. The \(K_{m,n}\) component contributes \(mn-(m+n)+1=(m-1)(n-1)\) circles. The connected direct product contributes \(2mn-mn+1=mn+1\) circles; if split into two components, each has \(mn\) edges and \(mn/2\) vertices, hence \(mn/2+1\) circles. This gives every asserted integral homotopy and homology formula, with no extension or torsion ambiguity.

**4. Geometric dihedral quotient.** The product group \(G\) preserves the two blocks of double vertices. On \(K_{m,n}\), it is transitive on each shore and on the edges, and no group element exchanges the two shores. Its geometric quotient is a closed interval. On \(C_m\times C_n\), independent rotations act transitively on vertices, and rotations together with reflection in either factor act transitively on edges. An edge \((i,j)\sim(i+1,j+1)\) is interchanged at its endpoints by the simultaneous reflections \(x\mapsto 2i+1-x\) and \(y\mapsto 2j+1-y\). The quotient of that edge under this reversal is a half-edge, with its vertex-orbit endpoint and its fixed-midpoint endpoint. Because all product vertices and edges form single respective orbits, there is exactly one such half-edge in the quotient. Hence this quotient is also a closed interval. These two graph blocks are not mixed by the factor-preserving action, yielding the claimed disjoint union of two intervals. The edge inversion is essential: collapsing to a naive graph with one orbit-vertex and one orbit-edge would incorrectly suggest a circle.

## Verification
The standalone `verify.py` independently enumerates all tetrahedral facets of \(C_m*C_n\), all double vertices, and all three complementary-pair partitions of each facet. It compares the resulting edge set with the explicit \(K_{m,n}\sqcup(C_m\times C_n)\) formula, checks the full graph component sizes, edge counts and first Betti ranks, and exhaustively checks dihedral vertex/edge orbits and endpoint-inverting symmetries. This covers **49 ordered pairs** with \(3\le m,n\le9\), including all pairs within the claimed \(m,n\ge4\) range there. The observed output in `verification_output.txt` ends `JOIN_CYCLES_DOUBLE_EXACT_PASS (49 ordered parameter pairs)`. Finite tests are corroboration; the proof for arbitrary parameters is Steps 1–4 above.

Run from the directory containing the files using `python3 verify.py`. Only the Python standard library is needed. A nonzero exit indicates that an assertion failed. This verification script does not claim to mechanically certify the infinite-parameter argument.

## Relationship to prior work
Lesh, Schreiner and Wahl introduced simplicial doubling and proved weak Cohen–Macaulay connectivity bounds [1], but their primary paper does not classify joins of two polygon boundaries or the factorwise dihedral orbit space. Their general theorem for a three-dimensional source supplies only the dimension-zero weak Cohen–Macaulay bound. Published calculations of doubles of cyclic four-polytope boundaries [2] also concern simplicial three-spheres, but these are neighborly complexes with complete one-skeleton; for \(m,n\ge4\) the join here lacks diagonals within the cyclic factors and is not a cyclic four-polytope boundary. A published calculation for the join of the boundaries of a tetrahedron and a four-simplex [3] concerns a different six-dimensional source sphere and a two-dimensional double, while the published iterated-tupling composition theorem [4] addresses a different operation. The standard connectivity criterion for a direct product of connected graphs is an ingredient **after** the new double-graph identification, not a pre-existing calculation of that double. The claim is the combined structural identification, complete homotopy classification and true geometric symmetry quotient; it is not a claim that graph-product connectivity or spanning-tree contraction is novel.

## Limitations
The theorem classifies first doubles of joins of two simplicial polygon boundaries for \(m,n\ge4\). It does not classify arbitrary simplicial three-spheres, higher iterated tuples, the full automorphism group in exceptional factor-symmetric cases, or the integral homology representation of \(G\) on first homology. In the quotient statement the group is exactly the **factor-preserving** dihedral product, not necessarily the full source-sphere automorphism group. An equivalent result may exist in unindexed opposite-edge-graph literature. Independent mathematical validation has not been performed.

## References
1. K. Lesh, B. Schreiner, N. Wahl, *The double of a simplicial complex*, arXiv:2506.10436, first posted 2025-06-12, revised 2026, Definition 2.1 and Theorem A. https://arxiv.org/abs/2506.10436
2. *Parity and dihedral homology of the doubled cyclic four-polytope boundary*, publicly indexed mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-parity-and-dihedral-homology-of-the-doubled-cyclic-four-polytope--1160db5d31ae
3. *A 710-sphere double of a join of two simplex boundaries*, publicly indexed mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-710-sphere-double-of-a-join-of-two-simplex-boundaries--c8d692438544
4. *Partition inflation and a composition law for iterated simplicial doubles*, publicly indexed mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-partition-inflation-and-a-composition-law-for-iterated-simplicia--c33689e940ec
