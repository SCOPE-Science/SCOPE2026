# Optimal Rayleigh law for the first triangle in a full-choice semi-random graph

## Finding

Consider the online semi-random graph process on the fixed vertex set \([n]=\{1,\ldots,n\}\). At each round a vertex \(U_t\) is sampled independently and uniformly from \([n]\); after observing it and all previous rounds, a Builder chooses any distinct vertex \(V_t\in[n]\setminus\{U_t\}\) and adds the undirected edge \(U_tV_t\). Repeated edges are permitted but the underlying simple graph determines triangle presence. Let \(T_n\) be the first round containing a triangle, with \(T_n=\infty\) for a strategy that never succeeds.

For \(m\in\mathbb Z_{\ge0}\), write
\[
S_n(m)=\inf_{\mathcal A}\Pr_{\mathcal A}(T_n>m),
\]
where the infimum is over all nonanticipating, possibly randomized strategies. **Theorem.** For every fixed \(L>0\), uniformly over integers \(0\le m\le L\sqrt n\),
\[
\boxed{S_n(m)=\exp\!\left(-\frac{2m^2}{3n}\right)+O_L(n^{-1/2}).}
\]
Consequently, for every \(x\ge0\),
\[
\boxed{\lim_{n\to\infty}\sup_{\mathcal A}\Pr_{\mathcal A}(T_n\le\lfloor x\sqrt n\rfloor)=1-e^{-2x^2/3}.}
\]
A single explicit strategy based on assembling vertex-disjoint four-vertex paths achieves the bound simultaneously for all bounded \(m/\sqrt n\). Its limiting rescaled first-triangle time has Rayleigh survival function \(e^{-2x^2/3}\); the limiting scale parameter is \(\sqrt{3/4}\).

## Assumptions and scope

There is **full choice** of the second endpoint: the candidate-set size is exactly \(n-1\). The random offered vertices are independent, with replacement. The Builder may remember the entire past but not future offered vertices. The statement is about the first occurrence of a triangle; it is not a statement about triangle avoidance, triangle counts, offline builders, or smaller random candidate sets. Constants in \(O_L(\cdot)\) can depend on \(L\), not on \(n,m\), or the strategy. The finite-horizon statement applies for all sufficiently large \(n\) depending on \(L\).

Call a vertex of a triangle-free simple graph **closable** when it is an endpoint of a length-two path whose other endpoint is not already adjacent to it. Equivalently, it has a possible new incident edge that completes a triangle. Write \(a(G)\) for the number of closable vertices and \(e(G)\) for the number of distinct edges. Let \(P_4\) denote the path with four vertices and three edges.

## Proof

**1. Sharp deterministic exposure bound.** For every finite triangle-free simple graph,
\[
\boxed{a(G)\le \frac43 e(G).}
\]
The inequality is additive across connected components. An isolated vertex contributes zero. A one-edge component contributes zero. A two-edge connected component must be \(P_3\) and has exactly two closable endpoints, so its contribution is \(2\le8/3\). For a connected component with \(e\ge3\) edges and \(v\) vertices, closable vertices number at most \(v\le e+1\le4e/3\). Summation proves the claim. A disjoint union of \(P_4\)'s achieves equality: all four vertices of each \(P_4\) are closable.

**2. Universal survival lower bound.** Conditional on a triangle-free history at time \(j\), a triangle created by the next edge must contain the newly offered vertex \(U_{j+1}\). Therefore its conditional probability is at most \(a(G_j)/n\le4j/(3n)\), because the underlying graph has at most \(j\) edges. For \(m\le L\sqrt n\), all factors below are positive for large \(n\), and induction gives, for every strategy,
\[
\Pr_{\mathcal A}(T_n>m)\ge B_{n,m}:=\prod_{j=0}^{m-1}\left(1-\frac{4j}{3n}\right).
\]
For such \(m\), uniformly,
\[
\log B_{n,m}=-\frac{2m(m-1)}{3n}+O(m^3/n^2)
=-\frac{2m^2}{3n}+O_L(n^{-1/2}).
\]

**3. An online nearly extremal strategy.** Maintain a collection of completed, vertex-disjoint reserved \(P_4\)'s, and at most one partial reserved path of one or two edges. Every vertex incident to any existing edge is marked **used**. Upon receiving \(U_{j+1}=u\), first close a triangle immediately if \(u\) is closable. Otherwise, if \(u\) is unused, make a **productive move**: if there is no partial reserved path, join \(u\) to another unused vertex to start a \(P_2\); if there is one, attach \(u\) to its designated free endpoint, extending \(P_2\) to \(P_3\) or \(P_3\) to a completed \(P_4\). Every third productive move completes another disjoint reserved \(P_4\). If \(u\) is already used and is not closable, make a nonproductive move by joining \(u\) to a currently unused vertex. All these choices are possible at the stated time scale, because at most \(2j\) vertices are used after \(j\) rounds.

