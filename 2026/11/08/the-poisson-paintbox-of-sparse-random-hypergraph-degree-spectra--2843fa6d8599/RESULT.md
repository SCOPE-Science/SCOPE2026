# The Poisson paintbox of sparse random hypergraph degree spectra

## Finding

Let every subset of \(\{1,\ldots,n\}\) of size \(r\ge2\) be an independent hyperedge with probability \(p_{n,r}\), equal for all subsets of the same size. Suppose
\[
\lambda_n=\sum_{r=2}^n\binom{n-1}{r-1}p_{n,r}\longrightarrow\lambda\in(0,\infty),\qquad
\epsilon_n=\max_{2\le r\le n}p_{n,r}\longrightarrow0,
\]
and the finite measures
\[
\nu_n=\sum_{r=2}^n\binom{n-1}{r-1}p_{n,r}\,
\delta_{(r-1)/(n-1)}\Longrightarrow\nu
\]
converge weakly on \([0,1]\). Thus \(\nu([0,1])=\lambda\). Let \(D_{n,i}\) count hyperedges containing vertex \(i\), and \(F_n(k)=n^{-1}\sum_{i=1}^n\mathbf1\{D_{n,i}=k\}\) be its empirical degree mass function.

**Theorem (random degree-spectrum limit and identification).** In distribution in \(\ell^1(\mathbb N_0)\), \(F_n\Longrightarrow P_\nu\), a random probability mass function whose probability generating function conditional on a Poisson point process \(\Pi\) is
\[
G_\nu(z)=\sum_{k\ge0}P_\nu(k)z^k
=\exp\!\bigl(\nu(\{0\})(z-1)\bigr)
\prod_{x\in\Pi}(1-x+xz),\quad0\le z\le1,
\]
where \(\Pi\) has intensity \(x^{-1}\nu(dx)\) on \((0,1]\). Its factors are independent Bernoulli trials conditional on \(\Pi\). The product exists almost surely because \(\sum_{x\in\Pi}x<\infty\) almost surely.

For any fixed number \(m\) of distinct tagged vertices, the limiting vector of degrees has the form \(D_j=\sum_{S\ni j}H_S\), where the \(H_S\), indexed by nonempty subsets \(S\subseteq\{1,\ldots,m\}\), are mutually independent Poisson variables with means
\[
\mu_S=\int_{[0,1]}x^{|S|-1}(1-x)^{m-|S|}\,\nu(dx).
\]
The convention at \(x=0\) is the continuous polynomial extension. Every one-vertex marginal is \(\operatorname{Pois}(\lambda)\), even when the empirical distribution is random.

In particular,
\[
\mathbb E P_\nu(0)=e^{-\lambda},\qquad
\operatorname{Var}(P_\nu(0))=e^{-2\lambda}
\left[\exp\left(\int_{[0,1]}x\,\nu(dx)\right)-1\right].
\]
Thus \(F_n\) converges to the deterministic \(\operatorname{Pois}(\lambda)\) mass function in probability **if and only if** \(\nu=\lambda\delta_0\). Otherwise there are persistent random empirical-degree fluctuations.

**Identification.** For \(M_j=\int_{[0,1]}x^j\,\nu(dx)\), every positive integer \(k\) satisfies
\[
\log\mathbb E[P_\nu(0)^k]
=\sum_{j=1}^k(-1)^j\binom{k}{j}M_{j-1}.
\]
The moments of the single random isolate fraction recover all \(M_j\) recursively, and hence uniquely recover \(\nu\) by determinacy of the Hausdorff moment problem. Every finite positive \(\nu\) of nonzero mass is attainable under the stated hypotheses.

As an explicit phase transition, for a single hyperedge rank \(r_n\), with \(r_n/n\to\alpha\in[0,1]\), expected vertex degree tending to \(\lambda\), and individual rank inclusion probability tending to zero: if \(\alpha=0\), the limit is deterministically \(\operatorname{Pois}(\lambda)\). If \(0<\alpha\le1\), the limiting empirical distribution is \(\operatorname{Bin}(K,\alpha)\) conditional on \(K\sim\operatorname{Pois}(\lambda/\alpha)\), hence is random. This includes the endpoint \(\alpha=1\) when \(r_n<n\) eventually, ensuring \(\epsilon_n\to0\) for this single-rank construction.

## Assumptions and scope

Each subset of the same size is sampled with one common probability, all individual subset indicators are independent, and only sizes at least two are allowed. All convergence statements hold along the full sequence satisfying the displayed finite-intensity, small-individual-probability, and weak-size-spectrum conditions. Weak measure convergence is on the compact interval \([0,1]\); repeated mass points in the Poisson process retain multiplicity. The limit is a probability measure on probability mass functions, not almost-sure convergence to a fixed law. Fixed-dimensional degree limits are for distinct tagged vertices, with \(m\) fixed as \(n\to\infty\).

## Proof

