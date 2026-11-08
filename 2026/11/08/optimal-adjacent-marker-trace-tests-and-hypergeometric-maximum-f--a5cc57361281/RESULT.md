# Optimal adjacent-marker trace tests and hypergeometric maximum formula

## Finding

For independent binary deletions with retention probability \(p\in(0,1)\), the two sources containing a unique \(1\) at adjacent locations admit a likelihood-ratio test independent of the channel retention probability, for any number of independent traces. Their exact one-trace total variation distance has both a binomial-expectation expression and a hypergeometric maximum formula for arbitrary adjacent locations; in the central case it reduces to a two-mass binomial difference law, with an exact closed form at retention \(1/2\). The central one-trace total variation and squared Hellinger distances have respectively sharp \(r^{-1/2}\) and \(r^{-1}\) constants.

Explicitly, for integers \(n\ge2\) and \(1\le i<n\), let \(e_i=0^{i-1}10^{n-i}\) and \(e_{i+1}=0^{i}10^{n-i-1}\). Let \(P_i,P_{i+1}\) be their one-trace laws, and write \(d_{n,i}(p)=\|P_i-P_{i+1}\|_{\mathrm{TV}}\). For independent \(U\sim\operatorname{Bin}(i,p)\) and \(V\sim\operatorname{Bin}(n-i,p)\),

\[
d_{n,i}(p)=\frac{p}{2(1-p)}\mathbb E\left|\frac{U}{i}-\frac{V}{n-i}\right|.
\]

A second, more concentrated expression is available. Put \(a=i-1\), \(b=n-i-1\), \(m=n-2\), and define

\[
G_{n,i}(p)=p^2\sum_{t=0}^{m}p^t(1-p)^{m-t}
\max_{\max(0,t-b)\le u\le\min(a,t)}\binom{a}{u}\binom{b}{t-u}.
\]

Then \(d_{n,i}(p)=G_{n,i}(p)\) for every permitted \(n,i,p\). Thus the exact total variation is a weighted maximum-coefficient profile of hypergeometric point masses. In particular, it can be evaluated with finite integer binomial coefficients, without enumerating exponentially many traces.

If a nonzero received trace has \(u\) zeros before its unique \(1\) and \(v\) zeros after it, the equal-prior optimal decision selects \(e_i\) exactly when \(iv\ge(n-i)u\), apart from arbitrary tie-breaking. For any number of independent traces, multiply the individual likelihood ratios below; every such optimal decision rule is independent of \(p\).

For \(n=2r\), \(i=r\), \(r\ge1\), and \(b_k=\Pr\{\operatorname{Bin}(r-1,p)=k\}\), setting \(b_r=0\),

\[
d_{2r,r}(p)=p^2\left(\sum_{k=0}^{r-1}b_k^2+\sum_{k=0}^{r-2}b_kb_{k+1}\right),
\qquad d_{2r,r}(1/2)=\frac{\binom{2r-1}{r}}{2^{2r}}.
\]

Let \(A_r(p)=\sum_y\sqrt{P_r(y)P_{r+1}(y)}\) for this central pair and \(H_r^2(p)=1-A_r(p)\). Define

\[
S_r(p)=\sum_{k=0}^{r}\sqrt{\Pr\{\operatorname{Bin}(r-1,p)=k\}\Pr\{\operatorname{Bin}(r,p)=k\}}.
\]

Then \(A_r(p)=1-p+pS_r(p)^2\), and for fixed \(0<p<1\) as \(r\to\infty\),

\[
\sqrt r\,d_{2r,r}(p)\longrightarrow\frac{p^{3/2}}{\sqrt{\pi(1-p)}},\qquad
rH_r^2(p)\longrightarrow\frac{p^2}{4(1-p)}.
\]

For \(m_r/r\to t\ge0\), the affinity between the two \(m_r\)-trace product laws converges to \(\exp[-tp^2/(4(1-p))]\). The exact equal-prior minimum one-trace classification error is \((1-d_{n,i}(p))/2\).

## Assumptions and scope

Every bit is independently retained with the same probability \(p\in(0,1)\); deletion does not substitute, reorder, or insert. Length \(n\) and the adjacent candidate marker positions \(i,i+1\) are known. Empty traces are allowed. The observation of a retained marker is its ordered output string, without original indices. The test uses equal prior probabilities on the two candidate source strings; its likelihood-ratio ordering also applies to arbitrary prescribed prior odds. Distances are over full probability distributions on variable-length traces, with total variation \(\frac12\sum_y|P(y)-Q(y)|\) and squared Hellinger \(1-\sum_y\sqrt{P(y)Q(y)}\). The sharp asymptotic statements fix \(p\) while \(r\) grows.

## Proof

