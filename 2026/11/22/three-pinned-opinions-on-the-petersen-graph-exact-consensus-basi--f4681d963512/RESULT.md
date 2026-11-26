# Three pinned opinions on the Petersen graph: exact basins and sharp entry times

## Finding

On the Petersen graph, permanently pin three vertices at opinion one. At each simultaneous update every other vertex takes the strict binary majority of its three neighbors. Identify the vertices with the edges of \(K_5\), with disjoint edges adjacent. The pin shape determines the basin sizes and sharp worst-case time to reach a periodic state:

| Shape of the three pinned edges in \(K_5\) | Labelled pin sets | Starts reaching unanimous one, out of 128 | Starts reaching a primitive two-cycle | Starts reaching another fixed point | Sharp first-periodic-entry time |
| --- | ---: | ---: | ---: | ---: | ---: |
| Three-edge star | 20 | 128 | 0 | 0 | 3 |
| Triangle | 10 | 98 | 28 | 2 | 2 |
| Three-edge path | 60 | 124 | 0 | 4 | 5 |
| Two-edge wedge plus a disjoint edge | 30 | 94 | 30 | 4 | 4 |

Thus the twenty star placements are exactly the three-pin sets for which the entire compatible state space reaches consensus; the worst-case time for each is exactly three. The census also distinguishes the two pin-pair types: the all-one basin has size 141 out of 256 for each of the fifteen adjacent pairs and 188 out of 256 for each of the thirty nonadjacent pairs.

The scalar minimum pin budget of three is background: it is the Petersen specialization of the known two-neighbor bootstrap percolation number of odd graphs. The connection uses the **least** compatible initial state; it does not identify the reversible-majority basins of arbitrary compatible states with bootstrap outcomes. The exact distribution of outcomes and entry times by pin shape is the object studied here.

## Assumptions and scope

The vertex set is \(\binom{\{0,1,2,3,4\}}2\), and \(N(v)=\{u:u\cap v=\varnothing\}\). For fixed pins \(S\), legal states are sets \(A\supseteq S\) of one-valued vertices. The synchronous update is
\[
F_S(A)=S\cup\{v:|N(v)\cap A|\ge2\}.
\]
The first-periodic-entry time is the least \(t\ge0\) for which \(F_S^t(A)\) is on a temporal orbit. The entry time is not necessarily a time to consensus. Basin counts refer to labelled initial states and include periodic starts; two-cycles have least period two. Other outcomes in the table reach a fixed point different from the all-one state.

## Proof

**1. Pin shapes and placement counts.** The automorphisms induced by permutations of the five labels carry any given pin shape to every placement of that shape and commute with the dynamics upon moving the pin set. There are four possible three-edge shapes: a connected three-edge graph is a star, triangle or path; the only disconnected possibility on five labels that uses three edges is a wedge and a disjoint edge. There are \(5\binom43=20\) stars, \(\binom53=10\) triangles, \(\binom54 4!/2=60\) paths, and \(5\binom42=30\) wedges with their complement edge. Two pins correspond to disjoint or intersecting edges in \(K_5\); the first gives fifteen Petersen-adjacent pairs, and the second the remaining thirty.

**2. Least-state trajectories and the bootstrap connection.** The map \(F_S\) is order preserving, with \(S\subseteq F_S(S)\). Thus for \(A_t=F_S^t(S)\) we have \(A_t\subseteq A_{t+1}\), so
\[
A_{t+1}=A_t\cup\{v: |N(v)\cap A_t|\ge2\}.
\]
This is exactly the two-neighbor bootstrap recurrence with initial set \(S\). For any compatible start \(A\supseteq S\), \(F_S^t(A)\supseteq A_t\); universal unanimity therefore holds if and only if \(A_t\) fills the graph. Mohammadian, Rezaie Zareie and Tayfeh-Rezaie's odd-graph formula [1, Theorem 1.2 in v3] gives \(\lceil(k^2+3k+2)/4\rceil\) for disjointness on the \(k\)-subsets of \(2k+1\) labels, which is three at \(k=2\).

