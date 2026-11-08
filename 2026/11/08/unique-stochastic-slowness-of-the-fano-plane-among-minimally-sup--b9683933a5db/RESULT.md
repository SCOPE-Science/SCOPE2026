# Unique stochastic slowness of the Fano plane among minimally supported fair triple-collectors

## Finding
Let \(V=\{0,1,\ldots,6\}\) and let \(\mathcal F\) range over all *simple* families of seven distinct three-element subsets of \(V\), such that each vertex belongs to exactly three members of \(\mathcal F\). At each independent round, select uniformly one member of \(\mathcal F\), and let \(T_{\mathcal F}\) be the first positive round when the union of all selected members equals \(V\). Let \(\mathcal P\) be the seven lines of the Fano plane. For every integer \(t\ge0\),
\[
\Pr(T_{\mathcal P}>t)\ge\Pr(T_{\mathcal F}>t).
\]
For every \(t\ge3\), equality occurs if and only if \(\mathcal F\) is isomorphic to \(\mathcal P\); equality is automatic for \(t=0,1,2\). In particular \(\mathcal P\) uniquely maximizes mean completion time, up to relabeling, and the sharp mean values are
\[
\mathbb E T_{\mathcal P}=\frac{163}{30},\qquad
\max_{\mathcal F\not\cong\mathcal P}\mathbb E T_{\mathcal F}=\frac{16}{3},\qquad
\text{gap}=\frac1{10}.
\]

## Assumptions and scope
Every draw is independent, uniformly selecting one of seven distinct triples; repetitions *between rounds* are permitted, but duplicates *inside the seven-element family* are excluded. The uniform degree-three incidence condition is fairness. A simple three-uniform, point-regular family on seven points has a number \(b\) of distinct blocks divisible by seven, since \(3b=7r\). Thus \(b=7\) is the smallest possible support for nonempty fair mechanisms of this kind. The theorem optimizes only this natural minimal-support class, not all fair mechanisms with \(b\in\{14,21,28,35\}\), nor weighted or non-simple families. The natural primary classification is MSC2020 60C05.

## Proof
For nonempty \(A\subseteq V\), put \(d(A)=|\{B\in\mathcal F:B\cap A=\varnothing\}|\), the number of admissible blocks avoiding all coupons in \(A\). Inclusion-exclusion over unseen coupons gives, for integer \(t\ge1\),
\[
\Pr(T_{\mathcal F}>t)=7^{-t}\sum_{\varnothing\ne A\subseteq V}(-1)^{|A|+1}d(A)^t
=7^{-t}\sum_{k=1}^{4}c_k(\mathcal F)k^t,
\]
where \(c_k=\sum_{\varnothing\ne A\subseteq V:d(A)=k}(-1)^{|A|+1}\). The upper limit four follows from the degree-three condition: each single vertex is avoided by four blocks, and avoiding a larger set cannot increase that count. Define \(c_0\) by the same formula at \(k=0\). Summing the tail yields the exact rational mean
\[
\mathbb ET_{\mathcal F}=\sum_{k=0}^4\frac{7c_k(\mathcal F)}{7-k}.
\]
Here the sum includes \(k=0\) because \(\Pr(T>0)=1\), so the geometric-series identity is evaluated from \(t=0\).

The complete combinatorial classification follows by enumerating the \(\binom{35}{7}=6,724,520\) subsets of the 35 possible triples, retaining precisely those with all seven degrees three, and evaluating the preceding 127-term integer sum. There are exactly 11,205 admissible labeled families with the following **exhaustive** coefficient profiles; each row lists \((c_0,c_1,c_2,c_3,c_4)\), the number of labeled families and the exact mean:

| Coefficients | Number | Mean |
|---|---:|---:|
| \((-6,21,-21,0,7)\) | 30 | \(163/30\) |
| \((-4,15,-15,-2,7)\) | 630 | \(16/3\) |
| \((-3,12,-12,-3,7)\) | 1,680 | \(317/60\) |
| \((-2,9,-9,-4,7)\) | 3,780 | \(157/30\) |
| \((-1,6,-6,-5,7)\) | 3,360 | \(311/60\) |
| \((1,0,0,-7,7)\) | 360 | \(61/12\) |
| \((0,4,-6,-3,6)\) | 1,260 | \(301/60\) |
| \((0,5,-9,0,5)\) | 105 | \(49/10\) |

