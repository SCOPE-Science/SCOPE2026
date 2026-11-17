# The full automorphism character of the Pappus matching complex

## Finding
For the standard Pappus graph \(P\), the forty-dimensional rational group representation on fifth reduced homology of the ordinary matching complex has the **complete character below**. In particular,
\[
\widetilde H_5(\mathcal M(P);\mathbb Q)^{\operatorname{Aut}(P)}=0.
\]
The part-preserving index-two subgroup likewise fixes no nonzero vector. The nonequivariant homotopy equivalence \(\mathcal M(P)\simeq\bigvee^{40}S^5\) is prior work and is not claimed as a new result.

| Class | Size | Order | \(\chi\) | Representative on vertices 0–17 |
|---:|---:|---:|---:|:---|
| 0 | 1 | 1 | 40 | `identity` |
| 1 | 18 | 2 | -4 | `(3 13)(4 12)(5 17)(6 16)(7 9)(10 14)(11 15)` |
| 2 | 9 | 2 | 0 | `(2 8)(3 9)(4 16)(5 17)(6 12)(7 13)` |
| 3 | 36 | 6 | -1 | `(1 5 17)(2 4 16 8 6 12)(3 15 9 7 11 13)(10 14)` |
| 4 | 12 | 3 | 1 | `(1 5 17)(2 6 16)(3 11 9)(4 12 8)(7 15 13)` |
| 5 | 18 | 2 | 4 | `(0 1)(2 5)(3 4)(6 13)(7 12)(8 17)(9 16)(10 15)(11 14)` |
| 6 | 18 | 4 | 0 | `(0 1)(2 5 8 17)(3 6 9 12)(4 7 16 13)(10 11)(14 15)` |
| 7 | 36 | 6 | -2 | `(0 1 2 3 4 5)(6 17 8 13 10 15)(7 12 9 14 11 16)` |
| 8 | 18 | 12 | 0 | `(0 1 2 3 10 11 6 7 14 15 16 17)(4 9 12 5 8 13)` |
| 9 | 12 | 3 | 4 | `(0 2 4)(1 3 5)(6 8 10)(7 9 11)(12 14 16)(13 15 17)` |
| 10 | 18 | 6 | 0 | `(0 2 10 6 14 16)(1 3 11 7 15 17)(4 12 8)(5 13 9)` |
| 11 | 18 | 12 | 0 | `(0 3 6 9 14 17 2 5 10 7 16 13)(1 4 11 8 15 12)` |
| 12 | 2 | 3 | 4 | `(0 10 14)(1 11 15)(2 6 16)(3 7 17)(4 8 12)(5 9 13)` |

Each representative is a permutation in disjoint-cycle notation; omitted vertices are fixed. The class numbering here is only a stable enumeration of the thirteen conjugacy classes, not a group-theoretic name. Since the group is finite and its rational representations are semisimple, this character determines the rational isomorphism class of the homology representation.

## Assumptions and scope
Set \(V(P)=\{0,1,\ldots,17\}\). Add the eighteen cycle edges \(\{i,i+1\pmod{18}\}\) and the edges \(\{i,i+s_i\pmod{18}\}\), where \((s_0,\ldots,s_{17})\) is the threefold repetition of \((5,7,-7,7,-7,-5)\). After deduplication there are 27 edges, all vertices have degree three, and this is the Levi graph of the classical Pappus configuration.

A \(k\)-simplex of \(\mathcal M(P)\) is a set of \(k+1\) edges with pairwise disjoint endpoints. The group \(G=\operatorname{Aut}(P)\) acts by permutation of graph edges and therefore acts on oriented simplicial chains and on reduced rational homology. Orientation is the increasing order of the 27 graph edges in lexicographic order. No choice of a particular orientation affects the trace. The calculation concerns ordinary partial matchings, not the perfect-matching complex or vertex independence complex.

## Proof
**1. Rational homology concentration.** The complete nonempty face counts, by matching size one through nine, are
\[
(27,297,1719,5643,10557,10737,5319,1026,42).
\]
In the augmented simplicial chain complex the exact ranks of successive boundary maps over \(\mathbb F_2\), for simplex dimensions zero through eight, are
\[
(1,26,271,1448,4195,6362,4335,984,42).
\]
The resulting reduced mod-two Betti vector in dimensions zero through eight is \((0,0,0,0,0,40,0,0,0)\), and the reduced Euler characteristic is \(-40\). For each integral simplicial boundary matrix, its rational rank is at least its rank modulo two; therefore each rational Betti number is at most its mod-two counterpart. Rational homology can occur only in degree five, and the rational Euler characteristic forces \(\dim\widetilde H_5=40\). The attached pure-Python verifier reconstructs the face counts and every mod-two rank from the explicit graph, independently of the published nonequivariant homotopy calculation.

