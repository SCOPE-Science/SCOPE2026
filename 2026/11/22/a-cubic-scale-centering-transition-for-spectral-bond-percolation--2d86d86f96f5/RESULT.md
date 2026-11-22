# A cubic-scale centering transition for spectral bond percolation on growing clique windmills

## Finding

For each integer \(n\ge1\) and integer \(s=s_n\ge1\), form a windmill \(G_{n,s}\) by identifying one vertex \(o\) in each of \(n\) disjoint copies of \(K_{s+1}\). Thus the hub \(o\) has \(ns\) neighbours and there are \(n\) mutually disjoint peripheral cliques of order \(s\). Assume \(s=o(n)\). Set

\[
\rho_{n,s}=\frac{s-1+\sqrt{(s-1)^2+4ns}}2,\qquad
p_n=\frac{c}{\rho_{n,s}},\qquad c>0\text{ fixed},
\]

with \(n\) large enough that \(p_n\le1\). Retain every edge independently with probability \(p_n\). Let \(C_n\) be the number of vertices in the open component of \(o\), and put

\[
\mu_n=ns p_n,\qquad \sigma_n=\sqrt{ns p_n(1-p_n)}.
\]

**Theorem (sharp mesoscopic shift).** If \(s/n^{1/3}\to t\in[0,\infty)\), then

\[
\frac{C_n-1-\mu_n}{\sigma_n}\ \Longrightarrow\
\operatorname{Normal}\!\left(c^{3/2}t^{3/4},1\right).
\]

If instead \(s/n^{1/3}\to\infty\), while \(s=o(n)\) is retained, then

\[
\frac{C_n-1-\mu_n}{\sigma_n}\xrightarrow{\mathbb P}+\infty.
\]

In addition, if \(s\to\infty\), let \(A_n\) count the open edges incident to \(o\). The indirect portion \(B_n=C_n-1-A_n\) satisfies

\[
\frac{B_n}{s}\xrightarrow{\mathbb P}c^2.
\]

Thus the Gaussian centered only at the directly attached population is centered for \(s=o(n^{1/3})\), has an explicit nonzero mean shift at \(s\asymp n^{1/3}\), and escapes to the right for \(n^{1/3}\ll s\ll n\). The theorem concerns the **hub-rooted component**, not the graph's largest component or a giant-component threshold.

## Assumptions and scope

The number of peripheral cliques \(n\to\infty\), their order \(s=s_n\) is an arbitrary integer sequence satisfying \(1\le s=o(n)\), and \(c\) is a fixed positive real number. Every individual undirected edge is retained independently with one common probability. The hub exists before percolation and is always included in its open cluster. There is no assertion of a uniform limit over varying \(c\) or any claim about non-bond models. The term \(\rho_{n,s}\) is **exactly** the adjacency spectral radius of the underlying windmill, as shown next.

## Proof

**1. Spectral normalization.** On the subspace of vectors constant on all peripheral vertices, the adjacency matrix acts through the quotient

\[
\begin{pmatrix}0&ns\\1&s-1\end{pmatrix}.
\]

The positive eigenvalue is \(\rho_{n,s}\). A strictly positive eigenvector exists, so the Perron–Frobenius theorem identifies it with the graph's largest eigenvalue. As \(s=o(n)\),

\[
\rho_{n,s}/\sqrt{ns}\to1,\quad sp_n\to0,\quad ns p_n\sim c\sqrt{ns},\quad
\sigma_n\sim\sqrt c\,(ns)^{1/4}.
\]

**2. A direct–indirect decomposition.** Index the peripheral cliques by \(i\in\{1,\ldots,n\}\), and their vertices by \(u\in\{1,\ldots,s\}\). Write \(H_{iu}\) for the indicator of the open hub-to-\(u\) spoke and \(E_{iuv}=E_{ivu}\) for the indicator of an open edge within clique \(i\); all underlying edge indicators are mutually independent Bernoulli variables with parameter \(p_n\). Then

\[
A_n=\sum_{i,u}H_{iu}\sim\operatorname{Bin}(ns,p_n),\qquad
C_n=1+A_n+B_n,
\]

where \(B_n\) is the number of peripheral vertices with closed spokes nevertheless connected to the hub by a longer open path. Define the **two-step path count**

\[
Z_n=\sum_{i=1}^n\sum_{u\ne v}H_{iu}(1-H_{iv})E_{iuv}.
\]

Its exact expectation is

\[
\mathbb EZ_n=ns(s-1)p_n^2(1-p_n).
\]

Let \(B_{2,n}\) count closed-spoke vertices having at least one open two-edge path from the hub. For any such vertex \(v\), the number of these paths is \(N_v=\sum_{u\ne v}H_{iu}E_{iuv}\). Consequently \(B_{2,n}\le Z_n\), and counting pairs of paths with a common terminal vertex gives

\[
\mathbb E(Z_n-B_{2,n})\le\frac{ns(s-1)(s-2)}{2}p_n^4(1-p_n).
\]

Every vertex counted by \(B_n-B_{2,n}\) has a simple open hub path of at least three edges within its unique peripheral clique. The expected number of *all* such paths is at most

\[
 n\sum_{\ell=3}^{s}s^\ell p_n^\ell
 \le\frac{n(sp_n)^3}{1-sp_n}
\]

for all sufficiently large \(n\). Therefore

\[
\tag{1}
\mathbb E|B_n-Z_n|\le
\frac{n(sp_n)^3}{1-sp_n}+\frac{ns^3}{2}p_n^4.
\]

