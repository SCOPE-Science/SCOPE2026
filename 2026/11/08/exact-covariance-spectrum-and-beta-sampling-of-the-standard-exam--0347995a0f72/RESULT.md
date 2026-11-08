# Exact covariance spectrum and beta sampling of the standard-example order polytope

## Finding
For every integer \(n\ge2\), consider the \(2n\)-dimensional order polytope
\[
P_n=\{(a_1,\ldots,a_n,b_1,\ldots,b_n)\in[0,1]^{2n}:a_i\le b_j\text{ whenever }i\ne j\}.
\]
This is the order polytope of the standard-example poset with \(n\) minimal and \(n\) maximal elements. A uniformly volume-distributed vector \((A,B)\in P_n\) has the exact beta-factorized sampling law specified below. It yields **every polynomial moment** by a finite beta-polynomial expectation, and the covariance matrix has the following four explicit eigenvalues:
\[
\begin{aligned}
\lambda_{0,+}&=\frac1{12},\\
\lambda_{0,-}&=\frac{n^4+3n^3+4n^2-9n+37}{12(n+1)^2(2n+1)^2},\\
\lambda_{1,+}&=\frac{n^3+4n^2+2n+2}{24(n+1)^2(2n+1)},\\
\lambda_{1,-}&=\frac{n^4+4n^3+8n^2+26n+48}{24n(n+1)^2(2n+1)}.
\end{aligned}
\]
The first two have multiplicity one; the last two each have multiplicity \(n-1\). The four formula branches need not be distinct at small \(n\). In the standard coordinate metric, the first corresponds to the all-ones direction. All four eigenvalues are positive. Covariances between every two distinct coordinates are strictly positive for \(n\ge3\); at \(n=2\), the only zero off-diagonal covariances are between coordinates from different independent two-chains. Moreover, for distinct indices \(i\ne j\),
\[
\operatorname{Cov}(A_i,B_j)-\operatorname{Cov}(A_i,B_i)
=\frac{n^2+4n+8}{8n(n+1)^2(2n+1)}>0.
\]
The exact ordinary coordinate volume is \(\operatorname{Vol}(P_n)=(n-1)!(n+1)!/(2n)!\), a **previously known** result, not a novelty claim. The affine-invariant isotropic constant therefore satisfies
\[
L(P_n)^2=\frac{\left[\lambda_{0,+}\lambda_{0,-}(\lambda_{1,+}\lambda_{1,-})^{n-1}\right]^{1/(2n)}}{\operatorname{Vol}(P_n)^{1/n}}
\longrightarrow \frac1{12}\quad (n\to\infty).
\]
Here \(L(K)^2=\det(\operatorname{Cov}(X))^{1/d}/\operatorname{Vol}(K)^{2/d}\) for a uniformly distributed point \(X\) in a full-dimensional \(d\)-body \(K\).

## Assumptions and scope
The body is in the full ambient coordinate space \(\mathbb R^{2n}\), with unnormalized Lebesgue volume, not an intrinsic metric on an affine quotient. Every inequality is weak but boundary sets have zero volume. The minimum \(n=2\) consists of two independent two-element chains. The result covers all integers \(n\ge2\), not arbitrary height-two posets and not cyclic crown posets of larger size. All random draws described below are independent except where explicitly coupled by their formulas.

## Proof
**1. Disintegration and exact sampler.** Set \(v\) and \(u\) to be the second-largest and largest coordinates among the lower row \((a_i)\), with unique indices \(\ell\) and \(k\), respectively, almost surely. For every fixed lower row the allowed upper-row box is \([v,1]\) at coordinate \(k\) and \([u,1]\) at all other coordinates. Consequently the upper-box volume is \((1-v)(1-u)^{n-1}\). For fixed \(0<v<u<1\), the lower-row integration measure, summed over the \(n(n-1)\) ordered index pairs, is \(n(n-1)v^{n-2}\,dv\,du\). Thus
\[
\operatorname{Vol}(P_n)=n(n-1)\int_0^1\int_v^1v^{n-2}(1-v)(1-u)^{n-1}\,du\,dv
=(n-1)\operatorname B(n-1,n+2)=\frac{(n-1)!(n+1)!}{(2n)!}.
\]
Normalize the preceding density: \(V=v\sim\operatorname{Beta}(n-1,n+2)\). Conditional on \(V\), \(U=u=V+(1-V)Z\), where \(Z\sim\operatorname{Beta}(1,n)\) is independent of \(V\). Select ordered distinct indices \((k,\ell)\) uniformly. Set \(A_k=U\), \(A_\ell=V\), and make every other \(A_i\) independently uniform on \([0,V]\). Conditional on these lower coordinates, draw \(B_k\) uniformly on \([V,1]\) and every \(B_j\), \(j\ne k\), independently uniformly on \([U,1]\). The normalized disintegration proves this sampler has **exactly the uniform volume law** of \(P_n\).

