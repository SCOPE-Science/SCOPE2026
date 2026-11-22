# Cross-work, Spearman footrule, and exact finite permutation fluctuations

## Finding
For a full transformation \(f:[n]\to[n]\), \(n\ge2\), define its *cross-work* and its Spearman footrule by
\[
W(f)=\sum_{i=1}^{n-1}\bigl(|i-f(i+1)|+|i+1-f(i)|\bigr),\quad
D(f)=\sum_{i=1}^n|i-f(i)|.
\]
Let \(F(f)=|\{i\in[n]:f(i)=i\}|\) and \(\Delta(f)=f(n)-f(1)\). **For every full transformation**,
\[
\boxed{W(f)=2D(f)+2F(f)+\Delta(f)-(n+1).}\tag{1}
\]
Let \(\Pi\) be uniform over the permutation group \(S_n\). The following hold exactly for every integer \(n\ge2\):
\[
\boxed{\mathbb E W(\Pi)=\frac{(n-1)(2n-1)}3,\quad
\operatorname{Var}W(\Pi)=\frac{16n^3-29n^2-229n+536}{90},}\tag{2}
\]
\[
\boxed{\operatorname{Cov}(W(\Pi),D(\Pi))=
\frac{(n+1)(8n^2-15n-32)}{90}.}\tag{3}
\]
The covariance is negative for \(n=2,3\), and positive for every \(n\ge4\). Moreover,
\[
\operatorname{Corr}(W(\Pi),D(\Pi))=1-\frac{15}{32n}+O(n^{-2}),\quad
\frac{W(\Pi)-\mathbb EW(\Pi)}{\sqrt{\operatorname{Var}W(\Pi)}}
\ \Longrightarrow\ N(0,1).\tag{4}
\]
If \(U\) is uniform over the full transformation monoid \(T_n=[n]^{[n]}\), then the mean remains that in (2), but
\[
\boxed{\operatorname{Var}W(U)=
\frac{(n-1)(6n^3-9n^2-79n+176)}{30n}.}\tag{5}
\]
Its standardized cross-work is also asymptotically standard normal, and the ratio of permutation to full-transformation cross-work variances tends to \(8/9\).

## Assumptions and scope
The domain is \([n]=\{1,\ldots,n\}\), with \(n\ge2\). A full transformation is *any* map \([n]\to[n]\); a permutation is a bijective full transformation. Each of \(S_n\) and \(T_n\) carries the uniform finite probability measure separately. All absolute values are ordinary integer absolute values. No independence of the images of a uniform permutation is assumed. The two normal-limit statements concern \(n\to\infty\), after centering by the exact mean and dividing by the exact standard deviation.

## Proof
**1. Pointwise decomposition.** For every integer \(i\) and \(x\),
\(|i-1-x|+|i+1-x|=2|i-x|+2\mathbf1_{\{i=x\}}\).
The contribution of an interior image \(f(i)\), for \(2\le i\le n-1\), to \(W(f)\) is therefore its corresponding contribution to \(2D(f)+2F(f)\). At the first and last images the exact residuals are respectively \(-f(1)\) and \(f(n)-(n+1)\). These identities also hold at the endpoints when \(f(1)=1\) or \(f(n)=n\). Summation proves (1), including \(n=2\).

**2. Random permutation moment identities.** Write \(D=D(\Pi)\), \(F=F(\Pi)\), and \(\Delta=\Delta(\Pi)\). Uniformity of every image gives
\[
\mathbb ED=\frac{n^2-1}{3},\quad \mathbb EF=1,\quad \mathbb E\Delta=0,
\quad \operatorname{Var}F=1,
\quad \operatorname{Var}\Delta=\frac{n(n+1)}6.\tag{6}
\]
The variance of \(F\) is exactly one for all \(n\ge2\), by the first and second factorial moments of fixed-point count. For the footrule, consider the array \(a_{ij}=|i-j|\). The variance formula for a uniform random assignment of this array is
\[
\operatorname{Var}\Bigl(\sum_i a_{i,\Pi(i)}\Bigr)
=\frac{\displaystyle\sum_{i,j}a_{ij}^2-
\frac1n\sum_i r_i^2-\frac1n\sum_j c_j^2+
\frac1{n^2}(\sum_{i,j}a_{ij})^2}{n-1},\tag{7}
\]
where \(r_i=\sum_j a_{ij}\), \(c_j=\sum_i a_{ij}\). It follows directly from the one-image and distinct-two-image sampling rules, not an independence approximation. Here \(r_i=c_i=\tfrac12[i(i-1)+(n-i)(n-i+1)]\),
\[
\sum_{ij}a_{ij}=\frac{n(n^2-1)}3,\quad
\sum_{ij}a_{ij}^2=\frac{n^2(n^2-1)}6,\quad
\sum_i r_i^2=\frac{n(n-1)(n+1)(7n^2-8)}{60}.
\]
Substitution yields
\[\operatorname{Var}D=\frac{(n+1)(2n^2+7)}{45}.\tag{8}\]
There are three mixed moments:
\[
\operatorname{Cov}(D,F)=-\frac{n+1}3,\quad
\operatorname{Cov}(D,\Delta)=-\frac{n(n+1)}6,\quad
\operatorname{Cov}(F,\Delta)=1.\tag{9}
\]
For the first, conditional on the fixed point \(\Pi(i)=i\), the remaining permutation is uniform; its mean footrule is \((T-2r_i)/(n-1)\), with \(T=\sum_{ij}a_{ij}\). Summing over \(i\) and subtracting \(\mathbb ED\) proves the first equality of (9). For the second, the random-assignment covariance gives
\[
\operatorname{Cov}(D,\Pi(j))=\frac1{n-1}\sum_{k=1}^n
\left(k-\frac{n+1}2\right)|j-k|.
\]
At \(j=1\) this equals \(n(n+1)/12\), and at \(j=n\) its negative. Taking their difference establishes the second equality. For the last, conditioning on a fixed point away from the endpoints makes the endpoint-image difference mean zero; conditioning on either endpoint fixed gives mean difference \(n/2\), each with probability \(1/n\). Thus \(\mathbb E(F\Delta)=1\).

