# Exact gap-depth spectrum and negative-binomial deviations for an infinite-branch Cantor return map

## Finding
For the affine return-map construction of Cunha, Novaes, and Ponce (Appendix B.1 of [1]), every gap generation \(k\geq1\) contributes exactly \(2^{k-1}\) inverse branches of contraction ratio \(r^{-k}\), with \(r>3\). Write \(\Lambda(r)\) for its forward survivor and \(\kappa(x)=k\) when \(x\) belongs to a branch of generation \(k\). For an integer \(n\geq1\), put \(S_n(x)=\sum_{j=0}^{n-1}\kappa(\varphi^j x)\).

**Theorem.** For every \(n\geq1\) and every integer \(S\geq n\), the number of length-\(n\) admissible branch words with \(S_n=S\) is exactly
\[
N_{n,S}=2^{S-n}\binom{S-1}{n-1}.
\]
Every corresponding interval cylinder has diameter \(2r^{-S}\). For every finite \(m\geq1\), the set
\[
E_m=\left\{x\in\Lambda(r):\lim_{n\to\infty}S_n(x)/n=m\right\}
\]
has Hausdorff dimension
\[
\dim_H E_m=\frac{H(m)}{m\log r},\qquad
H(m)=m\log m-(m-1)\log(m-1)+(m-1)\log 2,
\]
with the convention \(0\log0=0\). This spectrum is strictly increasing on \((1,3)\), strictly decreasing on \((3,\infty)\), and attains its unique maximum \(\log3/\log r\) at \(m=3\). It has the nonzero high-depth limit
\[
\lim_{m\to\infty}\dim_HE_m=\frac{\log2}{\log r}.
\]

For the invariant conformal probability \(\mu\) naturally associated with this affine example, the successive depths are independent with \(\mu(\kappa=k)=\frac13(\frac23)^{k-1}\). In particular,
\[
\mu(S_n=S)=2^{S-n}\binom{S-1}{n-1}3^{-S}.
\]
Let \(m_n=S/n\) remain in any fixed compact subinterval of \((1,\infty)\) as \(n\to\infty\). Uniformly over such integers \(S\), the precise local large-deviation law is
\[
\mu(S_n=S)=\frac{\exp[-nI(m_n)]}{\sqrt{2\pi n m_n(m_n-1)}}\left(1+O(n^{-1})\right),\qquad
I(m)=m\log3-H(m).
\]
The rate \(I\) is nonnegative and vanishes only at \(m=3\). The boundary probability \(\mu(S_n=n)=3^{-n}\) is exact.

## Assumptions and scope
The map is precisely the middle-third-gap affine construction in [1, Appendix B.1], or an affine realization with the same disjoint open-set placement, branch multiplicities, and ratios. Its domain is a union of isolated disjoint closed intervals, each mapped diffeomorphically onto \([-1,1]\). There is one branch for each of the \(2^{k-1}\) gaps created at ternary stage \(k\), and the inverse branches have absolute derivative \(r^{-k}\) for one fixed \(r>3\). Orientation and the locations of the branches within the corresponding gaps do not affect the claimed symbolic counts and dimensions. The survivor consists of points with a fully defined infinite branch itinerary. All dimension assertions concern \(\Lambda(r)\), not its closure; the closure also contains singular points related to the background Cantor set. The theorem addresses finite limiting depth means \(m\); it makes no dimension claim for infinite or nonexistent depth averages.

## Proof
**1. Coding and exact count.** The disjoint branch images give injective coding by the full countable shift, as established in [1, Theorem A and Appendix B.1]. An itinerary of \(n\) branches of depths \(k_1,\dots,k_n\geq1\) has \(2^{k_1-1}\cdots 2^{k_n-1}=2^{S-n}\) possible labels when its depth sum is \(S=\sum_jk_j\). The number of positive integer compositions of \(S\) into \(n\) parts is \(\binom{S-1}{n-1}\), proving the first formula. Affinity makes the composition derivative \(r^{-S}\), hence the image of \([-1,1]\) has diameter \(2r^{-S}\). Equivalently, the one-step counting series is \(z/(1-2z)\) and the length-\(n\) coefficient is that of its \(n\)-th power.

