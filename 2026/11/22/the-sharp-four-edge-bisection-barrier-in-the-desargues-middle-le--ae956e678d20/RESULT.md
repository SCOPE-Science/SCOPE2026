# The sharp four-edge bisection barrier in the Desargues middle-levels graph

## Finding
Let \(D\) have as vertices the two-element and three-element subsets of \([5]=\{0,1,2,3,4\}\), with adjacency precisely when one set is contained in the other. This is the twenty-vertex, thirty-edge Desargues graph, also the middle levels of the five-cube and \(GP(10,3)\).

For a ten-vertex subset \(S\), let \(c(S)=|\delta_D(S)|\), the number of edges with exactly one endpoint in \(S\). An *unordered bisection* is \(\{S,V(D)\setminus S\}\). Its cardinality is half the number of side-labelled ten-vertex subsets, because complementation has no fixed point.

**Theorem.** The minimum of \(c(S)\) is six. There are exactly five unordered minimizing bisections, namely the partitions by membership of a coordinate \(i\in[5]\):
\[
S_i=\{X\in V(D):i\in X\},\qquad i=0,1,2,3,4.
\]
The complete unordered bisection polynomial is
\[
\begin{aligned}
B_D(z)={}&5z^6+180z^8+2646z^{10}+10320z^{12}+22995z^{14}\\
&+25950z^{16}+20300z^{18}+7926z^{20}\\
&+1815z^{22}+210z^{24}+30z^{26}+z^{30}.
\end{aligned}
\]

For \(b\ge6\), define \(\mathcal R_b(D)\) with a vertex for **each side-labelled** ten-vertex set \(S\) satisfying \(c(S)\le b\). Join \(S\) and \(T\) precisely when \(|S\setminus T|=|T\setminus S|=1\). The connected-component multisets are
\[
\begin{array}{c|c|c}
b&|V(\mathcal R_b(D))|&\text{component sizes}\\\hline
6&10&1^{\times10}\\
8&370&31^{\times10},\ 1^{\times60}\\
10&5662&5650^{\times1},\ 1^{\times12}.
\end{array}
\]
Every 31-state component at budget eight contains exactly one of the ten labelled optima; the 5650-state component at budget ten contains all ten. Therefore the least maximum cut width needed to exchange any two optimum bisections by balanced vertex swaps is **ten**, an excess of exactly four crossing edges above the optimum. Passing to unordered bisections by complementation gives five 31-state components and thirty isolated states at budget eight; at budget ten, a 2825-state component containing every optimum and six isolated states.

## Assumptions and scope
The graph is simple, labelled by its subsets of \([5]\), and edges are unweighted. A balanced set always has exactly ten vertices. A move exchanges exactly one selected and one unselected vertex. The width constraint holds **at every intermediate state**, not only at the start and finish. Both orientations of every cut are included in the reconfiguration graph; this avoids conflating a choice of side with the complementary side. The statement concerns this single canonical graph and does not assert an infinite-family theorem.

## Proof
**1. Structural lower bound and equality.** Write a balanced vertex set \(S=A\cup B\), where \(A\subseteq\binom{[5]}2\), \(B\subseteq\binom{[5]}3\), and \(|A|=r\), \(|B|=10-r\). Define
\[
d_A(T)=\left|\{e\in A:e\subseteq T\}\right|,\qquad T\in\binom{[5]}3.
\]
Because \(D\) is cubic and \(|S|=10\), its internal edge count \(e_D(S)\) satisfies \(c(S)=30-2e_D(S)\). For a fixed \(A\), the maximum possible internal edge count over choices of \(B\) is the sum of the \(10-r\) largest values in the ten-entry list \((d_A(T))_T\).