**1. Exact tagged patterns.** Fix \(m\) distinct vertices. For each nonempty \(S\subseteq\{1,\ldots,m\}\), let \(H_{n,S}\) count included hyperedges whose intersection with the tagged set is exactly \(S\). These counts are independent as they involve disjoint collections of independently included subsets. If \(s=|S|\), their exact expectations are
\[
\mu_{n,S}=\sum_{r=2}^n\binom{n-m}{r-s}p_{n,r},
\]
with out-of-range binomial coefficients defined to be zero. For fixed \(m\), elementary falling-factorial algebra yields uniformly in \(2\le r\le n\)
\[
\frac{\binom{n-m}{r-s}}{\binom{n-1}{r-1}}
=\frac{(r-1)_{s-1}(n-r)_{m-s}}{(n-1)_{m-1}}
=x_{n,r}^{s-1}(1-x_{n,r})^{m-s}+O_m(n^{-1}),
\]
where \(x_{n,r}=(r-1)/(n-1)\), with the same convention for vanishing falling factorials. It follows by weak convergence of \(\nu_n\) that \(\mu_{n,S}\to\mu_S\) as claimed.

**2. Rare-event vector approximation.** The multivariate count vector \((H_{n,S})_{S\ne\emptyset}\) is a product of Poisson-binomial distributions. Applying the elementary Bernoulli-to-Poisson total-variation coupling to all constituent subset indicators gives
\[
d_{\mathrm{TV}}\!\left(
\mathcal L((H_{n,S})_{S\ne\emptyset}),
\bigotimes_{S\ne\emptyset}\operatorname{Pois}(\mu_{n,S})
\right)
\le\sum_{S\ne\emptyset}\sum_{e:\,e\cap[m]=S}p_{n,|e|}^2
\le\epsilon_n\,m\lambda_n\longrightarrow0.
\]
(The convention for total variation may replace the first constant by a universal constant without changing the limit.) Taking sums over \(S\ni j\) yields the asserted joint limit. At \(m=1\) its mean is \(\sum_{r}\binom{n-1}{r-1}p_{n,r}\to\lambda\), proving the Poisson marginal.

**3. A consistent paintbox.** Construct a Poisson point process \(\Pi\) on \((0,1]\) with intensity \(\nu(dx)/x\). Independently for each \(x\in\Pi\), mark each of a countable sequence of vertices Bernoulli with success probability \(x\). Add independent \(\operatorname{Pois}(\nu(\{0\}))\) singleton counts to each vertex. Poisson thinning by the exact subset of marked vertices gives independent Poisson counts with means \(\int x^{|S|-1}(1-x)^{m-|S|}\nu(dx)\) for \(|S|\ge2\), while singleton patterns receive the remaining intensity at \(x=0\). This identifies exactly the finite-dimensional laws from step 2. Conditional on \(\Pi\), different vertices are identically and independently distributed with mass function \(P_\nu\) and the stated generating function. Since \(\mathbb E\sum_{x\in\Pi}x=\nu((0,1])\le\lambda\), the Bernoulli sum is almost surely finite and defines a genuine probability distribution.

**4. Empirical convergence.** For fixed \(k_1,\ldots,k_m\), expand \(\mathbb E\prod_{j=1}^m F_n(k_j)\) as a sum over ordered vertex-index tuples. Tuples with any repeated index account for \(O_m(n^{-1})\) after division by \(n^m\); all distinct-index summands are identical by exchangeability and converge by step 2 to \(\mathbb E\prod_j P_\nu(k_j)\), using the paintbox. Thus every finite set of histogram coordinates converges jointly in law: they are bounded, so joint monomial convergence determines the law on the compact cube. For tightness in \(\ell^1\), uniformly in large \(n\),
\[
\mathbb E\sum_{k>K}F_n(k)=\Pr(D_{n,1}>K)
\le\frac{\lambda_n}{K+1},
\]
and the analogous bound holds for \(P_\nu\) from its Poisson one-vertex mixture. Markov's inequality and finite-coordinate tightness yield \(\ell^1\) tightness and the desired weak convergence.

**5. Isolates and the exact boundary.** Conditional on \(\Pi\), \(P_\nu(0)=e^{-\nu(\{0\})}\prod_{x\in\Pi}(1-x)\). The Poisson Laplace functional gives for integers \(k\ge1\),
\[
\log\mathbb E P_\nu(0)^k=-k\nu(\{0\})
+\int_{(0,1]}\frac{(1-x)^k-1}{x}\nu(dx)
=\sum_{j=1}^k(-1)^j\binom{k}{j}M_{j-1}.
\]
Here integrability is immediate from the bound \(|(1-x)^k-1|\le kx\). Taking \(k=1,2\) proves the mean and variance. Since \(\int x\nu(dx)=0\) if and only if \(\nu((0,1])=0\), isolate fluctuations vanish exactly in the stated regime. If \(\nu=\lambda\delta_0\), the process has no atoms and \(P_\nu\) is deterministically Poisson; otherwise its isolate mass is nonconstant. This establishes both directions of the deterministic-limit equivalence. From the displayed triangular moment identity, \(M_{k-1}\) has coefficient \((-1)^k\ne0\), so all \(M_j\) are recovered successively. Finite Borel measures on \([0,1]\) are determined by their power moments, proving identifiability.

