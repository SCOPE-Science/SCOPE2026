# All nonidentity subgroup-fixed homotopy types of the Heawood matching complex

## Finding
Let \(H\) be the Heawood graph, the fourteen-vertex point–line incidence graph of the Fano plane, and let \(K=\mathcal M(H)\) be its **ordinary matching complex**: the vertices of \(K\) are the twenty-one incidence edges, and simplices are collections of pairwise disjoint graph edges. The full automorphism group \(G=\operatorname{Aut}(H)\) has order \(336\).

For every nonidentity subgroup \(U\leq G\), the geometric fixed-point space \(|K|^U\) has **exactly one** of the following seven homotopy types. The complete census, including the number of subgroups realizing each type, is

| Geometric fixed-space type | Number of subgroups |
|---|---:|
| Empty | 46 |
| Contractible | 105 |
| Two isolated points, \(S^0\) | 140 |
| Three isolated points, \(S^0\vee S^0\) | 30 |
| \(S^1\vee S^1\) | 42 |
| \(\bigvee^4 S^2\) | 28 |
| \(S^1\vee S^2\) | 21 |
| **Total** | **412** |

There are \(413\) subgroups of \(G\), including the trivial subgroup, in \(23\) conjugacy classes. Thus the census covers exactly \(22\) nonidentity classes. The \(28\)-subgroup polarity-involution class with fixed space \(\bigvee^4 S^2\) was determined in an earlier published calculation; **this class is prior work**. The contribution asserted here is the exhaustive all-nonidentity-subgroup classification, particularly the order-two class not covered in the inspected literature with mixed homotopy \(S^1\vee S^2\).

## Assumptions and scope
Identify the seven points with nonzero vectors \(x\in\mathbb F_2^3\); a Fano line is a three-point set \(\{x,y,x+y\}\) for independent nonzero \(x,y\). The Heawood graph has one vertex for every point and line, joining incident pairs. Its automorphism group consists of the \(168\) invertible linear maps and their compositions with the orthogonal point–line polarity. The latter sends a point \(x\) to the line \(\{y:x\cdot y=0\}\), and conversely. Both types are retained: no restriction to incidence-preserving automorphisms is made.

Geometric fixed points refer to **fixed points of the topological realization** rather than to the simplicial subcomplex of individually fixed edge-vertices. In particular, the barycenter of a two-edge orbit may represent a genuine fixed-space vertex. An empty fixed space is interpreted literally as the empty topological space. Conjugate subgroups have isomorphic geometric fixed spaces.

## Proof
**1. The full group and subgroup census.** An incidence-preserving automorphism is determined by the images of any three noncollinear Fano points, each image triple being a basis of \(\mathbb F_2^3\), so there are \(168\) such automorphisms. A fixed polarity exchanges the two bipartition classes; because the incidence graph is connected and bipartite, every remaining automorphism is a composition with this polarity. Hence the full order is \(336\).

The exact finite verification enumerates this group as permutations of fourteen vertices, constructs its complete multiplication and inverse tables, and starts with the identity subgroup. For every subgroup already obtained and every group element outside it, it adjoins that element and takes the generated subgroup. As every subgroup has a finite generating sequence, this procedure exhausts all subgroups. The resulting count is \(413\). Direct conjugation partitions them into \(23\) conjugacy classes; one is trivial and the other \(22\) have total size \(412\).

**2. Geometric fixed-space reduction.** For a subgroup \(U\) acting on the twenty-one matching-complex vertices, a fixed point has equal barycentric coordinates along each orbit. Consequently \(|K|^U\) is PL-homeomorphic to the simplicial complex whose vertices are the orbits of incidence edges that are themselves matchings, and whose faces are collections of these orbits whose unions remain matchings. The finite checker verifies this description independently by enumerating all \(3,461\) nonempty matchings of \(H\) and comparing the setwise-invariant matchings directly with orbit-model faces for every subgroup representative.

**3. Exhaustive elementary collapses.** For each representative, enumerate its edge-orbit face complex. Repeatedly choose a nonempty codimension-one face contained in exactly one strictly larger face; delete that free face and its unique coface. The accompanying certificate records every deletion. Each is a genuine elementary simplicial collapse, hence a homotopy equivalence. For all twenty-two representatives, the remaining complexes have dimensions at most two and are described by the following complete class table.

| Class | Subgroup order | Conjugates | Fixed-space homotopy type | Admissible edge orbits | Nonempty faces |
|---:|---:|---:|---|---:|---:|
| 1 | 2 | 21 | \(S^1\vee S^2\) | 9 | 69 |
| 2 | 2 | 28 | \(\bigvee^4 S^2\) | 12 | 137 |
| 3 | 3 | 28 | Two points, \(S^0\) | 5 | 8 |
| 4 | 4 | 14 | Three points, \(S^0\vee S^0\) | 3 | 3 |
| 5 | 4 | 21 | Contractible | 3 | 5 |
| 6 | 4 | 42 | \(S^1\vee S^1\) | 6 | 19 |
| 7 | 6 | 28 | Two points, \(S^0\) | 3 | 4 |
| 8 | 6 | 28 | Two points, \(S^0\) | 4 | 6 |
| 9 | 6 | 28 | Two points, \(S^0\) | 2 | 2 |
| 10 | 7 | 8 | Three points, \(S^0\vee S^0\) | 3 | 3 |
| 11 | 8 | 21 | Contractible | 1 | 1 |
| 12 | 8 | 21 | Contractible | 1 | 1 |
| 13 | 8 | 21 | Contractible | 3 | 5 |
| 14 | 12 | 14 | Empty | 0 | 0 |
| 15 | 12 | 28 | Two points, \(S^0\) | 2 | 2 |
| 16 | 14 | 8 | Three points, \(S^0\vee S^0\) | 3 | 3 |
| 17 | 16 | 21 | Contractible | 1 | 1 |
| 18 | 21 | 8 | Empty | 0 | 0 |
| 19 | 24 | 14 | Empty | 0 | 0 |
| 20 | 42 | 8 | Empty | 0 | 0 |
| 21 | 168 | 1 | Empty | 0 | 0 |
| 22 | 336 | 1 | Empty | 0 | 0 |


