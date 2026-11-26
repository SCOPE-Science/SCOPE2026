# Exact attraction-basin spectrum for binary majority dynamics on the Desargues graph

## Finding

Let \(D\) be the 20-vertex Desargues graph, and apply synchronous binary strict-neighbor majority to every vertex. The resulting map has **124 fixed configurations** and **7,626 primitive temporal two-cycle orbits**. The new numerical classification is the **complete distribution of individual attraction-basin sizes**, not merely the numbers of recurrent orbits:

| Eventual orbit | Attractor-basin size | Number of distinct attractors |
|---|---:|---:|
| Fixed | 1 | 72 |
| Fixed | 100 | 50 |
| Fixed | 51,076 | 2 |
| Primitive two-cycle | 2 | 2,556 |
| Primitive two-cycle | 20 | 3,600 |
| Primitive two-cycle | 200 | 1,225 |
| Primitive two-cycle | 452 | 144 |
| Primitive two-cycle | 4,520 | 100 |
| Primitive two-cycle | 102,152 | 1 |

The two unanimous fixed points each attract precisely 51,076 initial configurations. The two-cycle exchanging the all-zero and all-one colorings attracts precisely 102,152 configurations, **the sum of both unanimous fixed-point basins**.

If \(\tau(x)\) denotes the first update at which the future of configuration \(x\) is periodic, the complete entry-time distribution is

| \(\tau(x)\) | Initial configurations |
|---:|---:|
| 0 | 15,376 |
| 1 | 132,080 |
| 2 | 467,200 |
| 3 | 202,560 |
| 4 | 231,360 |

All \(2^{20}=1,048,576\) labelled configurations are accounted for. Four updates are necessary for some configurations and sufficient for all. The fixed-point basins together contain 107,224 configurations, while the two-cycle basins together contain 941,352.

## Assumptions and scope

A graph is simple and undirected. A configuration is \(x\in\{0,1\}^{V(D)}\). The simultaneous update \(F_D\) is defined for every vertex \(v\) by
\[
(F_Dx)_v=\mathbf{1}\!\left\{\sum_{u\sim v}x_u\geq 2\right\}.
\]
Each vertex has degree three, so ties never arise. The basin of a temporal orbit \(\mathcal O\) is the set of initial configurations whose forward orbit eventually reaches \(\mathcal O\); its size counts all labelled initial configurations, not symmetry classes. A two-cycle is counted once as an unordered orbit, not twice by phase. The entry time is \(\tau(x)=\min\{t\geq0:F_D^{t+2}(x)=F_D^t(x)\}\).

An explicit 30-edge labelling of \(D\) appears in `direct_enumerator.cpp`. The certificate `verify_lift.py` provides a bijection identifying those twenty labels with the two layers of the bipartite double cover of the ten-vertex Petersen graph; thus the graph is not identified merely by an unverified name. The formula and classification refer to this exact finite graph, not to arbitrary cubic graphs.

## Proof

**1. Base dynamics.** Let \(P\) be the ten-vertex Petersen graph with the 15 edges listed in the accompanying code, and \(f\) its strict-neighbor majority map. Direct exhaustive evaluation of its 1,024 binary configurations establishes \(f^6=f^4\) as maps, with exact entry-time counts
\[
(c_0,c_1,c_2,c_3,c_4)=(124,260,400,120,120).
\]
Consequently \(R=\{r:f^2(r)=r\}\) has exactly 124 members and the eventual even-phase map \(p(x)=f^4(x)\in R\) is well-defined. Set \(b(r)=|p^{-1}(r)|\). Enumerating the 1,024 explicitly specified inputs gives the exact multiset
\[
\bigl\{b(r):r\in R\bigr\}=\bigl\{1^{[72]},10^{[50]},226^{[2]}\bigr\},
\]
where \(a^{[j]}\) signifies that the value \(a\) occurs with multiplicity \(j\), **not** exponentiation. The two values of 226 occur at the unanimous configurations. These are full finite enumerations, independently checked by a second graph-level implementation, not estimates from sampled states.

**2. Cover dynamics.** For the bipartite double cover of \(P\), write a colouring as the two 10-bit vectors \((x,y)\). Its strict-majority update is exactly
\[
T(x,y)=(f(y),f(x)),\qquad T^2(x,y)=(f^2(x),f^2(y)).
\]
The explicit labelling permutation in `verify_lift.py` verifies that \(T\) is the update of \(D\). Every pair eventually reaches \(R\times R\), and the induced permutation on this 15,376-element set is \(\sigma(r,s)=(f(s),f(r))\), whose square is the identity. A pair \((r,s)\) is fixed if and only if \(s=f(r)\), giving 124 fixed points. The remaining \(124^2-124\) ordered pairs form exactly \((124^2-124)/2=7,626\) temporal two-cycles. This **general bipartite orbit-count principle is prior work**; only its specific basin populations are advanced here.

