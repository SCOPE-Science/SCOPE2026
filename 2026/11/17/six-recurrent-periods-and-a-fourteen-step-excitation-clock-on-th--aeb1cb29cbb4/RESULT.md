# Six recurrent periods and a fourteen-step excitation clock on the Heawood graph

## Finding

The four-state threshold-one Greenberg–Hastings automaton on the Heawood graph has exactly the primitive periods \(1,4,5,6,10,14\). Its labelled recurrent-state populations, its total attraction-basin populations, and its orbit counts are:

| Least eventual period | Recurrent states | Recurrent orbits | Initial states eventually entering this period |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 68,891,440 |
| 4 | 896 | 224 | 24,352,272 |
| 5 | 420 | 84 | 17,913,840 |
| 6 | 252 | 42 | 101,286,864 |
| 10 | 840 | 84 | 39,412,464 |
| 14 | 1,344 | 96 | 16,578,576 |

There are exactly \(3,753\) recurrent configurations and \(531\) recurrent orbits among all \(4^{14}=268435456\) initial configurations. Every orbit becomes periodic in at most fourteen steps; precisely \(2,688\) initial states first enter recurrence at step fourteen, all into primitive five-cycles. The attached `heawood4_census.csv` contains all sixty-four nonempty entry-time/eventual-period populations, including time zero.

## Assumptions and scope

The labelled Heawood graph has vertices \(p_i,\ell_j\) for \(i,j\in\{0,\ldots,6\}\). The vertex \(p_i\) is adjacent to \(\ell_j\) precisely when \(j-i\pmod 7\in\{0,1,3\}\). Each vertex has degree three, the graph is bipartite, and this incidence model is isomorphic to the fourteen-vertex Heawood graph. A configuration assigns one of \(0,1,2,3\) to each vertex. Synchronous updating follows

\[
F(x)_v=\begin{cases}1,&x_v=0\text{ and some }w\sim v\text{ has }x_w=1,\\0,&x_v=0\text{ and no such neighbor exists},\\x_v+1,&x_v\in\{1,2\},\\0,&x_v=3.\end{cases}
\]

Define \(\tau(x)\) as the least nonnegative number of updates before the trajectory is on its eventual directed cycle. Let \(p(x)\) be the least period of that cycle. Each graph vertex is individually labelled; no quotient by graph automorphisms is used in counting configurations. Recurrent orbits identify states only under temporal rotation.

## Proof

This is a finite, exhaustive computational proof with two separate state-graph algorithms and complete program sources. Encode the seven point colors and seven line colors as two fourteen-bit base-four words, together forming an integer in \([0,4^{14}-1]\). The supplied programs construct the actual Fano incidence adjacency and the exact synchronous update for every encoded state. Refractory updates are unconditional; only a resting vertex consults its opposite-shore neighbors currently in state one.

In `heawood4_walk.cpp`, every yet-unclassified state is followed forward. Since the state set is finite, its trajectory encounters a previously classified state or repeats a state on its own path. In the former case the known eventual period and entry depth propagate backwards, increasing the depth by one per predecessor; in the latter the repeated segment is the directed cycle, and the prefix is a transient chain. All states are classified, and each contributes exactly once to one \((\tau,p)\) class.

In `heawood4_pruning.cpp`, the indegree of every state in the full functional graph is computed. Queue-based repeated removal of zero-indegree states leaves exactly the cycle vertices of a finite functional graph. Their primitive cycle lengths are counted by following their successors, and removed vertices are labelled in reverse removal order. This does not use the forward-path classification or its visitation data. The complete output of both algorithms agrees in all sixty-four nonempty joint classes, totals \(4^{14}\), and has maximum entry depth fourteen. The one nonzero class at depth fourteen is period five and contains \(2688\) states. The recurrent populations and orbit numbers are obtained from the depth-zero entries; for period \(p\), the orbit number is the recurrent-state count divided by \(p\).

All arithmetic is integer, the state-space range is exhaustively covered, and both implementations detect their respective small-integer overflow conditions. The accompanying verifier compiles both codes and rejects any mismatch with the complete attached CSV census. The proof is finite and pertains only to this graph and this four-state local rule.

## Verification

Run `python3 verify_heawood4.py` using Python 3 and a C++17 compiler (`g++`). The verifier builds both standalone enumerators, checks each of the sixty-four nonzero joint census entries, confirms that their sum is \(268435456\), and confirms that the number of recurrent states is \(3753\). Both complete enumerations passed when the present package was assembled. The pruning verifier may require several gigabytes of free memory because it explicitly stores the functional graph's indegrees and reverse-elimination queue. See `CHECKS.txt` for the exact validated totals.

## Relationship to prior work

Durrett and Griffeath introduced archival analyses of multi-state Greenberg–Hastings dynamics, emphasizing spatial threshold and large-lattice phenomena [1]. Gravner, Lyu and Sivakoff study the three-color dynamics on arbitrary graphs [2], which does not directly treat four refractory states. A separately indexed three-state Heawood census has eight possible primitive periods and a ten-step entry cutoff [3]. Changing to four states here eliminates the three- and eight-step periods from that model's recurrent spectrum and produces a fourteen-step sharp entrance time. These are comparisons between different state alphabets, not deductions from the three-state result. Earlier four-state results on other graphs do not imply this graph's numerical census.

## Limitations

The numerical classification is specific to the labelled Heawood graph, threshold one, and exactly four local states; no analogous result on arbitrary cubic graphs is asserted. Mathematical correctness relies on complete finite-state enumeration and inspectable programs, not a short symbolic characterization of all orbits. Historical priority remains uncertain because the full text of some early general excitable-media literature was unavailable. Independent external mathematical auditing has not been performed.

## References

[1] R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, initially public 1993-03-22, https://arxiv.org/abs/patt-sol/9303002.

[2] J. Gravner, H. Lyu and D. Sivakoff, *Limiting Behavior of 3-Color Excitable Media on Arbitrary Graphs*, arXiv:1610.07320, initially public 2016-10-24, https://arxiv.org/abs/1610.07320.

[3] *Exact Heawood excitation census: eight primitive periods and a ten-step maximal transient*, published mathematical research record, identifier 29120402709f; its three-state assumption is different from the present four-state one.
