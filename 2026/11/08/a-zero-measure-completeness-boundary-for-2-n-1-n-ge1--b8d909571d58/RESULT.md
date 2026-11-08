# A zero-measure completeness boundary for \((2^n+1)_{n\ge1}\)

## Finding

Let \(s_n=2^n+1\) for integers \(n\ge1\). For each real \(\alpha>0\), define \(a_n(\alpha)=\lfloor\alpha s_n\rfloor\), and let \(P_\alpha\) consist of all finite sums of terms \(a_n(\alpha)\) with distinct indices, including the empty sum. Put
\[
V=\{\alpha>0:P_\alpha=\mathbb N_0\}.
\]
Then \(V\subseteq(0,1/2]\), \(V\) has Lebesgue measure zero, and every \(2^{-k}\), \(k\ge1\), lies in \(V\). More quantitatively, for Lebesgue-almost every \(\alpha\in(0,1/2)\), the integer interval
\[
I_n(\alpha)=\left[1+\sum_{j=1}^n a_j(\alpha),\ a_{n+1}(\alpha)-1\right]\cap\mathbb Z
\]
is nonempty for all sufficiently large \(n\), contains no element of \(P_\alpha\), and has size
\[
|I_n(\alpha)|=\left(\tfrac12-\alpha\right)n+o(n).
\]
These intervals are pairwise disjoint whenever nonempty. In particular, for almost every \(\alpha\in(0,1/2)\), there are arbitrarily long consecutive runs of nonrepresentable integers.

The sequence is strictly increasing, satisfies \(s_{n+1}<2s_n\) at every index, and has \(s_{n+1}/s_n\to2\). Thus the positive-measure conclusion known under a fixed ratio bound strictly below two cannot be extended merely by assuming the pointwise strict inequality \(s_{n+1}<2s_n\), although existence of a suitable scaling persists.

## Assumptions and scope

All powers have integer indices \(n\ge1\). Terms \(a_n(\alpha)\) are nonnegative integers; zeros are permitted and repeated indices are not. **Strong completeness** here means \(P_\alpha=\mathbb N_0\), as defined in the motivating paper, not the distinct property of completeness after deleting arbitrarily many finite terms. The zero-measure claim concerns ordinary one-dimensional Lebesgue measure on \((0,\infty)\). The asymptotic gap statement holds for almost every parameter, not for every parameter; notably it fails at the explicitly complete dyadic parameters.

## Proof

**1. No scaling above one-half works.** If \(\alpha\ge2/3\), then \(a_1=\lfloor3\alpha\rfloor\ge2\), and monotonicity gives \(a_n\ge2\) for all \(n\). Thus \(1\notin P_\alpha\). Suppose instead that \(1/2<\alpha<2/3\), and write \(\varepsilon=\alpha-1/2>0\). Exact arithmetic gives
\[
a_n=2^{n-1}+\left\lfloor2^n\varepsilon+\alpha\right\rfloor.
\]
For \(n=1\), the second summand equals \(\lfloor3\alpha-1\rfloor=0\). Since \(2^n\varepsilon+\alpha\to\infty\), there is a smallest \(N\ge2\) for which the second summand is at least one. For \(j<N\), we have \(a_j=2^{j-1}\), and therefore
\[
\sum_{j=1}^{N-1}a_j=2^{N-1}-1,
\qquad a_N\ge2^{N-1}+1.
\]
The integer \(2^{N-1}\) is not representable: sums using earlier indices are too small, whereas any summand at index \(N\) or later is too large. Hence \(V\subseteq(0,1/2]\).

**2. Infinitely many explicit complete scalings.** For every integer \(k\ge1\), direct division yields
\[
\left\lfloor 2^{-k}(2^n+1)\right\rfloor=
\begin{cases}
0,&1\le n<k,\\
2^{n-k},&n\ge k.
\end{cases}
\]
The positive terms are exactly \(1,2,4,8,\ldots\). Ordinary binary expansion represents every nonnegative integer as a finite sum of distinct such terms, proving \(2^{-k}\in V\).

**3. Exact gap identity.** For any \(\alpha>0\), let \(\{x\}=x-\lfloor x\rfloor\), and put
\[
H_n(\alpha)=1+\sum_{j=1}^n a_j(\alpha)-a_{n+1}(\alpha).
\]
Since \(\sum_{j=1}^n(2^j+1)-(2^{n+1}+1)=n-3\), subtraction of fractional parts gives the identity
\[
H_n(\alpha)=1+\alpha(n-3)-\sum_{j=1}^n\{\alpha(2^j+1)\}+\{\alpha(2^{n+1}+1)\}.
\tag{1}
\]
If \(H_n<0\), every integer between \(1+\sum_{j\le n}a_j\) and \(a_{n+1}-1\) is absent from \(P_\alpha\): a sum with indices at most \(n\) is no larger than the former bound minus one, and a sum using any later index is at least \(a_{n+1}\). The number of missing consecutive integers in that interval is exactly \(-H_n\). Intervals corresponding to different indices are disjoint: the upper endpoint of \(I_n\) is below \(a_{n+1}\), whereas the lower endpoint of \(I_{n+1}\) is greater than \(a_{n+1}\).

