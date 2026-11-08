# Four independent two-torsion classes in three-particle Möbius–Kantor configurations

## Finding
Let \(M=\operatorname{GP}(8,3)\) denote the sixteen-vertex Möbius–Kantor graph, and let \(B_3(M)\) be the space of **unordered configurations of three distinct points** on its geometric realization. Then
\[
H_3(B_3(M);\mathbb Z)\cong\mathbb Z,
\qquad H_2(B_3(M);\mathbb Z)[2]\cong(\mathbb Z/2)^4.
\]
Here \(A[2]=\{a\in A:2a=0\}\) denotes the subgroup annihilated by two; the latter equality determines the exact number of independent order-two classes, **not** the entire two-primary invariant-factor decomposition of \(H_2\). Four integral two-cycles representing independent order-two classes are explicitly specified by the accompanying certificate and its generating-basis conventions.

## Assumptions and scope
The graph \(M\) has vertices \(u_i,v_i\), with \(i\in\mathbb Z/8\), and edges \(u_iu_{i+1}\), \(u_iv_i\), \(v_iv_{i+3}\), modulo eight. It is a simple cubic graph with 16 vertices and 24 edges, isomorphic to the Levi graph of the Möbius–Kantor \((8_3)\) configuration. Graph edges are topological closed intervals; points may lie in their interiors. The configuration space consists of unordered triples of pairwise distinct points, without vertex-only or fixed-discretization restrictions. Integral homology is singular homology of that space.

## Proof
We use the weight-three summand of the integral **reduced Świątkowski complex**, whose homology agrees with the integral homology of unordered graph configuration spaces by the cellular-chain comparison of An–Drummond-Cole–Knudsen and the reduced comparison recalled by An–Knudsen. The following specifies the entire finite chain complex and certificates.

Label \(u_i=i\) and \(v_i=8+i\). Sort the graph edges lexicographically by their two numeric endpoints. For each vertex \(v\), order its three incident edges as \(e_{v,0}<e_{v,1}<e_{v,2}\), and introduce two degree-one weight-one reduced half-edge symbols \(a_{v,0}=h_{v,e_{v,0}}-h_{v,e_{v,2}}\) and \(a_{v,1}=h_{v,e_{v,1}}-h_{v,e_{v,2}}\). Their differentials are \(d a_{v,j}=e_{v,j}-e_{v,2}\). Each graph-edge variable has homological degree zero and weight one.

An ordered basis for \(C_d\), \(0\le d\le3\), consists of all products of \(d\) symbols \(a_{v,j}\) at **distinct vertices**, with vertices in strictly increasing numeric order, times a commutative monomial of degree \(3-d\) in the 24 edges. Enumerate vertices first in lexicographic combination order, then the binary choices \(j\), then the weakly increasing edge-index tuples. A differential replaces a chosen symbol by its edge difference with sign \((-1)^p\), where \(p\) is its zero-based position in the list of distinct chosen vertices. The differential is extended by the graded Leibniz rule. These conventions agree exactly with the attached program and certificate. The chain ranks are
\[
(\operatorname{rank}C_0,\operatorname{rank}C_1,\operatorname{rank}C_2,\operatorname{rank}C_3)=(2600,9600,11520,4480).
\]

Write \(D_3:C_3\to C_2\) and \(D_2:C_2\to C_1\). The executable certificate verifies \(D_2D_3=0\) on all 4480 basis columns and computes **exact finite-field elimination ranks**
\[
\operatorname{rank}_{\mathbb F_2}(D_3)=4475,
\qquad\operatorname{rank}_{\mathbb F_3}(D_3)=4479,
\qquad\operatorname{rank}_{\mathbb F_5}(D_3)=4479.
\]
The attached explicit integral chain \(k\) has 1919 nonzero terms, has gcd of coefficients one, and satisfies \(D_3k=0\). Consequently \(\operatorname{rank}_{\mathbb Q}D_3=4479\): the nonzero modular rank is a lower bound on rational rank, and the exhibited nonzero integral kernel gives the matching upper bound. It follows that \(\ker_{\mathbb Z}D_3=\mathbb Zk\), since \(k\) is primitive. There are no degree-four chains in weight three, hence \(H_3=\mathbb Z\).

