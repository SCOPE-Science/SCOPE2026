# Cross-free triple placements distinguish the two thirteen-point Steiner systems

## Finding

Let \(\mathcal S_c\) and \(\mathcal S_n\) be the cyclic and noncyclic Steiner triple systems on thirteen points, respectively, with the explicit block sets defined below. A **cross-free placement of size three** is an *unordered* collection \(\{A,B,C\}\) of pairwise disjoint three-point sets such that no block of the Steiner system meets all three sets. The vertex set of its exchange graph \(\mathcal R(\mathcal S)\) consists of all such placements; two vertices are adjacent if one selected point in exactly one class is replaced by one of the four unused points, with the other two classes unchanged (class names do not matter).

The two exchange graphs have **different complete component-size and small-component-shape classifications**:

| Design | Placements | Exchanges | Connected components |
| --- | ---: | ---: | --- |
| Cyclic \(\mathcal S_c\) | 6214 | 25896 | One connected 5902-vertex graph, \(39K_4\), and \(156K_1\) |
| Noncyclic \(\mathcal S_n\) | 6148 | 25032 | One connected 5904-vertex graph, \(18K_4\), four copies of two \(K_4\)'s identified at exactly one vertex, and \(144K_1\) |

Thus a single Pasch switch changes the total number of extremal cross-free placements by 66 and changes the topology of their single-point replacement components. The common placements number 3868; 2346 occur only in \(\mathcal S_c\), and 2280 only in \(\mathcal S_n\). There are respectively 196 and 167 connected components. Every nontrivial component outside the unique giant is a four-clique or, only in the noncyclic case, a seven-vertex union of two four-cliques meeting in one point.

The largest possible cross-free size in either design is three. The upper bound is a short general counting argument; the exact enumerations and graph component classifications are computer-assisted finite theorems, established by complete enumeration over precisely \(\binom{13}{3}\binom{10}{3}\binom{7}{3}/6=200200\) unordered candidate placements per design. These claims cover **both** isomorphism types of Steiner triple systems of order thirteen, not all higher orders.

## Assumptions and scope

Use the point set \(V=\mathbb Z/13\mathbb Z\), written with residues 0 through 12. Every block has three distinct points. The cyclic design \(\mathcal S_c\) has precisely the translates modulo 13 of the starter triples \(\{1,3,9\}\) and \(\{2,5,6\}\), giving 26 blocks. Construct \(\mathcal S_n\) by deleting

\[
\{2,4,10\},\quad\{2,5,6\},\quad\{4,6,12\},\quad\{5,10,12\}
\]

and inserting

\[
\{2,4,6\},\quad\{2,5,10\},\quad\{4,10,12\},\quad\{5,6,12\}.
\]

These are the cyclic and noncyclic isomorphism classes respectively, by the classical classification of the order-thirteen Steiner triple systems; the generators and switch are also documented in Pavone's detailed description [2]. The accompanying programs independently verify the defining pair-uniqueness property for both block sets, so no unverified block table is being assumed. Classes \(A,B,C\) are **unlabelled**: the six permutations of three class names represent the same placement. Points themselves remain labelled by their residues. The word exchange always means removal of exactly one selected point followed by addition of exactly one previously unused point to the same class, without changing the number of points in any class.

## Proof

**The maximal size is at most three.** Suppose four-point classes \(A,B,C\) were pairwise disjoint and cross-free. Their union would contain twelve points and there would be just one unused point \(u\). Each block not containing \(u\) must contain two points from some common class: otherwise its three points, all selected, would lie in three different classes and violate cross-freeness. There are \(26-6=20\) blocks avoiding \(u\), since each point belongs to six blocks of an order-thirteen Steiner triple system. But the three four-point classes contain only \(3\binom42=18\) same-class pairs, and different blocks cannot share a pair. This is impossible. Any larger three-class placement contains a four-point subplacement, so four is excluded for all larger sizes. Three-point witnesses appear in the two independent verification programs and in the next paragraph, proving equality.

For explicit witnesses, convert the following displayed indices from 1-based to the residues above: \(\{1,2,3\},\{4,5,8\},\{7,9,12\}\) is cross-free in \(\mathcal S_c\); \(\{1,2,3\},\{4,5,8\},\{9,11,12\}\) is cross-free in \(\mathcal S_n\). Every block is tested against each witness by the supplied programs.

**Exchange lemma.** For any three disjoint equal-size classes \(A,B,C\) in any triple system and unused \(y\), adding \(y\) to \(A\) preserves cross-freeness precisely when there is no block containing \(y\), one point of \(B\), and one point of \(C\). This criterion does not depend on which point of \(A\) is removed. Hence, for each eligible unused point \(y\), replacing *any* member of \(A\) by \(y\) is legal, while for each ineligible \(y\) no replacement from \(A\) is legal. In particular, every degree in the size-three exchange graph is divisible by three, and each eligible insertion gives a complete \(K_4\) comprising the four ways of retaining three of the four points of \(A\cup\{y\}\). This lemma explains why a small nontrivial component can be a \(K_4\), and permits an independent consistency check on the enumerated adjacency.

