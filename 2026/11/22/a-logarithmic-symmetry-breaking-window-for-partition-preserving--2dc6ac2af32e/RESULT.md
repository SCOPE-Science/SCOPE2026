# A logarithmic symmetry-breaking window for partition-preserving retractions

## Finding

Fix an integer \(m\ge 2\) and real numbers \(\beta_1,\ldots,\beta_m\). For every sufficiently large positive integer \(n\), partition a labeled set into \(m\) labeled blocks of sizes
\[
s_j(n)=n+\lfloor\beta_j\log n\rfloor\qquad(1\le j\le m).
\]
Choose uniformly from the idempotent elements of the monoid of full maps preserving this partition (each source block must map wholly into a single target block). Write \(K_n\) for the number of blocks that contain image points and, when \(K_n=1\), write \(J_n\) for that block's index.

**Theorem (critical logarithmic asymmetry).** For each \(j\in\{1,\ldots,m\}\),
\[
\boxed{\lim_{n\to\infty}\Pr(K_n=1,\ J_n=j)
=\frac{\exp(m\beta_j)}{\sum_{i=1}^{m}\exp(m\beta_i)}.}
\]
Moreover, with \(\gamma_m=m\log m-(m-1)\log(m-1)>0\),
\[
\boxed{\Pr(K_n\ge2)=\exp(-\gamma_m n+o(n)).}
\]
The logarithmic size scale is sharp in the following sense. More generally, if \(s_j(n)=n+o(n)\) for all fixed \(j\), then (a) if all pairwise size gaps are \(o(\log n)\), the unique image block tends to the uniform law; (b) if one block exceeds every other block by \(\omega(\log n)\), that block is the image block with probability tending to one. The exact finite enumeration used below is an antecedent, not a new claim.

## Assumptions and scope

All logarithms are natural. The number \(m\) of source blocks is fixed as \(n\to\infty\); it is not allowed to grow. A partition-preserving transformation need not preserve each block individually: it induces a function on the set of block labels. A retraction here means an idempotent full transformation, \(f^2=f\). Block labels remain distinguishable. The estimates assume every block size is positive; this is automatic for all sufficiently large \(n\) in the theorem. The dominant probability is over all such idempotents, not over all transformations.

## Proof

**1. Exact rooted-fiber decomposition (previously known counting mechanism).** For integers \(1\le s\le M\), let
\[
H_s(M)=\sum_{r=1}^{s}\binom sr r^{M-r}.
\]
This counts idempotent maps from a collection of \(M\) source points into a distinguished target block of \(s\) points, fixing every image point: first choose the \(r\) fixed image points in the target block, then map all remaining \(M-r\) points freely to those points.

Every idempotent partition-preserving map induces an idempotent block map \(\phi\colon[m]\to[m]\). If \(B_j=\phi^{-1}(j)\) is the fiber of its fixed target block \(j\), its corresponding number of point maps is \(H_{s_j}(M_j)\), with \(M_j=\sum_{i\in B_j}s_i\). Different rooted fibers are independent. Consequently the number inducing \(\phi\) is exactly
\[
W(\phi)=\prod_{j\in\operatorname{im}\phi}H_{s_j}(M_j).
\]
In particular there is exactly one block map with unique image \(j\), and its weight is \(H_{s_j}(N)\), where \(N=\sum_i s_i\). This decomposition is a direct specialization of the established classification and enumeration of partition-preserving idempotents in Dolinka--East--Mitchell (2015), Proposition 3.1 and Proposition 3.2.

**2. Uniform logarithmic saddle.** Fix any integer \(t\in\{1,\ldots,m\}\), and suppose \(M=tn+o(n)\), \(s=n+o(n)\) with \(s\le M\). Define \(T_s(M,r)=\binom sr r^{M-r}\). Its exact successive-term ratio is
\[
\frac{T_s(M,r+1)}{T_s(M,r)}
=\frac{s-r}{r(r+1)}\left(1+\frac1r\right)^{M-r-1}
\qquad(1\le r<s).
\]
This ratio decreases strictly in \(r\). At \(r=\lfloor c n/\log n\rfloor\) for fixed \(c>0\), its logarithm is
\[
\left(\frac tc-1\right)\log n+o(\log n).
\]
Therefore the weight distribution \(T_s(M,r)/H_s(M)\) concentrates at \(r\log n/n\to t\), with exponentially small tails outside each fixed neighborhood of \(t\). Uniform Stirling estimates at such \(r\) give
\[
\log T_s(M,r)=M(\log n-\log\log n+\log c)-cn+o(n),
\]
which is maximized at \(c=t\). There are at most \(s=O(n)\) summands, so
\[
\boxed{\log H_s(M)=M(\log n-\log\log n)+tn(\log t-1)+o(n).}\tag{1}
\]
Both this estimate and the concentration are uniform when \(s/n\to1\) and \(M/n\to t\).

