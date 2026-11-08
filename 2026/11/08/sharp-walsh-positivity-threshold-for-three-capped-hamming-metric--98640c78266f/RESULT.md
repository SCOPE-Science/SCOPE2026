# Sharp Walsh positivity threshold for three-capped Hamming metrics

## Finding

For \(n\ge4\), equip \(G_n=\mathbb F_2^n\) with the **three-capped Hamming metric**
\[
\rho_n(x,y)=\min\{\operatorname{wt}(x-y),3\}.
\]
The capped radial Schoenberg kernels
\[
K_{t,p}(x,y)=\exp\bigl(-t\rho_n(x,y)^p\bigr),\qquad t>0,\ p>0,
\]
are positive semidefinite for every \(t>0\) **exactly** for \(0<p\le\beta_n\), where the unique \(\beta_n\in(0,1)\) solves
\[
\boxed{\begin{aligned}
(n-2)3^{\beta_n}-(n-4)2^{\beta_n}&=4&& (n\text{ even}),\\
(n-5)3^{\beta_n}-(n-9)2^{\beta_n}&=6&& (n\text{ odd}).
\end{aligned}}
\]
For \(p>\beta_n\), the kernel is not positive semidefinite for all sufficiently small positive \(t\). Equivalently, \(\rho_n^p\) has strict negative type below the threshold, nonstrict negative type at it, and no negative type above it.

Set
\[
s_n=\begin{cases}n/2+1,&n\text{ even},\\(n+3)/2,&n\text{ odd}.\end{cases}
\]
At the endpoint, the full zero-sum nullspace is spanned by Walsh characters indexed by subsets of size \(s_n\), and has dimension \(\binom n{s_n}\). The minimal Euclidean dimension of a realization of the distances \(\rho_n^{p/2}\) is
\[
\begin{cases}2^n-1,&0<p<\beta_n,\\2^n-1-\binom n{s_n},&p=\beta_n.\end{cases}
\]
Above the threshold there is no such real Hilbert realization. Moreover, with \(L=\log(3/2)\),
\[
\beta_n=\frac{2}{nL}+\frac{c_n}{n^2}+O(n^{-3}),\qquad
c_n=\begin{cases}
(2\log3-10\log2)/L^2,&n\text{ even},\\
(8\log3-20\log2)/L^2,&n\text{ odd}.
\end{cases}
\]
In particular, \(n\beta_n\to2/\log(3/2)\), and the endpoint dimension loss satisfies \(\binom n{s_n}\sim2^n\sqrt{2/(\pi n)}\).

## Assumptions and scope

All calculations concern the full Boolean group \(G_n\), every integer \(n\ge4\), and real exponents \(p>0\). The binary Hamming weight is the number of nonzero coordinates; \(\rho_n\) equals ordinary Hamming distance for weights at most three and equals three for all larger weights. It is a metric because \(u\mapsto\min(u,3)\) is nondecreasing and subadditive on nonnegative reals. The normalization uses unnormalized Walsh transforms and ordinary squared Euclidean distances. The special case \(n=3\), where capping changes nothing, is excluded: its critical exponent is one with a different endpoint nullspace.

## Proof

**1. Fourier diagonalization.** For each subset \(S\subseteq\{1,\ldots,n\}\), let \(\chi_S(x)=(-1)^{\sum_{j\in S}x_j}\) and \(s=|S|\). Translation invariance diagonalizes \(D_p=(\rho_n(x,y)^p)_{x,y\in G_n}\) on these characters. For a nonconstant character, the sums over shells of weights one and two are
\[
K_1(s)=n-2s=:z,\qquad K_2(s)=\frac{z^2-n}{2}.
\]
Since the Fourier sum of the indicator of all nonzero vectors is \(-1\), every nonconstant eigenvalue is
\[
\lambda_s(p)=-3^p+(1-3^p)z+(2^p-3^p)\frac{z^2-n}{2},\quad 1\le s\le n,
\]
with multiplicity \(\binom ns\). The constant-character eigenvalue is positive for \(p>0\). By character orthogonality, \(D_p\) is conditionally negative semidefinite exactly when all \(\lambda_s(p)\le0\).

**2. Unique critical Walsh level.** For \(p>0\), the displayed expression is a strictly concave quadratic in the permitted integers \(z=n-2s\), and its real vertex is \(-R(p)\), with
\[
R(p)=\frac{3^p-1}{3^p-2^p}=\frac{1-e^{-p\log3}}{1-e^{-p\log(3/2)}}.
\]
The function \(R\) decreases strictly: the derivative of \(\log R\) is \(\log3/(e^{p\log3}-1)-\log(3/2)/(e^{p\log(3/2)}-1)<0\), because \(a/(e^{pa}-1)\) decreases in \(a>0\). Hence \(2\le R(p)<\log3/\log(3/2)<3\) for \(0<p\le1\). Therefore, among all admissible \(z\), the unique maximum is at \(z=-2\) when \(n\) is even, and at \(z=-3\) when \(n\) is odd and \(p<1\). The odd case has a tie with \(z=-1\) only at \(p=1\), which is beyond the critical exponent.

