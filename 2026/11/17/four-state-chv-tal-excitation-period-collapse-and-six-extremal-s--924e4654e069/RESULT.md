# Four-state Chvátal excitation: period collapse and six extremal symmetry classes

## Finding

On the standard labelled Chvátal graph, synchronous threshold-one four-state Greenberg–Hastings dynamics has **exactly one fixed configuration and 29,602 primitive four-cycles**, with no other primitive temporal periods. Equivalently, its periodic-state population is exactly \(118{,}409\): one quiescent state and \(118{,}408\) rotating four-periodic states. The whole map satisfies the sharp global identity

\[F^{16}=F^{12}.\]

Every one of the \(4^{12}=16{,}777{,}216\) labelled configurations first enters a periodic orbit by time \(12\), and exactly \(48\) configurations require time \(12\). Those 48 configurations all enter four-cycles and split into **six orbits of eight configurations** under the graph's full eight-element automorphism group. The exact joint distribution of first periodic entry time and eventual least period has 21 nonempty classes, all given in `chvatal4_joint_census.csv`.

Every nonzero periodic configuration is precisely a *successor-supported four-coloring*: for every vertex \(v\) there is an adjacent vertex \(u\) with \(x(u)\equiv x(v)+1\pmod4\). The local dynamics then rotates all twelve colors synchronously. The four-state period spectrum is therefore much smaller than the six-period spectrum of the three-state excitation automaton on the same graph; the latter has primitive eleven-cycles, whereas the four-state system has none.

## Assumptions and scope

Let \(G=(V,E)\) have \(V=\{0,1,\ldots,11\}\) and exactly the following 24 undirected edges, in the standard Chvátal labelling:

```text
(0,1) (0,4) (0,6) (0,9) (1,2) (1,5) (1,7) (2,3)
(2,6) (2,8) (3,4) (3,7) (3,9) (4,5) (4,8) (5,10)
(5,11) (6,10) (6,11) (7,8) (7,11) (8,10) (9,10) (9,11)
```

This is a simple connected 4-regular graph, with no loops, 12 vertices, girth four and chromatic number four. For any \(x\in\{0,1,2,3\}^{V}\), set

\[
(Fx)(v)=\begin{cases}
1,&x(v)=0\text{ and some neighbor has state }1,\\
0,&x(v)=0\text{ and no neighbor has state }1,\\
x(v)+1,&x(v)\in\{1,2\},\\
0,&x(v)=3.
\end{cases}
\]

All vertices update simultaneously from the old configuration. There is no stochastic input. The first periodic-entry time \(\tau(x)\) is the least \(t\ge0\) for which \(F^t(x)\) lies on a directed temporal cycle. The eventual least period \(p(x)\) is the length of that cycle. An orbit is a set of periodic states modulo time shifts; a spatial symmetry acts by permuting vertex labels.

## Proof

**Rigid four-periodic states.** Suppose \(x\) has a temporal period dividing four. At any vertex, either the local state remains zero throughout all four phases or it takes, cyclically, the four distinct values \(0,1,2,3\) in deterministic order: once state 1 occurs, states 2, 3 and 0 necessarily follow before the initial phase repeats. On a connected graph, a forever-zero vertex cannot have a periodically rotating neighbor, because the neighbor becomes excited at some time and would excite that zero vertex. Therefore either all vertices remain zero or all rotate synchronously through the four phases. For the latter, each vertex must see a neighbor of its successor color precisely at its zero phase, which is equivalent to the stated successor-supported coloring condition at any fixed phase. Conversely, a coloring satisfying that condition rotates by a global one-step phase shift; this preserves the condition and yields primitive period four. The all-zero coloring is the unique fixed point, since no nonzero state is locally fixed.

**Exact exhaustive finite-state certificate.** Encode each state bijectively by \(s=\sum_{j=0}^{11}x(j)4^j\) in the integer range \(0\le s<2^{24}\). The fully supplied program `census.cpp` constructs the unique successor for *every* integer in that range, computes each state's indegree and performs zero-indegree elimination. A finite functional graph consists of disjoint cycles with directed in-trees: repeatedly removing zero-indegree vertices leaves precisely those cycles. Traversing each remaining cycle yields its exact least period, and processing removed states in reverse elimination order yields

\[\tau(s)=1+\tau(Fs),\qquad p(s)=p(Fs).\]

Thus the complete output, not a finite sample or extrapolation, certifies period counts \(1:1\) and \(4:29{,}602\) (cycles), a sharp maximum entry time \(12\), 48 maximizers and the 21-class joint census. The unique period-one orbit and the \(118{,}408\) period-four states are consistent with the separate successor-support count. Because all states enter a period-one or period-four cycle by time 12, \(F^{16}=F^{12}\) on the entire state space. Since a state of entry time 12 exists, no earlier uniform entry bound is valid.

