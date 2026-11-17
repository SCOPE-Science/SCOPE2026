# Three-step collapse and the exact oscillation basin of threshold-two cyclic dynamics on friendship graphs

## Finding

For every integer \(k\ge1\), take the friendship graph \(F_k=K_1\vee(kK_2)\), the union of \(k\) triangles meeting at one hub. Apply the synchronous three-colour cyclic automaton with contact threshold two: a vertex currently coloured \(c\in\mathbb Z/3\mathbb Z\) changes to \(c+1\pmod3\) exactly when **at least two** distinct neighbours already have that successor colour. Write \(T\) for the global map. Then
\[
T^6=T^3,
\]
so every configuration first becomes periodic within three updates, and the only possible least periods are \(1\) and \(3\). The sharp maximum first-periodic-entry time is \(1\) for \(k=1\) and \(3\) for every \(k\ge2\). Primitive three-cycles exist exactly for \(k\ge3\).

Define \(B_1=9\), and for \(k\ge2\),
\[
B_k=3\cdot6^k+2k6^{k-1}+2k4^{k-1}-(3+2k)3^k-2k.
\]
Among the \(3^{2k+1}=3\cdot9^k\) labelled configurations, precisely \(3B_k\) eventually reach a fixed point and precisely \(3(9^k-B_k)\) reach a primitive three-cycle. The counts of configurations already periodic at time zero are
\[
N_{\mathrm{fixed}}=3(1+2k)2^k,\qquad
N_{\mathrm{period\ 3}}=3(3^k-3\cdot2^k+3).
\]
For independent uniform initial colours,
\[
\Pr(\text{eventually fixed})=\frac{B_k}{9^k}
=\left(3+\frac{k}{3}\right)\left(\frac23\right)^k
+O\!\left(k\left(\frac49\right)^k\right).
\]
In particular the oscillation basin has probability tending to one, though the initially periodic three-cycle population has exponentially vanishing relative density.

## Assumptions and scope

The graph is simple and undirected; a petal is an edge joining two degree-two vertices, and the hub is adjacent to both endpoints of every petal. The colour set is \(\{0,1,2\}\), with **successor** interpreted modulo three. The update is simultaneous, deterministic and uses open-neighbourhood counts; no self-neighbour and no random tie rule is present. The integer \(k\) is arbitrary but positive, and the counts concern all labelled initial configurations, not merely pair-unlabelled multisets.

For counting, use cyclic colour symmetry to set the initial hub colour to zero. Record the six unordered petal types as \(00,01,02,11,12,22\), with multiplicities \(A,B,C,D,E,F\), respectively. A mixed petal has exactly two ordered realisations and a constant-colour petal has one. Accordingly, for fixed hub the weight of a count vector is
\[
\frac{k!}{A!B!C!D!E!F!}\,2^{B+C+E}.
\]

## Proof

**Petal freezing lemma.** If the hub currently has colour \(h\), the only petal type able to change is \(\{h-1,h\}\) (colours modulo three). Its predecessor-coloured vertex advances to \(h\), making the petal monochromatic. All other petal types remain unchanged, and a monochromatic petal never changes. If the hub does not advance at a step, its successor-coloured neighbour count cannot increase: only \(\{h-1,h\}\) petals can move, and they contain no successor-coloured vertex. Therefore the hub cannot begin advancing again after it first stalls; all motion then stops after at most one further update.

**Four tests for persistent rotation.** Initially take hub colour zero. At the first update, all \(02\) petals become \(00\), and the hub advances to one iff
\[
B+2D+E\ge2.\tag{1}
\]
Conditional on advancing, the second update makes each \(01\) petal become \(11\), and the hub advances to two iff
\[
E+2F\ge2.\tag{2}
\]
Conditional on advancing again, the third update converts every \(12\) petal to \(22\), and the hub advances back to zero iff
\[
A+C\ge1.\tag{3}
\]
At this point all petals are monochromatic, with counts \(A+C\), \(B+D\), \(E+F\) of the three colours. The hub continues advancing iff
\[
B+D\ge1.\tag{4}
\]
The earlier second test guarantees \(E+F\ge1\), and the third test guarantees \(A+C\ge1\). Thus (1)--(4) are necessary and sufficient for eventual primitive period three. When any test fails, the freezing lemma proves eventual fixation. Every state is therefore on a periodic orbit by time three, establishing \(T^6=T^3\).

For \(k=1\) the hub can advance at most once, so its entry time is at most one; a hub of colour zero with its one petal \(02\) first becomes fixed after one step. For any \(k\ge2\), take hub colour zero, two petals of type \(12\), and all remaining petals of type \(22\). The hub advances twice, then stalls at colour two while the two mixed petals become \(22\). This configuration first becomes fixed at time three, showing sharpness. Conditions (3), (4), and (2) require at least one petal in each of the disjoint groups \(\{00,02\}\), \(\{01,11\}\), and \(\{12,22\}\); hence primitive period three requires \(k\ge3\). Conversely one monochromatic petal of each colour gives a period-three orbit for every \(k\ge3\), adding arbitrary further monochromatic petals.

