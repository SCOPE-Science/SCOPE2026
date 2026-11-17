# Exact excitation-clock reconstruction and period divisibility for three-color graph automata

## Finding

Let \(G=(V,E)\) be any finite simple undirected graph, possibly disconnected, and start the synchronous three-color cyclic cellular automaton (CCA) and the three-state Greenberg–Hastings model (GHM) from exactly the same coloring \(c:V\to\{0,1,2\}\). Write \(C_v(t)\) for the number of CCA color advances at vertex \(v\) during updates \(0,\ldots,t-1\), and \(H_v(t)\) for the number of GHM **rest-to-excited** transitions \(0\to1\) at that vertex over the same time interval. Define \(h(0)=0\), \(h(1)=-2\), and \(h(2)=-1\). Then, for every vertex and every integer \(t\ge0\),

\[
\boxed{H_v(t)=\left\lceil\frac{C_v(t)+h(c(v))}{3}\right\rceil.}
\]

In particular the GHM excitation events are recoverable from the CCA advance counts at that vertex alone. For every vertex, the eventual least temporal period of its GHM color sequence divides the eventual least temporal period of its CCA color sequence. Consequently, the eventual least period \(P_H\) of the entire GHM configuration divides the eventual least period \(P_C\) of the entire CCA configuration:

\[\boxed{P_H\mid P_C.}\]

This is a statement about matched initial colorings, not about arbitrary states drawn separately from the two automata.

## Assumptions and scope

At each synchronous update, CCA advances \(i\) to \(i+1\pmod3\) exactly when a neighbor currently has the successor color, and otherwise remains at \(i\). GHM always performs \(1\to2\to0\); it performs \(0\to1\) exactly when a neighbor is in state \(1\), and otherwise leaves \(0\) at rest. There are no self-loops, stochastic updates, or threshold-two contacts. The graph has finitely many vertices, so both trajectories become eventually periodic. An isolated vertex and each connected component are included without exceptional conventions.

For any vertex \(v\), its *eventual least local period* is the least positive integer \(p\) for which the color at that vertex at time \(t+p\) equals its color at \(t\) for every sufficiently large integer \(t\). The global period is the least common multiple of these local periods.

## Proof

**Known maximum-walk representation.** Gravner, Lyu and Sivakoff (2016, Lemma 1, with its tournament-expansion proof in Section 3) establish the following exact identity separately for three-color CCA and GHM. Given the corresponding antisymmetric initial edge weight \(d_C\) or \(d_H\), the number of its designated excitations at \(v\) up to time \(t\) equals the maximum sum of initial edge weights over all walks starting at \(v\) and of length at most \(t\), including the empty walk. For CCA, \(d_C(u,w)\) is the representative of \(c(w)-c(u)\pmod3\) in \(\{-1,0,1\}\). For GHM, \(d_H(u,w)=1\) when \((c(u),c(w))=(0,1)\), \(-1\) when that pair is \((1,0)\), and zero otherwise. These are distinct weights: applying the CCA weight to GHM would be incorrect.

**Three-to-one cohomology identity.** Checking the three unordered pairs of distinct colors (and their reversals) gives, on *each* oriented edge,

\[d_C(u,w)=3d_H(u,w)+h(c(w))-h(c(u)).\]

Consequently, every walk \(W\) from \(v\) to an endpoint \(z\) satisfies

\[\int_W d_C=3\int_W d_H+h(c(z))-h(c(v)).\]

Put \(M=\max_{|W|\le t}\int_W d_H=H_v(t)\). The integer value of any nonmaximizing GHM walk is at most \(M-1\). Since \(-2\le h\le0\), its CCA walk integral is at most \(3M-3-h(c(v))\). On the other hand, a GHM-maximizing walk exists, and its CCA integral is at least \(3M-2-h(c(v))\). Thus **no nonmaximizing GHM walk can maximize CCA**. The maximum CCA integral belongs to \(\{3M-2-h(c(v)),3M-1-h(c(v)),3M-h(c(v))\}\). The maximum-walk representation therefore yields

\[3H_v(t)-2\le C_v(t)+h(c(v))\le3H_v(t),\]

