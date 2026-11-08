# Edge-conditioned graphon limit for uniform sequential attachment

## Finding
For every fixed \(\rho\in(0,1/2)\) and every integer sequence \(m_n\in\{0,\ldots,n(n-1)/2\}\) with \(m_n/n^2\to\rho\), consider the uniform sequential-attachment random graph \(G_n\) conditioned on having exactly \(m_n\) edges. Its age-and-attachment-propensity empirical measure converges in probability to an explicitly tilted measure, and its graphon converges in probability to a corresponding **age-dependent** graphon. For orientation, the scalar edge-count distribution has the classical Mahonian inversion-count law and a corresponding large-deviation exponent at speed \(n\); this scalar exponent is not asserted as new.

For \(a\in\mathbb R\), put
\[
Z(a)=\int_0^1e^{au}\,du,\quad h(a)=\frac{Z'(a)}{Z(a)},\quad \Lambda(\theta)=\int_0^1\log Z(\theta x)\,dx.
\]
There is a unique \(\theta=\theta(\rho)\in\mathbb R\) satisfying
\[
\rho=\Lambda'(\theta)=\int_0^1 xh(\theta x)\,dx.
\]
On \(S=[0,1]^2\), with coordinates \((x,u)\) for age and attachment propensity, define
\[
\mu_\theta(dx,du)=dx\,\frac{e^{\theta xu}}{Z(\theta x)}\,du,
\qquad W((x,u),(y,v))=\begin{cases}u,&x>y,\\v,&y>x.\end{cases}
\]
The diagonal \(x=y\) may be assigned any value. For every fixed finite simple graph \(F\),
\[
t(F,G_n)\ \xrightarrow[\,n\to\infty\,]{\mathbb P(\,\cdot\mid |E(G_n)|=m_n)}\ t(F,W;\mu_\theta).
\]
Equivalently the unlabelled graphs converge in probability in dense-graph cut distance to the indicated graphon. For the same integer sequences,
\[
\lim_{n\to\infty}\frac1n\log \mathbb P(|E(G_n)|=m_n)=-I(\rho),\qquad
I(\rho)=\theta\rho-\Lambda(\theta).
\]
In particular \(\theta=0\) corresponds to \(\rho=1/4\); otherwise the limiting propensity law varies with vertex age and is not the unconditioned uniform propensity law.

## Assumptions and scope
For each \(n\ge2\), construct the graph on vertices \(1,\ldots,n\) as follows. At each arrival \(j\in\{2,\ldots,n\}\), independently choose \(K_j\) uniformly from \(\{0,1,\ldots,j-1\}\) and then choose, uniformly without replacement, precisely \(K_j\) older vertices as neighbours. All random choices are independent across arrivals. Thus \(M_n:=|E(G_n)|=\sum_{j=2}^nK_j\). Every admissible exact edge count has positive probability. This is the uniform sequential-attachment construction, not a fixed-outdegree or preferential-attachment graph.

The condition \(m_n/n^2\to\rho\in(0,1/2)\) imposes no rate or divisibility restriction. Limits do not assert convergence for the endpoints \(\rho=0\) or \(\rho=1/2\), when the speed and normalizations can change. The primary statement concerns each fixed test graph \(F\), not growing subgraphs, local neighborhoods, or a quantitative rate in cut distance.

For \(j\ge2\), let \(U_j=K_j/(j-1)\). The stronger marked empirical statement is
\[
\frac1n\sum_{j=2}^n\delta_{(j/n,U_j)}\ \xrightarrow{\mathbb P(\,\cdot\mid M_n=m_n)}\ \mu_\theta
\]
weakly as finite measures; the omitted initial vertex has asymptotically zero mass.

## Proof
**1. Exponential tilting and the unique parameter.** Set \(Z_{j,n}(\eta)=j^{-1}\sum_{k=0}^{j-1}e^{\eta k/n}\). Under a tilted measure \(\mathbb Q_{\eta,n}\), the \(K_j\) remain independent with
\[
\mathbb Q_{\eta,n}(K_j=k)=\frac{e^{\eta k/n}}{jZ_{j,n}(\eta)}
\qquad(0\le k<j).
\]
For every \(\eta\) and every allowed \(m\), conditional measures agree exactly:
\[
\mathbb P(\,\cdot\mid M_n=m)=\mathbb Q_{\eta,n}(\,\cdot\mid M_n=m).
\]
The conditional neighbour selection laws are unaffected. Write \(\rho_n=m_n/n^2\). For sufficiently large \(n\), there is a unique \(\eta_n\) for which \(\mathbb E_{\mathbb Q_{\eta_n,n}}M_n=m_n\), because that expectation is a strictly increasing continuous function of \(\eta\), ranging from \(0\) to \(n(n-1)/2\).

Uniform Riemann-sum convergence on compact parameter sets gives
\[
\frac1n\sum_{j=2}^n\log Z_{j,n}(\eta)\to\Lambda(\eta),
\qquad \frac1{n^2}\mathbb E_{\mathbb Q_{\eta,n}}M_n\to\Lambda'(\eta).
\]
Here \(Z_{j,n}(\eta)\) is a discrete approximation to \(Z(\eta j/n)\), with negligible boundary indices. Since \(\Lambda''(\eta)=\int_0^1 x^2\operatorname{Var}_{\eta x}(U)\,dx>0\), and \(\Lambda'(\eta)\) ranges strictly from \(0\) to \(1/2\), the unique \(\eta_n\) tends to the specified \(\theta\).

**2. A lattice local limit bound.** Under \(\mathbb Q_{\eta_n,n}\), independence and Riemann sums imply
\[
\operatorname{Var}(M_n)/n^3\to v_\theta:=\int_0^1x^2\operatorname{Var}_{\theta x}(U)\,dx>0,
\]
where \(U\) has density \(e^{au}/Z(a)\) on \([0,1]\) under \(\operatorname{Var}_{a}\). Moreover,
\[
\mathbb Q_{\eta_n,n}(M_n=m_n)=\frac{1+o(1)}{\sqrt{2\pi v_\theta n^3}}.
\]
For completeness, here is a Fourier justification. For \(j\in[\lceil n/2\rceil,n]\), the tilted mass function is a truncated geometric progression with ratio \(e^{\eta_n/n}\). Its characteristic function, after centering, has modulus \(\le e^{-cj^2t^2}\) for \(|t|\le\delta/n\), because differences of two independent copies have variance uniformly comparable to \(j^2\) and \(1-\cos z\ge c'z^2\) on a fixed small interval. For \(\delta/n\le |t|\le C/n\), scaled characteristic functions converge uniformly (for \(j/n\in[1/2,1]\) and bounded \(\eta_n\)) to characteristic functions of nondegenerate absolutely continuous tilted uniform laws; on this compact set their moduli are uniformly less than one. For \(C/n\le |t|\le\pi\), the finite-geometric-series formula yields modulus \(\le C_1/(j|\sin(t/2)|)\); choosing \(C\) large makes this uniformly less than one. Thus all Fourier modes outside \(O(n^{-3/2})\) make a negligible contribution to the inversion integral. In the central window \(t=O(n^{-3/2})\), a Taylor expansion of the logarithms of the characteristic functions is Gaussian, since \(\sum_{j=2}^n\mathbb E|K_j-\mathbb E K_j|^3=O(n^4)\), making the total third-order remainder \(O(n^{-1/2})\). Fourier inversion and the preceding variance limit give the displayed lattice local limit at the mean \(m_n\). In particular this event has probability at least \(c_\theta n^{-3/2}\) for all large \(n\).

**3. Conditional marked empirical measure.** For every bounded continuous \(f\) on \(S\), the tilted variables \(f(j/n,U_j)\) are independent, bounded, and have expectations whose averages converge by Riemann summation to \(\int f\,d\mu_\theta\). Hoeffding's inequality gives an exponentially small probability of a fixed positive deviation. Conditioning on \(M_n=m_n\) multiplies this upper bound by at most \(O(n^{3/2})\), by Step 2. This proves convergence of integrals of bounded continuous \(f\). A countable determining class gives the asserted weak convergence in probability.

**4. Edges and homomorphism densities.** Conditional on all \(K_j\), take independent uniform \([0,1]\) priorities \(T_{ij}\) for every \(i<j\). Choose the \(K_j\) smallest among \(\{T_{ij}:i<j\}\) to form the required neighbours. On the same space form an auxiliary graph \(H_n\) using an edge \(\{i,j\}\), \(i<j\), whenever \(T_{ij}\le U_j\). Conditional on the marks, edges of \(H_n\) are independent with probabilities \(U_j\). In column \(j\), the number of differing edges is exactly \(|\operatorname{Binomial}(j-1,U_j)-K_j|\), whose conditional expectation is at most \(\sqrt{j-1}\). Hence the expected total symmetric difference of edge sets is \(O(n^{3/2})\), uniformly over the marks and under the exact-edge conditioning. By Markov's inequality it is \(o_\mathbb P(n^2)\). For a fixed \(F\), changing one edge affects at most \(2|E(F)|n^{|V(F)|-2}\) homomorphism maps, so \(|t(F,G_n)-t(F,H_n)|=o_\mathbb P(1)\).

Given the marks, \(H_n\) has independent edges. Distinct homomorphism terms have covariance zero unless their images share an unordered pair of vertices, apart from the \(O(1/n)\) fraction of noninjective maps. It follows that \(\operatorname{Var}(t(F,H_n)\mid U_2,\ldots,U_n)=O_F(n^{-2})\) with the harmless noninjective contribution handled deterministically. Its conditional mean differs by \(O_F(1/n)\) from \(t(F,W;\nu_n)\), where \(\nu_n=n^{-1}\sum_{j=1}^n\delta_{(j/n,U_j)}\), with an arbitrary initial mark. The only discontinuities of \(W\) are at equal age coordinates, a set of \(\mu_\theta^{\otimes2}\)-measure zero. The marked empirical convergence from Step 3 therefore implies \(t(F,W;\nu_n)\to t(F,W;\mu_\theta)\) in probability. This proves convergence of all fixed-graph homomorphism densities, hence the claimed graphon limit.

**5. Mahonian scalar-rate identity (background, not a novelty claim).** The original and tilted masses at \(M_n=m_n\) satisfy the exact likelihood-ratio identity
\[
\mathbb P(M_n=m_n)=e^{-\eta_nm_n/n}\Bigl(\prod_{j=2}^n Z_{j,n}(\eta_n)\Bigr)\mathbb Q_{\eta_n,n}(M_n=m_n).
\]
Taking logarithms, dividing by \(n\), and applying Steps 1 and 2 proves \(-\theta\rho+\Lambda(\theta)=-I(\rho)\).

## Verification
The standalone file `verify.py` checks the finite exact convolution formula for \(M_n\), complement symmetry, exact moments, tilt-conditioning invariance, coupling moment bounds and numerical properties of the limiting cumulant function. Run with `python verify.py` using Python's standard library. All claims about unbounded \(n\), graphon convergence and the large-deviation exponent are justified by the analytic proof above; finite checks are not substituted for that proof.

Two consistency consequences of the limit are \(t(K_2,W;\mu_\theta)=2\rho\) and
\[
t(K_3,W;\mu_\theta)=6\int_{0<b<c<1}b\,h(\theta b)\,\frac{Z''(\theta c)}{Z(\theta c)}\,db\,dc.
\]
At \(\theta=0\), these give \(t(K_2)=1/2\) and \(t(K_3)=1/6\), rather than the Erdős--Rényi triangle density \(1/8\) at the same edge density.

## Relationship to prior work
The outdegree vector \(K_2,\ldots,K_n\) has exactly the distribution of the independent inversion-table coordinates of a uniform permutation. Consequently \(M_n\) is a classical Mahonian inversion count; inversion-count generating functions, Mallows exponential tilting and scalar large deviations are established subjects and are **not claimed as novel**. Borga, Das, Mukherjee and Winkler (2022) study permutation and Mallows large deviations, including inversion-constrained permuton limits; those describe a permutation diagram, not the graph generated by independently sampling each new vertex's neighbours. The new assertion here is the explicit **conditional random-graph graphon** under an exact edge count and its proof by conditional coupling. Severini and Weisstein (2026) define the exact uniform sequential-attachment distribution and analyze extremal unlabelled graph likelihood and entropy; its stated theorems do not condition the graph on a macroscopic atypical edge count. Janson and Severini (2012/2013), Theorems 5.1--5.5, give the **unconditioned** graphon for fixed limiting propensity laws and stationary-step regimes. Their fixed limiting distribution condition does not imply the present age-dependent conditional latent measure, and their theorem does not give exact-count probabilities. The present conditional limit uses a horizon-dependent exponential tilt, a lattice local-limit argument and an exact microcanonical conditioning step. The general speed-\(n\) graphon-sampling LDP of Grebík--Pikhurko applies to this distribution after random relabeling; it establishes an abstract variational principle, not the explicit microcanonical age-dependent conditional graphon given here. The independent exact-point calculation in Step 5 is included for completeness and is consistent with the known Mahonian rate theory.

## Limitations
The theorem covers fixed interior normalized edge counts and convergence in probability of dense subgraph statistics. It does not cover boundary edge counts, joint growing-pattern statistics, sparse-regime limits, quantitative cut-distance rates, or conditional fluctuations. The proof assumes the specific uniform choice of each outdegree; a different arrival law need not have the stated tilt. The stated originality is subject to broader historical-priority searches, including large deviations for conditioned graph-growth models. No independent audit is asserted here.

## References
1. S. Severini and E. W. Weisstein, *The minimum of the graph likelihood*, first posted 19 August 2026, https://arxiv.org/abs/2608.19467 .
2. S. Janson and S. Severini, *An example of graph limits of growing sequences of random graphs*, first posted 20 June 2012, https://arxiv.org/abs/1206.4586 .
3. L. Lovász, *Large Networks and Graph Limits*, American Mathematical Society, 2012, for the equivalence between homomorphism-density convergence and graphon cut convergence.
4. J. Borga, S. Das, S. Mukherjee and P. Winkler, *Large deviation principle for random permutations*, first posted 9 June 2022, https://arxiv.org/abs/2206.04660 , for Mallows and inversion-constrained permutations.
5. J. Grebík and O. Pikhurko, *Large deviation principles for graphon sampling*, first posted 11 November 2023, https://arxiv.org/abs/2311.06531 ; Electronic Journal of Probability 31 (2026), https://doi.org/10.1214/26-EJP1512 . The general speed-\(n\) LDP applies to this unconditioned graphon-sampling ensemble; this paper is directly relevant prior coverage of that general statement, but it does not evaluate the present exact-count conditional limit.
