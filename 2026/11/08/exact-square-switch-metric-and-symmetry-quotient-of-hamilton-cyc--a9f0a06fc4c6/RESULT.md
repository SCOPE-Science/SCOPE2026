# Exact square-switch metric and symmetry quotient of Hamilton cycles in \(Q_4\)

## Finding

Let \(Q_4\) have vertex set \(\{0,1\}^4\), with adjacent binary words differing in exactly one coordinate. A *configuration* is an undirected Hamilton cycle represented by its set of sixteen undirected edges: choosing a starting vertex or traversing in reverse does not change the configuration. A *square switch* replaces two disjoint, opposite used edges of a coordinate square by its other two edges, **only if** the new spanning two-regular subgraph is one Hamilton cycle. Let \(\mathcal H_4\) be the resulting configuration graph.

**Exact census theorem.** The graph \(\mathcal H_4\) has \(1344\) vertices, \(1920\) edges and exactly \(241\) connected components: \(240\) singleton components and one component on \(1104\) vertices. The latter has radius \(10\) and diameter \(12\). Its vertex eccentricity distribution is \(96\) at eccentricity \(10\), \(192\) at eccentricity \(11\), and \(816\) at eccentricity \(12\). Across all configurations, the vertex degree distribution is \(240\) of degree \(0\), \(384\) of degree \(1\), \(192\) of degree \(2\), \(288\) of degree \(4\), and \(240\) of degree \(8\).

Under the full \(384\)-element cube automorphism group, the configurations form nine orbits. Number the orbits from \(0\) to \(8\) as in the table. The final column lists the number of neighbors in each orbit (in order \(0,1,\ldots,8\)) of *any* vertex in the row. Hence it is an exact equitable symmetry quotient, not merely a list of orbit sizes.

| Orbit | Size | Degree | Sorted coordinate-use counts | Neighbor counts by orbit |
|---|---:|---:|---|---|
| 0 | 48 | 0 | (2,2,4,8) | (0,0,0,0,0,0,0,0,0) |
| 1 | 96 | 0 | (2,4,4,6) | (0,0,0,0,0,0,0,0,0) |
| 2 | 96 | 0 | (2,4,4,6) | (0,0,0,0,0,0,0,0,0) |
| 3 | 384 | 1 | (2,4,4,6) | (0,0,0,0,0,0,0,0,1) |
| 4 | 192 | 2 | (4,4,4,4) | (0,0,0,0,0,0,0,0,2) |
| 5 | 96 | 4 | (2,2,6,6) | (0,0,0,0,0,0,0,0,4) |
| 6 | 192 | 4 | (2,4,4,6) | (0,0,0,0,0,0,0,2,2) |
| 7 | 48 | 8 | (2,2,6,6) | (0,0,0,0,0,0,8,0,0) |
| 8 | 192 | 8 | (2,4,4,6) | (0,0,0,2,2,2,2,0,0) |

The numerical count of Hamilton cycles, the existence of frozen configurations, and the underlying local inversion move are **not** claimed as new. The asserted refinement is the complete square-switch graph structure, its exact metric radius/diameter and eccentricity spectrum, and its equitable automorphism quotient.

## Assumptions and scope

All graphs here are undirected and simple; cube vertices have fixed four-bit labels. The total cube edge set has exactly \(32\) edges and the cube contains exactly \(24\) coordinate square faces. Only a single two-edge *square switch* counts as a move; arbitrary swaps of two edges or arbitrary changes to a Gray code are outside the statement. All counting is for the labeled cube; the nine types are orbits under cube automorphisms rather than a quotient replacing the original \(1344\) labeled cycles. Radius and diameter refer exclusively to the unique nonsingleton component; the full graph is disconnected and has no finite all-pairs diameter.

## Proof

This is an exact finite exhaustive proof, implemented by two algorithmically distinct enumerations and documented by a complete adjacency certificate.

**Complete configurations.** Encode cube vertices by integers \(0,1,\ldots,15\), with adjacency when their bitwise XOR is one of \(1,2,4,8\). Fix the first vertex of every directed Hamilton tour at \(0\). Depth-first extension visits each of the other \(15\) vertices exactly once and retains precisely those paths whose last vertex is adjacent to \(0\). Any undirected Hamilton cycle admits exactly two such rooted orientations; imposing that the second vertex be numerically smaller than the last makes the representation unique. The independent path-based enumeration finds exactly \(1344\) canonical Hamilton cycles. The face-based implementation instead deduplicates each rooted tour by the bit mask of its \(16\) edges and gets the same \(1344\) masks.

