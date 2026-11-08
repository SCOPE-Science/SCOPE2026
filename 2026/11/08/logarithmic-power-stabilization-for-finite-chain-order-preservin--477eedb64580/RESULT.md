# Logarithmic power stabilization for finite-chain order-preserving contractions

## Finding

Let \(\mathcal C_n\) be the monoid of all maps \(f:[n]\to[n]\) such that \(f(i+1)-f(i)\in\{0,1\}\) for \(1\le i<n\). These are exactly the order-preserving full contractions, equivalently the weak endomorphisms of the consistently directed path on \([n]\). Write \(f^0=\operatorname{id}\), and define its **power-stabilization index**
\[
\tau(f)=\min\{j\ge0:f^{j+1}=f^j\}.
\]

For every nonempty interval \(I=[a,b]\subseteq[n]\), choose \(f\) **uniformly conditional on** \(\operatorname{Fix}(f)=I\), and put \(t=n-|I|\). The following convergence holds **uniformly in the location and length of \(I\)**, as long as \(t\to\infty\): for every \(\varepsilon>0\),
\[
\lim_{t\to\infty}\ \sup_{\substack{n\ge t+1,\ 1\le a\le b\le n\\n-(b-a+1)=t}}
\Pr\left(\left|\frac{\tau(f)}{\log_2 t}-1\right|>\varepsilon
\ \middle|\ \operatorname{Fix}(f)=[a,b]\right)=0.
\]
In particular, for a uniformly random \(F_n\in\mathcal C_n\),
\[
\boxed{\displaystyle\frac{\tau(F_n)}{\log_2 n}\xrightarrow{\mathbb P}1.}
\]

The new assertion is the **power-stabilization law** (especially its uniform fixed-interval form). Existing exact enumerations of transformation rank and fixed-point count are credited as prior work and are not claimed as new.

## Assumptions and scope

The ground set is the labeled totally ordered chain \([n]=\{1,\ldots,n\}\), with \(n\ge1\). Maps are total, order-preserving and nonexpansive for the ordinary chain distance. Products are functional compositions and powers repeat the **same** map. There is no independent map resampling between iterations. When \(t=0\), the unique map with all points fixed is the identity and has \(\tau=0\); the conditional asymptotic theorem assumes \(t\to\infty\).

A map of this type has at least one fixed point, and its fixed-point set is a consecutive interval. In fact, the displacement \(f(i)-i\) changes by \(-1\) or \(0\) between successive inputs; it begins nonnegative and ends nonpositive. Thus the zeros form a nonempty interval \([a,b]\). For \(i<a\), \(f(i)>i\); for \(i>b\), \(f(i)<i\). Since every iterate moves toward this fixed interval and cannot cross it, a finite power equals the retraction to \([a,b]\). In particular \(\tau(f)\) is finite and \(\operatorname{im}(f^{\tau(f)})=\operatorname{Fix}(f)\).

## Proof

**1. Independent Bernoulli tail encoding.** Fix the interval \(I=[a,b]\), and write \(L=a-1\), \(R=n-b\) and \(t=L+R\). If \(L>0\), the step from \(a-1\) to \(a\) must be flat: \(f(a-1)=a\). Every earlier adjacent step on the left is independently free to be flat or increase by one. If \(R>0\), the step from \(b\) to \(b+1\) is flat: \(f(b+1)=b\), and every subsequent adjacent step on the right is independently free to be flat or increase by one. Each choice produces a valid map with **exactly** \(I\) as fixed set, because outside the interval the displacement has a strict sign. Conversely every such map arises uniquely. Hence the conditional uniform distribution consists of two independent strings of fair Bernoulli bits, of lengths \((L-1)_+\) and \((R-1)_+\).

For either tail of length \(s>0\), enumerate its independent bits from the fixed interval outward, and let \(S_j\) be the number of ones among the first \(j\), with \(S_0=0\). A point at distance \(h\in\{1,\ldots,s\}\) from the fixed interval is sent to distance
\[
\phi(h)=S_{h-1}.
\]
Thus the successive distances are \(h,\phi(h),\phi^2(h),\ldots,0\), and \(\phi(h)\le h-1\). Since \(S_{h-1}\) increases weakly in \(h\), the most distant endpoint is the last point of that tail to reach the fixed interval. The global index \(\tau(f)\) is the larger of the two endpoint absorption times (with the empty tail contributing zero).

**2. Uniform prefix concentration.** Fix \(0<\delta<1/4\). Standard Bernoulli concentration yields, for each \(j\ge1\),
\[
\Pr\bigl(|S_j-j/2|>\delta j/2\bigr)\le 2\exp(-\delta^2j/2).
\]
Choose \(h_0(t)=\lceil C_\delta\log\log(t+e^e)\rceil\), with \(C_\delta>4/\delta^2\). Summing the preceding exponential bound over all \(j\ge h_0(t)-1\) shows that with probability \(1-o(1)\), simultaneously for both tails and **every** integer \(h\ge h_0(t)\) within the tail,
\[
(1/2-\delta)h\le S_{h-1}\le (1/2+\delta)h.
\]
The \(o(1)\) is independent of the chosen interval and its two tail lengths. The change from \(j=h-1\) to \(h\) is absorbed by the fixed \(\delta\) margin for sufficiently large \(h_0\).

