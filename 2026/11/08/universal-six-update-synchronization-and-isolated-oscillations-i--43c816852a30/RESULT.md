# Universal six-update synchronization and isolated oscillations in three-color multipartite firefly networks

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be any labelled complete multipartite graph, with \(r\ge3\) nonempty parts and positive integers \(n_1,\ldots,n_r\). Under the synchronous three-color inhibitory firefly rule defined below, the only eventual least periods are \(3\) and \(4\), and every initially nonperiodic configuration synchronizes within six updates. Thus the global map satisfies
\[
F^{18}=F^6.
\]
Every configuration that eventually remains asynchronous is **already periodic at time zero**: there are no proper transient basins feeding asynchronous orbits. More precisely, the periodic states are exactly:

1. The three monochromatic states, forming one primitive three-cycle.
2. A configuration with all vertices of one part occupying **all three** colors and every vertex outside that part in color \(2\). These form primitive asynchronous three-cycles.
3. A configuration with exactly two distinct parts having both colors \(\{0,2\}\) and \(\{1,2\}\), respectively, with all other vertices in color \(2\). These form primitive four-cycles.

Put \(U_2(n)=2^n-2\) and \(U_3(n)=3^n-3\cdot2^n+3\). The number of primitive asynchronous three-cycle orbits and the number of primitive four-cycle orbits are, respectively,
\[
Q_3=\frac13\sum_{i=1}^{r}U_3(n_i),\qquad
Q_4=\frac12\sum_{1\le i<j\le r}U_2(n_i)U_2(n_j).
\]
There is also exactly one synchronized three-cycle. The exact population that eventually synchronizes is
\[
3^{\sum_i n_i}-\sum_iU_3(n_i)-2\sum_{i<j}U_2(n_i)U_2(n_j).
\]
A primitive four-cycle exists exactly when at least two parts have size at least two; a primitive asynchronous three-cycle exists exactly when at least one part has size at least three. The **sharp largest first-periodic-entry time** is \(3\) when every part has size one, and \(6\) otherwise. For fixed \(r\ge3\), on the balanced graphs with all part sizes \(n\to\infty\), the probability of nonsynchronization is asymptotic to
\[
r(r-1)\left(\frac4{3^r}\right)^n,
\]
and conditional on nonsynchronization, the probability of eventual least period \(4\) tends to one.

## Assumptions and scope
The graph is simple and loopless, and its \(r\) labelled nonempty parts have no internal edges and every possible edge between distinct parts. Each vertex has a phase in \(\{0,1,2\}\), with blinking phase \(1\). Simultaneously at each integer step, a vertex in phase \(2\) **stays at phase \(2\)** if it has a neighbor in phase \(1\); every other vertex advances by one modulo \(3\). The first-periodic-entry time \(T(x)\) is the least nonnegative \(t\) for which \(F^t(x)\) belongs to its eventual periodic orbit. Synchronization means all vertices share one phase (and then advance together in a primitive three-cycle). All formulas count labelled initial colorings, without identifying spatial automorphisms.

## Proof
**Step 1: exact representative dynamics.** Each part has identical external neighborhoods, so vertices in the same part with the same initial color always retain identical future color histories. For each part record the nonempty initial support \(S\subset\{0,1,2\}\), one of seven masks \(1,\ldots,7\), and keep a separately tagged representative of every initially present color. Tags are retained even if two color classes later merge. The resulting tagged dynamics agrees with all original labelled vertex trajectories, including exact first-periodic-entry times.

**Step 2: multiplicity saturation at two.** Let \(c_S\) be the number of parts with initial support \(S\). All parts of the same support type have the same tagged histories, by induction. At any later time let \(b_S\in\{0,1\}\) indicate whether that type currently contains a blinking color. A part of type \(S\) sees a blinking neighbor precisely when
\[
\bigvee_T\bigl(b_T=1\ \text{and}\ c_T-\mathbf1_{T=S}>0\bigr).
\]
This Boolean expression depends on every \(c_T\) only through \(\min(c_T,2)\). Therefore replacing any number \(c_T\ge2\) by exactly two tagged copies preserves every tagged representative's entire history, hence its first-periodic-entry time and eventual least period. A complete classification for arbitrarily many parts thus reduces to the finite set of seven-tuples \(d\in\{0,1,2\}^7\) realizable by at least three original parts: either one coordinate equals \(2\), or at least three coordinates equal \(1\). There are exactly \(2158\) such tuples.

