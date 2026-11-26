# Gaussian descent fluctuations and a variance peak under linear record bias

## Finding
For each integer \(n\ge 2\), let \(\sigma_n\) have the record-biased law
\[
\Pr\{\sigma_n=\sigma\}=\frac{\theta_n^{\operatorname{rec}(\sigma)}}{\theta_n(\theta_n+1)\cdots(\theta_n+n-1)},
\]
where \(\theta_n>0\) and \(\operatorname{rec}(\sigma)\) counts left-to-right maxima. Let \(D_n\) count indices \(1\le j<n\) with \(\sigma_n(j)>\sigma_n(j+1)\). For every deterministic parameter sequence satisfying \(\theta_n/n\to\lambda\in(0,\infty)\),
\[
\frac{\operatorname{Var}(D_n)}n\longrightarrow v(\lambda)
=\frac{6\lambda^2+4\lambda+1}{12(1+\lambda)^3},\qquad
\frac{D_n-\mathbb E D_n}{\sqrt n}\ \Rightarrow\ N(0,v(\lambda)).
\]
The exact centering is the previously known formula
\[
\mathbb E D_n=\frac{n(n-1)}{2(\theta_n+n-1)}.
\]
Furthermore \(v\) has one global maximizer on the positive half-line:
\[
\lambda_* =\frac{2+\sqrt{10}}6,\qquad
v(\lambda_*)=\frac{68+5\sqrt{10}}{729}.
\]
In particular, descent fluctuations initially *increase* when linear record bias rises from zero, before decreasing for stronger bias.

## Assumptions and scope
The permutation law is the standard record-weighted law with real, positive \(\theta_n\). The limit assumes \(n\to\infty\), \(\lambda>0\), and no further rate restriction on convergence \(\theta_n/n\to\lambda\). The normalization is \(\sqrt n\), and the Gaussian has the nonzero variance displayed above. For arbitrary slowly converging \(\theta_n/n\), it is essential to center by the exact expectation, not automatically by \(n/[2(1+\lambda)]\). The case \(\lambda=0\) is not included in the triangular-array theorem, although the continuous extension of \(v\) to zero is \(1/12\).

## Proof
**Independent insertion ranks.** For a word representing a permutation, let \(R_j\in\{1,\ldots,j\}\) be the rank of its value at position \(j\) among the first \(j\) values. The existing record-biased insertion construction (Reference 2, Section 3.2) gives independence of \(R_1,\ldots,R_n\), with
\[
\Pr(R_j=r)=\begin{cases}
1/(\theta+j-1),&1\le r<j,\\
\theta/(\theta+j-1),&r=j.
\end{cases}
\]
Here and below \(\theta\) denotes an arbitrary fixed parameter at a single finite size, later specialized to \(\theta_n\). The indicator \(B_j=\mathbf1_{\{\sigma(j)>\sigma(j+1)\}}\) equals \(\mathbf1_{\{R_{j+1}\le R_j\}}\). Consequently the sequence \(B_1,\ldots,B_{n-1}\) is **1-dependent**: collections of indicators at index distance at least two are independent.

**Exact first and adjacent second moments.** Summation over \(R_j,R_{j+1}\) gives, for \(1\le j<n\),
\[
p_j:=\Pr(B_j=1)=\frac{j(2\theta+j-1)}{2(\theta+j-1)(\theta+j)}.
\]
This marginal and the resulting expectation are already in References 1–2. For \(1\le j<n-1\), summation over three independent ranks gives
\[
\Pr(B_j=B_{j+1}=1)
=\frac{j(j+1)(j-1+3\theta)}{6(\theta+j-1)(\theta+j)(\theta+j+1)}.
\]
Indeed, condition on \(R_{j+1}=u\), sum \(u(j-u+\theta)\) over \(u=1,\ldots,j\), and divide by the three rank denominators. Subtracting \(p_jp_{j+1}\) simplifies the adjacent covariance to
\[
c_j=-\frac{j(j+1)(6\theta^2+4\theta(j-1)+j(j-1))}{12(\theta+j)^2(\theta+j-1)(\theta+j+1)}<0.
\]
Thus all nonadjacent covariances vanish, and the **finite exact variance identity** is
\[
\operatorname{Var}(D_n)=\sum_{j=1}^{n-1}p_j(1-p_j)
+2\sum_{j=1}^{n-2}c_j.
\tag{1}
\]
The bound \(c_j<0\) is valid for every \(\theta>0\) and every admissible index; it does not assert joint independence of adjacent indicators.

