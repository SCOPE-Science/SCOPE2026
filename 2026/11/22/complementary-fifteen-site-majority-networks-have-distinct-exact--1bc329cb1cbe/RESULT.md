# Complementary fifteen-site majority networks have distinct exact attraction-basin spectra

## Finding
Let \(\mathcal E=\binom{\{1,2,3,4,5,6\}}{2}\), so \(|\mathcal E|=15\). The *triangular* graph \(T(6)=L(K_6)\) joins two different elements of \(\mathcal E\) when they intersect; its complement, the *Kneser* graph \(KG(6,2)\), joins them when they are disjoint. On each graph run synchronous binary open-neighbor strict majority with incumbent retention on a tie. For each initial configuration \(x\), let \(\tau(x)\) be the first nonnegative \(t\) such that \(F^{t+2}(x)=F^t(x)\), and let \(p(x)\in\{1,2\}\) be the eventual least period.

For **both** graphs, \(F^5=F^3\) on the entire \(2^{15}\)-state space and the sharp maximum entrance time is three. The *complete* first-entry/period populations are:

| graph | \((p,t)=(1,0)\) | \((1,1)\) | \((1,2)\) | \((1,3)\) | \((2,0)\) | \((2,1)\) |
|---|---:|---:|---:|---:|---:|---:|
| \(T(6)\) | 164 | 8544 | 15600 | 6660 | 1080 | 720 |
| \(KG(6,2)\) | 502 | 4426 | 13680 | 5040 | 5340 | 3780 |

All omitted pairs \((p,t)\) have population zero. In particular there are 164 fixed configurations and 540 distinct primitive two-orbits for \(T(6)\), versus 502 fixed configurations and 2670 primitive two-orbits for \(KG(6,2)\).

Define the basin of a temporal orbit \(O\) to be \(B(O)=\{x:\text{the forward orbit of }x\text{ eventually reaches }O\}\), including its periodic configurations. The complete **orbit-basin size spectrum** is:

| graph | least period | basin size | number of distinct attractor orbits |
|---|---:|---:|---:|
| \(T(6)\) | 1 | 1 | 120 |
| \(T(6)\) | 1 | 22 | 30 |
| \(T(6)\) | 1 | 236 | 12 |
| \(T(6)\) | 1 | 13678 | 2 |
| \(T(6)\) | 2 | 2 | 180 |
| \(T(6)\) | 2 | 4 | 360 |
| \(KG(6,2)\) | 1 | 1 | 360 |
| \(KG(6,2)\) | 1 | 10 | 140 |
| \(KG(6,2)\) | 1 | 10944 | 2 |
| \(KG(6,2)\) | 2 | 2 | 2460 |
| \(KG(6,2)\) | 2 | 20 | 210 |

Thus an unbiased uniformly random initial configuration reaches an oscillating attractor with respective probabilities \(1800/32768\) and \(9120/32768\), whose ratio is \(76/15\); the complementary graphs have equal sharp settling times but markedly unequal oscillatory basins. Both giant fixed basins belong to the two consensus configurations: sizes \(13678\) and \(10944\) on the respective graphs.

## Assumptions and scope
The vertices are all unordered two-element subsets of \(\{1,\ldots,6\}\), indexed lexicographically beginning with index zero for \(\{1,2\}\). Each state \(x\in\{0,1\}^{15}\) gives one opinion per graph vertex. For any graph vertex \(e\), write \(N(e)\) for its open neighborhood and \(d\) for the common degree (eight for \(T(6)\), six for \(KG(6,2)\)). The simultaneous update at \(e\) is one if \(2\sum_{f\in N(e)}x_f>d\), zero if the strict reverse inequality holds, and \(x_e\) in case of equality. There are no random updates or tie coin flips. All counts concern labelled configurations with the fixed vertex indexing. An attractor is an individual temporal orbit, not an orbit under spatial graph automorphisms.

## Proof
The claim is a **finite, exhaustive exact-arithmetic theorem**, not an extrapolation from samples. The supplied `verify_iterates.py` enumerates the full interval of binary integers from zero to \(2^{15}-1\), which bijects with all configurations through their fifteen binary digits. For each ordered pair \((e,f)\), it includes \(f\) in \(N(e)\) exactly when the two root edges meet, or exactly when they do not meet, according to the graph. It then computes every output bit with the displayed integer majority inequality, with ties retaining the input bit. No approximate arithmetic is used.