**6. Attainability and the one-rank regime.** Given any finite nonzero \(\nu\), for large \(n\) choose a measurable map \(r_n:[0,1]\to\{\lceil\sqrt n\rceil,\ldots,n-\lceil\sqrt n\rceil\}\) such that \(\sup_{x\in[0,1]}|(r_n(x)-1)/(n-1)-x|\to0\), by rounding and clipping. Put \(q_{n,r}=\nu(\{x:r_n(x)=r\})\) and \(p_{n,r}=q_{n,r}/\binom{n-1}{r-1}\) at these ranks, zero otherwise. Then \(\lambda_n=\nu([0,1])\), \(\nu_n\Rightarrow\nu\), and \(\epsilon_n\to0\) because the denominators grow uniformly without bound. For a single rank with \(r_n/n\to\alpha\), the intensity limit is \(\nu=\lambda\delta_\alpha\). At \(\alpha=0\), the deterministic limit was shown above. For \(\alpha>0\), \(\Pi\) consists of \(K\sim\operatorname{Pois}(\lambda/\alpha)\) points at \(\alpha\), so its conditional generating function is \((1-\alpha+\alpha z)^K\), proving the random-binomial assertion.

## Verification

Run \(`python3 check.py`\) in a directory containing the accompanying standalone checker. It exhaustively verifies exact tagged-incidence combinatorial identities for bounded \(n,m,r\), enumerates all \(2^{10}\) configurations of a four-vertex model with rational independent edge probabilities, checks finite Poisson-shock means and recovers rational spectral moments from the isolate identities. The passing execution reports 3,652 checks. None of these finite checks certifies an infinite limit; that is furnished by proof steps 1–6.

## Relationship to prior work

Xie and Bhattacharya [1] establish dependent Poisson limits for monochromatic-hyperedge counts in random colorings, a related but different rare-event statistic. Kraakman and Stegehuis [2] study simplicity in configuration-model hypergraphs with prescribed degree sequences, not the independently generated random degree spectrum. Bergman and Leskelä [3] analyze connectivity and isolated-node estimates for shotgun random hypergraphs with variable sizes; their isolation computations do not evaluate this paintbox histogram limit or inverse characterization. Pal and Makowski [4] emphasize the general distinction between nodal and empirical degree distributions and give a nonconcentrating threshold-graph counterexample; their general criterion does not give the present explicit hypergraph spectrum. López [5] computes the distribution of the number of distinct *neighbors* in projected fixed-rank hypergraphs, not the number of incident hyperedges or the random empirical mass function. Zhu, Xu and Reinert [6] approximate *fixed-dimensional* degree vectors by independent Poisson laws in regimes of low shared incidence; the explicit correlated Poisson subset shocks in this manuscript instead allow macroscopic shared hyperedges and give the empirical-law limit and isolate reconstruction. Their work first appeared on November 3, 2026, and is included as comparative context. Goldschmidt and Norris [7] use independent Poisson hyperedge multiplicities at fixed-size intensities for collapse and essential-edge statistics; their Theorem 2.1 does not determine the random empirical degree spectrum when macroscopic ranks carry bounded expected vertex incidence.

## Limitations

The conclusions require edge indicators to be independent, size exchangeability within each rank, a finite limiting expected degree, and a vanishing largest individual inclusion probability. Arbitrary inhomogeneous vertex-dependent sampling, growing-dimensional tagged vectors, rates for the empirical-law convergence, and central limit fluctuations around deterministic regimes are not established. The general construction uses a random finite-intensity measure parameter \(\nu\), not a result for dependent or configuration-model hyperedges. Historical coverage by a general Poisson-paintbox theorem in the literature remains possible; the explicit combination of empirical spectrum, threshold and inverse isolate law is the asserted contribution.

## References

[1] Y. Xie and B. B. Bhattacharya, "Joint Poisson Convergence of Monochromatic Hyperedges in Multiplex Hypergraphs," arXiv:2412.00610, publicly posted 2024-11-30, https://arxiv.org/abs/2412.00610.

[2] Y. J. Kraakman and C. Stegehuis, "Simplicity of random hypergraphs," arXiv:2604.05921, publicly posted 2026-04-07, https://arxiv.org/abs/2604.05921.

[3] E. Bergman and L. Leskelä, "Connectivity of random hypergraphs with a given hyperedge size distribution," arXiv:2207.04799, https://arxiv.org/abs/2207.04799.

[4] S. Pal and A. M. Makowski, "Asymptotic degree distributions in large (homogeneous) random networks: A little theory and a counterexample," arXiv:1710.11064, https://arxiv.org/abs/1710.11064.

[5] E. López, "The distribution of the number of node neighbors in random hypergraphs," arXiv:1302.2830, https://arxiv.org/abs/1302.2830.

[6] X. Zhu, W. Xu and G. Reinert, "Approximating Distributions on Vertex Degrees in Random Hypergraphs via Stein's Method," arXiv:2611.04705, first posted 2026-11-03, https://arxiv.org/html/2611.04705v1.

[7] C. Goldschmidt and J. Norris, "Essential edges in Poisson random hypergraphs," arXiv:math/0401143, https://arxiv.org/abs/math/0401143.