**1. Likelihood and channel-independent optimal test.** On a trace without a \(1\), the two laws agree exactly: the unique marker was deleted, and the \(n-1\) remaining zero positions undergo the same independent retention trials. On a trace of form \(0^u10^v\), with \(u,v\ge0\), let \(c=p^{u+v+1}(1-p)^{n-u-v-1}\). Its two probabilities are

\[
P_i(0^u10^v)=c\binom{i-1}{u}\binom{n-i}{v},\qquad
P_{i+1}(0^u10^v)=c\binom{i}{u}\binom{n-i-1}{v}.
\]

Binomial coefficients outside their natural ranges are zero. On the joint support, their likelihood ratio, interpreted in the extended nonnegative reals, is

\[
\frac{P_i(0^u10^v)}{P_{i+1}(0^u10^v)}
=\frac{(i-u)(n-i)}{i(n-i-v)}.
\]

A trace outside the union of supports is irrelevant. The ratio exceeds, equals, or falls below one according as \(iv-(n-i)u\) is positive, zero, or negative. The common factor \(c\) cancels, so this test does not need \(p\). For \(m\) independent traces, the joint likelihood ratio is the product of the individual ratios; a zero-marker trace contributes one, proving the asserted rate-independent optimal test at every sample size.

**2. Arbitrary-position total variation.** Use the reference joint law of independent \(U\sim\operatorname{Bin}(i,p)\) and \(V\sim\operatorname{Bin}(n-i,p)\). The two surviving-marker trace masses, relative to this reference law, are respectively

\[
\frac{p(i-U)}{i(1-p)},\qquad \frac{p(n-i-V)}{(n-i)(1-p)}.
\]

This follows from \(\binom{i-1}{u}/\binom iu=(i-u)/i\) and the additional \((1-p)^{-1}\) factor. Since all marker-deleted masses cancel in total variation, taking one half the absolute mass difference and summing gives the formula for \(d_{n,i}(p)\). All boundary values \(u=i\) and \(v=n-i\) are included because the corresponding density factor vanishes.

**3. Hypergeometric maximum identity.** Let \(X\sim\operatorname{Bin}(i-1,p)\), \(Y\sim\operatorname{Bin}(n-i-1,p)\), and \(B\sim\operatorname{Bern}(p)\) independent. Conditional on retaining the marker, the two trace-coordinate laws are \((X,Y+B)\) and \((X+B,Y)\). Their common \(B=0\) component cancels pointwise; the remaining difference has weight \(p\) in addition to marker-survival weight \(p\). Hence

\[
d_{n,i}(p)=p^2\|\mathcal L(X,Y+1)-\mathcal L(X+1,Y)\|_{\mathrm{TV}}.
\]

Let \(T=X+Y\), so \(T\sim\operatorname{Bin}(n-2,p)\), and conditional on \(T=t\) the count \(X\) has the hypergeometric point masses

\[
h_t(u)=\frac{\binom{a}{u}\binom{b}{t-u}}{\binom{m}{t}}.
\]

The two conditional laws on the same sum \(t+1\) shift the count by one. Because the hypergeometric masses are unimodal in \(u\), their shift distance satisfies \(\frac12\sum_u|h_t(u)-h_t(u-1)|=\max_u h_t(u)\), with out-of-range masses interpreted as zero. Averaging over \(T\) and canceling \(\binom mt\) yields the displayed exact maximum-coefficient formula. This is an all-position formula, not just a central-pair reduction.

