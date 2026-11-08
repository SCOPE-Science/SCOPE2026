# Full 1440-element homology character of two unordered particles on the Tutte–Coxeter graph

## Finding
Let \(T\) be the 30-vertex Tutte–Coxeter graph, the Levi graph of the Cremona–Richmond \((15_3)\)-configuration. Let \(B_2(T)=\{\{x,y\}:x,y\in |T|,\ x\ne y\}\) be the configuration space of two distinct **unordered** points on its geometric realization. Its full graph-automorphism group \(G=\operatorname{Aut}(T)\) has order \(1440\), with index-two subgroup \(S_6\) that preserves the duad and syntheme classes. Then
\[
H_2(B_2(T);\mathbb Z)\cong\mathbb Z^{90},\qquad
H_1(B_2(T);\mathbb Q)\cong\mathbb Q^{16}.
\]
The complete rational character \(\chi(g)=\operatorname{tr}(g_*\mid H_2(B_2(T);\mathbb Q))\) is
\[
\boxed{\chi(g)=\begin{cases}
90,&g=1,\\
-6,&g\in S_6\text{ and }g\text{ has order }2,\\
2,&g\in S_6\text{ and }g\text{ has order }4,\\
0,&\text{otherwise}.
\end{cases}}
\]
Here the cases for order \(2\) and order \(4\) are restricted to the canonical, color-preserving subgroup; **every color-exchanging automorphism has trace zero**. The restriction to \(S_6\) has the explicit rational Specht decomposition
\[
\boxed{H_2(B_2(T);\mathbb Q)\big|_{S_6}\cong
2\left(S^{(4,1,1)}\oplus S^{(3,2,1)}\oplus
S^{(3,1,1,1)}\oplus S^{(2,2,1,1)}\right).}
\]
Thus neither \(S_6\) nor the full group \(G\) fixes a nonzero rational second-homology class.

## Assumptions and scope
A **duad** is a two-element subset of \(\{1,2,3,4,5,6\}\); a **syntheme** is a partition of that set into three duads. The graph has one vertex for each of the 15 duads and 15 synthemes; a duad is adjacent to a syntheme exactly when it belongs to that syntheme. This specifies the graph without referring to a drawing. The order-\(720\) subgroup \(S_6\) permutes the six labels and preserves the two vertex classes. The claimed homology is **ordinary** homology, not Borel–Moore homology or homology with a nontrivial exchange local system. The character and Specht statements use rational coefficients; the asserted integral result is the abelian group structure of top homology, not an integral representation-lattice decomposition. The complex is two-dimensional, so all higher homology groups vanish.

## Proof
**1. Cubical model and boundaries.** Prue and Scrimshaw's subdivision criterion (arXiv:0909.5511, Theorem 3.2) applies to two particles: distinct essential graph vertices are separated by at least one edge, and every noncontractible closed edge-path has at least three edges (the graph in fact has girth eight). Consequently the unordered discrete configuration cubical complex models \(B_2(T)\). Its 0-cells are unordered pairs of distinct vertices, its 1-cells are a graph edge and a vertex not incident to it, and its 2-cells are unordered pairs of vertex-disjoint graph edges. There are respectively
\[
\binom{30}{2}=435,\quad45(30-2)=1260,\quad
\binom{45}{2}-30\binom32=900
\]
such cells. Orient each graph edge from the smaller to the larger labeled vertex, and orient a 2-cell by the product orientation of its two edges in increasing edge-index order. For vertex-disjoint oriented edges \(e=[a,b]\), \(f=[c,d]\) with \(e<f\), the cellular boundary is
\[
\partial_2[e,f]=[f,b]-[f,a]-[e,d]+[e,c],
\quad \partial_1[e,v]=[b,v]-[a,v].
\]
This is a complete, unambiguous signed chain presentation.

**2. Rank and exact homology bounds.** The graph of 0- and 1-cells is connected (the accompanying verifier explicitly traverses its 435 vertices), so \(\operatorname{rank}\partial_1=434\). Exact sparse modular elimination of the **specified 1260-by-900 integer boundary**, performed from its 900 four-term columns in the standalone verifier, gives \(\operatorname{rank}_{\mathbb F_3}\partial_2=810\). Therefore \(\operatorname{rank}_{\mathbb Q}\partial_2\ge810\). An independent enumeration finds 90 distinct graph octagons and selects 16 with linearly independent edge-incidence vectors over \(\mathbb F_2\). Since the connected graph has cycle rank \(45-30+1=16\), they span rational graph homology. For each octagon, fix a graph vertex outside its eight vertices and run one particle around the octagon with the other parked. These 16 configuration 1-cycles map to the independent graph octagons under the **sum-of-particle-chains** map, which is a cellular chain map to the graph. Hence \(\dim H_1(B_2(T);\mathbb Q)\ge16\), giving
\[
\operatorname{rank}_{\mathbb Q}\partial_2
\le1260-434-16=810.
\]
Both bounds force equality. Thus \(b_1=16\) and \(b_2=900-810=90\). Because there are no 3-cells, \(H_2=\ker\partial_2\) is a subgroup of a free abelian group, so \(H_2(B_2(T);\mathbb Z)\cong\mathbb Z^{90}\). The sum-of-particle map is an isomorphism on rational first homology, since its image contains all 16 independent graph cycles.

**3. The entire automorphism group.** Two duads lie in a common syntheme exactly when they are disjoint; hence a color-preserving graph automorphism induces an automorphism of the disjointness graph on duads. The six maximal intersecting families of five duads are exactly the six stars consisting of all pairs through a specified label. Every automorphism must permute these six stars, giving an injection into \(S_6\); conversely every label permutation induces a graph automorphism, so the color-preserving subgroup is exactly \(S_6\). The standalone code supplies an explicit color-swapping involution and verifies that it preserves all 45 graph edges. Thus the full graph-automorphism group contains \(2(720)=1440\) distinct elements; any connected bipartite graph automorphism either preserves or swaps its two classes, proving equality.