Enumerating all \(2^{10}=1024\) subsets \(A\) in this exact finite expression gives, for \(r=0,1,\ldots,10\), the maximum counts
\[
(0,3,6,9,12,11,12,9,6,3,0),
\]
and the number of \(A\) attaining each value respectively
\[
(1,10,45,90,5,120,5,90,45,10,1).
\]
These are complete finite sums, not statistical samples: the first loop of `verify_middle_levels.py` enumerates all 1024 choices of the ten two-sets and checks both lists. The maximum internal count is twelve, attained only for \(r=4\) and \(r=6\), with five choices in each case. At \(r=4\), \(A\) is one of the five four-edge stars centred at \(i\), and the unique maximizing \(B\) is the family of six triples containing \(i\). At \(r=6\), \(A\) is one of the five complementary six-edge cliques avoiding \(i\), and the unique maximizing \(B\) is the family of four triples avoiding \(i\). Thus these ten choices are the five coordinate cuts and their complements, each with width \(30-2\cdot12=6\). Every nonoptimum has smaller internal edge count. Since \(c(S)\) is always even, every other width is at least eight.

**2. Exact polynomial.** The complete sum
\[
B_D(z)=\tfrac12\sum_{S\subseteq V(D),\,|S|=10}z^{c(S)}
\]
contains exactly \(\frac12\binom{20}{10}=92378\) terms with multiplicity. The second loop of `verify_middle_levels.py` examines all 184756 labelled choices and all thirty edges for each choice. The independent `verify_gp.cpp` computes the same 184756 cuts from the twenty-vertex generalized Petersen representation \(GP(10,3)\). Both yield the coefficients displayed above; their sum is 92378.

**3. Exchange barrier.** For every budget \(b\in\{6,8,10\}\), the verification code constructs all legal states from the same exhaustive cut table. For each state it generates **all** ten choices of a vertex to remove and ten choices of a vertex to insert; a neighbor is retained exactly when its width is at most \(b\). A breadth-first component traversal then counts all vertices and all components, and separately the number of optimal states in each component. The component-size certificates above are reproduced independently by `verify_middle_levels.py` and `verify_gp.cpp`, whose edge sets arise from nonidentical graph representations. No path between distinct optima can have width at most eight, because each component at budget eight has at most one optimum; paths of width at most ten exist between every pair, since all ten optima are in the single 5650-state component. Every cut width is even, completing the sharpness argument.

## Verification
Run `python3 verify_middle_levels.py`. Independently compile `g++ -std=c++17 -O3 verify_gp.cpp -o verify_gp` and execute `./verify_gp`. These are standalone standard-library programs with no external inputs or downloaded dependencies. Their exact reference outputs are embedded as `verification_middle_levels.txt` and `verification_gp.txt`. Both were executed successfully on the embedded source before packaging. The finite checks are exhaustive for the specified twenty-vertex graph and are sufficient here because the theorem makes no assertion about larger graphs.

## Relationship to prior work
Mütze's 2014 middle-levels paper [1] treats Hamilton cycles in the middle layers of hypercubes; Mütze and Su's 2015 bipartite Kneser paper [2] establishes Hamiltonicity of that larger graph class. The present question is different: exact bisection distribution and low-width vertex-swap mobility. General descriptions of the Desargues graph [3] verify the equivalence of its incidence and generalized Petersen representations but do not establish the cut counts. Prior work on the dodecahedral graph's first low-width bisection excursion concerns another twenty-vertex cubic graph and a different barrier: no result for that graph implies this theorem.

## Limitations
The result is an exact finite classification, not an all-order edge-isoperimetric theorem. Its exchange graph uses single-vertex swaps with exact balance preserved, and its connectedness claims apply only to the listed width budgets. The proof of the numerical component census uses complete independently reproduced enumeration rather than a uniform symbolic classification. A literature search cannot certify absolute priority; unindexed tables and historical work may overlap.

## References
[1] Torsten Mütze, *Proof of the middle levels conjecture*, arXiv:1404.4442, first posted 2014-04-17, https://arxiv.org/abs/1404.4442.

[2] Torsten Mütze and Pascal Su, *Bipartite Kneser graphs are Hamiltonian*, arXiv:1503.09175, first posted 2015-03-31, https://arxiv.org/abs/1503.09175.

[3] Eric W. Weisstein, *Desargues Graph*, MathWorld, https://mathworld.wolfram.com/DesarguesGraph.html.