which is exactly the ceiling formula. This proof also covers \(t=0\), since the empty walk has zero weight and the ceiling of \(h(c(v))/3\) is zero.

**Period transfer.** Let \(p\) be the eventual least local period of the CCA color sequence at \(v\). For sufficiently late \(t\), the sequence of its zero-or-one advance events is \(p\)-periodic. Let \(k\) count its advances in one such block. Returning to the same color implies \(k\equiv0\pmod3\). Hence for late \(t\), \(C_v(t+p)=C_v(t)+k\), and the ceiling identity gives

\[H_v(t+p)=H_v(t)+k/3.\]

Therefore the zero-or-one GHM rest-to-excited event sequence \(H_v(t+1)-H_v(t)\) is eventually \(p\)-periodic. For every sufficiently large \(t\), the GHM color at time \(t\) is \(1\) when the event at update \(t-1\) occurred, \(2\) when the event at update \(t-2\) occurred, and \(0\) otherwise. The two events cannot both occur, because states \(1,2\) are refractory. Thus the eventual GHM color sequence at \(v\) has period \(p\); its least local period divides \(p\). Taking least common multiples across all vertices proves \(P_H\mid P_C\). The empty-graph and disconnected cases follow componentwise.

## Verification

The included standard-library Python checker independently builds CCA and GHM update trajectories, counts their designated events, checks the rounding formula at every time \(0\le t\le10\), and computes both maximum-walk functionals directly for \(0\le t\le5\). It exhausts all \(75\) labelled graphs of orders \(1\) to \(4\) and all \(5421\) graph/coloring pairs: \(235653\) vertex/time clock comparisons passed. This checks the nonstandard maximum-walk bridge independently of the cited implementation.

A separate C++17 checker constructs both functional graphs and resolves eventual periods by explicit cycle detection. It checks **every** labelled simple graph of order at most \(6\), including disconnected graphs, and every initial three-coloring: \(33867\) graphs and \(24142125\) graph/coloring pairs. All period-divisibility comparisons passed. These finite tests validate the implementations and edge cases; the preceding all-order proof, not sampling, establishes the theorem.

Reproduce with `python3 verify_clock_quotient.py` and `c++ -O3 -std=c++17 verify_period_divisibility.cpp -o verify_period_divisibility && ./verify_period_divisibility`. Recorded outputs are in the two corresponding `.out` files.

## Relationship to prior work

The exact maximum-walk identity and tournament expansion are **prior results**, proved by Gravner, Lyu and Sivakoff (arXiv:1610.07320, first submitted 2016-10-24; later published in 2018). The present derivation does not rebrand that identity, their synchronization criterion, or their limiting cycle-mean formula as new. The additional observation is a pointwise, integer-rounded comparison of two *different* weight functions, followed by a local-period transfer for matched initial colorings. The cited work analyzes each automaton's excitation and asymptotic activity, but does not state the cross-model rounding reconstruction or local-period-divisibility consequence.

Doba (2018) analyzes GHM evolution and maximum cycle densities on finite graphs; its results concern one automaton and do not supply a comparison of matched CCA and GHM trajectories. Previously recorded exact matched-initial-coloring classifications for particular graphs and complete bipartite families are compatible examples but do not imply an all-graph statement.

## Limitations

The result applies to the specified three-state, threshold-one synchronous rules, not to other alphabet sizes, nonstandard contact thresholds, asynchronous dynamics or directed graphs. It does not assert equality of periods; strict divisibility occurs on known finite graphs. The relationship is an event-history reconstruction, **not** a memoryless conjugacy of the two state-update maps. The proof depends materially on a published maximum-walk lemma, and an exhaustive bibliographic claim of first priority is not made. No independent external mathematical audit has been performed.

## References

1. J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, initial public submission 2016-10-24; *Annals of Applied Probability* **28** (2018), 3324–3357. In particular, the definitions and Lemma 1 (maximum-walk representation), and its proof in Section 3. https://arxiv.org/abs/1610.07320
2. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, *Complex Systems* **27** (2018), 101–126, DOI:10.25088/ComplexSystems.27.2.101. https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf
3. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002 (1993). Background for the two models; no period-transfer theorem attributed to it.
