# A six-step relaxation clock and exact temporal census for four-state excitation on cocktail-party graphs

## Finding
For every integer \(m\ge4\), let \(G_m=K_{2m}-M_m\) be the graph with labelled vertices \(0,1,\ldots,2m-1\), in which every edge is present except the disjoint pairs \(\{2j,2j+1\}\), \(0\le j<m\). Apply the synchronous four-state Greenberg–Hastings update \(F_m\) with excitation threshold one. **Every state becomes periodic within six updates**, and this bound is sharp for every \(m\ge4\):
\[
F_m^{10}=F_m^6,\qquad \max_{x}\tau(x)=6.
\]
The unique fixed state is all resting. Every other recurrent state has primitive temporal period four; no other primitive period occurs.

Moreover, the complete time-resolved, eventual-period-resolved census has an **exact finite exponential generating formula independent of graph size**. Let
\[
T=\{(a,b):0\le a\le b\le3\},\quad
w_{ab}=\begin{cases}1,&a=b,\\2,&a<b,\end{cases}
\quad H_0(z)=1,\ H_1(z)=z,\ H_2(z)=e^z-1-z.
\]
Let \(\mathcal C_{t,p}\subseteq\{0,1,2\}^{T}\) be the explicitly defined, finite signature classes constructed below, where \(t\in\{0,\ldots,6\}\) is first periodic-entry time and \(p\in\{1,4\}\) is eventual least period. Then, **for every** \(m\ge4\), the number of initially labelled colorings with \((\tau,p)=(t,p)\) is exactly
\[
\boxed{N_{m,t,p}=m!\,[z^m]\sum_{\sigma\in\mathcal C_{t,p}}
\prod_{(a,b)\in T} H_{\sigma_{ab}}(w_{ab}z).}
\]
The ten pair-type alphabet, all \(3^{10}=59049\) signatures, and the two deterministic transition cases are specified in the proof and exhaustively verified in the accompanying standalone checker. The formula gives every population, not merely the sharp cutoff or initially recurrent states. In particular, for a uniformly random initial coloring the probability of immediate period-four recurrence is \(1-O(m(3/4)^{2m})\) as \(m\to\infty\).

## Assumptions and scope
Each site has local state \(0\) (rest), \(1\) (excited), \(2,3\) (two successive refractory states). The synchronous local rule maps \(1\to2\to3\to0\); a resting vertex maps \(0\to1\) exactly when at least one adjacent vertex is excited, otherwise it stays at zero. The graph is simple and loopless. A temporal period counts updates of the **full labelled configuration**, rather than repeated sets of locally occupied colors. For each initial state \(x\), \(\tau(x)\) is the least \(t\ge0\) at which \(F_m^t(x)\) is on a periodic orbit. No results are asserted here for fewer than four matched pairs, for other thresholds, or for asynchronous updates. Earlier classifications on three matched pairs or for three local states are treated as comparisons, not as new consequences.

## Proof
**1. A complete pair-type quotient.** Every vertex is adjacent to every vertex other than itself and its matched partner. For each initial configuration, classify each of the \(m\) matched pairs by its unordered pair of colors \((a,b)\in T\), with multiplicities \(n_{ab}\), and record the *capped* multiplicities \(\sigma_{ab}=\min(2,n_{ab})\). There are ten types and \(3^{10}=59049\) formal capped signatures. The update depends only on the present pair types and these capped multiplicities: the number of excited vertices can be distinguished as zero, one, or at least two from \(\sigma\). All pairs of a type evolve into one common next pair type, and the new capped multiplicities are computed by saturating the sums of incoming multiplicities at two.

Write \(R(c)=c+1\pmod4\) and \(h(0)=0,\ h(1)=2,\ h(2)=3,\ h(3)=0\). Let \(E\) be the (capped) total number of excited vertices. If \(E=0\), apply \(h\) to both entries of every pair. If \(E\ge2\), apply \(R\) to every entry. If \(E=1\), let \(u\) be the sole excited vertex. Every resting vertex other than the mate of \(u\) is excited, so the entire configuration rotates under \(R\), **except** when the mate of \(u\) is resting; in that case the unique type \((0,1)\) maps to \((0,2)\), instead of its regular rotated image \((1,2)\). These three cases define a deterministic, exact map \(\Phi\) on the 59049 signatures. In particular, no assumption that \(m\) is bounded is made in this reduction.