**Complete finite classification.** Every unordered placement occurs exactly once when one chooses three pairwise disjoint three-subsets and canonicalizes the three bit masks (or assigns three nonzero colours with three points per colour and then canonicalizes the names). There are \(200200\) such candidates. For each candidate the legality test examines all 26 blocks; a block is forbidden exactly when it has a point in each of the three disjoint classes. Both implementation paths therefore enumerate **all** vertices, not a sample. For each valid vertex the first program tries all nine selected points and all four unused points; the second program swaps all nonzero and zero entries in an independently encoded four-symbol point assignment. Both canonicalize class names, retain only valid destinations, deduplicate neighbors and verify graph symmetry. Graph traversals from every unvisited vertex enumerate every connected component; internal degree checks identify isolated vertices, four-cliques, and the seven-vertex motif. For the seven-vertex motif, the unique degree-six vertex is joined to all other six, whose induced subgraph consists of two disjoint triangles (six edges, two triangles), proving the glued-\(K_4\) structure. The independent programs return precisely the table above, including all vertex and edge counts.

The finite classification covers the two isomorphism types because every Steiner triple system of order thirteen is isomorphic to one of these two designs [2]. Isomorphism carries blocks, cross-free placements and replacement adjacency bijectively, so the enumerated graph invariants do not depend on the particular coordinates.

## Verification

Run `python3 verify_crossfree.py`; independently run `g++ -O3 -std=c++17 verify_crossfree.cpp -o verify_crossfree && ./verify_crossfree`. Neither implementation depends on the output of the other. Both reconstruct 26 blocks and verify all 78 point-pairs occur exactly once. The Python version enumerates canonical triple-bit-mask families and checks adjacency, component shapes, and overlap of the two valid-state sets. The C++ version represents states as thirteen two-bit digits with values \(0,1,2,3\), canonicalizes colour names, retests each permitted exchange directly, verifies reverse edges and reports the component-degree profiles. Exact expected stdout is embedded as `python_expected.txt` and `cpp_expected.txt`. Each verifier is complete on the finite domain and does not use random sampling or a timeout-based argument.

## Relationship to prior work

Gyárfás [1] defines cross-free sets in Steiner triple systems and motivates the maximal size through monochromatic-component questions. That article supplies general extremal bounds and constructions but neither these order-thirteen counts nor the single-point replacement graphs. The bound of three here is a finite instance of the broader extremal framework, not claimed to be novel by itself. Pavone [2] documents the two order-thirteen block models, the Pasch switch and conventional *weak* three-colourings. A weak colouring forbids monochromatic blocks on all thirteen points; our partial, balanced three-class placements forbid three-colour rainbow blocks on nine selected points, so one invariant does not determine the other. Heinlein and Östergård [3] study algorithms for counting fixed-line configurations in Steiner systems, not these cross-free partition exchange graphs. Prior studies of the line-avoiding complexes of both designs examine subsets containing no complete block rather than three disjoint balanced classes avoiding transverse blocks; their homotopy data do not imply the present exact graph decompositions. The mathematical comparisons concern differing definitions and logical implications, not just absent search terms.

## Limitations

This is an exact finite result for order thirteen, not an extension to arbitrary Steiner orders and not a proof about higher-order cross-free maximum values. The two large connected components are characterized here by their size, connectivity and edge count, not by an abstract isomorphism presentation or complete metric. The exhaustive computations are transparent and reproducible, but have not received independent external scholarly validation. Although indexed literature and close primary texts have been compared, unpublished or unindexed prior enumerations may exist. No claim about priority beyond the checked material is made.

## References

1. A. Gyárfás, *Large Cross-Free Sets in Steiner Triple Systems*, Journal of Combinatorial Designs **23** (2015), 321–327; arXiv:1509.05527, first submitted 2015-09-18. https://arxiv.org/abs/1509.05527
2. M. Pavone, *A visual representation of the Steiner triple systems of order 13*, Art of Discrete and Applied Mathematics **6** (2023), #P3.04. https://iris.unipa.it/retrieve/674a8990-dc17-457f-b6b2-f2261c09ebde/Picture%20STS%2813%29_2023_01_05.pdf
3. D. Heinlein and P. R. J. Östergård, *Algorithms and complexity for counting configurations in Steiner triple systems*, Journal of Combinatorial Designs **30** (2022), 527–546. https://doi.org/10.1002/jcd.21839
