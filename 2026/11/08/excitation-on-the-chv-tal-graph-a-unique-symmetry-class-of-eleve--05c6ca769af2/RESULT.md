# Excitation on the Chvátal graph: a unique symmetry class of eleven-cycles and the complete entrance census

## Finding

Let \(H\) be the labelled 12-vertex, 24-edge Chvátal graph specified below, and let \(F\) be the synchronous three-state Greenberg–Hastings update with states 0 (resting), 1 (excited), and 2 (refractory). In the finite dynamical system \(F:\{0,1,2\}^{12}\to\{0,1,2\}^{12}\):

* The **only eventual least periods** are \(1,3,4,7,10,11\). The respective numbers of primitive temporal cycles are exactly \(1,4768,294,1012,504,8\). Thus there are exactly \(6587\) primitive temporal cycles and \(27693\) periodic labelled configurations.
* The eight primitive eleven-cycles form **one orbit under graph automorphisms**: every primitive eleven-cycle is the vertex-relabelled image of every other. In each eleven-cycle, **each of the twelve vertices becomes excited exactly three times**. This is a statement about temporal cycles modulo their own time rotations, not about the 88 distinct states belonging to these cycles.
* Every initial state reaches its eventual periodic cycle in at most **ten** updates, and the bound is sharp. Exactly \(64\) states require ten updates: \(32\) eventually enter a period-three cycle and \(32\) enter a period-eleven cycle.
* The joint distribution of first-periodic-entry time and eventual least period has exactly \(52\) nonempty classes, provided in `chvatal_joint_census.csv`. Every one of the \(531441\) labelled states is counted exactly once.

In particular, the Chvátal graph—an extremal four-chromatic triangle-free four-regular graph—admits a highly constrained symmetry class of prime-period eleven oscillations, while extremal transient states split between two different ultimate periods.

## Assumptions and scope

Number vertices \(0,\ldots,11\), and take the edge set

```text
(0,1) (0,4) (0,6) (0,9) (1,2) (1,5) (1,7) (2,3)
(2,6) (2,8) (3,4) (3,7) (3,9) (4,5) (4,8) (5,10)
(5,11) (6,10) (6,11) (7,8) (7,11) (8,10) (9,10) (9,11)
```

The graph is simple and undirected; these vertices are **labelled** and there are no self-loops. This is the standard Chvátal graph, which has degree four at each vertex, girth four and chromatic number four. The update at time \(t+1\) is: every 1 becomes 2; every 2 becomes 0; a 0 becomes 1 if and only if at least one neighboring vertex is 1, otherwise it stays 0. All updates read only the states at time \(t\), and no random input or threshold above one is used.

For state \(x\), its first periodic entry time \(\tau(x)\) is the least nonnegative \(t\) for which \(F^t(x)\) lies on a temporal cycle; the least period \(p(x)\) is the least positive period of that destination cycle. A primitive cycle is a time-rotation equivalence class of exactly \(p\) distinct periodic states. Spatial automorphisms act on entire cycles by relabelling vertices.

## Proof

The proof is finite, exhaustive, and reproducible. It is not an inference from a sample of trajectories. The listed graph has twelve vertices, so encoding a state by

\[s=\sum_{i=0}^{11}x_i3^i\]

runs bijectively through the interval \(0\le s<3^{12}=531441\). `chvatal_enum.cpp` enumerates every such integer and computes its unique successor from the explicit four neighbors of each vertex. It constructs the complete functional directed graph, including a length-\(531441\) successor array.

The routine then removes all zero-indegree states one by one, decrementing the indegree of their successors (Kahn elimination). Because each state has **exactly one outgoing edge**, the unreduced vertices are precisely the directed cycles. The remaining cycles are traversed individually, so the cycle lists and periods are exact. Processing removed states in reverse removal order assigns \(\tau(x)=1+\tau(F(x))\) and \(p(x)=p(F(x))\). This yields the six cycle counts, all 52 joint classes, and the sharp ten-step bound including 64 equality cases. The complete output is in `chvatal_census.txt`.

A separate implementation, `chvatal_independent.py`, independently evaluates the local rule using a distinct explicit neighbor-list representation and classifies trajectories by memoized first-visit dictionaries, **not** indegree elimination. It agrees on all six primitive-period counts, every one of the 52 joint counts (as checked against the C++ output), the maximal entry time, its 64 attainers and their period split.

