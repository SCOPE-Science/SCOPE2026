# Sharp log-periodic covariance of part count and maximum in uniform compositions

## Finding

Choose uniformly from the \(2^{N-1}\) unrestricted positive-integer compositions of \(N\). Let \(K_N\) be its number of parts and \(M_N\) its largest part. Write \(n=N-1\), \(m=\lfloor\log_2 n\rfloor\), and \(\theta=\{\log_2 n\}\). Define the positive, continuous, one-periodic function
\[
h(\theta)=\sum_{j\in\mathbb Z}2^{\theta-1-j}\exp(-2^{\theta-1-j}).
\]
For \(\theta\in[0,1]\), define an integer-valued law \(Z_\theta\) by
\[
\Pr(Z_\theta<j)=\exp(-2^{\theta-1-j}),\qquad j\in\mathbb Z,
\]
and put \(v(\theta)=\operatorname{Var}(Z_\theta)>0\). Then, as \(N\to\infty\), uniformly over the phase \(\theta=\{\log_2(N-1)\}\),
\[
\boxed{\operatorname{Cov}(K_N,M_N)=-\frac{\log_2 n}{2}\,h(\theta)+o(\log n)}
\]
and
\[
\boxed{\operatorname{Corr}(K_N,M_N)=-\frac{\log_2 n}{\sqrt n}\,\frac{h(\theta)}{\sqrt{v(\theta)}}\,(1+o(1)).}
\]
In particular, \(\operatorname{Corr}(K_N,M_N)=-\Theta((\log N)/\sqrt N)\), and \(\operatorname{Corr}(K_N,M_N)(\ln N)^{5/2}\to0\). This excludes the previously proposed asymptotic \(C(\ln N)^{-5/2}\) for any fixed \(C<0\).

The oscillatory covariance profile is genuinely nonconstant. Its Fourier coefficients are \(\widehat h(\ell)=\Gamma(1-2\pi i\ell/\ln2)/\ln2\), which are nonzero for all integer \(\ell\).

## Assumptions and scope

The random composition is uniform and unrestricted. Results concern the joint law of its number of parts and its largest part, not the analogous model disallowing parts of size one. All asymptotic statements hold along the complete integer sequence \(N\to\infty\), with the explicit phase retained; there is no claim of a phase-independent variance limit. The correlation formula is interpreted with its positive phase-dependent denominator.

## Proof

**1. Bernoulli coupling and exact finite representation.** Insert an independent fair cut indicator after each of the first \(n=N-1\) unit positions. For independent bits \(X_1,\dots,X_n\), put \(S_n=\sum_iX_i\) and let \(R_n\) be the maximum number of consecutive zeros (zero if all bits are one). Then \((K_N,M_N)\) has the law of \((1+S_n,1+R_n)\). For \(p\in(0,1)\), temporarily replace fair bits by independent Bernoulli-\(p\) bits, write \(q=1-p\), and set \(F_{n,r}(p)=\Pr_p(R_n<r)\).

