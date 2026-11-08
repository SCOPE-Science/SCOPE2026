# Gaussian stationary-occupation fluctuations detect antisymmetric disorder on dense networks

## Finding
For a complete continuous-time jump network with exchangeable random rate pairs, the first nontrivial finite-size stationary occupation variance depends on **edge nonreciprocity**, not on the marginal rate variance alone. Write \(A=X-X'\), \(\mu=\mathbb E X\), and \(v=\mathbb E A^2\). Every fixed collection of sites has asymptotically independent Gaussian occupation errors,
\[
(n^{3/2}(\pi_i-1/n))_{i=1}^k\Longrightarrow\mathcal N_k(0,(v/\mu^2)I_k),
\]
while the empirical law of these rescaled errors converges weakly in probability to \(\mathcal N(0,v/\mu^2)\). The simultaneous global statement is
\[
 n^2\sum_{i=1}^n(\pi_i-1/n)^2\xrightarrow{\mathbb P}v/\mu^2.
\]
If \(v=0\), the stationary distribution is exactly uniform at every size. These conclusions are joint consequences of the same leading perturbation formula.

## Assumptions and scope
For each integer \(n\ge2\), form a complete directed rate matrix. Unordered edge pairs \(\{(X_{ij},X_{ji}):i<j\}\) are independent identically distributed; each pair is exchangeable, \((X,X')\stackrel d=(X',X)\), and there are deterministic constants \(0<c<C<\infty\) such that \(c\le X,X'\le C\) almost surely. Edges belonging to one pair need not be independent. Let \(\mu=\mathbb E X\), \(v=\mathbb E (X-X')^2\). Set \(W_{ij}=X_{ij}\) when \(i\ne j\), and \(W_{jj}=-\sum_{i\ne j}X_{ij}\), so columns sum to zero. Strictly positive rates make \(W\) irreducible; its unique stationary probability column \(\pi\) obeys \(W\pi=0\) and \(\boldsymbol1^{\mathsf T}\pi=1\). All limits refer to randomness in the edge pairs as \(n\to\infty\), not to long-time fluctuations of one trajectory. No energetic vertex factors are present; this is the equal-energy specialization of the dense-disorder model of Calvert [1].

## Proof
**1. Exact centered balance identity.** Put \(u=\boldsymbol1/n\) and \(\delta=\pi-u\), with \(\boldsymbol1^{\mathsf T}\delta=0\). Write
\[
 W=\mu(\boldsymbol1\boldsymbol1^{\mathsf T}-nI)+B,
 \quad B_{ij}=X_{ij}-\mu\;(i\ne j),\quad
 B_{jj}=-\sum_{i\ne j}(X_{ij}-\mu).
\]
Then \(\boldsymbol1^{\mathsf T}B=0\). The imbalance vector \(s=B\boldsymbol1\) has components
\[
s_i=\sum_{j\ne i}(X_{ij}-X_{ji}),\qquad \sum_i s_i=0.
\]
Stationarity yields \(0=-\mu n\delta+B\delta+s/n\), and hence the *exact* identity
\[
\delta=\frac{s}{\mu n^2}+r,
\qquad r=\frac{B\delta}{\mu n}.
\tag{1}
\]
In particular, the first correction uses the difference between total incoming and outgoing rates, rather than either total alone.

