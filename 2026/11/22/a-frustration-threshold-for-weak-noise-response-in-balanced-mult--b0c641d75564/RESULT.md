# A frustration threshold for weak-noise response in balanced multipartite anti-voter dynamics

## Finding
For the rate-one anti-voter process with fair independent refreshes at rate \(a>0\) on a balanced complete \(r\)-partite graph \(K_{n,\ldots,n}\), define the magnetization contrast \(M=m_1-m_2\) between two specified parts. For every integer \(r\ge2\), integer \(n\ge2\), and real \(a>0\), the stationary time covariance is exactly
\[
\operatorname{Cov}(M(t),M(0))=\frac{2(r-1)(1+a)(2+a)}{D_{r,n}(a)}\exp\!\left[-\left(a+\frac{r-2}{r-1}\right)t\right],\qquad t\ge0,
\]
where
\[
D_{r,n}(a)=1+n\big[2(r-2)+(3r-4)a+(r-1)a^2\big].
\]
Consequently the integrated stationary susceptibility \(\chi_{r,n}(a)=\int_0^\infty\operatorname{Cov}(M(t),M(0))\,dt\) is
\[
\chi_{r,n}(a)=\frac{2(r-1)(1+a)(2+a)}{D_{r,n}(a)\big(a+(r-2)/(r-1)\big)}.
\]
In the weak-refresh window \(a=c/n\), for any fixed \(c>0\), two shores have a distinct scaling regime from three or more shores:
\[
\begin{aligned}
 r=2:&\quad \lim_{n\to\infty}\operatorname{Var}(M)=\frac{4}{1+2c},\quad \lim_{n\to\infty}\frac{\chi_{2,n}(c/n)}{n}=\frac{4}{c(1+2c)},\\
 r\ge3:&\quad \lim_{n\to\infty}n\operatorname{Var}(M)=\frac{2(r-1)}{r-2},\quad \lim_{n\to\infty}n\chi_{r,n}(c/n)=\frac{2(r-1)^2}{(r-2)^2}.
\end{aligned}
\]
The two-time limits are similarly sharp: for \(s\ge0\), \(\operatorname{Cov}(M(ns),M(0))\to4e^{-cs}/(1+2c)\) if \(r=2\), whereas for each fixed \(t\ge0\) and \(r\ge3\), \(n\operatorname{Cov}(M(t),M(0))\to [2(r-1)/(r-2)]e^{-(r-2)t/(r-1)}\).

## Assumptions and scope
The graph has \(r\) parts, each with exactly \(n\) vertices, and all edges join vertices from different parts. Each vertex has its own rate-one Poisson clock; when it rings, that vertex chooses one of its \((r-1)n\) neighbors uniformly and takes the **opposite** spin. Independently, each vertex has a rate-\(a\) Poisson refresh clock and replaces its spin by a fair sign \(+1\) or \(-1\). Clocks are independent. Part magnetizations are \(m_j=n^{-1}\sum_{i\text{ in part }j}\sigma_i\), and \(M=m_1-m_2\). All stationarity and two-time statements use the unique stationary distribution. The limit \(n\to\infty\) holds for fixed integer \(r\) and fixed \(c>0\); no joint \(r\)-growth is asserted. This is a continuous-time, finite-spin system and no diffusion-process limit is claimed.

## Proof
**Stationarity and symmetry.** The positive fair-refresh rate makes the finite-state chain irreducible. Its stationary law is therefore unique and invariant under simultaneous spin reversal and permutations within/between equal-sized parts. Hence every spin has stationary mean zero. Let \(u\) denote the two-spin expectation for distinct vertices in the same part, and \(v\) the expectation for vertices in different parts.

**Pair equations.** Acting with the generator on a product of two distinct spins and then taking stationary expectations gives, for a same-part pair,
\[
(1+a)u+v=0.
\]
For a different-part pair, exactly one neighbor of each selected vertex is its counterpart. Its contribution is \(\sigma_i^2=1\); the other neighbors contribute \((n-1)u\) and \((r-2)nv\). Thus
\[
(1+a)v+\frac{1+(n-1)u+(r-2)nv}{(r-1)n}=0.
\]
Solving these two equations yields
\[
u=D_{r,n}(a)^{-1},\qquad v=-(1+a)D_{r,n}(a)^{-1}.
\]
In particular, the denominator is strictly positive throughout the stated domain. This uses the exact finite generator, not a mean-field approximation.