**2. All polynomial moments.** Define the polynomial \(H_m(t)=(1+t+\cdots+t^m)/(m+1)\) for every integer \(m\ge0\). For arbitrary nonnegative integer vectors \(\alpha,\beta\in\mathbb Z_{\ge0}^n\), the sampling law gives
\[
\begin{aligned}
&\mathbb E\left[\prod_{i=1}^n A_i^{\alpha_i}B_i^{\beta_i}\right]\\
&=\frac1{n(n-1)}\sum_{k\ne\ell}\frac{\mathbb E_{V,Z}\left[U^{\alpha_k}V^{\sum_{i\ne k}\alpha_i}H_{\beta_k}(V)\prod_{j\ne k}H_{\beta_j}(U)\right]}{\prod_{i\notin\{k,\ell\}}(\alpha_i+1)}.
\end{aligned}
\]
The expectation is a finite polynomial beta integral: expand \(U=V+(1-V)Z\), then use
\[
\mathbb E[V^p(1-V)^q Z^r(1-Z)^s]
=\frac{\operatorname B(n-1+p,n+2+q)}{\operatorname B(n-1,n+2)}\,
\frac{\operatorname B(1+r,n+s)}{\operatorname B(1,n)}
\]
for nonnegative integers \(p,q,r,s\). Hence each moment is a computable rational number, without an unquantified integration or numerical limit.

**3. First and second moments.** Conditional averaging, together with the beta moments above, gives
\[
\begin{aligned}
\mu_n:=\mathbb E[A_i]&=\frac{(n+2)(n^2+1)}{2n(n+1)(2n+1)}, &\mathbb E[B_i]&=1-\mu_n,\\
S_n:=\operatorname{Var}(A_i)&=\frac{n^6+6n^5+10n^4+18n^3+13n^2-12}{12n^2(n+1)^2(2n+1)^2},\\
C_n:=\operatorname{Cov}(A_i,A_j)&=\frac{(n-2)(n^4+4n^3+9n^2+6n+4)}{8n^2(n+1)^2(2n+1)^2}\quad (i\ne j),\\
M_n:=\operatorname{Cov}(A_i,B_i)&=\frac{(n-2)(n-1)(n+2)(n^2+2n+2)}{8n^2(n+1)^2(2n+1)^2},\\
N_n:=\operatorname{Cov}(A_i,B_j)&=\frac{n^5+3n^4+5n^3+14n^2+8n+8}{8n^2(n+1)^2(2n+1)^2}\quad (i\ne j).
\end{aligned}
\]
The coordinate complementation \((a,b)\mapsto(1-b,1-a)\) preserves the body and interchanges the two levels, so \(\operatorname{Var}(B_i)=S_n\) and \(\operatorname{Cov}(B_i,B_j)=C_n\) for distinct indices. For reproducibility, the intermediate beta expectations can be taken as
\[
\begin{aligned}
\mathbb E V&=\frac{n-1}{2n+1},&\mathbb E V^2&=\frac{n(n-1)}{2(n+1)(2n+1)},\\
\mathbb E U&=\frac{n^2+n+1}{(n+1)(2n+1)},&\mathbb E U^2&=\frac{n^2+n+2}{2(n+1)(2n+1)},\\
\mathbb E UV&=\frac{(n-1)(n^2+2n+2)}{2(n+1)^2(2n+1)}.
\end{aligned}
\]
For example, the conditional index averaging gives, for distinct \(i,j\),
\[
\begin{aligned}
\mathbb E A_i^2&=\mathbb E\left[\frac{U^2+(n+1)V^2/3}{n}\right],\\
\mathbb E A_iA_j&=\mathbb E\left[\frac{UV}{n-1}+\frac{(n+1)(n-2)V^2}{4n(n-1)}\right],\\
\mathbb E A_iB_i&=\mathbb E\left[\frac{U(1+V)}{2n}+\frac{V(1+U)}4\right],\\
\mathbb E A_iB_j&=\mathbb E\left[\frac{V(1+V)}{4(n-1)}+\frac{U(1+U)}{2n}+\frac{(n-2)V(1+U)}{4(n-1)}\right].
\end{aligned}
\]
These and the five beta expectations suffice to reproduce every displayed covariance entry by subtracting the appropriate product of coordinate means.

