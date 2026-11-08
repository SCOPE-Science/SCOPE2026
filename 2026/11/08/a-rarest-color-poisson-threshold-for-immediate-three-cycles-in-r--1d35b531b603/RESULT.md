# A rarest-color Poisson threshold for immediate three-cycles in random excitable networks

## Finding

Consider the three-state Greenberg–Hastings automaton on a random labelled graph \(G(n,p)\), with independent initial vertex states having probabilities \(\pi_0,\pi_1,\pi_2>0\), whose sum is one. A resting vertex in state \(0\) enters state \(1\) when a neighbor is in state \(1\); otherwise it stays at \(0\). States \(1\) and \(2\) always advance to \(2\) and \(0\), respectively. The graph and initial states are independent.

Let \(B_n\) count the vertices whose initial state has **no neighbor in the next cyclic state** (state \(i+1\pmod 3\)). Let \(N_i\) be the number of initially \(i\)-colored vertices, indices taken modulo three. For all integers \(n\ge1\) and \(0\le p\le1\),

\[
B_n\mid(N_0,N_1,N_2)\ \overset{d}{=}\ \sum_{i=0}^2 \operatorname{Bin}\bigl(N_i,(1-p)^{N_{i+1}}\bigr),
\]

where the three binomial random variables on the right are **independent**. Consequently the probability that all vertices already execute a primitive three-cycle is exactly

\[
\sum_{a+b+c=n}\frac{n!}{a!b!c!}\pi_0^a\pi_1^b\pi_2^c
\prod_{i=0}^2\bigl[1-(1-p)^{N_{i+1}}\bigr]^{N_i},
\qquad (N_0,N_1,N_2)=(a,b,c).
\]

At the boundary \(p=1\), interpret \(0^0\) by the empty-product convention. All three-color distributions have positive masses, but the finite formula includes color count zero.

Write \(m=\min_i\pi_i\), \(w=\sum_{i:\pi_{i+1}=m}\pi_i\), and for any fixed real \(t\) set

\[
p_n(t)=\frac{\log n+t}{mn}
\]

for sufficiently large \(n\), when this lies in \([0,1]\). Then

\[
B_n\ \xrightarrow[\mathrm{TV}]{d}\ \operatorname{Poisson}(w e^{-t}),
\qquad
\Pr(B_n=0)\longrightarrow\exp(-w e^{-t}).
\]

Moreover \(G(n,p_n(t))\) is connected with probability tending to one. Therefore the same limit is the joint probability that the *entire initial Greenberg–Hastings configuration* has least temporal period three, with no transient. For every fixed positive color distribution, the event \(B_n=0\) has a sharp threshold at \(p\sim(\log n)/(mn)\): it tends to zero below the window and to one above it, in the usual monotone-coupling sense.

For uniform initial states, \(m=1/3\), \(w=1\), and the critical probability is \(p_n(t)=3(\log n+t)/n\), with limit \(\exp(-e^{-t})\). For \((\pi_0,\pi_1,\pi_2)=(1/2,1/3,1/6)\), one has \(m=1/6\), \(w=1/3\): the critical probability is \(6(\log n+t)/n\), with limit \(\exp(-e^{-t}/3)\).

## Assumptions and scope

All graphs are finite, simple, undirected and loopless. \(G(n,p)\) means independent edges among the \(\binom n2\) labelled unordered vertex pairs. The initial states are independent and identically distributed with a *fixed* positive three-state distribution, independent of the graph. The main probability statements are **annealed**: probabilities are joint over the graph and its initial state. They do not assert concentration of the fraction of periodic configurations on an individually sampled graph (a quenched result).

The three-cycle event in the theorem is the event that **every vertex rotates one step at every update**; on any connected graph it is equivalent to the entire configuration having primitive temporal period three. For disconnected graphs, a three-periodic configuration may contain components that remain at rest, so the two events are not asserted equal there. At the critical window the random graph is connected with probability tending to one, making the distinction asymptotically immaterial.

## Proof

**1. Characterize the dynamics.** On any fixed finite connected graph, a trajectory whose state after three updates equals its initial state has, at each vertex, either the constant three-symbol word \(000\), or a cyclic rotation of \(012\). Indeed, states \(1\) and \(2\) necessarily advance, and returning within three updates excludes a delay in state \(0\) for an active vertex. If a vertex remains at \(0\) for the whole cycle while an adjacent vertex rotates, the latter is excited at one of the three times and must excite the former, a contradiction. Connectedness forces either all vertices to stay at \(0\), or all vertices to rotate. In the latter case a vertex of initial state \(i\) must see a neighbor of initial state \(i+1\pmod3\); the condition at all vertices is also sufficient, since all states then rotate synchronously under each subsequent update. Such a trajectory has least period three.

**2. Exact conditional law.** Hold the initial coloring fixed. For a vertex \(v\) of color \(i\), the event that \(v\) has no successor-colored neighbor depends on the \(N_{i+1}\) edges from \(v\) to vertices of color \(i+1\). Each candidate edge belongs to the test of *at most one* source vertex: an edge joining colors \(i\) and \(i+1\) supports the color-\(i\) endpoint, but not the color-\(i+1\) endpoint (which seeks color \(i+2\)). These sets of Bernoulli edges are disjoint for distinct source vertices. Their deficiency events are therefore mutually independent, with probabilities \((1-p)^{N_{i+1}}\). Grouping the sources by color proves the binomial sum. The multinomial distribution of \((N_0,N_1,N_2)\) gives the finite probability formula by conditioning on the count vector and setting \(B_n=0\). In particular, the exact probability generating function is

