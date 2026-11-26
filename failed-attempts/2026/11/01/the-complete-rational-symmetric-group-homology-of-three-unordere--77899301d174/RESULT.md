# The complete rational symmetric-group homology of three unordered particles on the Petersen graph

## Finding
Let \(P=\mathrm{KG}(5,2)\) be the Petersen graph, and let \(B_3(P)\) be the unordered configuration space of three pairwise distinct points on its underlying topological graph. For the natural \(S_5=\mathrm{Aut}(P)\)-action, the complete nonzero rational homology modules are
\[
H_0(B_3(P);\mathbb Q)\cong\mathbf1,\qquad
H_1(B_3(P);\mathbb Q)\cong S^{(3,1,1)},
\]
\[
H_2(B_3(P);\mathbb Q)\cong S^{(2,1,1,1)}\oplus S^{(3,2)}\oplus 2S^{(2,2,1)}\oplus S^{(3,1,1)}.
\]
Here \(S^\lambda\) denotes the rational Specht module for partition \(\lambda\) of five. Their dimensions are \(1,6,25\), respectively; \(H_i(B_3(P);\mathbb Q)=0\) for \(i\ge3\). The degree-two character on the conjugacy types \((1^5),(2,1^3),(3,1^2),(2^2,1),(4,1),(3,2),(5)\) is
\[
(25,-3,-2,1,1,0,0).
\]
No nonconstant rational homology class is invariant under all automorphisms. Therefore the orbit space \(B_3(P)/S_5\) is **rationally acyclic**. Contractibility is not claimed.

## Assumptions and scope
The Petersen graph has vertices the ten unordered two-subsets of \(\{0,1,2,3,4\}\); two vertices are joined precisely when they are disjoint. Thus it has ten vertices, fifteen edges, and three edges incident to every vertex. Configurations are unordered sets of exactly three distinct points in the topological realization, not triples of graph vertices. This distinction is essential.

All homology assertions in this finding are over \(\mathbb Q\), except the explicitly noted injectivity of one integral differential. The full symmetry action is by permutations of the five underlying symbols. The exact computations use the weight-three **reduced Świątkowski complex** of the graph; its homology is naturally the homology of the topological configuration space, by the comparison theorem in [1, §4] and [2, §2].

## Proof
At each graph vertex \(v\), order its three incident edges \(e_0(v),e_1(v),e_2(v)\) and take the local generators \(1\) in homological degree zero and \(h_1(v)-h_0(v)\), \(h_2(v)-h_0(v)\) in degree one. Tensor these local modules with the polynomial ring on all fifteen graph edges. Each edge-variable has weight one and homological degree zero; each local difference has weight one and degree one. Restrict to weight exactly three. The differential removes a local difference, replacing it by \(e_i(v)-e_0(v)\), with Koszul signs when more than one local difference occurs. Thus the complex has ranks
\[
(\operatorname{rank} C_0,\operatorname{rank} C_1,\operatorname{rank} C_2,\operatorname{rank} C_3)=(680,2400,2700,960).
\]
There are no higher chain groups. The accompanying standard-library checker constructs each basis as an ordered set of local generators together with a degree-complementary sorted multiset of edges; it checks \(\partial^2=0\) over the integers and performs exact finite-field elimination. Its boundary ranks in degrees \((1,2,3)\) are \((679,1715,960)\) modulo three and five, and \((679,1714,960)\) modulo two.

These finite-field computations give **lower** bounds on rational ranks; here the matching upper bounds have independent proofs. Every degree-zero differential column sums to zero, giving \(\operatorname{rank}_{\mathbb Q}\partial_1\le679\). For the second differential, consider the natural Abel–Jacobi map sending an unordered three-particle motion to its total oriented graph path. The six explicitly listed Petersen pentagons
\[
(0,7,3,4,9),\ (0,7,3,5,8),\ (0,7,6,1,9),\ (0,7,6,2,8),\ (0,8,2,4,9),\ (0,8,5,1,9)
\]
are expressed in the canonical lexicographic ordering of the ten two-subset vertices. Each pentagon has at least two outside vertices at which the other particles can be fixed. The resulting six one-particle-traversal loops in \(B_3(P)\) map to linearly independent graph cycles: the certificate checks their fifteen-edge signed incidence vectors have rank six modulo \(101\). Since the connected graph has cycle rank \(15-10+1=6\), these cycles span \(H_1(P;\mathbb Q)\). In particular, \(\dim H_1(B_3(P);\mathbb Q)\ge6\). Combining this with the rank-\(679\) lower bound for \(\partial_1\) gives \(\operatorname{rank}_{\mathbb Q}\partial_2\le2400-679-6=1715\). Together with the finite-field lower bound, both ranks are exact; \(\partial_3\) is injective over \(\mathbb Q\) because all its \(960\) columns are independent modulo three. Therefore
\[
(\beta_0,\beta_1,\beta_2,\beta_3)=(1,6,25,0).
\]
The six pentagon loops also make the Abel–Jacobi map onto \(H_1(P;\mathbb Q)\). As source and target both have dimension six, it is an \(S_5\)-equivariant isomorphism in degree one. The graph cycle-space character is the signed edge-permutation character minus the vertex-permutation character plus the trivial character; it is \(S^{(3,1,1)}\).

