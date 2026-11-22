# Batch record breaking: an exact marked Stirling law and a Gaussian–Pareto limit

## Finding

Let \(X_1,\ldots,X_n\) be independent identically distributed observations from an arbitrary continuous distribution, where \(n\ge3\) and \(2\le m<n\). An *upper record* at position \(i\) is an observation strictly larger than all preceding observations. Delete the initial \(m\) observations, retaining the order of the remaining sample. Let \(K_{n,m}\) be the number of positions in the retained sample that become upper records but were not records in the original sample. Write \(M_m=\max(X_1,\ldots,X_m)\), and let \(J\) be the first index \(j>m\) with \(X_j>M_m\), with \(J=n+1\) when there is no such index through \(n\). Thus \(J\) marks the first point where the two record histories agree again.

Let \(c(\ell,k)\) be the unsigned Stirling number of the first kind, with \(c(0,0)=1\), and set \(r_\ell(k)=c(\ell,k)/\ell!\) for \(\ell\ge0\). The following joint law is exact and distribution-free:

\[
\begin{aligned}
\Pr\{K_{n,m}=k,J=j\}&=\frac{m}{j(j-1)}\,r_{j-m-1}(k),&&m+1\le j\le n,\\
\Pr\{K_{n,m}=k,J=n+1\}&=\frac mn\,r_{n-m}(k).
\end{aligned}
\]

Out-of-range values have probability zero. In particular,
\[
\Pr\{K_{n,m}=0\}=\frac1{m+1},\qquad
\mathbb E K_{n,m}=H_m+H_{n-m}-H_n,
\]
where \(H_s=\sum_{j=1}^s1/j\).

Extend the same i.i.d. sequence indefinitely, and count the records in the suffix before its first observation exceeding \(M_m\). Denote this count by \(K_{\infty,m}\). There are independent zero-based geometric random variables \(G_1,\ldots,G_m\), with
\[
\Pr\{G_j=k\}=\frac{j}{j+1}\left(\frac1{j+1}\right)^k,\quad k\ge0,
\]
such that
\[
K_{\infty,m}\ \stackrel{\mathrm d}=\ \sum_{j=1}^mG_j,\qquad
\mathbb E z^{K_{\infty,m}}=\prod_{j=1}^m\frac{j}{j+1-z},\qquad
 d_{\mathrm{TV}}\bigl(\mathcal L(K_{n,m}),\mathcal L(K_{\infty,m})\bigr)\le\frac mn.
\]
Consequently \(\mathbb E K_{\infty,m}=H_m\) and \(\operatorname{Var}(K_{\infty,m})=H_m+H_m^{(2)}\), where \(H_m^{(2)}=\sum_{j=1}^m1/j^2\). If \(m=m_n\to\infty\) and \(m_n/n\to0\), then
\[
\frac{K_{n,m_n}-H_{m_n}}{\sqrt{H_{m_n}+H_{m_n}^{(2)}}}\ \xrightarrow{\mathrm d}\ N(0,1).
\]

There is also a different, fully finite-horizon, marked limit for a *macroscopic* deleted prefix. If \(m_n/n\to\alpha\in(0,1)\), put \(C_n=\min(J/n,1)\). Then
\[
\left(\frac{K_{n,m_n}-\log n}{\sqrt{\log n}},C_n\right)
\xrightarrow{\mathrm d}(Z,C_\alpha),
\]
where \(Z\sim N(0,1)\) is independent of \(C_\alpha\), and \(C_\alpha\) has density \(\alpha t^{-2}\) on \(\alpha<t<1\), together with an atom of mass \(\alpha\) at \(t=1\). Equivalently, \(\Pr\{C_\alpha>t\}=\alpha/t\) for \(\alpha<t<1\). The atom represents failure to recover the original prefix maximum by the end of the sample. The recovery time is not Gaussian, despite its asymptotic independence from the Gaussian number of exposed records.

## Assumptions and scope

The distribution of the observations is common, continuous, and otherwise arbitrary. Continuity excludes ties almost surely, and the probability integral transform reduces all rank statements to independent \(\operatorname{Uniform}(0,1)\) variables. The finite joint identity is asserted for integers \(n\ge3\), \(2\le m<n\), and all integer \(k\ge0\). The auxiliary infinite-suffix coupling is formed on the same i.i.d. probability space. All limits refer to \(n\to\infty\). The case \(m=1\) satisfies the same algebra but is already covered at the level of its marginal record-breaking law by the cited one-arrival literature and is not asserted as new.

