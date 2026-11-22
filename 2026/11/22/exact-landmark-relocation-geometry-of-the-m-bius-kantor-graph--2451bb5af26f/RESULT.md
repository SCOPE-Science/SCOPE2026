# Exact landmark relocation geometry of the Möbius–Kantor graph

## Finding

Let \(G\) be the Möbius–Kantor graph \(GP(8,3)\), as defined below. A *metric basis* is a minimum-cardinality set of vertices whose distance signatures distinguish every two vertices. Its metric dimension is \(4\), and it has **exactly 320** metric bases in **six graph-automorphism orbits**, with orbit sizes \(24,24,32,48,96,96\).

Define two graphs on these 320 configurations. Two bases are adjacent in \(J\) when one is obtained from the other by replacing exactly one vertex, and are adjacent in \(T\) when the removed and inserted vertices must additionally be adjacent in \(G\). The complete, exact results are:

| Quantity | Unrestricted replacement \(J\) | Edge sliding \(T\) |
|---|---:|---:|
| Configurations | 320 | 320 |
| Edges | 1,984 | 576 |
| Components | 1 | 1 |
| Radius | 4 | 12 |
| Diameter | 5 | 12 |
| Degree distribution | 288 of degree 12; 32 of degree 16 | 192 of degree 3; 96 of degree 4; 32 of degree 6 |
| Eccentricity distribution | 128 of eccentricity 4; 192 of eccentricity 5 | all 320 of eccentricity 12 |

The complete numbers of **unordered distinct** pairs of bases at every possible distance are:

| Distance | \(J\) pairs | \(T\) pairs |
|---:|---:|---:|
| 1 | 1,984 | 576 |
| 2 | 9,888 | 1,440 |
| 3 | 23,008 | 3,072 |
| 4 | 16,064 | 5,744 |
| 5 | 96 | 7,392 |
| 6 | 0 | 9,192 |
| 7 | 0 | 8,448 |
| 8 | 0 | 7,584 |
| 9 | 0 | 4,512 |
| 10 | 0 | 2,344 |
| 11 | 0 | 576 |
| 12 | 0 | 160 |

The entire difference between the two reconfiguration metrics is also classified. There are \(4,480,5,856,7,200,10,048,10,152,7,968,3,984,1,216,136\) unordered pairs for which \(d_T-d_J\) equals respectively \(0,1,2,3,4,5,6,7,8\). Thus the sharp extra distance imposed by local motion is **eight** moves. In the notation below, \(A=\{0,1,10,11\}\) and \(B=\{4,5,10,11\}\) witness \(d_J(A,B)=2\) and \(d_T(A,B)=10\). In particular, the locally constrained graph is self-centered even though the unconstrained one is not.

## Assumptions and scope

All graphs are finite, simple, undirected and unweighted. Write the sixteen vertices as \(u_i=i\) and \(v_i=8+i\), for \(0\le i<8\). The 24 edges of \(G\) are exactly \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\), with indices reduced modulo \(8\). Distances \(d_G\) are shortest undirected path lengths. A set \(R\subseteq V(G)\) resolves \(G\) if for all distinct \(x,y\in V(G)\) some \(r\in R\) satisfies \(d_G(r,x)\ne d_G(r,y)\). A metric basis is such an \(R\) of least possible cardinality. Its tokens are indistinguishable, and no intermediate state may cease to be a metric basis. There is no requirement that the inserted vertex be previously adjacent for \(J\); for \(T\) that is mandatory. Unreachable pairs, if any, would have infinite distance; the verified graphs are connected.

## Proof

The assertions form a **finite exhaustive theorem** with standalone executable proof checks included in this package. The completeness of the finite search follows from the following explicit partition and path arguments, not from sampling.

1. Build the 24 prescribed edges, then compute the \(16\times16\) all-pairs graph-distance matrix. Every landmark is one of the sixteen listed vertices. For each of the \(\binom{16}{2}=120\) unordered pairs \(\{x,y\}\), form its *witness mask* \(M_{xy}=\{r:d_G(r,x)\ne d_G(r,y)\}\). The exact equivalence \(R\text{ resolves }G\iff R\cap M_{xy}\ne\varnothing\) for every pair is immediate from the definition. Enumerating all subsets of cardinality \(0,1,2,3\) establishes that none resolves. Enumerating all \(\binom{16}{4}=1,820\) four-subsets leaves precisely \(320\) passing the witness test. The independent checker instead evaluates distinct sixteen-component distance-signature vectors directly and obtains the same answer in a distinct graph labeling.

2. For each of the 320 optimum subsets, consider every ordered pair \((p,q)\) with \(p\) selected and \(q\) unselected. The replacement \((R\setminus\{p\})\cup\{q\}\) is legal exactly when it belongs to the explicitly enumerated list of bases. For \(T\) also require \(pq\in E(G)\). Thus there are no unlisted legal moves: this yields \(1,984\) edges for \(J\) and \(576\) for \(T\). A direct adjacency symmetry and vertex-degree check excludes directionality, loops and double counting.