For each of the \(32768\) initial configurations the program calculates the six exact iterates \(F^0(x),\ldots,F^5(x)\) and checks \(F^5(x)=F^3(x)\). It obtains the least entrance time by testing \(F^{t+2}(x)=F^t(x)\) consecutively for \(t=0,1,2,3\); on entry, the least period is one if the next state is identical and two otherwise. It increments a frequency table for the pair \((p,t)\). Since \(F^5=F^3\), the two states at times three and four form the eventual orbit; their smaller integer identifier provides an unambiguous orbit key. Tallying all \(32768\) initial states against this key yields the orbit basins and their complete multiplicities. The script asserts every tabulated entry and confirms both total basin and first-entry mass equal \(32768\).

Independently, `verify_paths.cpp` reconstructs the graph using integer-pair adjacency (without the Python bitmask-neighborhood builder), computes the same update function through loops over neighbor lists, and traverses each functional-graph component until a previously seen state is reached. It identifies cycle lengths and orbit representatives, back-propagates entrance depths and basin identifiers along all predecessor paths, and asserts the two displayed frequency tables and the sharp entrance bound. This is a separate whole-space cycle-decomposition method, rather than a re-expression of the two-step iterate test.

For transparent witnesses of sharpness, under the stated lexicographic bit order, initial integer 695 on \(T(6)\) follows \(695\mapsto111\mapsto7\mapsto0\), while initial integer 63 on \(KG(6,2)\) follows \(63\mapsto28704\mapsto32\mapsto0\). Neither begins its eventual fixed orbit before time three. These explicit trajectories are also reproducible by the checker.

## Verification
Run `python3 verify_iterates.py`. With a C++17 compiler, run `c++ -O2 -std=c++17 verify_paths.cpp -o verify_paths` followed by `./verify_paths`. Both programs use only standard languages and standard libraries; the compiled executable is generated locally and is not needed as a supplied dependency. Their assertions were executed successfully on the exact supplied sources. The first checks \(65536\) initial graph-state pairs directly, and the second independently checks \(65536\) functional-graph states. The complete labelled state spaces are exhausted in each case; there is no statistical uncertainty or untested initial state.

## Relationship to prior work
The classical theorem of Goles and Olivos establishes eventual fixed or two-periodic behavior for finite symmetric threshold automata; it does not state the entrance depths or orbit-by-orbit basin sizes for these two complementary fifteen-vertex graphs. The general 2011 treatment of bi-threshold networks likewise addresses permitted periods and constructions, not these finite attraction spectra. A published classification of two-cycles in line-graph majority dynamics by incidence half-factors gives relevant structural coverage of recurrent configurations on the triangular graph; *the recurrent-state counts here are not claimed as an independent general advance*. The present claim instead includes every transient configuration and its eventual temporal orbit on both complementary graphs, with exact basin-size multiplicities. Related published majority-basin computations for the Shrikhande and rook graphs address a different graph pair and do not imply these tables. No covering identical basin census was found in the searches documented in the companion scientific review.

## Limitations
The theorem is specific to the two canonical fifteen-vertex graphs built from two-subsets of a six-element set; it does not assert a formula for arbitrary root size. Its proof is exhaustive finite arithmetic rather than a compact symbolic count or a general graph-family classification. A full historical-priority guarantee is not possible: a closely related line-graph recurrent-classification paper was available through indexed summaries but its primary full text was not obtainable in this review. The published summary concerns recurrent states rather than attraction-basin multiplicities, but unexpected supplementary material could affect novelty. No independent external mathematical audit has yet been performed.

## References
1. E. Goles and J. Olivos, *Comportement periodique des fonctions a seuil binaires et applications*, Discrete Applied Mathematics **3** (1981), 93–105, https://doi.org/10.1016/0166-218X(81)90034-2 (published April 1981; day not established).
2. C. J. Kuhlman, H. S. Mortveit, D. Murrugarra and V. S. A. Kumar, *Bifurcations in Boolean Networks*, first public preprint of 2011-08-15, https://arxiv.org/abs/1108.2974 (the dated archival starting source).
3. *Incidence conservation and half-factor classification of two-cycles in line-graph majority dynamics*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-incidence-conservation-and-half-factor-classification-of-two-cyc--61b3de3ad47a (index summary inspected; full text inaccessible).
4. *Spectral twins separate under majority dynamics: exact Shrikhande–rook attraction censuses*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-spectral-twins-separate-under-majority-dynamics-exact-shrikhande--a7ee2eb89698 (index summary inspected; different graphs).