**Complete adjacency.** There are \(\binom42 2^{4-2}=24\) coordinate squares. For each Hamilton cycle mask \(c\) and each such face mask \(s\), a legal square switch can occur only if \(c\cap s\) is exactly two *vertex-disjoint* edges of the face. The candidate is the symmetric difference \(c\mathbin\triangle s\). It is a switch neighbor exactly when it belongs to the already exhaustive set of Hamilton masks. This tests **every** possible legal square switch, and no non-Hamilton two-cycle result is admitted. As an independent construction, the path-based checker considers every pair of nonincident tour edges around the cyclic vertex sequence; if the four endpoints form a coordinate square with the matching reconnection, it reverses the intervening subpath. Removing two tour edges and reconnecting the opposite endpoints by this inversion is equivalent to the same valid square switch.

**Graph and metric.** The complete switch graph is stored in `q4_flip_graph.tsv`, with one row for every eight-hex-digit cycle-edge mask and all of its neighbors. The independently constructed implementations obtain \(1920\) undirected edges and degree distribution \((0:240,1:384,2:192,4:288,8:240)\). Exhaustive component traversal obtains exactly one component of size \(1104\) and \(240\) isolates. A breadth-first search from *each* of the \(1104\) non-isolated vertices determines its full distance vector. Counting the largest distances from each source gives the eccentricity spectrum \((10:96,11:192,12:816)\), proving the radius is \(10\) and the diameter is \(12\). No sample or statistical inference is used.

**Symmetry quotient.** Every cube automorphism is a coordinate permutation followed by the bitwise XOR of one of the \(16\) binary words. All \(4!\cdot16=384\) actions are generated and applied to every cycle mask. This produces exactly nine orbits, and the face-based checker verifies that all states within each orbit have the same nine-component neighbor-orbit vector shown above. The table is therefore an exact equitable quotient.

## Verification

The standalone source `check_faces.py` implements edge-mask enumeration, all \(24\) square switches, all-pairs BFS for the nonsingleton component and all cube automorphisms; its recorded output is `check_faces.out`. The separately implemented C++ `check_inversions.cpp` enumerates oriented rooted tour sequences with reversal identification, generates the moves by subsequence inversion rather than face-mask tests, and performs independent all-pairs BFS; its output is `check_inversions.out`. Compile with `g++ -O2 -std=c++17 check_inversions.cpp -o check_inversions`, then execute `./check_inversions`. Run the Python checker as `python3 check_faces.py`.

The full labeled adjacency certificate is `q4_flip_graph.tsv`; `verify_certificate.py` parses it, checks that each row is genuinely a Hamilton cycle, independently recomputes all legal square switches from the twenty-four squares, and recomputes components, radius, diameter and eccentricities. Execute `python3 verify_certificate.py`; the recorded output is `verify_certificate.out`. These checks use standard Python only, and the C++ program uses only the C++17 standard library.

## Relationship to prior work

Gregor and Mütze (first arXiv publication 29 July 2016) give constructions and existence results for cyclic Gray codes and Hamilton cycles in subgraphs of cubes, but do not classify the space of all cyclic Gray codes under square-switch inversions. Gilbert's 1958 work already enumerates the isomorphism types of closed Gray-code paths on cubes up to dimension four; the nine types are background rather than a novelty claim.

Contassot-Vivier, Couchot and Héam (2018, §2 and §5) describe precisely the subsequence-inversion operation corresponding to the square switches here; they also discuss isolated Gray codes, exhibit examples in dimension four, and tabulate *isolation percentages* for dimensions two to five. Those facts are prior work, not new discoveries here. In the available main-text sections, no complete degree distribution, proof that all \(1104\) nonisolated four-cube cycles belong to one component, all-pairs radius/diameter and eccentricity spectrum, or nine-orbit adjacency quotient is stated. This absence is not taken as proof of absolute novelty; see limitations.

## Limitations

The theorem is restricted to \(Q_4\), with no claim about larger cubes, mixing times, or arbitrary local moves. The graph-theoretic conclusions rely on auditable exhaustive finite enumeration and not on a symbolic infinite-family classification. The numerical cells of the 2018 paper's Table 2 were not extractable from its available HTML rendering; its isolation counts may already imply some subsidiary statistics here and are not asserted as novel. Earlier or unindexed priority claims remain possible. The scientific checks are reproducible but have not undergone an independent external audit.

## References

1. P. Gregor and T. Mütze, *Trimming and gluing Gray codes*, first publicly available 2016-07-29, arXiv:1607.08806, https://arxiv.org/abs/1607.08806.
2. S. Contassot-Vivier, J.-F. Couchot and P.-C. Héam, *Gray Codes Generation Algorithm and Theoretical Evaluation of Random Walks in N-Cubes*, Mathematics **6** (2018), 98, https://doi.org/10.3390/math6060098.
3. E. N. Gilbert, *Gray Codes and Paths on the n-Cube*, Bell System Technical Journal **37** (1958), 815–826, https://doi.org/10.1002/j.1538-7305.1958.tb03887.x.
