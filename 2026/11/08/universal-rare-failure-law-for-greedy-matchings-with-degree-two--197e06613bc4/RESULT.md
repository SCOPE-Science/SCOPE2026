# Universal rare-failure law for greedy matchings with degree-two forbidden edges

## Finding

Let \(N\ge 6\) be even, and let \(H\) be any simple graph on \(N\) labeled vertices with maximum degree at most two. Put \(m=|E(H)|\) and \(G=K_N\setminus E(H)\). Starting with all vertices unmatched, repeatedly choose an edge uniformly from those joining two currently unmatched vertices in \(G\), match its endpoints, and remove them. Write \(F\) for the event that the terminal matching is not perfect, and \(U\) for the unordered pair of unmatched vertices just before the possible final matching step.

**Theorem.** There is an absolute constant \(C\) such that for every such \(N,H\) and every \(e\in E(H)\),
\[
\left|\Pr(U=e)-\frac{3}{N^2-1}\right|\le C\frac{\log N}{N^3}.
\]
Consequently, uniformly over all choices of \(H\),
\[
\Pr(F)=\frac{3m}{N^2-1}+O\!\left(\frac{m\log N}{N^3}\right).
\]
If \(m>0\), the failure probability is \((3/2+O(\log N/N))\,m/\binom N2\); conditional on failure, the identity of the unmatched forbidden edge is within \(O(\log N/N)\) in total variation of the uniform distribution on \(E(H)\). All constants are universal. For \(m=0\), failure is impossible. If \(H\) consists of a single edge, its survival probability is **exactly** \(3/(N^2-1)\) for every even \(N\ge4\).

The factor \(3/2\) is a universal amplification relative to the naive missing-edge fraction, even if \(H\) is a collection of paths and cycles with highly unequal components.

## Assumptions and scope

All graphs are finite, simple, labeled, and undirected. Only uniformly chosen *currently feasible* edges are used; choosing a random unmatched vertex first would be a different algorithm. The asymptotics are as even \(N\to\infty\), uniformly in the degree-two forbidden graph, with no density or component-size assumption on \(H\). With \(N\ge6\), \(G\) has minimum degree at least \(N-3\ge N/2\) and therefore possesses a perfect matching. The theorem concerns a random maximal matching's failure to find one.

Because \(\Delta(H)\le2\), every induced subgraph of \(G\) on at least four vertices has an edge: otherwise \(H\) would contain a four-clique. Thus the process reaches a two-vertex remainder. It fails exactly when that pair is an edge of \(H\).

## Proof

**1. A uniform survival estimate.** Let \(S_s\) be the set of \(s\) unmatched vertices, at the stage where \(s\) is even, before the next pairing; \(S_N\) is the entire vertex set. For each fixed set \(A\) of \(k\le4\) vertices, and all \(s\ge k\),
\[
\Pr(A\subseteq S_s)\le C_k(s/N)^k,
\tag{1}
\]
where \(C_k\) is independent of \(N,H,A,s\). Indeed, if \(A\subseteq S_s\), at least \(k(s-k)-2k\) feasible edges between \(A\) and its complement meet \(A\), because each vertex has at most two forbidden neighbors. Hence, for \(s\ge16\),
\[
\Pr(A\subseteq S_{s-2}\mid S_s)
\le 1-\frac{2k(s-k-2)}{s(s-1)}
=\frac{(s-k)(s-k-1)}{s(s-1)}+\frac{k(k+3)}{s(s-1)}.
\]
The first summand is the survival factor for a uniformly sampled \(s-2\) subset of an \(s\) set. Because \(k\le4\) and \(s\ge16\), the complete right-hand side is at most this first summand multiplied by \(1+C'_k/s^2\). Taking products of these bounds from \(N\) down to \(s\) yields \(C''_k(s)_k/(N)_k\le C'''_k(s/N)^k\). For smaller \(s\), monotonicity of survival and the bound at size sixteen prove (1), after enlarging \(C_k\); the finitely many \(N<16\) can also be absorbed into \(C_k\).

