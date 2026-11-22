# Exact extinction-time polynomial for multi-state two-contact excitation on friendship graphs

## Finding
For every integer \(m\ge1\) and every integer \(k\ge3\), let \(W_m\) be the friendship graph consisting of \(m\) labelled triangles sharing exactly one hub. Its vertices are a hub \(h\) and distinct labelled pairs \((a_i,b_i)\), \(1\le i\le m\). The only edges are \(ha_i\), \(hb_i\), and \(a_ib_i\). Apply synchronous \(k\)-state Greenberg–Hastings dynamics with the absolute excitation threshold **two distinct excited neighbours**: positive states increment modulo \(k\); a resting vertex enters state one precisely when at least two neighbours are in state one.

For an initial colouring \(x\in\{0,1,\ldots,k-1\}^{2m+1}\), let \(\tau(x)\) be the first update at which every vertex is resting. Define the sharp last-layer population
\[
C_{k,m}=2k^{2m}-(k-1)^{2m}-2m(k-1)^{2m-1}-(k^2-2)^m.
\]
The **complete, labelled extinction-time census** is
\[
\begin{aligned}
N_0&=1,\\
N_j&=(j+1)^{2m+1}-j^{2m+1} &&(1\le j\le k-2),\\
N_{k-1}&=k^{2m+1}-(k-1)^{2m+1}-C_{k,m},\\
N_k&=C_{k,m},\\
N_j&=0 &&(j>k).
\end{aligned}
\]
Here \(N_j=|\{x:\tau(x)=j\}|\), and all exponents count distinct labelled vertices, without symmetry quotienting. In particular, **every** initial colouring vanishes by update \(k\), the bound is attained for every \(m,k\), and the all-rest state is the sole recurrent configuration.

For each fixed \(k\ge3\), a uniformly random initial colouring exhibits a two-layer limiting law:
\[
\lim_{m\to\infty}\Pr(\tau=k)=\frac{2}{k},\qquad
\lim_{m\to\infty}\Pr(\tau=k-1)=1-\frac{2}{k},\qquad
\lim_{m\to\infty}\Pr(\tau\le k-2)=0.
\]
The last convergence is exponential in \(m\). In the single-triangle case \(C_{k,1}=3\) for every \(k\ge3\). For \(k=3\), the final-layer count simplifies to \(2\cdot9^m-(m+1)4^m-7^m\).

## Assumptions and scope
The graph is finite, simple, undirected, and has exactly the displayed shared-hub structure. Every update is simultaneous. State zero is resting; state one is excited; states two through \(k-1\) are successive refractory states. A vertex in a positive state increments by one, with state \(k-1\) returning to zero. A zero becomes one only on receiving two **distinct** simultaneous contacts from neighbours in state one. No spontaneous excitation, self-contact, stochastic recovery, or external input is allowed. The colouring at time zero is arbitrary. The claim covers every integer \(m\ge1\) and \(k\ge3\); no statement is made for modified graph classes or different excitation thresholds.

## Proof
**One-generation propagation lemma.** At the first update, a non-hub vertex can be newly excited only if its own initial state is zero and **both** its neighbours, the hub and its partner, were initially in state one. Thus newly excited non-hub vertices require an initially excited hub. Conversely the hub can be newly excited only if it was initially zero and at least two peripheral vertices were excited. These conditions are disjoint. Moreover, if the initial hub was zero, *no* peripheral vertex is excited at time one: old ones have advanced to two, while resting peripherals cannot have two excited neighbours without an excited hub. If a peripheral vertex is excited at time one, the initial hub must have been one, so the hub is refractory (state two) at time one.

**No excitation beyond update one.** There are two exhaustive possibilities. If the hub is excited at time one, no peripheral is excited at time one, so no resting peripheral can satisfy the two-contact condition at the next update. If some peripheral is excited at time one, the hub is in state two, hence not resting and unable to become newly excited at time two. Its peripheral partners may be excited at time one only in the separate petals, but no resting peripheral can meet threshold two because its excited hub-neighbour is absent. If neither is excited at time one, of course no activation can occur at time two. Hence **no new zero-to-one transitions occur at update two**. Every state-one vertex at time one advances to two at update two; any state one initially also advanced at update one. Thus no vertex is excited at time two, and no zero-to-one transition can occur later. All remaining positive states simply progress through the refractory chain to zero. A vertex newly excited at time one is resting for the first time at time \(k\). An initially positive vertex in state \(r\) becomes resting at time \(k-r\).

**Characterisation of the last layer.** The preceding lemma proves that \(\tau=k\) precisely when some zero-to-one transition occurs at update one. This happens in exactly one of two disjoint ways:

1. The hub begins in state zero and at least two of the \(2m\) peripherals begin in state one. There are \(k^{2m}-(k-1)^{2m}-2m(k-1)^{2m-1}\) choices.
2. The hub begins in state one and at least one of the \(m\) ordered peripheral pairs equals \((0,1)\) or \((1,0)\). There are \(k^{2m}-(k^2-2)^m\) choices.

Their sum is \(C_{k,m}\). Both events are realized already when \(m=1\), proving strict positivity and the sharp maximum \(k\).

