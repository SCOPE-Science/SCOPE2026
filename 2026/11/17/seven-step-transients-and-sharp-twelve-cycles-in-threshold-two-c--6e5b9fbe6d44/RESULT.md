# Seven-step transients and sharp twelve-cycles in threshold-two cyclic dynamics on cone-bicliques

## Finding
Let \(m,n\ge1\), and let \(F\) be the synchronous three-colour threshold-two cyclic cellular automaton on the complete tripartite graph \(K_{1,m,n}\), with singleton hub and two labelled peripheral parts. Every labelled initial configuration satisfies
\[
F^{19}=F^7.
\]
In particular, every configuration is periodic from time at most \(7\), and its eventual **least** period belongs to \(\{1,3,12\}\). The bound \(7\) is attained on \(K_{1,3,4}\). Primitive period \(12\) occurs **if and only if** \(m,n\ge4\); primitive period \(3\) occurs **if and only if** either \(m,n\ge5\), or \(\min(m,n)\in\{1,2\}\) and \(\max(m,n)\ge6\).

Define the exact nonnegative integers
\[
A_s=s![z^s](e^z-1-z)^3,\qquad
B_s=s![z^s]z(e^z-1-z)^2,\qquad
U_s=\begin{cases}2&s\in\{1,2\},\\0&\text{otherwise.}\end{cases}
\]
Among the \(3^{m+n+1}\) **labelled initial configurations**, the number eventually attracted to least period \(3\) is
\[
N_3(m,n)=3\bigl((A_m+B_m)(A_n+B_n)+U_mA_n+A_mU_n\bigr).
\]
There is also an exact, constant-size, coefficient-extraction formula for the period-\(12\) basin. For a capped vector \(a=(a_0,a_1,a_2)\in\{0,1,2\}^3\), set \(G_a(z)=\prod_{c=0}^2g_{a_c}(z)\), where \(g_0(z)=1\), \(g_1(z)=z\), and \(g_2(z)=e^z-1-z\). Define \(\mathcal S_{12}\) to be the **50** ordered pairs of capped peripheral vectors of period \(12\) for fixed initial hub colour zero under the explicit finite recurrence in the proof (the complete construction and executable enumeration are in `verify_capped.py` and `verify_weighted.py`). Then
\[
N_{12}(m,n)=3m!n![z^mw^n]\sum_{(a,b)\in\mathcal S_{12}}G_a(z)G_b(w),\quad
N_1(m,n)=3^{m+n+1}-N_3(m,n)-N_{12}(m,n).
\]
For balanced parts, the period-\(12\) attraction probability has the asymptotic law
\[
\frac{N_{12}(n,n)}{3^{2n+1}}=(2n+6)\left(\frac23\right)^n+O\!\left(n^2\left(\frac49\right)^n\right).
\]

## Assumptions and scope
The graph is the **simple undirected** \(K_{1,m,n}\) with all edges between distinct parts and no edges inside a part; the singleton is called the hub. Colours are \(0,1,2\). A vertex of colour \(c\) changes synchronously to \(c+1\pmod3\) if and only if at least **two distinct neighbours** currently have that successor colour; otherwise its colour is unchanged. All configurations and basins count labelled vertices. For a finite deterministic map, *first periodic-entry time* is the smallest integer \(t\ge0\) such that the state at time \(t\) is periodic. The stated identity is an equality of global maps for every \(m,n\), not an equality merely of population vectors.