**4. Exact diagonalization, strict signs and asymptotics.** With \(I_n\) the identity and \(J_n\) the all-ones matrix, the covariance has block form
\[
\Sigma_n=\begin{pmatrix}(S_n-C_n)I_n+C_nJ_n&(M_n-N_n)I_n+N_nJ_n\\(M_n-N_n)I_n+N_nJ_n&(S_n-C_n)I_n+C_nJ_n\end{pmatrix}.
\]
On the constant line and its orthogonal complement in each level, and on the symmetric/antisymmetric level combinations, its eigenvalues are respectively
\[
S_n+(n-1)C_n\pm[M_n+(n-1)N_n],\qquad
S_n-C_n\pm(M_n-N_n).
\]
Direct common-denominator simplification yields the four rational expressions in the Finding. Every numerator is positive for \(n\ge2\). The formulas for \(C_n,M_n,N_n\) show the claimed strict positivity for \(n\ge3\) and the \(n=2\) exceptions; subtracting \(M_n\) from \(N_n\) gives the strict gap. Since \(\lambda_{0,+}\equiv1/12\), whereas the other three eigenvalues converge to \(1/48\), the geometric mean of all \(2n\) eigenvalues tends to \(1/48\). Also \(\operatorname{Vol}(P_n)=[(n+1)/n]\binom{2n}{n}^{-1}\) implies \(\operatorname{Vol}(P_n)^{-1/n}\to4\). Their product is the asserted isotropic limit.

## Verification
The accompanying standalone `checker.py` performs an independent exact-rational verification against the canonical ordered-simplex triangulation, rather than using the beta sampler. For each \(n\in\{2,3,4\}\), it enumerates all permutations of \(2n\) coordinate labels, retains those respecting the standard-example relations, computes order-statistic moments directly, and checks volume, centroids, all four covariance orbit types, symmetry, and the four spectral formulas. There are respectively \(6,48,720\) valid simplices, totaling \(774\). Run `python3 checker.py` with Python 3; success prints `STANDARD_EXAMPLE_EXACT_CHECKS_PASSED 774 3`. These finite checks do not prove the formulas for all \(n\); that proof is the preceding beta disintegration and algebra.

## Relationship to prior work
Reilly, Scheinerman, and Zhang (2014, Proposition 14) already counted the linear extensions of this **same standard-example poset**, yielding the identical volume formula. Neither that count nor the known canonical order-polytope triangulation is asserted as new. Von Bell and collaborators (arXiv:2102.11306, 2021) study the triangulations and volumes of generalized snake order polytopes; their theorems concern a different poset family and do not supply this covariance spectrum. Chan and Pak (arXiv:2212.11954, 2022) establish broad discrete \(P\)-partition correlation inequalities, not the present exact continuous-volume covariance eigenvalues or beta sampler. The cyclic crown poset ordinarily has only two upper neighbors per lower vertex, whereas the standard example has \(n-1\), so they coincide only in the six-element case and should not be conflated.

## Limitations
The theorem treats only the standard-example family and canonical coordinates. The beta factors yield exact moments but do not imply identical laws under arbitrary affine transformations. The positive-covariance sign itself is compatible with general positive-association phenomena for order-preserving constraints; the intended novelty is the complete **evaluated spectrum**, the **factorized sampler**, and the **exact unmatched-minus-matched gap**. A search of accessible sources does not certify historical uniqueness, and a still-unseen equivalent calculation remains possible. No independent mathematical audit has been performed.

## References
1. E. Reilly, E. Scheinerman and Y. Zhang, *Random Threshold Digraphs*, Electronic Journal of Combinatorics **21** (2014), P2.48, Proposition 14, https://doi.org/10.37236/4050 (already proves volume for this poset).
2. M. von Bell et al., *Triangulations, order polytopes, and generalized snake posets*, arXiv:2102.11306 (first public version 2021-02-22), https://arxiv.org/abs/2102.11306.
3. S. H. Chan and I. Pak, *Multivariate correlation inequalities for P-partitions*, arXiv:2212.11954 (first public version 2022-12-22), https://arxiv.org/abs/2212.11954.
4. T. Lundström and L. Saud Maia Leite, *Order polytopes of crown posets*, European Journal of Combinatorics **133** (2026), 104304, https://doi.org/10.1016/j.ejc.2025.104304 (a different family when \(n\ge4\)).
