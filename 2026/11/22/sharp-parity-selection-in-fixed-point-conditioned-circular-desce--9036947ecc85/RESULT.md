# Sharp parity selection in fixed-point-conditioned circular descents

## Finding

Let \(\pi\) be uniformly random in the symmetric group on \(n\ge3\) labels. Define the number of fixed points
\[F=\sum_{i=1}^n\mathbf 1\{\pi(i)=i\}\]
and the **one-line circular descent count**
\[C=\sum_{i=1}^n\mathbf 1\{\pi(i)>\pi(i+1)\},\qquad \pi(n+1)=\pi(1).\]
The final wrap-around comparison is part of the definition. This is not the cycle-descent statistic defined by reading individual permutation cycles.

For an integer \(m\ge0\) put \(D_m=m!\sum_{j=0}^m(-1)^j/j!\), the derangement number. For each feasible \(F=k\) with \(m=n-k\ge2\), the exact conditional mean is
\[
\mathbb E[C\mid F=k]=\frac n2-\frac{k^2-3k+1}{2(n-1)}+\frac{(m-1)(-1)^m}{2(n-1)D_m}.
\]
The remaining feasible case \(k=n\) has \(\mathbb E[C\mid F=n]=1\). There is no permutation with exactly \(n-1\) fixed points.

The conditional mean has a **unique maximum** at \(k=1\) for every odd \(n\ge3\), and at \(k=2\) for every even \(n\ge4\). This parity alternation holds for every sample size; it is not just asymptotic.

More strongly, write \((F)_r=F(F-1)\cdots(F-r+1)\), with \((F)_0=1\). For \(0\le r<n\),
\[
\operatorname{Cov}((F)_r,C)=-\frac{\binom r2}{n-1},
\]
whereas \(\operatorname{Cov}((F)_n,C)=1-n/2\). Thus \(\operatorname{Cov}(F,C)=0\) but \(\operatorname{Cov}(F(F-1),C)=-1/(n-1)\).

## Assumptions and scope

The measure is uniform on all \(n!\) labeled permutations, without Ewens or derangement conditioning unless explicitly stated. The first result is a conditional expectation, not conditional stochastic ordering. We use the convention \(D_0=1,D_1=0\). For \(n=2\), circular descents are deterministic, so the parity-maximizer theorem is intentionally stated only for \(n\ge3\).

## Proof

**1. An exact forced-fixed-point regression.** Fix an integer \(0\le r<n\), and choose uniformly a subset \(S\subset[n]\) of \(r\) positions. Condition on every point of \(S\) being fixed. The remaining \(m=n-r\) positions carry a uniformly random permutation of their complement. Average over the uniformly chosen \(S\). For any ordinary adjacency \(i,i+1\) (\(1\le i<n\)), the probability of a descent is
\[
p_{\mathrm{line}}=\frac{(m-1)(m+2r)}{2n(n-1)}.
\]
Indeed, if both endpoints lie in the complement, the contribution is \(m(m-1)/(2n(n-1))\); if exactly one is fixed, its two orientation contributions combine to \(r(m-1)/(n(n-1))\), since \((i-1)+(n-i-1)=n-2\). Two fixed adjacent positions never make an ordinary descent. This computation is valid for \(m\ge2\); at \(m=1\) the remaining permutation is the identity and the formula still gives zero.

For the wrap-around pair \(n,1\), two forced fixed points and either one forced fixed point both create a descent, while two nonfixed points contribute probability \(1/2\). Hence
\[
p_{\mathrm{wrap}}=\frac{r(r-1)+2rm+m(m-1)/2}{n(n-1)}.
\]
Summation gives
\[
\mathbb E[C\mid S\text{ uniformly chosen and fixed}]=(n-1)p_{\mathrm{line}}+p_{\mathrm{wrap}}=\frac n2-\frac{r(r-1)}{2(n-1)}.
\]