**4. Almost-everywhere equidistribution, with proof.** Let \(h\) be a nonzero integer and put
\[
T_N(\alpha)=\frac1N\sum_{j=1}^N e^{2\pi i h2^j\alpha}.
\]
Orthogonality of distinct integer frequencies gives the exact integral
\[
\int_0^1|T_N(\alpha)|^2\,d\alpha=\frac1N.
\]
Apply Chebyshev's inequality and the first Borel--Cantelli lemma along \(N=k^2\). Since \(\sum_{k\ge1}k^{-2}<\infty\), for almost every \(\alpha\) one has \(T_{k^2}(\alpha)\to0\). For \(k^2\le N<(k+1)^2\), adding at most \(2k+1\) unit-modulus summands and changing normalization yields
\[
|T_N(\alpha)-T_{k^2}(\alpha)|\le \frac{2(2k+1)}{k^2}\longrightarrow0.
\]
Intersecting the full-measure sets over countably many nonzero \(h\), Weyl's criterion implies that \((\{2^j\alpha\})_{j\ge1}\) is uniformly distributed modulo one for almost every \(\alpha\in(0,1)\). Translation by the fixed \(\alpha\) preserves uniform distribution, hence for almost every \(\alpha\in(0,1/2)\),
\[
\lim_{n\to\infty}\frac1n\sum_{j=1}^n\{\alpha(2^j+1)\}=\int_0^1x\,dx=\frac12.
\]
The fractional part is Riemann integrable on the unit circle despite its jump, so uniform distribution applies.

**5. Quantitative gaps and measure.** Divide (1) by \(n\). Its constant and terminal fractional-part terms are bounded independently of \(n\), so for almost every \(\alpha\in(0,1/2)\),
\[
\frac{H_n(\alpha)}n\longrightarrow\alpha-\frac12<0.
\]
Thus \(I_n(\alpha)\) is eventually a positive-length gap and has length \(-H_n(\alpha)=(1/2-\alpha)n+o(n)\), as claimed. Therefore almost every parameter in \((0,1/2)\) is not in \(V\); the remaining candidates consist of a null subset of \((0,1/2)\) together with the single point \(1/2\). Since no parameter above \(1/2\) works, \(\mu(V)=0\). All conclusions follow.

## Verification

The standalone `verify.py` uses exact rational arithmetic to confirm identity (1) on 1,330 rational parameter pairs for \(1\le n\le22\), checks the dyadic basis for \(1\le k\le32\), verifies the upper-half obstruction across denominators 2 through 60, and exhibits finite nonrepresentable gaps for 12 deterministic binary fractions at index 180. Execute `python3 verify.py` in the directory containing this text and the verifier. The almost-everywhere and infinite assertions are proved above, not inferred from finite checks.

## Relationship to prior work

Wu and Ma, *A note on a problem of Ma and Chen* (arXiv:2610.38288v1, first posted 2026-10-28), prove existence of a strongly complete scaling under the critical condition \(s_{n+1}\le2s_n\). Their introduction cites the earlier Ma--Chen positive-measure theorem under a fixed uniform growth factor smaller than two; their complete theorem and proof do not give the measure-zero example or the gap asymptotic above. The present result separates **existence** at the critical threshold from **positive measure** and quantifies typical failure. The subset-sum gap criterion itself is classical and is already presented as Brown's lemma in Wu--Ma; no novelty is claimed for that criterion, for binary expansion, or for the classical Weyl criterion. The 2022 Ma--Chen paper's official abstract was inspected, but its full text could not be accessed during this comparison. Unindexed equivalents and material inaccessible in that earlier article remain priority risks.

## Limitations

The measure-zero and linear-gap statements are only almost-everywhere, not classifications of the exceptional set \(V\). No Hausdorff dimension, precise structure of all valid parameters, or general theorem for every sequence with ratio tending to two is asserted. The available source comparison is not an exhaustive historical-priority proof; an inaccessible historical full text may contain related constructions.

## References

1. B.-L. Wu and W.-X. Ma, *A note on a problem of Ma and Chen*, arXiv:2610.38288v1, 2026-10-28. https://arxiv.org/html/2610.38288v1
2. W.-X. Ma and Y.-G. Chen, *Hegyvári's theorem on complete sequences, II*, Acta Arith. 203 (2022), 307–318, doi:10.4064/aa210811-30-3. Official publisher abstract: https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/203/4/114716/hegyvari-s-theorem-on-complete-sequences-ii
3. Brown's subset-sum criterion, as reproduced and proved in reference 1, Lemma 2.1.
4. Weyl's uniform-distribution criterion; the needed a.e. doubling-map consequence is proved directly in Step 4 above.