The independent clique contributions to \(Z_n\) are sums of ordered two-edge-path indicators. Two different indicators are independent unless their paths share an edge variable; a shared spoke in opposite roles makes their joint occurrence impossible. Every indicator has at most \(O(s)\) potentially positively covarying partners, and their joint expectations are at most \(p_n^3\) if they share an open spoke and \(p_n^4\) if they share a closed-spoke condition. Directly expanding the variance therefore gives the absolute-constant bound

\[
\tag{2}
\operatorname{Var}(Z_n)
\le ns(s-1)p_n^2+4ns^3(p_n^3+p_n^4).
\]

**3. The indirect contribution.** Under \(s=o(n)\), the right-hand side of (1) is \(O(s\sqrt{s/n})\), and (2) is \(O(s+s^{3/2}/\sqrt n)\), with constants depending on \(c\). Moreover \(\mathbb EZ_n/s\to c^2\) if \(s\to\infty\). The error in (1), divided by \(s\), tends to zero, and (2) divided by \(s^2\) tends to zero. Markov's and Chebyshev's inequalities prove

\[
B_n/s\xrightarrow{\mathbb P}c^2\qquad(s\to\infty).
\]

For arbitrary \(s=o(n)\), including bounded \(s\), the same estimates give \(\mathbb EB_n=O(s)\). Hence when \(s=o(n^{1/3})\),

\[
\frac{\mathbb EB_n}{\sigma_n}
=O\left(\left(\frac{s^3}{n}\right)^{1/4}\right)\to0,
\]

so \(B_n/\sigma_n\to0\) in probability.

**4. The limiting laws.** Since \(ns p_n\to\infty\) and \(p_n\to0\), the elementary binomial central limit theorem yields

\[
(A_n-\mu_n)/\sigma_n\Longrightarrow\operatorname{Normal}(0,1).
\]

If \(s/n^{1/3}\to t>0\), the preceding indirect-count law and

\[
\frac{s}{\sigma_n}\to\frac{t^{3/4}}{\sqrt c}
\]

imply \(B_n/\sigma_n\to c^{3/2}t^{3/4}\) in probability. If \(t=0\), the direct expectation bound instead gives a zero limit. Slutsky's theorem proves the finite-\(t\) Gaussian statement; it does not require independence of \(A_n\) and \(B_n\). If \(s/n^{1/3}\to\infty\), then \(s\to\infty\) and \(s/\sigma_n\to\infty\); combining \(B_n/s\to c^2>0\) with tightness of the standardized binomial gives the asserted divergence. This completes the proof.

## Verification

The standalone, standard-library-only `checker.py` exhaustively enumerates all bond patterns in one peripheral clique for \(1\le s\le5\), at two rational probabilities for each \(s\). Using exact `fractions.Fraction` arithmetic, it recomputes rooted clusters, verifies the path-count inequalities state by state, evaluates the exact first moments, and verifies the finite upper bound corresponding to (1). The executable reports **203236 passed assertions**. A separate numerical scale comparison of the exact two-path expectation over the binomial standard deviation confirms approach to the predicted critical shift. These checks are finite regression tests only; Steps 1–4 above prove the infinite claims.

## Relationship to prior work

Christoph, Morawski and Wigderson (2026) prove broad finite-graph spectral-scale percolation bounds and discuss irregular graphs for which the spectral radius is comparable to the square root of the maximum degree. Their bounds do not specify centered hub-component fluctuations or the \(n^{1/3}\) size transition in growing clique windmills. Allard, Hébert-Dufresne, Young and Dubé (2015) give general exact finite component recursions for clustered graphs; such a framework is consistent with the present model but does not state this asymptotic, which requires the particular two-step estimate and joint scale comparison.

Related published finite-hub bipartite percolation results establish Poisson hub connectivity and (mixed) Gaussian ordinary-vertex fluctuations when the number of hubs is fixed. Here there is one shared hub, a growing number of peripheral *cliques*, and a growing peripheral clique size. There are no random hub-merger states in this model; instead, indirect intra-clique paths produce a deterministic centering correction precisely when they reach the direct-neighbor Gaussian standard-deviation scale. General elementary binomial CLTs and short-path counting are credited as tools rather than claimed as new.

## Limitations

Only the hub-rooted component is analyzed. The theorem requires \(s=o(n)\) and fixed \(c>0\); it does not determine the largest-component distribution or establish a new percolation threshold. The large-\(s\) statement after direct-neighbor centering diverges, rather than providing a different centered limit. The exact finite-graph formulas of earlier general percolation theories could, after nontrivial asymptotic analysis, yield the same conclusion; the novelty comparison is based on inspected published statements and is not independently certified.

## References

1. M. Christoph, P. Morawski and Y. Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145, first publicly posted 2026-08-19, https://arxiv.org/abs/2608.19145 (especially Introduction, Theorems 1.3–1.4 and Section 3).
2. A. Allard, L. Hébert-Dufresne, J.-G. Young and L. J. Dubé, *General and exact approach to percolation on random graphs*, arXiv:1509.01207, first publicly posted 2015-09-03, https://arxiv.org/abs/1509.01207 (Section II, finite clustered-graph recursions).
3. *Poisson multigraph coalescence and cycle surplus at the finite-hub percolation threshold*, published published-finding corpus finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-poisson-multigraph-coalescence-and-cycle-surplus-at-the-finite-h--df9adda72dcf.
4. *Poisson hub connectivity and mixed-Gaussian outbreak fluctuations in bipartite bond percolation*, published published-finding corpus finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-poisson-hub-connectivity-and-mixed-gaussian-outbreak-fluctuation--1b8b0b0e5eb8.
