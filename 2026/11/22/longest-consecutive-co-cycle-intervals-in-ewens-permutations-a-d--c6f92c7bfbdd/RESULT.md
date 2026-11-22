# Longest consecutive co-cycle intervals in Ewens permutations: a Dickman random scale and a quenched Poisson onset

## Finding

Given an Ewens\((\theta)\) permutation of the integers \(1,\ldots,n\), call an interval of *numerically consecutive labels* cycle-cohesive if all its labels lie in one disjoint cycle; no requirement is imposed on their order around that cycle. Let \(L_n\) be its maximum length. The largest logarithmic cycle-cohesion run is controlled by the largest asymptotic cycle mass, rather than by a deterministic Bernoulli parameter:

\[
\frac{L_n}{\log n}\longrightarrow\frac{1}{-\log P_*}\qquad\text{almost surely under the coherent Ewens coupling},
\]
where \(P_*\) is the largest atom of a Poisson–Dirichlet\((\theta)\) random mass partition. For the uniform permutation case \(\theta=1\), this limit has the explicit distribution
\[
\lim_{n\to\infty}\Pr\left(\frac{L_n}{\log n}\le t\right)=\rho(e^{1/t})\quad(t>0),
\]
with Dickman's \(\rho\) characterized by \(\rho(u)=1\) for \(0\le u\le1\) and \(u\rho'(u)=-\rho(u-1)\) for \(u>1\).

There is also a *quenched* (paintbox-conditional) Poisson law for the longest runs. With \(p=P_*\), for any integer sequence \(k_n\) satisfying \(n(1-p)p^{k_n}\to\lambda\in(0,\infty)\), the number \(N_{n,k_n}\) of runs of the unique most frequent cycle label of length at least \(k_n\) converges in total variation to \(\operatorname{Poisson}(\lambda)\). All other cycle labels contribute an asymptotically vanishing probability of reaching this length; hence
\[
\Pr(L_n<k_n\mid (P_j)_{j\ge1})\to e^{-\lambda}.
\]
The integer threshold may depend on the paintbox realization. Such sequences exist along suitable subsequences; this statement does not assert a nonlattice centered Gumbel limit along every \(n\).

## Assumptions and scope

Fix \(\theta>0\). The Ewens probability of \(\pi\in S_n\) is proportional to \(\theta^{K(\pi)}\), where \(K(\pi)\) is its number of disjoint cycles. Consistency means restricting the *cycle partition* from the first \(n+1\) labels to the first \(n\) labels; it is not the restriction of one-line permutation strings. Under the standard Ewens Chinese restaurant construction, the cycle partition of all positive integers is exchangeable. Kingman's paintbox representation assigns random masses \(P_j>0\) with \(\sum_jP_j=1\); conditional on those masses, the color labels \(Z_1,Z_2,\ldots\) of consecutive integers are independent with \(\Pr(Z_i=j\mid(P_j))=P_j\), and equality of colors is equivalent to sharing a permutation cycle.

The ranked masses have law \(\mathrm{PD}(\theta)\); their size-biased enumeration has law GEM\((\theta)\). Almost surely \(0<P_*<1\), and \(P_*\) is a unique maximum; write \(P_{(2)}<P_*\) for the second-largest mass. All probability limits conditional on the paintbox are for almost every realization of these masses.

## Proof

**1. Reduction to runs of a random categorical word.** By the exchangeable partition representation, \(L_n\) is exactly the longest constant-color run of \((Z_1,\ldots,Z_n)\). Condition throughout on one paintbox with \(p=P_*\), unique maximizing color \(j_*\), and \(q=P_{(2)}<p\). Write \(a=-\log p\in(0,\infty)\).

**2. Almost-sure scale: upper estimate.** A constant-color interval of length \(k\) starting at a given site has conditional probability \(\sum_jP_j^k\le p^{k-1}\), because \(\sum_jP_j=1\). Hence \(\Pr(L_n\ge k\mid(P_j))\le np^{k-1}\). For \(n=2^m\) and \(k=\lceil(1+\varepsilon)\log n/a\rceil\), this is at most \(p^{-1}2^{-m\varepsilon}\), summable over \(m\). The first Borel–Cantelli lemma bounds the limsup along dyadic \(n\).

**3. Almost-sure scale: lower estimate.** Set \(k=\lfloor(1-\varepsilon)\log n/a\rfloor\), for \(n=2^m\). Partition the \(n\) labels into \(\lfloor n/k\rfloor\) disjoint windows of size \(k\). The events that each window is entirely color \(j_*\) are independent and each has probability \(p^k\ge n^{-(1-\varepsilon)}\). Thus the probability none is homogeneous is bounded by \(\exp[-\lfloor n/k\rfloor p^k]\le\exp[-c_p n^{\varepsilon}/\log n]\), summable over dyadic \(n\). Borel–Cantelli bounds the liminf. Since \(L_n\) is nondecreasing and \(\log(2^{m+1})/\log(2^m)\to1\), interpolation and then \(\varepsilon\downarrow0\) yield \(L_n/\log n\to 1/a\) almost surely. Conditioning and Fubini transfer this to the coherent random paintbox.