**2. Signed Lefschetz formula.** Fix \(g\in G\) and let \(\mathscr O_g\) be the orbits of its permutation on the 27 graph edges. Discard any orbit containing two graph edges sharing a graph vertex, since no matching can contain that orbit in full. For the remaining orbits, call a subcollection admissible when all edges in their union have pairwise disjoint endpoints, and include the empty subcollection. Then
\[
\boxed{\chi(g)=\sum_{J\subseteq\mathscr O_g\,\text{admissible}}(-1)^{|J|}.}
\]
Indeed, a setwise-fixed matching is exactly such a union of edge orbits. If its size is \(m\) and it is a union of \(j\) orbits, the induced oriented simplex has sign \((-1)^{m-j}\) and its contribution to the *reduced* simplicial Lefschetz number is \((-1)^{m-1}(-1)^{m-j}=-(-1)^j\). This also holds for the empty augmented simplex, whose contribution is \(-1\). Since all reduced rational homology lies in odd degree five, the reduced Lefschetz number equals \(-\chi(g)\), giving the formula.

**3. Exhaustiveness and character table.** Enumerating all graph automorphisms by adjacency-preserving bijections produces exactly 216 elements. Composing these permutations and conjugating each element gives thirteen disjoint conjugacy classes, whose sizes total 216. Applying the fixed-edge-orbit formula to all 216 elements gives the thirteen values in the table. As an independent calculation, one can enumerate all 35,367 nonempty matching simplices and sum their signed fixed-face traces directly; this agrees with the orbit formula for every automorphism. The two complete procedures and the class representatives are reproducible from `verify_pappus.py`.

The class sizes and traces yield \(\sum_{g\in G}\chi(g)=0\). By the character average projection, the invariant-subspace dimension is zero. The bipartition-preserving subgroup has 108 elements, and its character sum is also zero, proving the second fixed-space statement. As a consistency check, the exact character norm satisfies \(\langle\chi,\chi\rangle_G=12\), a positive integer.

## Verification
With Python 3.9 or later, run `python3 verify_rational_concentration.py`, which uses only the Python standard library and proves the augmented mod-two boundary-rank data from explicit finite matrices. Install NetworkX 3.x to run `python3 verify_pappus.py`; it constructs the LCF graph, enumerates all 216 automorphisms, evaluates 216 traces by *two separately implemented methods*, and verifies every conjugacy class, class size, fixed-space dimension, and character inner product. The recorded outputs `verify_rational_concentration.stdout` and `verify_pappus.stdout` are included. Both scripts use no input files or internet access. Reproducing a program output is a computational check; the mathematical argument from chain ranks and Lefschetz theory is stated above.

## Relationship to prior work
Shareshian and Wachs study the topology, torsion and symmetric-group representation theory of complete-graph matching complexes \(M_n\) and chessboard complexes \(M_{m,n}\); their full text supplies historical motivation for studying homology representations but no Pappus-graph group character. A published Pappus-specific calculation determines reduced mod-two homology, and a subsequent published result determines the integral homotopy type \(\bigvee^{40}S^5\). Neither determines the automorphism character: different 40-dimensional rational representations of a 216-element group can have different class traces and invariant dimensions.

An existing character calculation for the *vertex* independence complex of the Pappus graph concerns a different simplicial complex. The known full character of the Heawood *matching* complex concerns the different fourteen-vertex Fano incidence graph. Searching the equivalent presentation \(\mathcal M(P)=\operatorname{Ind}(L(P))\), the Pappus Levi-graph name, the Bouwer graph \(B(3,2,3)\), and the honeycomb toroidal graph \(HTG(3,6,3)\) revealed no inspected result covering this 216-element Pappus matching-complex character. These searches are evidence of noncoverage in inspected sources, not a proof of bibliographic uniqueness.

## Limitations
The theorem computes a complete **rational** character for this one finite graph. It does not give an integral \(\mathbb Z[G]\)-lattice decomposition, construct an equivariant sphere-wedge splitting, or classify characters for other incidence graphs. Primary literature and exact published prior computations were compared; publication-priority uncertainty remains for obscure or unindexed equivalent work. The underlying nonequivariant homotopy classification and its rank forty are explicitly acknowledged as prior art.

## References
1. John Shareshian and Michelle L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054, initially posted 2004-09-03. https://arxiv.org/abs/math/0409054
2. *Integral homotopy type of the Pappus graph matching complex*, previously published exact computation. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-integral-homotopy-type-of-the-pappus-graph-matching-complex--db6c6c11f317
3. *Mod-2 homology of the Pappus matching complex*, previously published exact computation. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-mod-2-homology-of-the-pappus-matching-complex--a28326a5f491
4. *Order-three symmetry on Pappus independence homology*, previously published independent-complex computation. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-order-three-symmetry-on-pappus-independence-homology--ea65a5211f31
5. *Full automorphism module of the Heawood matching complex*, previously published equivariant result for a different graph. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-full-operatorname-aut-h-module-of-the-heawood-matching-complex--d7a042784870
6. *Pappus Graph*, Wolfram MathWorld, for the LCF description and graph aliases. https://mathworld.wolfram.com/PappusGraph.html