Write \(ij\) for \(\{i,j\}\). Direct threshold counting for the star \(S=\{01,02,03\}\) gives
\[
A_0=S,\qquad A_1=A_0\cup\{14,24,34\},\qquad
A_2=A_1\cup\{12,13,23\},\qquad A_3=A_2\cup\{04\}=V(P).
\]
This gives the uniform bound of three updates, attained by the least start. In contrast, the triangle \(\{01,02,12\}\) adds only \(34\) in one step and is then fixed; the path \(\{01,12,23\}\) adds only \(04,34\) and is then fixed; and the wedge-plus-edge \(\{01,02,34\}\) is already fixed, all by the same disjoint-neighborhood test. These trajectories also give the placement characterization without enumerating other compatible states. The census below gives a separate check against forcing with two pins. Adding pins cannot turn a forcing set into a nonforcing set (compare the ordered trajectories via the update rule), so the pair obstruction rules out smaller sets as well.

**3. Complete finite census.** For every pin set \(S\) of cardinality three (respectively two), enumerate the \(2^{10-|S|}\) subsets of its complement and adjoin \(S\). For each start keep a map from states to the time they were first seen, and iterate the displayed \(F_S\) until a state repeats:

```text
time := 0; seen := empty map
while A not in seen:
    seen[A] := time
    A := S union { v : at least two members of N(v) are in A }
    time := time + 1
entry := seen[A]
period := time - entry
```

The update uses the old state for all coordinates. The first repeated state appears by update \(2^{10-|S|}\). Since the dynamics are deterministic, the index of that state's first occurrence is exactly the first entry, and the index difference is precisely the least period. The census gives only periods one and two; for period one the repeated state is tested for unanimity. Taking the class counts and the maximum entry index yields the table. Thus no finite sampling or assumptions about long transients are needed. The computation counts 15,360 legal start/pin instances over the triples and 11,520 over the pairs.

## Verification

The accompanying, unchanged `check_bitmask.py` implements the census with integer masks; `check_tuples.py` implements the triple census with ten-entry tuples and a separate five-letter edge representation. Run each with Python 3 (the bitmask implementation requires `int.bit_count`, available in Python 3.10+). Their reference outputs are `bitmask_results.json` and `tuple_results.json`; the bitmask output includes the pair census and representative entry/period distributions. Only the finite counts rely on this enumeration; the least-state equivalence and placement trajectories above are direct proofs.

## Relationship to prior work and limitations

Two-neighbor bootstrap percolation is also called \(P_3\)-hull closure [1,2]. Irreversible strict-majority dynamic monopolies model that closure on a cubic graph [3]. As shown in the proof, for **universal** forcing with pins these results are directly relevant, not simply studies of the same underlying graph. They do not give the frequencies of reversible-majority outcomes when free sites may start at one and later flip back to zero. Benjamini et al. [4, Theorem 1.1] discuss general eventual fixed/period-two behavior in finite synchronous majority dynamics. That behavior does not fix the relative basin sizes or the sharp entry time for each pinned shape. The unpinned Petersen majority census [5] uses a different transition map and does not supply these pinned basins. The precise profiles concern this ten-vertex graph and fixed-one pins only; no analogous classification is asserted for other graph families, asynchronous updates or a mixture of zero and one pins.

## References

1. A. Mohammadian, S. Rezaie Zareie, and B. Tayfeh-Rezaie, *2-Neighbor Bootstrap Percolation on Odd Graphs*, [arXiv:2606.03687v3](https://arxiv.org/abs/2606.03687v3), Theorem 1.2.
2. L. N. Grippo, A. Pastine, P. Torres, M. Valencia-Pabon, and J. C. Vera, *On the \(P_3\)-Hull Number of Kneser Graphs*, Electron. J. Combin. 28(3) (2021), #P3.32, [article](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v28i3p32).
3. K. Khoshkhah, H. Soltani, and M. Zaker, *On dynamic monopolies of graphs: the average and strict majority thresholds*, [arXiv:1202.1146v1](https://arxiv.org/abs/1202.1146v1).
4. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, [arXiv:1405.2486v1](https://arxiv.org/abs/1405.2486v1).
5. *A four-step Petersen majority projection and the Desargues double-cover basin spectrum*, [Resultary, `b8bcbb0b4dff`](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-a-four-step-petersen-majority-projection-and-the-desargues-doubl--b8bcbb0b4dff).
