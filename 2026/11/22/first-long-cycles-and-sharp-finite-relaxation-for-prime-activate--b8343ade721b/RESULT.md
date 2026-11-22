# First long cycles and sharp finite relaxation for prime-activated Boolean tournaments

## Finding

For the synchronous prime-activated Boolean map on all loopless tournaments of order \(1\le n\le7\), the complete least-period spectra \(\mathcal P_n\) and maximum first-periodic-entry times \(\tau_n\) are:

| Number of vertices \(n\) | Complete attainable least-period set \(\mathcal P_n\) | Sharp \(\tau_n\) |
|:--:|:--|:--:|
| 1 | \(\{1\}\) | 1 |
| 2 | \(\{1\}\) | 1 |
| 3 | \(\{1\}\) | 2 |
| 4 | \(\{1\}\) | 2 |
| 5 | \(\{1\}\) | 4 |
| 6 | \(\{1,3\}\) | 9 |
| 7 | \(\{1,2,3,4,5,6,7,8,9\}\) | 23 |

In particular, a nonfixed cycle first occurs for a tournament on six vertices. At seven vertices, every period from one through nine occurs, and no longer period occurs.

Exactly \(10080\) of the \(2^{21}=2097152\) labeled seven-vertex tournaments have longest cycle of length nine. Under relabeling they form exactly two isomorphism classes, each consisting of \(5040\) labeled tournaments. Exactly \(5040\) ordered pairs consisting of a labeled seven-vertex tournament and an initial Boolean state attain first-periodic-entry time \(23\); they form one orbit under simultaneous relabeling.

The exact counts of labeled seven-vertex tournaments by their **maximum** least period are:

| Maximum least period | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|--|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Count | 1633632 | 30240 | 329840 | 25200 | 30240 | 21840 | 11040 | 5040 | 10080 |

## Assumptions and scope

A *tournament* is a finite directed graph on a labeled vertex set \(V=\{0,\dots,n-1\}\) with no loops and exactly one directed edge between each distinct pair. In particular it is **not** the bidirected complete graph. A Boolean state is an active-vertex subset \(S\subseteq V\). One synchronous update is

\[
F_G(S)=\left\{v\in V:\left|N^-_G(v)\cap S\right|\text{ is prime}\right\}.
\]

The least period of a periodic state \(S\) is the smallest positive integer \(p\) such that \(F_G^p(S)=S\). The first-periodic-entry time of any state is the least \(t\ge0\) such that \(F_G^t(S)\) is periodic. We quantify over **every** tournament and **every** initial state on each specified number of vertices; \(\tau_n\) is the maximum such entry time. Since each count of incoming active neighbors is at most six, the only relevant primes are \(2,3,5\).

A tournament is encoded by an integer from \(0\) to \(2^{\binom n2}-1\). For each pair \((i,j)\) with \(i<j\), ordered lexicographically, the corresponding bit equals one for the arc \(i\to j\) and zero for \(j\to i\). A state is the integer whose bit at position \(i\) records activity at vertex \(i\).

## Proof

This is an exact finite exhaustive proof with two independent state-space classifiers and a third relabeling classifier. To make exhaustiveness a mathematical assertion rather than an inference from output alone, we specify their loops and invariants.

**1. Exhaustiveness of graph encoding.** Each of the \(\binom n2\) unordered vertex pairs independently admits exactly two arc orientations. The integer code ranges through all \(2^{\binom n2}\) possible bit strings without omission or repetition. Since every labeled tournament gives exactly one such code, enumeration of this interval is exhaustive. The code visits \(1,2,8,64,1024,32768,2097152\) tournaments at orders one through seven, respectively.

**2. Exhaustiveness of each dynamical system.** Fix a graph code. The programs build the predecessor bitmask \(I_v\) for each vertex and construct the full transition table by setting bit \(v\) of \(F_G(s)\) precisely when

\[
\operatorname{popcount}(I_v\mathbin{\&}s)\in\{2,3,5\}.
\]

The table contains a successor for every one of the \(2^n\) possible states. No sampling, floating-point comparisons, randomized optimization, or timeouts are involved.

**3. Enumeration of all periodic orbits, by two independent methods.** The first program (`tournament_scan.cpp`) follows each as-yet-unseen state and records the first repeated state on its deterministic successor path. If this repeated state belongs to the current exploration stack, the portion of the stack starting there is exactly one directed cycle. The stack is then marked processed; a previously processed state cannot contribute a new cycle. Therefore this procedure finds every cycle exactly once and its exact length. The second program (`tournament_census.cpp`) constructs the full functional graph indegrees and repeatedly removes indegree-zero states. An edge into a directed cycle cannot be peeled; every state not on a cycle eventually becomes peelable. Consequently the surviving vertices are exactly the periodic states. Following successors among them then independently determines every cycle length. The programs agree on every graph-maximum period count for each order one through seven, giving the table above.

