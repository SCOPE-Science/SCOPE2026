# Complete subgroup-fixed homotopy classification of the Pappus independence complex

## Finding
Let \(P\) be the Pappus graph, let \(K=\operatorname{Ind}(P)\) be its simplicial independence complex, and let \(G=\operatorname{Aut}(P)\). The complete geometric subgroup-fixed-point classification is as follows. There are \(216\) graph automorphisms and \(380\) subgroups distributed into \(44\) conjugacy classes. For **every** subgroup \(H\leq G\), the fixed space \(|K|^H\) is one of the following ten types, with the indicated exact multiplicities.

| Integral homotopy type of \(|K|^H\) | Number of subgroups | Number of conjugacy classes |
|---|---:|---:|
| Empty | 52 | 11 |
| Contractible | 153 | 7 |
| Two isolated points | 60 | 15 |
| Three isolated points | 9 | 1 |
| \(\bigvee^{10}S^4\) | 1 | 1 |
| \(S^1\) | 54 | 3 |
| \(S^2\) | 12 | 2 |
| \(S^1\vee S^1\) | 12 | 2 |
| \(S^2\vee S^2\) | 18 | 1 |
| \(S^3\vee S^3\) | 9 | 1 |
| **Total** | **380** | **44** |

Here \(S^d\) is the ordinary \(d\)-sphere, and \(\vee\) denotes wedge. In particular, fixed spaces have positive-dimensional homology in several different degrees even though the underlying complex has only fourth-dimensional reduced homology. The classification concerns **geometric fixed spaces**, not orbit-space quotients or homology fixed vectors.

## Assumptions and scope
Number vertices \(0,1,\ldots,17\). Join \(i\) to \(i+1\pmod{18}\) and \(i+a_i\pmod{18}\), where \(a_i\) repeats the six-entry list \((5,7,-7,7,-7,-5)\) three times. Duplicate undirected edges are identified. This defines a simple three-regular graph with 18 vertices and 27 edges, isomorphic to the Pappus point-line incidence graph. The independence complex \(K\) consists of all vertex subsets with no graph edge. The group \(G\) is the entire graph automorphism group, including point-line interchanges; all subgroups, including the trivial subgroup and \(G\), are in scope. Fixed spaces are taken in the ordinary Euclidean geometric realization of \(K\). No coefficient field is required: the statements are about integral homotopy types.

## Proof
**Complete symmetry census.** The embedded program `pappus_fixed_core.py` constructs the graph from the given LCF list, computes every pairwise graph distance, and backtracks over all bijections preserving that matrix. Every automorphism preserves distances, while each output bijection is separately checked to preserve adjacency; hence no automorphism can be omitted and no nonautomorphism is retained. There are exactly \(216\) automorphisms. The code constructs their complete product and inverse tables. Beginning with the trivial subgroup, it adjoins each group element in turn and takes exact generated subgroup closures until no new subgroup occurs. Every subgroup can be reached by successively adjoining a generating set, so this is exhaustive. The resulting \(380\) subgroups are checked for closure, identity and inverses; conjugation partitions them into exactly \(44\) classes.

**Exact geometric fixed-point model.** For any subgroup \(H\), partition the 18 graph vertices into \(H\)-orbits. Retain exactly those orbits that are independent sets in \(P\). Make a simplicial complex \(F_H\) whose vertices correspond to these eligible orbits, and where a collection is a face exactly when the union of its orbits is independent. A point of the geometric realization \(|K|\) is \(H\)-fixed if and only if its barycentric coordinates are constant on every \(H\)-orbit. Within each invariant simplex, its fixed points are therefore precisely the convex hull of the normalized orbit barycenters. These convex hulls glue compatibly, so \(|F_H|\) is PL-homeomorphic to \(|K|^H\). This description includes empty fixed spaces and fixed points at barycenters of nontrivially permuted faces.