**2. Upper dimension bound for a prescribed finite average.** For \(m>1\), let \(\delta>0\) be small and consider cylinders with integer totals in \([n(m-\delta),n(m+\delta)]\). Every point of \(E_m\) belongs to this family for all sufficiently large \(n\). By Stirling's formula, uniformly for \(S/n\) in a compact subinterval of \((1,\infty)\),
\[
\log N_{n,S}=nH(S/n)+O(\log n).
\]
For any \(s>\sup_{|u-m|\leq\delta}H(u)/(u\log r)\), the sum over that family's \(s\)-powers of cylinder diameters is at most \(O(n^C)\exp(-cn)\) for some \(c>0\); thus the \(s\)-dimensional Hausdorff measure of \(E_m\) vanishes. Taking \(\delta\downarrow0\) yields the desired upper bound. For \(m=1\), use the same argument with \(S/n\in[1,1+\delta]\): since \(H(1)=0\), its limiting upper dimension is zero.

**3. Matching lower bound.** For \(m>1\), put \(q_k=m^{-1}(1-m^{-1})^{k-1}\), the geometric distribution on positive depths with mean \(m\). Give each of the \(2^{k-1}\) branches of depth \(k\) probability \(q_k/2^{k-1}\). The resulting one-step Shannon entropy is
\[
-\sum_{k\geq1}q_k\log(q_k/2^{k-1})=H(m),
\]
while the mean one-step logarithmic contraction is \(m\log r\). To avoid relying on any countable-alphabet dimension theorem, first restrict to a finite set of depths: truncate the geometric law at depth \(K\), normalize, then mix with a sufficiently small mass at depth \(K+1\) to restore mean exactly \(m\). As \(K\to\infty\), its entropy converges to \(H(m)\), and finite-support Bernoulli typical points lie in \(E_m\) by the strong law of large numbers. For each fixed \(K\), the selected affine inverse branches form a finite, strongly separated similarity system; the classical dimension formula for its Bernoulli measure is entropy divided by mean logarithmic contraction. Hence \(\dim_HE_m\geq H(m)/(m\log r)\) on letting \(K\to\infty\). The case \(m=1\) is already determined by the upper bound (and \(E_1\) contains the infinite repetition of its unique depth-one branch).

**4. Shape of the spectrum.** Direct differentiation gives
\[
\frac{d}{dm}\left(\frac{H(m)}m\right)=\frac{\log(2/(m-1))}{m^2}\qquad(m>1).
\]
This proves the monotonicity and unique maximum at \(m=3\), whose value is \(H(3)/3=\log3\). Dividing the explicit entropy expression by \(m\) and passing to infinity gives the limiting value \(\log2\).

**5. The invariant probability and local deviations.** Set \(d=\log3/\log r\), the Hausdorff dimension already computed in [1, Appendix B.1]. Since \(\sum_{k\geq1}2^{k-1}r^{-kd}=\sum_{k\geq1}2^{k-1}3^{-k}=1\), assigning each depth-\(k\) branch mass \(3^{-k}\) defines a Bernoulli probability on the coding shift. Its pushforward is invariant. For any Borel set \(A\) in the survivor and any branch inverse \(\psi_i\) of depth \(k\), it satisfies \(\mu(\psi_i A)=3^{-k}\mu(A)=r^{-kd}\mu(A)\); thus it is the \(d\)-conformal invariant probability for the affine construction. Uniqueness within the equivalent invariant conformal class follows from [1, Theorem A(f)]; no uniqueness among all invariant probabilities is asserted. Its one-step depth mass is \(2^{k-1}3^{-k}=\frac13(\frac23)^{k-1}\), and depths are independent. Multiply the exact word count by their common per-word mass \(3^{-S}\) to obtain the exact negative-binomial distribution.

