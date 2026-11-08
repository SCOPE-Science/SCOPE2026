# Compact mixed Cesàro products and sharp Hilbert–Schmidt dimension thresholds on Drury–Arveson space

## Finding
Let \(d\ge 2\) be a finite integer. On the complex Drury–Arveson space \(H_d^2\) with reproducing kernel \((1-\langle z,w\rangle)^{-1}\), take the coordinate Cesàro operators introduced in [1]:
\[
C_j z^\alpha=\sum_{q=0}^{\infty}\frac{z^{\alpha+qe_j}}{|\alpha|+q+1},\qquad 1\le j\le d.
\]
For every pair of distinct indices \(i,j\), both mixed products \(C_iC_j\) and \(C_jC_i\) are compact. More sharply, writing \(\mathcal S_2\) for the Hilbert–Schmidt ideal,
\[
\boxed{C_iC_j\in\mathcal S_2\ \Longleftrightarrow\ 2\le d\le3},\qquad
\boxed{[C_i,C_j]\in\mathcal S_2\ \Longleftrightarrow\ 2\le d\le5}.
\]
Here \([C_i,C_j]=C_iC_j-C_jC_i\). The operators genuinely fail to commute: the coefficients of \(z_i\) and \(z_j\) in \([C_i,C_j]1\) are respectively \(1/4\) and \(-1/4\). Each \(C_j\) itself is noncompact, so the corresponding nonzero elements of the Calkin algebra annihilate each other pairwise. Thus this noncommuting tuple is pairwise zero-multiplicative, and hence commuting, modulo compact operators, even in dimensions where its commutators are not Hilbert–Schmidt.

## Assumptions and scope
All statements concern one fixed finite \(d\ge2\), the standard complex Drury–Arveson Hilbert space, and distinct coordinate operators from the displayed definition. Multi-indices \(\alpha\) have nonnegative integer coordinates; \(n=|\alpha|\). The squared monomial norm is
\[
w_\alpha=\|z^\alpha\|^2=\frac{\alpha!}{|\alpha|!},\qquad e_\alpha=\frac{z^\alpha}{\sqrt{w_\alpha}}.
\]
Compactness is in the usual operator norm. The characterization of \(\mathcal S_2\) includes both borderline dimensions; it does not state a classification of other Schatten ideals or joint spectra.

## Proof
**1. Exact matrix coefficients.** For \(k,l\ge0\), set \(r=k+l\). Applying \(C_j\) first and then \(C_i\), with \(i\ne j\), gives the coefficient of \(z^{\alpha+ke_i+le_j}\) as
\[
P_{n;k,l}=\frac{1}{(n+l+1)(n+r+1)}.
\]
Interchanging \(i\) and \(j\) gives \(P_{n;l,k}\); their difference is
\[
D_{n;k,l}=\frac{k-l}{(n+k+1)(n+l+1)(n+r+1)}.
\]
The corresponding orthonormal-basis coefficients acquire the factor \(\sqrt{w_{\alpha+ke_i+le_j}/w_\alpha}\). Distinct pairs \((k,l)\) give distinct output basis elements for each input.

**2. Exact degree-summed weight identity.** With the rising factorial notation \((a)_r=a(a+1)\cdots(a+r-1)\),
\[
\frac{w_{\alpha+ke_i+le_j}}{w_\alpha}
=\frac{(\alpha_i+1)_k(\alpha_j+1)_l}{(n+1)_r}.
\]
Using \(\sum_{a\ge0}\binom{a+k}{k}x^a=(1-x)^{-k-1}\), the coefficient of degree \(n\) in \((1-x)^{-(d+r)}\) gives the exact finite sum
\[
\boxed{W_d(n;k,l):=\sum_{|\alpha|=n}\frac{w_{\alpha+ke_i+le_j}}{w_\alpha}
=\frac{k!l!}{(r+d-1)!}\prod_{s=1}^{d-1}(n+r+s)}.
\]
Consequently the squared Hilbert–Schmidt norms, whenever finite, are exactly the nonnegative series
\[
\|C_iC_j\|_{\mathcal S_2}^2=\sum_{n,k,l\ge0}P_{n;k,l}^2W_d(n;k,l),
\qquad
\|[C_i,C_j]\|_{\mathcal S_2}^2=\sum_{n,k,l\ge0}D_{n;k,l}^2W_d(n;k,l).
\]
These series remain valid as extended nonnegative quantities when they diverge.

**3. Upper Hilbert–Schmidt bounds.** The elementary inequality
\(\sum_{k=0}^{r}k!(r-k)!\le3r!\) follows because the endpoints contribute \(2r!\) and each interior reciprocal binomial coefficient is at most \(1/r\) (handle \(r=0,1\) directly). For constants depending only on \(d\), group the above series by \(r=k+l\). For the product, use \(n+l+1\ge n+1\) to bound the grouped contribution by
\[
C_d\frac{(n+r+1)^{d-3}}{(n+1)^2(r+1)^{d-1}}.
\]
If \(d\le3\), its value is at most \(C_d/(n+1)^2(r+1)^2\), so the double sum converges. For the commutator, use \((n+k+1)(n+l+1)\ge(n+1)(n+r+1)\) and \(|k-l|\le r\). The grouped contribution is bounded by
\[
C_d\frac{r^2(n+r+1)^{d-5}}{(n+1)^2(r+1)^{d-1}}.
\]
For \(d\le5\), this is at most \(C_d/(n+1)^2(r+1)^2\), again summable.

