# A centered-walk law for Coxeter-period stabilization in type-A zero-Hecke monoids

## Finding

Let \(n\ge3\) and let \(c\) be a Coxeter element of the type-A \(0\)-Hecke monoid \(H_0(S_n)\): one occurrence of each idempotent generator \(\pi_1,\ldots,\pi_{n-1}\), in some order. Let \(K(c)=\min\{r\ge1:c^r=w_0\}\), with Demazure multiplication and absorbing longest element \(w_0\). Choose uniformly from **distinct Coxeter elements**, not from the \((n-1)!\) orders of the generators.

The finite law is given by a lazy symmetric walk. For an integer interval \(I\) containing 0, let \(T_I\) be the matrix with diagonal 2, immediate-neighbor entries 1 and all other entries zero; \(e_0\) is the coordinate vector of 0 and \(\mathbf 1\) is the all-one column. For \(k\ge0\), the cumulative **counts** are
\[
\begin{aligned}
\#\{c\in\mathcal C_{2m}:K(c)\le m+k\}&=e_0^{\mathsf T}T_{[-k,k]}^{m-1}\mathbf 1, &&m\ge2,\\
\#\{c\in\mathcal C_{2m+1}:K(c)\le m+1+k\}&=2e_0^{\mathsf T}T_{[-k-1,k]}^{m-1}\mathbf 1, &&m\ge1 .
\end{aligned}
\]
Here \(\mathcal C_n\) has \(2^{n-2}\) elements; divide by that number for probabilities. In particular \(\lceil n/2\rceil\le K\le n-1\). The fastest-level counts are \(2^{m-1}\) and \(2\cdot3^{m-1}\) respectively, included as checks and not claimed as new. The maximum time is attained by the two constant orientations.

There is a nondegenerate limiting law on the \(\sqrt n\) scale:
\[
\frac{K(c)-n/2}{\sqrt n}\ \Longrightarrow\ \frac12\sup_{0\le t\le1}|B(t)|,
\]
where \(B\) is standard Brownian motion. Its distribution function is zero for \(x\le0\); for \(x>0\) it is
\[
\frac4\pi\sum_{j=0}^{\infty}\frac{(-1)^j}{2j+1}
 \exp\!\left[-\frac{(2j+1)^2\pi^2}{32x^2}\right].
\]
This is the standard two-sided Brownian exit-time series evaluated at the boundary \(2x\). The result describes the typical scale and the full finite law, not just the extremal orientations.

## Assumptions and scope

Write \(\varepsilon_i=1\) if \(\pi_i\) occurs before \(\pi_{i+1}\) and \(-1\) otherwise, for \(1\le i\le n-2\). Put \(H_1=0\), \(H_{i+1}=H_i+\varepsilon_i\). Orientations are in bijection with Coxeter elements. Every orientation of the generator path is acyclic and realized by a linear extension; different linear extensions of the same orientation differ by swaps of commuting letters. A word using each generator once is reduced: before the first use of a comparator at position \(j\), all labels originally on each side have stayed on that side, so its first use increases length in the descending-comparator convention. By the reduced-word braid theorem, reduced words for the same element are connected by commutations and braid moves; no braid of length three is possible from a word with each letter appearing once, even after commutations. The \(0\)-Hecke elements are indexed by permutations, so distinct signs give distinct monoid elements. Uniform choice therefore means independent symmetric signs. There is no field or characteristic hypothesis, and ordinary group powers are not involved.

## Deterministic input and its prior coverage

The deterministic formula underlying the random law is
\[
K(c)=\frac{n+\max_{1\le i<n}|H_i-H_{n-i}|}{2}.
\tag{1}
\]
It is a consequence of Ceballos–Labbé–Stump [1, Theorem 7.2, Algorithm 7.3 and Remark 7.6], even though those passages concern sorting words rather than \(0\)-Hecke period times. To see this, use the lexicographically first reduced subword for \(w_0\) in \(c^\infty\). It is obtained by greedily accepting every length increase: such an accepted reduced prefix with product \(w\) can always be extended to a reduced word for \(w_0\) because \(\ell(w^{-1}w_0)=\ell(w_0)-\ell(w)\), and any finite reduced completion embeds in the remaining infinite repetitions. A length-decreasing letter cannot extend a reduced prefix. This is exactly the selection rule for the Demazure product. Consequently the last occupied block of the sorting word is the first Demazure stabilization round.

For \(\phi_i\) the occurrence counts of the simple generators in that sorting word, [1, Theorem 7.2] gives \(\phi_i-\phi_{i+1}=(\varepsilon_i+\varepsilon_{n-i-1})/2\) in type A: if the earlier-to-later order on an adjacent pair is reversed under conjugation by \(w_0\), the earlier generator occurs once more, otherwise their counts are equal. Remark 7.6 gives \(\phi_i+\phi_{n-i}=n\) since type A has Coxeter number \(n\) and conjugation sends \(i\) to \(n-i\). These relations determine \(\phi_i=(n+H_{n-i}-H_i)/2\). Algorithm 7.3 puts generator \(i\) in exactly the first \(\phi_i\) blocks, so \(K=\max_i\phi_i\), yielding (1) by symmetry. Thus the pointwise formula is prior-covered and is not the originality claim.

