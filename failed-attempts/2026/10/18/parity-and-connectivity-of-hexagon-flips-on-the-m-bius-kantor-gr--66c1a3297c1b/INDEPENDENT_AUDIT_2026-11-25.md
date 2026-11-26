# Independent mathematical audit

## correctness

PASS

The symmetric difference of two bipartite perfect matchings consists of disjoint alternating even cycles. Their relative permutation moves the left vertices on these cycles, so disagreement at exactly three positions gives one three-cycle, hence one alternating simple six-cycle, and conversely. Its permutation sign is positive, so the sign of a matching is conserved. An independent Python replay branches at the least uncovered vertex and lists simple six-cycles by extending paths from their least vertex; it cross-checks the entire adjacency by all 8! bipartite assignments and compares the generated certificate exactly to the frozen JSON. It found 33 matchings, 24 six-cycles, 96 flips, components 30+1+1+1, and 24 degree-six plus six degree-eight vertices in the large component. The three isolated positive masks 00d554, 662221, 99088a partition the 24 edges; the connected class is exactly the 30 negatives in the printed orders. All-pairs BFS establishes diameter four; the geodesic 06c341 -> 05d0c1 -> 25508a -> 215432 -> 603434 witnesses it. Replay path: /workspace/branches/34974772-bb7b-42dc-9bde-975ad5a0739f/independent_gp_hex.py, with the frozen hexagon_flip_certificate.json path as its sole argument. The frozen verifiers were inspected, not executed. For the circulant version, the dihedral generating set y,xy,x^3y gives the displayed offsets. The product of 1+s+s^3 over eighth roots s is 3 times -1 times 1 twice times 3 twice, or -27; the permanent is the same 33 matchings. The three displayed positive permutations are valid, even, and differ in every row from one another. This also checks the signed count in that convention.

## originality

FAIL

The complete six-cycle census is demonstrably covered by a distinct catalog result on the identical graph and the identical all-simple-six-cycle rule. It supplies the same components, degrees, edge count and diameter, along with more detailed distances and two additional move rules. The parity labels and one-factorization of the isolates follow directly from that classification and the known symmetry of the graph, as shown below. This is a coverage judgment, not a historical priority claim: the matching catalog record has a later listed date. The inaccessible embedding paper is not the basis of the failure.

## value

FAIL

The natural graph and the distinction between all simple cycles and facial cycles would justify an unknown exact reachability classification. Here, however, the stronger existing six/eight-cycle classification already supplies the six-only graph's components and metrics. The parity criterion and the edge partition are short consequences of that classification and edge transitivity. The reproducible certificate confirms correctness but does not supply a separate unknown exact invariant or a general result beyond that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
