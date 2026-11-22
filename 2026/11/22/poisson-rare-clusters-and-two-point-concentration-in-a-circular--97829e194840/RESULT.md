# Poisson rare clusters and two-point concentration in a circular nearest-neighbor forest

## Finding
Let \(n\ge3\) points be independently uniform on a circle of circumference one. Give each point a directed edge to its unique closest point in the circular geodesic metric, and let \(G_n\) be the undirected simple graph obtained by forgetting directions and duplicate edges. Let \(W_n(k)\) count connected components of \(G_n\) containing at least \(k\) points, and let \(L_n\) be its largest component size. For integers \(k\ge2\) define
\[
q_k=\frac{k2^k}{(k+2)!},\qquad v_k=\frac{2^{k-2}}{(k-1)!}.
\]
For every \(n\ge2k+4\), the exact mean and quantitative Poisson bound are
\[
\mathbb E W_n(k)=nq_k,\quad
d_{\mathrm{TV}}\bigl(\mathcal L(W_n(k)),\operatorname{Poisson}(nq_k)\bigr)
\le 2\min\{1,(nq_k)^{-1}\}\bigl[n(2k+3)q_k^2+4nv_k^2\bigr].
\]
Consequently, for every integer sequence \(k=k_n\to\infty\) with \(2k_n+4\le n\), \(k_n^4/n\to0\), and \(nq_{k_n}\to\lambda\in[0,\infty)\),
\[
W_n(k_n)\xrightarrow{d}\operatorname{Poisson}(\lambda),\qquad
\Pr(L_n<k_n)\longrightarrow e^{-\lambda}.
\]
The discrete factorial tail creates an additional sharp phenomenon. For all sufficiently large \(n\), set
\[
b_n=\max\{k\ge2:nq_k\ge\sqrt{k}\}.
\]
Then
\[
b_n\sim\frac{\log n}{\log\log n},\qquad
\Pr\bigl(L_n\in\{b_n,b_n+1\}\bigr)\longrightarrow1.
\]
Thus the largest connected component lies asymptotically on two neighboring integers, even though the graph has order \(n\) components.

## Assumptions and scope
All sampling is independent and uniform on the unit circle; the geodesic distance is the length of the shorter circular arc. There are almost surely no distance ties. The connected components considered here are those of the *undirected one-nearest-neighbor graph*, not the fixed-radius geometric graph, an online nearest-neighbor tree, or the independent-edge random-link model. All asymptotics are as \(n\to\infty\). Critical Poisson limits are subsequential because the ratio of successive factorial tail probabilities tends to zero. The statement makes no assertion of a single continuously centered Gumbel law or of independence of consecutive cluster sizes.

## Proof
**1. Exact gap encoding.** Fix one sampled vertex as the cyclic origin and let \(D_0,\ldots,D_{n-1}\) be the clockwise spacings. Their joint law is Dirichlet with all parameters one; equivalently \(D_i=E_i/\sum_jE_j\), for independent mean-one exponentials \(E_i\). The comparisons between adjacent gaps therefore have precisely the joint law of comparisons between independent continuous variables. The edge across gap \(i\) is absent exactly if \(D_i>D_{i-1}\) and \(D_i>D_{i+1}\), with cyclic indices. Every component is a path between two successive strict local maxima of the gap sequence; its number of vertices equals the index distance between those maxima. The global largest gap ensures at least one missing edge.

**2. The known one-gap probability and its exact tail.** Write \(p_j\) for the probability that gap \(0\) is a local maximum and the next local maximum occurs at gap \(j\). The distribution of distances between consecutive local maxima of independent continuous variables was previously investigated by Kuketayev; it is used here as an input, not claimed as a new discovery. For completeness it can be recovered by conditioning on the unique intervening minimum. If that minimum is at index \(a\), \(1\le a\le j-1\), let \(s\in(0,1)\) be one minus its uniformized height. Conditional integration of the strictly descending and strictly ascending chains, including the two outer inequalities that define endpoint maxima, gives
\[
p_j=\sum_{a=1}^{j-1}\frac{1}{a!(j-a)!}
\int_0^1s^j\left(1-\frac{s}{a+1}\right)
\left(1-\frac{s}{j-a+1}\right)ds
=\frac{(j-1)(j+2)2^j}{(j+3)!}.
\]
The last equality follows by expanding the product and summing ordinary binomial coefficients. The telescoping identity
\[
\frac{(j-1)(j+2)2^j}{(j+3)!}
=\frac{j2^j}{(j+2)!}-\frac{(j+1)2^{j+1}}{(j+3)!}
\]
shows that the *unconditional* probability that a specified gap begins a component of size at least \(k\) is \(q_k=k2^k/(k+2)!\). The event depends only on the \(k+2\) gaps with indices \(-1,0,\ldots,k\), so its probability and the exact identity \(\mathbb EW_n(k)=nq_k\) hold for the finite circular model as soon as these indices are distinct.

**3. Dependency neighborhoods.** Let \(I_i(k)\) indicate that gap \(i\) is a strict local maximum and none of gaps \(i+1,\ldots,i+k-1\) is a strict local maximum. Then \(W_n(k)=\sum_iI_i(k)\). Each indicator uses exactly the independent exponential variables with cyclic indices from \(i-1\) through \(i+k\). Thus it is independent of all other indicators with cyclic start distance at least \(k+2\). The dependency neighborhood has at most \(2k+3\) starts. Two starts at distance \(1,\ldots,k-1\) cannot both occur, because the earlier event forbids the later peak.

