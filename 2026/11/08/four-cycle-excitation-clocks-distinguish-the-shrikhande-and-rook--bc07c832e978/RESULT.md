# Four-cycle excitation clocks distinguish the Shrikhande and rook graphs

## Finding

Let \(R\) be the \(4\times4\) rook graph and let \(S\) be the Shrikhande graph. They are nonisomorphic, ordinary-adjacency-cospectral strongly regular graphs, both with parameters \((16,6,2,2)\) and spectrum \(6^1,2^6,(-2)^9\). On the complete space of three-state vertex configurations, apply the synchronous threshold-one Greenberg–Hastings map \(F_G\). The *exact* temporal classifications are:

| Graph | Primitive cycles of length \(1\) | Length \(3\) | Length \(4\) | Periodic configurations | Sharp maximum transient \(T_{\max}\) |
|---|---:|---:|---:|---:|---:|
| \(R\) | 1 | 3,987,936 | 98 | 11,964,201 | 8 |
| \(S\) | 1 | 4,109,384 | 6 | 12,328,177 | 9 |

Every one of the \(3^{16}=43,046,721\) labelled configurations on either graph has eventual primitive period in \(\{1,3,4\}\); the zero-rest state is the sole fixed point. Precisely 54,144 configurations on \(R\) first become periodic at time \(8\), and precisely 96 configurations on \(S\) first become periodic at time \(9\). The supplementary `temporal_census.csv` gives *every* nonempty class by first-periodic-entry time and eventual primitive period: 19 classes on \(R\), 21 on \(S\).

Under their full graph automorphism groups, the primitive four-cycles partition as follows:

| Graph | Full automorphism-group order | Four-cycle symmetry-orbit sizes | Stabilizer orders |
|---|---:|---|---|
| \(R\) | 1,152 | 32, 48, 18 | 36, 24, 64 |
| \(S\) | 192 | 6 | 32 |

The three rook-graph symmetry types have cyclic firing-population profiles \((1,3,9,3)\), \((2,6,6,2)\), and \((4,4,4,4)\), respectively up to rotation of the time coordinate. All six Shrikhande four-cycles have firing profile \((4,4,4,4)\). Therefore **the two induced finite dynamical systems are not conjugate**, even as unlabelled set maps, because their numbers of primitive four-cycles differ.

## Assumptions and scope

Both graphs have vertex set \(V=\mathbb Z_4^2\), ordered lexicographically as \(v=4a+b\) for \(0\le a,b\le3\). Two distinct rook vertices \((a,b)\) and \((c,d)\) are adjacent when \(a=c\) or \(b=d\). Two Shrikhande vertices are adjacent exactly when their difference modulo four belongs to \(\{\pm(1,0),\pm(0,1),\pm(1,1)\}\).

A configuration is \(x\in\{0,1,2\}^{V}\), with resting color \(0\), excited color \(1\), refractory color \(2\). At every vertex \(v\), simultaneously,
\[
(F_Gx)(v)=\begin{cases}1,&x(v)=0\text{ and some }u\sim v\text{ has }x(u)=1,\\0,&x(v)=0\text{ and no such neighbor exists},\\2,&x(v)=1,\\0,&x(v)=2.\end{cases}
\]
The first-periodic-entry time \(T(x)\) is the least \(t\ge0\) such that \(F_G^t(x)\) is periodic; \(P(x)\) is the *least positive period* of this eventual cycle. A primitive temporal cycle is a cyclic orbit of \(F_G\), *not* an orbit of graph automorphisms. A graph automorphism acts on configurations by relabelling vertices, commutes with \(F_G\), and therefore acts on primitive temporal cycles. All claims concern this fixed rule on these two finite graphs only.

## Proof

**Graph identities.** Direct calculation from the displayed adjacency rules gives 16 vertices, degree six, and exactly two common neighbors for every two distinct vertices, whether adjacent or nonadjacent. The strongly regular adjacency identity is \(A^2=4I+2J\). The spectra coincide as stated; this is also classical. The induced neighborhood of a rook vertex is two disjoint triangles, while that of a Shrikhande vertex is one six-cycle, so the graphs are nonisomorphic.

**Complete functional-graph certification.** Encode \(x\) uniquely as \(\operatorname{enc}(x)=\sum_{v=0}^{15}x(v)3^v\), giving every integer in \([0,3^{16}-1]\). The supplied `exhaustive_graphs.cpp` performs the following *complete*, finite computation separately for the two explicit adjacency lists. It first calculates the unique successor of each of the \(3^{16}\) codes using the displayed rule, and the indegree of every code in the functional digraph. It repeatedly removes every indegree-zero vertex, decrementing its successor indegree; all unremoved vertices are exactly the disjoint directed cycles. Traversing each such cycle computes its least period and adds one to that period's primitive-cycle count. Reverse traversal of the removal order assigns \(T(x)=T(F_Gx)+1\) and \(P(x)=P(F_Gx)\) to every removed state, starting from \(T=0\) on the cycles. Counting the resulting ordered pairs \((T,P)\) gives the displayed table and the exact 40 class records in `temporal_census.csv`. The total number of states counted on each graph is exactly \(43,046,721\). These are exhaustive finite sums, not samples or an inference from a finite subset of a larger family.