**3. Exponential suppression of multiple target blocks.** If \(\phi\) has \(k\) fixed image blocks whose rooted block-fibers have sizes \(t_1,\ldots,t_k\), then \(\sum_a t_a=m\) and (1) gives
\[
\log W(\phi)=N(\log n-\log\log n)-mn
+n\sum_{a=1}^{k}t_a\log t_a+o(n).
\]
A one-root map has logarithmic weight \(N(\log n-\log\log n)+mn(\log m-1)+o(n)\). For \(k\ge2\), strict convexity of \(x\log x\) shows the largest possible \(\sum_a t_a\log t_a\) is \((m-1)\log(m-1)\), attained by a two-fiber split into \(m-1\) and \(1\) source blocks. Such splits exist. The number of induced block maps depends only on fixed \(m\). Summation therefore proves the stated exact logarithmic rarity exponent \(-\gamma_m\), and in particular \(\Pr(K_n=1)\to1\).

**4. The second, logarithmic symmetry-breaking scale.** Fix \(N=mn+o(n)\). For consecutive admissible target-block sizes \(u\) and \(u+1\), the binomial identity
\[
\binom{u+1}{r}=\binom ur\frac{u+1}{u+1-r}
\]
for \(1\le r\le u\) yields the exact formula
\[
\frac{H_{u+1}(N)}{H_u(N)}
=\mathbb E_u\left[\frac{u+1}{u+1-R}\right]
+\frac{(u+1)^{N-u-1}}{H_u(N)},\tag{2}
\]
where \(\Pr_u(R=r)=T_u(N,r)/H_u(N)\). In the interval \(u=n+o(n)\), the second (new-endpoint) term in (2) is \(\exp[-\Omega(n\log n)]\), because \(N\sim mn\) and \(m\ge2\). The saddle concentration from step 2 gives \(R/u=(m+o_{\Pr}(1))/\log n\). Exponentially small tails and the bound \((u+1)/(u+1-R)\le u+1\) justify taking expectations and the Taylor expansion. Thus, uniformly for \(u=n+o(n)\),
\[
\boxed{\log H_{u+1}(N)-\log H_u(N)
=\frac{m+o(1)}{\log n}.}\tag{3}
\]
Telescoping (3), with either sign of the size difference, gives for \(s_i-s_j=o(n)\)
\[
\log\frac{H_{s_i}(N)}{H_{s_j}(N)}
=\frac{(m+o(1))(s_i-s_j)}{\log n},\tag{4}
\]
provided both sizes are \(n+o(n)\). When \(s_j=n+\lfloor\beta_j\log n\rfloor\), equation (4) makes this ratio tend to \(\exp(m(\beta_i-\beta_j))\). Normalizing the \(m\) one-root weights and using step 3 proves the softmax law. Likewise, pairwise \(o(\log n)\) gaps yield uniformity, while a unique maximum separated by \(\omega(\log n)\) forces every competing ratio to zero. This completes the proof.

## Verification

The included `checker.py` independently enumerates all partition-preserving maps and tests idempotence on six small labeled partitions, comparing the full image-block-set multiplicities against the rooted-fiber formula. It also tests the exact binomial step identity, including its necessary new-endpoint summand, on thirty finite parameter pairs. The accompanying `checker_output.txt` records successful results. These finite checks verify the combinatorial mechanism; the infinite limits require the saddle and telescoping arguments above and are not inferred from numerical convergence.

## Relationship to prior work

Dolinka and East (2014) enumerate idempotents and analyze generators for uniform partitions. Dolinka, East, and Mitchell (2015) explicitly classify idempotents and give a recurrence for arbitrary nonuniform partitions. Their finite enumeration, including Proposition 3.2, covers the exact underlying weights and is not claimed as original. Earlier fixed-equal-block asymptotics describe entropy suppression of multiple image blocks but do not resolve which image block is selected after the equal-size symmetry is perturbed by only \(O(\log n)\) points. The new statement is the second-scale logarithmic selection limit and its sharp crossover. Unlike conclusions confined to the uniform diagonal \(s_1=\cdots=s_m\), this result depends on the entire nonconstant vector of logarithmic size perturbations. It requires a distinct uniform one-step sensitivity estimate, including the endpoint term of (2).

## Limitations

The number of blocks is fixed; no claim covers growing \(m\), blocks of different limiting proportions, or non-idempotent transformations. The rate in step 3 is inherited from the already understood equal-block entropy mechanism; it is included to certify the one-target approximation, not presented as a separate new phenomenon. The result uses and does not replace an earlier complete finite counting formula. Broad unlocated work on asymptotics of random idempotent mappings could contain an equivalent sensitivity estimate, so publication priority should be independently checked before citing this as a first discovery.

## References

1. I. Dolinka and J. East, *Idempotent generation in the endomorphism monoid of a uniform partition*, arXiv:1407.3312, first posted 2014-07-11. https://arxiv.org/abs/1407.3312
2. I. Dolinka, J. East, and J. D. Mitchell, *Idempotent rank in the endomorphism monoid of a non-uniform partition*, arXiv:1504.02520, first posted 2015-04-09, Proposition 3.1 and Proposition 3.2. https://arxiv.org/abs/1504.02520