A witness for the first profile is the family of bitmask triples \((7,25,97,42,82,76,52)\), where the bit positions are the seven points. Each pair of its vertices lies in exactly one block, so it is the Fano plane. The exact code verifies that all 30 families with this profile form its complete relabeling orbit (the Fano automorphism group has order 168).

It remains to compare all the tails, not just means. Write \(D_t=7^t(\Pr(T_{\mathcal P}>t)-\Pr(T_{\mathcal F}>t))\) for \(t\ge1\). For the five non-Fano profiles with \(c_4=7\),
\[
D_t=b(3^t-3\cdot2^t+3),\qquad b\in\{2,3,4,5,7\}.
\]
The parenthesis vanishes at \(t=1,2\) and is strictly increasing thereafter, because its forward increment equals \(2\cdot3^t-3\cdot2^t>0\) for \(t\ge2\). For the remaining profile with \(c_4=6\),
\[
D_t=4^t+3\cdot3^t-15\cdot2^t+17;
\]
its forward increment \(3\cdot2^t(2^t+2(3/2)^t-5)\) is positive for \(t\ge2\), while \(D_2=0\). For the profile with \(c_4=5\),
\[
D_t=2(2^t-2)(2^t-4),
\]
which vanishes for \(t=1,2\) and is positive for all \(t\ge3\). At \(t=0\), survival is one for every family. This establishes strict first-order stochastic maximality. The mean values and gap are the exact rational values in the census.

## Verification
The accompanying standalone `verify.py` uses only the Python standard library. `python verify.py` recursively enumerates every admissible simple seven-block degree-three family, verifies the eight complete profiles and their multiplicities, checks the Fano relabeling orbit, the sharp rational means, and exact tail inequalities for sampled small integer times. `python verify.py --full` additionally independently enumerates **all** \(6,724,520\) seven-block subsets without incidence-pruning and checks that the complete profile histogram agrees. Both modes executed successfully. The infinite family of inequalities in the theorem is proved symbolically by the three difference formulas, not inferred from finite tests. The 35-choice exhaustive search is finite and complete for the stated seven-point scope.

## Relationship to prior work
Barak-Pelleg and Berend, *Fano Geometry and Slow Coupon Collecting*, arXiv:2606.28216v1 (first public June 26, 2026), establish the Fano-plane example and its comparison with unrestricted uniform triple sampling, along with higher-order projective-plane and star examples. Their calculations supply the motivating setting and the Fano mean, which are not claimed as new. Grunbaum and Yaakobi, *General Coverage Models: Structure, Monotonicity, and Shotgun Sequencing*, arXiv:2510.25305v1, provide general hypergraph recovery-set methods and comparisons, but not the complete seven-block 3-regular census or the stochastic maximum over that class. The present claim concerns the entire **minimal-support regular class**, not merely Fano versus the complete 35-block design, and obtains strict stochastic order rather than a comparison of expectations alone.

## Limitations
The finding does not classify arbitrary nonuniform or multiset-supported laws, the cases with 14 or more distinct triples, or general orders of projective planes. Prior general coupon-coverage identities are used without claiming them as new. The finite census is a transparent reproducible exhaustive certificate, not an analytical classification of all orders; historical priority requires independent literature review. No independent mathematical validation has been carried out.

## References
1. D. Barak-Pelleg and D. Berend, *Fano Geometry and Slow Coupon Collecting*, arXiv:2606.28216v1, June 26, 2026. https://arxiv.org/abs/2606.28216
2. Y. Grunbaum and E. Yaakobi, *General Coverage Models: Structure, Monotonicity, and Shotgun Sequencing*, arXiv:2510.25305v1, October 29, 2025. https://arxiv.org/abs/2510.25305