For the symmetry statement, the independent program explicitly reconstructs all eight eleven-cycles. Their smallest state-code representatives are

```text
11084, 11085, 11163, 11167, 15440, 15441, 15519, 15523
```

The program contains eight explicit bijections of the twelve vertices. It verifies that each bijection preserves the full set of 24 edges; hence each commutes with \(F\). When applied to the first representative, these eight bijections land in **eight distinct** temporal eleven-cycles. The independent checker also verifies that every vertex fires exactly three times per temporal eleven-cycle. Since the exhaustive enumeration has proved that there are only eight such cycles, all eight belong to one spatial automorphism orbit. Proving that these eight maps are the whole automorphism group is **unnecessary** for transitivity.

## Verification

With a standard C++17 compiler and Python 3, in the extracted directory run:

```sh
g++ -O3 -std=c++17 chvatal_enum.cpp -o chvatal_enum
./chvatal_enum > chvatal_census.txt
python3 chvatal_independent.py > chvatal_independent.txt
python3 compare_joint.py > compare_joint.txt
```

The first Python command also regenerates `chvatal_joint_census.csv`; `compare_joint.py` checks every row against the C++ census. The files `chvatal_census.txt` and `chvatal_independent.txt` contain captured reference outputs. An independent comparison of the complete joint class tables was performed; both implementations yielded identical class-by-class counts. The Python checker verifies graph degree four, triangle-freeness and four-chromaticity, checks the eight graph automorphism witnesses, and prints `PERIOD11_AUTOMORPHISM_TRANSITIVITY_OK`.

The primitive counts imply exactly \(1+3(4768)+4(294)+7(1012)+10(504)+11(8)=27693\) periodic configurations; all joint census entries sum to \(531441\). The maximal-entry row of the CSV consists precisely of the two entries `(10,3,32)` and `(10,11,32)`. These independent accounting identities are reproducibility cross-checks, not substitutes for the complete enumeration.

## Relationship to prior work

Chvátal's 1970 construction identifies the canonical smallest triangle-free four-regular four-chromatic graph. Gravner, Lyu and Sivakoff (first posted 2016-10-24) prove general finite-graph synchronization criteria and excitation activity formulas, including their Theorem 3. Doba (2018) gives cycle-density criteria for eventual behavior and illustrates an eleven-period excitation on a **different** example graph (his Figures 10–13). Thus prime-period eleven itself, the deterministic rule and the general finite-graph asymptotic theory are **not** claimed new.

The assessed distinction is the **complete labelled Chvátal-graph temporal census**, its **single automorphism class of eight eleven-cycles**, and its precise ten-step extremal transient split. The general activity theorems do not state the Chvátal-specific primitive-orbit populations or the class-by-class first-entry counts. A review of relevant primary articles and available research records did not identify an equivalent Chvátal-graph census, but this does not establish absolute historical priority.

## Limitations

The theorem is about **one fixed finite graph**, not all four-regular or four-chromatic graphs. It establishes no universal connection between chromatic number and attainable temporal periods. The computer-assisted classification depends on the correctness of the two supplied programs, the explicit adjacency representation and the semantics of the synchronous local update. The calculations are exhaustive for the specified \(3^{12}\)-state system, not for other graph sizes or update rules. The original 1970 graph paper was not inspected in full; its graph-definition role was cross-checked using an independent graph reference. An equivalent unindexed previous census cannot be excluded without further bibliographic investigation.

## References

1. V. Chvátal, *The smallest triangle-free 4-chromatic 4-regular graph*, Journal of Combinatorial Theory **9** (1970), 93–94. DOI: 10.1016/S0021-9800(70)80057-6.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (first publicly posted 2016-10-24); Annals of Applied Probability **28** (2018), 3324–3357. DOI: 10.1214/17-AAP1350.
3. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems **27** (2018), 101–126. DOI: 10.25088/ComplexSystems.27.2.101. Lawful full text: https://content.wolfram.com/uploads/sites/13/2018/09/27-2-1.pdf.
4. E. W. Weisstein, *Chvátal Graph*, MathWorld, https://mathworld.wolfram.com/ChvatalGraph.html (graph identity and parameters).