**Independent recurrence and support checks.** `independent.cpp` independently constructs successors by base-four division and an explicit four-neighbor array, then classifies all trajectories using memoized path exploration rather than indegree elimination. Its period/entry count table exactly matches `census.cpp` class by class. `phase_coloring.cpp` independently enumerates all \(4^{12}\) four-colorings for the local successor-support condition, obtaining exactly \(118{,}408\), or 29,602 primitive four-orbits. These computations are exact finite enumerations with integer arithmetic.

**Extremal spatial symmetry.** `census_with_reps.cpp` produces the complete list of 48 states with \(\tau=12\). `symmetry_check.py` independently enumerates all vertex bijections preserving adjacency, pruning a finite backtracking search only when a mapped edge/nonedge disagreement makes completion impossible. It finds exactly eight automorphisms and checks that their action partitions the list of 48 maximal states into six size-eight orbits. The least numeric representatives are 631068, 1610979, 2029061, 2029253, 2029317 and 2029509 in the above base-four coding.

## Verification

After extracting the supplied files into one directory, use a C++17 compiler and Python 3:

```sh
g++ -O3 -std=c++17 census.cpp -o census
./census > check_census.out
diff -u census.out check_census.out

g++ -O3 -std=c++17 independent.cpp -o independent
./independent > check_independent.out
diff -u independent.out check_independent.out
diff -u check_census.out check_independent.out

g++ -O3 -std=c++17 census_with_reps.cpp -o census_with_reps
./census_with_reps > check_reps.out
diff -u census_with_reps.out check_reps.out

python3 symmetry_check.py

g++ -O3 -std=c++17 phase_coloring.cpp -o phase_coloring
./phase_coloring
```

The last Python command must run where the supplied `census_with_reps.out` is present. `chvatal4_joint_census.csv` includes all nonzero entries of the exact joint census. The full table sums to \(16{,}777{,}216\); its period-one basin totals \(3{,}791{,}756\), and its period-four basin totals \(12{,}985{,}460\). The periodic population totals \(1+4\cdot29{,}602=118{,}409\). Two independent all-state algorithms and a separate direct periodic-coloring enumeration agree. These files are computational proof artifacts for this exact finite graph, not evidence of independent external mathematical validation.

## Relationship to prior work

Durrett and Griffeath introduced broad finite-color Greenberg–Hastings models in their study of excitable spatial media, emphasizing spirals and phase diagrams on lattices rather than an exact labelled finite-graph orbit census. Gravner, Lyu and Sivakoff develop general finite-graph limiting theory explicitly for **three-color** excitation (2016, Theorem 3); Doba independently studies a three-valued deterministic graph Greenberg–Hastings model (2018, Sections 2–7). The accessible earlier Chvátal-graph census is also a **three-state** result: its six least periods include 11, and its sharp first periodic-entry time is 10. Neither changing the refractory-state count nor transporting those orbit counts to four states is a valid implication. Related four-state complete multipartite results involve graph families unlike the triangle-free four-chromatic Chvátal graph and do not determine this 12-step cutoff or the six extremal symmetry classes.

The contribution claimed here is solely the complete **four-state Chvátal-graph** period/entry classification, its successor-supported recurrence description, and extremal symmetry census. The model, the graph, the general connected-graph synchronization phenomena, and the earlier three-state spectrum are not claimed as discoveries.

## Limitations

All statements concern this specific labelled 12-vertex graph and its deterministic threshold-one rule; they establish no general theorem for every four-regular or four-chromatic graph, nor that increasing the refractory count always removes long periods. The exhaustive proof is computer-assisted: the claim depends on the supplied finite-state algorithms and their correct implementation of the explicit graph and update rule. Agreement of independently implemented algorithms is strong evidence but is not an external expert review. The 1993 model paper was inspected for its general setup, and relevant later finite-graph primary texts were reviewed; inaccessible or unindexed equivalently specific historical results cannot be ruled out absolutely.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, Experimental Mathematics 2 (1993), 183–208; first public arXiv version 1993-03-22, https://arxiv.org/abs/patt-sol/9303002. Author's lawful open copy: https://services.math.duke.edu/~rtd/reprints/paper79.pdf.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (2016-10-24), https://arxiv.org/html/1610.07320v1.
3. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems 27 (2018), 101–126, https://content.wolfram.com/uploads/sites/13/2018/09/27-2-1.pdf.
4. V. Chvátal, *The smallest triangle-free 4-chromatic 4-regular graph*, Journal of Combinatorial Theory 9 (1970), 93–94; DOI 10.1016/S0021-9800(70)80057-6. Standard graph parameters and labelling cross-referenced with https://mathworld.wolfram.com/ChvatalGraph.html.
5. *Excitation on the Chvátal graph: a unique symmetry class of eleven-cycles and the complete entrance census* (public three-state Chvátal-graph result, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-excitation-on-the-chv-tal-graph-a-unique-symmetry-class-of-eleve--05c6ca769af2.