**Linear-bias variance limit.** Set \(\theta=\theta_n\) with \(\theta_n/n\to\lambda>0\), and write \(x=j/n\). Uniformly for indices on the full scaled interval \([0,1]\), the rational functions in (1) converge to the continuous profiles
\[
p(x)=\frac{x(2\lambda+x)}{2(\lambda+x)^2},\qquad
c(x)=-\frac{x^2(6\lambda^2+4\lambda x+x^2)}{12(\lambda+x)^4}.
\]
Uniformity at \(x=0\) follows because \(\lambda>0\), keeping all rescaled denominators bounded away from zero. The Riemann sums therefore give
\[
\lim_{n\to\infty}\frac{\operatorname{Var}(D_n)}n
=\int_0^1[p(x)(1-p(x))+2c(x)]\,dx.
\]
Direct algebra shows that the integrand is
\[
\frac{x(12\lambda^3+6\lambda^2x+4\lambda x^2+x^3)}{12(\lambda+x)^4}
=\frac{d}{dx}\left[\frac{x^2(6\lambda^2+4\lambda x+x^2)}{12(\lambda+x)^3}\right].
\]
Evaluation at zero and one proves the claimed formula for \(v(\lambda)>0\).

**Triangular-array central limit theorem.** Set \(Z_{n,j}=B_j-\mathbb EB_j\). For each \(n\), this is a bounded, mean-zero, 1-dependent array with total variance asymptotic to \(nv(\lambda)\). Partition \(\{1,\ldots,n-1\}\) into contiguous blocks of length \(\ell_n=\lfloor n^{1/4}\rfloor\), separated by one discarded index (and allow a shorter terminal block). Block sums are mutually independent because separate blocks have indicator-index distance at least two. The discarded collection contains \(O(n/\ell_n)\) bounded centered variables, themselves with covariance only at distance one, so its sum has variance \(O(n/\ell_n)=o(n)\). Consequently the independent block sums retain asymptotic variance \(nv(\lambda)\). Each centered block sum has absolute value at most \(\ell_n=o(\sqrt n)\), so the Lindeberg condition holds and the Lindeberg–Feller theorem gives a Gaussian limit for the normalized sum of blocks. The discarded sum is negligible in \(L^2/\sqrt n\); Slutsky's theorem yields the asserted limit for \(D_n\).

**Sharp bias at peak variance.** Differentiation gives
\[
v'(\lambda)=\frac{-6\lambda^2+4\lambda+1}{12(1+\lambda)^4}.
\]
The numerator has exactly one positive zero, \(\lambda_*=(2+\sqrt{10})/6\), with positive derivative before and negative derivative afterward. Substitution gives \(v(\lambda_*)=(68+5\sqrt{10})/729\). The coefficient tends to zero as \(\lambda\to\infty\), establishing global uniqueness.

## Verification
The accompanying dependency-free `check.py` uses exact rational arithmetic and independently enumerates every permutation of sizes two through seven for four distinct positive rational biases. It compares the normalization, every one-site descent probability, every adjacent and nonadjacent two-site descent probability, the exact expectation, and the exact variance. It also evaluates finite-size variance against the asymptotic coefficient for positive rational ratios, with exact rational inequalities. Running `python3 check.py` completes with `PASS 376 exact assertions`. This is corroboration, **not** an infinite-size proof; the latter is the algebra, Riemann-sum argument, and blocking theorem above.

## Relationship to prior work
Auger, Bouvel, Nicaud and Pivoteau (2016, Reference 1) introduced the record-biased law and gave descent probabilities and expectations, including the linear-bias expectation regime. Bouvel, Nicaud and Pivoteau (2024, Reference 2) provide the independent diagram insertion construction and prove a descent CLT **when the record bias is fixed**, while studying linear bias through expectations and a deterministic permuton limit. Their Sections 4.2 and 4.3 explicitly distinguish these regimes. Féray (Reference 3) studies asymptotics of permutation statistics for the classical fixed-parameter Ewens model; a growing-parameter implication was not established from the inspected materials. The present claim concerns a growing positive bias with its explicit second-order variance coefficient, the associated Gaussian fluctuation law, and the unique peak of that coefficient. Generic finite-dependence CLTs supply a tool but do not state this model-specific coefficient. The already-known mean formula is not claimed as novel.

## Limitations
This proves the Gaussian limit only when \(\theta_n/n\) converges to a **finite, strictly positive** constant. It provides neither a uniform Berry–Esseen bound nor a theorem for sublinear or superlinear bias. Stronger published general fluctuation theorems or an unnoticed treatment of anti-exceedances under varying Ewens parameter might imply part of the assertion; historical priority therefore remains open to independent review. No independent audit has been conducted.

## References
1. N. Auger, M. Bouvel, C. Nicaud, C. Pivoteau, *Analysis of Algorithms for Permutations Biased by Their Number of Records*, AofA 2016, arXiv:1605.02905v1, https://arxiv.org/pdf/1605.02905.
2. M. Bouvel, C. Nicaud, C. Pivoteau, *Record-biased permutations and their permuton limit*, arXiv:2409.01692v1 (public September 3, 2024), https://arxiv.org/html/2409.01692v1, Sections 3.2, 4.1–4.3.
3. V. Féray, *Asymptotic behavior of some statistics in Ewens random permutations*, arXiv:1201.2157 (2012), https://arxiv.org/abs/1201.2157.