## Proof
**1. A uniform exact finite quotient with vertex tags.** Fix an initial configuration. For each of the three graph parts \(j\), and colour \(c\), let \(q_{j,c}\) be the number of vertices of colour \(c\), truncated at \(2\): \(q_{j,c}=\min(2,\#\{\text{colour-}c\text{ vertices in part }j\})\). A threshold query requires only whether a neighbouring colour population is at least \(2\), so the truncated populations determine the update decision for every colour in every part. Set
\[
\delta_j(c)={\bf1}\Bigl\{\sum_{\ell\ne j}q_{\ell,c+1\bmod3}\ge2\Bigr\}.
\]
The exact next truncated population is
\[
q'_{j,d}=\min\left(2,\sum_{c:(c+\delta_j(c))\bmod3=d}q_{j,c}\right).
\]
This formula is exact because \(u\mapsto\min(2,u)\) preserves nonnegative integer sums after truncation. In addition, all vertices in one initial part-and-colour class always move together: let \(T_{j,c}(t)\) be their current colour, initialized by \(T_{j,c}(0)=c\). The exact vertex-tag recurrence is
\[
T_{j,c}(t+1)=\bigl(T_{j,c}(t)+\delta_j(T_{j,c}(t))\bigr)\bmod3.
\]
The hub has only three possible one-hot vectors; each peripheral capped vector belongs to \(\{0,1,2\}^3\). Thus **all sizes** reduce to exactly \(3\cdot 3^3\cdot3^3=2187\) formal initial capped states, including harmless unrealizable formal states. Equality of their tagged states implies equality of every actual labelled vertex configuration; an unoccupied initial class has no effect.

**2. Exhaustive finite lemma and sharp clocks.** The fully specified recurrence above is evaluated over all \(2187\) formal states in `verify_capped.py`, without numerical approximation or sampling. At times \(7\) and \(19\), the **entire** capped state and **all nine** initial-class colour tags agree in every case. It follows that \(F^{19}=F^7\) for all graph sizes. Comparing the state at time \(7\) to the times \(8,9,10,11,13,19\) for initially occupied classes, the finite table has \(2001\) signatures with least period \(1\), \(36\) with least period \(3\), and \(150\) with least period \(12\), and none with periods \(2,4,6\). This supplies a finite exhaustive proof of the universal period restriction, not an extrapolation from a finite selection of graph sizes. For sharp entry time, the actual colouring \(0\mid122\mid0012\) on \(K_{1,3,4}\) satisfies \(F^6(x)\ne F^{18}(x)\), whereas the universal identity forces \(F^7(x)=F^{19}(x)\). Hence its first periodic entry is exactly \(7\).

**3. Period existence and exact three-cycle basin.** Fix hub colour \(0\), and abbreviate a peripheral capped vector by three digits. The complete period-\(3\) signature set produced by the finite recurrence is exactly
\[
\begin{split}
\{&(a,222):a\in\{000,001,010,011\}\}\\
{}\cup\;&\{(222,b):b\in\{000,001,010,011\}\}\\
{}\cup\;&\{(a,b):a,b\in\{122,222\}\}.
\end{split}
\]
For positive part sizes, \(000\) is unrealizable; the other short signatures occur at part sizes \(1\) or \(2\), while \(122\) and \(222\) occur from sizes \(5\) and \(6\), respectively. This proves the asserted sharp period-\(3\) criterion. By counting the labelled assignments in these disjoint signature sets, and then rotating the hub colour in three ways, one obtains exactly the stated formula for \(N_3\).

The complete period-\(12\) signature set has \(50\) pairs for fixed hub colour. Each pair has at least **four** required vertices on each peripheral side (sum of capped entries), proving necessity of \(m,n\ge4\). The pair \((022,202)\) is in this set and is feasible for any \(m,n\ge4\): assign at least two vertices of each positive colour class and put any additional vertices in one of those classes. This proves sufficiency. Counting each capped signature by its exponential generating function yields the stated coefficient formula for \(N_{12}\), and the fixed-point basin is the complement.

**4. Balanced large-size asymptotics.** Among the period-\(12\) signatures for initial hub colour zero, those with one peripheral side \(222\) consist precisely of the other side belonging to \(\{022,121,202,212,220,221\}\), with either shore playing the \(222\) role. The dominant terms arise from the two patterns \(212,221\) of one exact occurrence and two capped-at-least-two colours, and the three patterns \(022,202,220\) of one absent colour and two large classes. Their labelled counts on an \(n\)-vertex side are, respectively,
\[
n2^{n-1}+O(n^2),\qquad 2^n+O(n),
\]
while the count for \(222\) is \(3^n+O(n2^n)\). The remaining pattern \(121\) has \(O(n^2)\) assignments, and every signature with neither side \(222\) has at most \(O(n^2 4^n)\) assignments in total. Summing the two shore choices and three hub colours gives
\[
N_{12}(n,n)=6(n+3)2^n3^n+O(n^2 4^n),
\]
which is the claimed probability asymptotic.

## Verification
Run `python verify_capped.py` for the complete formal-state certificate, `python verify_vertices.py` for a separately implemented direct labelled-vertex update on seven graph sizes (including all \(177147\) states on \(K_{1,5,5}\)), and `python verify_weighted.py` for independent exact multinomial basin weighting. Outputs appear in the three accompanying `.out` files and were regenerated from these source files. The formal-state certificate checks every possible truncated input rather than merely the listed small graphs. The direct checker confirms the sharp seven-step witness and the period-\(12\) labelled-state census; the weighted checker evaluates larger balanced cases and the analytical \(N_3\) formula.

## Relationship to prior work
The contact-threshold definition is classical in the cyclic cellular-automaton literature, notably Durrett and Griffeath's study of lattice excitation and Bello and Sivakoff's treatment of infinite regular trees. The latter works address lattice or infinite-tree oscillation and fixation, not a finite complete-tripartite cone with an exact global map identity and labelled attraction-basin formulas. An earlier exact result for the *bipartite* graph \(K_{m,n}\) under this rule has a three-step transient bound and possible period \(4\); its conclusions do **not** imply this theorem, as joining one universal vertex changes every peripheral update condition, creates genuine labelled period \(12\), and changes the settling bound. General finite-graph cyclic-network period bounds are also distinct from the sharp family-specific classification and coefficient law supplied here.

## Limitations
This result is restricted to the specific three-colour contact rule with threshold two, to the graph family \(K_{1,m,n}\), and to synchronous updates. The period-\(12\) coefficient formula uses a finite 50-signature set defined constructively by the included recurrence, rather than a single short closed polynomial in \(m,n\). The theorem does not classify the number of distinct *temporal orbits* within each attraction basin, and makes no claim about threshold values other than two. The original full text of a plausible 1995 finite-graph cyclic-network predecessor was not accessible through authorized sources, so mathematical historical priority is qualified.

## References
1. Richard Durrett and David Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, first publicly posted 1993-03-22, https://arxiv.org/abs/patt-sol/9303002.
2. Martín Matamala and Eric Goles, *Cyclic Automata Networks on Finite Graphs*, LATIN 1995, Lecture Notes in Computer Science 911, pp. 398–410, https://doi.org/10.1007/3-540-59175-3_105.
3. Jason Bello and David Sivakoff, *Cyclic Cellular Automata and Greenberg–Hastings Models on Regular Trees*, arXiv:2108.06404, first publicly posted 2021-08-13, https://arxiv.org/abs/2108.06404.