For completeness there is a direct comparator proof of (1). Descending adjacent comparators commute with every binary threshold. The increasing permutation is sent to the decreasing permutation exactly when every thresholded input \(0^a1^b\), \(a+b=n\), is sent to \(1^b0^a\). Label the zeros from right to left and the ones from left to right. The crossing of zero \(i\) and one \(j\) uses comparator \(p=a-i+j\) and must wait for crossings \((i-1,j)\) and \((i,j-1)\), when present. These are sufficient: once both predecessors have occurred, the pair have made exactly the \(j-1\) and \(i-1\) swaps needed to become adjacent, and neither can pass the other without their common comparison. If a predecessor occurred in round \(r\), the child can use that round only if its comparator is later in the round. Thus \(R_{1,1}=1\) and the earliest round of a later crossing is the maximum of the predecessor rounds plus penalties \((1+\varepsilon_p)/2\) from comparator \(p+1\), and \((1-\varepsilon_{p-1})/2\) from \(p-1\), omitting absent predecessors. Each penalty equals \((1-\Delta H)/2\), with \(\Delta H\) the change of comparator height from predecessor to child. Along any grid path from \((1,1)\) to \((a,b)\), the \(n-2\) penalties sum to \((n-2-H_b+H_a)/2\). The last crossing is therefore in round \((n+H_a-H_b)/2\), and taking the maximum over thresholds proves (1). Parity follows because each height difference spans \(|n-2i|\) signs.

## Proof of the two random laws

For \(n=2m\), the signed sums of successive central intervals of the orientation range start at 0 and add a new disjoint pair of signs at each step. If \(Y_r\) is half their sum, its increments are \(-1,0,1\) with probabilities \(1/4,1/2,1/4\). There are \(m-1\) steps. Equation (1) gives \(K=m+\max_{0\le r\le m-1}|Y_r|\). Counting paths staying in \([-k,k]\) with the three step multiplicities \(1,2,1\) gives the even count.

For \(n=2m+1\), the central sign \(\varepsilon_m\) is independent of the symmetric pairs. The sums are \(\varepsilon_m+2Y_r\) for \(0\le r\le m-1\), with the same lazy walk. Conditional on the positive central sign, the inequality for the maximum in (1) is precisely that \(Y\) stay in \([-k-1,k]\). The negative sign gives the reflected interval, with the same count, so the factor is 2. For \(k=0\) the even interval has one state with two choices of signs per step; the odd interval has two states, each with three admissible choices per step for each fixed central sign. The upper endpoint \(n-1\) can only occur when the sum over all \(n-2\) signs has absolute value \(n-2\), which gives the two constant orientations, including \(n=3\).

For both parities the walk has increment variance \(1/2\) and \(m-1\sim n/2\) steps. Its linearly interpolated path divided by \(\sqrt n\) converges in law to \(B/2\) by the invariance principle. In odd rank the shift \(\varepsilon_m/2\) changes the maximum by at most \(1/2\) before scaling. The absolute supremum is continuous on continuous paths for the uniform norm, so the probability limit follows. This probabilistic analysis uses the distribution over all orientations, which is not given by the deterministic sorting-word multiplicities alone.

## Verification

`CHECKER.py` checks comparator stabilization, individual binary-block times and transfer counts for all \(1022\) orientations for \(3\le n\le11\) (9216 binary-block checks), 840 seeded trials through \(n=60\), and verifies the transfer extremes through \(n=30\). The accompanying `CHECKER_OUTPUT.txt` records those finite checks. Run `python3 CHECKER.py` with the standard library. The exact law and convergence follow from the proofs, not from finite checking.

## Relationship to prior work and limitations

Ceballos–Labbé–Stump already determine the deterministic occurrence profile and block structure [1, §7]; (1) is an explicit type-A consequence. Pilaud–Stump [2] use the same lexicographic sorting word in their study of brick polytopes. Speyer [3] proves repeated-word reducedness in the infinite setting and notes longest-element reachability in the finite setting. Kosuda [4] treats ordinary group powers and minimum-level admissibility and counts; those special cases are not treated here as novel. Denton–Hivert–Schilling–Thiéry [5] provide type-independent \(0\)-Hecke background. The finite all-threshold random census and the Brownian limit for uniform distinct type-A Coxeter elements are the contribution claimed here, not new deterministic sorting-word counts or new walk limit theorems. The cited deterministic results do not state that random law. The literature comparison does not establish exhaustive historical priority. The result makes no assertion for other Coxeter types, other elements, uniform generator orders, or convergence rates for the limit.

## References

1. C. Ceballos, J.-P. Labbé and C. Stump, *Subword complexes, cluster complexes, and generalized multi-associahedra*, https://arxiv.org/abs/1108.1776, §7.
2. V. Pilaud and C. Stump, *Brick polytopes of spherical subword complexes and generalized associahedra*, https://arxiv.org/abs/1111.3349.
3. D. E. Speyer, *Powers of Coxeter Elements in Infinite Groups are Reduced*, https://arxiv.org/abs/0710.3188.
4. M. Kosuda, *Coxeter elements of the symmetric groups whose powers afford the longest*, https://arxiv.org/abs/1411.5761.
5. T. Denton, F. Hivert, A. Schilling and N. M. Thiéry, *On the Representation Theory of Finite J-Trivial Monoids*, https://arxiv.org/abs/1010.3455.
