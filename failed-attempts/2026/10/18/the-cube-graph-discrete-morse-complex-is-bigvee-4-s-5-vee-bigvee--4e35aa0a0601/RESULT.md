# The cube-graph discrete Morse complex is \(\bigvee^4 S^5\vee\bigvee^{139}S^6\)

## Finding
For the cube graph \(Q_3\), the ordinary complex \(\mathcal M(Q_3)\) of acyclic discrete Morse matchings has the integral homotopy type
\[
\mathcal M(Q_3)\simeq \bigvee^{4}S^5\vee\bigvee^{139} S^6.
\]
In particular its integral reduced homology is free, with rank \(4\) in dimension \(5\) and rank \(139\) in dimension \(6\), and is zero otherwise. This is an exact homotopy classification for this particular graph, not an assertion about all hypercubes.

## Assumptions and scope
The graph \(Q_3\) has vertex set \(\{0,1\}^3\), identified with integers \(0,\ldots,7\) by binary encoding; vertices are adjacent exactly when their encodings differ by \(1\), \(2\), or \(4\) in one bit. Regard this graph as a one-dimensional simplicial complex. A vertex of its ordinary discrete Morse matching complex is a vertex–edge incidence \((u,\{u,v\})\), written \(u\to v\). Faces are pairwise disjoint Hasse incidences whose reversal does not create a directed cycle. Equivalently, a face is a partial orientation of graph edges in which each graph vertex is the tail of at most one arrow and there is no directed cycle. This is **not** the ordinary matching complex of the cube and is **not** the strong-Morse or pure subcomplex.

Number vertices of \(\mathcal M(Q_3)\) by the \(24\) arcs \(u\to(u\mathbin{\mathrm{xor}}2^j)\), ordering \(u=0,\ldots,7\) and then \(j=0,1,2\). A simplex is encoded by a \(24\)-bit mask. Within a simplex, order its arc vertices by increasing index, which fixes its orientation and integral simplicial boundary signs.

## Proof
**Exhaustive face set.** Two exhaustive descriptions agree. First, choose independently for each of the eight graph vertices either no arrow or one of its three neighboring arrow targets and reject directed cycles. Second, independently choose for each of the twelve undirected cube edges one of three states (unused, first orientation, reverse orientation), rejecting duplicated tails and directed cycles. Both yield precisely the same \(23{,}625\) augmented simplices, of dimensions \(-1\) through \(6\) in the counts
\[
(1,24,240,1296,4080,7488,7424,3072).
\]
For an independent counting check the cube Laplacian spectrum is \(0,2,2,2,4,4,4,6\), and the spanning-forest identity gives \(\det(tI+L)=t(t+2)^3(t+4)^3(t+6)\), whose coefficients reproduce the counts.

**Complete discrete-Morse reduction.** On the augmented face poset, inspect the \(24\) arcs in the fixed order above. At each arc, match every still-unmatched face omitting that arc to its coface containing that arc, whenever both are still unmatched. This deterministic procedure gives exactly \(11{,}698\) pairs. The unpaired faces are exactly \(47\) five-simplices and \(182\) six-simplices. The empty simplex pairs with a vertex; removing this pair from the augmented poset leaves the usual one critical vertex, together with the stated positive-dimensional critical cells.

For a rigorous acyclicity test, orient every cover relation from higher to lower face, reversing the arrows precisely on matching pairs. Enumerate every face and every one of its codimension-one subfaces. The resulting directed Hasse graph has \(23{,}625\) nodes and \(124{,}200\) arrows and is exhausted by Kahn's topological-sort algorithm. Thus the matching is acyclic and discrete Morse theory produces a CW model with one zero-cell, \(47\) five-cells and \(182\) six-cells, and no other cells.

**Integral attaching degrees.** Write \(A:\mathbb Z^{182}\to\mathbb Z^{47}\) for the cellular differential from degree six to degree five. For an upper simplex \(\sigma\) and a facet \(\tau\), assign the incidence \((-1)^j\) when deleting its \(j\)-th increasing-order arc. Each paired lower five-simplex contributes a unit cancellation through its paired six-simplex; recursively substituting its other facets gives the integral gradient-path coefficient in every critical five-cell. The included verifier constructs all \(47\times182\) coefficients in two different ways: memoized recursive gradient projection and topological propagation of signed chains. They agree entry by entry. The matrix has \(334\) nonzero entries, all in \(\{-1,1\}\). Its signed-row encoding, with \(-1,0,1\) mapped to bytes \(0,1,2\), has SHA-256 digest `c5d099140b205ee3bc820da7ae1a15884d4571827ae031d129773635bc82fdd2`.