Insert (6), (8), and (9) into (1):
\[
\begin{aligned}
\operatorname{Var}W={}&4\operatorname{Var}D+4\operatorname{Var}F
+\operatorname{Var}\Delta+8\operatorname{Cov}(D,F)\\
&+4\operatorname{Cov}(D,\Delta)+4\operatorname{Cov}(F,\Delta),\\
\operatorname{Cov}(W,D)={}&2\operatorname{Var}D
+2\operatorname{Cov}(D,F)+\operatorname{Cov}(D,\Delta).
\end{aligned}
\]
These simplify to (2)--(3). In the covariance polynomial \(8n^2-15n-32\), the values at \(n=2,3\) are negative, and it is increasing and positive for integer \(n\ge4\). By (1), \(W-2D\) has variance \((n^2+n+48)/6=O(n^2)\), whereas \(\operatorname{Var}D\sim2n^3/45\). The classical uniform-permutation footrule central limit theorem therefore transfers to \(W\) by Slutsky's theorem. Expanding the exact correlation from (2), (3), and (8) gives \(1-15/(32n)+O(n^{-2})\).

**3. Uniform full transformations.** Under the uniform law on \(T_n\), the coordinates \(U(i)\) are independent uniform values in \([n]\). Put
\[
g_{ij}=\mathbf1_{\{i>1\}}|i-1-j|+
\mathbf1_{\{i<n\}}|i+1-j|.
\]
Then \(W(U)=\sum_i g_{i,U(i)}\) is a sum of independent random variables. Direct finite arithmetic progressions give
\[
\sum_{ij}g_{ij}=\frac{n(n-1)(2n-1)}3,\quad
\sum_{ij}g_{ij}^2=\frac{2n^4-6n^3+n^2+21n-24}{3},
\]
\[
\sum_i\left(\sum_jg_{ij}\right)^2
=\frac{n(14n^4-45n^3+80n^2-45n-64)}{30}.
\]
By coordinate independence, \(\operatorname{Var}W(U)=(1/n)\sum_{ij}g_{ij}^2-(1/n^2)\sum_i(\sum_jg_{ij})^2\), giving (5), while the first sum yields the common mean. The total variance is asymptotic to \(n^3/5\); individual centered contributions are bounded by \(2(n-1)\). Thus the maximum centered summand divided by the standard deviation tends to zero, verifying Lindeberg's condition and proving the full-transformation CLT. Comparing \(8n^3/45\) with \(n^3/5\) yields the limiting variance ratio \(8/9\).

## Verification
Run `python3 verify_crosswork.py` (Python standard library only) in the same directory. The checker independently computes the original adjacent cross-work sum, rather than defining it from the footrule. It exhaustively checks (1)--(3) for all \(n!\) permutations at each \(2\le n\le8\), and (1), (2)'s mean and (5) for all \(n^n\) full maps at each \(2\le n\le6\). It also checks permutation row/column assignment covariance and independent-image variance from their defining arrays at \(n=9,10,20,50,100\), using exact rational arithmetic. A successful run ends `VERIFY_OK`. Exhaustive finite checks support but do not replace the all-size proof.

## Relationship to prior work
Udo, Owai and Francis (2026, arXiv:2610.34902v1) define cross-work and obtain group/monoid total or average formulas; those definitions and means are prior work. Francis and Ranaivomanana (2026) investigate cross-work for partial transformations, with extremal and enumerative results. Diaconis and Graham (1977) establish fundamental footrule results, including its permutation central limit theorem; the latter is explicitly invoked here. The new contribution asserted is the **pointwise cross-work/footrule/fixed-point/endpoint identity together with its exact permutation covariance transition, both complete finite-sample variances, and their asymptotic comparison**. The existing footrule variance and CLT are not claimed as new.

## Limitations
The assertions apply only to the full transformation monoid and its unit group, not arbitrary partial transformations, weighted transformations or nonuniform laws. The pointwise identity does not itself determine the entire distribution of \(W\), and the Gaussian results are asymptotic, not finite-sample normality. Earlier nonindexed or differently named second-moment formulas may affect historical priority. No independent mathematical audit or external certification has been performed.

## References
1. N. E. Udo, V. A. Owai, M. O. Francis, *Cross work induced by transformations on symmetric group and related transformation semigroups*, arXiv:2610.34902v1 (first posted 2026-10-26). https://arxiv.org/html/2610.34902
2. M. O. Francis, V. H. Ranaivomanana, *Cross Work Performed by Partial Transformations*, Palestine Journal of Mathematics 15(1) (2026), 673–688. https://pjm.ppu.edu/sites/default/files/papers/PJM_15(1)_2026_673_to_688.pdf
3. P. Diaconis, R. L. Graham, *Spearman's Footrule as a Measure of Disarray*, Journal of the Royal Statistical Society B 39 (1977), 262–268. https://mathweb.ucsd.edu/~ronspubs/77_04_spearmans.pdf