For each of the seven cycle types of \(S_5\), the checker represents the induced permutation on the ten graph vertices, fifteen edges, and the reduced halfedge-difference bases. It enumerates all fixed basis vectors with their Koszul and local-change-of-basis signs, obtaining the chain traces below. By the equivariant Euler–Poincaré formula and the preceding degree-zero and degree-one determinations, the fourth column determines the degree-two character.

| Cycle type | Class size | Trace on \((C_0,C_1,C_2,C_3)\) | \(\mathrm{tr}(H_1)\) | \(\mathrm{tr}(H_2)\) |
|---|---:|---|---:|---:|
| \((1^5)\) | 1 | \((680,2400,2700,960)\) | 6 | 25 |
| \((2,1^3)\) | 10 | \((28,24,-18,-12)\) | 0 | -3 |
| \((3,1^2)\) | 20 | \((5,0,0,6)\) | 0 | -2 |
| \((2^2,1)\) | 15 | \((28,0,-24,0)\) | -2 | 1 |
| \((4,1)\) | 30 | \((2,0,0,0)\) | 0 | 1 |
| \((3,2)\) | 20 | \((1,0,0,0)\) | 0 | 0 |
| \((5)\) | 24 | \((0,0,0,0)\) | 1 | 0 |

Inner products of the degree-two character with the seven rational irreducible characters are, in partition order \((5),(1^5),(4,1),(2,1,1,1),(3,2),(2,2,1),(3,1,1)\), exactly \((0,0,0,1,1,2,1)\). This yields the asserted module decomposition. The degree-one character has no trivial constituent; neither does degree two. For a finite group acting on a space, rational homology of the quotient agrees with the invariant rational homology. All reduced invariants vanish here, proving rational acyclicity of the quotient.

## Verification
Run `python3 verify_petersen_B3.py` with Python's standard library. The script reconstructs all graph data, the four weight-three basis layers, all signed boundary columns, the integer chain-complex identity, modular ranks for primes two, three, five, all six pentagon cycle vectors, the seven conjugacy-class traces and irreducible multiplicities. The exact recorded output is `verification_output.txt`. The final line is `PETERSEN_THREE_PARTICLE_RATIONAL_CHARACTER_VERIFIED`. The computations are finite and exhaustive for the stipulated weight and graph; the topological identification and rank bounds are proved in the preceding argument.

## Relationship to prior work
The reduced Świątkowski model and natural comparison theorem are established in [1] and [2]; those are **not** claimed as new. The 2020 work [2] highlights unresolved nonplanar graph-braid second homology, while its principal generator theorem concerns planar graphs and hence does not determine the present Petersen calculation. The earlier first-homology work [3] does not imply the second-homology character. Computations for *two* particles on the Petersen graph, for *three* particles on the Heawood and Pappus graphs, or for different simplicial constructions on the Petersen graph have different spaces or particle counts. Relevant indexed and primary-source searches did not identify a theorem implying this specific degree-two \(S_5\)-module. Absence from searched sources is not a proof of universal novelty.

## Limitations
The proof establishes the complete **rational** homology representation for exactly three unordered particles on the Petersen graph. It does not classify integral torsion, determine cohomology products, prove that the symmetry quotient is contractible, or provide an all-particle-count or all-graph-family formula. The mod-two Betti ranks differ from the rational ranks in degrees one and two; this is explicitly not interpreted here as an integral torsion classification. Other unindexed or inaccessible equivalents remain possible.

## References
[1] B. H. An, G. C. Drummond-Cole, B. Knudsen, *Subdivisional spaces and graph braid groups*, arXiv:1708.02351, §§1,4; first public August 8, 2017, published *Documenta Mathematica* 24 (2019).
[2] B. H. An, B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371 (first public August 24, 2020), §§1–2, *Journal of Topology* 15 (2022), 666–691, doi:10.1112/topo.12228.
[3] K. H. Ko, H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648 (2011), *Discrete & Computational Geometry* 48 (2012), 915–963.
