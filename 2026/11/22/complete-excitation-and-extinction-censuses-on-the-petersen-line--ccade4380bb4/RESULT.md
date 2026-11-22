# Complete excitation and extinction censuses on the Petersen line graph

## Finding

Let \(P\) be the Petersen graph and \(G=L(P)\) its fifteen-vertex, four-regular line graph. For each integer contact threshold \(\theta\in\{1,2,3,4\}\), apply synchronous three-state Greenberg–Hastings dynamics \(F_\theta\) to all \(3^{15}=14{,}348{,}907\) labelled configurations. At a resting vertex, excitation occurs if at least \(\theta\) open neighbors are currently excited; the excited and refractory phases advance unconditionally. The exact attractor populations and maximum first-periodic-entry times are:

| Contact threshold | Fixed states | Primitive 3-cycles | Primitive 4-cycles | Primitive 5-cycles | Primitive 8-cycles | Sharp maximum entry time |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 220,810 | 60 | 30 | 60 | 12 |
| 2 | 1 | 0 | 0 | 0 | 0 | 6 |
| 3 | 1 | 0 | 0 | 0 | 0 | 3 |
| 4 | 1 | 0 | 0 | 0 | 0 | 3 |

The only fixed state is the all-rest state. Thus a single extra required excited contact annihilates all **220,960 primitive nonconstant temporal attractors**. More strongly, every threshold-two state is completely at rest after at most six updates, and this is sharp:

\[
F_2^6(x)=\mathbf 0\quad\text{for every }x\in\{0,1,2\}^{15},
\qquad F_2^5\ne\mathbf 0\text{ as a map}.
\]

Exactly **930** labelled initial states first reach rest on their sixth update. The threshold-one dynamics has only eventual least periods \(1,3,4,5,8\), and satisfies the sharp full-system periodic-entry identity
\[
F_1^{132}=F_1^{12},\qquad F_1^{131}\ne F_1^{11}.
\]

The threshold-one *basin populations*, grouped by eventual least period, are respectively \(277{,}077\), \(13{,}229{,}250\), \(201{,}240\), \(536{,}580\), and \(104{,}760\). Their sum is \(14{,}348{,}907\). The complete individual-basin-size histograms, exact entrance-time-by-period counts, and periodic-orbit representatives are available in the included reproducible census outputs.

The exact first-periodic-entry populations by time \(t\) are:

| \(t\) | Threshold 1 | Threshold 2 | Threshold 3 | Threshold 4 |
|---:|---:|---:|---:|---:|
| 0 | 663,301 | 1 | 1 | 1 |
| 1 | 711,247 | 32,767 | 32,767 | 32,767 |
| 2 | 2,415,219 | 1,986,454 | 8,504,178 | 13,475,228 |
| 3 | 4,096,486 | 9,546,631 | 5,811,961 | 840,911 |
| 4 | 3,082,074 | 2,642,574 | 0 | 0 |
| 5 | 1,856,250 | 139,550 | 0 | 0 |
| 6 | 660,330 | 930 | 0 | 0 |
| 7 | 476,160 | 0 | 0 | 0 |
| 8 | 274,080 | 0 | 0 | 0 |
| 9 | 93,120 | 0 | 0 | 0 |
| 10 | 14,640 | 0 | 0 | 0 |
| 11 | 4,800 | 0 | 0 | 0 |
| 12 | 1,200 | 0 | 0 | 0 |

## Assumptions and scope

All graphs are finite, simple, unweighted and undirected. Fix a labelled presentation of the Petersen graph with outer vertices \(0,1,2,3,4\) and inner vertices \(5,6,7,8,9\). Its edges are \(\{i,i+1\bmod5\}\), \(\{i,i+5\}\), and \(\{i+5,5+((i+2)\bmod5)\}\) for \(i=0,1,2,3,4\). The fifteen vertices of \(G=L(P)\) represent these fifteen edges, listed in lexicographic order in `threshold1.txt`; two are adjacent if and only if the corresponding Petersen edges meet. Every vertex of \(G\) has degree four.

A state \(x\) assigns \(0\) (rest), \(1\) (excited), or \(2\) (refractory) to each vertex. In one simultaneous update: \(1\mapsto2\), \(2\mapsto0\), and \(0\mapsto1\) precisely when at least \(\theta\) of the four neighboring vertices have state \(1\); otherwise \(0\mapsto0\). The first periodic-entry time of \(x\) is the smallest \(t\ge0\) for which \(F_\theta^t(x)\) is itself periodic. The least eventual period is the least positive period of that periodic state. Attractor/basin counts do not quotient by spatial automorphisms or color permutations.

## Proof

This is an **exhaustive finite-state computational proof**, not a claim of an unbounded-graph theorem. The following algorithms, fully specified by the included standalone C++17 source files, collectively verify the exact classification.

**First complete classifier:** `threshold_census.cpp` builds the Petersen edges by the three independent explicit edge families above, sorts them to fix the line-graph vertex labels, and constructs exactly four neighbors of each line-graph vertex by checking shared endpoints. It enumerates every integer \(s\) with \(0\le s<3^{15}\), reads its fifteen base-three digits, and computes the unique simultaneous successor by applying the stated local threshold rule. Thus its vector `nxt` is the full transition function, not a sample. It computes each vertex's indegree and iteratively removes all zero-indegree vertices; the remaining vertices belong to directed cycles of this finite functional graph. It traverses each residual cycle once to record its least period and size; it then processes the removed states in reverse elimination order, assigning every state its successor's cycle label and one more unit of entry depth. These operations assign each of the \(3^{15}\) states to exactly one periodic orbit and record its exact earliest entrance time and individual attractor-basin size.

