# A Bessel transition for missing cycles in partial-permutation centralizers

## Finding
Let \(\ell,m\ge 1\), and let \(\sigma\) be a permutation consisting of \(m\) disjoint cycles, each of length \(\ell\), on a set of \(m\ell\) points. Write \(\mathcal I_{m\ell}\) for the symmetric inverse monoid of all partial bijections and \(C(\sigma)=\{f\in\mathcal I_{m\ell}:f\sigma=\sigma f\}\). Choose \(F\) uniformly from \(C(\sigma)\), and define its *omitted-cycle count* by \(J=m-|\operatorname{dom}F|/\ell\).

The exact domain-rank polynomial and omitted-cycle law are
\[
\sum_{f\in C(\sigma)}z^{|\operatorname{dom}f|}
=\sum_{k=0}^{m}\binom{m}{k}^{\!2}k!\ell^k z^{k\ell},
\qquad
\Pr(J=j)=\frac{(m)_j}{(j!)^2\ell^j}\bigg/\sum_{h=0}^{m}\frac{(m)_h}{(h!)^2\ell^h},
\]
for integers \(0\le j\le m\), where \((m)_j=m!/(m-j)!\). The enumerator is the direct finite counting consequence of the known structural description of partial-permutation centralizers, and is not asserted to be new by itself.

For any sequence of such pairs \((m,\ell)\) with \(m\to\infty\), put \(\tau=m/\ell\). There is a three-regime limit:

1. If \(\tau\to0\), then \(\Pr(J=0)\to1\): almost every centralizing partial bijection is a full permutation.
2. If \(\tau\to\lambda\in(0,\infty)\), then \(J\) converges in total variation to the discrete Bessel distribution
\[
\Pr(J_\lambda=j)=\frac{\lambda^j}{(j!)^2\,I_0(2\sqrt\lambda)},\quad j=0,1,2,\ldots,\qquad I_0(2\sqrt\lambda)=\sum_{j=0}^{\infty}\frac{\lambda^j}{(j!)^2}.
\]
3. If \(\tau\to\infty\), then \(J/\sqrt\tau\to1\) in probability.

Thus, when the number of equal cycles becomes comparable to their length, the number of cycles omitted by a uniformly sampled centralizer element crosses from zero to a nondegenerate Bessel law, before growing at the precise square-root scale.

## Assumptions and scope
All assertions are purely finite and combinatorial, valid for every pair of positive integers \(m,\ell\). In limits, \(m\to\infty\) and \(\ell=\ell(m)\) is any sequence of positive integers. The *rank* is the cardinality of the domain of a partial bijection; \(J\) counts omitted \(\sigma\)-cycles, not missing individual points. A statement about the Bessel regime concerns \(J\), while the missing-point count equals \(\ell J\). Convergence in total variation is on the nonnegative integers. No claim is made about arbitrary partial bijections with chain components or about nonuniform sampling.

## Proof
First, equality \(f\sigma=\sigma f\) of partial maps requires equality of their domains. Since \(\sigma\) is a full permutation, this implies \(\operatorname{dom} f\) is invariant under \(\sigma\); it is thus a union of complete cycles. The same holds for the image, since commutation and bijectivity of \(f\) imply \(\sigma(\operatorname{im}f)=\operatorname{im}f\). On its domain, \(f\) is an equivariant bijection and therefore sends each length-\(\ell\) cycle bijectively onto another length-\(\ell\) cycle, with exactly \(\ell\) possible phase shifts. If \(k\) cycles are retained, their source and target sets can each be chosen in \(\binom{m}{k}\) ways; a matching of the selected cycles contributes \(k!\), and independent phase shifts contribute \(\ell^k\). This proves the rank polynomial.

For \(j=m-k\), divide the rank-\((m-j)\ell\) coefficient by the full-rank coefficient \(m!\ell^m\) to obtain \(w_j=(m)_j/((j!)^2\ell^j)\), proving the probability formula.

