# Independent mathematical audit

## correctness

PASS

Independently rebuilt and exhaustively checked the graph and both state graphs with /workspace/audit-work/coxeter_recount.py (run with python3). The GF(2)^3 line model is isomorphic to the specified cyclic Fano-plane labels via i -> a^i in GF(8), where a^3=a+1, so a^i+a^{i+1}=a^{i+3}; the seven nonzero elements comprise the cyclic powers of a. Disjoint-vertex triples gave 28 vertices of degree 3 and 42 edges. A forcing event queue maintained the live count of unobserved neighbors of every vertex, starting from the closed seed neighborhood. Marking is monotone, obsolete events are skipped and termination has no remaining force: this is the least forcing-closed superset, since every valid force must be in any larger forcing-closed set containing the marks so far. Generation accounted for 1, 28, 378 and 3276 candidates in sizes 0–3 with 0, 0, 0 and 336 successes. Independent overlap-pair buckets gave the jump and slide graphs, checking the joint (slide degree, jump degree, parent-distance signature) counts: 168 of (0,12,(3,3,3)) and 168 of (2,9,(3,3,4)). Counting all parent triples by signature gave another 168 non-power-dominating triples with each of those signatures. Bitset layer sweeps gave 168 singleton components and 28 six-cycles with distinct six-vertex supports, each inducing a three-edge matching with exactly two complementary missing endpoint choices. All 336 jump layer sweeps reached all states; the radius and diameter were 5 and 6, eccentricities counted 112 and 224, and the unordered jump distances counted (1764,7392,19740,22428,4844,112). In particular distance one counts 1764 jump edges. This is exhaustive for the bound model.

## originality

PASS

The same base graph and general power-domination methodology are classical. The exact optimal state census, the induced-matching geometry of slides, and the full jump metric are not implied by the primary statements or the distinct indexed results examined.

## value

PASS

On a classical cubic symmetric graph, the minimum number of sensors alone leaves their permitted relocation unclear. A complete classification distinguishes local freezing from unrestricted connectivity and identifies a simple induced-matching obstruction: removing two opposite choices from a three-edge cube leaves exactly a mobile hexagon. The complete finite state benchmark with cross-checked jump distances and the signature limitation is useful for testing relocation results on a natural graph; the structural result is more informative than the metric table alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