**2. Exact characterization of full recurrence.** A signature is *resting* if every occupied pair is of type \((0,0)\). A signature is *safe rotating* if all four colors occur and, for each color \(c\) that occurs on exactly one vertex, that vertex's mate does not have color \(c-1\pmod4\). These conditions depend only on the capped pair counts. A safe rotating microscopic state advances every coordinate by \(R\) at each step: whenever the excited class has size at least two every rest site sees excitation, and a singleton excited site fails to stimulate only its mate, which by safety is not resting. Since all four colors occur, such an orbit has primitive period four. A resting state is fixed. Both classes are forward invariant. Conversely, if a state is periodic and some forward iterate is resting or safe rotating, then the state is in the same cycle and is itself in that class.

**3. Finite exhaustive lemma, providing the uniform all-size bound.** The accompanying `verify_quotient.py` constructs \(\Phi\) from the preceding elementary three cases, independently constructs the resting and safe-rotating predicates, and evaluates every one of the \(59049\) formal signatures for all steps \(0\le t\le6\). It verifies exhaustively that each signature first enters one of those two recurrent classes by time six. This is an exhaustive finite lemma over the full size-independent quotient, **not** a computational sample of graph sizes. The precise class \(\mathcal C_{t,p}\) consists of signatures for which the first such entrance occurs at time \(t\), with \(p=1\) for resting or \(p=4\) for safe rotating. By the preceding paragraphs, its entrance time and period equal those of every microscopic state realizing that signature, including any multiplicities above the cap. This proves \(F_m^{10}=F_m^6\) and the period classification for all \(m\ge4\).

**4. Sharpness.** For any \(m\ge4\), take \(m-2\) pairs of type \((0,0)\), one pair \((0,3)\), and one pair \((1,2)\). Direct application of the displayed local rule gives first recurrence at step six (the state extinguishes at that step); the certificate also checks its capped signature. Thus the universal bound is attained for every permitted \(m\).

**5. Exact labelled enumeration.** Fix an ordered list of the \(m\) labelled matched pairs. For any type \((a,b)\), each pair has one realization if \(a=b\), and two orientations if \(a<b\). Therefore exactly \(w_{ab}\) microscopic choices realize that type on a given pair. For a signature coordinate \(\sigma_{ab}=0\), the number of corresponding pairs is exactly zero; for value one, exactly one; and for value two, at least two. Consequently their exponential generating factors are respectively \(H_0(w_{ab}z), H_1(w_{ab}z),H_2(w_{ab}z)\). Products enforce independent choices of all ten type multiplicities. The coefficient multiplied by \(m!\) distributes these pairs among the distinct labelled matching positions. Summation over the disjoint signature classes proves the boxed formula for every \((t,p)\) and all \(m\). The classes exhaust all signatures, so \(\sum_{t,p}N_{m,t,p}=4^{2m}\) holds identically.

**6. Typical immediate recurrence.** Any coloring in which every one of the four colors appears on at least two vertices is automatically safe rotating. A union bound under uniform independent initial colors gives \(\Pr(\text{some color occurs fewer than twice})\le4(3/4)^{2m}+4(2m)(1/4)(3/4)^{2m-1}=O(m(3/4)^{2m})\). This bounds the proportion not initially in primitive period-four recurrence. The all-resting state has probability \(4^{-2m}\) and is covered by the same error bound.

## Verification
The `verify_quotient.py` script checks **all 59049** capped signatures and computes weighted full-state populations by independent multinomial summation for \(m=2,3,4,5,6\). The separately written C++17 program `verify_direct.cpp` creates the complete functional graph directly from vertex adjacency and independently computes period and first-entry depth for **every one** of \(4^{2m}\) labelled states, also for \(m=2,3,4,5,6\). It does not use the capped quotient or any assumed period bound. Both programs were run; their exact output is in `quotient_output.txt` and `direct_output.txt`. The two methods agree for every displayed parameter. The small cases \(m=2,3\) are boundary comparisons only, not new claims.