**Equal-time contrast.** The mean of \(M\) is zero. Its second moment is
\[
\operatorname{Var}(M)=\frac{2}{n}\left[1+(n-1)u-nv\right]
=\frac{2(r-1)(1+a)(2+a)}{D_{r,n}(a)}.
\]
The first equality includes diagonal terms \(\sigma_i^2=1\).

**Exact time dependence.** Write \(S=\sum_{j=1}^r m_j\). On each part magnetization the generator satisfies
\[
\mathcal Lm_j=-(1+a)m_j-\frac{S-m_j}{r-1}.
\]
Subtracting the equations for parts one and two gives the exact observable eigenfunction relation
\[
\mathcal LM=-\lambda_r(a)M,\qquad \lambda_r(a)=a+\frac{r-2}{r-1}>0.
\]
Consequently \(\mathbb E[M(t)\mid\sigma(0)]=e^{-\lambda_r(a)t}M(0)\). Multiply by \(M(0)\) and average in stationarity to obtain the displayed two-time covariance; integration over \(t\ge0\) gives \(\chi\). No assertion is made about the spectral gap of the entire chain or any other observable.

**Singular weak-refresh limit.** Substitute \(a=c/n\) in the exact expressions. At \(r=2\), \(D_{2,n}(c/n)=1+2c+c^2/n\) and \(\lambda_2(c/n)=c/n\). At any fixed \(r\ge3\), \(D_{r,n}(c/n)=2(r-2)n+O(1)\) and \(\lambda_r(c/n)=(r-2)/(r-1)+O(1/n)\). These elementary expansions give the four variance/susceptibility limits and the two time-covariance limits as stated.

## Verification
The standalone `verify.py` constructs the full finite-state Markov generator for four small nontrivial systems (including 2- and 3-part cases), computes the stationary law by linear algebra, compares all same-part and cross-part spin expectations with the displayed rational formulas, and tests the exact conditional semigroup at three positive time lags. It also checks all displayed algebraic identities symbolically with SymPy. The checks are supplementary finite examples; the all-size and all-parameter assertions follow from the preceding generator identities and limiting argument.

Run with `python verify.py` using Python 3 with NumPy, SciPy and SymPy available.

## Relationship to prior work
The signed-edge anti-voter model predates this calculation. Gantert, Löwe and Steif study ergodicity for signed voter systems on infinite graphs; Masuda studies conformist/contrarian mixtures with mean-field and fluctuation approximations. Kitching and collaborators give network-general results about stationary spatial order in binary-state systems with unfaithful copying: their general stationary-correlation framework can encompass parts of the equal-time pair calculation. Accordingly the standalone novelty claim is **not** the existence of anti-voter dynamics, ergodicity under refresh, or all stationary spatial correlations. The specific result assessed here is the *joint exact time-dependent magnetization-contrast response and the sharp two-shore versus three-or-more-shore singular susceptibility scaling*, including its quantitative time rescaling. The 2004 stationary-distribution study by Huber and Reinert is especially relevant; its complete text was unavailable for a decisive comparison. See the research review for residual historical-priority risk.

## Limitations
The model has equal part sizes, equal normalized per-vertex copying clocks, unbiased independent refreshes, and all edges of negative (contrarian) type. No unequal-part theorem, arbitrary signed-edge network result, full distributional limiting process, claim of thermodynamic criticality in a general graph class, or complete literature priority certificate is given. The accessible literature does not rule out an equivalent earlier specialization, especially in the unavailable Huber–Reinert chapter; the novelty conclusion is bounded by that access limit. Independent scientific validation has not been performed.

## References
1. N. Masuda, “Voter models with contrarian agents,” arXiv:1306.4401v1 (first publicly submitted 2013-06-19), https://arxiv.org/abs/1306.4401.
2. N. Gantert, M. Löwe and J. E. Steif, “The voter model with anti-voter bonds,” *Annales de l'Institut Henri Poincaré (B)* 41 (2005), 767–780, https://www.numdam.org/item/10.1016/j.anihpb.2004.03.007.pdf.
3. D. Kitching et al., “Estimating transmission noise on networks from stationary local order,” *Europhysics Letters* 150 (2025), article adc9de, https://doi.org/10.1209/0295-5075/adc9de.
4. M. Huber and G. Reinert, “The stationary distribution in the Antivoter model: exact sampling and approximations,” *IMS Lecture Notes–Monograph Series* 46 (2004), 79–93, https://www.jstor.org/stable/4356335. Full text not examined.
5. N. S. Matloff, “Ergodicity conditions for a dissonant voting model,” *Annals of Probability* 5 (1977), 371–386, https://doi.org/10.1214/aop/1176995798.