**4. Character from signed cellular Lefschetz traces.** For any graph automorphism \(g\), the sum-of-particle isomorphism identifies its rational first-homology character with that of the graph. With the signed orientation action on graph edges, this character is
\[
\chi_1(g)=1-\operatorname{tr}(g\mid C_0(T;\mathbb Q))+
\operatorname{tr}(g\mid C_1(T;\mathbb Q)).
\]
The two-dimensional cubical Lefschetz identity therefore gives
\[
\chi(g)=\operatorname{tr}(g\mid C_0(B_2(T)))
-\operatorname{tr}(g\mid C_1(B_2(T)))
+\operatorname{tr}(g\mid C_2(B_2(T)))
-1+\chi_1(g).
\]
Every trace on the right is an exact signed fixed-cell count. On a fixed pair of edges, exchanging the two factors contributes an additional minus sign. The reproducible program enumerates the 720 label permutations and their 720 compositions with the explicit class-exchanging involution. It checks full boundary equivariance for every 2-cell and every automorphism, then evaluates the above identity. Among all 1440 elements, the resulting trace frequencies are \(90:1\), \(-6:75\), \(2:180\), and \(0:1184\); every one of the 720 class-exchanging elements lies in the last case. The 75 nonidentity involutions of \(S_6\) have trace \(-6\), its 180 order-four elements have trace \(2\), and all its other elements except the identity have trace \(0\). This proves the character formula for **every** automorphism, not just a sampled set.

**5. Rational irreducibles.** Apply the Murnaghan–Nakayama rule to all eleven conjugacy classes of \(S_6\), and take the exact character inner products using their class sizes. The four nonzero multiplicities are each \(2\), for partitions \((4,1,1)\), \((3,2,1)\), \((3,1,1,1)\), and \((2,2,1,1)\), of dimensions \(10,16,10,9\). Their weighted total is \(2(10+16+10+9)=90\). The trivial-representation multiplicity is zero, proving the fixed-subspace conclusion.

## Verification
Run `python3 verify_configuration.py` with Python 3 and no third-party packages. The program reconstructs the graph from duads and synthemes, all 2595 cubical cells, each signed 2-boundary, connectedness of the one-skeleton, ranks modulo 2, 3, and 5, the independent octagon basis, all 1440 distinct automorphisms, boundary equivariance under each automorphism, all signed Lefschetz traces, the eleven symmetric-group class characters, and the Murnaghan–Nakayama decomposition. The independently recorded output is in `verification_output.txt`. The modular ranks alone are **not** asserted to prove the rational rank: the 16 parked-octagon cycles provide the separate reverse inequality. Similarly, exhaustive enumeration is a valid proof for this named finite graph, not for arbitrary graphs.

## Relationship to prior work
Barnett and Farber (arXiv:0903.2180) develop intersection methods for ordered two-particle graph configurations, notably planar graphs. Farber and Hanbury (arXiv:1005.2300) give broad nonequivariant rank and homology results for *ordered* configurations on certain nonplanar mature graphs. Neither gives the natural 1440-element character of **ordinary unordered** two-point Tutte–Coxeter homology. Prue and Scrimshaw (arXiv:0909.5511) establish the discretized model used here, but not these calculations. Maciążek and Sawicki's 2019 subcubic graph results give general product-cycle generators and do not specify the exceptional outer-automorphism character. Indexed same-graph work computes the scale-three **Vietoris–Rips** homology representation, a different functor with a different homology dimension; indexed same-configuration-functor work instead studies the Petersen, dodecahedral, and cuboctahedral graphs. A published general calculation of exchange-sign **Borel–Moore** homology uses a different homology theory and local system. None of these inspected statements implies the present character or four-Specht decomposition without a new, graph-specific calculation.

## Limitations
This identifies ordinary rational second-homology representations and the rank of the integral second-homology group for **exactly** the 30-vertex Tutte–Coxeter graph. It does not determine the integral representation lattice, the full integral first-homology torsion, the cohomology ring, or analogous configurations of more particles. The graph-specific character may be equivalent to an unindexed calculation; the literature search cannot establish absolute priority. No independent mathematical audit has been performed.

## References
1. Kathryn Barnett and Michael Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180v1, first public 2009-03-12.
2. Paul Prue and Travis Scrimshaw, *Abrams's Stable Equivalence for Graph Braid Groups*, arXiv:0909.5511, first public 2009-09-30, Theorem 3.2.
3. Michael Farber and Elizabeth Hanbury, *Topology of Configuration Space of Two Particles on a Graph, II*, arXiv:1005.2300, first public 2010-05-13.
4. John Baez, *Tutte–Coxeter Graph*, Visual Insight, 2015-08-15, https://blogs.ams.org/visualinsight/2015/08/15/tutte-coxeter-graph/ .
5. Tomasz Maciążek and Adam Sawicki, *Non-abelian Quantum Statistics on Graphs*, Communications in Mathematical Physics 371 (2019), 921–973, DOI:10.1007/s00220-019-03583-5, especially Section 5.7.
6. *The natural \(S_6\)-homology representation of the scale-three Tutte–Coxeter Vietoris–Rips complex*, publicly indexed mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-natural-s-6-homology-representation-of-the-scale-three-tutte--df31ab97e550 .
7. *Exchange-sign Borel–Moore homology of two-point graph configurations*, publicly indexed mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exchange-sign-borel-moore-homology-of-two-point-graph-configurat--68e49e70a285 .