For possible overlapping starts at distance \(k\) or \(k+1\), take a block of \(k-1\) independent gaps immediately after the first start and another block of \(k-1\) gaps immediately after the later start, omitting the shared endpoint variables. These two blocks are disjoint. On each, the event requires that there be no strict internal local maximum. Of the \((k-1)!\) relative orderings of \(k-1\) independent continuous values, exactly \(2^{k-2}\) have no strict internal local maximum: their order decreases to a single minimum and then increases. Therefore
\[
\Pr(I_i(k)=I_j(k)=1)\le v_k^2
\quad\text{for any overlapping compatible starts},\qquad
\frac{v_k}{q_k}=\frac{(k+1)(k+2)}4.
\]
The bound is valid whether or not the two events can actually coexist; no assumption of independence between consecutive component sizes is made.

**4. Quantitative Poisson approximation.** Apply the standard dependency-neighborhood Chen–Stein inequality for sums of Bernoulli indicators, with local terms \(b_1\) and \(b_2\). Here
\[
b_1\le n(2k+3)q_k^2,\qquad b_2\le4nv_k^2,
\]
and the external-dependence term vanishes because disjoint collections of exponential coordinates are independent. The displayed total-variation bound follows. Since \(v_k/q_k=O(k^2)\), if \(nq_k\) stays bounded and \(k^4/n\to0\), both error terms vanish. Because \(L_n<k\) if and only if \(W_n(k)=0\), the extreme-value zero-count law follows.

**5. Two-point concentration.** The same dependency classification gives
\[
\operatorname{Var}(W_n(k))\le nq_k+4nv_k^2.
\]
From Stirling's approximation,
\[
\log q_k=-k\log k+(1+\log2)k+O(\log k),
\]
so \(b_n\sim\log n/\log\log n\). By definition \(nq_{b_n}\ge\sqrt{b_n}\to\infty\), while
\[
\frac{\operatorname{Var}(W_n(b_n))}{(\mathbb EW_n(b_n))^2}
\le\frac1{nq_{b_n}}+\frac{(b_n+1)^2(b_n+2)^2}{4n}\longrightarrow0.
\]
Hence \(\Pr(L_n\ge b_n)\to1\). Finally,
\[
\frac{q_{k+1}}{q_k}=\frac{2(k+1)}{k(k+3)},\qquad
nq_{b_n+1}<\sqrt{b_n+1},
\]
so \(nq_{b_n+2}=O(b_n^{-1/2})\to0\). Markov's inequality gives \(\Pr(L_n\ge b_n+2)\to0\), proving the stated two-integer concentration.

## Verification
The accompanying `verify.py` performs exact-rational checks of the valley integrals, factorial-tail and ratio identities, exhaustive cyclic gap-order enumeration for \(5\le n\le8\), and exhaustive metric-vs-gap-graph equivalence checks through seven vertices. It also checks the deterministic threshold inequalities for selected large sample sizes. Its recorded run passed 368786 assertions. These are independent finite checks; the Poisson and two-point asymptotics rely on the explicit analytic proof above, not on simulations or finite enumeration.

## Relationship to prior work
The **single-gap distribution is prior work**: Kuketayev (2006) computed the law of distances between successive local maxima, and Zubkov, Kharitonova and Khil (2012) derived gap distributions and multivariate central limit results for frequencies of fixed gap lengths. This result does not re-present either the one-gap formula or fixed-size frequencies as new. Eppstein, Paterson and Yao studied nearest-neighbor graph components and raised component-size questions, mainly in the planar setting. Penrose and Wade studied the one-dimensional nearest-neighbor *length* statistic; the online graph in their title is a distinct model. The contribution asserted here is a **growing-size rare-component count in total variation, with a quantitative overlap bound, and two-adjacent-integer concentration of the largest component**. These assertions do not follow by simply substituting a fixed gap size into a fixed-dimensional central limit theorem. They use the exact separation/exclusion structure for growing rare windows.

## Limitations
The full texts of the 2012 gap-frequency paper and the 2014 neighboring-gap hidden-Markov paper were not accessible in this examination; their abstracts were read, and more general coverage cannot be categorically excluded. Classical rare-pattern Poisson approximation may offer alternative derivations. Priority should be checked by an independent literature specialist. The theorem applies only to the uniform circular one-nearest-neighbor graph; it is not a claim about planar samples, nonuniform spacings, higher nearest-neighbor ranks or finite-sample independent cluster sizes. The asymptotic Poisson limit is along integer thresholds with the stated expected-count limit, not universally after continuous centering.

## References
- A. Kuketayev, *Probability distribution of distances between local extrema of random number series*, arXiv:math/0611130, first submitted 6 November 2006. https://arxiv.org/abs/math/0611130
- A. M. Zubkov, N. A. Kharitonova and E. V. Khil, *Gaps between local maxima in sequences of random variables*, Theory of Probability and Its Applications 56 (2012), 590–601. https://doi.org/10.1137/S0040585X97985649
- E. V. Khil, *Markov structure of the sequence of local maxima and the gaps between them*, Theory of Probability and Its Applications 58 (2014), 430–441. https://doi.org/10.1137/S0040585X97986631
- D. Eppstein, M. S. Paterson and F. F. Yao, *On nearest-neighbor graphs*, Discrete & Computational Geometry; accessible author manuscript dated 12 January 2000. https://www-dev.ics.uci.edu/~eppstein/pubs/EppPatYao-DCG-97.pdf
- M. D. Penrose and A. R. Wade, *Limit theory for the random on-line nearest-neighbour graph*, arXiv:math/0603561, 23 March 2006. https://arxiv.org/abs/math/0603561
- R. Arratia, L. Goldstein and L. Gordon, *Two moments suffice for Poisson approximations: the Chen–Stein method*, Annals of Probability 17 (1989), 9–25. https://projecteuclid.org/euclid.aop/1176991491
