# The signed five-point symmetry representation of Desargues independence homology

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph, with ten vertices the two-element subsets of \([5]\), and with edges joining disjoint subsets. Let \(D=P\times K_2\) be its canonical bipartite double cover, the Desargues graph \(G(10,3)\), and \(X=\operatorname{Ind}(D)\) its ordinary independence complex. The full graph automorphism group is \(G\cong S_5\times C_2\). Write \(\varepsilon\) for the nontrivial character of the layer-interchange factor, \(\operatorname{sgn}\) for the sign of a permutation of five labels, and \(\mathbb Q^5\) for the permutation representation on those five labels.

**The complete reduced rational homology representation is**
\[
\widetilde H_4(X;\mathbb Q)\cong \operatorname{sgn}\boxtimes\varepsilon,
\qquad
\widetilde H_5(X;\mathbb Q)\cong \mathbb Q^5\boxtimes\varepsilon.
\]
All other reduced rational homology groups vanish. In particular the deck/layer involution acts as minus the identity in *both* nonzero degrees. The known nonequivariant wedge \(S^4\vee\bigvee^5S^5\) is not claimed as new here.

Let \(S_5\) denote the subgroup preserving each layer, \(A_5\) its alternating subgroup, and \(\langle\tau\rangle\) the order-two deck group. The ordinary topological quotients satisfy the rational cohomology-ring identities
\[
H^*(|X|/S_5;\mathbb Q)\cong H^*(S^5;\mathbb Q),\quad
H^*(|X|/A_5;\mathbb Q)\cong H^*(S^4\vee S^5;\mathbb Q),
\]
\[
H^*(|X|/\langle\tau\rangle;\mathbb Q)
\cong H^*(|X|/G;\mathbb Q)\cong\mathbb Q
\quad\text{(concentrated in degree zero).}
\]
These are rational cohomology statements, not assertions of quotient homotopy equivalence to spheres.

## Assumptions and scope
Use vertices \((a,b)\) with \(a\in\binom{[5]}2\) and \(b\in\{0,1\}\). There is an edge between \((a,0)\) and \((c,1)\) precisely when \(a\cap c=\varnothing\); no edges lie within a layer. The natural action sends \((a,b)\) to \((\sigma a,b\oplus\delta)\), for \(\sigma\in S_5\), \(\delta\in C_2\). The independence complex has a face for each vertex subset containing no graph edge. Chain complexes are augmented simplicial chains with the standard increasing-label orientation and \(\widetilde C_{-1}=\mathbb Q\).

The group displayed is the full automorphism group, not just a selected subgroup. To see this, the Petersen graph's five maximal four-vertex independent sets are the five stars of two-subsets containing a fixed label. Every automorphism permutes those stars, and each graph vertex is the intersection of two stars, proving \(\operatorname{Aut}(P)=S_5\). The Petersen adjacency matrix \(A\) obeys \(A^2=2I-A+J\); hence \(A\) is nonsingular since \(Av=0\) would imply \((2I+J)v=0\). A bipartition-preserving automorphism of \(D\) has permutation matrices \(U,V\) with \(UAV^{\mathsf T}=A\). Multiplication by the transpose gives \(UA^2U^{\mathsf T}=A^2\), hence \(UAU^{\mathsf T}=A\) and, by invertibility, \(V=U\). Any bipartition exchange is a preserving automorphism followed by the central layer flip. Since \(D\) is connected, this exhausts all automorphisms.