## Proof

**1. Record-exposure identity.** Write \(A_i\) for the indicator that \(i>m\) is an upper record of the suffix and \(B_i\) for the indicator that it is an upper record of the original sample. Every original record in the suffix is a suffix record, so \(B_i\le A_i\). Before the first \(X_j>M_m\), all suffix records have values below \(M_m\), hence \(A_i-B_i=A_i\). At \(j=J\), the sample maxima of both histories agree; every later record indicator then agrees. Therefore \(K_{n,m}\) equals the number of suffix records at positions \(m+1,\ldots,J-1\), or all suffix records if \(J=n+1\).

**2. Exact marked law.** For \(m+1\le j\le n\), the event \(J=j\) says that the maximum of the first \(j-1\) observations lies among the initial \(m\), and that the \(j\)-th observation exceeds this maximum. Uniform relative ranks give
\[
\Pr\{J=j\}=\frac1j\frac{m}{j-1}=\frac{m}{j(j-1)}.
\]
The no-recovery event says the overall maximum is in the deleted prefix, so \(\Pr\{J=n+1\}=m/n\). Conditional on either event, the relative order of observations in the pre-recovery suffix block remains uniform by permutation symmetry: the condition only compares its maximum with values in other blocks. Hence the count of upper records within a block of length \(\ell\) has the usual distribution \(r_\ell(k)=c(\ell,k)/\ell!\), proving the displayed joint laws, including \(\ell=0\). This argument also proves the marks sum to one by telescoping \(\sum_{j=m+1}^{n}m/[j(j-1)]=1-m/n\).

Only \(J=m+1\) permits \(K_{n,m}=0\), since every nonempty suffix block has at least one record. Thus \(\Pr\{K_{n,m}=0\}=\Pr\{J=m+1\}=1/(m+1)\). For a fixed suffix index \(i\), the probability of being its relative record is \(1/(i-m)\), whereas the probability of being an original record is \(1/i\). Subtracting and summing yields
\[
\mathbb EK_{n,m}=\sum_{i=m+1}^n\left(\frac1{i-m}-\frac1i\right)=H_m+H_{n-m}-H_n.
\]

**3. Infinite-horizon geometric factorization.** After the probability integral transform, let \(U\) denote a suffix record value. The next suffix record is uniformly distributed on \((U,1)\), conditional on \(U\). Consequently its increment in the coordinate \(-\log(1-U)\) is an independent unit-rate exponential variable; the first suffix record has this same transformed law. Thus transformed suffix record values are the arrival times of a rate-one Poisson process, independent of the deleted-prefix maximum. The transformed threshold \(T=-\log(1-M_m)\) has CDF \((1-e^{-t})^m\), the distribution of the maximum of \(m\) independent unit-rate exponentials. Hence \(K_{\infty,m}\mid T\sim\operatorname{Poisson}(T)\) and
\[
\mathbb E z^{K_{\infty,m}}=m\int_0^1u^{m-1}(1-u)^{1-z}\,du
=\frac{m!\,\Gamma(2-z)}{\Gamma(m+2-z)}
=\prod_{j=1}^m\frac{j}{j+1-z}.
\]
Each factor is the generating function of the stated independent geometric variable. Differentiation gives the moments. On the event \(J\le n\), finite and infinite counts agree pathwise, so the mismatch probability is at most \(\Pr\{J=n+1\}=m/n\), giving the total-variation bound.

**4. Sublinear prefixes.** The independent geometric summands have variance \(1/j+1/j^2\) and a uniformly summable third absolute centered-moment bound \(O(1/j)\) for \(j\ge1\). Their total variance is \(H_m+H_m^{(2)}\sim\log m\), so Lyapunov's ratio is \(O((\log m)^{-1/2})\) and the independent-summand central limit theorem applies as \(m\to\infty\). The preceding total-variation coupling transfers convergence to finite \(K_{n,m}\) when \(m/n\to0\).

**5. Macroscopic prefixes and asymptotic independence.** Write \(m/n\to\alpha\in(0,1)\). For \(m\le r\le n\), the event that no later value has exceeded the deleted-prefix maximum by index \(r\) is exactly that the maximum of \(X_1,\ldots,X_r\) lies among the first \(m\), with probability \(m/r\). Hence, for \(\alpha<t<1\),
\[
\Pr\{C_n>t\}=\frac{m}{\lfloor nt\rfloor}\longrightarrow\frac\alpha t,
\]
while \(\Pr\{C_n=1\}\to\alpha\). This identifies the continuous density and atom of \(C_\alpha\).

