# Exact absorption-time separation for a cospectral family of public-good networks

## Finding

For every integer \(m\ge2\), put \(N=m^2+1\), \(q=(m-1)^2\), and consider the two graphs
\[
G_m=K_{1,m^2},\qquad H_m=K_{m,m}\sqcup qK_1.
\]
They have the same order and adjacency characteristic polynomial \(z^{N-2}(z^2-m^2)\). For the asynchronous unit-externality linear network-public-good best-response process, started at all-zero activity and with one uniformly chosen vertex updating per step, let \(T_G,T_H\) denote the first step at which the entire action vector is a Nash equilibrium.

Write \(H_s=\sum_{j=1}^s j^{-1}\), \(B(a,b)=\int_0^1 v^{a-1}(1-v)^{b-1}\,dv\), and
\[
 a_{m,k}=(-1)^k\binom{m-1}{k}\frac{2m}{2m-k},\quad 0\le k\le m-1.
\]
Then the following exact, finite expressions hold:
\[
\boxed{\mathbb E T_G=m^2H_{m^2},}
\]
\[
\boxed{\mathbb E T_H=N\left[H_q+
\sum_{k=1}^{m-1}(-a_{m,k})B(k,q+1)
+\left(\sum_{k=0}^{m-1}a_{m,k}\right)B(2m,q+1)\right].}
\]
In particular their difference is unbounded, with the sharp first-order and logarithmic expansion
\[
\boxed{\mathbb E T_G-\mathbb E T_H=m-2\log m+O(1)\quad(m\to\infty).}
\]
Already at \(m=2\), the original five-vertex cospectral pair \(K_{1,4}\) and \(C_4\sqcup K_1\) has \(\mathbb E T_G=25/3\) and \(\mathbb E T_H=33/4\), a strict difference of \(1/12\) update. All times are individual vertex-update steps, not rounds. Dividing by \(N\) converts to rounds. The assertion of an unbounded difference concerns absolute update counts; the relative gap tends to zero.

## Assumptions and scope

Graphs are finite, undirected, simple; \(K_1\) is an isolated vertex and \(\sqcup\) denotes disjoint union. At every integer step one vertex \(i\) is drawn independently and uniformly from the \(N\) vertices. With \(A\) the graph's adjacency matrix, that vertex alone performs
\[
 x_i\longleftarrow\max\left\{0,1-\sum_j A_{ij}x_j\right\},
\]
all other activities being unchanged. Initially \(x_i(0)=0\) for every vertex. Unit externality is the endpoint \(\delta=1\) of the studied parameter range, not a limiting \(\delta\uparrow1\) statement. \(T\) is the first state satisfying all best responses exactly. This coincides with the source's first residual-below-\(\varepsilon\) stopping time for every fixed \(0<\varepsilon\le1\), since all iterates are binary and the residual is either zero or one.

## Proof

**1. The relevant discrete dynamics is random greedy maximal-independent-set formation.** Starting from zero, induction shows that every coordinate remains in \(\{0,1\}\). A vertex becomes one exactly when it and all its neighbors have never become active. Once a vertex becomes one, no neighbor can become one, so it never reverts to zero. The active set is independent and increases; it reaches an equilibrium exactly when it dominates every vertex, i.e. it is a maximal independent set. Repeated selections of already active or dominated vertices do nothing.

**2. Spectrum.** The nonzero adjacency eigenvalues of \(K_{a,b}\) are \(\pm\sqrt{ab}\), with all other eigenvalues zero. The star is \(K_{1,m^2}\), while \(K_{m,m}\) has eigenvalues \(\pm m\). Both graphs therefore have exactly two nonzero eigenvalues \(\pm m\), and the same \(N-2\) zeros. Thus their full characteristic polynomials coincide.

**3. Star waiting time.** The first selected vertex is the center with probability \(1/N\), in which case equilibrium is reached at step one. Otherwise the first selection is a leaf, and equilibrium occurs exactly when every leaf has been selected at least once. Conditional on a leaf being selected first, the expected additional waiting time is \(N H_{m^2-1}\) by the coupon-collector identity (there are \(N\) equally likely labels per step and \(m^2-1\) missing leaves). Thus
\[
\mathbb E T_G=1+\frac{m^2}{N}N H_{m^2-1}=m^2H_{m^2}.
\]

**4. Bipartite-plus-isolates waiting time.** Poissonize selections by putting independent rate-one Poisson clocks on every vertex. The superposed clock has rate \(N\), with independent uniform vertex labels. If \(\mathcal T_H\) denotes continuous time to equilibrium, the standard stopped-Poisson counting identity gives \(\mathbb E T_H=N\mathbb E\mathcal T_H\).