**3. Exact basin formula.** Because \(p(x)\) and \(p(y)\) are independent eventual even phases, the basin of the fixed point \((r,f(r))\) has size \(b(r)b(f(r))\). For a nonfixed pair \((r,s)\), its two-cycle basin has size
\[
b(r)b(s)+b(f(s))b(f(r)).
\]
Iterating over the completely enumerated 124-element set \(R\), identifying unordered cycles under \(\sigma\), yields exactly the nine rows in the table above. In particular, the two unanimous base phases have \(b=226\), and the cover has two unanimous fixed basins of \(226^2=51,076\), while the complementary-unanimity two-cycle has basin \(2\cdot226^2=102,152\). Every basin has been included once: the weighted totals are
\[
\begin{split}
72+50(100)+2(51,076)&=107,224,\\
2556(2)+3600(20)+1225(200)+144(452)+100(4520)+102,152&=941,352.
\end{split}
\]
They sum to 1,048,576.

**4. Exact entry-time law.** A lifted state is periodic as soon as and only when both coordinates are base-recurrent; hence
\[
\tau_T(x,y)=\max\{\tau_f(x),\tau_f(y)\}.
\]
With \(C_t=\sum_{j=0}^t c_j\) and \(C_{-1}=0\), the number of lifted states first becoming periodic at update \(t\) is \(C_t^2-C_{t-1}^2\). The cumulative base counts \((124,384,784,904,1024)\) yield precisely the entry-time table. Since \(c_4=120\), the bound four is sharp.

## Verification

Two different complete computations agree:

1. `direct_enumerator.cpp` builds the original ten-vertex Petersen graph and, separately, a 20-vertex edge set for the Desargues graph. It applies majority updates independently to **every** one of the 1,024 and 1,048,576 binary configurations, follows their trajectories, and groups results by first-periodic-entry time and actual orbit basin. Reproduce with `c++ -std=c++17 -O2 -Wall -Wextra direct_enumerator.cpp -o check && ./check`. Recorded output is in `direct_output.txt`.
2. `verify_lift.py` does not enumerate the 20-vertex configurations. It verifies an explicit graph-isomorphism witness, computes base eventual phase preimage counts, and reconstructs every Desargues basin and time layer by integer formulas. Reproduce with `python3 verify_lift.py`. It raises an assertion on any disagreement.

The two methods have distinct computational decompositions, although they share the stated graph definition and majority rule. Both are exact integer procedures; they do not certify originality or replace independent mathematical review.

## Relationship to prior work

Adam, Dahleh and Ozdaglar's *On Threshold Models over Finite Networks* (first public preprint 2012-11-04, arXiv:1211.0654) explicitly defines bipartite expansion (Definition 4.14) and proves its general bipartite recurrent-cycle count formula (Lemma 6.10). **Neither bipartite expansion nor counting \(\binom{124}{2}\) two-cycles is claimed as new.** Their general treatment does not state the Desargues graph's individual attraction-basin sizes or the sharp labelled entrance-time distribution calculated here. The classical eventual-period-at-most-two theorem, reviewed by Benjamini et al. (arXiv:1405.2486), is also not claimed as new. Kaaser, Mallmann-Trenn and Natale (arXiv:1508.03519) study general voting-time bounds, not this specific full basin-size spectrum. The Desargues graph's identity as a 20-vertex symmetric cubic graph is standard, as documented by MathWorld.

Published related exact majority-dynamics censuses on the 20-vertex dodecahedral graph, the 14-vertex Heawood graph and other network families concern different graph objects; none of those retrieved claims implies this graph's individual basin-size distribution. The graph-cover relation alone and the general period-two theorem do not supply the numerical phase-preimage multiplicities \(1,10,226\). Exact historical equivalence remains a residual possibility.

## Limitations

The new claim is restricted to one canonical labelled finite graph and its entire \(2^{20}\)-state majority automaton; no universal basin formula for arbitrary cubic graphs is asserted. The cover-factorization construction is known. The explicit numerical basin distribution is established by exhaustive finite computation plus the elementary exact factorization shown above; it is not an infinite-family theorem. The search and source inspection do not rule out unpublished, unindexed or differently named earlier tabulations, and the result has not undergone independent validation.

## References

- E. M. Adam, M. A. Dahleh, A. Ozdaglar, *On Threshold Models over Finite Networks*, first arXiv submission 2012-11-04, arXiv:1211.0654; https://arxiv.org/abs/1211.0654. Relevant: Definition 4.14 and Lemma 6.10.
- I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, first arXiv submission 2014-05-11, arXiv:1405.2486; https://arxiv.org/abs/1405.2486.
- D. Kaaser, F. Mallmann-Trenn, E. Natale, *On the Voting Time of the Deterministic Majority Process*, first arXiv submission 2015-08-14, arXiv:1508.03519; https://arxiv.org/abs/1508.03519.
- E. W. Weisstein, *Desargues Graph*, MathWorld; https://mathworld.wolfram.com/DesarguesGraph.html.