For the first and second regimes, \(0\le w_j\le\tau^j/(j!)^2\). When \(\tau\to0\), \(1\le \sum_jw_j\le\sum_{j\ge0}\tau^j/(j!)^2\to1\); hence \(\Pr(J=0)\to1\). When \(\tau\to\lambda\in(0,\infty)\), for each fixed \(j\), \(w_j=\tau^j(j!)^{-2}\prod_{r=0}^{j-1}(1-r/m)\to\lambda^j/(j!)^2\). The same uniform summable upper bound applies once \(\tau\) is bounded. Dominated convergence gives convergence of the normalizing sums, and Scheffé's lemma for discrete probability masses gives total-variation convergence to the displayed Bessel law.

For the supercritical regime, write \(R=\sqrt\tau\to\infty\). The ratios of consecutive positive weights are
\[
\frac{w_{j+1}}{w_j}=\frac{m-j}{\ell(j+1)^2}.
\]
Since \(R/m=1/\sqrt{m\ell}\to0\), for every fixed \(\varepsilon\in(0,1)\), the ratio is bounded below by a constant greater than one uniformly for \(j\le(1-\varepsilon/2)R\), and bounded above by a constant smaller than one uniformly for \(j\ge(1+\varepsilon/2)R\). Comparing weights across the intervals from \((1-\varepsilon)R\) to \((1-\varepsilon/2)R\), and from \((1+\varepsilon/2)R\) to \((1+\varepsilon)R\), yields exponentially vanishing left and right tails, respectively; the exterior tail sums are bounded geometrically by the respective boundary weights. Explicitly, the bounds are \(O_\varepsilon(e^{-c_\varepsilon R})\) after dividing by the normalizer, for some \(c_\varepsilon>0\). Consequently \(\Pr(|J/R-1|>\varepsilon)\to0\).

## Verification
The self-contained `checker.py` independently enumerates all partial injections by choices of domain, image and bijection, then tests the two partial compositions pointwise against the exact coefficient formula for ten parameter pairs with up to six underlying points. It also computes finite total-variation distances in two critical scalings; all checks passed. Reproduce with `python checker.py`; the captured deterministic output is in `checker_output.txt`. The asymptotic laws are established by the proof, not by these finite enumerations.

## Relationship to prior work
Konieczny's 2012 centralizer characterization already describes how commuting partial injections act on the cycles of a prescribed permutation (Theorem 3.4, cycle case). Hence the finite coefficient enumeration above is a straightforward consequence and is explicitly credited as such. The aspect assessed here is the varying-parameter *three-regime probabilistic transition*, especially the nondegenerate discrete Bessel window at \(m/\ell\asymp1\). Araújo–Bentz–Konieczny (2012) studies the commuting graph, maximum commutative families and ideal diameters of the symmetric inverse semigroup; its rank counts for certain disjoint-support semigroups are not the conditional centralizer law or its Bessel scaling. A later (2020) paper of Konieczny studies finite inverse-semigroup centralizers and Green relations, but its full text was not available during this assessment; the priority risk is expressly retained. The exact full-rank/partial-rank input and the Bessel series are classical; their independent novelty is not claimed.

## Limitations
The coefficient formula is structurally implied by established centralizer theory, and the new contribution asserted here is limited to its three asymptotic regimes. A Bessel-law discussion in unavailable or unindexed centralizer literature could preempt this contribution; bibliographic search does not certify uniqueness. The 2020 finite-centralizer paper and the full 1997 Lipscomb monograph were not verified in full. No independently performed audit or external publication-priority certification is claimed. The proof does not establish quantitative rates in the supercritical regime beyond exponential concentration on each fixed relative-deviation set.

## References
- J. Konieczny, *Centralisers in the Infinite Symmetric Inverse Semigroup*, Bulletin of the Australian Mathematical Society 87 (2013), 462–479; first online 28 September 2012. https://doi.org/10.1017/S0004972712000779
- J. Araújo, W. Bentz and J. Konieczny, *The Commuting Graph of the Symmetric Inverse Semigroup*, arXiv:1205.1664v1, 8 May 2012. https://arxiv.org/abs/1205.1664
- J. Konieczny, *The structure of centralizers in the finite symmetric inverse semigroup*, Communications in Algebra 48 (2020), 5181–5194, abstract checked; full text not inspected. https://doi.org/10.1080/00927872.2020.1782926
- S. Lipscomb, *Symmetric Inverse Semigroups*, AMS Mathematical Surveys and Monographs 46 (1997); not inspected in full. https://doi.org/10.1090/surv/046