Nonproductive moves never touch a completed \(P_4\) on a triangle-free history: each vertex of such a path is closable, and would instead trigger immediate success. They also cannot damage any already reserved path, because their chosen second endpoint is unused. An extra branch attached to a partial path does not erase its designated path edges. In particular, if \(R_j\) denotes the count of nonproductive rounds among the first \(j\) rounds on a surviving history, then the graph has at least \(\lfloor(j-R_j)/3\rfloor\) completed disjoint \(P_4\)'s and hence
\[
a(G_j)\ge4\left\lfloor\frac{j-R_j}{3}\right\rfloor
\ge\frac{4j}{3}-\frac{4R_j}{3}-4.
\]
Conditional on a surviving history before round \(i+1\), no more than \(2i\) vertices are used, so the probability that this round is nonproductive is at most \(2i/n\). On non-surviving histories define \(R_j\) arbitrarily as zero. Then
\[
\mathbb E[\mathbf1_{\{T_n>j\}}R_j]
\le\sum_{i=0}^{j-1}\frac{2i}{n}
=\frac{j(j-1)}{n}.
\]
Since the strategy closes a triangle whenever the offered vertex is closable, its survival probability \(s_j=\Pr(T_n>j)\) satisfies
\[
\begin{aligned}
s_{j+1}&=\mathbb E\left[\mathbf1_{\{T_n>j\}}\left(1-\frac{a(G_j)}n\right)\right]\\
&\le\left(1-\frac{4j}{3n}\right)s_j
+\frac{4j(j-1)}{3n^2}+\frac4n.
\end{aligned}
\]
Iterating from \(s_0=1\), using factors in \([0,1]\), gives
\[
 s_m\le B_{n,m}+\sum_{j=0}^{m-1}\left(\frac{4j(j-1)}{3n^2}+\frac4n\right)
=B_{n,m}+O\!\left(\frac{m^3}{n^2}+\frac mn\right).
\]
The right-hand error is \(O_L(n^{-1/2})\), and the universal lower bound from Step 2 applies to this strategy. Combining the two inequalities proves the theorem. The strategy does not depend on \(L\), so the same strategy works for every fixed bounded \(m/\sqrt n\).

## Verification

The supplied standalone Python script `verify.py` enumerates every labeled simple triangle-free graph on up to six vertices and checks \(3a(G)\le4e(G)\), including exact equality for \(P_4\). It tests the reserved-path count and closability invariants along seeded sample paths and compares empirical survival with the derived Rayleigh profile. Run `python verify.py` with Python 3 (standard library only). In the recorded run, 6,228 triangle-free labeled graphs were checked, and the seeded simulations passed. Finite checks are corroboration; the infinite-dimensional optimization and probability limit follow from the proof above, not simulation.

## Relationship to prior work

Ben-Eliezer, Hefetz, Kronenberg, Parczyk, Shikhelman and Stojaković introduced the fully adaptive model in [1]. Their Theorems 1.10 and 1.11 and proof of Claim 5.1 show the correct \(\sqrt n\) high-probability threshold scale for triangle creation but do not give the sharp fixed-probability window or its optimal constant. Akhmejanova and Kupavskii [2], particularly Theorem 3 and Section 4.1, establish an interpolating-candidate-set model and high-probability order-of-magnitude clique hitting times. In its full-choice endpoint, their result does not give the exact Rayleigh profile. The deterministic closable-vertex extremum and the matching \(P_4\) strategy together supply the additional optimization needed here. Gao and Koerts [3] compare pre- and post-positional models for fixed-degenerate targets but do not state the constant-probability first-triangle law. These comparisons concern the mathematical statements, not simply terminology or titles.

## Limitations

The proof is restricted to full choice of the second endpoint; it does not give the sharp profile for \(s<n-1\). The asymptotic bound is uniform only on fixed bounded intervals after normalization by \(\sqrt n\), and it does not claim an exact finite-\(n\) optimal strategy. This work has not received independent mathematical review. Literature search and accessible-source inspection do not establish absolute historical priority; an unlocated earlier precise optimal quantile theorem remains possible.

## References

[1] O. Ben-Eliezer, D. Hefetz, G. Kronenberg, O. Parczyk, C. Shikhelman, M. Stojaković, *Semi-random graph process*, arXiv:1805.02259 (publicly posted 2018-05-06); Random Structures & Algorithms **56** (2020), 648–675. https://arxiv.org/abs/1805.02259

[2] M. Akhmejanova, A. Kupavskii, *Between the Semi-Random Process and G(n,p)*, arXiv:2610.33854v1 (publicly posted 2026-10-24), Theorem 3 and Section 4.1. https://arxiv.org/abs/2610.33854

[3] P. Gao, H. Koerts, *On the Pre- and Post-Positional Semi-Random Graph Processes*, Journal of Graph Theory, DOI:10.1002/jgt.23202 (first published 2024-12-12). https://doi.org/10.1002/jgt.23202
