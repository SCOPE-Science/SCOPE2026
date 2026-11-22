# A sharp hidden-matching recovery window from random local maxima

## Finding

For every even integer \(n=2q\ge2\), let \(M\) be an unknown perfect matching on the *known*, permanently labelled vertex set \([n]\). The hidden graph is \(G_M=K_n\setminus M\). In each of \(m\) independent experiments, assign a uniformly random total order to the vertices and observe **only the set of vertices that are strict local maxima** relative to their graph neighbors. The orders and all edges are hidden.

Let \(R_{n,m}\) be the maximum, over randomized estimators, of the minimum over all hidden perfect matchings of the probability of identifying \(M\) exactly. Put \(p_n=2/[n(n-1)]=1/[q(2q-1)]\). Let \(U\) be the number of hidden matching edges never observed together as a pair of local maxima. Then, for all \(q\ge1\) and integers \(m\ge0\),
\[
R_{n,m}=\mathbb E\bigl[(2U-1)!!^{-1}\bigr],\qquad
\mathbb E[(U)_{\underline r}]=(q)_{\underline r}(1-rp_n)^m,\quad 0\le r\le q,
\]
where \((-1)!!=1\). In particular this specifies an exact finite-sample recovery probability, by inclusion-exclusion, with no approximation.

For each fixed real \(x\), if
\[
m=m_n=\left\lfloor q(2q-1)(\log q+x)\right\rfloor
\]
(for all sufficiently large \(q\)), then, writing \(\lambda=e^{-x}\),
\[
U\xrightarrow{d}\operatorname{Poisson}(\lambda),\qquad
\boxed{\ R_{2q,m_n}\longrightarrow e^{-\lambda}\cosh(\sqrt{2\lambda})\ }.
\]
More generally, if \(m_n p_n-\log q\to+\infty\), recovery tends to one, whereas if the difference tends to \(-\infty\), recovery tends to zero. Thus the minimax exact-recovery transition in this observation model is centered at \(q(2q-1)\log q\), of order \(n^2\log n\), and the transition profile is **not** the classical probability of seeing every coupon.

## Assumptions and scope

The vertex labels and the promise that the hidden graph is a complete graph with precisely a perfect matching of missing edges are known. Only the matching itself is unknown. Each observed experiment uses a fresh independent uniform permutation of all \(n\) priorities; no priority values or full orderings are revealed, only the set of strict graph-local maxima. Exact identification includes every missing pair. Randomized estimators are allowed; the minimax probability refers to the smallest exact-success probability over the finite matching family. No assumption about arbitrary graphs or partial observations of a peak set is included.

## Proof

**Step 1: exact observation channel.** Let \(a\) be the unique highest-priority vertex. All other vertices except the partner \(b\) of \(a\) in \(M\) are adjacent to \(a\), so none is a local maximum. The partner \(b\) is another local maximum precisely if it is second highest in the order. Consequently the observed peak set is either \(\{a\}\) or \(\{a,b\}\), and the latter occurs only on a hidden matching edge. For every labelled vertex \(v\) and every unordered pair \(e\),
\[
\Pr_M(S=\{v\})=\frac{n-2}{n(n-1)},\qquad
\Pr_M(S=e)=\begin{cases}p_n,&e\in M,\\0,&e\notin M.\end{cases}
\]
These probabilities add to one: \(n(n-2)/[n(n-1)]+q\cdot2/[n(n-1)]=1\). The singleton probabilities carry **no information about which matching is hidden**. Non-singleton observations are a lazy, uniformly sampled coupon from the \(q\) matching edges.

**Step 2: exact posterior and minimax identity.** Give all \((n-1)!!\) perfect matchings an initially uniform prior. Conditional on any sequence of observed singletons and matched pairs, its likelihood is constant over precisely the matchings containing every distinct observed pair, and zero elsewhere. If \(U=u\) matching edges have not been observed, there remain \(2u\) uncovered vertices and exactly \((2u-1)!!\) equally likely compatible perfect matchings. No estimator can have conditional success probability above its reciprocal. Conversely, choosing uniformly among those completions attains that conditional success. This estimator has the same success probability for every true \(M\) by relabelling symmetry. The uniform-prior Bayes upper bound on the minimum-over-\(M\) success probability is therefore attained, proving the exact minimax formula.