**Second complete classifier:** `independent.cpp` reconstructs the same abstract graph from a different presentation of the Petersen graph, namely the disjointness graph on the ten two-element subsets of a five-element set. It independently builds the line graph, encodes the active and refractory locations in separate fifteen-bit planes, and calculates each successor with bit intersections and population counts rather than base-three digit operations. Instead of indegree peeling it directly walks forward from every unclassified starting state, separates the reached cycle from its transient prefix, and propagates root, period and depth backward down that actual path. Both constructions cover the whole \(3^{15}\)-state space and agree on every attractor count, first-entry histogram, period-by-entry histogram, and basin-size histogram for all four thresholds (see `replay.py`). Because the graph labels differ, numerical witness encodings can differ between the implementations; the aggregate quantities are graph-isomorphism invariants.

For a directly checkable sharp threshold-two witness in the **first** graph labeling, the integer \(s=66495\) denotes the digits \((0,1,2,2,1,0,1,0,1,0,1,0,0,0,0)\), least significant first. The complete trajectory of encoded integers is
\[
66495\to5626834\to12602018\to3228168\to169\to2\to0.
\]
The intermediate states are nonzero and the sixth update first reaches the absorbing zero state. The exhaustive census establishes that no state requires longer, so the threshold-two bound is attained. Similarly the threshold-one state encoded by \(94238\) has first periodic-entry depth exactly twelve. The specific cycle representatives with least periods \(3,4,5,8\) are given as full closed trajectories in `threshold1.txt`, proving every listed exceptional period is realized. At thresholds three and four, the exhaustive classifications give sharp entry depth three.

Counting complete graphs with a deterministic map proves all claimed finite enumerations, and reconstructing every step from source avoids reliance on a summary log as proof. No extension to arbitrary graph orders or other thresholds is asserted.

## Verification

From this directory run `python3 replay.py` with Python 3, a C++17 compiler (`g++`), and sufficient memory for the fifteen-vertex complete-state functional graphs (roughly a few hundred megabytes). The replay script compiles the two C++ files, executes them for each of the four thresholds, independently parses the new outputs, compares them to the recorded outputs and to one another, and checks the expected totals, every individual basin-size histogram entry, entry-time-by-period count, fixed and primitive cycle counts, sharp maximum entry time and total \(3^{15}\) population. The complete run passed; the source, not just the captured stdout, is provided.

The individual output files are `threshold1.txt` through `threshold4.txt` and `independent1.txt` through `independent4.txt`. The two independently defined vertex orderings need not produce matching integer state labels; the mathematically invariant full counts agree. No external computer-assisted proof system or third-party certification is claimed.

## Relationship to prior work

The three-state Greenberg–Hastings automaton and contact-threshold questions predate this census. Durrett and Griffeath's 1993 preprint addresses threshold-dependent excitable automata, principally in extended spatial systems [1]. Doba's finite-graph theorem [2] studies the **single-contact** graph Greenberg–Hastings map and its asymptotic behavior using path/cycle geometry; it does not present the threshold-two Petersen line-graph extinction census. Gravner, Lyu and Sivakoff [3] study long-time activity and synchronization for three-state **threshold-one** excitation on arbitrary finite graphs; their results do not supply the labelled exact attractor/basin populations of this specific graph or the threshold-two collapse.

Two particularly relevant structural results [4,5] must be distinguished carefully. The previously established cubic-line-graph/Tait-coloring correspondence [4] eliminates *initially primitive three-cycles* under threshold two when the base cubic graph is the snark Petersen graph. A separate half-degree rigidity theorem [5] characterizes threshold-two initial three-cycles on any connected four-regular graph by balanced proper colorings. Neither result excludes periods other than three nor certifies global extinction or a sharp six-step bound. Furthermore, the previously established induced-edge-density extinction criterion [6] applies only when \(\rho(G)<\theta\). This line graph is four-regular, so \(\rho(G)=|E(G)|/|V(G)|=30/15=2\): the condition **fails exactly at the critical threshold \(\theta=2\)**. Its universal-extinction result therefore cannot imply the key boundary case computed here. The novelty claim is specifically the exact four-threshold dynamics, the full period-and-basin census and the critical extinction cutoff, not the known absence of threshold-two primitive three-cycles.

## Limitations

The theorem concerns the one explicitly defined fifteen-vertex labelled graph and the four indicated contact thresholds. It does not claim a universal extinction criterion for arbitrary cubic line graphs, class-two bases, or larger networks. The proof relies on exhaustive integer computation of a finite functional graph; compiling and rerunning it is required to reproduce its numerical certificate. The two classifiers were implemented separately but their scientific assessment is not independent external validation. Existing graph-theoretic statements, historical computational tables, or unindexed publications may contain equivalent classifications not found in the literature and repository comparisons; priority is qualified, not certified. The full 1993 original preprint was not inspected in full text and should not be treated as definitively excluding an equivalent result.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, first publicly posted 1993-03-22, arXiv:patt-sol/9303002, https://arxiv.org/abs/patt-sol/9303002.
2. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems 27 (2018), 101–135, https://doi.org/10.25088/ComplexSystems.27.2.101.
3. J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, first posted 2016-10-24, https://arxiv.org/abs/1610.07320.
4. *Tait colourings as primitive-three excitation on cubic line graphs, with a constant-six seam law*, 2026 public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-tait-colourings-as-primitive-three-excitation-on-cubic-line-grap--c4fb511b080a.
5. *Half-degree rigidity and a sharp contact-threshold collapse on squared cycles*, 2026 public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-half-degree-rigidity-and-a-sharp-contact-threshold-collapse-on-s--7c3fe196f42d.
6. *A densest-subgraph threshold and finite excitation budget for three-state graph dynamics*, 2026 public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-densest-subgraph-threshold-and-finite-excitation-budget-for-th--352367f51e91.