**3. Sharp threshold and strictness.** At these critical levels, direct substitution gives
\[
2\lambda_{s_n}(p)=\begin{cases}
(n-2)3^p-(n-4)2^p-4,&n\text{ even},\\
(n-5)3^p-(n-9)2^p-6,&n\text{ odd}.
\end{cases}
\]
Both expressions equal \(-2\) at \(p=0\), are positive at \(p=1\), and are strictly increasing for all \(p\ge0\). For even \(n\), this follows from \((n-2)\log3\,3^p>(n-4)\log2\,2^p\). For odd \(n=5,7,9\), the stated expression has only positive coefficients of its nonconstant terms; for odd \(n\ge11\), \((n-5)\log3\,3^p>(n-9)\log2\,2^p\). There is thus a unique zero \(\beta_n\in(0,1)\). All other nonconstant Walsh levels are strictly negative there, while the critical level becomes positive for every \(p>\beta_n\). This proves the entire conditional-negative-type phase diagram for all \(p>0\).

**4. Positive definite kernels and Hilbert dimension.** The finite Schoenberg correspondence gives positive semidefiniteness of \(\exp(-t D_p)\) for all \(t>0\) if and only if \(D_p\) is conditionally negative semidefinite. Conversely, if \(\lambda_{s_n}(p)>0\), then the Fourier eigenvalue of the entrywise exponential kernel on this character is \(-t\lambda_{s_n}(p)+O(t^2)<0\) as \(t\downarrow0\). For any \(p\le\beta_n\), the centered Gram matrix of the Euclidean points realizing \(\rho_n^{p/2}\) is \(-\tfrac12 JD_pJ\), where \(J=I-2^{-n}\mathbf1\mathbf1^T\). It has one zero constant mode and exactly the nonconstant zero modes just determined. Its rank is the minimal affine Euclidean embedding dimension. At \(p=\beta_n\), every critical Walsh character is an explicit equality witness for the negative-type inequality.

**5. Asymptotic expansion.** Uniformly for \(p=O(n^{-1})\), expand \(3^p\) and \(2^p\) in the parity-specific threshold equations. The constant terms give \(n\beta_n\to2/L\), with \(L=\log(3/2)\); monotonicity of the threshold functions bounds the root by two fixed multiples of \(1/n\). Substituting \(\beta_n=2/(nL)+c_n/n^2\) and matching the coefficient of \(n^{-1}\) gives respectively
\[
c_n=\frac{2\log3-10\log2}{L^2},\qquad c_n=\frac{8\log3-20\log2}{L^2}.
\]
The residual is \(O(n^{-2})\) in the defining equation, whose derivative is \(nL+O(1)\), so the root error is \(O(n^{-3})\). Finally Stirling's formula gives \(\binom n{s_n}\sim2^n\sqrt{2/(\pi n)}\).

## Verification

The self-contained `capped_hamming3_checker.py` recomputes the full nonconstant Walsh spectrum, numerically isolates the unique threshold for each integer \(4\le n\le14\), checks the strict sign separation and endpoint nullity, and independently evaluates the complete group-character sums for \(4\le n\le10\). It also checks the parity-specific second-order asymptotic approximation at large dimensions. Running `python3 capped_hamming3_checker.py` produced `CAPPED_HAMMING3_WALSH_CHECKS_OK`. Illustrative values are \(\beta_4=0.630929753571\), \(\beta_5=0.584962500721\), \(\beta_6=0.482147185182\), and \(\beta_7=0.447991390556\). Numerical checks are corroboration, not the proof of the infinite-family theorem.

## Relationship to prior work

The general theory of strict negative type, powered-distance determinants, and Hamming-cube harmonic analysis appears in Li–Weston [1], Sánchez [2], Murugan [3], and Barg–Skriganov [4]. In particular, Sánchez supplies a general determinant characterization of finite-metric exponents, while Murugan analyzes the **uncapped** cube and its subsets at exponent one. Barg–Skriganov explains the Hamming-scheme/Krawtchouk spectral connection. The present specialization fixes the capped metric with three nonzero distance levels and derives its exact first failing Walsh layer, its endpoint multiplicity, and its two-term dimensional asymptotic rather than merely a general decision criterion. Deza–Maehara's earlier truncated-graph-metric work [5] is a relevant potential antecedent; accessible secondary descriptions concern two-distance graph truncations, not the present complete family, but the unavailable original full text remains a historical-comparison risk.

## Limitations

The result does not classify other cap radii, nonbinary alphabets, or arbitrary radial metric transforms, and it does not claim the historical priority of the sharp exponent beyond the bounded literature search. The identified inaccessible older source could require a further originality comparison. Independent validation is not represented by the finite checker or the present self-review.

## References

1. H. Li and A. Weston, *Strict p-negative type of a metric space*, first public arXiv version 6 January 2009, https://arxiv.org/abs/0901.0695.
2. S. Sánchez, *On the supremal p-negative type of a finite metric space*, first public arXiv version 2 August 2011, https://arxiv.org/html/1108.0451v1.
3. M. K. Murugan, *Generalized roundness of vertex transitive graphs*, first public arXiv version 23 December 2011, https://arxiv.org/abs/1112.5657.
4. A. Barg and M. Skriganov, *Association schemes on general measure spaces and zero-dimensional Abelian groups*, first public arXiv version 20 October 2013, https://arxiv.org/abs/1310.5359.
5. M. Deza and H. Maehara, *Metric transforms and Euclidean embeddings*, Transactions of the American Mathematical Society 317 (1990), 661–671, DOI:10.1090/S0002-9947-1990-0974513-6. (Original full text not inspected.)