**Independent exhaustive reconstruction.** The separately implemented `independent_orbits.cpp` obtains state colors through independent precomputed two-block base-three decoding and constructs the successor from firing masks. Rather than indegree elimination, it iteratively follows a path from every previously unseen state, detects the first repeated state or a previously classified state, assigns the new cycle's least period, and propagates times and periods backward along the path. Its *entire* \((T,P)\) table agrees entry-by-entry with the first computation for each graph. `cycle_reps.cpp` independently reconstructs and lists one least-code representative of each primitive four-cycle. Both programs visit exactly the full declared state set, with explicit range and period checks.

**Full symmetry groups and four-cycle orbits.** On the rook graph, the permutations of the four rows, the four columns, and the interchange of row and column yield \(2(4!)^2=1152\) distinct automorphisms. On the Shrikhande graph, translation by each of 16 group elements and the 12 linear maps of \(\mathbb Z_4^2\) preserving the six-neighbor difference set yield \(192\) distinct automorphisms. These are full groups: on either graph the nine nonneighbors of a fixed vertex have pairwise distinct two-vertex traces in its neighborhood, so an automorphism fixing a vertex and all six neighbors is the identity. The induced neighbor graphs have automorphism groups of size 72 (two triangles) and 12 (a six-cycle), bounding the complete groups by \(16\cdot72=1152\) and \(16\cdot12=192\). Thus the constructed groups meet their upper bounds. The standalone `analyze_symmetries.py` checks adjacency preservation, enumerates the exact full groups, and sends each of the 98 or six four-cycle representatives through every graph automorphism, then identifies resulting temporal-cycle representatives. The computed orbit partitions are \(32+48+18=98\) and \(6\), with stabilizer sizes obtained by orbit–stabilizer. The four-step configurations of representatives `41`, `44`, `3608` (rook) and `3320` (Shrikhande), read with the specified base-three encoding, give the indicated excitation-population profiles; invariance under graph automorphisms and temporal shift makes these exact profiles for their whole orbit classes.

**Nonconjugacy.** A bijection of state spaces intertwining the two update maps would map primitive four-cycles bijectively to primitive four-cycles. Since \(98\ne6\), no such conjugacy exists. This distinction is genuinely dynamical and is not determined by the common ordinary adjacency spectrum.

## Verification

Run `python3 verify.py` in a directory containing the supplied source programs, outputs, representative lists, and census CSV, using a C++17 compiler. The command builds three standalone programs from sources, reruns both complete algorithms and the independent cycle enumeration for each graph, compares their full classifications and archived output files, checks all \(3^{16}\) state counts, recomputes all graph automorphism classes, checks the complete 40-line census, and independently verifies graph adjacency identities and four-step firing profiles using `check_graph_invariants.py`. The captured output `verification_output.txt` ends in `VERIFICATION_OK`. All three program families were compiled and replayed from the actual package, not from previous-run paths. The exact per-class counts are included as text and CSV and are reproducible without proprietary libraries.

## Relationship to prior work

The rule is classical: Greenberg and Hastings (1978) introduced a model of excitable media with a refractory stage. Gravner, Lyu and Sivakoff's preprint of October 24, 2016, later published in 2018, analyzes three-color Greenberg–Hastings and cyclic automata on arbitrary graphs; its Theorem 3 provides a criterion for synchronization and asymptotic activity in terms of closed-walk circulation. It does **not** state the complete labelled transient/cycle census or the graph-automorphism classification for the Shrikhande/rook pair. Brouwer and Haemers document the cospectral strongly regular pair and their relation by switching; that is graph-theoretic prior knowledge and does not determine the nonlinear automaton's temporal census. No claim is made that the local update rule, the graphs, or general synchronization criteria are new. The stated contribution is this exact two-graph dynamical distinction with a full temporal and symmetry census.

## Limitations

The theorem is restricted to the two explicitly specified 16-vertex graphs and three colors. It does not classify Greenberg–Hastings dynamics on all strongly regular graphs, additional colors, or noisy/asynchronous updates. Finite exhaustive programs are sufficient for this *finite* claim but are not an infinite-family proof. Independence of implementations reduces programming error risk but is not an external formal audit. A historically unindexed equivalent exact census remains possible.

## References

1. J. M. Greenberg and S. P. Hastings, *Spatial patterns for discrete models of diffusion in excitable media*, SIAM Journal on Applied Mathematics 34 (1978), 515–523. DOI: `10.1137/0134040`.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, first public arXiv posting October 24, 2016, `arxiv:1610.07320`; Annals of Applied Probability 28 (2018), 3324–3357. DOI: `10.1214/17-AAP1350`. Full lawful open-access text at `https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf`.
3. A. E. Brouwer and W. H. Haemers, *Spectra of Graphs*, Springer, 2012, Chapter 9 (regular two-graphs, four-by-four grid and Shrikhande switching). ISBN `9781461419389`.
4. S. S. Shrikhande, *The uniqueness of the \(L_2\) association scheme*, Annals of Mathematical Statistics 30 (1959), 781–798.
