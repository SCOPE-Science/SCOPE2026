# A sharp singleton–block covariance transition in size-conditioned noncrossing partitions

## Finding
For every integer \(n\ge5\) and \(3\le k\le n-2\), sample a uniform noncrossing partition of \([n]\) conditional on having \(K=k\) blocks. Write \(X_j\) for the number of size-\(j\) blocks. For every integer \(2\le s\le n-k+1\),
\[
\boxed{\operatorname{Cov}(X_1,X_s\mid K=k)=\frac{k(k-1)\binom{n-s-1}{k-2}}{\binom{n-1}{k-1}}\frac{ks-2(n-1)}{(n-1)(n-s-1)}.}
\]
Consequently the covariance is negative if \(ks<2(n-1)\), zero exactly if \(ks=2(n-1)\), and positive if \(ks>2(n-1)\). Since \(2<2(n-1)/k<n-k+1\), there is exactly one negative-to-positive threshold across the admissible block sizes, possibly with a zero at the threshold.

If \(k=k(n)\) and \(k/n\to\alpha\in(0,1)\), then for each fixed integer \(s\ge2\),
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(X_1,X_s\mid K=k)}{n}=\alpha^3(1-\alpha)^{s-1}(\alpha s-2).
\]
Thus the sign change persists when the conditioned number of blocks is proportional to the sample size. For instance, at the typical proportion \(\alpha=1/2\), the fixed-size asymptotic covariance is positive for every \(s\ge5\) and negative for \(s\in\{2,3\}\), while the first-order coefficient vanishes for \(s=4\).

## Assumptions and scope
A partition \(\pi\) of \([n]=\{1,\ldots,n\}\) is noncrossing when no two distinct blocks contain elements \(a<c\) and \(b<d\), respectively, with \(a<b<c<d\). Condition on the event \(K=k\), where \(K\) is the total number of blocks. Every such partition has equal probability. The range \(3\le k\le n-2\), \(2\le s\le n-k+1\) makes each binomial coefficient and denominator above well-defined and guarantees that both signs occur. No claim is made for the excluded degenerate cases without reformulation.

## Proof
**1. Count complete block-size profiles.** Introduce formal weights \(w_j\) for size-\(j\) blocks and let \(C(z;w)\) be their ordinary generating function by total size. Decomposing at the block containing the first element, with an independently noncrossing partition in each gap, gives
\[
C(z;w)=1+\sum_{j\ge1} w_j\bigl(zC(z;w)\bigr)^j.
\]
Set \(T=zC\) and \(\Phi(t)=1+\sum_{j\ge1}w_jt^j\); then \(T=z\Phi(T)\). Lagrange inversion yields
\[
[z^n]C(z;w)=\frac1{n+1}[t^n]\Phi(t)^{n+1}.
\]
Hence the number of noncrossing partitions with \(m_j\) blocks of size \(j\), where \(\sum_jm_j=k\) and \(\sum_j j m_j=n\), is exactly
\[
\frac{n!}{(n-k+1)!\prod_j m_j!}.
\]
This is the classical Kreweras block-type enumeration, rederived here to make the argument self-contained. After conditioning on \(K=k\), its profile probabilities are proportional to \(k!/\prod_jm_j!\). These are exactly the profile probabilities of a **uniform ordered positive composition** \((A_1,\ldots,A_k)\) of \(n\) after discarding the order. Therefore all symmetric size-count statistics have precisely the same conditional joint law in the two models.