Apply only invertible integral elementary row/column operations: whenever a unit pivot is present, swap it to the next diagonal position, clear its column and row, and continue on the remaining block. Exactly \(43\) such pivots are found. The entire remaining \(4\times139\) block is identically zero. The integral Smith factors of \(A\) are therefore \(43\) copies of \(1\) and no nonunit factors; \(\ker A\cong\mathbb Z^{139}\), while \(\operatorname{coker} A\cong\mathbb Z^4\). All of these claims are checked by the self-contained verifier using integer arithmetic.

**Homotopy, not just homology.** The five-skeleton of the Morse CW model is \(\bigvee^{47}S^5\). Every attaching map of a six-cell lies in \(\pi_5(\bigvee^{47}S^5)\cong\mathbb Z^{47}\) and is uniquely specified by its integral degree column in \(A\); there are no possible higher homotopy corrections in this dimension. Elementary unimodular changes of the five-sphere basis and of the six-cell attaching maps give a homotopy equivalent model with a diagonal matrix containing \(43\) unit entries and a zero remainder. Each unit six-cell kills one five-sphere by an elementary CW cancellation. The surviving \(4\) five-spheres and \(139\) freely attached six-spheres give the displayed wedge. This last argument would not follow from a mod-two Betti-number calculation alone.

## Verification
Run `python3 verify_cube_homotopy.py` using only the Python standard library. It independently enumerates all faces in two ways, reconstructs the Laplacian generating polynomial, verifies all Hasse incidences and matching acyclicity, calculates the two independent integral gradient-path matrices, performs the explicit unit-pivot Smith reduction, and checks the digest above. The final report is:

```
VERIFY_OK faces=23625 hasse_incidences=124200 matching_pairs=11698 critical5=47 critical6=182 morse_shape=47x182 morse_nonzero=334 unit_smith_factors=43 smith_zeros=4 H5_rank=4 H6_rank=139 matrix_sha256=c5d099140b205ee3bc820da7ae1a15884d4571827ae031d129773635bc82fdd2
```

The verifier creates the entire finite combinatorial object from the explicit graph definition; no external datasets, saved matrices, symbolic packages, or unprovided certificates are needed. The computation is finite and exhaustive for this eight-vertex graph. The topological step additionally uses the standard discrete-Morse CW theorem and the elementary homotopy classification of maps between wedges of spheres in the lowest dimension.

## Relationship to prior work
Scoville's April 20, 2026 paper [1] studies the homotopy types and structural results of complexes of discrete Morse matchings, including complexes associated with simplices and their boundaries, but does not classify the cube graph \(Q_3\). Scoville–Zaremsky [2] give general connectivity estimates rather than this exact homotopy type. Contreras–Tawfeek [3] relate face counts to graph Laplacians, which supplies a counting check but does not control the integral attaching degrees.

A published computation [4] covers **the identical cube-graph Morse complex** and determines only the reduced mod-two homology ranks \(4\) in degree \(5\) and \(139\) in degree \(6\). Its explicit limitations exclude integral homology, torsion, and homotopy type. The present integral attaching-degree calculation strictly strengthens that result. Published exact Morse-complex classifications for other graphs do not cover \(Q_3\).

The 2020 thesis of Courtney [5] on directed forest complexes of Cayley graphs is a potentially overlapping source: the cube is a Cayley graph and the directed-forest interpretation resembles the present one. Its institutional abstract was inspected, but the full thesis could not be obtained, so the possibility of an earlier equivalent exact classification cannot be excluded.

## Limitations
The theorem concerns the **ordinary** Morse matching complex of exactly the cube graph \(Q_3\). It gives neither a general result for \(Q_n\) with \(n\ge4\) nor an equivariant homotopy classification. The presentation relies on a finite exhaustive integer-arithmetic certificate, rather than a symbolic closed-form matching argument. Mathematical originality remains subject to published or unindexed results not located, especially the unavailable full text of [5].

## References
1. N. A. Scoville, *The complex of discrete Morse matchings of the n-simplex: homotopy types and structural results*, arXiv:2604.18172v1 (first posted 2026-04-20). https://arxiv.org/abs/2604.18172
2. N. A. Scoville and M. C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481 (2020). https://arxiv.org/abs/2004.10481
3. I. Contreras and A. R. Tawfeek, *On discrete gradient vector fields and Laplacians of simplicial complexes*, arXiv:2105.05388 (2021). https://arxiv.org/abs/2105.05388
4. *Mod-2 homology of the cube-graph Morse complex is concentrated in degrees 5 and 6*, public published-finding corpus mathematical record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-mod-2-homology-of-the-cube-graph-morse-complex-is-concentrated-i--3861de13b7e0
5. K. Courtney, *The Directed Forest Complex of Cayley Graphs*, Boise State University thesis (2020), DOI:10.18122/td/1684/boisestate. https://scholarworks.boisestate.edu/td/1684/
