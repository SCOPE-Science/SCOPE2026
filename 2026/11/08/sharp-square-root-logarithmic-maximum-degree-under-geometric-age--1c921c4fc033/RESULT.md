# Sharp square-root-logarithmic maximum degree under geometric age preference

## Finding

For each fixed integer \(m\ge 1\) and real \(\beta>0\), consider the age-preferential growing multigraph defined below. Write \(M_n\) for the maximum number of incoming edges at time \(n\), counting parallel edges. Let \(\Delta_n\) be the maximum undirected degree, also counting multiplicity. Then, on the probability space carrying all successive edge choices,

\[
\boxed{\lim_{n\to\infty}\frac{M_n}{\sqrt{\log n}}
=\lim_{n\to\infty}\frac{\Delta_n}{\sqrt{\log n}}
=\sqrt{\frac{2m}{\beta}}\quad\text{almost surely}.}
\]

The constant is sharp for every fixed \(m\) and \(\beta\). This resolves the first-order largest-degree question identified for the exponentially preferential recursive tree, and extends the result from one parent per arrival to arbitrary fixed arrival multiplicity.

## Assumptions and scope

Start from one vertex \(v_0\) and no edges. At birth time \(t\ge1\), introduce \(v_t\) and select \(m\) parents independently, with replacement, among \(v_0,\ldots,v_{t-1}\). The choice of parent \(v_k\) has probability

\[
p_{k,t}=\frac{e^{\beta k}}{\sum_{\ell=0}^{t-1}e^{\beta\ell}}
=\frac{(1-q)q^{t-1-k}}{1-q^t},\qquad q=e^{-\beta}\in(0,1).
\]

All choices are mutually independent across birth times and across edges at a birth. We count parallel edges separately, and do not insert loops. Let \(D_{k,n}=\sum_{t=k+1}^n\sum_{a=1}^m\mathbf1\{\text{the \(a\)-th parent at birth \(t\) is \(k\)}\}\) for \(0\le k\le n\) and \(D_{n,n}=0\). Set \(M_n=\max_{0\le k\le n}D_{k,n}\). For the undirected degree \(\deg_n(v_k)\), \(\deg_n(v_0)=D_{0,n}\) and \(\deg_n(v_k)=m+D_{k,n}\) for \(1\le k\le n\). Therefore \(M_n\le\Delta_n\le M_n+m\).

## Proof

**Step 1: A uniform sharp leading upper tail.** For every \(k<t\), put \(j=t-k-1\). The normalization gives

\[
(1-q)q^j\le p_{k,t}\le q^j.
\]

For any \(s\ge0\), independence and the Bernoulli moment-generating function yield, uniformly in \(k\) and \(n\),

\[
\mathbb E e^{sD_{k,n}}
=\prod_{t=k+1}^{n}\left(1+p_{k,t}(e^s-1)\right)^m
\le\prod_{j=0}^{\infty}(1+e^{s-\beta j})^m.
\]

The elementary estimate \(\log(1+e^x)\le x_++\min\{\log2,e^{-|x|}\}\), or a split at \(j=\lfloor s/\beta\rfloor\), proves for some constant \(C_\beta<\infty\), independent of \(s\),

\[
\sum_{j=0}^{\infty}\log(1+e^{s-\beta j})
\le\frac{s^2}{2\beta}+C_\beta(s+1).
\]

Indeed, the positive-part sum is \(s^2/(2\beta)+O_\beta(s+1)\), the at-most-\(\lfloor s/\beta\rfloor+1\) terms before the split contribute at most \(\log2\) beyond their positive parts, and the remainder is geometrically summable. Chernoff's bound with \(s=\beta r/m\), for any integer \(r\ge1\), now gives a constant \(C_{m,\beta}\) such that

\[
\sup_{n\ge k\ge0}\mathbb P(D_{k,n}\ge r)
\le\exp\left(-\frac{\beta r^2}{2m}+C_{m,\beta}(r+1)\right).
\]

The same bound holds for the almost-surely finite total future indegree of any fixed vertex; finiteness also follows from \(\sum_{t>k}p_{k,t}\le(1-q)^{-1}\) and Borel–Cantelli.

**Step 2: A matching lower tail from full-hit blocks.** Put \(h=\lceil r/m\rceil\). For a vertex \(k\), let \(E_{k,h}\) be the event that *all* \(m\) choices at each birth \(k+1,\ldots,k+h\) attach to \(k\). On \(E_{k,h}\), the vertex receives at least \(r\) edges, and

\[
\mathbb P(E_{k,h})
=\prod_{j=0}^{h-1}p_{k,k+j+1}^{m}
\ge(1-q)^{mh}q^{m h(h-1)/2}
=\exp\left(-\frac{\beta r^2}{2m}+O_{m,\beta}(r+1)\right).
\]

The last \(O\)-term is a two-sided algebraic expansion of \(h=r/m+O(1)\); the displayed inequality uses its lower-bound direction. The important point is that the quadratic coefficient exactly matches Step 1. For \(k\) in the arithmetic progression \(0,h+1,2(h+1),\ldots\), the birth-time intervals \(\{k+1,\ldots,k+h\}\) are disjoint. Thus the corresponding \(E_{k,h}\) events are independent. Provided \(k+h\le n\), there are at least \(n/[2(h+1)]\) such events for large \(n\) with \(h=O(\sqrt{\log n})\).