## Proof
**1. Chain ranks and rational homology bounds.** Exact enumeration of the independent faces gives the face vector by dimensions \(0,1,\ldots,9\):
\[
(20,160,660,1510,1924,1320,480,115,20,2).
\]
There are \(6211\) nonempty faces. Using the oriented simplicial boundary, with signs suppressed over \(\mathbb F_2\), the ranks of the augmented boundary maps \(\partial_k\), for \(k=0,\ldots,9\), are
\[
(1,19,141,519,991,932,383,97,18,2).
\]
Each rank is obtained by complete binary column elimination, using integer bit vectors (not random sampling). Therefore the only nonzero reduced mod-two Betti numbers are \(\widetilde\beta_4=1\) and \(\widetilde\beta_5=5\). An integer boundary matrix has rank over \(\mathbb Q\) at least its rank over \(\mathbb F_2\); hence the rational Betti numbers are zero outside these degrees, and \(\beta_4\leq1\), \(\beta_5\leq5\). The reduced Euler characteristic, determined by the face vector, is \(-4\), so \(\beta_5=\beta_4+4\).

**2. Signed simplicial Lefschetz character.** For \(g\in G\) put
\[
E(g)=\sum_{k=-1}^{9}(-1)^k\operatorname{tr}(g\mid \widetilde C_k(X;\mathbb Q))
=\operatorname{tr}(g\mid\widetilde H_4)-\operatorname{tr}(g\mid\widetilde H_5).
\]
For any \(g\), form its vertex orbits. Discard any orbit containing an internal graph edge. Two remaining orbits are adjacent when a graph edge joins them. Let \(T_g\) be this orbit graph. An invariant independent face is the union of some independent orbits. If it uses \(r\) vertex orbits, its signed contribution to the augmented alternating chain trace is \((-1)^{r-1}\), including the empty face contribution \(-1\). Thus
\[
E(g)=-I(T_g;-1),
\]
where \(I(T;t)\) is the independence polynomial. This finite exact evaluation is reproduced with the recursion \(I(T;-1)=I(T-v;-1)-I(T-N[v];-1)\).

The exhaustive fourteen-conjugacy-class table is below. Here \(c(\sigma)\) is the cycle type of \(\sigma\in S_5\), and the rightmost column corresponds to composition with the deck flip \(\tau\).

| \(c(\sigma)\) | Class size in \(S_5\) | \(E(\sigma,0)\) | \(E(\sigma,\tau)\) |
| --- | ---: | ---: | ---: |
| \(1^5\) | 1 | -4 | 4 |
| \(2,1^3\) | 10 | -4 | 4 |
| \(2^2,1\) | 15 | 0 | 0 |
| \(3,1^2\) | 20 | -1 | 1 |
| \(3,2\) | 20 | -1 | 1 |
| \(4,1\) | 30 | -2 | 2 |
| \(5\) | 24 | 1 | -1 |

This table is independently checked by counting every fixed oriented simplex for one representative of each of the fourteen classes. All 240 automorphisms are checked by the orbit-polynomial method, and the signed and orbit methods agree on the representatives.

**3. Actual rational dimensions.** If \(\beta_4=0\), then \(\beta_5=4\) and the transposition class, having \(E=-4\), would act with trace \(4\) on a four-dimensional space. Because a transposition is an involution, it must act as the identity. All transpositions generate \(S_5\), so every three-cycle would have trace \(4\), contrary to its required trace \(1\) from \(E=-1\). Hence \(\beta_4=1\) and \(\beta_5=5\).

**4. The \(S_5\) modules.** On one-dimensional fourth homology, \(S_5\) acts by either its trivial character or its sign. Trivial action would make every transposition act with trace \(5\) on fifth homology, forcing the entire \(S_5\) action there to be trivial. A three-cycle would then have trace \(5\), whereas the Lefschetz table gives \(1-(-1)=2\). Thus fourth homology carries \(\operatorname{sgn}\). The fifth-homology character is consequently \(\operatorname{sgn}(\sigma)-E(\sigma,0)\), which on the seven cycle types is
\[
(5,3,1,2,0,1,0).
\]
These are precisely the numbers of fixed labels in the natural permutation action of \(S_5\) on five points. Equality of rational characters yields \(\widetilde H_5|_{S_5}\cong\mathbb Q^5\).