**4. Exact central total variation.** Set \(a=r-1\), let \(X,X'\) be independent \(\operatorname{Bin}(a,p)\) variables, and independently \(B\sim\operatorname{Bern}(p)\). Conditional on retaining the marker, one law is that of \((X,X'+B)\) and the other that of \((X'+B,X)\). The ratio between successive binomial sizes is increasing with the count; consequently the signed difference is positive on \(u<v\) and negative on \(u>v\). Conditional total variation is \(\Pr(X<X'+B)-\Pr(X>X'+B)\). On \(B=0\) this difference vanishes by exchangeability. On \(B=1\) it is \(\Pr(X-X'=0)+\Pr(X-X'=1)\). Multiplying by the marker-survival probability \(p\) yields \(p^2(\sum b_k^2+\sum b_kb_{k+1})\). When \(p=1/2\), Vandermonde convolution gives \(\sum b_k^2=4^{-a}\binom{2a}{a}\) and \(\sum b_kb_{k+1}=4^{-a}\binom{2a}{a-1}\). Pascal's identity gives the stated closed form.

**5. Exact Hellinger affinity.** In the marker-deleted event, total common mass is \(1-p\). In the surviving-marker event, the conditional laws are product measures with the two \(\operatorname{Bin}(r-1,p)\) and \(\operatorname{Bin}(r,p)\) coordinates swapped. Their affinity is the square of their one-coordinate affinity \(S_r(p)\). Hence \(A_r(p)=1-p+pS_r(p)^2\).

**6. Sharp asymptotics.** The difference \(X-X'\) is an aperiodic centered integer-valued random variable with variance \(2(r-1)p(1-p)\). The lattice local central limit theorem implies, for fixed \(j\in\{0,1\}\),

\[
\Pr(X-X'=j)=\frac{1+o(1)}{\sqrt{4\pi(r-1)p(1-p)}}.
\]

Using step 4 proves the total-variation constant. For the affinity, if \(K\sim\operatorname{Bin}(r,p)\), the binomial probability ratio yields

\[
S_r(p)=\mathbb E\sqrt{Z_r},\qquad Z_r=\frac{r-K}{r(1-p)}.
\]

Here \(\mathbb EZ_r=1\), \(\operatorname{Var}(Z_r)=p/[r(1-p)]\), and the centered third absolute moment is \(O_p(r^{-3/2})\). On the high-probability event \(|Z_r-1|\le1/2\), Taylor's theorem with bounded third derivative gives

\[
\mathbb E\sqrt{Z_r}=1-\frac{p}{8r(1-p)}+o(r^{-1}).
\]

The complementary event contributes \(o(r^{-1})\) by exponential binomial concentration and boundedness of \(\sqrt{Z_r}\) for fixed \(p\). Squaring and substituting into step 5 yields \(H_r^2=p^2/[4r(1-p)]+o(r^{-1})\). Affinity tensorizes for independent traces, so \(A_r^{m_r}\to\exp[-tp^2/(4(1-p))]\). Finally the optimal equal-prior testing error identity follows directly by summing the pointwise minima of the two trace masses.

## Verification

The standalone `check_trace.py` enumerates all deletion masks exactly using rational probabilities for every adjacent marker pair at lengths \(2\) through \(9\) and retention values \(1/4,1/2,2/3\) (108 pairs in total). For each it checks normalization, the likelihood-sign rule, and both general total-variation identities, including the hypergeometric maximum formula. For central pairs it additionally checks the finite binomial-difference formula, the closed form at \(1/2\), and the affinity against direct enumeration. It prints convergence diagnostics for three values of the retention probability at central half-lengths \(10,40,100\). These computations check finite instances only; the proof above supplies the general and asymptotic claims. Reproduce with `python3 check_trace.py` using Python's standard library, in the directory containing the extracted file.

## Relationship to prior work

McGregor, Price and Vorotnikova (2014), Section 3.3 and Lemma 11, already introduced precisely the central adjacent-marker source pair and identified its two product-binomial trace laws, establishing an \(O(r^{-1})\) squared Hellinger bound. Therefore the existence of this indistinguishable pair, its conditional binomial structure, and an order bound are *not* new. The exact central affinity identity here is an explicit evaluation of their stated product structure, not a separate novelty claim. The additional result is a unified sharp decision-theoretic description: an optimal retention-rate-free likelihood test for *all adjacent positions and all sample counts*, arbitrary-position exact total variation in two forms including a hypergeometric maximum-coefficient identity, the central two-probability binomial identity, the exact half-retention finite formula, and the leading constants for both distances and many-trace affinity. In particular, the 2014 central-pair law does not determine the general off-center hypergeometric maximum profile; its Hellinger order bound alone also does not quantify the exact Bayes risk or its likelihood rule. Rivkin, Valiant and Valiant (2024) study the related generalized trace channel and motivated renewed attention to quantitative distinguishability, but do not state this exact adjacent-marker testing theorem.

## Limitations

The result is restricted to hypotheses differing by moving a *single* marker one position in an otherwise zero word under homogeneous independent deletion. It is not a minimax theorem over all source pairs, does not recover an arbitrary unknown string, and does not supply a closed-form multi-trace total-variation distance. The constants require fixed interior retention probability; no uniformity as \(p\to0\) or \(p\to1\) is asserted. Classical 2014 source formulas nearly determine some intermediate identities, and a 2026 finite-computation report for length at most ten suggests priority risk for individual special numerical cases. Full historical priority remains to be checked independently.

## References

1. A. McGregor, E. Price, and S. Vorotnikova, *Trace Reconstruction Revisited*, European Symposium on Algorithms, 2014, Section 3.3, Lemma 11. Author manuscript: https://people.cs.umass.edu/~mcgregor/papers/14-esa.pdf
2. J. Rivkin, G. Valiant, and P. Valiant, *A Generalized Trace Reconstruction Problem: Recovering a String of Probabilities*, arXiv:2412.00674v1, publicly submitted 2024-12-01. https://arxiv.org/abs/2412.00674
3. X. Chen, A. De, C. H. Lee, R. A. Servedio, and S. Sinha, *Approximate Trace Reconstruction from a Single Trace*, SODA 2023, https://doi.org/10.1137/1.9781611977554.ch27