**4. Sharp transient depths.** In the second program, after indegree peeling, the removed vertices are processed in reverse removal order. Every peeled vertex \(s\) points either into a cycle or to a vertex removed later, so its successor's depth is already known. The recurrence \(d(s)=1+d(F_G(s))\), with \(d=0\) on cycles, therefore computes the *exact* first periodic entry time for every state. Its maximum over all graph codes and states yields the stated \(\tau_n\), including \(\tau_7=23\). The equality witness and the complete state list below directly verify attainment.

**5. Completeness of the relabeling classification.** For each of the \(10080\) nine-cycle-bearing labeled tournaments, `tournament_extremes.cpp` applies all \(7!=5040\) vertex permutations to the graph code and deletes all encountered encodings from a set. Exactly two iterations empty the set, and each removes \(5040\) different labeled tournaments. Thus there are exactly two relabeling classes. The same procedure, with the initial-state mask permuted simultaneously with the arcs, empties the complete \(5040\)-pair set of depth-23 extrema in a single orbit. Each set starts from the exhaustive graph-and-state classifier, so these conclusions do not rely on searching for a few graph isomorphisms.

**6. Explicit attainment.** A six-vertex three-cycle has code \(344\) and initial state \(31\), with successive states \(31,47,61\). A seven-vertex nine-cycle has code \(9393\) and initial state \(15\), with successive states

\[
15,99,122,23,107,126,55,105,62.
\]

For the sharp transient, seven-vertex code \(1721\) and state \(86\) give the 24-state prefix

\[
86,46,13,3,96,28,7,98,60,15,99,124,27,110,61,31,111,127,115,118,54,14,1,0,
\]

followed by the fixed point \(0\). The states before zero are distinct, so the first periodic entry occurs after exactly \(23\) updates. The companion `tournament_witnesses.py` independently checks these and witnesses for each intermediate period.

Together, exhaustive coverage plus correctness of the two exact finite classifiers establishes every assertion for \(1\le n\le7\). This is a finite exhaustive theorem, not an extrapolation from experiments.

## Verification

Build and run with a C++17 compiler and Python 3.8 or later:

```bash
g++ -O3 -std=c++17 tournament_scan.cpp -o tournament_scan
g++ -O3 -std=c++17 tournament_census.cpp -o tournament_census
g++ -O3 -std=c++17 tournament_extremes.cpp -o tournament_extremes
for n in 1 2 3 4 5 6 7; do ./tournament_scan "$n"; ./tournament_census "$n"; done
./tournament_extremes 7
python3 tournament_witnesses.py
```

For order seven, both principal programs must report maximum period nine and the graph-count vector in the first table. The second must additionally report maximum depth \(23\). The symmetry program reports two size-\(5040\) nine-cycle graph classes and one size-\(5040\) extremal graph–state class. These are integer-only computations; cycle detection is checked by two different finite-functional-graph algorithms. Source files included are self-contained and require no external data.

## Relationship to prior work

Methawisal, *Pulse Graphs: Prime-Activated Boolean Dynamics on Directed Graphs* (first public posting July 11, 2026), introduced this update rule, found the unrestricted loopless-digraph maximum periods through five vertices, and classified the bidirected complete graphs. Its conclusion explicitly asks for exact attainable-period sets and graph restrictions. Those unrestricted and bidirected results do not determine the present strict one-orientation-per-pair tournament subfamily; in particular their first nontrivial cycles occur earlier because bidirected edges are allowed.

Classical symmetric threshold automata results of Goles and Olivos restrict periods to at most two, but their symmetric-threshold hypotheses fail here: the tournament adjacency is asymmetric, and prime-count activation is not monotone in the number of active inputs. Results about other finite-state graph automata or tournament topology do not specify this prime-count transition law. Literature searches did not locate an exact tournament census for this rule, although absence of a match cannot certify historical novelty.

## Limitations

This is a finite classification **only** for tournaments of order at most seven. It does not determine their full basin sizes, classify tournaments of order eight or above, or solve the largest-period question over all loopless directed graphs. It does not claim that the unique relabeling class of depth-23 pairs means all graph-and-state isomorphism classes have been enumerated for smaller depths. The computational proof depends on correctly implementing integer bit operations and is accompanied by two independent exact cycle algorithms, an additional symmetry enumeration, and explicit orbit witnesses, not an external independent mathematical audit.

## References

- P. Methawisal, *Pulse Graphs: Prime-Activated Boolean Dynamics on Directed Graphs*, arXiv:2607.10453, first publicly posted July 11, 2026. https://arxiv.org/abs/2607.10453
- E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1