The first clock ringing in \(K_{m,m}\) chooses which bipartition eventually becomes fully active. Its arrival time \(\tau\) is exponential with rate \(2m\). By exponential memorylessness the other \(m-1\) vertices on the winning side have independent, rate-one residual first-arrival times. Let \(M_s\) be the maximum of \(s\) independent rate-one exponentials, with the isolate maximum \(I=M_q\) independent of both \(\tau\) and the winning-side residual maximum. Put \(R=\tau+M_{m-1}\). Then
\[
\mathcal T_H=\max(I,R),\quad \mathbb E I=H_q,
\quad \mathbb P(I\le t)=(1-e^{-t})^q.
\]
Conditional on \(\tau=s\), the winning side is complete by time \(t\) with probability \((1-e^{-(t-s)})^{m-1}\) for \(s\le t\). Expanding the binomial and integrating the exponential density gives
\[
\mathbb P(R\le t)=\int_0^t2me^{-2ms}(1-e^{-(t-s)})^{m-1}\,ds
=\sum_{k=0}^{m-1}a_{m,k}\bigl(e^{-kt}-e^{-2mt}\bigr).
\]
Since \(a_{m,0}=1\), the tail has representation
\[
\mathbb P(R>t)=\sum_{k=1}^{m-1}(-a_{m,k})e^{-kt}
+\left(\sum_{k=0}^{m-1}a_{m,k}\right)e^{-2mt}.
\]
Consequently
\[
\mathbb E[(R-I)_+]=\int_0^\infty(1-e^{-t})^q\mathbb P(R>t)\,dt.
\]
Substitute \(v=e^{-t}\) and use the beta integral \(\int_0^\infty e^{-kt}(1-e^{-t})^qdt=B(k,q+1)\) to obtain the boxed formula. Although the finite sum has alternating terms, it equals the manifestly nonnegative integral.

**5. Asymptotic gap.** Write \(Z_m=\mathbb E[(R-I)_+]\). For \(0\le z\le1\), the bounds
\[
(m-1)z-\binom{m-1}{2}z^2\le1-(1-z)^{m-1}\le(m-1)z
\]
combined with the exponential law of \(\tau\) and integrated against \((1-e^{-t})^q\) give
\[
Z_m=\frac{(m-1)2m}{(2m-1)(q+1)}+O\!\left(\frac{m^2}{(q+1)(q+2)}\right).
\]
For clarity, the truncated exponential moments produce only beta-integral errors bounded by a constant multiple of \(m B(2m,q+1)\), and \(B(2m,q+1)\le B(2,q+1)=1/[(q+1)(q+2)]\); the quadratic error has the explicitly bounded factor \(\binom{m-1}{2}\,2m/(2m-2)\). Since \(q=(m-1)^2\), this yields \(Z_m=1/m+O(m^{-2})\).

Moreover, \(H_{m^2}-H_q=2/m+O(m^{-2})\) and \(H_{m^2}=2\log m+O(1)\). Therefore
\[
\begin{aligned}
\mathbb E T_G-\mathbb E T_H
&=N(H_{m^2}-H_q)-H_{m^2}-NZ_m\\
&=m-2\log m+O(1),
\end{aligned}
\]
which completes the proof. The stated five-vertex values follow by substituting \(m=2\), \(q=1\) into the exact beta sums.

## Verification

The standalone script `check_absorption.py` uses exact rational arithmetic to implement the boxed beta-sum formula and an independent finite-state recurrence for the random vertex-update process. The recurrences agree identically for every integer \(m=2,\ldots,8\), and direct recursion on adjacency-defined active subsets independently reproduces both values for \(m=2,3\). In particular the script checks the \(1/12\) five-vertex difference. Execute with Python 3 using `python check_absorption.py`; only the Python standard library is required. The code checks finite instances; the asymptotic statement follows from the preceding analytic inequalities, not from tests.

## Relationship to prior work

Misiak and Dziubiński (2026) define the identical linear best-response rule, update ordering, equilibrium-residual stopping criterion, and exhibit \(K_{1,4}\) and \(C_4\sqcup K_1\) as cospectral examples with different *simulated* convergence behavior. They also classify equilibria on complete bipartite graphs and prove general local stochastic stability results. The present finding fixes \(\delta=1\) and the all-zero initial state, gives exact finite-step absorption expectations for an entire cospectral family, and quantifies their unbounded (though relatively vanishing) difference. The existing qualitative spectral distinction and the underlying greedy-independent-set interpretation are not claimed as new.

Existing random-greedy maximal-independent-set results on complete multipartite and threshold graphs determine the distribution of the terminal independent set, not the number of *uniform-with-replacement vertex updates* before reaching a maximal independent set. That distinction matters: repeated draws can delay a Nash equilibrium well after the eventual selected class is determined. The result is an exact benchmark, not a new general theorem for all graphs or non-unit externality values.

## Limitations

The two cospectral graphs have different connectivity: \(G_m\) is connected but \(H_m\) has \((m-1)^2\) isolated vertices. The calculated gap need not extend to connected cospectral pairs. The process starts from zero at the endpoint \(\delta=1\); no conclusion is asserted for arbitrary initial real-valued states or \(\delta<1\). The mean-time gap grows as order \(\sqrt N\), but both mean times grow as order \(N\log N\), so the relative gap vanishes. The search does not rule out an unindexed equivalent arrival-time calculation in random-sequential-adsorption literature.

## References

1. W. Misiak and M. Dziubiński, *Convergence rates of random-order best-response dynamics in public good games on networks*, arXiv:2602.15986v1, first posted 17 February 2026, https://arxiv.org/html/2602.15986v1 . Section 2 defines the updates; Section 3.2.2 and Figure 2 discuss complete bipartite and five-vertex cospectral examples; Appendix B discusses convergence-time measurement.
2. M. Krivelevich, P. Mészáros, B. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, Random Structures & Algorithms 64 (2024), 986–1015, DOI:10.1002/rsa.21200, first published 18 December 2023.
3. *Sharp variance of random greedy maximal independent sets on complete multipartite graphs*, public research record, September 2026, https://github.com/published-finding corpus/2026/blob/main/2026/9/19/SCOPE-random-greedy-mis-variance-complete-multipartite--9cd73ef8690f/RESULT.md .
4. *Exact random-greedy independent-set law on threshold graphs*, public research record, October 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-random-greedy-independent-set-law-on-threshold-graphs--13703984bf2d/RESULT.md .
