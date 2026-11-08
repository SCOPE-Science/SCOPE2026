# Joint Gaussian fluctuations of sources, sinks, and isolated vertices under subcritical acyclicity conditioning

## Finding
Fix \(0<\lambda<1\). In the loop-free binomial directed graph on \(n\) labelled vertices, independently include every ordered arc between distinct vertices with probability \(p_n=\lambda/n\), and condition on the graph being acyclic. Write \(S_n\), \(K_n\), and \(I_n\) for the numbers of vertices of indegree zero, outdegree zero, and both indegree and outdegree zero, respectively. Then
\[
 n^{-1/2}\begin{pmatrix}S_n-ne^{-\lambda}\\K_n-ne^{-\lambda}\\I_n-ne^{-2\lambda}\end{pmatrix}
 \ \xrightarrow{\mathrm d}\ N_3(0,\Sigma_\lambda),
\]
where, setting \(s=e^{-\lambda}\),
\[
\Sigma_\lambda=
\begin{pmatrix}
 s(1-s)&\lambda s^2&s^2(1-s)+\lambda s^3\\
 \lambda s^2&s(1-s)&s^2(1-s)+\lambda s^3\\
 s^2(1-s)+\lambda s^3&s^2(1-s)+\lambda s^3&s^2(1-s^2)+2\lambda s^4
\end{pmatrix}.
\]
This matrix is positive definite, with
\[
\det(\Sigma_\lambda)=s^4(1-s)^2[1+(\lambda-1)s][1-(\lambda+1)s]>0.
\]
In particular all three distinct pairwise limiting covariances are strictly positive, and the conditional covariances divided by \(n\) converge to their corresponding entries of \(\Sigma_\lambda\). The asymptotic Gaussian vector is also independent of every fixed finite vector of directed-cycle counts in the unconditioned graph, in their joint weak limit. The claim concerns *joint* fluctuations and their covariance matrix; the individual marginal central limit theorems are prior results.

## Assumptions and scope
Arcs \(u\to v\) and \(v\to u\) are distinct, independent Bernoulli variables. A directed cycle has length at least two; a pair of opposite arcs forms a two-cycle. The acyclic law is the independent-arc law conditional on absence of all such cycles. The real parameter \(\lambda\) is fixed in \((0,1)\) while \(n\to\infty\). The centering constants are deterministic and differ by only \(O(1)\) from the exact unconditioned expectations. No conclusions at \(\lambda\ge1\), or uniform in \(\lambda\), are asserted.

## Proof
**1. Exact unconditioned moments.** Let \(q=1-p\), \(a=q^{n-1}\), \(b=q^{2(n-1)}=a^2\), and let the counts refer temporarily to the independent-arc law with arbitrary \(0<p<1\). A vertex has source and sink probabilities \(a\), and isolation probability \(b\). The incoming sets for two distinct vertices are disjoint; likewise the outgoing sets for two distinct vertices, and the incoming and outgoing sets at one vertex. For distinct vertices, the conditions “source at one, sink at the other” have precisely one forbidden arc in common, while isolation conditions at two distinct vertices have two forbidden arcs in common. Consequently
\[
\begin{aligned}
\mathbb E S_n=\mathbb E K_n&=na,&\mathbb E I_n&=nb,\\
\operatorname{Var}(S_n)=\operatorname{Var}(K_n)&=na(1-a),&
\operatorname{Cov}(S_n,K_n)&=n(n-1)pq^{2n-3},\\
\operatorname{Cov}(S_n,I_n)=\operatorname{Cov}(K_n,I_n)
 &=nb(1-a)+n(n-1)pq^{3n-4},\\
\operatorname{Var}(I_n)&=nb(1-b)+n(n-1)q^{4n-6}(1-q^2).
\end{aligned}
\]
For example, the two different-vertex isolated indicators have joint probability \(q^{4n-6}\), whereas the product of their probabilities is \(q^{4n-4}\); the other cross terms follow by the same one-arc overlap count. Substituting \(p=\lambda/n\) and dividing the covariance matrix by \(n\) gives the displayed \(\Sigma_\lambda\). The exact means differ from \(ns\) and \(ns^2\) by \(O(1)\).

