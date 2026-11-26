# Strict likelihood-ratio ordering of coupon-collection times by the final coupon

## Finding

A heterogeneous coupon collector's completion time is ordered by the identity of the final newly discovered label. A more probable label, **conditional on being the last label discovered**, accompanies a strictly earlier completion time in the likelihood-ratio sense—not merely a smaller conditional mean.

Write \(F_i(t)=\Pr(C=i,T=t)\). For all \(i\ne j\) with \(p_i>p_j\) and integers \(m\le t<u\),
\[
 F_i(t)F_j(u)>F_i(u)F_j(t).
\]
Thus \(\Pr(T=t\mid C=i)/\Pr(T=t\mid C=j)\) is strictly decreasing in \(t\). Equality of the entire conditional law for two labels occurs exactly at equal label weights.

## Assumptions and scope

Fix any integer \(m\ge2\) and strictly positive real probabilities \(p_1,\ldots,p_m\) summing to \(1\). Independently at each positive integer time, draw one label with replacement, with label \(i\) having probability \(p_i\). Define \(T\) to be the **first** time all \(m\) labels have appeared. Define \(C\) to be the unique label drawn at that time, never previously observed. Thus \(T\ge m\), \(C\in\{1,\ldots,m\}\), and every \(\Pr(C=i,T=t)\) with \(t\ge m\) is strictly positive.

The coefficient operator \([z^k]\) extracts the coefficient of \(z^k\) from a formal power series, and all convolution sequences below are indexed by nonnegative integers with zero outside their support. Likelihood-ratio order means that the ratio of the two strictly positive probability mass functions is nonincreasing in time; we prove strict decrease.

## Proof

**Exact marked mass.** For the completion event \(\{C=i,T=t\}\), the \(t\)-th draw is \(i\), the preceding \(t-1\) draws contain every other label at least once, and none is \(i\). Summing over the positive counts of those labels via the multinomial theorem gives, for every integer \(t\ge m\),
\[
 F_i(t)=p_i(t-1)!\,[z^{t-1}]\prod_{r\ne i}(e^{p_rz}-1). \tag{1}
\]
In particular, all labels share \(F_i(m)=(m-1)!\prod_{r=1}^m p_r\).

**Log-concavity lemma.** A nonnegative sequence with interval support and \(a_k^2\ge a_{k-1}a_{k+1}\) has a totally positive order-two Toeplitz kernel \(a_{u-v}\): for \(w<v\) and \(k<l\),
\[
 a_{w-k}a_{v-l}-a_{w-l}a_{v-k}\ge0. \tag{2}
\]
Indeed, in the positive support the ratios \(a_{r+1}/a_r\) decrease in \(r\); cross-multiplying appropriate consecutive ratios proves (2), while all boundary cases follow from interval support. Conversely the adjacent minors recover log-concavity. Toeplitz kernels multiply under convolution, and each minor of a product of two such kernels is a sum of products of nonnegative minors (Cauchy–Binet); for any chosen finite indices this is a finite sum because these sequences vanish at negative indices. Thus convolution preserves nonnegative log-concavity with interval support. Here the sequence with coefficients \(a_0=0\) and \(a_k=p^k/k!\) for integers \(k\ge1\) satisfies the hypothesis, since \(a_{k+1}/a_k=p/(k+1)\) decreases strictly. Products of the exponential series below therefore have nonnegative log-concave coefficient sequences.

**The strict two-row inequality.** Fix \(i,j\) with \(p_i>p_j\). Put
\[
 G(z)=\prod_{r\notin\{i,j\}}(e^{p_rz}-1)=\sum_{r\ge0}g_rz^r,
 \quad A_k=\frac{p_j^k}{k!},\quad B_k=\frac{p_i^k}{k!}\quad(k\ge1).
\]
For \(m=2\) set \(g_0=1\), and \(g_r=0\) for \(r\ne0\). For \(m\ge3\), the log-concavity lemma shows that \(g\) has a log-concave coefficient sequence, with \(g_r>0\) exactly for integers \(r\ge m-2\). Define
\[
 U_w=\sum_{k\ge1}A_kg_{w-k},\qquad
 V_w=\sum_{k\ge1}B_kg_{w-k},\quad w\ge m-1.
\]
Formula (1) gives \(F_i(w+1)=p_iw!U_w\) and \(F_j(w+1)=p_jw!V_w\). For integers \(m-1\le w<v\), an exact paired-index determinant expansion yields
\[
 U_wV_v-U_vV_w=\sum_{1\le k<l}
 (A_kB_l-A_lB_k)
 (g_{w-k}g_{v-l}-g_{w-l}g_{v-k}). \tag{3}
\]
Every summand is nonnegative by (2) and \(A_kB_l-A_lB_k>0\) for \(k<l\), since \(p_i/p_j>1\). At least one is strictly positive. If \(m\ge3\), choose \(k=w-(m-2)\ge1\) and \(l=k+1\). Then \(g_{w-k}=g_{m-2}>0\), \(g_{w-l}=g_{m-3}=0\), and \(g_{v-l}>0\), since \(v>w\). If \(m=2\), choose \(k=w\), \(l=v\), and use the point mass \(g_0=1\). Hence (3) is strictly positive. Multiplying by the positive factors \(p_ip_jw!v!\) proves for all \(m\le t<u\),
\[
 F_i(t)F_j(u)>F_i(u)F_j(t).\tag{4}
\]