For every integer \(1\le r\le n\), inclusion–exclusion over beginnings of long zero-runs preceded by a one or by the left boundary gives the **exact polynomial**
\[
F_{n,r}(p)=1+\sum_{k=1}^{\lfloor n/r\rfloor}(-1)^k q^{kr}
\left[p^k\binom{n-kr}{k}+p^{k-1}\binom{n-kr}{k-1}\right].\tag{1}
\]
Indeed, two specified starts must be separated by at least \(r+1\) sites. The first binomial counts sets of \(k\) starts excluding the boundary, each with its preceding one; the second counts sets including the boundary, so only \(k-1\) preceding ones are imposed. Their remaining unspecified bits integrate to probability one. The score identity for Bernoulli product measures is
\[
\operatorname{Cov}_p(S_n,G)=pq\,\frac{\mathrm d}{\mathrm dp}\mathbb E_p G
\]
for any fixed statistic \(G\). Since \(R_n=\sum_{r=1}^{n}(1-\mathbf1_{\{R_n<r\}})\),
\[
\boxed{\operatorname{Cov}(K_N,M_N)=-\frac14\sum_{r=1}^{n}F'_{n,r}(1/2).}\tag{2}
\]

**2. Fixed-phase local asymptotics.** Put \(m=\lfloor\log_2 n\rfloor\), \(\theta=\log_2 n-m\), and \(r=m+j\) for a fixed integer \(j\). Then \(r/m\to1\), and \(n(1/2)2^{-r}\to x_j=2^{\theta-1-j}\), with \(\theta\) allowed to vary in \([0,1]\). In (1), for each fixed \(k\), the no-boundary summand tends to \((-1)^kx_j^k/k!\), and the boundary summand is \(o(1)\). Differentiating the \(k\)-th term at \(p=1/2\) and dividing by \(m\), the factor from \(q^{kr}\) tends to \(-2k\) and all other differentiated factors contribute \(o(1)\). The terms and their scaled derivatives are dominated, for fixed \(j\), by \(C_j^k(1+k)/k!\). Hence termwise limiting and summation yield, uniformly in \(\theta\),
\[
F_{n,m+j}(1/2)=e^{-x_j}+o(1),\qquad
\frac{F'_{n,m+j}(1/2)}m=2x_je^{-x_j}+o(1).\tag{3}
\]

**3. Uniform summable tail for derivatives.** The pivotal-coordinate formula gives \(F'_{n,r}(1/2)\ge0\). An individual bit can be pivotal for absence of an \(r\)-zero run only if forcing it to zero places it inside one of at most \(r\) possible all-zero \(r\)-windows. This local event has probability at most \(r2^{-(r-1)}\). If \(r\le n/8\), there is a disjoint contiguous segment of length at least \(n/4\) outside the pivotal bit's \(r\)-neighborhood. Pivotality also forces this segment to contain no \(r\)-zero run, independently of the local event.

For any independent fair-bit segment of length \(t\), consider its first \(\lfloor t/4\rfloor\) complete zero-runs terminated by a one. A binomial Chernoff bound shows that these runs do not all finish by time \(t\) with probability at most \(e^{-ct}\). Otherwise all those independent geometric runs must have length below \(r\), an event of probability at most \(\exp(-\lfloor t/4\rfloor 2^{-r})\). Thus, for a universal \(c>0\),
\[
0\le F'_{n,r}(1/2)\le Cnr2^{-r}\big(\exp(-cn2^{-r})+e^{-cn}\big),\quad 1\le r\le n/8.\tag{4}
\]
For \(r>n/8\), the simpler bound \(F'_{n,r}(1/2)\le Cnr2^{-r}\) suffices. When \(r=m+j\), division by \(m\) makes the positive-\(j\) tail bounded by \(C(1+j)2^{-j}\) and the negative-\(j\) tail by \(C2^{-j}e^{-c2^{-j}}\); the \(e^{-cn}\) terms and \(r>n/8\) contribute \(o(1)\) to the normalized sum. Both bounding sequences are summable. Therefore (2)–(4) imply uniformly in phase
\[
\frac{\operatorname{Cov}(K_N,M_N)}m
=-\frac12\sum_{j\in\mathbb Z}x_je^{-x_j}+o(1)
=-\frac{h(\theta)}2+o(1),
\]
proving the covariance assertion.

**4. Variance and correlation.** The fixed-phase distributional limit in (3) gives \(R_n-m\Rightarrow Z_\theta\) along every sequence whose phases tend to \(\theta\). To pass to moments, a union bound gives \(\Pr(R_n\ge r)\le n2^{-r}\); the same geometric-run argument gives \(\Pr(R_n<r)\le \exp(-cn2^{-r})+e^{-cn}\). These provide uniform geometric upper tails and doubly exponential lower tails for \(R_n-m\), including uniform integrability of the second moments. Consequently
\[
\operatorname{Var}(R_n)=v(\theta)+o(1)
\]
uniformly in phase (by compactness and subsequences). The integer law is nondegenerate, so \(v(\theta)>0\); it and \(h(\theta)\) are continuous, one-periodic and bounded away from zero on the circle. Since \(\operatorname{Var}(K_N)=n/4\), correlation is the covariance divided by \((\sqrt n/2)\sqrt{v(\theta)+o(1)}\), establishing the displayed formula and the rejection of the proposed slower decay.

For the Fourier claim, substitute \(u=2^{\theta-1-j}\) in the period integral. Unfolding the sum over \(j\) converts its \(\ell\)-th Fourier coefficient into \((\ln2)^{-1}\int_0^\infty e^{-u}u^{-2\pi i\ell/\ln2}\,\mathrm du\), the stated Gamma value. The Gamma function has no zeros.

## Verification

The standalone \(\texttt{verify.py}\) compares (1) and its derivative with exhaustive enumeration of all binary words through length nine using exact rational arithmetic (45 threshold-length comparisons). It also checks the covariance extracted from the derivatives for four bits and independently computes correlations from a trailing-zero-state recursion for lengths 100, 200 and 1000, matching the first, second and tenth unrestricted numerical entries of Finch's published table within stated rounding tolerance. Execute \(\texttt{python3 verify.py}\) with Python 3; no external packages are needed. These finite checks support the algebra, while the uniform tail bounds and limiting argument establish the infinite-sequence theorem.

## Relationship to prior work

Finch's “Covariance within Random Integer Compositions” (first released 2020-10-13, arXiv:2010.06643) treats precisely \((K_N,M_N)\), tabulates correlations and conjectures \(\rho(N)\sim C(\ln N)^{-5/2}\) for an unspecified negative constant; the proposed order conflicts with the sharp decay proved here. A related published treatment, “Rigorous decorrelation of part count and maximum in uniform compositions,” establishes stochastic antitonicity and the bound \(0<-\operatorname{Cov}(K_N,M_N)=O((\log N)^2)\), hence root-\(N\) polylogarithmic decorrelation, explicitly without a matching lower asymptotic. Its full proof and scope do not imply the present sharp logarithmic-order coefficient or nonconstant periodic profile. Philippou and Makri (1986) gave exact conditional run-length distributions, valuable prior art for finite joint laws rather than a stated sharp covariance asymptotic.

## Limitations

This treats only unrestricted uniform compositions, not compositions with minimum part size two or biased cuts. The phase-dependent constants are specified by convergent series and a discrete extreme-value law rather than a phase-independent numerical constant. Historical priority cannot be guaranteed against implicit older run-statistics derivations, particularly the exact conditional-law literature. No independent scientific audit has been performed.

## References

1. S. R. Finch, “Covariance within Random Integer Compositions,” arXiv:2010.06643, version 1 submitted 2020-10-13; version 2 2020-10-19, especially p. 3.
2. “Rigorous decorrelation of part count and maximum in uniform compositions,” public mathematical record `2026/10/4/SCOPE-rigorous-decorrelation-of-part-count-and-maximum-in-uniform-comp--0ee24a72cd31`, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-rigorous-decorrelation-of-part-count-and-maximum-in-uniform-comp--0ee24a72cd31 .
3. A. N. Philippou and F. S. Makri, “Successes, runs and longest runs,” *Statistics & Probability Letters* 4 (1986), 101–105 and 211–215 (corrected issue); DOI 10.1016/0167-7152(86)90069-6.
4. M. F. Schilling, “The Longest Run of Heads,” *The College Mathematics Journal* 21 (1990), 196–207, DOI 10.1080/07468342.1990.11973306.