**Step 3: finite exhaustive lemma.** The standalone file `verify_reduced.py` implements the exact tagged transition using only the preceding definition; it enumerates each of the \(2158\) tuples and follows its orbit until its first repeated complete tagged configuration. It asserts for every tuple that the first repetition occurs with preperiod at most six and least period three or four; every positive-preperiod orbit enters a synchronized three-cycle. Among tuples with preperiod zero and at least three realizable parts, the only recurrent patterns are: one singleton support repeated (uniform global color); one all-three-color part plus otherwise pure color-\(2\) parts; or exactly one \(\{0,2\}\) part, one \(\{1,2\}\) part, and otherwise pure color-\(2\) parts. The certificate separately asserts this **entire finite classification**, not merely the convergence bound, and reports a checksum census of the temporal classes. Since the equivalence in Step 2 holds for all positive part sizes and all numbers of parts, this bounded finite enumeration is exhaustive for the stated infinite graph family. The complete finite algorithm is embedded, not assumed as an external oracle.

**Step 4: labelled counting.** For a specified part of size \(n\), the number of phase assignments that use exactly a specified support of cardinality two is \(U_2(n)=2^n-2\). For a specified support of cardinality three it is \(U_3(n)=3^n-3\cdot2^n+3\), by inclusion–exclusion. The recurrent configurations characterized in Step 3 therefore comprise \(3+\sum_iU_3(n_i)\) phase-three states and \(2\sum_{i<j}U_2(n_i)U_2(n_j)\) phase-four states. Dividing by their least periods yields the orbit counts. Since every nonperiodic orbit subsequently synchronizes, subtracting the asynchronous populations from all \(3^{\sum n_i}\) labelled configurations gives the exact synchronization basin. The stated existence thresholds are immediate from \(U_k(n)>0\iff n\ge k\).

**Step 5: sharp boundaries.** If every part is a singleton, the graph is a complete graph; the finite lemma restricts its first-entry times to at most three, and the configuration with all but one vertex in phase \(0\) and the remaining vertex in phase \(2\) first becomes periodic at step three. If any part has at least two vertices, put both phases \(0\) and \(2\) in that part, and put all other vertices in phase \(0\). The tagged transition exhibits first periodic entry at step six, for every number of other parts and every positive part size. Hence both maxima are attained. The global functional identity follows from entry time at most six and least period dividing \(12=\operatorname{lcm}(3,4)\).

**Step 6: balanced asymptotics.** For \(r\) fixed parts of equal size \(n\), the total nonsynchronizing population is \(rU_3(n)+r(r-1)U_2(n)^2\). Since \(U_2(n)\sim2^n\) and \(U_3(n)\sim3^n\), the second term dominates and division by \(3^{rn}\) proves the asserted rare-nonsynchronization and conditional period-four limits.

## Verification
Run `python3 verify_reduced.py` and `python3 verify_direct.py` in the directory containing these embedded files. The first program exhaustively classifies all \(2158\) realizable saturated support-multiplicity patterns and checks the complete recurrent pattern descriptions. The second independently updates every individual vertex using an explicit adjacency list. It checks every labelled initial coloring of \(19\) graph instances with \(3\) through \(6\) parts, covering \(84{,}753\) configurations. Both programs passed. Their actual captured stdout is in `reduced_output.txt` and `direct_output.txt`. The independent graph enumeration corroborates the theorem; the all-size proof is Steps 1–4 plus the exhaustive, bounded transition certificate.

## Relationship to prior work
Lyu introduced and analysed this inhibitory firefly update in the publicly available 2014 preprint and established synchronization criteria on paths and trees, with broader geometric and branch-width results; the 2016 tree analysis focuses on general-color degree criteria and synchronization complexity. Those results do not give the present unbounded-part complete-multipartite recurrent classification or the six-step sharp bound. Existing calculations for bipartite three-color firefly dynamics concern only two parts; their formulas do not imply the behavior after adding all cross-edges of one or more additional parts. Related five-color tripartite and binary additive parity models have different transition rules, so their periodic orbit statements do not entail the present theorem. The reported enumeration is not a claim of a new general finite-automata method.

## Limitations
The result applies to simple complete multipartite graphs with at least three nonempty parts and exactly three inhibitory firefly colors. It does not apply to general graphs, other blinking thresholds, asynchronous updates, or stochastic pulse transmission. Novelty is assessed against accessible literature and known related classifications, not certified against all unpublished or unindexed work. The finite certificate has been checked by ordinary code execution, not an external formal proof assistant; a separate independent mathematical audit has not occurred.

## References
1. H. Lyu, *Synchronization of finite-state pulse-coupled oscillators*, arXiv:1407.1103, first posted 2014-07-04. https://arxiv.org/abs/1407.1103
2. H. Lyu, *Time complexity of synchronization of discrete pulse-coupled oscillators on trees* (later titled *Phase transition in firefly cellular automata on finite trees*), arXiv:1610.00837, first posted 2016-10-04. https://arxiv.org/abs/1610.00837