The finite-field nullspace \(\ker(D_3\bmod2)\) has dimension five. The reduction \(\bar k\) of the primitive kernel generator is nonzero. The certificate contains four further binary degree-three chains \(c_1,\ldots,c_4\), whose supports have sizes 878, 810, 772, and 763. Their reductions and \(\bar k\) are linearly independent over \(\mathbb F_2\). The program verifies that every coefficient in \(D_3c_i\) is even, so
\[
w_i=\tfrac12 D_3c_i\in C_2(\mathbb Z),
\qquad D_2w_i=0,
\qquad 2w_i=D_3c_i.
\]
Each \(w_i\) therefore represents an integral two-homology class of order dividing two. Suppose a nonempty mod-two combination of these four classes were zero. Writing its integer \(0\)-\(1\) combination of the \(c_i\) as \(c\), we would have \(D_3(c-2z)=0\) for an integral three-chain \(z\). As the integral kernel is \(\mathbb Zk\), reducing the equality \(c-2z=ak\) modulo two would contradict the independence of \(\bar k,\bar c_1,\ldots,\bar c_4\). Thus these are four independent classes of exact order two.

For exhaustiveness of the order-two subgroup, the mod-two kernel has dimension five and contains exactly one dimension from the mod-two reduction of the integral kernel. The standard reduction exact sequence gives
\[
\dim_{\mathbb F_2}(\operatorname{coker}D_3)[2]
=\dim_{\mathbb F_2}\ker(D_3\bmod2)
-\operatorname{rank}_{\mathbb Z}\ker D_3=5-1=4.
\]
Moreover, the natural quotient \(\operatorname{coker}D_3\twoheadrightarrow\operatorname{im}D_2\) has kernel \(H_2\), and \(\operatorname{im}D_2\) is a subgroup of the free abelian group \(C_1\), hence torsion-free. Therefore the torsion subgroups of \(\operatorname{coker}D_3\) and \(H_2\) agree. This proves the asserted exact subgroup \(H_2[2]\cong(\mathbb Z/2)^4\).

## Verification
The files `verify.py`, `certificate.json`, and `verification_output.txt` are complete standalone artifacts. Run `python verify.py certificate.json` using Python 3 and the standard library in a directory containing both files. The program reconstructs the 24-edge graph and every degree-two/degree-three matrix column, verifies all chain-complex identities and the four half-boundaries integrally, and reproduces the three finite-field ranks. The recorded output ends in `MOBIUS_KANTOR_THREE_PARTICLE_TORSION_PASS`. All chains use zero-based basis column indices generated by the documented ordering. Unlike a floating-point experiment, the checks are finite exact integer arithmetic and finite-field elimination. Their validity is conditional on the correctness of the verified chain-model comparison theorem and the readily inspectable program implementation.

## Relationship to prior work
Ko–Park [1] compute first homology of graph braid groups and characterize planarity by first-homology torsion; that does not determine second homology of this graph. The Świątkowski chain-model comparison in [2] and reduced complex discussion in [3] are used as known tools, not claimed as new results. An–Knudsen [3] classify generators of second homology for **planar** graphs; the Möbius–Kantor graph is nonplanar. The complete-bipartite family and torsion calculations of An [4] concern different graphs and do not determine this exact configuration space. Maciążek–Sawicki [5] analyze graph braid homology and torsion examples, but the inspected material does not give the stated Möbius–Kantor computation. Previously indexed results for the **independence**, **matching**, and **cut** complexes of the same finite graph, and three-particle configuration spaces of the Heawood and Pappus graphs, address distinct topological objects or input graphs. The equalities here are not inferred from any of those computations.

## Limitations
The result determines the free third-homology group and the complete order-two subgroup of second homology. It **does not** determine the free rank of second homology, all possible odd torsion, or whether second homology contains elements of order four or higher. No claim is made about all generalized Petersen graphs or an equivariant decomposition. Full publication-priority assessment remains incomplete: another source under a different graph alias (Knödel graph or honeycomb toroidal graph) or a broader unindexed computation may contain an equivalent statement. The computational proof depends on reproducible finite certificates and the published integral chain model; independent mathematical audit has not been performed.

## References
1. K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648v1 (first public 2011-01-13), https://arxiv.org/abs/1101.2648.
2. B. H. An, G. C. Drummond-Cole, and B. Knudsen, *Subdivisional spaces and graph braid groups*, arXiv:1708.02351, https://arxiv.org/abs/1708.02351.
3. B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371, https://arxiv.org/abs/2008.10371.
4. B. H. An, *Torsion of every finite order in the homology of graph braid groups*, arXiv:2610.04305 (2026), https://arxiv.org/abs/2610.04305.
5. T. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, Communications in Mathematical Physics (2019), DOI:10.1007/s00220-019-03583-5.
6. E. W. Weisstein, *Möbius–Kantor Graph*, MathWorld, https://mathworld.wolfram.com/Moebius-KantorGraph.html.
