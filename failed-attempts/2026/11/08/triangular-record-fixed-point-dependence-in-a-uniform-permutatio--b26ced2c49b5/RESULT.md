# Triangular record–fixed-point dependence in a uniform permutation

## Finding

Let \(\Pi\) be uniform on the permutations of \(\{1,\ldots,n\}\), with integer \(n\ge2\). Write \(R_i=\mathbf1\{\Pi(i)>\max_{h<i}\Pi(h)\}\) for the left-to-right record indicator (and \(R_1=1\)), and \(I_j=\mathbf1\{\Pi(j)=j\}\) for the fixed-point indicator. For \(2\le i\le n\), the full mixed covariance matrix is

\[
\operatorname{Cov}(R_i,I_j)=
\begin{cases}
\dfrac{1}{ni(i-1)},&1\le j<i,\\[4pt]
\dfrac1n\left(\binom{n-1}{i-1}^{-1}-\dfrac1i\right),&j=i,\\[4pt]
0,&i<j\le n.
\end{cases}
\]

All covariances in the first row \(i=1\) are zero. The strict lower-triangular entries are positive, while the diagonal is negative for \(2\le i\le n-2\), zero for \(i=n-1\), and positive for \(i=n\); no diagonal sign assertion is needed when its range is empty.

Writing \(F=\sum_{j=1}^n I_j\) and \(R=\sum_{i=1}^n R_i\), all positive lower-triangular contributions and the potentially negative diagonal contributions cancel to give the exact reciprocal-binomial record profile

\[
\boxed{\operatorname{Cov}(R_i,F)=\frac{1}{n\binom{n-1}{i-1}}\quad (2\le i\le n).}
\]

In particular,

\[
\boxed{\operatorname{Cov}(R,F)=\frac1n\sum_{k=1}^{n-1}\binom{n-1}{k}^{-1}>0.}
\]

Moreover, as \(n\to\infty\),

\[
\operatorname{Cov}(R,F)=\frac1n+\frac{2}{n(n-1)}+O(n^{-3}),\qquad
\operatorname{Corr}(R,F)\sim\frac{1}{n\sqrt{\log n}}.
\]

## Assumptions and scope

The permutation is chosen uniformly among all \(n!\) bijections of \(\{1,\dots,n\}\). Record positions use *strict* left-to-right maxima in the one-line representation, not cycles or the values of records. Fixed points mean equality of position and value in that representation. All claims are exact for integers \(n\ge2\) except the stated asymptotics. The diagonal classification is interpreted only at indices that exist. No randomization beyond the uniform permutation is assumed.

## Proof

**Conditional probabilities.** By exchangeability of the relative order of the first \(i\) images, \(\Pr(R_i=1)=1/i\) for \(i\ge1\). Also \(\Pr(I_j=1)=1/n\) for each \(j\). Fix \(2\le i\le n\) and condition on \(I_j=1\).

If \(j>i\), fixing an image outside the prefix leaves the order of the first \(i\) images exchangeable, so \(\Pr(R_i=1\mid I_j=1)=1/i\).

If \(j<i\), the prefix has the fixed image \(\Pi(j)=j\) plus \(i-1\) distinct remaining images, sampled from \(\{1,\ldots,n\}\setminus\{j\}\). There are only \(j-1\le i-2\) possible images below \(j\). Hence at least one of those \(i-1\) images exceeds \(j\). The record event is therefore exactly that the image at position \(i\) is the maximum of the \(i-1\) exchangeable *unfixed* prefix images; its conditional probability is \(1/(i-1)\).

If \(j=i\), the image \(\Pi(i)=i\) is forced. The record event occurs exactly when every one of the preceding \(i-1\) images is in \(\{1,\ldots,i-1\}\). Conditioned on \(\Pi(i)=i\), the preceding set is uniformly selected among the \(\binom{n-1}{i-1}\) subsets of size \(i-1\) of the remaining \(n-1\) symbols, exactly one of which is entirely below \(i\). Thus \(\Pr(R_i=1\mid I_i=1)=\binom{n-1}{i-1}^{-1}\).

**Covariance matrix and cancellation.** For every \(j\),

\[
\operatorname{Cov}(R_i,I_j)=\frac1n\left(\Pr(R_i=1\mid I_j=1)-\frac1i\right).
\]

Substitution proves all three cases. Since \(R_1=1\) almost surely, its row is zero. Summing over \(j\) gives