Conditional on \(J=j\), the number of newly exposed records has the law of the record count \(R_\ell\) of a uniform permutation of length \(\ell=j-m-1\), and for \(J=n+1\) it has the law of \(R_{n-m}\). The independent relative-rank representation gives \(R_\ell\stackrel{\mathrm d}=\sum_{i=1}^\ell\operatorname{Bernoulli}(1/i)\). For every fixed \(\delta>0\), uniformly for \(\delta n\le\ell\le n\), its mean \(H_\ell\) differs from \(\log n\) by a bounded constant, its variance is \(\log n+O_\delta(1)\), and the Lindeberg central limit theorem yields
\[
\frac{R_\ell-\log n}{\sqrt{\log n}}\xrightarrow{\mathrm d}N(0,1)
\]
uniformly over such \(\ell\). The probability of a recovered block shorter than \(\delta n\) is at most \(1-m/(m+\lceil\delta n\rceil)\to\delta/(\alpha+\delta)\). Taking \(n\to\infty\) and then \(\delta\downarrow0\) proves that the conditional Gaussian law becomes independent of the marked recovery index. Testing products of bounded continuous functions yields the asserted joint convergence.

## Verification

The self-contained Python 3 script `verify_prefix_records.py` performs exact rational checks over all \(n\in\{2,\ldots,8\}\) and \(1\le m<n\). It enumerates every permutation of the ranks, computes the actual record exposure and recovery position, and compares the resulting entire joint distribution to the unsigned-Stirling formula. It independently checks the exact expectation, recovery-position law, and a finite set of geometric-product coefficients. Run `python3 verify_prefix_records.py`. The supplied run passed 406 finite joint-law assertions and 30 product consistency assertions. These finite computations are not substitutes for the all-size proofs or the infinite-limit arguments.

## Relationship to prior work

The classical positional-record and Stirling formulas are due to Rényi and are developed, for example, in Wilf (1995) and Myers and Wilf (2007). Ahsanullah, Nevzorov and Nevzorova (2014) treat record-value transformations and distributional characterizations; their paper does not state the batch-deletion/recovery-time law. Naiman and Torcaso (2022) proved a geometric limit for the number of current records destroyed by **one** newly arriving observation. A subsequent published analysis gives exact finite one-arrival identities and a sharp total-variation rate for that same case. By reversing temporal order, its one-arrival count is the marginal \(m=1\) case here, **so that case is covered prior work, not part of the new contribution**. The contribution assessed here is the all-batch exact joint count/recovery-time law for \(m\ge2\), its factorized infinite-batch law, the sublinear-prefix coupling/CLT, and the macroscopic independent Gaussian–Pareto marked limit. None of the inspected primary statements supplies these multi-arrival assertions. No independent certification of historical priority is claimed.

## Limitations

The results concern i.i.d. continuously distributed scalar observations, a contiguous initial block of deletions, and upper records. Arbitrary internal deletions, ties, nonidentical or dependent samples, and vector-valued Pareto records are outside scope. The bound \(m/n\) is a valid total-variation upper bound, not a claim of optimal sharpness. The Gaussian limit applies only in the stated growing-prefix regimes; the exact marked distribution covers every finite admissible \((n,m)\). The one-arrival geometric law is known and not asserted as new. Literature not retrieved or differently indexed may contain stronger results, and independent mathematical audit has not been performed.

## References

1. H. S. Wilf, *On the outstanding elements of permutations* (manuscript dated January 1995), https://www2.math.upenn.edu/~wilf/website/outstelmts.pdf.
2. A. Myers and H. S. Wilf, *Left-to-right maxima in words and multiset permutations*, arXiv:math/0701078v1 (2007-01-03), https://arxiv.org/abs/math/0701078.
3. M. Ahsanullah, V. B. Nevzorov and L. Nevzorova, *Characterizations of distributions via record values with random exponential shifts*, *Journal of Statistical Theory and Applications* 13 (2014), 311–316, published 2014-12-30, https://doi.org/10.2991/jsta.2014.13.4.4.
4. D. Q. Naiman and F. Torcaso, *A Geometric(1/2) Distribution Associated with Record Breaking*, arXiv:2210.08426v1 (2022-10-16), https://arxiv.org/html/2210.08426v1.
5. *Sharp total-variation convergence for the number of records broken by an observation* (published research record), https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-sharp-total-variation-convergence-for-the-number-of-records-brok--3626aee77ba9/RESULT.md.
