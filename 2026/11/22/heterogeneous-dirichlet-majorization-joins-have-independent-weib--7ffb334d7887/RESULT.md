# Heterogeneous Dirichlet majorization joins have independent Weibull scales

## Finding
Fix an integer \(d\ge 2\) and a vector of positive, not-all-equal parameters \(\boldsymbol\alpha=(\alpha_1,\ldots,\alpha_d)\). Write \(A=\sum_i\alpha_i\) and let \(\alpha_{[1]}\le\cdots\le\alpha_{[d]}\) be the ordered parameters. For \(1\le k<d\), define
\[
\gamma_k=\sum_{i=1}^{d-k}\alpha_{[i]},\qquad
h_k=\#\left\{J\subseteq\{1,\ldots,d\}:|J|=d-k,\ \sum_{i\in J}\alpha_i=\gamma_k\right\},
\]
\[
c_k=\frac{h_k\Gamma(A)}{\Gamma(\gamma_k+1)\Gamma(A-\gamma_k)}.
\]
Let \(P^{(1)},\ldots,P^{(m)}\) be independent random vectors with common \(\operatorname{Dirichlet}(\boldsymbol\alpha)\) distribution. Rearrange each vector decreasingly and let \(V_m\) be their least upper bound in the majorization order. Then, jointly for all \(1\le k<d\),
\[
\left(m^{1/\gamma_k}\left(1-\sum_{i=1}^k(V_m)_i\right)\right)_{k=1}^{d-1}
\ \xrightarrow{\mathrm d}\ (W_1,\ldots,W_{d-1}),
\qquad
\Pr(W_k>x)=e^{-c_kx^{\gamma_k}}\quad(x\ge0),
\]
where the \(W_k\) are **independent**. In addition, the least-concave-majorant adjustment required to form the join becomes unnecessary with probability tending to one: asymptotically, every prefix sum of \(V_m\) is exactly the maximum of the corresponding sample prefix sums.

For example, with \(\boldsymbol\alpha=(1,1,2,4)\), the respective Weibull shape exponents are \((4,2,1)\) and the respective rate constants are \((35,21,14)\). Repeated smallest parameters enter the rate through their exact minimizing-subset multiplicities. The all-equal case follows from the same proof but is not claimed as new.

## Assumptions and scope
The dimension \(d\) and all parameters \(\alpha_i>0\) are fixed while the sample size \(m\to\infty\). The Dirichlet law is the distribution of independent Gamma variables of shapes \(\alpha_i\), normalized by their sum. Let \(p^\downarrow\) denote the decreasing rearrangement of a probability vector. Majorization on decreasing vectors means \(p\preceq q\) when \(\sum_{i=1}^k p_i\le\sum_{i=1}^k q_i\) for every \(1\le k<d\). The majorization join is determined by the least concave majorant, on integer arguments \(0,\ldots,d\), of the coordinatewise maxima of these prefix sums, with endpoints \(0\) and \(1\).

No statement is made for zero Dirichlet parameters, dimension growing with sample size, non-Dirichlet dependence, or a quantitative finite-sample approximation rate.