**Step 3: finite coupon identities.** For any specified set of \(r\) distinct missing-matching edges, the probability that none has ever appeared is \((1-rp_n)^m\). Summing over ordered \(r\)-tuples gives the factorial moment identity. Inclusion-exclusion yields
\[
\Pr(U=u)=\binom qu\sum_{j=0}^{q-u}(-1)^j\binom{q-u}{j}\bigl[1-(u+j)p_n\bigr]^m,
\]
and hence the fully explicit formula for \(R_{n,m}\) by weighting each \(u\) by \((2u-1)!!^{-1}\). All bases are nonnegative because \(qp_n=1/(n-1)\le1\), including the \(n=2\) boundary.

**Step 4: critical window and endpoint regimes.** For \(m_n=\lfloor p_n^{-1}(\log q+x)\rfloor\) and every fixed integer \(r\ge0\),
\[
(q)_{\underline r}(1-rp_n)^{m_n}\longrightarrow e^{-rx}=\lambda^r.
\]
The factorial-moment criterion (or Bonferroni inequalities together with tightness) gives \(U\Rightarrow\operatorname{Poisson}(\lambda)\). Since \(0<(2u-1)!!^{-1}\le1\), bounded convergence in distribution on the countable state space yields
\[
\lim R_{2q,m_n}=e^{-\lambda}\sum_{u\ge0}\frac{\lambda^u}{u!(2u-1)!!}
=e^{-\lambda}\sum_{u\ge0}\frac{(2\lambda)^u}{(2u)!}
=e^{-\lambda}\cosh(\sqrt{2\lambda}).
\]
For the supercritical regime \(\mathbb E U=q(1-p_n)^m\le q e^{-mp_n}\to0\), so \(R\to1\). For the subcritical regime \(\mathbb E U\to\infty\) (using \(mp_n^2=o(1)\) when \(mp_n\le\log q\)), and \(\operatorname{Var}(U)\le\mathbb E U\) because \((1-2p_n)^m\le(1-p_n)^{2m}\). Thus \(U\to\infty\) in probability and the reciprocal double factorial tends to zero, proving \(R\to0\).

## Verification

Run \(\texttt{python verify.py}\) with Python 3 standard library. It exhaustively enumerates all perfect matchings and all priority permutations for \(n=2,4,6\), verifies the exact singleton and co-peak probabilities, and checks the finite inclusion-exclusion/minimax expressions in rational arithmetic for several small \(q,m\). The checker cannot prove the asymptotic theorem; that requires Steps 3–4. There is no Monte Carlo inference or reliance on external services.

## Relationship to prior work

Burdzy and Pal's *Twin peaks* (first publicly submitted June 26, 2016) develops random graph labellings conditional on one or two local maxima, primarily on grids, ladders and trees. Its full-text sections and results do not state the inverse problem for a missing perfect matching, the observation-channel identity, minimax posterior calculation or the critical recovery law. Classical coupon-collector occupancy provides the limiting number of unseen categories after identifying this model's observation channel, but does not alone establish the matching posterior or the nonstandard \(e^{-\lambda}\cosh(\sqrt{2\lambda})\) success curve. Related graph-tomography results using extrema covariances or threshold-subgraph degrees require different observations and do not imply this experiment's exact minimax law. Historical literature outside the inspected sources may still contain equivalent formulations.

## Limitations

The sharp recovery theorem applies only to a hidden perfect matching of deleted edges in an otherwise complete graph, with the labelled vertex set and the graph family known. It does not establish minimax complexity for general unknown graphs, incomplete local-maximum sets, or noisy and dependent experiments. The lower/upper transition and its profile are asymptotic as even \(n\to\infty\). The mathematical result has undergone a self-review, not independent validation or certification.

## References

1. K. Burdzy and S. Pal, *Twin peaks*, arXiv:1606.08025, version 1 publicly posted 2016-06-26, https://arxiv.org/abs/1606.08025 ; freely accessible full HTML: https://arxiv.org/html/1606.08025v2 .
2. P. Erdős and A. Rényi, *On a classical problem of probability theory* (1961), classical coupon-collector threshold, cited for conceptual precedent; no claim that this reference analyzes hidden graph recovery.
