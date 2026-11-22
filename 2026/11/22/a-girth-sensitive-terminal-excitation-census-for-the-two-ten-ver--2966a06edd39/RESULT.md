# A girth-sensitive terminal-excitation census for the two ten-vertex generalized Petersen graphs

## Finding

Consider synchronous three-state, two-contact Greenberg–Hastings excitation on the two graphs \(GP(5,1)\) and \(GP(5,2)\), respectively the pentagonal prism and Petersen graph. For **every** one of the \(3^{10}=59{,}049\) labelled initial configurations of **either** graph, the first all-rest time \(\tau\) is at most four, with sharp equality. The exact first-hitting populations are:

| First all-rest time \(t\) | \(GP(5,1)\) | \(GP(5,2)\) |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 1,023 | 1,023 |
| 2 | 25,415 | 25,205 |
| 3 | 29,230 | 31,300 |
| 4 | 3,380 | 1,520 |

If \(E(x)=\#\{v:x_v=1\}\) is the number of initially excited vertices, the *complete last-wave polynomials* are
\[
\begin{aligned}
L_1(z)&=\sum_{\tau(x)=4}z^{E(x)}=640z^3+1240z^4+1040z^5+400z^6+60z^7,\\
L_2(z)&=\sum_{\tau(x)=4}z^{E(x)}=420z^4+720z^5+320z^6+60z^7.
\end{aligned}
\]
Thus a configuration exhibiting a second excitation generation needs only three initially excited sites on the prism but at least four on the Petersen graph. Of the final-wave configurations, exactly \(3{,}340\) and \(1{,}460\), respectively, have a single excited vertex at update two; the remaining \(40\) and \(60\) have exactly two.

## Assumptions and scope

Write the vertices of \(GP(5,k)\), \(k\in\{1,2\}\), as \(u_0,\ldots,u_4,v_0,\ldots,v_4\), with subscripts modulo five. Its undirected edge set is \(\{u_i u_{i+1},\,u_i v_i,\,v_i v_{i+k}:0\le i<5\}\). Each vertex has three distinct neighbors; there are ten vertices and fifteen edges. At each discrete time, every vertex simultaneously updates its state in \(\{0,1,2\}\) according to
\[
F(x)_v=\begin{cases}
2,&x_v=1,\\
0,&x_v=2,\\
1,&x_v=0\text{ and }\#\{w\sim v:x_w=1\}\ge2,\\
0,&\text{otherwise}.
\end{cases}
\]
Here zero is rest, one excited, two refractory; there is no stochastic forcing, self-contact, or asynchronous updating. The first all-rest time is \(\tau(x)=\min\{t\ge0:F^t(x)=\mathbf0\}\). We count **labelled states**, not graph-automorphism orbits. All statements concern exactly these two graph parameters, not arbitrary generalized Petersen graphs or arbitrary cubic graphs.

## Proof

**A general short-cycle obstruction to three-site second-generation excitation.** Let \(A_t=\{v:F^t(x)_v=1\}\). Suppose \(|A_0|\le3\) but \(A_2\ne\varnothing\). A vertex \(w\in A_2\) has two distinct neighbors \(y,z\in A_1\); since \(w\) was resting at time one, \(w\notin A_0\). Each of \(y,z\), being newly excited at update one, has at least two neighbors in \(A_0\). Two two-element subsets of a set of size at most three intersect, so there exists \(a\in A_0\) adjacent to both \(y,z\). Distinctness follows from \(a\in A_0\), \(y,z\in A_1\), \(w\notin A_0\), and \(w\ne y,z\). Therefore \(a,y,w,z\) form a four-cycle. Consequently, on any four-cycle-free graph, a nonempty second-generation excitation requires at least four initially excited vertices. The Petersen graph has girth five. The prism admits such a three-site wave; one explicit initial state in the fixed vertex order is \((0,0,0,0,1,0,1,0,1,0)\), evolving through
\[
0000101010\to0001202121\to0012000202\to0020000000\to0000000000.
\]
The ten-character words in this display list the states of the named vertices in order, not integer-valued quantities.

**Complete finite certificate.** The finite remainder of the theorem is established by exhaustive application of the displayed local rule. Every state is encoded uniquely as \(s=\sum_{i=0}^{9}x_i3^i\) for \(0\le s<59049\). For each graph, the supplied `verification/check_python.py` constructs precisely the fifteen edges, decodes the full ordered state space by vectorized base-three arithmetic, and evaluates the local rule on all states at each of four steps. Its assertion that **every** state at update four is zero establishes the universal bound without assuming extinction beforehand. The first time a state equals the all-zero vector gives its unique \(\tau\), because that configuration is fixed. The script increments every first-hitting class once, computes the full \(L_k\) coefficients by inspecting \(E(x)\), and counts the size of \(A_2\) for each last-wave state. Each table column sums to exactly \(59{,}049\), and the nonzero final row proves sharpness.

A separate standalone `verification/check_independent.cpp` constructs the same graphs from independent edge loops and decodes states through successive integer divisions, then updates one configuration at a time with an imperative vertex loop. It compares the complete histograms and excitation-support coefficient vectors, without using NumPy or sharing an intermediate transition array. Both fully cover the \(59{,}049\) base-three integers for each graph. The direct update rule, the bijection between states and integers, and the exhaustive bounded loops constitute an exact finite computation, rather than a sample or numerical approximation. These two verifiers reproduce all displayed data.

**Why the last-wave event is a second-generation event.** An excited vertex at time \(t\) automatically becomes refractory at \(t+1\) and resting at \(t+2\). Both exhaustive checks establish \(A_3=A_4=\varnothing\) for all initial states. Hence \(\tau(x)=4\) if and only if \(A_2\ne\varnothing\). This proves that the last-wave polynomial above counts exactly the configurations producing a second generation of excitation; no assertion about later generations is inferred merely from the sample tables.

## Verification

The package contains three complete verifiers, including an independent graph-geometry construction. From the root of its extracted contents, run `python3 verification/check_python.py` (requires NumPy), or compile `g++ -std=c++17 -O2 verification/check_independent.cpp -o check_independent` and run `./check_independent` (C++17 standard library only). They assert complete four-step extinction, exact five-bin first-hitting histograms, and the complete last-wave polynomials; two also check the distribution of second-generation excited sites. The C++ program prints every initial-excitation coefficient of \(L_k\), and both Python programs print their coefficients. Their outputs are included in `verification/results.txt`. The third program, `verification/check_geometry.py`, uses only the Python standard library and builds the Petersen graph from disjoint two-subsets, independently of the outer/inner pentagon representation. There are precisely \(2\cdot3^{10}=118{,}098\) initial states checked by each implementation; no stochastic trials or extrapolation are used.

## Relationship to prior work

Greenberg–Hastings-type excitable automata and contact thresholds originate in the classical literature (Greenberg–Hastings 1978; Durrett–Griffeath 1993). Gravner–Lyu–Sivakoff (2016, §2 and Theorem 3) analyze **threshold-one** three-color excitation on arbitrary graphs: their update activates a resting site with *at least one* excited neighbor, whereas the present update requires *at least two*. Their synchronization theorem is therefore not a theorem about this update. The published exact censuses for the same two generalized Petersen graphs under the threshold-one rule report nontrivial temporal periods seven and eight, respectively, and a six- to eight-update entry cutoff. The threshold-two rule here instead removes every oscillation by update four; the complete finite first-rest and last-wave tables are different mathematical quantities, not corollaries of the one-contact census. Published work on threshold-two complete bipartite, tripartite, wheel, and split graphs concerns other underlying graphs and does not imply this labelled ten-vertex comparison. These comparisons address implication and exact scope, not merely title matching.

## Limitations

The exact counts are finite, computed through exhaustive state enumeration rather than closed all-parameter graph formulas. The short-cycle obstruction is universal, but the two numerical censuses are not claimed to extend beyond \(GP(5,1)\) and \(GP(5,2)\). The threshold-one papers do not settle threshold-two novelty, and unpublished or unindexed earlier enumerations may exist. The original full 1978 and 1993 texts were not fully inspected in this study; only verified bibliographic and available abstract material was used for those references. No independent external mathematical audit is claimed.

## References

1. J. M. Greenberg and S. P. Hastings, *Spatial Patterns for Discrete Models of Diffusion in Excitable Media*, SIAM J. Appl. Math. 34 (1978), 515–523, https://doi.org/10.1137/0134040.
2. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, first arXiv submission 1993-03-22, https://arxiv.org/abs/patt-sol/9303002.
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, first arXiv submission 2016-10-24, https://arxiv.org/abs/1610.07320.
4. *Exact recurrence and basins on the two ten-vertex generalized Petersen graphs*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-recurrence-and-basins-on-the-two-ten-vertex-generalized-pe--7d4c1d4df82a. Its explicitly stated excitation threshold is one.
5. *Five periods and two extremal symmetry orbits in Petersen excitation dynamics*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-five-periods-and-two-extremal-symmetry-orbits-in-petersen-excita--82c758a50988. Its explicitly stated excitation threshold is one.