\[
\operatorname{Cov}(R_i,F)
=\frac{i-1}{ni(i-1)}+\frac1n\left(\binom{n-1}{i-1}^{-1}-\frac1i\right)
=\frac1{n\binom{n-1}{i-1}}.
\]

For \(2\le i\le n-2\), one has \(\binom{n-1}{i-1}\ge\binom{i+1}{i-1}=i(i+1)/2>i\), so the diagonal is negative. At \(i=n-1\) the binomial coefficient equals \(i\), and at \(i=n\) it equals \(1<i\), proving the boundary signs.

**Aggregate asymptotics.** Summing the rows yields the exact total covariance. For \(m=n-1\), split \(\sum_{k=1}^m \binom{m}{k}^{-1}\) into the two edge terms \(k=1,m-1\), the term \(k=m\), and the interior. The interior contribution is \(O(m^{-2})\): the terms at \(k=2,m-2\) contribute \(O(m^{-2})\), while for \(3\le k\le m-3\) there are at most \(m\) terms each bounded by \(\binom{m}{3}^{-1}=O(m^{-3})\). Therefore this sum equals \(1+2/m+O(m^{-2})\), proving the covariance expansion.

The \(I_j\) satisfy \(\mathbb EI_j=1/n\) and \(\mathbb E[I_jI_k]=1/(n(n-1))\) for distinct indices, hence \(\operatorname{Var}(F)=1\) for \(n\ge2\). The relative ranks of successive prefix endpoints are independent uniforms on \(\{1,\ldots,i\}\) under a uniform permutation. Hence the \(R_i\) are independent Bernoulli variables of respective means \(1/i\), giving \(\operatorname{Var}(R)=H_n-H_n^{(2)}\sim\log n\). Combining these two variances with the covariance expansion proves the correlation limit. This is a covariance statement only; it does not assert full independence of \(F\) and \(R\).

## Verification

Run `python3 verify.py` using Python's standard library. The verifier exhaustively enumerates every permutation for sizes \(2\le n\le8\), computes joint frequencies of all record-position and fixed-point indicators, and compares every entry and row sum with the displayed formulas using exact rational arithmetic. It also checks the matrix support and signs algebraically for sizes \(2\le n\le99\). Its observed output reports **324,079 exact rational assertions passed**. The exhaustive finite checks are independent diagnostics; the preceding conditional-probability argument proves the statements for all sizes.

## Relationship to prior work

Gnedin and Gorin (2012) study record-dependent probability measures and record-position sets, not the finite joint record/fixed-point covariance matrix. Diaconis, Evans and Graham (2013/2014) give a fixed-point-set distributional identity for one-line successions; their Theorem 1.1 concerns a different local statistic and does not supply record/fixed-point joint probabilities. More recent work of Dubach (2025) develops asymptotic high-record limits for conjugation-invariant permutations conditional on cycle types, including regimes with many fixed points, but its stated asymptotic results do not give this uniform-model finite matrix. These are substantive neighboring results, not independent evidence of priority. The full Gnedin–Gorin manuscript could not be inspected, and implicit coverage elsewhere remains possible.

## Limitations

The contribution concerns mixed *second moments* in the uniform model. It does not give the full joint law of record and fixed-point sets, or a conditional central limit theorem. A general moment or generating-function result not located in the inspected literature could imply the formulas; originality is therefore a qualified assessment rather than a guarantee. Empirical enumeration is limited to size eight, while the theorem itself is established for all sizes by counting.

## References

1. A. Gnedin and V. Gorin, *Record-dependent measures on the symmetric groups*, arXiv:1202.3680 (first public preprint February 16, 2012), DOI: 10.1002/rsa.20526. https://arxiv.org/abs/1202.3680
2. P. Diaconis, S. N. Evans and R. Graham, *Unseparated pairs and fixed points in random permutations*, Berkeley Statistics Technical Report 822 (August 1, 2013), later *Advances in Applied Mathematics* **61** (2014), 102–124, DOI: 10.1016/j.aam.2014.05.006. https://mathweb.ucsd.edu/~ronspubs/14_05_pairs.pdf
3. V. Dubach, *A geometric approach to conjugation-invariant random permutations*, published November 8, 2025, *Probability Theory and Related Fields* **194** (2026), 245–298, DOI: 10.1007/s00440-025-01449-7. https://link.springer.com/article/10.1007/s00440-025-01449-7
4. E. Y. Jin, *Symmetric generating functions and Euler–Stirling statistics on permutations*, arXiv:2210.08789 (2022). https://arxiv.org/abs/2210.08789