| Matched pairs \(m\) | Primitive-four states | Four-cycle orbits | Sharp \(\tau\) | Last-layer states | Extinction basin | Four-cycle basin |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 23096 | 5774 | 6 | 448 | 25560 | 39976 |
| 5 | 586760 | 146690 | 6 | 2460 | 234896 | 813680 |
| 6 | 12001368 | 3000342 | 6 | 12144 | 2125360 | 14651856 |

Reproduce the finite lemma with `python3 verify_quotient.py`; reproduce direct enumeration with `g++ -std=c++17 -O2 verify_direct.cpp -o check && ./check`. The checker sources have no third-party library dependencies. Complete direct enumeration for \(m\le6\) corroborates the exact all-size quotient theorem; it is not used to extrapolate a finite-data pattern to infinite graph orders.

## Relationship to prior work
Greenberg and Hastings introduced the excitable-media rule; Durrett and Griffeath's first public 1993 preprint concerns excitable lattice automata [1]. Fisch and Gravner's 1995 article [2] develops general multicolor one-dimensional Greenberg–Hastings models, on lattice neighborhoods rather than dense matching-deleted complete graphs. Gravner, Lyu and Sivakoff [3] and Doba [4] study **three-color** excitation on finite arbitrary graphs and provide graph-wide circulation/activity criteria; those do not determine this four-state size-uniform time census.

The closest explicitly compared published graph-family results are the three-state cocktail-party period and basin classifications [5,6], and the four-state complete-tripartite relaxation and extinction classifications [7,8]. The latter apply to precisely **three** nonadjacency classes and consequently include \(G_3=K_{2,2,2}\), but **not** \(G_m\) for \(m\ge4\). The three-state cocktail-party results have the correct graph family but a different local state space and period-three dynamics. Neither stronger result is silently rebranded here: the claimed contribution is the four-state, \(m\ge4\) exact quotient and all-size first-entry/period census. A three-state complete-bipartite time-census [9] is another nearby but non-implying comparison.

## Limitations
The finite exhaustive quotient lemma is essential to the universal six-step identity; the separate direct-state program only corroborates bounded graph sizes. The formula is an explicit finite coefficient prescription, not a simplified elementary closed polynomial for each time class. Other thresholds, other local-state counts, general multipartite shore sizes and different update schedules are not covered. The full 1993 Durrett–Griffeath preprint could not be inspected from available full-text routes; its accessible record supports only chronology and model provenance, not a whole-document noncoverage assertion. Other unindexed historical sources could contain overlapping results, and no independent external mathematical audit has occurred.

## References
1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, first publicly posted 1993-03-22. https://arxiv.org/abs/patt-sol/9303002
2. R. Fisch and J. Gravner, *One-dimensional Deterministic Greenberg–Hastings Models*, *Complex Systems* 9 (1995), 329–348. https://content.wolfram.com/sites/13/2018/02/09-5-1.pdf
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320 (2016). https://arxiv.org/abs/1610.07320
4. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, *Complex Systems* 27 (2018), 101–126. https://doi.org/10.25088/ComplexSystems.27.2.101
5. *Three-state excitation on cocktail-party graphs: a sharp period transition and exact orbit count* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-three-state-excitation-on-cocktail-party-graphs-a-sharp-period-t--b65add71b337
6. *Exact extinction basins and recurrent populations for three-state excitation on cocktail-party graphs* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-extinction-basins-and-recurrent-populations-for-three-stat--1f53ca3d838e
7. *A sharp six-update cutoff and an exact four-cycle census for tripartite excitation* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-six-update-cutoff-and-an-exact-four-cycle-census-for-tri--6dbbcd0a300b
8. *Four-state excitation on tripartite graphs: identical four-cycle orbits, different transients, and exact extinction* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-four-state-excitation-on-tripartite-graphs-identical-four-cycle--6411c0882be0
9. *Exact temporal-basin polynomial for Greenberg–Hastings dynamics on complete bipartite graphs* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-temporal-basin-polynomial-for-greenberg-hastings-dynamics--41763c4e3744