**2. Unconditioned multivariate central limit theorem.** For each vertex \(v\), form the bounded, three-dimensional indicator vector \(Y_v\) recording whether it is a source, sink, or isolated. Every component is a product of absence indicators for a set of arcs, and a product of any finite collection of such components has expectation \(q^{|U|}\), where \(U\) is the union of their forbidden-arc sets. When the underlying indicators are attached to \(d\) distinct vertex labels, a forbidden-arc set belonging to one label intersects a set belonging to another at at most two arcs. Such a shared arc contributes a factor \(q^{-1}=1+O(n^{-1})\) compared with disjoint groups.

Here is the connected-cumulant argument in detail. For any fixed order \(r\), first group the \(r\) chosen component indicators by their distinct vertex labels. Their joint moments factor into within-group moments times a product of pair-group interaction factors of the form \(1+O(n^{-1})\): there are no arcs simultaneously forbidden by three distinct vertex groups. Expand these factors as \(1+h_{uv}\), with \(h_{uv}=O(n^{-1})\) uniformly in the labels. In the partition formula for their joint cumulant, all terms whose interaction graph on the \(d\) label-groups is disconnected cancel (one can equivalently apply the usual connected-graph expansion to the log of the multivariate moment-generating function). Every surviving graph has at least \(d-1\) interaction edges, so each fixed-order cumulant is \(O(n^{-(d-1)})\); constants depend only on \(r\) and \(\lambda\). This also covers repeated indicators on a single vertex by keeping their within-group moments together. In the \(r\)th cumulant of any fixed linear combination of the three vertex totals, summing over choices with \(d\) distinct vertex labels gives \(O(n^d)n^{-(d-1)}=O(n)\). Thus the centered, \(n^{-1/2}\)-normalized totals have cumulants of every fixed order \(r\ge3\) of order \(O(n^{1-r/2})\to0\); their second cumulants converge to \(\Sigma_\lambda\). The method of moments (Gaussian moments are determinate) and Cramér–Wold prove the claimed unconditioned vector convergence. The same cumulant bounds imply a uniform bound on each fixed normalized absolute even moment, including fourth moments.

**3. Cycle counts and their asymptotic decoupling.** Let \(C_{n,\ell}\) be the number of directed simple \(\ell\)-cycles in the unconditioned graph, \(\ell\ge2\). Its exact expectation is
\[
\mathbb E C_{n,\ell}=\frac{(n)_\ell}{\ell}(\lambda/n)^\ell\le\lambda^\ell/\ell.
\]
For every fixed \(L\), joint factorial moments show that \((C_{n,2},\ldots,C_{n,L})\) converges to independent Poisson variables with means \(\lambda^\ell/\ell\). Collections of vertex-disjoint cycles give the product of the means asymptotically. Collections containing overlapping, non-identical cycles use strictly more distinct arcs than distinct vertices and contribute \(O(n^{-1})\) to each fixed factorial moment.

Crucially, these Poisson limits are independent of the normalized source/sink/isolation vector. To see this without assuming independence, fix any prescribed family of mutually vertex-disjoint cycles with total arc count \(t\), where \(t\) is fixed. Condition on their arcs being present and couple with the original independent-arc graph by forcing only these \(t\) arcs. Only their at most \(t\) incident vertices can have their source/sink/isolation indicators altered; therefore each vertex count changes by at most \(t\), deterministically. After division by \(\sqrt n\) the discrepancy is at most \(t/\sqrt n\). This is uniform over cycle locations. Multiply by the exact probability \(p^t\), sum over disjoint prescribed families, and use the \(O(n^{-1})\) overlapping-family bound to factor every fixed mixed factorial moment of the cycles and each bounded continuous function of the normalized vector. Hence finite cycle-count vectors and the Gaussian vector converge jointly and independently.