**Exact discrete-Morse certificates.** The program constructs \(F_H\) for the canonical representative of each conjugacy class. The embedded JSON certificate contains the complete representative subgroup, its conjugacy multiplicity, a vertex-toggle pivot order, and all unmatched faces. The verifier reconstructs each complex and checks that every matched pair is a facet/cofacet pair, that pairs are disjoint, and that the recorded critical-face list agrees exactly. It then inspects **every** nonempty-face Hasse cover, directs matched covers upwards and all other covers downwards, and topologically sorts the resulting directed graph. Successful visitation of all vertices proves acyclicity of each matching, not merely its putative critical-cell count.

The 44 matchings contain exactly 1,616 pairs and the full directed checks cover 13,096 Hasse incidences. Every residual critical-face signature is either zero critical faces (empty complex), a specified number of isolated critical vertices, or exactly one critical vertex together with \(r\) critical cells all in one positive dimension \(d\), with the values \((r,d)=(1,1),(2,1),(1,2),(2,2),(2,3),(10,4)\). Forman's discrete-Morse theorem gives a CW complex with precisely these cells. When the only positive-dimensional cells have a common degree and there is one vertex, all their attaching maps are constant for dimension one and attach to a point for dimensions greater than one, so its homotopy type is \(\bigvee^r S^d\). The isolated-vertex and empty cases are immediate. Graph automorphism conjugation identifies the fixed-point complexes of conjugate subgroups, yielding the displayed 380-subgroup table.

## Verification
The complete self-contained files are `pappus_fixed_core.py`, `pappus_fixed_certificate.json`, and `pappus_fixed_output.txt`. Python 3 and its standard library suffice. From the same directory run `python3 pappus_fixed_core.py verify pappus_fixed_certificate.json` to reconstruct and check all subgroups, all representative fixed complexes, every matching, and all Hasse-cover acyclicity tests; compare standard output to `pappus_fixed_output.txt`. To regenerate the exact certificate from scratch instead, run `python3 pappus_fixed_core.py generate pappus_fixed_certificate.json`, then verify it. Successful replay reports `PAPPUS_INDEPENDENCE_ALL_SUBGROUP_FIXED_HOMOTOPY_PASS` and checks both column totals and each type tally. This is an exhaustive **finite** proof for this graph, not extrapolation to arbitrary graphs. Independent mathematical auditing has not been performed.

## Relationship to prior work
Barmak's 2010 preprint on star clusters in independence complexes establishes general nonequivariant constructions and suspension techniques for triangle-free graphs. It does not give an all-subgroup geometric fixed-space classification of the Pappus graph. The already available complete Pappus graph automorphism-character calculations (references 3 and 4) determine the 13 conjugacy-class traces of the 216-element group on the known fourth homology, and the ordinary nonequivariant type \(K\simeq\bigvee^{10} S^4\). They **do not** classify \(|K|^H\) for noncyclic subgroups or establish their integral homotopy types: representation traces and quotient rational homology cannot recover this information. Earlier isolated cyclic-action calculations are encompassed by the known character, not claimed here as new. The full subgroups' geometric fixed-point homotopy census is the specific contribution.

## Limitations
The conclusion applies specifically to the Pappus graph with its complete natural graph-automorphism action; it makes no assertion about other symmetric incidence graphs, equivariant attaching maps, normalizer representations, or orbit-space fundamental groups. The enumeration and discrete-Morse proof are entirely reproducible, but software implementations can contain errors and an independent mathematical audit has not occurred. Publication priority is limited by unindexed equivalent calculations. Tsukuda's 2017 incidence-graph theorem was compared through available descriptive material rather than full primary text; it concerns ordinary nonequivariant homotopy, and no dominating fixed-space theorem was identified, but an equivalent uninspected source cannot be excluded.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first publicly available 2010-07-02. https://arxiv.org/abs/1007.0418
2. E. W. Weisstein, *Pappus Graph*, MathWorld (standard LCF presentation). https://mathworld.wolfram.com/PappusGraph.html
3. *Complete automorphism character of the Pappus independence complex*, public mathematical result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-automorphism-character-of-the-pappus-independence-compl--9a42f6d28b4b
4. *The full rational homology character of the Pappus independence complex*, public mathematical result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-the-full-rational-homology-character-of-the-pappus-independence--03b67feab9d4
5. S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12 (2017), 28–46, DOI:10.55016/ojs/cdm.v12i1.62277. https://cdm.ucalgary.ca/article/view/62277