For \(m_n=S/n\) in a compact set strictly above one, factorial Stirling expansions applied to \(\binom{S-1}{n-1}\) yield
\[
\binom{S-1}{n-1}=\frac{\exp[n\{m_n\log m_n-(m_n-1)\log(m_n-1)\}]}{\sqrt{2\pi n m_n(m_n-1)}}\left(1+O(n^{-1})\right).
\]
The exponent and the factor \(2^{S-n}3^{-S}\) combine to give the rate \(I(m_n)=m_n\log3-H(m_n)\) and the stated uniform asymptotic. The geometric distribution has expectation three; equivalently, \(I'(m)=\log[3(m-1)/(2m)]\) changes sign only at three, proving strict positivity away from the mean. At \(S=n\), there is exactly one all-depth-one word, of probability \(3^{-n}\).

## Verification
Run `python3 checks/verify_gap_depth.py` with the Python standard library only. It enumerates all labelled depth choices through five branch steps for bounded totals and checks the exact coefficient formula; checks 88 consecutive probability ratios with exact rational arithmetic; verifies the local asymptotic prefactor numerically at four sample lengths; and checks the expected spectrum shape at seven finite means. The finite tests are corroboration only. The proof of the infinite-dimensional level sets and asymptotic estimates is the preceding argument.

## Relationship to prior work
Cunha, Novaes, and Ponce [1] construct this particular affine Cantor-gap return map and explicitly prove the survivor's total dimension \(\log3/\log r\), countable full-shift conjugacy, and existence/ergodicity of an invariant conformal measure. The branch multiplicities and ratios are theirs, not newly derived here. They do not state the depth-conditioned cylinder census, the complete finite-mean Hausdorff spectrum, or the normalized exact local deviation law. Iommi and Jordan [2,3] developed broad multifractal variational principles for countable Markov maps; the spectrum method here is consistent with that theory, not a new general formalism. Their stated EMR interval setting uses one accumulating branch-endpoint location, whereas this construction accumulates across a Cantor set. The present result is a closed-form, direct proof for this specific natural example, not a theorem about arbitrary countable expanding maps. Generic negative-binomial algebra and finite-alphabet Bernoulli entropy formulas are standard ingredients, not standalone novelty claims.

## Limitations
The formulas assume identical affine ratios within each gap generation, exact multiplicities, and the full-shift property. They do not extend automatically to nonlinear distorted return branches or to the other examples in [1]. The spectrum describes finite limits of mean gap generations only; it says nothing about infinite averages, oscillatory averages, basin geometry, or the physical-time statistics of any ambient Filippov flow. The proof uses classical finite-IFS measure-dimension facts and Stirling asymptotics; the included computation is not an independent proof. Historical priority for specialized spectra on related countable IFS constructions is not completely excluded by the inspected literature.

## References
[1] M. G. C. Cunha, D. D. Novaes, G. Ponce, *Infinite-Piecewise Expanding Maps: Chaos, Ergodicity and Invariant-Set Complexity*, arXiv:2608.00398, v1 first public 2026-08-01; especially Theorem A, Section 5.6, and Appendix B.1. https://arxiv.org/abs/2608.00398

[2] G. Iommi and T. Jordan, *Multifractal analysis of Birkhoff averages for countable Markov maps*, arXiv:1003.2979, 2010; Sections 1–3 and 5. https://arxiv.org/abs/1003.2979

[3] G. Iommi and T. Jordan, *Multifractal analysis for quotients of Birkhoff sums for countable Markov maps*, arXiv:1303.2596, 2013. https://arxiv.org/abs/1303.2596

[4] R. D. Mauldin and M. Urbański, *Dimensions and Measures in Infinite Iterated Function Systems*, Proc. London Math. Soc. 73 (1996), 105–154, DOI 10.1112/plms/s3-73.1.105. General CIFS dimension and measure theory; not an asserted source of the explicit depth law.
