# Hyperuniform age-block indegrees and the two-boundary law for exponential attachment

## Finding
For the exponentially age-preferential growth multigraph with a fixed positive integer \(m\) of independently sampled parents at every birth and fixed \(q=e^{-\beta}\in(0,1)\), let \(X_j\) be the **lifetime** number of edges received by vertex \(j\) from later vertices, counting parallel edges. For integers \(k\ge0\) and \(L\ge1\), define the centered block indegree
\[
B_{k,L}=\sum_{j=k+1}^{k+L}(X_j-m).
\]
Let \(Z\) and \(Z'\) be independent copies of the almost surely finite random variable
\[
Z=m+\sum_{h=1}^{\infty}\sum_{a=1}^{m}\xi_{h,a},
\qquad \Pr(\xi_{h,a}=1)=q^h,
\]
where all Bernoulli variables are independent. Then, **uniformly for every \(k,L\)**,
\[
\boxed{d_{\mathrm{TV}}\!\left(\mathcal L(B_{k,L}),\mathcal L(Z'-Z)\right)
\le\frac{m q^{k+1}+2m q^L}{1-q}.}
\]
Consequently, as \(k\to\infty\) and \(L\to\infty\) in any joint fashion, the block excess converges in total variation to a symmetric, nondegenerate, non-Gaussian integer-valued law with characteristic function
\[
\boxed{\mathbb E e^{it(Z'-Z)}
=\prod_{h=1}^{\infty}\left|1-q^h+q^h e^{it}\right|^{2m},\quad
\operatorname{Var}(Z'-Z)=\frac{2m q}{1-q^2}.}
\]
This is **bounded block fluctuation rather than a square-root-block central limit theorem**, even though individual lifetime indegrees are random. More precisely, the stationary bulk indegree field \((X_j^*)_{j\in\mathbb Z}\) has covariance
\[
\gamma(0)=\frac{2m q}{1+q},\qquad
\gamma(d)=-\frac{m(1-q)q^{|d|}}{1+q}\quad(d\ne0),
\]
so that the exact stationary block variance and spectral density (Fourier convention \(S(\theta)=\sum_{d\in\mathbb Z}\gamma(d)e^{id\theta}\)) are
\[
\boxed{\operatorname{Var}\!\left(\sum_{j=1}^{L}(X_j^*-m)\right)
=\frac{2m q(1-q^L)}{1-q^2},\qquad
S(\theta)=\frac{2m q(1-\cos\theta)}{1-2q\cos\theta+q^2}.}
\]
In particular, \(S(\theta)\sim m q\theta^2/(1-q)^2\) as \(\theta\to0\): a quadratic spectral zero (hyperuniformity).

## Assumptions and scope
Start with vertex \(v_0\). At each time \(n\ge1\), vertex \(v_n\) makes exactly \(m\) independent parent choices among \(v_0,\ldots,v_{n-1}\), with
\[
\Pr(\text{parent at birth }n\text{ is }v_j)
=\frac{(1-q)q^{n-1-j}}{1-q^n},\qquad0\le j<n.
\]
All choices over all times are independent. Parallel edges are retained **with multiplicity**. An edge is oriented toward the older vertex only to define incoming edge multiplicity; the underlying graph may be viewed as undirected. Lifetime incoming degree \(X_j\) counts edges from all later births, not just those seen at a finite terminal time. It is finite almost surely since the sum of its edge probabilities is finite. The origin \(v_0\) is excluded from the observed blocks, and both \(m\) and \(q\) stay fixed. The result does not concern the simple-graph degree after merging parallel edges.

## Proof
**1. Stationary construction and quantitative coupling.** Introduce, independently for each integer source \(n\in\mathbb Z\) and each parent-choice label \(a\in\{1,\ldots,m\}\), a geometric lag \(G_{n,a}\) with
\[
\Pr(G_{n,a}=h)=(1-q)q^{h-1},\quad h\ge1.
\]
The edge from \(n\) points to \(n-G_{n,a}\). Define \(X_j^*\) to be the number of incoming edges to \(j\) from all sources \(n>j\). The field is stationary and every \(X_j^*\) is almost surely finite. At a positive birth time \(n\), the original model's lag distribution is exactly \(G_{n,a}\) conditional on \(G_{n,a}\le n\). Maximally couple each original lag with its stationary lag; a disagreement has probability \(\Pr(G_{n,a}>n)=q^n\). Since the block count depends only on choices from source times \(n\ge k+1\), the union bound over all such sources yields
\[
 d_{\mathrm{TV}}\left(\mathcal L(B_{k,L}),
 \mathcal L(B^*_{k,L})\right)
 \le \sum_{n=k+1}^{\infty} m q^n
 =\frac{m q^{k+1}}{1-q},
\]
where \(B^*_{k,L}=\sum_{j=k+1}^{k+L}(X_j^*-m)\). Stationarity makes its distribution independent of \(k\).

**2. Boundary conservation and independent crossings.** Work with the stationary block \(\{1,\ldots,L\}\). Exactly \(mL\) edges originate inside it. Let \(O_L\) count those directed outside to nonpositive indices; let \(I_L\) count edges from sources at indices greater than \(L\) that land inside the block. Deterministically,
\[
 B^*_{0,L}=I_L-O_L.
\]
The two counts use disjoint sets of independent source choices, so they are independent. For the edge choices at source \(t\in\{1,\ldots,L\}\), the probability to cross the left boundary is \(q^{t-1}\). For source \(L+s\) with \(s\ge1\), the probability to land in the block is \(q^{s-1}(1-q^L)\). Consequently,
\[
 O_L\ \overset d=\ \sum_{t=1}^{L}\operatorname{Bin}(m,q^{t-1}),\qquad
 I_L\ \overset d=\ \sum_{s=1}^{\infty}
 \operatorname{Bin}(m,q^{s-1}(1-q^L)),
\]
with all binomial summands mutually independent. The infinite sums are a.s. finite.

**3. Two independent limiting boundary fluxes.** With independent Bernoulli summands on a common space, the missing tail in \(O_L\) relative to \(Z\) has mean \(m q^L/(1-q)\), so
\[
 d_{\mathrm{TV}}(\mathcal L(O_L),\mathcal L(Z))\le m q^L/(1-q).
\]
For each source \(s\), couple the success probabilities \(q^{s-1}(1-q^L)\) and \(q^{s-1}\) with a common uniform random variable. The probability of any discrepancy is at most their total difference, \(m q^L/(1-q)\). Hence an independent copy \(Z'\) satisfies
\[
 d_{\mathrm{TV}}(\mathcal L(I_L),\mathcal L(Z'))\le m q^L/(1-q).
\]
Apply the triangle inequality and the initial coupling to obtain the stated uniform total-variation estimate. Independence produces the product characteristic function. Since \(\sum_{h\ge1}q^h(1-q^h)=q/(1-q^2)\), each boundary has variance \(m q/(1-q^2)\). This proves symmetry, variance, and the nondegenerate discrete non-Gaussian limit.

**4. Exact covariance and spectral cancellation.** Write \(p_h=(1-q)q^{h-1}\). At a fixed source, the indicators of choosing two *different* targets are mutually exclusive, while different sources and different edge-choice labels are independent. It follows that
\[
 \operatorname{Var}(X_0^*)=m\sum_{h\ge1}p_h(1-p_h)
 =\frac{2m q}{1+q},
\]
and, for every \(d\ge1\),
\[
 \operatorname{Cov}(X_0^*,X_d^*)
 =-m\sum_{h\ge1}p_h p_{h+d}
 =-\frac{m(1-q)q^d}{1+q}.
\]
The sequence is absolutely summable. Expanding the variance of the \(L\)-term sum, or equivalently adding the independent boundary variances in Step 2, yields exactly \(2m q(1-q^L)/(1-q^2)\). Summing the geometric covariance Fourier series gives
\[
 \gamma(0)+2\sum_{d\ge1}\gamma(d)\cos(d\theta)
 =\frac{2m q(1-\cos\theta)}{1-2q\cos\theta+q^2}.
\]
The denominator tends to \((1-q)^2\), and \(2(1-\cos\theta)\sim\theta^2\). This completes the proof.

## Verification
`checker.py` is a standalone Python 3 exact-rational checker. It tests the Bernoulli crossing probabilities, the covariance and finite-block variance identities for multiple rational \(q\) and integer \(m\), independently enumerates finite parent histories to check edge-flow conservation, and compares finite convolutions of the crossing probabilities to the exact means and variance-tail inequalities. It completed **17,174 exact-rational assertions**. Finite computation verifies the finite algebra and definitions; the infinite products, couplings, total-variation bounds, and asymptotic spectral limit follow from the analytical proof rather than enumeration.

## Relationship to prior work
Tang, Wang and Wu, *Random Walk on age-preferential random growth processes* (arXiv:2611.02329, first public November 2, 2026), define the **same multigraph** and prove almost-sure recurrence and infinitely many collisions of independent walks. Their whole accessible preprint's introduction, model, recurrence and collision arguments were examined. Their terminal-cut and renewal structures do not determine the full distribution of a long **bulk** block's signed incoming-degree excess, the exact covariance kernel, or its quadratic spectral zero. All model definitions are credited.

Aguech, Mahmoud, Mohamed and Yang, *Exponentially preferential trees* (published April 14, 2025), introduce the one-parent exponential-label model and analyze one-vertex outdegree means, distributional phases, and approximations. Their accessible HTML sections on model generation and node outdegrees do not present a two-sided **block indegree** flux limit or the spectral-density cancellation. The present statement includes their one-parent model as \(m=1\) but concerns an intrinsically cross-vertex observable.

Related published analyses of the same geometric-age multigraph establish almost-sure maximal degree of order \(\sqrt{\log n}\), while another establishes finite motifs and transitivity optima for a simple-graph projection; these give different observables and do not imply a bounded signed block-indegree limit. A related one-parent analysis proves a Gaussian leaf-count limit with summably negative covariances, rather than this indegree hyperuniformity. The stationary lag coupling and conservation-of-outflow are standard mechanisms, but neither alone determines the quantitative error, boundary law, covariance function and spectral cancellation jointly. Broader perturbed-lattice results already establish hyperuniformity for independent displacements with finite moments, and Flimmel (2025/2026) gives a general structure-factor framework. Thus **hyperuniformity by itself is not claimed as novel**; the specifically claimed new contribution is the sharp quantitative two-boundary **total-variation law for the finite-start age-preferential graph**, together with its explicitly evaluated Poisson-binomial law and exact model-specific kernel. General statements about hyperuniformity do not give the displayed finite-start total-variation bound or the joint two-boundary law merely by specialization. Mastrilli (2025) treats smooth rapidly decaying linear statistics, rather than sharp indicator-window counts or the growing multigraph’s finite-start correction. Related sharp-count statements from general perturbed-lattice literature are a residual priority risk.

## Limitations
The result fixes \(m\ge1\), \(\beta>0\) and takes the joint bulk/length limit \(k,L\to\infty\); it makes no assertion that \(k\) can remain fixed, or that parameters may vary with the block length. The stationary covariance and spectral identities are exact for the **stationary comparison field**, not falsely asserted as exact at the growing graph's initial boundary. No independent review or exhaustive historical-priority verification has been performed. The statistic counts parallel edges with multiplicity and requires infinite-time completed degrees. The non-Gaussian limit is at fixed parameters; other regimes may have Gaussian behavior.

## References
1. J.-s. Tang, F. Wang, X.-Y. Wu, *Random Walk on age-preferential random growth processes*, arXiv:2611.02329 (first public 2026-11-02), https://arxiv.org/abs/2611.02329.
2. R. Aguech, H. Mahmoud, H. Mohamed, Z. Yang, *Exponentially preferential trees*, Network Science 13 (2025), e5, published online 2025-04-14, https://doi.org/10.1017/nws.2025.3.
3. *Sharp square-root-logarithmic maximum degree under geometric age preference*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-square-root-logarithmic-maximum-degree-under-geometric-age--1c921c4fc033.
4. *Functional Gaussian leaf fluctuations in exponentially age-biased recursive trees*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-functional-gaussian-leaf-fluctuations-in-exponentially-age-biase--c7cff8a9c92e.
5. *Exact triangle and transitivity optima in exponentially age-preferential random graphs*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-triangle-and-transitivity-optima-in-exponentially-age-pref--027a95dadcb2.
6. D. Flimmel, *Fitting regular point patterns with a hyperuniform perturbed lattice*, arXiv:2503.12179 (first posted 2025-03-15), https://arxiv.org/abs/2503.12179 (general hyperuniformity and structure-factor framework, not this explicit finite-start TV law).
7. D. Dereudre, D. Flimmel, M. Huesmann, T. Leblé, *(Non)-hyperuniformity of perturbed lattices*, arXiv:2405.19881 (2024), https://arxiv.org/abs/2405.19881 (general displacement-hyperuniformity coverage).
8. G. Mastrilli, *Asymptotic fluctuations of smooth linear statistics of independently perturbed lattices*, arXiv:2503.02627 (2025), https://arxiv.org/abs/2503.02627 (smooth linear statistics, unlike sharp interval counts).
9. P. Gracar, A. Grauer, L. Lüchtrath, P. Mörters, *The age-dependent random connection model*, arXiv:1810.03429 (2018), https://arxiv.org/abs/1810.03429 (spatial, nonidentical growth mechanism).