**Exact basin enumeration.** Let \(\mathcal E_i\) denote failure of test (i), for \(i=1,2,3,4\). In terms of the initial type counts these events are
\[
\begin{aligned}
\mathcal E_1&:\ D=0,\ B+E\le1,\\
\mathcal E_2&:\ F=0,\ E\le1,\\
\mathcal E_3&:\ A=C=0,\\
\mathcal E_4&:\ B=D=0.
\end{aligned}
\]
Each petal type contributes exponential weight \(wz\), where weights for \(00,01,02,11,12,22\) are respectively \(1,2,2,1,2,1\). Inclusion--exclusion over the four failure events gives the following exponential generating function for initial colourings with fixed hub zero that **fail at least one test**:
\[
\begin{aligned}
U(z)&=\sum_{k\ge0}B_k\frac{z^k}{k!}\\
&=1+4z-2ze^z-(3+6z)e^{3z}+2ze^{4z}+(3+2z)e^{6z}.
\end{aligned}
\]
For clarity, one of the four event exponential generating functions is \(e^{4z}(1+4z)\) for \(\mathcal E_1\): the three unrestricted types have total weight four and at most one of the two weight-two types occurs. The other three are \(e^{6z}(1+2z)\), \(e^{6z}\), and \(e^{6z}\), respectively. Their intersections are evaluated by imposing the indicated zero/at-most-one restrictions simultaneously. For instance \(\mathcal E_1\cap\mathcal E_2\) has exponential generating function \(e^{3z}(1+4z)\). The fifteen nonempty inclusion--exclusion terms simplify to the displayed \(U\); the full finite arithmetic may also be checked from the six-type enumeration code.

Taking coefficients yields \(B_1=9\) and the displayed formula for every \(k\ge2\), while the complementary \(9^k-B_k\) weighted choices are the three-cycle basin for each of three possible initial hub colours. Their ratio proves the asserted asymptotic formula, since the \(6^k\) and \(k6^{k-1}\) terms dominate the others.

**Periodic populations.** A fixed state with hub colour zero has no \(02\) petal and fewer than two petals' worth of colour-one neighbours. Thus it has arbitrary \(00\) and \(22\) petals and at most one \(01\) or \(12\) petal. There are \(2^k+4k2^{k-1}=(1+2k)2^k\) such labelled states. In a primitive three-cycle every petal must already be monochromatic (a mixed one is irreversibly frozen when the hub attains the corresponding colour), and the three monochromatic petal colours must all be represented. There are \(3^k-3\cdot2^k+3\) such petal assignments for each initial hub colour. These complete the two time-zero counts.

## Verification

`code/verify_labelled.py` independently enumerates every labelled colouring for \(1\le k\le5\), computes the graph dynamics from adjacency and checks both \(T^6=T^3\) and the four-test basin criterion. The program examines \(199287\) labelled states in total and matches all five values of the closed basin formula. `code/verify_symbolic.py` uses capped multiplicities \(0,1,\ge2\) and tags all six original petal types, checking the universal identity on \(3\cdot3^6=2187\) finite symbolic classes; it also compares independent weighted-count enumeration with the formula through \(k=27\). Exact output is embedded in `evidence/verify_labelled.out` and `evidence/verify_symbolic.out`. All integer computations are exact. The finite checks are corroboration; the proof above is valid for every \(k\) without extrapolation.

## Relationship to prior work

The threshold/contact cyclic rule and its excitable-media motivation were developed in Fisch--Gravner--Griffeath (1991) and Durrett--Griffeath (1993), principally for spatial lattice configurations and large-range periodic wave structures. Gravner--Lyu--Sivakoff (2016) treats the **one-neighbour threshold**, with a general finite-graph criterion based on cycle increments; that criterion does not determine this threshold-two dynamics or its basins. Bello--Sivakoff (2021) studies contact thresholds at least two on **infinite regular trees**, not finite shared-triangle bouquets. The explicit petal-freezing mechanism, universal three-update cutoff, exact labelled basin law, and polynomially corrected exponential fixation tail on the friendship graph are not consequences of the statements inspected there. Related finite bipartite threshold-two automata and other graph dynamics do not imply the shared-hub pair reduction. These comparisons are conditional on the literature actually inspected, not an assertion of exhaustive historical priority.

## Limitations

The claim is restricted to three colours, contact threshold exactly two, synchronous updates, and friendship graphs with degree-two outer vertices. It does not determine the time-three entrance distribution within each period class, and it makes no claim about more colours, higher thresholds, other triangle cacti, or asynchronous rules. An independent external audit has not been performed. Other formulations or lesser-indexed prior results could overlap despite the targeted literature comparisons.

## References

1. R. Fisch, J. Gravner, D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing **1** (1991), 23--39. DOI: 10.1007/BF01890834. Open copy: https://www.stat.cmu.edu/~cshalizi/462/2008/readings/fgg.pdf
2. R. Durrett, D. Griffeath, *Asymptotic behavior of excitable cellular automata*, Experimental Mathematics **2** (1993), 183--208. Public preprint posted 1993-03-22: https://arxiv.org/abs/patt-sol/9303002 ; author-hosted text: https://sites.math.duke.edu/~rtd/reprints/paper79.pdf
3. J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (posted 2016-10-24), https://arxiv.org/abs/1610.07320
4. J. Bello, D. Sivakoff, *Cyclic cellular automata and Greenberg--Hastings models on regular trees*, arXiv:2108.06404v1 (posted 2021-08-13), https://arxiv.org/abs/2108.06404