## Proof
**1. A one-observation lower tail.** For a subset \(J\) of size \(d-k\) write \(S_J=\sum_{i\in J}P_i\) and \(a_J=\sum_{i\in J}\alpha_i\). The Gamma normalization gives \(S_J\sim\operatorname{Beta}(a_J,A-a_J)\), so, as \(t\downarrow0\),
\[
\Pr(S_J\le t)=\frac{\Gamma(A)}{\Gamma(a_J+1)\Gamma(A-a_J)}t^{a_J}(1+O(t)).\tag{1}
\]
If \(R_k\) is the sum of the \(d-k\) smallest coordinates, then \(R_k=\min_{|J|=d-k}S_J\). For distinct subsets \(J,J'\) of that size, \(S_J\le t\) and \(S_{J'}\le t\) imply \(S_{J\cup J'}\le2t\). The shape sum of the union exceeds \(\gamma_k\), because all parameters are strictly positive and the union strictly contains a size-\(d-k\) subset. This event has probability \(o(t^{\gamma_k})\), by a Beta lower-tail bound whenever the union is proper, and is impossible for small \(t\) when the union is all coordinates. Inclusion-exclusion and (1) therefore yield the sharp coefficient
\[
\Pr(R_k\le t)=c_k t^{\gamma_k}+o(t^{\gamma_k}).\tag{2}
\]
Only subsets attaining the least shape sum contribute at leading order, accounting for \(h_k\).

**2. Different ranks cannot be extreme in the same observation.** Fix \(1\le k<\ell<d\), and put \(t_k=x_km^{-1/\gamma_k}\), \(t_\ell=x_\ell m^{-1/\gamma_\ell}\), where the \(x\)'s are fixed positive constants. If both \(R_k\le t_k\) and \(R_\ell\le t_\ell\), there are subsets \(J,K\) of sizes \(d-k,d-\ell\) with \(S_J\le t_k\) and \(S_K\le t_\ell\). Since \(|J|>|K|\), the set \(J\setminus K\) is nonempty; it is disjoint from \(K\), and its coordinate sum is at most \(t_k\). For two disjoint nonempty coordinate sets \(B,C\), the joint Dirichlet aggregation density near the origin implies
\[
\Pr(S_B\le u, S_C\le v)=O(u^{\sum_{i\in B}\alpha_i}v^{\sum_{i\in C}\alpha_i})\quad(u,v\downarrow0),\tag{3}
\]
provided some coordinates remain outside the union. If their union is all coordinates, the probability is zero for \(u+v<1\). The constant in (3) depends only on the fixed parameter vector and subsets. Apply (3) to \(B=K\), \(C=J\setminus K\). Since \(a_K\ge\gamma_\ell\) and \(a_{J\setminus K}>0\), the bound is
\[
O\!\left(m^{-a_K/\gamma_\ell-a_{J\setminus K}/\gamma_k}\right)=o(m^{-1}).
\]
There are finitely many pairs of subsets, so
\[
\Pr(R_k\le t_k, R_\ell\le t_\ell)=o(m^{-1}).\tag{4}
\]
This remains valid for all positive, noninteger parameters and all parameter ties.

**3. The multivariate extreme law.** Let \(\Delta_{k,m}=\min_{1\le j\le m}R_k(P^{(j)})\). Equation (2), equation (4), and the finite union formula show that for fixed positive \(x_1,\ldots,x_{d-1}\),
\[
\Pr\bigl(\Delta_{k,m}>x_km^{-1/\gamma_k}\ \text{for every }k\bigr)
=\left(1-\frac{\sum_kc_kx_k^{\gamma_k}}m+o(m^{-1})\right)^m
\longrightarrow\prod_{k=1}^{d-1}e^{-c_kx_k^{\gamma_k}}.\tag{5}
\]
The limiting joint survival function factors. Thus the scaled deficits \(m^{1/\gamma_k}\Delta_{k,m}\) converge jointly to the asserted independent Weibull variables.

**4. The join requires no asymptotic correction.** Because all \(\alpha_i\) are positive, \(\gamma_1>\gamma_2>\cdots>\gamma_{d-1}>0\). The continuous positive limiting laws in (5) imply \(\Delta_{1,m}\to0\) and \(\Delta_{k+1,m}/\Delta_{k,m}\to0\) in probability for every \(1\le k<d-1\). Set \(q_0=0\), \(q_d=1\), and \(q_k=1-\Delta_{k,m}\) otherwise. Its increments are
\[
q_1-q_0=1-\Delta_{1,m},\quad
q_k-q_{k-1}=\Delta_{k-1,m}-\Delta_{k,m}\ (2\le k<d),\quad
q_d-q_{d-1}=\Delta_{d-1,m}.
\]
The successive increments are positive and strictly decreasing with probability tending to one, by the stated scale separation. Hence \(q\) is already concave with probability tending to one, so it coincides with its least concave majorant. On that event the actual join deficit equals \(\Delta_{k,m}\) for each \(k\), and the asserted joint convergence follows from (5). \(\square\)

## Verification
The accompanying standard-library checker `check.py` verifies symbolic subset and exponent inequalities across several integer parameter vectors, the exact Gamma/Beta leading constants in the example, and the reduction to the known uniform-parameter coefficients. A fixed-seed finite simulation also checks the predicted Weibull scales, high finite-sample concavity frequency, and decreasing incidence of shared extremizing observations. Its output is diagnostic only; the preceding argument supplies the infinite-sample proof. Run `python3 check.py` with Python 3.9 or later. No network access or nonstandard packages are required.

## Relationship to prior work
Hariharan, Krishnan and Deshpande (2026) study the majorization simplex, its joins and Rényi metrics, but not sample extrema under nonuniform Dirichlet laws. Bisi, Cunden, Gramegna and Ligabò (2026, Theorem 4.12) independently establish the fixed-dimensional join law for **uniform** simplex sampling, equivalent to \(\operatorname{Dirichlet}(1,\ldots,1)\). Their formula is recovered by taking \(\gamma_k=d-k\) and \(h_k=\binom{d}{k}\), which gives \(c_k=\binom{d}{k}\binom{d-1}{k-1}\); their discussion of other sampling measures does not establish the heterogeneous constants. Hashorva (2014) investigates tails of power-weighted aggregate Dirichlet risks and joint asymptotic independence for a different extremal family; these are not statements of a majorization join or its coordinated ranks. Corradini and Strokorb (2024) address stochastic orderings among max-stable Dirichlet dependence families, rather than extremes of ordered prefix sums of finite Dirichlet samples.

## Limitations
The theorem is fixed-dimensional, asymptotic, and assumes strictly positive fixed shape parameters. It does not estimate convergence rates, give a growing-dimension phase diagram, or classify meet limits. The equal-parameter case is already known. Literature searches and detailed inspections found no covering theorem for the heterogeneous case, but they cannot establish absolute historical priority; specialized literature beyond the inspected sources could contain related results. Independent mathematical validation has not been performed.

## References
1. T. Hariharan, P. Krishnan, A. Deshpande, *On Measures of Dissimilarity on the Majorization Simplex*, arXiv:2610.16687 (first posted 12 October 2026). https://arxiv.org/abs/2610.16687
2. E. Bisi, F. D. Cunden, G. Gramegna, M. Ligabò, *Extreme value statistics for majorisation partial orders*, arXiv:2611.23612v1 (first posted 17 November 2026), Theorem 4.12 and Section 7.3. https://arxiv.org/abs/2611.23612
3. E. Hashorva, *Extremes of aggregated Dirichlet risks*, arXiv:1404.3304 (2014); *Journal of Multivariate Analysis* 133 (2015), 334–345. https://doi.org/10.1016/j.jmva.2014.09.018
4. M. Corradini, K. Strokorb, *Stochastic ordering in multivariate extremes*, *Extremes* 27 (2024), 357–396. https://doi.org/10.1007/s10687-024-00486-0