**2. Exact mixed factorial moments.** Since every specified \(r\)-subset is fixed with probability \(1/(n)_r\), \(\mathbb E(F)_r=1\), for \(0\le r\le n\). Weighted averaging over all \(r\)-subsets in step 1 therefore gives, for \(r<n\),
\[
\mathbb E[C(F)_r]=\frac n2-\frac{\binom r2}{n-1}.
\]
For \(r=n\) only the identity survives; thus \(\mathbb E[C(F)_n]=1\). Also \(\mathbb E C=n/2\), because each circular pair has equally likely order. Subtraction yields the stated mixed covariances.

**3. Conditional fixed-point regression.** Let \(0\le k\le n-2\) and \(m=n-k\). Inclusion–exclusion gives the exact identity of random variables
\[
\mathbf1\{F=k\}=\frac1{k!}\sum_{s=0}^m\frac{(-1)^s}{s!}(F)_{k+s}.
\]
Writing \(S_j=\sum_{s=0}^j(-1)^s/s!\), its expectation is \(S_m/k!=D_m/(k!m!)\). Substitute step 2 into the mixed expectation. The \(r=n\) term differs from the continuation of the quadratic formula by exactly \(1\), so
\[
\mathbb E[C\mid F=k]=\frac n2-\frac{\binom k2 S_m-k S_{m-1}+S_{m-2}/2}{(n-1)S_m}+\frac{(-1)^m}{m!S_m}.
\]
Using \(S_{m-1}=S_m-(-1)^m/m!\) and \(S_{m-2}=S_m+(m-1)(-1)^m/m!\) reduces this to the displayed expression in the Finding. The event \(F=n\) consists only of the identity.

**4. Sharp parity maximizer.** For \(m\ge2\), \(D_m\ge m-1\), with equality only at small orders, so \(h_m=(m-1)(-1)^m/D_m\) has absolute value at most one and the sign of \((-1)^m\). Apart from the constant factor \(1/[2(n-1)]\), maximizing the regression is equivalent to maximizing
\[
g_n(k)=-k^2+3k-1+h_{n-k}.
\]
For \(k=0\) and every feasible \(k\ge3\), \(g_n(k)\le0\). At \(k=1\) and \(k=2\) the quadratic part is exactly \(1\). If \(n\) is odd, \(h_{n-1}>0>h_{n-2}\), so \(k=1\) is uniquely maximal. If \(n\) is even, the signs reverse and \(k=2\) is uniquely maximal. For \(k=n\), the conditional mean is \(1\), strictly below that at the indicated maximizer for all \(n\ge3\). This proves all size and boundary cases.

## Verification

`verify.py` performs independent exhaustive integer enumeration of every permutation for \(3\le n\le8\), comparing the regression formula for each feasible fixed-point count, every mixed falling-factorial moment, and the unique maximizing class. It prints `Exact enumeration assertions passed: 117`. The arbitrary-size proof is the counting and inclusion–exclusion derivation above; enumeration is a finite cross-check, not a substitute for the proof.

## Relationship to prior work

Eriksen, Freij and Wästlund (2008/2009) develop enumeration of derangements with prescribed **linear** descents; Foata and Han (2007) give a multivariate enumerator containing fixed-point and linear-descent statistics. The previously recorded circular covariance cancellation covers only \(\operatorname{Cov}(F,C)=0\), not the factorial-moment hierarchy or parity-sharp conditional maximizer. The wrap-around comparison and the precise fixed-point conditional mean are essential here. The general generating-function machinery may permit independent derivations; no historical uniqueness is asserted.

## Limitations

Only expectations and mixed factorial covariances are determined; this does not give the full joint law or an ordering of conditional distributions. The claim applies to uniform one-line permutations, not their separate cycle-descent statistic. The result is supported by a complete finite-n proof and independent finite checks but has not undergone independent audit or historical-priority certification.

## References

- N. Eriksen, R. Freij, J. Wästlund, *Enumeration of derangements with descents in prescribed positions* (first arXiv version 12 November 2008), https://arxiv.org/abs/0811.1925.
- D. Foata, G.-N. Han, *Fix-Mahonian Calculus III; A Quadruple Distribution* (arXiv 15 March 2007), https://arxiv.org/abs/math/0703454.
