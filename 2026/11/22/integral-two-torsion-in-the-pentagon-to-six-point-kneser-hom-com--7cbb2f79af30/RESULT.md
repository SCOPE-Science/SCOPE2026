# Integral two-torsion in the pentagon-to-six-point Kneser Hom complex

## Finding
Let \(G=\operatorname{KG}(6,2)\) and \(X=\operatorname{Hom}(C_5,G)\), the ordinary undirected graph-Hom complex. Its complete integral singular homology is
\[
H_i(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z^{9}\oplus\mathbb Z/2\mathbb Z,&i=1,\\
\mathbb Z^{728},&i=2,\\
0,&i\ge3.
\end{cases}
\]
In particular the unreduced Hom space has genuine order-two torsion. No claim of a wedge decomposition or of a particular fundamental-group presentation is made.

## Assumptions and scope
The graph \(G\) has the fifteen vertices given by unordered two-element subsets of \(\{0,1,2,3,4,5\}\). Two such vertices are adjacent if and only if their underlying two-element sets are disjoint. The graph \(C_5\) is the undirected five-cycle, vertices numbered cyclically. A closed cell of \(X\) is an ordered five-tuple \((A_0,A_1,A_2,A_3,A_4)\) of **nonempty** subsets of \(V(G)\), satisfying complete bipartite adjacency \(A_j\times A_{j+1}\subseteq E(G)\) for each cyclic position. It is the product \(\prod_{j=0}^4\Delta^{|A_j|-1}\) and has dimension \(\sum_j(|A_j|-1)\). The attaching maps use the ordinary product orientations in increasing target-vertex order. All computations below are integral unless specified.

## Proof
The finite exhaustive certificate is reproduced by the standalone `VERIFY.py`. Start with all proper homomorphisms \(C_5\to G\) (singleton coordinate cells), and iteratively adjoin a single target vertex to any coordinate when all adjacent-coordinate compatibility conditions remain satisfied. Every nonempty multihomomorphism cell admits a monotone chain of such additions from a singleton cell, so this upward enumeration is exhaustive. The algorithm finds exactly \(104220\) cells, with counts \((6570,28350,40500,22950,5400,450)\) in dimensions zero through five.

For every cell, the program constructs every codimension-one product-simplex face by removing one element from one non-singleton coordinate. It then repeatedly removes a codimension-one face belonging to precisely one remaining upper cell, together with that unique upper cell. Each is a valid elementary collapse in a regular CW complex: a proper face of a product of simplices is itself a regular subcomplex, and there are no other cofaces of the free face. The actual executable test of *all remaining upper cofaces* supplies the freeness condition at each step. There are \(32058\) such pairs, leaving a CW complex \(Y\) with \(6570\) vertices, \(19692\) edges and \(13842\) two-cells, no higher cells. The retained incidence lists are the actual face relations of this CW subcomplex.

The one-skeleton of \(Y\) is connected. Contracting a spanning tree of \(6569\) edges is a homotopy equivalence and leaves \(13123\) oriented loops. The signed integral boundary of every two-cell is computed using the alternating simplex-face formula within each factor and the product sign arising from preceding factor dimensions. Tree edges vanish in the contracted boundary. The resulting integer matrix has \(13123\) rows and \(13842\) columns. Each elimination step uses a coefficient \(\pm1\) and exact integer row/column operations, so it preserves the integral Smith invariants. The algorithm removes \(13113\) unit pivot pairs. The remaining nonzero entries lie in a seven-row by seventy-five-column submatrix, with all entries equal to \(\pm2\). Direct exact Smith reduction of this **small residual matrix** has invariant diagonal \((2,0,0,0,0,0,0)\). Hence the integral boundary rank is \(13114\), with all nonzero Smith factors \(1\) except one \(2\).

Since \(\partial_1\) vanishes after contracting the spanning tree and \(C_i(Y)=0\) for \(i\ge3\), it follows that the degree-one homology is the cokernel \(\mathbb Z^{13123}/\operatorname{im}\partial_2\cong\mathbb Z^9\oplus\mathbb Z/2\mathbb Z\). The kernel of a homomorphism of free abelian groups is free, and its rank in degree two is \(13842-13114=728\). Connectedness gives \(H_0\cong\mathbb Z\). The collapse preserves integral homology, completing the proof.

## Verification
Run `python VERIFY.py` with Python 3.10+ and SymPy installed. Its exact output is `VERIFY_output.txt`. The complete cell count gives ordinary Euler characteristic \(720\), independently matching \(1-9+728=720\). An independent mod-two elimination on the retained two-dimensional face incidences has \(\operatorname{rank}_{\mathbb F_2}\partial_2=13113\), hence \(\dim H_1(X;\mathbb F_2)=10\) and \(\dim H_2(X;\mathbb F_2)=729\), matching the integral answer and the universal coefficient theorem. The mod-two calculation does **not** replace the integer Smith computation.

## Relationship to prior work
Nilakantan and Singh classify the open-neighborhood complex of the same two-subset Kneser family (at this parameter a wedge of nineteen two-spheres), rather than \(\operatorname{Hom}(C_5,G)\); it is equivalent to the graph-Hom construction with *source an edge*, not the source pentagon. Osztényi determines homotopy of \(\operatorname{Hom}(K_\ell,\operatorname{KG}(m,n))\) for *complete* source graphs; its theorem does not include the five-cycle. Schultz studies \(\operatorname{Hom}(C_5,K_n)\) for a *complete target graph*, not a Kneser target. These statements neither state nor immediately imply the present integral first-homology torsion and the 728-dimensional second-homology lattice. This is a comparison of the actual objects, not a claim of global priority based on keyword absence.

## Limitations
This is a complete integral **homology** classification of one explicitly specified natural finite graph-Hom complex, not an infinite-family theorem or an integral **homotopy** classification. The proof is computer-assisted but exhaustive and reproducible: the certificate enumerates all CW cells, carries out every elementary free-face operation and performs exact integer reductions. A separate implementation of the integral Smith reduction has not been supplied; the mod-two rank is corroborated by a distinct arithmetic path. Equivalent results not located in the inspected sources remain a bibliographic risk.

## References
1. N. Nilakantan and A. Singh, *Homotopy type of Neighborhood Complexes of Kneser graphs, KG_{2,k}*, arXiv:1802.05848, first version 2018-02-16, https://arxiv.org/html/1802.05848v1 .
2. J. Osztényi, *The homotopy type of complexes of homomorphisms from a complete graph to a Kneser graph*, Acta Sci. Math. (Szeged) **76** (2010), 713–722, DOI 10.1007/BF03592970.
3. C. Schultz, *Small models of graph colouring manifolds and the Stiefel manifolds Hom(C_5,K_n)*, arXiv:math/0510535, https://arxiv.org/abs/math/0510535 .
