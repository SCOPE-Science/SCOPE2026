# The full symmetric-group character of the tetrahedral discrete-Morse complex

## Finding
Let \(K=\Delta^3\) be the full tetrahedron on four labeled vertices, and let \(X=\mathcal M(K)\) be its ordinary (non-pure) complex of acyclic discrete-Morse matchings. Its natural \(S_4\)-action on rational fourth homology has character, in cycle-type order \((1^4),(2,1,1),(2,2),(3,1),(4)\),
\[
\chi_{\widetilde H_4}(g)=(99,1,-1,0,-1).
\]
Consequently the full rational isotypic decomposition is
\[
\widetilde H_4(X;\mathbb Q)\cong 4S^{(4)}\oplus13S^{(3,1)}\oplus8S^{(2,2)}\oplus12S^{(2,1,1)}\oplus4S^{(1,1,1,1)}.
\]
In particular \(\dim\widetilde H_4(X;\mathbb Q)^{S_4}=4\), and the sign-isotypic subspace also has dimension four. The known nonequivariant homotopy type is \(X\simeq\bigvee^{99}S^4\), due to Scoville; it is not a new claim here.

## Assumptions and scope
The 15 nonempty faces of \(K\) are encoded by the nonzero four-bit masks. The 28 vertices of \(X\) are Hasse arrows \(a\subset b\) with \(|b|=|a|+1\). A set of these arrows is a simplex exactly when the arrows are disjoint as pairs of faces and the directed Hasse diagram, oriented from smaller to larger face except with selected arrows reversed, has no directed cycle. The empty matching is not a vertex or simplex of \(X\). The \(S_4\)-action permutes the four labels, hence the 15 faces and the 28 arrows. Specht modules and character decompositions are over \(\mathbb Q\).

## Proof
For an automorphism \(g\), consider the induced action on the 28 vertices of \(X\), and split these vertices into \(g\)-orbits. A simplex \(W\) is fixed as a set exactly when it is the union of complete orbits. If the included orbits have sizes \(\ell_1,\ldots,\ell_b\), then the permutation of the \(|W|\) oriented simplex vertices has sign \((-1)^{|W|-b}\). Its contribution to the simplicial Lefschetz number is therefore \((-1)^{|W|-1}(-1)^{|W|-b}=(-1)^{b-1}\). This gives a rigorous integer formula requiring only the enumeration of admissible collections of complete arrow-orbits.

For one representative of each cycle type the exhaustive orbit-count table below lists the number of admissible nonempty unions containing exactly \(b\) arrow-orbits, for \(b=1,2,\ldots\). A union is tested for both disjoint endpoints and acyclicity of the reversed Hasse diagram. Every other group element is conjugate to a representative and has the same count.

| Cycle type | Orbit-union count by \(b\ge1\) | Lefschetz number |
| --- | --- | ---: |
| \((1^4)\) | \((28,300,1544,3932,4632,2128,256)\) | \(100\) |
| \((2,1,1)\) | \((10,36,56,36,8)\) | \(2\) |
| \((2,2)\) | \((8,8)\) | \(0\) |
| \((3,1)\) | \((3,3,1)\) | \(1\) |
| \((4)\) | empty | \(0\) |

The orbit counts come from the complete finite algorithm in `orbit_check.py`. For an independent method, `tetra_sym.py` enumerates all 12,820 nonempty simplices and computes each fixed oriented simplex's permutation sign directly, for all 24 group elements; both methods agree. The first row also reproduces Scoville's published \(f\)-vector.

Scoville proved that \(X\) is connected and \(\widetilde H_i(X;\mathbb Q)=0\) for \(i\ne4\), with \(\dim\widetilde H_4(X;\mathbb Q)=99\) [1, Theorem 20 and Tables 1–2]. Thus only \(H_0\cong\mathbb Q\) and \(H_4\cong\mathbb Q^{99}\) contribute to the homological Lefschetz number. Both degrees are even, and \(H_0\) has trace one. Subtracting one from the third column yields \((99,1,-1,0,-1)\).

The five irreducible \(S_4\)-characters, in the same conjugacy-class order, are \((1,1,1,1,1)\), \((3,1,-1,0,-1)\), \((2,0,2,-1,0)\), \((3,-1,-1,0,1)\), and \((1,-1,1,1,-1)\). The class sizes are \((1,6,3,8,6)\). Their character inner products with \((99,1,-1,0,-1)\), divided by 24, are exactly \((4,13,8,12,4)\). These multiplicities are nonnegative integers, and the dimension sum \(4+39+16+36+4=99\) cross-checks the decomposition.

## Verification
The attached `tetra_sym.py` recreates the nonempty-face Hasse diagram, enumerates acyclic partial matchings, verifies the full face vector, evaluates signed simplicial traces on every group element, checks conjugacy-class invariance, and computes Specht multiplicities. The independent `orbit_check.py` instead enumerates complete arrow-orbit unions, testing each for endpoint disjointness and directed acyclicity; it reproduces all five Lefschetz numbers. `mod2_check.py` constructs mod-two boundary maps on the entire complex and verifies ordinary Betti numbers \((1,0,0,0,99,0,0)\). Executable results are recorded in `VERIFY_OUTPUT.txt`. The rational character proof depends on the known integral homology concentration from [1], not on extrapolating mod-two checks.

## Relationship to prior work
Scoville [1] proved the nonequivariant homotopy type and enumerated the same face vector, but its Theorem 20 and Tables 1–2 report homology ranks rather than the representation of \(S_4\). Lin and Scoville [2] established the automorphism-group structure of Morse complexes, which makes the natural \(S_4\) action canonical, but does not determine its homology character. The present computation determines the character and all Specht constituents. A related calculation for the *pure* Morse complex of the *boundary* tetrahedron concerns degree-three homology, and neither its domain nor its statement implies this degree-four representation of the full non-pure tetrahedron.

## Limitations
The result is a finite four-vertex calculation, not a formula for larger simplices, not an integral \(\mathbb Z[S_4]\)-lattice decomposition, and not a full equivariant homotopy classification. Although exact finite enumeration gives a mathematical proof, unindexed equivalent computations in the literature remain a possible novelty risk; independent scholarly review has not been performed.

## References
[1] N. A. Scoville, *The complex of discrete Morse matchings of the n-simplex: homotopy types and structural results*, arXiv:2604.18172v1 (first submitted 2026-04-20), especially Definitions 1–3, Section 5.1, Tables 1–2, Theorem 20. https://arxiv.org/abs/2604.18172

[2] M. Lin and N. A. Scoville, *On the automorphism group of the Morse complex*, arXiv:1904.10907v1 (2019), journal version: Advances in Applied Mathematics 131 (2021), 102250. https://arxiv.org/abs/1904.10907