**4. Sharp failures above the thresholds.** The \(k=l=0\) coefficient in \(C_iC_j\) equals \((n+1)^{-2}\) on each degree-\(n\) monomial. Hence
\[
\|C_iC_j\|_{\mathcal S_2}^2\ge
\sum_{n\ge0}\binom{n+d-1}{d-1}\frac1{(n+1)^4}=+\infty\quad(d\ge4).
\]
For the commutator, take \((k,l)=(1,0)\). Then \(|D_{n;1,0}|=((n+1)(n+2)^2)^{-1}\), and the squared monomial weight ratio is \((\alpha_i+1)/(n+1)\). For all sufficiently large \(n\), there are at least \(c_dn^{d-1}\) degree-\(n\) multi-indices with \(\alpha_i\ge n/2\). On them this ratio is at least \(1/2\). Their contribution therefore dominates \(c_d\sum_n n^{d-7}\), which diverges precisely for \(d\ge6\).

**5. Compactness in every finite dimension.** Fix a coordinate \(j\). For each choice of exponents away from coordinate \(j\), let \(m\ge0\) be their total. The invariant orthogonal slice is a weighted \(\ell_2\) space with weights \(w_{q,m}=q!m!/(q+m)!\). On its normalized basis the matrix of \(C_j\) is
\[
A^{(m)}_{q,s}=\boldsymbol1_{q\ge s}\frac1{q+m+1}
\sqrt{\frac{w_{q,m}}{w_{s,m}}}.
\]
For \(m\ge1\), the row sums are at most one. Since \(\log(1+m/t)\ge m/(t+m)\), one obtains, for \(q\ge s\),
\[
\sqrt{\frac{w_{q,m}}{w_{s,m}}}\le
\left(\frac{s+m+1}{q+m+1}\right)^{m/2}.
\]
The column sums are then bounded by the first term plus its integral:
\[
\sum_{q\ge s}A^{(m)}_{q,s}
\le\frac1{s+m+1}+\frac2m\le\frac3m.
\]
Schur's test gives \(\|C_j\|_{\text{slice }m}\le\sqrt{3/m}\). At \(m=0\) the slice is the classical Cesàro operator, with norm \(2\) [3]. Thus \(\|C_j\|\le2\), and the restriction to any exponent-coordinate projection \(P_{N,k}\), with \(k\ne j\) and exponent \(\alpha_k\ge N\), satisfies \(\|C_jP_{N,k}\|\le\sqrt{3/N}\).

Each \(C_j\) only increases exponents, so every \(P_{N,k}\) is invariant under every coordinate operator. For \(i\ne j\), at least one of the two factors in \(C_iC_j\) has \(k\) as a spectator coordinate. Therefore \(\|C_iC_jP_{N,k}\|\le2\sqrt{3/N}\) for all \(k\). Every monomial of total degree at least \(dN\) has some coordinate at least \(N\). Partition the high-degree basis by its first such coordinate, and apply the triangle inequality across the \(d\) parts. If \(Q_N\) projects onto degrees at least \(dN\), then
\[
\|C_iC_jQ_N\|\le2d\sqrt{3/N}\longrightarrow0.
\]
The complementary low-degree projection has finite rank; hence \(C_iC_j\) is compact. The same applies to the reversed product, making their commutator compact. Finally, restricting \(C_j\) to functions of \(z_j\) alone recovers the noncompact classical Cesàro operator, so its Calkin class is nonzero. The coefficient computation in Step 1 proves \([C_i,C_j]\ne0\).

## Verification
An accompanying standalone script `check_cesaro_products.py` checks \(4056\) finite exact identities or numerical inequalities, including the degree-summed factorial formula, coefficient antisymmetry, and finite Schur bounds. Run it using `python check_cesaro_products.py`; it prints `COORDINATE_CESARO_FINITE_IDENTITIES_OK 4056`. The finitary checks corroborate algebraic steps only. Convergence/divergence, compactness, and ideal membership are proved by the preceding infinite arguments, not by enumeration.

## Relationship to prior work
Pilla [1] introduced these coordinate operators, proved boundedness, and observed noncommutation. Pilla [2] determined their exact individual norm and studied Rhaly-type generalizations. Neither of these inspected works gives the mixed-product compactness theorem, the Calkin annihilation structure, or either sharp Hilbert–Schmidt dimension threshold. The classical one-variable Cesàro bound [3] is used only for the zero-spectator slice. All elementary factorial identities and Schur estimates are proved above rather than claimed as new standalone results.

## Limitations
The results are for finite complex dimension \(d\), the canonical Drury–Arveson norm, and the exact coordinate Cesàro tuple. They do not characterize \(\mathcal S_p\) for \(p\ne2\), numerical approximation rates, or the essential joint Taylor spectrum. The originality comparison is best-knowledge rather than independently certified; an older general operator-ideal result for multivariable Cesàro or Hausdorff matrices could potentially imply parts of the classification.

## References
[1] M. R. Pilla, *Cesàro-Type Operators Acting on the Drury-Arveson Space*, arXiv:2606.24710v1, publicly submitted June 23, 2026, https://arxiv.org/abs/2606.24710.

[2] M. R. Pilla, *Rhaly-Type Operators in Several Complex Variables*, arXiv:2606.25885v1, publicly submitted June 24, 2026, https://arxiv.org/abs/2606.25885.

[3] A. Brown, P. R. Halmos, and A. L. Shields, *Cesàro operators*, Acta Sci. Math. (Szeged) **26** (1965), 125–137 (classical Hardy-space Cesàro norm).