**3. Absorption-time bounds.** Put \(\alpha=1/2-\delta\) and \(\beta=1/2+\delta\). On the event just described, every distance \(h\ge h_0\) shrinks in one step to a number between \(\alpha h\) and \(\beta h\). Every subsequent distance below \(h_0\) takes at most \(h_0\) more steps to reach zero, because \(\phi(h)\le h-1\). Therefore
\[
\tau(f)\le\frac{\log t}{\log(1/\beta)}+h_0(t)+2.
\]
At least one tail has length \(H=\max(L,R)\ge t/2\). Starting from that tail endpoint, its distance cannot fall below \(h_0\) in fewer than \(\log(H/h_0)/\log(1/\alpha)-1\) steps. Hence
\[
\tau(f)\ge \frac{\log(t/(2h_0(t)))}{\log(1/\alpha)}-1
\]
for large \(t\). As \(h_0(t)=O_\delta(\log\log t)=o(\log t)\), division by \(\log_2 t=\log t/\log2\) gives a lower limiting bound \(\log2/\log(1/\alpha)\) and an upper limiting bound \(\log2/\log(1/\beta)\), outside an event of vanishing probability. Letting \(\delta\downarrow0\) proves the asserted uniform conditional convergence.

**4. Unconditional random map.** Existing fixed-point enumeration [2] states that for \(n\ge2\), the number of maps with exactly \(k\) fixed points is
\[
\#\{f\in\mathcal C_n:|\operatorname{Fix}(f)|=k\}=
\begin{cases}
(n-k+3)2^{n-k-2},&1\le k<n,\\
1,&k=n,
\end{cases}
\]
while \(|\mathcal C_n|=(n+1)2^{n-2}\). This established formula implies \(|\operatorname{Fix}(F_n)|=O_{\mathbb P}(1)\); in fact its distribution converges to \(\Pr(K=k)=2^{-k}\) for positive integers \(k\). Consequently \(t=n-|\operatorname{Fix}(F_n)|\) satisfies \(t/n\to1\) in probability. Apply the **uniform** conditional theorem to the random fixed interval, and use \(\log t/\log n\to1\), to obtain the unconditional law.

## Verification

The standalone `verify.py` enumerates all maps with adjacent increments in \(\{0,1\}\) for \(n=1,\ldots,10\). It computes \(\tau\) by literal composition of the maps, and independently via the two prefix-sum tail recurrences, and compares the results for every map. It reconstructs **each** conditional fixed-interval family independently from tail bits for \(n\le8\), and compares all joint fixed-point/image-rank counts with the published closed formula [2]. Its deterministic checks terminate with `VERIFY_OK`. Auxiliary seeded simulations at three larger tail lengths illustrate the theorem but are explicitly not a proof.

As a concrete finite observation, the number of elements with power-stabilization indices \(0,1,2,3,4\) when \(n=5\) is \(1,14,23,8,2\), respectively. The bound \(\tau(f)\le n-1\) is exact but is much larger than the typical logarithmic index.

## Relationship to prior work

Fernandes and Paulista [1], first publicly posted December 26, 2021, characterize the weak endomorphisms of a directed finite path, enumerate their ranks and idempotents, and establish the generating rank of the monoid. Adeshola and Umar [2] had already established the much stronger **joint exact enumeration by image rank and number of fixed points** for the equal monoid of order-preserving full contractions (their Proposition 2.3 and Corollaries 2.4 and 2.9). Those counts, the fixed-point interval property, and the resulting geometric fixed-point limit are **prior results or immediate corollaries**, not new claims.

The present theorem instead concerns the **number of powers of an individual element required to reach its idempotent limit**. Rank and fixed-point counts do not determine this index: for \(n=5\), the maps with value lists \((3,4,5,5,5)\) and \((2,3,4,4,4)\) both have image rank three and exactly one fixed point, but their indices are respectively two and three. The existing joint count therefore does not directly imply this time law.

Zubairu, Umar and Aliyu [3] study regular and idempotent subsemigroups of the same contraction monoid; their inspected statements concern enumeration and generating rank, not random power-stabilization time. The nearest differently structured comparison found is logarithmic settling of certain deterministic quantized affine contractions, whose hypotheses and dynamics do not cover uniform finite-chain order-preserving contractions. No inspected source was found proving the uniform conditional power-index law. This is a best-evidence originality assessment, not a proof of publication priority.

## Limitations

The convergence is in probability and gives the leading logarithmic constant; it does not establish a bounded additive error, a limiting centered distribution, a central limit theorem, or an optimal rate. It concerns repeated powers of one sampled map, not independently resampled contractions. The uniform conditional law requires the complement of the fixed interval to grow; arbitrary monotone maps without the one-step Lipschitz restriction and order-reversing contractions are outside the result. The sampled finite checks do not certify the infinite theorem. Priority remains subject to independent mathematical and bibliographic review.

## References

1. V. H. Fernandes and T. Paulista, *On the Rank of Monoids of Endomorphisms of a Finite Directed Path*, arXiv:2112.13427v1, December 26, 2021. https://arxiv.org/abs/2112.13427
2. A. D. Adeshola and A. Umar, *Combinatorial Results for Certain Semigroups of Order-Preserving Full Contraction Mappings of a Finite Chain*, arXiv:1303.7428v2, December 6, 2013; Proposition 2.3, Corollaries 2.4 and 2.9. https://arxiv.org/abs/1303.7428
3. M. M. Zubairu, A. Umar and M. J. Aliyu, *On the Combinatorial and Rank Properties of Certain Subsemigroups of Full Contractions of a Finite Chain*, arXiv:2205.00438v1, May 1, 2022. https://arxiv.org/abs/2205.00438