**Consequences.** Normalize each row \(F_i(t)\) by \(q_i=\Pr(C=i)>0\). The ratio \(\Pr(T=t\mid C=i)/\Pr(T=t\mid C=j)\) strictly decreases across all integers \(t\ge m\), so the former conditional duration is smaller in strict likelihood-ratio order. The usual single-crossing argument for strictly decreasing likelihood ratios gives strict first-order stochastic order (each nontrivial upper tail is strictly smaller), and therefore a strictly smaller conditional expectation; all these means are finite because the time to discover each positive-probability label has a geometric tail. If \(p_i=p_j\), swapping the two label names leaves the sampling law invariant, so \(F_i=F_j\). Conversely unequal weights force strict (4), prohibiting equality. Lastly, because \(F_i(m)=F_j(m)\), applying (4) at \(t=m\) proves \(F_i(u)<F_j(u)\) for each \(u>m\). Summation gives \(\Pr(C=i)<\Pr(C=j)\) when \(p_i>p_j\).

## Verification

A standalone pure-Python exact-rational checker is provided as `check.py`. Running `python check.py` checks \(30{,}533\) exact assertions: cross-products for 25 positive rational vectors with \(2\le m\le6\), the supporting coefficient log-concavity inequalities, and independent exhaustive enumeration of sample strings with \(m\le4\) and \(t\le8\). All assertions passed. These finite computations check the formulas and sign conventions, but the all-size conclusion rests on proof (1)–(4).

As a small illustration, for \((p_1,p_2,p_3)=(1/2,3/10,1/5)\), all three marked probabilities at \(t=3\) equal \(3/50\), while \(F_1(4)=9/200<63/1000=F_2(4)\). The strict inequality (4) holds for every larger pair of times, not just this example.

## Relationship to prior work

Ferrante and Frigo (2012) derive unmarked heterogeneous coupon-collection waiting-time formulas, and their first public version supplies the verified dated source anchor and the matching probability-classification context. Shank and Yang (2013) treat nonuniform coupon quotas via expectation integrals. Anceaume, Busnel and Sericola (2014) give unmarked full-collection waiting-time distributions by Markov chains; Anceaume, Busnel, Schulte-Geers and Sericola (2015) compare such waiting-time laws when the probability vector is changed. None of the inspected material in these sources asserts the strict likelihood-ratio comparison between **conditional** durations \(T\mid C=i\) for two possible last labels of one fixed heterogeneous law. In particular, stochastic optimization over distinct sampling distributions is not a conditional marked-label comparison. The coefficient identity can be derived by standard exponential generating functions; the asserted contribution is the universal strict two-label determinant order and its conditional statistical consequences.

## Limitations

The theorem addresses finite, strictly positive iid categorical models with a single arrival per draw. It does not cover zero-probability labels, dependent draws, group arrivals, random quotas or continuous-time multitype arrivals without additional work. The proof is mathematical, supplemented by finite exact tests; the tests alone are not an infinite certificate. Search and full-text comparison reduce but cannot eliminate the possibility of an older equivalent inequality implicitly encoded in the classical occupancy or totally-positive sequence literature. No independent mathematical audit or historical-priority certification has been performed.

## References

- M. Ferrante and N. Frigo, *A note on the coupon-collector's problem with multiple arrivals and the random sampling*, arXiv:1209.2667v1, first public 2012-09-12, https://arxiv.org/abs/1209.2667 .
- N. Shank and H. Yang, *Coupon Collector Problem for Non-Uniform Coupons and Random Quotas*, Electronic Journal of Combinatorics 20(2), #P33 (2013), https://doi.org/10.37236/3348 .
- E. Anceaume, Y. Busnel and B. Sericola, *New results on a generalized coupon collector problem using Markov chains*, arXiv:1402.5245 (2014), https://arxiv.org/abs/1402.5245 .
- E. Anceaume, Y. Busnel, E. Schulte-Geers and B. Sericola, *Optimization results for a generalized coupon collector problem*, arXiv:1504.03878 (2015), https://arxiv.org/abs/1504.03878 .