\[
\mathbb E[z^{B_n}]=\sum_{a+b+c=n}\frac{n!}{a!b!c!}\prod_{i=0}^2\pi_i^{N_i}
\prod_{i=0}^2\left[1+(z-1)(1-p)^{N_{i+1}}\right]^{N_i}.
\]

**3. Critical limit.** Since the color distribution is fixed and positive, with probability tending to one the three class sizes satisfy \(\lvert N_i-n\pi_i\rvert\le n^{2/3}\). On this event, uniformly in the class sizes, for each \(i\)

\[
(1-p_n(t))^{N_{i+1}}
=n^{-\pi_{i+1}/m}\,e^{-t\pi_{i+1}/m}(1+o(1)).
\]

Here \(p_n(t)=O((\log n)/n)\), so \(N_i p_n(t)^2=o(1)\), and the fluctuation of \(N_i\) in the exponent is at most \(O((\log n)n^{-1/3})\). Thus the total mean of the independent deficiency indicators tends uniformly to \(we^{-t}\): terms with \(\pi_{i+1}>m\) vanish, whereas terms with \(\pi_{i+1}=m\) contribute \(\pi_i e^{-t}\). The largest individual deficiency probability is \(O(1/n)\), and the sum of their squares tends to zero. The elementary Poisson approximation inequality for independent Bernoulli indicators bounds the total-variation distance to a Poisson law with matching mean by the sum of squares of probabilities. This bound and continuity in the Poisson mean imply total-variation convergence conditional on the typical color-count event. Averaging over color counts proves the unconditional convergence and the zero-deficiency limit.

**4. Connectivity and threshold.** Since \(m\le1/3\), at fixed \(t\) the edge probability satisfies \(p_n(t)\ge(3-o(1))\log n/n\). A union bound on a disconnected component of size at most \(n/2\) gives

\[
\Pr(G(n,p_n(t))\text{ disconnected})
\le\sum_{k=1}^{\lfloor n/2\rfloor}\binom nk(1-p_n(t))^{k(n-k)}=o(1).
\]

Indeed, the \(k\)-th term is at most \((en/k)^k\exp[-p_n(t)k(n-k)]\), which is summable over \(1\le k\le n/2\) using \(p_n(t)(n-k)\ge(3/2-o(1))\log n\). Step 1 now identifies the zero-deficiency event with immediate primitive period three, except on a graph event of vanishing probability. Finally, for any fixed initial coloring the event that each vertex has a successor-colored neighbor is increasing in the graph edges. Coupling graphs by the usual shared edge uniforms, then comparing to the fixed critical-window limits as \(t\to\pm\infty\), establishes the stated sharp threshold for this event.

## Verification

The two standalone scripts supplied with this result are executable with the Python standard library. `check_exact_random_gh.py` exhaustively enumerates every labelled graph and every three-coloring for \(1\le n\le5\), under two exactly rational edge/color distributions, and compares direct three-step trajectories on connected graphs against the structural criterion. It also independently evaluates the displayed finite probability formula in exact rational arithmetic. The script reports zero mismatches among \(180{,}102\) connected graph/coloring pairs per parameter set and agreement on all ten probability calculations.

`check_poisson_window.py` generates random *undirected graphs* edge by edge rather than sampling the conditional binomial law. For \(n=300\) it uses 500 seeded replicates at each of two distributions. For uniform initial colors it observed 0.392 zero-deficiency frequency versus the limiting 0.367879; for \((1/2,1/3,1/6)\) it observed 0.758 versus limiting 0.716531. On every zero-deficiency sample it directly checked the three-step orbit. These finite stochastic comparisons are diagnostic only; the preceding argument establishes the infinite-size theorem.

Reproduction commands: `python check_exact_random_gh.py` and `python check_poisson_window.py`. Captured exact outputs accompany the scripts. The computations require no network access or nonstandard Python modules.

## Relationship to prior work

Gravner, Lyu and Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs* (first available October 24, 2016; arXiv:1610.07320v1), analyzes synchronization and long-term activity on connected graphs and proves an Erdős–Rényi *eventual oscillation* transition for edge densities of order \(1/n\) (Theorem 6). That result does not state the finite conditional distribution of missing initial exciters, the rarest-color Poisson window, or the initial-state primitive-three probability. In particular, eventual oscillation and periodicity from time zero are different events, and the thresholds occur on different edge-density scales. The present theorem uses the same underlying dynamics but addresses immediate recurrent states, not eventual activity.

The Poisson step uses the classical approximation of a sum of rare independent Bernoulli indicators; this general probabilistic principle is not new. The mathematical contribution is the exact identification of those *independent* indicators for the excitable dynamics and the resulting biased-color critical window with its coefficient \(w\). Equivalent results may be expressible as isolated-vertex limits on three dependent-size bipartite edge cuts; a complete universal priority claim is not made.

## Limitations

The result is annealed, not quenched, and does not classify all eventual periodic states, basins or transient times. The threshold conclusion for general disconnected graphs concerns the all-rotating event; the equivalence to primitive three-periodicity is established on connected graphs and at the critical window with probability tending to one. The probabilities \(\pi_i\) must stay fixed and positive as \(n\) grows. No theorem for vanishing color masses, other refractory lengths, or correlated graph/initial-state distributions is asserted. The Poisson limit is asymptotic, not an exact finite-\(n\) Poisson identity. Literature coverage is incomplete, especially for equivalent isolated-vertex formulations.

## References

1. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (first public posting 2016-10-24), Sections 1–2 and 4; https://arxiv.org/abs/1610.07320 and https://arxiv.org/pdf/1610.07320.
2. B. Bollobás, *Random Graphs*, in *Modern Graph Theory* (1998), cited in reference 1 for classical connectivity context. The present connectivity estimate is proved directly.