**4. Conditioning away all cycles.** For \(\lambda<1\),
\[
\sup_n \mathbb E\sum_{\ell>L}C_{n,\ell}
\le\sum_{\ell>L}\frac{\lambda^\ell}{\ell}\xrightarrow[L\to\infty]{}0.
\]
The probability of no cycles of lengths at most \(L\) approaches \(\exp(-\sum_{\ell=2}^{L}\lambda^\ell/\ell)\), independently of the Gaussian limit. By the uniform tail bound, this gives both
\[
\Pr(D(n,\lambda/n)\text{ is acyclic})\longrightarrow
\exp\!\left(-\sum_{\ell\ge2}\lambda^\ell/\ell\right)
=(1-\lambda)e^\lambda>0
\]
and convergence of the Gaussian vector under conditioning on the acyclicity event, with the **same** covariance matrix. The uniform fourth-moment bound from Step 2, divided by the eventually positive acyclicity probability, yields uniform integrability of conditional squared normalized counts; thus the conditional scaled covariances also converge to the displayed matrix.

**5. Nondegeneracy.** Write \(s=e^{-\lambda}\). Direct determinant factorization yields the stated formula. Since \(0<s<1\), \(0<\lambda<1\), and \(e^\lambda>1+\lambda\), both remaining factors are positive. Likewise the first and second leading principal minors are positive: the second is \(s^2[1-(1+\lambda)s][1+(\lambda-1)s]\), so Sylvester's criterion proves positive definiteness.

## Verification
The standalone, standard-library script `verify.py` enumerates all ordered-arc subsets for \(n=2,3,4\) at three exact rational arc probabilities, and matches all nine mean/variance/covariance identities using rational arithmetic. It also tests positive definiteness and numerical convergence to the limiting covariance formula for five choices of \(\lambda\). Running `python3 verify.py` produced `VERIFY_OK 116 exact/algebraic and limit checks`. The proof of infinite-dimensional convergence, Poisson independence, and conditioning is analytic and **does not** follow from these finite computations.

## Relationship to prior work
Gessel's *Counting acyclic digraphs by sources and sinks* (1995 preprint / 1996 journal) already gives a complete **finite multivariate generating function** for the numbers of source-only, sink-only, and isolated vertices in acyclic digraphs; this subsumes finite counting and is not presented here as new. Ralaivaosaona's 2022 paper gives asymptotic normality for each of the source and isolated-vertex counts individually (and sinks by symmetry), explicitly using Gessel's multivariate generating function. Those known marginal results do **not** assert the explicit joint Gaussian law, its nonzero source–sink and isolation cross-covariances, positive-definiteness, or asymptotic independence from the short-cycle process under subcritical acyclicity conditioning. The present contribution is that joint limit and its probability-theoretic derivation. De Panafieu and Dovgal study acyclicity regimes and enumeration, not the stated three-way local-count fluctuation law. Priority beyond the inspected literature is not certified.

## Limitations
The theorem is confined to the fixed subcritical interval \(0<\lambda<1\). No convergence rate, large-deviation principle, joint local limit theorem, or extension through the critical point is proved. Finite-multivariate generating functions and separate marginal central limit theorems are established earlier results; originality is limited to the specified joint conditional fluctuation result and cross-covariance structure. This proof has received no independent mathematical audit. An earlier implicit or explicit joint limit derived elsewhere from Gessel's generating function remains a genuine historical-priority risk.

## References
1. I. M. Gessel, *Counting acyclic digraphs by sources and sinks*, preprint dated 1995; *Discrete Mathematics* 160 (1996), 253–258, https://people.brandeis.edu/~gessel/homepage/papers/acyclic.pdf, Theorem 2.
2. D. Ralaivaosaona, *The Number of Sources and Isolated Vertices in Random Directed Acyclic Graphs*, *LIPIcs AofA* 225 (2022), article 17, first publicly dated 2022-06-08, https://doi.org/10.4230/LIPIcs.AofA.2022.17, Theorems 1–2 and Lemma 3.
3. É. de Panafieu and S. Dovgal, *Counting directed acyclic and elementary digraphs*, arXiv:2001.08659, first posted 2020-01-23, https://arxiv.org/abs/2001.08659.