**2. Mark a size-\(s\) part.** There are \(\binom{n-1}{k-1}\) positive compositions of \(n\) into \(k\) parts. A specified part has size \(s\) with probability
\[
p_s=\frac{\binom{n-s-1}{k-2}}{\binom{n-1}{k-1}},\qquad \mathbb E[X_s\mid K=k]=kp_s.
\]
Similarly \(\mathbb E[X_1\mid K=k]=k(k-1)/(n-1)\). Under size bias by \(X_s\), one selected size-\(s\) part is distinguished; the remaining \(k-1\) positive parts are uniformly composed from \(n-s\). Because \(s\ge2\), the marked part contributes no singleton, giving the size-biased singleton mean
\[
\frac{\mathbb E[X_1X_s\mid K=k]}{\mathbb E[X_s\mid K=k]}=\frac{(k-1)(k-2)}{n-s-1}.
\]
Subtracting the unconditional singleton mean and multiplying by \(\mathbb E[X_s\mid K=k]\) proves
\[
\operatorname{Cov}(X_1,X_s\mid K=k)=kp_s\frac{(k-1)\bigl(ks-2(n-1)\bigr)}{(n-1)(n-s-1)},
\]
which is the displayed formula.

**3. Signs and boundaries.** Both \(p_s\) and every denominator are strictly positive throughout the stated range. The remaining factor is affine and strictly increasing in \(s\). At \(s=2\), it is \(2(k-n+1)<0\). At \(s=n-k+1\), it equals \((k-2)(n-k-1)>0\). This proves a unique crossing, allowing one exact zero only if the threshold is integral.

**4. Density limit.** For fixed \(s\) and \(k/n\to\alpha\in(0,1)\), elementary ratios of binomial coefficients give \(p_s\to\alpha(1-\alpha)^{s-1}\). Divide the exact identity by \(n\) and pass to the limit to obtain the asymptotic assertion.

## Verification
An independent exact-rational enumerator (the standalone file `verify_noncrossing.py`) generates all set partitions, filters by the noncrossing condition, groups them by \(K\), and computes conditional covariances directly. It verifies all \(50\) admissible parameter triples for \(5\le n\le9\), against the closed formula, and checks profile-law equality with uniform positive compositions. There are \(6{,}895\) noncrossing partitions across these five sizes. A separate exact algebraic check tests the size-biased identity for \(5\le n\le200\). The universal proof above, rather than these finite tests, establishes all parameter values.

An illustrative reversal occurs at \(n=5\), \(k=3\), and \(s=3\): the conditional covariance is \(1/4\), whereas under a uniform **unconditioned** noncrossing partition on five points it is \(-5/42\) (direct enumeration of its \(42\) partitions). Moreover, infinitely many zero-covariance pairs are nevertheless dependent: for any \(m\ge2\), take \(k=3\), \(n=3m+1\), and \(s=2m\). Then \(ks=2(n-1)\), yet the event \(X_s>0\) excludes \(X_1=2\), which occurs with positive probability under \(K=3\).

## Relationship to prior work
Kreweras' classical noncrossing partition enumeration counts every block-size profile. Arizmendi (arXiv:1201.6576, Section 2) obtains first moments of counts of prescribed block sizes conditional on the block count; this is precisely the starting conditional law here. Kargin (arXiv:1907.00632, Section 2.2) computes unconditional covariances and asymptotic distributions of block-size counts in random noncrossing partitions. None of those identified statements gives the complete conditional singleton-versus-size sign classification or its zero criterion as a stated theorem. The contribution is the conditional **qualitative sign phase** and sharp finite threshold, not the pre-existing multitype enumeration.

## Limitations
No priority claim is made against uninspected literature; the exact conditional moment can also be recovered algebraically from Kreweras' general profile formula, so previously unnoticed formulations of the same sign classification are a genuine priority risk. The finite illustration does not assert an all-size unconditional covariance sign theorem. The limit concerns fixed \(s\) and \(k/n\to\alpha\in(0,1)\); it does not treat block sizes growing with \(n\). Independent scientific validation has not been performed.

## References
1. V. Kargin, *Limit theorems for statistics of non-crossing partitions*, first public version 2019-07-01, https://arxiv.org/abs/1907.00632 (especially Section 2.2).
2. O. Arizmendi, *Statistics of blocks in k-divisible non-crossing partitions*, https://arxiv.org/abs/1201.6576 (especially Proposition 2.1 and the standard block-type formula).
3. G. Kreweras, *Sur les partitions non croisées d'un cycle*, Discrete Mathematics 1 (1972), 333–350 (classical block-type enumeration).
