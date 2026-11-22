# Majority attraction basins and a sharp seven-update clock on the Grötzsch graph

## Finding

Let \(G=\mu(C_5)\) be the eleven-vertex Grötzsch graph and let \(F\) be synchronous, open-neighborhood binary majority with retention at ties. Among the \(2^{11}=2048\) labelled initial configurations, precisely 22 are fixed, 70 lie on 35 primitive two-cycles, and no other periodic configurations exist. Every configuration enters its eventual fixed point or two-cycle by seven updates, and seven is attained: \(F^9=F^7\) but \(F^8\ne F^6\). Exactly 30 states have first-entry time seven, all in the basins of the two unanimous fixed points.

For any periodic orbit \(\mathcal O\), its *attraction basin* consists of every initial configuration whose forward orbit eventually enters \(\mathcal O\), including the periodic points. The entire labelled basin spectrum is:

| Orbit period | Number of distinct orbits | Basin size per orbit |
|---|---:|---:|
| 1 | 10 | 1 |
| 1 | 10 | 6 |
| 1 | 2 | 884 |
| 2 | 5 | 2 |
| 2 | 10 | 4 |
| 2 | 10 | 6 |
| 2 | 10 | 10 |

The two basins of size 884 are the all-zero and all-one equilibria. Thus precisely \(1768/2048=221/256\) of all initial configurations reach unanimity. The 20 nonunanimous fixed configurations attract 70 initial configurations altogether, while the 35 two-cycles attract the other 210.

Under the dihedral graph symmetries and simultaneous complementation of every bit, the seven rows of this basin table are also the seven distinct orbit classes: their class cardinalities are respectively 10, 10, 2, 5, 10, 10 and 10.

## Assumptions and scope

The vertex set is \(\{0,\dots,10\}\), with indices \(i\) interpreted modulo five. Write \(u_i=i\), \(v_i=5+i\) and \(w=10\). Edges are exactly \(\{u_i,u_{i+1}\}\), \(\{v_i,u_{i-1}\}\), \(\{v_i,u_{i+1}\}\) and \(\{w,v_i\}\), each for \(i=0,\dots,4\). These define a simple undirected graph of 11 vertices and 20 edges.

A configuration is \(x\in\{0,1\}^{11}\). At each vertex \(i\), count the ones among its neighbors. If more than half of its neighbors have state one, its new state is one; if fewer than half, its new state is zero; at equality the old state at \(i\) is retained. All vertices update simultaneously. A state's *entry time* is the smallest \(t\ge0\) for which \(F^t(x)\) belongs to a periodic orbit. The temporal period of a periodic orbit is its smallest positive return time. The graph is labelled; distinct states related by symmetry are counted separately unless explicitly grouped into symmetry classes.

This is an exact finite statement about this graph, not a theorem for all Mycielski graphs or all tie conventions.

## Proof

The complete state space has only 2048 elements, so an exhaustive finite classification with independently checkable transition and cycle enumeration is a valid proof of this particular claim. The two standalone programs `verify_paths.py` and `verify_pruning.py` provide distinct integer-only finite certificates, including all loops, transition definitions and asserted output checks. Their correctness rests on the following exhaustive algorithms, not on statistical sampling.

First construct every edge by the displayed four families and every state by its eleven-bit integer encoding. The local majority test in `verify_paths.py` compares twice the number of neighboring ones with the degree and retains the old bit at equality. Consequently its computed array `F` contains the exact successor of each of the 2048 states. Each unclassified state is followed until it reaches either an already classified state or a repetition in its current path. A repeated suffix is precisely a periodic cycle; all preceding states are assigned their exact distances from that suffix. Reverse propagation labels each state with an eventual period and a canonical sorted representative of its periodic orbit. The process visits every state and hence determines every basin cardinality, entry time and period without assuming an upper bound on convergence.

