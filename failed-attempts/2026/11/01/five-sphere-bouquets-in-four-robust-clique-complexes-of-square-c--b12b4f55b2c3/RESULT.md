# Five-sphere bouquets in four-robust clique complexes of square cactus flowers

## Finding
For every integer \(m\ge1\), let \(F_m\) be the bouquet of \(m\) four-cycles sharing exactly one vertex. Its four-robust clique complex has homotopy type
\[
R_4(F_m)\simeq\bigvee^{\binom m3}S^5.
\]
Here \(R_4(G)=\{S\subseteq V(G):\alpha(G[S])\le3\}\), with all subsets understood as simplices, including the empty face. A wedge with zero summands is a point. Consequently the reduced integral homology is free of rank \(\binom m3\) in degree five and zero in all other degrees.

## Assumptions and scope
The graph is simple and finite. Its vertices are \(z,a_i,b_i,c_i\), with \(1\le i\le m\). Its only edges are \(za_i,a_ib_i,b_ic_i,c_iz\). Different petals have no edges between their private vertices. The four-robust condition forbids independent sets of exactly four or more in an induced subgraph. The theorem applies for all positive integers \(m\) and makes no equivariant statement.

## Proof
**Step 1: supports.** For a face \(S\in R_4(F_m)\), define \(\operatorname{supp}(S)=\{i:S\cap\{a_i,b_i,c_i\}\ne\varnothing\}\). Private vertices in distinct petals have no edges between them. Choosing one vertex from each occupied petal therefore produces an independent set. Hence \(|\operatorname{supp}(S)|\le3\).

**Step 2: low-support cone.** Let \(B_m\subseteq R_4(F_m)\) be the subcomplex of faces supported on at most two petals. It is a cone with apex \(z\). Indeed, when \(z\notin S\) and \(|\operatorname{supp}(S)|\le2\), adding \(z\) gives
\[
\alpha(F_m[S\cup\{z\}])=\max\{\alpha(F_m[S]),\,1+|S\cap\{b_1,\ldots,b_m\}|\}\le3.
\]
The displayed equality follows because the private vertices not adjacent to \(z\) are exactly the mutually nonadjacent \(b_i\). Thus every face of \(B_m\) extends to a face containing \(z\). For \(m\le2\), the whole complex equals \(B_m\) and is contractible.

**Step 3: three-petal block.** We prove \(R_4(F_3)\simeq S^5\) by an exhaustive finite acyclic discrete-Morse matching. Label \(z=0\), \((a_i,b_i,c_i)=(3i-2,3i-1,3i)\) for \(i=1,2,3\). Encode subsets by ten-bit integer masks. Enumerating all 1,024 masks, accepting exactly those containing no independent four-subset, gives 537 faces including the empty face. The attached `matching_pairs.csv` contains 268 pairs of incident faces of adjacent dimensions. The attached `verify.py` independently enumerates all 537 faces from the explicit edge set, checks membership and disjointness of all 268 pairs, and orients every one of the 2,130 cover relations in the face poset upward for a matched edge and downward otherwise. Exhaustive Kahn topological sorting visits all 537 vertices: the directed graph is acyclic. Exactly one face is unmatched, mask 876, consisting of \(\{b_1,c_1,b_2,c_2,b_3,c_3\}\), of dimension five. The empty face is paired with vertex \(z\), so on the nonempty face poset the same matching leaves precisely one critical vertex and one critical five-face. Forman's discrete Morse theorem gives a CW complex with one zero-cell and one five-cell and no other cells, necessarily \(S^5\).

**Step 4: global gluing.** For each triple \(I\subseteq\{1,\ldots,m\}\), let \(K_I\) be the full induced subcomplex of \(R_4(F_m)\) on the shared hub and the three petals indexed by \(I\). By Step 1,
\[
R_4(F_m)=B_m\cup\bigcup_{|I|=3}K_I.
\]
For any triple, \(K_I\cong R_4(F_3)\). Its intersection \(K_I\cap B_m\) is the two-petal-support subcomplex and is a cone on \(z\) by Step 2. For distinct triples \(I\ne J\), \(K_I\cap K_J\subseteq B_m\). Thus collapsing the contractible simplicial subcomplex \(B_m\) yields the genuine quotient decomposition
\[
R_4(F_m)/B_m\cong\bigvee_{|I|=3}K_I/(K_I\cap B_m).
\]
Collapsing a nonempty contractible subcomplex of a CW complex is a homotopy equivalence, and the same applies to each contractible \(K_I\cap B_m\subset K_I\). Each quotient summand is therefore homotopy equivalent to \(S^5\). There are \(\binom m3\) triples, proving the theorem.

## Verification
Run `python3 verify.py matching_pairs.csv` in one directory containing the two attached artifacts. The verifier uses integer bitmask enumeration and graph-theoretic tests of all four-element vertex subsets; it does not assume the stated face count, pairing validity, or DAG acyclicity. Expected output: 537 faces; 268 valid pairs; 2,130 Hasse cover relations; one unmatched dimension-five simplex of mask 876; and successful acyclicity test. The symbolic all-\(m\) argument uses Steps 1, 2 and 4; the finite checker supplies precisely the Step 3 building-block certificate.

## Relationship to prior work
Filakovský introduced the robust clique construction and conjectured a \((2k-3)\)-sphere-wedge classification for general square-sequence graphs, proving it for \(k=2,3\) and for arbitrary \(k\) under a restrictive square-attachment hypothesis. Square cactus bouquets involve repeated corner attachments, so the unrestricted \(k=4\) case is not a direct instance of the edge-attachment result. This theorem supplies a complete new infinite-family corner-gluing case, including the multiplicity \(\binom m3\). The ordinary \(k=3\) theory and separate four-robust Euler-characteristic calculations on rectangular grids have different implications and do not determine the present homotopy classification.

## Limitations
The proof concerns only four-cycles with a single common hub and robustness threshold four. It does not classify arbitrary corner-glued square sequences or larger thresholds. The finite matching is a complete certificate only for the three-petal block; the arbitrary-petal conclusion is proved by the separate general support-and-quotient argument. No independent human mathematical audit has been performed.

## References
- Marek Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, initially submitted 2026-02-11, https://arxiv.org/abs/2602.11365.
- Robin Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
- Allen Hatcher, *Algebraic Topology*, Cambridge University Press (2002), homotopy properties of CW pairs and quotients.