3. For each configuration, breadth-first search of the just-constructed unweighted reconfiguration graph computes the exact minimal number of legal moves to every other configuration: paths of each length are explored by successive layers, and every graph edge is one move. All 320 distance searches reach all 320 states. Exhaustively counting the \(\binom{320}{2}=51,040\) unordered pairs yields the two histograms, eccentricities, radii and diameters above. The complete difference histogram is computed pairwise from these same certified distance matrices; the exhibited pair witnesses the sharp value eight.

4. Independently build the same abstract sixteen-vertex graph via the standard \(\mathrm{LCF}\) cycle-and-chord encoding \([5,-5]^8\). Rather than witness masks, evaluate direct distance signatures for all candidates; rather than breadth-first search on the placement graphs, use Floyd–Warshall all-pairs relaxation. The second program reproduces **every** asserted count. For the symmetry result, each program independently generates adjacency-preserving permutations by exact partial-permutation backtracking, finds \(96\) automorphisms, applies all of them to all bases, and obtains precisely six orbits with sizes \(24,24,32,48,96,96\). Its orbit-size sum is \(320\). The \(GP(8,3)\) orbit representatives, their jump and slide degrees, and their eccentricities are recorded in the machine-readable output of `verify_gp.py`.

Because every subset of size below four, every four-subset, every legal replacement, and every pair of configurations is included, the finite computations exhaust their stated domain. No inductive conclusion for general \(GP(n,k)\) is asserted.

## Verification

Run `python3 verify_gp.py` and `python3 verify_lcf.py` with a standard Python 3 interpreter. Both are pure standard-library programs. They terminate with `VERIFIED_GP_OK` and `VERIFIED_LCF_OK` respectively if and only if all their explicit assertions pass. Exact recorded outputs are supplied in `verified_gp.txt` and `verified_lcf.txt`. The checkers use different graph encodings, resolving-set predicates and shortest-path algorithms. Their generated degree, shortest-distance, orbit and penalty counts match the tables here. These are reproducible **self-review**, not independent formal or human certification.

## Relationship to prior work

The vertex metric-dimension literature motivates optimal distance landmarks. Imran, Baig, Shafiq and Tomescu, *On Metric Dimension of Generalized Petersen Graphs* (2014), explicitly identify \(P(8,3)\) as the Möbius–Kantor graph and give a four-vertex resolving set, but their theorems concern dimension bounds for \(P(n,3)\), not the full family of 320 optimizers or motion metrics. Hakanen, Junnila, Laihonen and Yero (first arXiv version March 16, 2021) study vertices contained in all or none of the metric bases of a graph, rather than the geometry of moving between all optimum bases. Bergougnoux, Defrain and Mc Inerney (arXiv first September 2023) study the computational complexity of enumerating minimal resolving sets via hypergraph transversals; this does not determine exact optimum counts, distances or movement restrictions for \(GP(8,3)\). Filipović, Kartelj and Kratica consider *edge* metric dimension of generalized Petersen graphs, which distinguishes edges rather than vertices. Searches of the mathematical findings index and public literature did not locate the same 320-state reconfiguration classification. The negative search is evidence of a gap, not proof that no equivalent has ever been published.

## Limitations

The theorem is finite and specific to \(GP(8,3)\): it does not determine metric-basis motion for any other generalized Petersen graph or imply an optimal algorithm for arbitrary graphs. Originality remains conditional on accessible indexing and the material inspected; a broad 2026 thesis on metric-basis reconfiguration was visible by title but its complete text was not located, so an unindexed treatment of this particular graph remains a priority risk. All proofs and computation checks were reviewed without external independent mathematical validation. Enumeration proves shortest-path properties of exactly the 320 defined states and no more.

## References

- M. Imran, A. Q. Baig, M. K. Shafiq and I. Tomescu, *On Metric Dimension of Generalized Petersen Graphs P(n,3)*, Ars Combinatoria 117 (2014), 113–130. https://combinatorialpress.com/article/ars/Volume%20117/volume-117-paper-10.pdf
- A. Hakanen, V. Junnila, T. Laihonen and I. G. Yero, *On Vertices Contained in All or in No Metric Basis*, arXiv:2103.08911, first submitted 2021-03-16. https://arxiv.org/abs/2103.08911
- B. Bergougnoux, O. Defrain and F. Mc Inerney, *Enumerating minimal solution sets for metric graph problems*, arXiv:2309.17419, first submitted 2023-09-29. https://arxiv.org/abs/2309.17419
- V. Filipović, A. Kartelj and J. Kratica, *Edge metric dimension of some generalized Petersen graphs*, arXiv:1807.00580, first submitted 2018-07-02. https://arxiv.org/abs/1807.00580