**2. Uniform operator control.** For each unordered \(\{i,j\}\), form its contribution to \(B\): the only nonzero entries, in the \(i,j\) rows and columns, are \(-Y_{ji},Y_{ij};Y_{ji},-Y_{ij}\), where \(Y_{ij}=X_{ij}-\mu\). These independent, mean-zero non-selfadjoint matrices have norm bounded by a constant depending on \(C\); both matrix variance parameters \(\|\sum\mathbb E M_{ij}M_{ij}^{\mathsf T}\|\) and \(\|\sum\mathbb E M_{ij}^{\mathsf T}M_{ij}\|\) are \(O(n)\) because at most \(n-1\) edge pairs meet each vertex. The rectangular matrix Bernstein inequality [4] therefore gives
\[
\|B\|_2=O_{\mathbb P}(\sqrt{n\log n}).
\tag{2}
\]
Independence across unordered pairs and exchangeability imply
\(\mathbb E\|s\|_2^2=n(n-1)v\), whence \(\|s\|_2=O_{\mathbb P}(n)\). With probability tending to one, \(\|B\|_2\le\mu n/2\). Thus stationarity and the Neumann estimate from (1) give
\[
\|\delta\|_2\le\frac{2\|s\|_2}{\mu n^2}=O_{\mathbb P}(n^{-1}),\quad
\|r\|_2=O_{\mathbb P}(\sqrt{\log n}\,n^{-3/2}).
\tag{3}
\]
All estimates hold also for \(v=0\); the exact equality case is handled in Step 5.

**3. Fixed-coordinate Gaussian law.** For every fixed \(k\), split
\(s_i=\sum_{j>k}(X_{ij}-X_{ji})+\sum_{1\le j\le k,j\ne i}(X_{ij}-X_{ji})\) for \(1\le i\le k\). The first sums are independent across different \(i\) and contain \(n-k\) bounded, centered, independent summands of variance \(v\); the second sums are bounded by constants depending only on \(k\). The classical multivariate central limit theorem therefore gives
\[
(s_i/\sqrt n)_{i=1}^k\Longrightarrow\mathcal N_k(0,vI_k).
\tag{4}
\]
By invariance under permutations of vertex labels, the joint law of \(r\) is exchangeable. For each fixed \(i\), \(n^3r_i^2\to0\) in probability: indeed, on an event where \(n^3\|r\|_2^2\le K^2\log n\), symmetry and Markov's inequality bound the probability that \(n^{3/2}|r_i|>\varepsilon\) by \(K^2\log n/(n\varepsilon^2)\); the exceptional probability can be made arbitrarily small using (3). Applying (1) and Slutsky's theorem to (4) yields the claimed independent Gaussian limits.

**4. Empirical and global laws.** Fix any bounded continuous function \(f\). By exchangeability and the jointly independent Gaussian limits for one and two coordinates, the first moment of \(n^{-1}\sum_i f(n^{3/2}\delta_i)\) tends to \(\mathbb E f(Z)\), and its variance tends to zero, where \(Z\sim\mathcal N(0,v/\mu^2)\). This proves empirical weak convergence in probability (for example, first take a countable convergence-determining family of bounded Lipschitz test functions). For the global squared norm, let \(A_{ij}=X_{ij}-X_{ji}\). Independence between unordered pairs gives \(\mathbb E s_i^2=(n-1)v\) and \(\operatorname{Var}(s_i^2)=O(n^2)\), since the fourth moments are bounded. For distinct \(i,j\), separate the shared pair: \(s_i=U+A_{ij}\), \(s_j=V-A_{ij}\), where \(U,V,A_{ij}\) are mutually independent, centered. Then
\[
\operatorname{Cov}(s_i^2,s_j^2)
=\mathbb E A_{ij}^4-v^2=\operatorname{Var}(A_{ij}^2)=O(1).
\]
Consequently \(\operatorname{Var}(n^{-2}\sum_i s_i^2)=O(1/n)\) and
\[
 \frac{1}{n^2}\sum_i s_i^2\xrightarrow{L^2}v.
\tag{5}
\]
From (1), (3), and Cauchy--Schwarz,
\[
 n^2\Big|\|\delta\|_2^2-\|s/(\mu n^2)\|_2^2\Big|
 \le n^2\|r\|_2\big(2\|s\|_2/(\mu n^2)+\|r\|_2\big)
 =O_{\mathbb P}(\sqrt{\log n/n})\to0.
\]
Combining with (5) gives the global susceptibility limit.