**2. Comparison with a single forbidden pair.** Fix a forbidden edge \(e=\{u,v\}\). Let \(a_s=\Pr(e\subseteq S_s)\). On the event \(e\subseteq S_s\), write \(R=S_s\setminus e\), \(h=|E(H[R])|\), and \(d\) for the number of forbidden edges from \(e\) to \(R\). Then \(0\le d\le4\), \(0\le h\le s\), and the exact conditional probability that both endpoints of \(e\) survive the next matching step is
\[
 f_s=\frac{\binom{s-2}{2}-h}{\binom{s}{2}-1-d-h}.
\]
If \(e\) were the only missing edge, this probability would be
\[
 q_s=\frac{\binom{s-2}{2}}{\binom{s}{2}-1}
=\frac{s-3}{s+1}.
\]
Set \(D_0=\binom{s}{2}-1\) and \(L=\binom{s-2}{2}\). Exact subtraction gives
\[
 f_s-q_s=\frac{L d-2(s-2)h}{D_0(D_0-d-h)}.
\tag{2}
\]
Since \(D_0\ge s^2/4\) and \(D_0-d-h=|E(G[S_s])|\ge s(s-3)/2\ge s^2/8\) for every even \(s\ge4\), (2) implies
\[
 |f_s-q_s|\le\frac{16d}{s^2}+\frac{64h}{s^3}.
\]
By (1), the expected \(d\) multiplied by the indicator of \(e\subseteq S_s\) is at most \(4C_3(s/N)^3\): each such edge uses one additional specified surviving vertex. Likewise, the expected \(h\) multiplied by that indicator is at most \(mC_4(s/N)^4\le NC_4(s/N)^4\): each such edge uses two additional specified surviving vertices. Thus, for an absolute constant \(B\),
\[
 |a_{s-2}-q_sa_s|\le B\frac{s}{N^3}
\qquad (s=4,6,\ldots,N).
\tag{3}
\]
This is the essential uniform stability estimate; no independence among the remaining vertices has been assumed.

**3. Telescoping and the rare-failure law.** We have \(a_N=1\), and the reference survival product telescopes exactly:
\[
 \prod_{s=4,6,\ldots,N}q_s
 =\prod_{s=4,6,\ldots,N}\frac{s-3}{s+1}
 =\frac3{(N-1)(N+1)}.
\tag{4}
\]
An error introduced at level \(s\) is subsequently multiplied by
\[
 \prod_{t=4,6,\ldots,s-2}q_t=\frac3{(s-3)(s-1)}.
\]
Using (3) therefore gives
\[
 \left|a_2-\frac3{N^2-1}\right|
 \le \frac{3B}{N^3}\sum_{\substack{4\le s\le N\\s\;\mathrm{even}}}\frac{s}{(s-3)(s-1)}
 = O\!\left(\frac{\log N}{N^3}\right).
\]
The bound is independent of \(H\) and \(e\). Since each failure corresponds to exactly one edge in \(E(H)\), summing the individual probabilities proves the failure expansion. When \(m>0\), normalize these nearly equal probabilities by their sum to obtain the claimed total-variation bound on the unmatched edge's conditional law. For \(H=\{e\}\), both \(d\) and \(h\) vanish at every step on survival, so (4) gives the stated exact identity. This completes the proof.

## Verification

Run `python check.py` with Python 3, using only its standard library. The checker exactly enumerates greedy residual-pair laws over deterministic families of degree-two deleted graphs and seeded diverse degree-two examples at even orders \(N=4,6,8,10,12\), independently compares random feasible-edge selection with exhaustive edge-priority orderings on selected four-vertex instances, and checks the exact single-edge and telescoping identities. A successful run prints `VERIFY_OK 28833 exact assertions` (reproduced when preparing this result). These computations inspect finite cases only; the uniform infinite-family error bound comes from (1)–(4).

## Relationship to prior work

Arnosti's 2021 study of RANDOM-EDGE matching establishes average-case comparisons among randomized algorithms on bipartite random graphs, not an asymptotic probability of failing to find a perfect matching on the deterministic, generally nonbipartite graph \(K_N\setminus E(H)\). Dyer and Frieze (1991) introduce and analyze the same random feasible-edge procedure for arbitrary graphs, emphasizing extremal approximation guarantees and sparse classes. Tang, Wu and Zhang (2019) investigate different vertex-first greedy rules. None of the inspected accessible material supplies the degree-two-forbidden-edge uniform defect-location law or its \(3/2\) constant. The deleted-perfect-matching case is one particularly symmetric example, whereas the theorem establishes a uniform result for all path-and-cycle configurations.

## Limitations

The hypothesis \(\Delta(H)\le2\) is essential to the present proof of a unique final pair; with maximum forbidden degree at least three the process can stop with four or more vertices. The error is an asymptotic bound with an absolute but unspecified constant, not a tight finite-order numerical interval. The theorem is about random feasible-edge selection, not random-vertex or weighted greedy matching. Its originality assessment is provisional: the full 1991 original paper was not available for line-by-line comparison, and independent validation has not been performed.

## References

- N. Arnosti, *Greedy Matching in Bipartite Random Graphs*, **Stochastic Systems** 12 (2022), 133–150; first online November 2, 2021. https://doi.org/10.1287/stsy.2021.0082
- M. Dyer and A. Frieze, *Randomized greedy matching*, **Random Structures & Algorithms** 2 (1991), 29–45. https://doi.org/10.1002/rsa.3240020104
- Z. G. Tang, X. Wu and Y. Zhang, *Towards a Better Understanding of Randomized Greedy Matching*, first arXiv version July 11, 2019. https://arxiv.org/abs/1907.05135
