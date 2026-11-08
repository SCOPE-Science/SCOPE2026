# An exact four-cycle chord sensitivity law for random greedy independent sets

## Finding

Let \(P_n\) be the path on vertices \(0,1,\ldots,n-1\), and, for every integer \(n\ge4\), let \(B_n\) be obtained by adding the single edge \(\{0,3\}\). Thus \(B_n\) is a four-cycle with a pendant path of length \(n-4\) attached at vertex \(3\) (a cycle-tailed graph; when \(n=4\) there is no pendant path). In the uniform random-vertex-order greedy maximal-independent-set process, let \(M(G)\) denote the expected number of selected vertices, and put \(\delta_n=M(B_n)-M(P_n)\).

**Theorem.** The complete finite-order edge sensitivity has generating function

\[
\sum_{n\ge4}\delta_n z^n
=\frac{(3-3z+z^2)-(3+3z+z^2)e^{-2z}}{2(1-z)}.
\]

Consequently \(\delta_4=\delta_6=0\), \(\delta_5=1/15\), and \(\delta_n>0\) for every \(n\ge7\). For \(n\ge5\), the exact increment is

\[
\delta_n-\delta_{n-1}=-\frac{(-2)^{n-2}(n-3)(n-4)}{2n!}.
\]

In particular,

\[
\lim_{n\to\infty}\delta_n=\frac{1-7e^{-2}}2>0,
\qquad
\left|\delta_n-\frac{1-7e^{-2}}2\right|
\le\frac{2^{n-1}(n-2)(n-3)}{2(n+1)!}\quad(n\ge6).
\]

Adding a single edge to a path can therefore *increase* the expected random-greedy independent-set size, even when that edge creates the smallest possible even cycle and the underlying graph remains bipartite.

## Assumptions and scope

All graphs are finite, simple, unweighted and labeled. Each vertex is processed once, in a uniformly random permutation. A vertex is accepted if and only if none of its already accepted neighbors is adjacent to it. Selected vertices form a maximal independent set. The expectation averages over all permutations; there are no further random weights, graph distributions or ties. The theorem compares only the specified endpoint chord \(\{0,3\}\), not arbitrary chords or arbitrary edge additions.

## Proof

Write \(f_n=M(P_n)\), set \(f_j=0\) for \(j\le0\), and write \(g_n=M(B_n)\) for \(n\ge4\). Conditioning on the first vertex, deleting its closed neighborhood, and adding the independent contributions from the remaining components gives, for \(n\ge1\),

\[
nf_n=n+2\sum_{j=0}^{n-2}f_j.
\]

Hence its ordinary generating function is

\[
F(z)=\sum_{n\ge0}f_n z^n=\frac{1-e^{-2z}}{2(1-z)^2}.
\]

In particular \(f_1=f_2=1\), \(f_3=5/3\), and \(g_4=2\). For \(n\ge5\), distinguish the first accepted vertex \(v\) among \(0,1,2,3,4\) and among the remaining tail vertices. The residual graphs for these five distinguished choices are, respectively, \(K_1\sqcup P_{n-4}\), \(P_{n-3}\), \(K_1\sqcup P_{n-4}\), \(K_1\sqcup P_{n-5}\), and \(P_3\sqcup P_{n-6}\). For each \(5\le v\le n-1\), the residual graph is \(B_{v-1}\sqcup P_{n-v-2}\). Empty paths contribute zero. Summing yields the **exact** recurrence

\[
ng_n=n+3+f_3+f_{n-3}+2f_{n-4}+f_{n-5}+f_{n-6}
+\sum_{j=4}^{n-2}g_j+\sum_{j=0}^{n-7}f_j.
\tag{1}
\]

Here and throughout, sums over empty index ranges equal zero. Define \(G(z)=\sum_{n\ge4}g_nz^n\). Multiply (1) by \(z^n\), sum over \(n\ge5\), and use the above formula for \(F\). The resulting linear formal-power-series differential equation has a unique solution with \([z^4]G=2\); simplifying gives

\[
G(z)-F(z)+z+z^2+\frac53z^3
=\frac{(3-3z+z^2)-(3+3z+z^2)e^{-2z}}{2(1-z)}.
\]

The left side is precisely \(\sum_{n\ge4}(g_n-f_n)z^n\), proving the generating-function assertion. Subtracting consecutive coefficients of this identity shows, for \(n\ge5\),

\[
\delta_n-\delta_{n-1}
=-\tfrac12[z^n](3+3z+z^2)e^{-2z}
=-\frac{(-2)^{n-2}(n-3)(n-4)}{2n!}.
\]

Its first two nonzero increments are \(1/15\) and \(-1/15\), so \(\delta_5=1/15\) and \(\delta_6=0\). Thereafter the nonzero increments alternate in sign and their absolute values decrease strictly: the ratio of consecutive absolute increments at index \(n\ge6\) equals \(2(n-2)/((n+1)(n-4))<1\). Thus every partial sum after index six is strictly positive (group successive positive and negative increments). This proves all sign assertions.

Finally the generating function has a simple pole at \(z=1\) whose numerator tends to \(1-7e^{-2}\); the coefficient sequence therefore converges to \((1-7e^{-2})/2\), as can also be seen by summing the absolutely convergent increment series. The alternating-series remainder is bounded by the magnitude of the first omitted increment, giving the stated factorial bound. Positivity of the limiting constant follows from \(e^2>7\). This completes the proof.

## Verification

The standalone, dependency-free script `verify.py` computes exact first-vertex recurrences independently for the path and the four-cycle-tail graph, compares these values with the closed generating function and increments through order \(149\), and compares the outputs directly against a memoized induced-subgraph recurrence through order \(13\). It also independently enumerates every vertex ordering for orders \(4\) through \(8\). Its final output is `VERIFY_OK 516 exact assertions`. All comparisons use rational arithmetic. The proof above, not finite checking, justifies the unrestricted theorem.

## Relationship to prior work

Krivelevich, Mészáros, Michaeli and Shikhelman analyze the same random-order greedy independent-set model. Their 2019 preprint / 2023 revision establishes path minimality **among trees**, an exact path expectation recurrence, and a different example of failure of edge-deletion monotonicity involving two stars joined by a bridge. Those results neither compare a path to this unicyclic graph nor give the four-cycle-tail generating function, sharp equality orders or limiting sensitivity constant. See especially their Theorem 1.4 and Section 8.

Penrose and Sudbury study the equivalent blocking random sequential adsorption process on general graphs, develop forward equations and prove results on regular infinite trees and finite-graph normal approximations. Those general equations are compatible with the first-arrival derivation here but do not state the exact chord perturbation or its sign classification. The literature comparison establishes a distinction in mathematical statements, not a proof of global historical priority.

## Limitations

Only one natural path chord, closing its first four vertices to an even cycle, is treated. The theorem makes no claim that adding an arbitrary edge increases expected greedy size, or that such an increase is optimal or unique. A previous general counterexample to edge-deletion monotonicity is known, so this is a precise boundary calculation at the path rather than discovery of nonmonotonicity itself. No independent mathematical audit or comprehensive historical-priority certification has been performed.

## References

1. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, arXiv:1907.07216, first submitted 16 July 2019; Random Structures & Algorithms 64 (2024), 986–1015, https://arxiv.org/abs/1907.07216 and https://doi.org/10.1002/rsa.21200.
2. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, Annals of Applied Probability 15 (2005), 853–889, https://arxiv.org/abs/math/0503519 and https://doi.org/10.1214/105051604000000765.