**5. Exact equilibrium boundary and distinct nonequilibrium ensembles.** If \(v=0\), then \(X_{ij}=X_{ji}\) for every pair almost surely. \(W\) is symmetric, and its unique stationary distribution is exactly \(u\). Conversely, if \(v>0\), the nondegenerate Gaussian limit and positive global susceptibility quantify the stationary response to asymmetric disorder.

As a concrete example, choose both directed rates marginally uniform on \(\{1,3\}\). When they are equal within a pair, \(v/\mu^2=0\). When the two rates are independent, \(v/\mu^2=1/2\). When they sum to four within each pair, \(v/\mu^2=1\). Hence even the *same marginal rate distribution* and same leading uniform occupation can hide three sharply distinct occupation-fluctuation laws.

## Verification
The standalone standard-library program `verify.py` constructs independent rate ensembles and solves \(W\pi=0\) directly by pivoted elimination. It checks normalization, positivity, stationary residuals, the exact identity (1), all three pair-coupling mechanisms, and finite-size susceptibility/linearization diagnostics for sizes \(12,24,48,72\), eight samples per size and coupling. The numerical verifier passes 96 independent generator instances. In additional exploratory computations (not required by the program), systems of size up to 480 produced susceptibility near the three predicted limits. These finite calculations are consistency checks, not proofs of (2), (4), or the infinite-size statements.

## Relationship to prior work
Calvert [1, Sections II--III and Appendix C] establishes asymptotically Boltzmann-like stationary occupation and a uniform finite-size error rate on dense edge-paired random networks, as well as qualitative comparisons between symmetric and asymmetric disorder. Neither their stated convergence result nor their numerical fluctuation plots supplies the exact \(n^{3/2}\)-scaled multivariate Gaussian law or the limiting normalized squared occupation deviation here. The earlier i.i.d.-rate theorem of Calvert, den Hollander and Randall [2, Theorem 1.1] concerns total-variation asymptotic uniformity and a local exit-rate proxy. Bordenave, Caputo and Chafaï [3, Theorem 1.7 and Section 6] prove uniform stationary occupation estimates in an i.i.d. random-generator model; their spectral and invariant-measure results do not state this pair-correlation-sensitive Gaussian/susceptibility limit. Their perturbative resolvent framework is related to Step 1. Matrix Bernstein [4] supplies the standard concentration step. General prior perturbation theorems may encompass ingredients of the proof; none of these comparisons proves publication uniqueness.

## Limitations
The theorem is for a complete network, equal energetic vertex factors, bounded strictly positive rates, independent unordered pairs, and pair exchangeability. It concerns the distribution across quenched network realizations, not time-series central limits. No result is claimed for unbounded heavy-tailed rates, sparse regimes, nonexchangeable directed pairs, or varying vertex energies. The Gaussian law is degenerate in the exactly symmetric case. Potential broader unlocated random Perron-vector or stationary-measure central-limit results remain a publication-priority risk; an independent scientific audit has not been performed.

## References
[1] J. Calvert, *Boltzmann-like occupation of nonequilibrium steady states on dense disordered networks*, arXiv:2606.14542 (first posted 12 June 2026), https://arxiv.org/abs/2606.14542 and https://arxiv.org/html/2606.14542v2.

[2] J. Calvert, F. den Hollander and D. Randall, *A note on the asymptotic uniformity of Markov chains with random rates*, arXiv:2505.01608 (2025), https://arxiv.org/abs/2505.01608.

[3] C. Bordenave, P. Caputo and D. Chafaï, *Spectrum of Markov generators on sparse random graphs*, arXiv:1202.0644 (2012; journal 2014), https://arxiv.org/abs/1202.0644.

[4] J. A. Tropp, *User-friendly tail bounds for sums of random matrices*, arXiv:1004.4389 (2010; journal 2012), https://arxiv.org/abs/1004.4389.
