# Mixed-dimensional integral homotopy of the octagonal-bipyramid matching complex

## Finding
Let \(B_8=C_8*\overline{K_2}\) be the graph of the octagonal bipyramid and let \(\mathcal M(B_8)\) be its *ordinary matching complex*. The exact integral homotopy type is
\[
\mathcal M(B_8)\simeq S^2\vee S^2\vee\bigvee^{9}S^3.
\]
In particular \(\widetilde H_2(\mathcal M(B_8);\mathbb Z)\cong\mathbb Z^2\), \(\widetilde H_3(\mathcal M(B_8);\mathbb Z)\cong\mathbb Z^9\), and all remaining reduced integral groups vanish.

## Assumptions and scope
This is a finite exact statement for one natural convex-polyhedral graph, not a claim for arbitrary polygonal bipyramids. The original graph has ten vertices numbered \(0,\ldots,9\). The rim is \(C_8\) on \(0,\ldots,7\); the nonadjacent apices are \(8,9\). In the edge index convention the eight rim edges \(\{i,(i+1)\bmod 8}\), for \(0\le i<8\), have indices \(0\) through \(7\); the apex-8 edges \(\{i,8}\) have indices \(8\) through \(15\), and the apex-9 edges \(\{i,9}\) have indices \(16\) through \(23\). A simplex of \(\mathcal M(B_8)\) is exactly any subset of these 24 indexed edges with disjoint endpoint sets. Orient each simplex by increasing edge index.

## Proof
**Exact exhaustive face set.** Enumerating all increasing edge subsets subject only to disjointness gives 951 faces, including the empty face, and the nonempty face vector \((24,172,416,306,32)\) by dimensions \(0,1,2,3,4\). The included `verify.py` reconstructs this list directly from the stated edge set; `certificate.json` stores the complete matching certificate.

**Acyclic matching.** Process edge indices in this fixed order:
`[18,11,4,6,5,10,0,3,9,2,20,21,12,22,15,7,16,17,8,1,13,19,14,23]`.
At each index \(v\), simultaneously match every still-available face \(\sigma\) not containing \(v\) for which \(\sigma\cup\{v}\) remains available, and remove both faces. This produces 468 facet pairs, leaving precisely four unpaired 2-faces and eleven unpaired 3-faces. The empty face is paired with one vertex; in the ordinary CW reduction there is a single 0-cell. Verify acyclicity by orienting every matched facet incidence upward and every unmatched incidence downward. The independently reconstructed directed Hasse graph has exactly 951 nodes and a topological ordering visiting all 951; thus it is acyclic and Forman's theorem applies.

**Integral attaching degrees.** The signed integral Morse boundary between the eleven 3-cells (columns) and the four 2-cells (rows) is, using the ascending critical-face ordering,
\[
\partial_3=\begin{pmatrix}
0&-1&0&1&1&0&0&0&-1&1&0\\
0&1&0&-1&-1&1&-1&0&1&-1&0\\
0&1&0&-1&-1&1&-1&0&1&-1&0\\
0&0&0&0&0&-1&1&0&0&0&0
\end{pmatrix}.
\]
It is obtained by exact recursive signed gradient-path cancellation, specified and reproduced by `verify.py`; no floating-point arithmetic is used. Its second and third rows agree; the first, second and fourth rows sum to zero. Hence its integral rank is at most two. The minor using rows one and four, columns two and six (all one-based) has determinant \(1\), so the rank is two and its two nonzero Smith factors are both \(1\). In particular there is no integral torsion.

**Homotopy conclusion.** Forman's CW model consists of one 0-cell, four 2-cells and eleven 3-cells, with no 1-cells or higher cells. Its 2-skeleton is \(\bigvee^4 S^2\). By the Hurewicz theorem \(\pi_2(\bigvee^4 S^2)\cong\mathbb Z^4\), so the integral degree matrix completely classifies all eleven attaching maps. Unimodular changes of the two- and three-cell bases carry the matrix to diagonal form with two unit entries and all others zero. The two unit attachments cancel two 2-spheres against two 3-cells; the other nine 3-cells attach trivially. The asserted wedge decomposition follows, with integral \(\widetilde H_2\) of rank two and \(\widetilde H_3\) of rank nine.

## Verification
Run `python3 verify.py certificate.json` in any Python 3 environment; `verify.py` requires only the standard library. It independently regenerates the graph and all 951 simplices, recomputes the 468 pairs and fifteen critical faces, checks the complete 951-node reversed Hasse graph for cycles, computes the signed integer Morse differential from every gradient path, and verifies rank two with an explicitly unit minor. A separate mod-two simplicial boundary computation yields reduced Betti ranks \(2\) in degree two and \(9\) in degree three, zero otherwise. The expected command output is included in `verification_output.txt`. These finite computations are exhaustive for this specified finite complex, not experimental extrapolation.

## Relationship to prior work
Barik, Mondal and Mukherjee's 2026 construction gives discrete-Morse matchings for independence complexes under a simplicial-vertex hypothesis and several defined graph classes. Although \(\mathcal M(B_8)=\operatorname{Ind}(L(B_8))\), every edge of \(B_8\) has two endpoints of degree at least four; its line-graph vertex neighborhood contains disjoint original edges and hence is not a clique. Thus that theorem's simplicial-vertex hypothesis fails and its application results do not provide this exact wedge.

Bayer, Jelić Milutinović and Vega's 2024 outerplanar-graph theorem cannot imply the conclusion: \(B_8\) has ten vertices and 24 edges, exceeding the outerplanar upper bound of 17 edges. Bayer, Goeckner and Jelić Milutinović's 2019 theorem classifies graph matching complexes which themselves are homology manifolds, not arbitrary non-manifold mixed-dimensional wedges. A publicly indexed 2026 description of Xu's *A Planar Counterexample to the Sphere-Wedge Conjecture for Matching Complexes* treats the **pentagonal** bipyramid and its torus matching complex; it does not state a classification of the **octagonal** bipyramid. That latter original full manuscript could not be inspected, leaving a literature-overlap caveat.

## Limitations
The result is a complete finite homotopy calculation for the single graph \(B_8\). No classification for other bipyramid sizes, no equivariant decomposition, and no statement about arbitrary planar graphs is proved. The finite exhaustive certificate is not an independent mathematical audit, and an inaccessible or unindexed stronger prior theorem could supersede the originality assessment.

## References
- Sucharita Barik, Anupam Mondal and Sajal Mukherjee, *A recursive construction of an acyclic matching on the independence complex of a graph with a simplicial vertex*, arXiv:2604.12606 (public 2026-04-14), https://arxiv.org/html/2604.12606v1.
- Margaret Bayer, Marija Jelić Milutinović and Julianne Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601 (public 2024-11-07), https://arxiv.org/html/2411.04601v2.
- Margaret Bayer, Bennet Goeckner and Marija Jelić Milutinović, *Manifold Matching Complexes*, arXiv:1906.03328 (public 2019-06-07), https://arxiv.org/html/1906.03328v3.
- Zihuan Xu, *A Planar Counterexample to the Sphere-Wedge Conjecture for Matching Complexes*, Zenodo record 23437631 (publicly indexed October 17, 2026), https://zenodo.org/records/23437631 (primary full text not retrieved).