**4. Quenched Poisson run starts.** For integers \(k\le n\), define \(I_1=\mathbf1\{Z_1=\cdots=Z_k=j_*\}\). For \(2\le i\le n-k+1\), define
\[
I_i=\mathbf1\{Z_{i-1}\ne j_*,\ Z_i=\cdots=Z_{i+k-1}=j_*\},\qquad N_{n,k}=\sum_{i=1}^{n-k+1}I_i.
\]
This counts **maximal runs beginning at a given site** whose length is at least \(k\), exactly once per run; the run may continue past the threshold. Its conditional mean is
\[
\mu_{n,k}=p^k+(n-k)(1-p)p^k.
\]
The indicators have a dependency graph joining sites at distance at most \(k\): at greater separations the underlying categorical coordinates are disjoint and independent, whereas at any distinct distance at most \(k\) they are mutually exclusive (the putative start of the later run requires the preceding symbol not to be \(j_*\), but the earlier run requires it to be \(j_*\)). The elementary dependency-graph Chen–Stein bound therefore gives, when \(np^k\) remains bounded,
\[
d_{\mathrm{TV}}\bigl(N_{n,k},\operatorname{Pois}(\mu_{n,k})\bigr)\le C_p(k+1)np^{2k}=O_p(k/n).
\]
The bound also covers the one exceptional first-site indicator and uses only pairwise products of probabilities (the overlapping joint-event term vanishes). If \(n(1-p)p^{k_n}\to\lambda\), then \(k_n=(\log n)/a+O_p(1)\) and \(\mu_{n,k_n}\to\lambda\). Hence \(N_{n,k_n}\) converges in total variation to \(\operatorname{Pois}(\lambda)\).

**5. Exclusion of other cycle colors.** A union bound gives
\[
\Pr(\exists\text{ run of another color of length at least }k\mid(P_j))
\le n\sum_{j\ne j_*}P_j^k\le nq^{k-1}.
\]
For the critical threshold \(k=k_n\), the right side vanishes: \(np^{k_n}\asymp1\), and \(q<p\) implies \(nq^{k_n-1}=O_p(n^{1-\log q/\log p})=o(1)\). Thus \(\Pr(L_n<k_n\mid(P_j))=\Pr(N_{n,k_n}=0\mid(P_j))+o(1)\to e^{-\lambda}\).

**6. Dickman specialization.** At \(\theta=1\), the largest paintbox atom has the classical largest-random-permutation-cycle limit \(P_*\), with \(\Pr(P_*\le1/u)=\rho(u)\) for \(u\ge1\). The map \(p\mapsto(-\log p)^{-1}\) is continuous and increasing on \((0,1)\); substituting \(p=e^{-1/t}\) gives the stated CDF at each \(t>0\). The Poisson–Dirichlet largest-atom law is continuous, so this identifies convergence in distribution, not just convergence under the coupling.

## Verification

`checker.py` independently enumerates permutations and weighted set partitions for every integer size from 2 through 8. Their exact distributions for the longest co-cycle label run coincide, including the all-one-cycle probability \(1/n\) for the uniform case. This checks the finite coloring equivalence but is not a proof of almost-sure convergence or of the Poisson limit. The latter rely on the union bounds, conditional independence, Borel–Cantelli, and explicit dependency-graph calculation above.

To replay, run `python checker.py` with a standard Python 3 interpreter (no third-party packages).

## Relationship to prior work

Kingman's paintbox and the Ewens partition representation are classical, as expounded by Pitman, *Combinatorial Stochastic Processes* (2006), Chapters 2 and 3. Arratia, Barbour and Tavaré (2006) establish convergence of random-permutation cycle-size proportions to Poisson–Dirichlet\((1)\). Longest iid head runs and their extreme-value behavior are classical (Gordon, Schilling and Waterman, 1986). Kong's 2016 paper supplies exact finite-alphabet, fixed-composition formulas for longest multicolor runs. These ingredients are acknowledged; the specific longest **numerically consecutive co-cycle interval** in an Ewens partition, its random largest-atom logarithmic scale, and its paintbox-dependent Poisson onset are the present statement. This is not a longest increasing subsequence, a one-line monotone run, or a string of successor edges of the permutation.

## Limitations

The almost-sure statement uses a coherent Ewens coupling. The quenched Poisson onset is along paintbox-dependent integer thresholds for which the limiting intensity exists; it does not assert that the centered maximum has a universal nonlattice Gumbel distribution. Rates in the Poisson approximation are conditional, not uniform over all paintbox realizations. The exact finite-size run distributions are already accessible through general conditional word formulas; this result is an asymptotic synthesis. Historical priority and whether an older general exchangeable-word extreme theorem subsumes the specific conclusion require further independent assessment.

## References

- J. Pitman, *Combinatorial Stochastic Processes*, 2006, Chapters 2–3, https://www.stat.berkeley.edu/~aldous/206-Exch/Papers/pitman_CSP.pdf.
- R. Arratia, A. D. Barbour and S. Tavaré, *A Tale of Three Couplings: Poisson–Dirichlet and GEM Approximations for Random Permutations*, *Combinatorics, Probability and Computing* 15 (2006), 31–62, https://www.columbia.edu/cu/simontavare/STpapers-pdf/ABT06.pdf.
- Y. Kong, *The mth longest runs of multivariate random sequences*, online 1 February 2016, *Annals of the Institute of Statistical Mathematics* 69 (2017), 497–512, https://doi.org/10.1007/s10463-015-0551-8. An author manuscript is available at https://arxiv.org/pdf/2405.01747.
- L. Gordon, M. F. Schilling and M. S. Waterman, *An extreme value theory for long head runs*, *Probability Theory and Related Fields* 72 (1986), 279–287, https://doi.org/10.1007/BF00699107.