**5. The deck action.** Since \(\tau\) is central, it acts on the one-dimensional fourth homology by a scalar \(a\in\{\pm1\}\). If \(a=1\), then \(E(\tau)=4\) implies \(\operatorname{tr}(\tau|\widetilde H_5)=-3\); the \(+1\) eigenspace of \(\tau\) on fifth homology is one-dimensional. For every \(\sigma\in S_5\), the above table and \(E(\sigma,\tau)=-E(\sigma,0)\) show that the character of this positive eigenspace is \(\operatorname{sgn}(\sigma)\). But the natural five-point permutation representation contains no sign subrepresentation: a vector reversed by every transposition must have every coordinate zero. This contradiction forces \(a=-1\). Then \(\operatorname{tr}(\tau|\widetilde H_5)=-5\), so the involution is minus the identity in all five dimensions. This proves both displayed full-group representations.

**6. Quotients.** A finite group action becomes without simplex inversions after barycentric subdivision. Over \(\mathbb Q\), cellular chains of an ordinary orbit space identify with invariant chains, and exactness of invariant-taking gives \(H^*(|X|/H;\mathbb Q)\cong H^*(|X|;\mathbb Q)^H\) for every subgroup \(H\leq G\). In degree four and five, respectively, the invariant dimensions for \(S_5\) are \((0,1)\), for \(A_5\) are \((1,1)\), and for \(\langle\tau\rangle\) and \(G\) are \((0,0)\). Since other positive-degree cohomology vanishes and any positive-degree cup product lands in a vanishing group, the cohomology-ring statements follow.

## Verification
Run `python3 verify_desargues.py` with the Python standard library. It constructs the graph, enumerates all faces and exact mod-two boundary ranks, verifies the Petersen adjacency identity and 240 concrete graph automorphisms, independently evaluates the Lefschetz table through orbit polynomial and oriented fixed-simplex methods, and averages characters for the four subgroups. It prints `DESARGUES_SIGNED_PERMUTATION_HOMOLOGY_PASS` on success. `verification_output.txt` contains the actual recorded output; `character_table.csv` gives all fourteen character rows.

## Relationship to prior work
Barmak's star-cluster theorem gives a suspension method for triangle-free independence complexes, but not a Desargues representation. Tsukuda's incidence-graph duality gives the suspension homotopy type of every finite bipartite graph as a reduction to another complex; it does not evaluate the Desargues representation. Earlier published calculations of this *same* Desargues independence complex already establish its integral wedge homotopy type \(S^4\vee\bigvee^5S^5\); the underlying Betti numbers and wedge decomposition are expressly excluded from the novelty claim. The present claim refines them by the full \(S_5\times C_2\) module, the negative deck action in both degrees, and cohomology of four natural quotient spaces. Broader work on Mycielskian and categorical-product independence complexes uses double covers as input or treats other graph families, without reporting this module.

## Limitations
The result is a complete **rational** character statement for one named graph. It does not determine integral equivariant homology lattices, quotient integral torsion, or equivariant homotopy types. The quotient cohomology-ring isomorphisms do not entail homotopy equivalence of the quotients to spheres. A title/alias search and targeted primary-source reading cannot exclude unindexed equivalent work. The computational certificate is finite and exact but is not an independent mathematical audit.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first submitted 2010-07-02; subsequently Adv. Math. 241 (2013), 33–57.
2. S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12 (2017), 28–46, DOI:10.55016/ojs.cdm.v12i1.62277, particularly Corollary 5.3.
3. A. Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457, especially Section 3.
4. A. Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432, especially Theorem 5.
5. *The Desargues independence complex is \(S^4\vee\bigvee^5S^5\)*, public scientific record e9aae0fc2563 (2026), Finding and Proof.
6. *Independence complex of the Desargues graph is \(S^4\vee\bigvee^5S^5\)*, public scientific record f3b1cf10aadb (2026), Finding and Proof.