**Step 3: Almost-sure maximum law.** Let \(c=\sqrt{2m/\beta}\), fix \(\varepsilon\in(0,1)\), and set \(r_n^+=\lceil(1+\varepsilon)c\sqrt{\log n}\rceil\). By Step 1 and a union bound over the \(n+1\) vertices,

\[
\mathbb P(M_n\ge r_n^+)
\le n^{-2\varepsilon-\varepsilon^2+o(1)}.
\]

For \(r_n^-=\lfloor(1-\varepsilon)c\sqrt{\log n}\rfloor\) and \(h_n=\lceil r_n^-/m\rceil\), each event in Step 2 has probability at least \(n^{-(1-\varepsilon)^2+o(1)}\). Independence of the disjoint blocks gives

\[
\mathbb P(M_n<r_n^-)
\le\exp\left(-n^{2\varepsilon-\varepsilon^2+o(1)}\right).
\]

Both failure probabilities are summable on the dyadic subsequence \(n=2^j\). By Borel–Cantelli, for every rational \(\varepsilon\in(0,1)\), eventually almost surely

\[
(1-\varepsilon)c\sqrt{\log(2^j)}-1
\le M_{2^j}\le
(1+\varepsilon)c\sqrt{\log(2^j)}+1.
\]

Because \(M_n\) is nondecreasing in \(n\) and \(\sqrt{\log(2^{j+1})}/\sqrt{\log(2^j)}\to1\), the dyadic limit extends to every integer \(n\). Finally \(M_n\le\Delta_n\le M_n+m\) transfers the same limit to undirected degree. This completes the proof.

## Verification

The independent-parent formula, normalization, pointwise geometric bounds, exact incoming-degree generating function and finite exhaustive joint laws are checked with rational arithmetic in `artifacts/verify.py` (Python 3 standard library). Running the extracted script produces `VERIFIED 61632 exact finite rational assertions`. The checker exhausts all parent-choice sequences through five births with one or two edges per birth for two rational values of \(q\). Its tests exercise the finite algebra, while the Gaussian-in-\(r\) tail estimate and almost-sure infinite limit are proved in Steps 1–3, not inferred from numerical sampling.

## Relationship to prior work

Aguech, Mahmoud, Mohamed and Yang (2025) introduced **exactly the one-edge exponential-age recursive tree**: at birth each new vertex selects a parent in proportion to \(a^k\), where \(a>1\) matches \(a=e^{\beta}\). They determine fixed-vertex degree laws and asymptotic phases, not the maximum over all vertices. Their concluding remarks explicitly identify *maximal degree* as a subject for future research. The present theorem supplies that missing first-order extreme-degree law, then extends it to every fixed number of independently sampled parents with replacement.

Tang, Wang and Wu (July 2026) study a different age-preferential recursive tree whose attachment window contains only the two most recent predecessors. Its degrees are uniformly bounded and its principal theorems concern one-endedness and random-walk collisions. Their November 2, 2026 paper *Random Walk on age-preferential random growth processes* independently formulates the same exponential-age **multigraph** used here and establishes recurrence and infinite collisions. Its formula and theorems are credited, but it does not assert the sharp \(\sqrt{\log n}\) maximum-degree constant.

Lodewijks and Ortgiese's weighted recursive graph results and Eslava–Lodewijks–Ortgiese's fine-asymptotic results concern exchangeable independent, identically distributed vertex weights; their logarithmic/extreme-value laws do not imply the deterministic exponentially increasing weight sequence here. Classical uniform recursive trees have different logarithmic maximum-degree scaling. The leading asymptotic in the present deterministic-weight, finite-memory-tail setting is therefore not a restatement of these theorems.

## Limitations

All asymptotics fix \(m\in\mathbb N\) and \(\beta>0\); they are not uniform as \(\beta\downarrow0\), \(\beta\uparrow\infty\), or \(m\to\infty\). The claim is first-order only: it does not identify centered extreme-value fluctuations, the location of the maximizing vertex or graph-walk behavior. Parallel edges are counted with multiplicity; a model suppressing repeated targets can have a different large-degree tail. Novelty is provisional pending a full historical-priority review of deterministic-weight recursive tree literature.

## References

1. R. Aguech, H. Mahmoud, H. Mohamed, and Z. Yang, *Exponentially preferential trees*, Network Science 13 (2025), e5 (published online April 14, 2025), https://doi.org/10.1017/nws.2025.3.
2. J.-s. Tang, F. Wang, and X.-Y. Wu, *Infinite collisions of simple random walks on random recursive trees generated by Bernoulli sequences*, arXiv:2607.02916 (first public July 3, 2026), https://arxiv.org/abs/2607.02916.
3. J.-s. Tang, F. Wang, and X.-Y. Wu, *Random Walk on age-preferential random growth processes*, arXiv:2611.02329v1 (November 2, 2026), https://arxiv.org/html/2611.02329v1.
4. B. Lodewijks and M. Ortgiese, *The maximal degree in random recursive graphs with random weights*, Annals of Applied Probability 34 (2024), 3469–3540; https://arxiv.org/html/2007.05438v4.
5. L. Eslava, B. Lodewijks, and M. Ortgiese, *Fine asymptotics for the maximum degree in weighted recursive trees with bounded random weights*, Stochastic Processes and their Applications 158 (2023), 505–569; https://arxiv.org/abs/2109.15270.
6. L. Devroye and J. Lu, *The strong convergence of maximal degrees in uniform random recursive trees and DAGs*, Random Structures & Algorithms 7 (1995), 1–14, https://doi.org/10.1002/rsa.3240070102.