Independently, `verify_pruning.py` builds the graph from a literal twenty-edge list and updates by signed neighbor sums, retaining the bit at zero sum. It removes every state of zero predecessor degree from the full functional graph, iterating the removal until only directed cycles remain. These remaining directed cycles are exactly the periodic points. Processing removed states in reverse order yields their unique eventual cycle and exact depth. This algorithm neither uses the first program's graph-generation logic nor its path-following cycle algorithm. Both procedures check the full joint population table:

| First-entry time \(t\) | Period one | Period two |
|---:|---:|---:|
| 0 | 22 | 70 |
| 1 | 262 | 130 |
| 2 | 594 | 10 |
| 3 | 290 | 0 |
| 4 | 280 | 0 |
| 5 | 230 | 0 |
| 6 | 130 | 0 |
| 7 | 30 | 0 |

Each table entry is an exact count over disjoint initial states, and the entries sum to 2048. Only the periods one and two appear. The final nonempty entry layer occurs at \(t=7\), which proves the sharp relation \(F^9=F^7\) and its failure when both exponents are reduced by one. The separate assertions on each orbit's basin in the programs yield the seven-row basin spectrum above. In particular the 22 fixed-point basins contribute \(10+60+1768=1838\), and the two-cycle basins contribute \(10+40+60+100=210\), exhausting the state space.

Finally, graph rotations and reflections act on both five-vertex layers with the same index map, fixing the apex; bit complementation acts on all eleven coordinates. Directly checking that these twenty transformations commute with \(F\), and applying them to every periodic orbit, partitions the 57 orbits into seven classes with exactly the asserted sizes. All 30 states in the last entry layer are independently checked to lead to unanimity.

## Verification

From the directory containing the two standalone Python 3 source files, execute `python3 verify_paths.py` and `python3 verify_pruning.py`. Each exits unsuccessfully on a failed assertion and prints respectively `VERIFY_PATHS_OK` or `VERIFY_PRUNING_OK` on success. Only the Python 3 standard library is required. The first program verifies the entire state classification and symmetries; the second constructs a second transition graph and verifies all entry, period, and basin counts and the two sharp functional identities. No cached tables, external files, randomized searches, numerical tolerances or third-party packages are used.

## Relationship to prior work

The graph is the Mycielski construction of the pentagon, a canonical smallest triangle-free graph of chromatic number four; this is established graph-theoretic background rather than claimed as new. Kaaser, Mallmann-Trenn and Natale (2015, arXiv:1508.03519) analyze deterministic synchronous majority voting and cite the general theorem that the eventual period is at most two; their full-text general voting analysis does not specify the 22 equilibria, 35 two-cycles, sharp seven-update settling, or Grötzsch attraction-basin spectrum. The explicit classification here supplies these graph-specific data, which do not follow numerically from the general eventual-period theorem. Separately recorded exact majority classifications for the Petersen, Heawood, icosahedral, Chvátal and Kneser graphs have different transition graphs and provide neither these basin numbers nor a covering universal family theorem. No exhaustive claim of historical uniqueness is made.

## Limitations

The proof is a complete, reproducible finite enumeration, not an analytic closed form for a family of growing graphs. It assumes binary open-neighborhood majority with tie retention, this exact vertex labelling, and synchronous updates. The exact percentages apply to uniformly sampled initial configurations, not to a stochastic update rule. The prior-art comparison cannot exclude every unindexed table or historical computation; independent external review has not been performed. The two verification programs are separate implementations but are both descriptions of the same finite dynamics.

## References

1. Dominik Kaaser, Frederik Mallmann-Trenn and Emanuele Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519, first submitted 2015-08-14. https://arxiv.org/abs/1508.03519
2. *Mycielski Graph*, Wolfram MathWorld. https://mathworld.wolfram.com/MycielskiGraph.html
3. *Grötzsch graph*, background construction and automorphisms. https://en.wikipedia.org/wiki/Gr%C3%B6tzsch_graph
