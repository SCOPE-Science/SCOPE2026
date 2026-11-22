# A Poisson fringe crossover for singleton types over random height-two posets

## Finding
Let \(\mathbb P\) be the countable universal homogeneous strict partial order. For each integer \(n\ge1\), take disjoint sets \(A_n,B_n\), each of size \(n\), and make a random finite parameter poset \(P_n\) with no within-shore comparisons and with each relation \(a<b\), \(a\in A_n,b\in B_n\), present independently with probability \(p_n\). Individually name its \(2n\) vertices inside \(\mathbb P\). Let \(T_n\) count its complete nonalgebraic singleton types and \(M_n\) count types with at least one named predecessor **and** at least one named successor. Define \(J_n\) as the number of order ideals of \(P_n\). For every fixed real \(t\), set
\[
 q_n=1-p_n=\frac{2\log n+t}{n},\qquad \alpha=e^{-t/2},
\]
for sufficiently large \(n\) that \(0<q_n<1\). Then, in probability as \(n\to\infty\),
\[
 \boxed{\quad \frac{J_n}{2^n}\longrightarrow2,\qquad
 \frac{M_n}{2^n}\longrightarrow2(e^{\alpha}-1),\qquad
 \frac{T_n}{2^n}\longrightarrow2(e^\alpha+1).\quad}
\]
In particular the **quenched** fraction of two-sided singleton types has the nondegenerate crossover
\[
 \boxed{\frac{M_n}{T_n}\xrightarrow{\mathbb P}
 \frac{e^\alpha-1}{e^\alpha+1}=\tanh(\alpha/2).}
\]
Here quenched means that the random finite parameter poset is sampled first and the types over that particular poset are then counted; the assertion is not merely a ratio of expected counts.

There is also a limiting type-level fringe law. Conditional on a sampled parameter poset, choose uniformly among its two-sided types and record \(K_n\), the smaller of the numbers of named predecessors and successors. With probability tending to one over the parameter poset, the conditional distribution of \(K_n\) converges in total variation to a zero-truncated Poisson law:
\[
 \boxed{\Pr(K_n=k\mid P_n,\text{two-sided})\xrightarrow{\mathbb P}
 \frac{\alpha^k}{k!(e^\alpha-1)},\quad k=1,2,\ldots.}
\]
The two possibilities for which shore is the small one each have asymptotic conditional probability \(1/2\). At \(t=0\), for example, the limiting two-sided fraction is \(\tanh(1/2)\), strictly between zero and one.

## Assumptions and scope
All logarithms are natural. The asserted limits use fixed \(t\), balanced, specified shores, independent cross-comparabilities, and complete nonalgebraic singleton types over all individually named parameters. Isolated vertices in either shore are allowed. The two-sided uniform-type draw is made only when \(M_n>0\); this event has probability tending to one. A finite realization of \(P_n\) embeds in the universal homogeneous poset, and homogeneity identifies the singleton types with the admissible one-point extensions. The result does not concern uniform random posets among all partial orders, nor uniformly selected elements of the infinite ambient poset.

For completeness, for every \(n\ge1\) and every fixed cross-comparability probability \(p\in[0,1]\), with \(q=1-p\), the exact **annealed** identities are
\[
 \mathbb E J_n=2^{n+1}-1+\sum_{i,j=1}^n\binom ni\binom nj q^{ij},\qquad
 \mathbb E M_n=\sum_{i,j=1}^n\binom ni\binom nj p^{ij},\qquad
 T_n=2J_n-1+M_n.
\]
These finite identities are part of the claim, but the nontrivial assertion is the joint quenched critical-window and fringe limit.

## Proof
**1. Type classification.** For a nonparameter element \(x\), write \(L=\{a\in P_n:a<x\}\) and \(U=\{a\in P_n:x<a\}\). The necessary and sufficient finite-extension conditions are that \(L\) is a downset, \(U\) an upset, and every member of \(L\) lies strictly below every member of \(U\). The finite one-point extension property realizes all such profiles, and distinct profiles give distinct complete types. Exactly \(2J_n-1\) profiles have either \(L\) or \(U\) empty. If both are nonempty, all members of \(L\) must be in \(A_n\), all members of \(U\) in \(B_n\), and the bipartite comparability graph must contain **every** edge from \(L\) to \(U\). Thus \(M_n\) is exactly the number of cross-edge-complete pairs of nonempty shore subsets. Writing \(H_n\) for the bipartite graph of **missing** comparisons, a lower ideal can be encoded by the omitted minima \(R\subseteq A_n\) and the included maxima \(S\subseteq B_n\), exactly when no comparison joins \(R\) to \(S\). Equivalently, every cross-edge from \(R\) to \(S\) is present in the missing-comparison graph. Thus \(J_n\) has \(2^{n+1}-1\) configurations with \(R\) or \(S\) empty, plus all nonempty bipartite cliques of the **missing** graph. Taking independent-edge expectations proves the displayed exact identities.