**4. The easy residual types.** A residual complex with no nonempty faces is empty. One, two, or three isolated vertices give the corresponding discrete spaces. A residual connected graph with six edges and five vertices has first Betti number two and is a wedge of two circles. These observations settle all but the two involution classes.

**5. The mixed-dimensional involution class.** In the order-two class with \(21\) conjugates, the orbit model has nine vertices and \(69\) nonempty faces. Twenty elementary collapses leave exactly eight triangles forming the suspension of a four-cycle: the base cycle is \(1-3-2-4-1\), and the suspension vertices are \(5\) and \(6\). This suspension is a two-sphere. The remaining edges \(0-5\) and \(0-6\) form an extra path joining two points of the sphere, adding a circle. Hence this fixed space is \(S^1\vee S^2\), proving both dimensions of its integral homotopy type, not only its homology ranks.

**6. The polarity-type involution class.** In the other order-two class, containing \(28\) subgroups, the orbit model has twelve vertices and \(137\) nonempty faces. Thirty-two elementary collapses leave a connected two-complex with \(12\) vertices, \(34\) edges and \(27\) triangles, so its Euler characteristic is \(5\). Contracting a chosen spanning tree gives a presentation of its fundamental group with \(23\) generators. The triangle relators successively eliminate all \(23\) generators by one-letter Tietze eliminations, as verified by the standalone program; consequently the fundamental group is trivial. A simply connected finite two-dimensional CW complex with Euler characteristic five has free second integral homology of rank four and is homotopy equivalent, by Hurewicz and Whitehead, to \(\bigvee^4 S^2\). This reproduces the previously published polarity fixed-space type by a separate finite certificate; no novelty is attributed to the isolated polarity calculation.

Since conjugation is realized by simplicial automorphisms, the classification of representatives gives the classification of every nonidentity subgroup. This completes the proof.

## Verification
Place `verify_fixed.py` beside `census.json` and run `python3 verify_fixed.py` using Python 3.10 or later. Only the Python standard library is required. The verifier reconstructs all \(336\) graph automorphisms, generates \(413\) subgroups, computes \(23\) conjugacy classes, independently enumerates the \(3,461\) nonempty matching faces, checks geometric invariance against the orbit-face models, verifies every recorded elementary collapse, and recomputes reduced mod-two homology. It checks both involution residual complexes; in the second case it verifies the explicit triangular-relator elimination of all \(23\) fundamental-group generators. It compares the entire recomputed census against `census.json` and prints `ALL_HEAWOOD_MATCHING_SUBGROUP_FIXED_HOMOTOPY_TYPES_PASS`. `verification_output.txt` records one successful execution. Mod-two ranks alone are not used as an integral homotopy certificate.

## Relationship to prior work
Björner, Lovász, Vrećica and Živaljević (1994) established foundational matching- and chessboard-complex topology; that work is the dated archive starting point. More specific published calculations establish \(\mathcal M(H)\simeq\bigvee^{16}S^4\), determine the complete rational \(336\)-automorphism character of its fourth homology, and identify a polarity-involution geometric fixed locus as \(\bigvee^4S^2\). The last of these **already covers the complete 28-subgroup class** in this census. The rational character by itself, however, cannot determine geometric fixed-space integral homotopy types, and the isolated polarity result does not classify the other twenty-one nonidentity conjugacy classes. The new mixed \(S^1\vee S^2\) class, alongside the full distribution of other fixed-space types, is not entailed by the inspected prior statements. Source- and claim-level comparisons, including the covered polarity class, are recorded in `AUDIT.json`.

## Limitations
This is an exhaustive finite theorem for the Heawood graph and its full automorphism group, not a formula for all incidence graphs or projective planes. The classification concerns strict geometric fixed points, not homotopy-fixed points or arbitrary symmetry quotients. All nonidentity subgroups are classified, whereas the trivial subgroup has the previously known ordinary homotopy type and is intentionally excluded from the new census. Computation certifies finite subgroup enumeration and elementary collapses; the homotopy deductions use the proved combinatorial models and classical topology. Independent mathematical audit and definitive historical publication-priority review are not performed. The existence of an equivalent older or differently indexed all-subgroup classification remains possible.

## References
1. A. Björner, L. Lovász, S. T. Vrećica, R. T. Živaljević, *Chessboard Complexes and Matching Complexes*, Journal of the London Mathematical Society 49 (1994), 25–39. DOI: 10.1112/jlms/49.1.25; first published 1994-02-01.
2. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
3. *The Heawood matching complex is a wedge of sixteen 4-spheres*, published mathematical report, identifier 7150930ba12a (2026).
4. *Full automorphism module of the Heawood matching complex*, published mathematical report, identifier d7a042784870 (2026).
5. *Four two-spheres in the Fano-polarity fixed locus of the Heawood matching complex*, published mathematical report, identifier 83468460611c (2026).