**All earlier layers.** If no zero-to-one transition occurs at time one, no future zero-to-one transition can occur. For an initial colouring containing a positive entry, the extinction time is then \(k-r_{\min}\), where \(r_{\min}\) is its smallest positive entry. If all entries are zero then \(\tau=0\), providing one colouring. For \(1\le j\le k-2\), the constraint \(r_{\min}=k-j\ge2\) precludes initial excitations and hence precludes newly excited vertices at time one. There are exactly \((j+1)^{2m+1}-j^{2m+1}\) such colourings, by subtracting the alphabets \(\{0,k-j+1,\ldots,k-1\}\) from \(\{0,k-j,\ldots,k-1\}\). The remaining non-last-layer colourings with an initial one are \(k^{2m+1}-C_{k,m}-(k-1)^{2m+1}\), all extinguishing at time \(k-1\). These disjoint cases sum to \(k^{2m+1}\), proving completeness.

**Limit law.** Divide by the total \(k^{2m+1}\). Since \((k-1)/k<1\) and \((k^2-2)/k^2<1\), the last-layer proportion tends to \(2/k\). The fraction extinct by time \(k-2\) is exactly \((k-1)^{2m+1}/k^{2m+1}\), which decays exponentially. The claimed complementary limit follows. Finally \(C_{k,1}=3\) by direct algebra.

## Verification
The standalone, standard-library-only `verify_extinction.py` independently constructs the labelled friendship graph updates and enumerates **every** initial state for fourteen \((k,m)\)-pairs: \(k=3\), \(1\le m\le5\); \(k=4\), \(1\le m\le4\); \(k=5\), \(1\le m\le3\); and \(k=6\), \(1\le m\le2\). It compares exact microscopic first-hitting histograms with every coefficient in the theorem, verifies sharpness, and reports `VERIFY_OK`. The actual stdout is supplied as `verify_output.txt`. Run `python3 verify_extinction.py`; no input files or third-party libraries are required. These finite tests corroborate the proof; the exhaustive **infinite parameter** statement rests on the preceding propagation lemma and counting argument, not on experiments.

## Relationship to prior work
Greenberg and Hastings (1978) introduced the excitable update framework; Durrett and Griffeath (1993, public preprint 1993-03-22) studied multi-colour, threshold-dependent excitable cellular automata chiefly in lattice settings. Fretter and coauthors (2014) analyze how topological motifs and thresholding affect excitation transmission, but use a degree-dependent threshold and primarily single-seed experiments. The published published-finding corpus friendship-graph classifications `13eed7214670` and `e79c2691fb75` analyze **threshold one**, not the two-contact rule here; their asymptotic regimes exhibit recurrent three-cycles instead of universal extinction. The published densest-induced-subgraph criterion `352367f51e91` *already implies eventual extinction* at threshold two for friendship graphs in the three-state case; its event-matching proof also extends directly to longer refractory chains. Thus eventual extinction for any \(k\ge3\) is **not** claimed as new. That theorem does not imply the sharp \(k\)-step clock, the all-\(k\) extinction-time polynomial, or the \(2/k\) limiting layer, and its explicit general budget is not equal to this clock. The published wheel theorem `58917bc0decb` proves a sharp five-update bound on a different family under the three-state two-contact rule, without deriving this friendship-graph census. The claimed addition is precisely the new full all-state/all-colour time distribution and structural depth-one trigger criterion.

## Limitations
The formula depends on absolute threshold two, homogeneous excitation rules, synchronous updates, and triangles meeting in exactly one vertex. It does not imply the same extinction law on general graphs with triangles, on square books, or for threshold one. The finite checker does not prove the universal quantifiers. Although searched comparisons did not identify an equivalent distribution, additional unindexed or inaccessible historical studies could affect priority. No independent external mathematical audit is asserted.

## References
1. J. M. Greenberg and S. P. Hastings, *Spatial Patterns for Discrete Models of Diffusion in Excitable Media*, SIAM Journal on Applied Mathematics **34** (1978), 515–523, https://doi.org/10.1137/0134040.
2. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, public preprint dated 1993-03-22, arXiv:patt-sol/9303002, https://arxiv.org/abs/patt-sol/9303002.
3. C. Fretter, A. Lesne, C. C. Hilgetag and M.-Th. Hütt, *Topological Determinants of Self-Sustained Activity in a Simple Model of Excitable Dynamics on Graphs*, public preprint dated 2014-03-24, arXiv:1403.6174, https://arxiv.org/abs/1403.6174.
4. published-finding corpus, *Exact entrance-time census for three-state excitation on friendship graphs* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-entrance-time-census-for-three-state-excitation-on-friends--13eed7214670.
5. published-finding corpus, *Shared three-cycle skeleton and unequal stopping-time laws for excitation on friendship graphs* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-shared-three-cycle-skeleton-and-unequal-stopping-time-laws-for-e--e79c2691fb75.
6. published-finding corpus, *A densest-subgraph threshold and finite excitation budget for three-state graph dynamics* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-densest-subgraph-threshold-and-finite-excitation-budget-for-th--352367f51e91.
7. published-finding corpus, *Sharp five-step extinction for threshold-two excitation on wheel graphs* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-five-step-extinction-for-threshold-two-excitation-on-wheel--58917bc0decb.