**2. One-sided profiles concentrate.** Denote by \(D_n=J_n-(2^{n+1}-1)\) the nonempty cross-biclique count in the missing-edge graph. Because \(ij\ge i+j-1\) for positive integers \(i,j\),
\[
 0\le\mathbb E D_n=\sum_{i,j\ge1}\binom ni\binom nj q_n^{ij}
 \le q_n^{-1}\big((1+q_n)^n-1\big)^2=O_t(n^5/\log n)=o(2^n).
\]
Markov's inequality gives \(J_n/2^n\to2\) in probability.

**3. Fixed fringe size.** For fixed positive integer \(k\), define
\[
 W_{n,k}=\sum_{\substack{L\subseteq A_n\\|L|=k}}
 \big(2^{N(L)}-1\big),
\]
where \(N(L)\) is the number of elements of \(B_n\) comparable above **every** element of \(L\). This counts two-sided profiles whose predecessor shore has exactly \(k\) elements. Since \(N(L)\sim\operatorname{Bin}(n,p_n^k)\),
\[
 \mathbb E W_{n,k}=\binom nk\big((1+p_n^k)^n-1\big),\qquad
 \frac{\mathbb E W_{n,k}}{2^n}\longrightarrow\frac{\alpha^k}{k!}.
\]
For two \(k\)-subsets \(L,L'\) having \(r\) common vertices, independent columns of the random comparability matrix give
\[
 \mathbb E 2^{N(L)+N(L')}=(1+2p_n^k+p_n^{2k-r})^n.
\]
When \(r=0\), this equals \((1+p_n^k)^{2n}\), so the covariance vanishes. For \(1\le r\le k\), the ratio to \((1+p_n^k)^{2n}\) is \(O_{k,t}(n^{r/2})\): the logarithm of the one-column ratio is \(rq_n/4+O_k(q_n^2)\). There are \(O_k(n^{2k-r})\) ordered pairs with intersection size \(r\), and \((1+p_n^k)^{2n}=O_{k,t}(4^n n^{-2k})\). Hence
\[
 \operatorname{Var}(W_{n,k})=O_{k,t}(4^n n^{-1/2}),
 \qquad W_{n,k}/2^n\xrightarrow{L^2}\alpha^k/k!.
\]
The identical conclusion holds with the two shores interchanged.

**4. Uniform control of large fringes.** Let \(R_{n,K}\) count complete-cross-edge profiles with both shore sizes greater than \(K\). We show
\[
 \lim_{K\to\infty}\limsup_{n\to\infty}\frac{\mathbb E R_{n,K}}{2^n}=0.\tag{*}
\]
Choose \(\delta=1/10\). By interchanging shores, all profiles having at least one shore size at most \(\delta n\) contribute at most twice
\(\sum_{K<i\le\delta n}\binom ni((1+p_n^i)^n-1)\).
For \(i\le n^{3/5}\), the elementary estimates \(\binom ni\le(en/i)^i\), \(p_n^i\le e^{-q_ni}\), and
\[
 \log\frac{1+e^{-v}}2=-v/2+\log\cosh(v/2)\le-v/2+v^2/8
\]
give, after division by \(2^n\), a summand bounded by \((C_t/i)^i\), uniformly for sufficiently large \(n\). For \(n^{3/5}<i\le n/\log n\), the same estimate is at most \(\exp(-c i\log n)\) for some absolute \(c>0\) and all sufficiently large \(n\): use \(\log i\ge(3/5)\log n\) and \(nq_n^2i/8\le(1/2+o(1))\log n\). For \(n/\log n<i\le\delta n\), the base \((1+p_n^i)/2\) is at most \((1+e^{-2+o(1)})/2\), whereas \(\binom ni\le\exp(nH(\delta))\), with \(H(\delta)<\log(2/(1+e^{-2}))\). Thus this range is exponentially negligible. Finally, when both shore sizes exceed \(\delta n\), all such pairs together have expectation at most \(4^n\exp(-q_n\delta^2n^2)=o(2^n)\). The convergent series \(\sum_i(C_t/i)^i\) proves (*).

**5. Limit and law.** For fixed \(K\), add the counts with exactly \(k\le K\) vertices on the predecessor shore and the analogous counts with exactly \(k\le K\) on the successor shore. Their overlap has at most \(\sum_{i,j\le K}\binom ni\binom nj=O_K(n^{2K})\) profiles, deterministically negligible relative to \(2^n\). Their normalized sum therefore tends in probability to \(2\sum_{k=1}^K\alpha^k/k!\). By (*) and Markov's inequality, the missing large-fringe contribution vanishes on letting \(K\to\infty\); hence \(M_n/2^n\to2(e^\alpha-1)\). Combining with the ideal estimate and \(T_n=2J_n-1+M_n\) yields the type-count and fraction limits. The same finite-\(k\) convergence, negligible overlap, and tail estimate prove the conditional distribution of the smaller shore size in total variation, with equally weighted choices of its orientation. This proves every asserted limit.

## Verification
A standalone, standard-library `verify.py` enumerates every cross-comparability graph on balanced shores through size three (respectively \(2\), \(16\), and \(512\) graphs), independently counts ideals and complete cross-edge subset pairs, and compares their uniform-graph averages with exact rational versions of the two expectation formulas. On selected graphs it separately enumerates all ternary new-point comparison profiles, checks transitive closure including preservation of all declared comparisons, and matches the direct type counts. It also evaluates the finite exact expectation of the mixed-type count for large \(n\) under several critical-window shifts against the proved limit. Run `python verify.py`; expected output is saved in `verification_output.txt`. These finite and numerical checks do not prove either probability limit; Steps 2–5 provide the unrestricted proof.

## Relationship to prior work
The generic partial order and its finite one-point extension property are established structural facts, developed for example in Hubička's 2010 thesis. The ideal/filter characterization of singleton types and the identity expressing height-two type counts through the independent-set counts of a bipartite incidence graph and its complement are also prior mathematics. None is presented as new here.

The critical comparison is with hard-core/independent-set results: a two-sided type is a nonempty biclique of the dense comparability graph, equivalently an independent set of the sparse missing-edge graph meeting **both** color classes. Classical hard-core and polymer expansions motivate the near-single-shore decomposition. Jenssen, Perkins and Potukuchi (2021, especially §§1,4–7) give approximation algorithms for regular bipartite expansion classes and describe polymer methods; their theorems do not determine a quenched, random, logarithmic-window partition-function constant or the uniform-type fringe law asserted here. Doležal, Hladký and Máthé (2015, §2 and §5) study the maximum biclique order in a distinct fixed-density inhomogeneous model, not the full biclique/type count at this varying density. The existing exact single-comparability sensitivity and weak-order-averaged one-type results address deterministic changes and a different random ensemble, respectively, so neither supplies the Poisson critical-window conclusion. Stronger unindexed hard-core asymptotics could conceivably imply this result; this remains a historical-priority risk.

## Limitations
The statement is an asymptotic theorem in probability at one fixed logarithmic window. It does not assert an almost-sure limit, uniformity for growing \(t\), concentration at all edge densities, or an exact finite distribution of the type count. The conditioning on a two-sided type involves a further uniform draw after the random base is fixed. The available literature search and mathematical implication comparisons do not constitute independent certification of historical novelty.

## References
1. J. Hubička, *Combinatorial Properties of Finite Models*, arXiv:1009.0566v1, first publicly posted 2010-09-03, §3.1, https://arxiv.org/html/1009.0566v1.
2. M. Doležal, J. Hladký and A. Máthé, *Cliques in dense inhomogeneous random graphs*, arXiv:1510.02335v1, first publicly posted 2015-10-08, especially the bipartite biclique-number discussion, https://arxiv.org/abs/1510.02335.
3. M. Jenssen, W. Perkins and A. Potukuchi, *Approximately counting independent sets in bipartite graphs via graph containers*, arXiv:2109.03744v1, §1, §4–7, https://arxiv.org/html/2109.03744v1.
4. *Sharp one-comparability sensitivity and local counting hardness for random-poset one-types*, publicly indexed research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-one-comparability-sensitivity-and-local-counting-hardness--9c2af418ff79.
5. *Quadratic average one-point type growth over random finite weak orders*, publicly indexed research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-quadratic-average-one-point-type-growth-over-random-finite-weak--a2d26ced4e39.
