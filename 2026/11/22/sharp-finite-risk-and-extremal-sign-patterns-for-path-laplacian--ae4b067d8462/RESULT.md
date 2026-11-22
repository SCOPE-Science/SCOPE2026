# Sharp finite risk and extremal sign patterns for path-Laplacian trace probes

## Finding
For every integer \(n\ge2\), let \(L_n\) be the unweighted path \(P_n\)'s combinatorial graph Laplacian, let \(B_n=L_n^\dagger\) denote its Moore–Penrose pseudoinverse, and let \(z\) have independent symmetric Rademacher coordinates. Write \(Z_n=z^\mathsf{T}B_nz\). Then
\[
\mathbb E Z_n=\frac{n^2-1}{6},\qquad
\operatorname{Var}(Z_n)=\frac{(n^2-1)(2n^3-6n^2+7n+9)}{90n}.
\]
The exact relative variance is
\[
\frac{\operatorname{Var}(Z_n)}{(\mathbb EZ_n)^2}
=\frac{2(2n^3-6n^2+7n+9)}{5n(n^2-1)}\longrightarrow\frac45.
\]
More strongly, every deterministic sign vector obeys the **sharp** range
\[
0\le z^\mathsf{T}B_nz\le M_n,
\quad M_n=\begin{cases}
\frac{n(n^2+2)}{12},&n\text{ even},\\
\frac{n^4-1}{12n},&n\text{ odd}.
\end{cases}
\]
Zero occurs only for the two constant sign vectors. The maximum occurs **only** at sign vectors with exactly one sign switch and two block lengths differing by at most one (two such vectors for even \(n\), four for odd \(n\)). Finally, with \(\beta\) a standard Brownian bridge,
\[
 n^{-2}Z_n\ \xrightarrow{\mathrm d}\ \int_0^1\beta(t)^2\,dt
 \ \overset{\mathrm d}=\ \sum_{j=1}^\infty\frac{\xi_j^2}{\pi^2j^2},
\]
where \(\xi_j\) are independent standard Gaussian variables. For \(m\ge1\) independent probes, averaging divides the displayed variance by \(m\); the large-\(n\) relative mean-square error is therefore \(4/(5m)\). These are connected statements about the same finite-path Rademacher trace-probe law.

## Assumptions and scope
The path has vertices \(1,\ldots,n\), unit edge conductances, and no boundary pinning. The Laplacian is the degree-minus-adjacency matrix with a single zero eigenvalue. Its pseudoinverse acts as the inverse on the mean-zero vertex subspace and vanishes on the constant vector. All coordinates of \(z\) are mutually independent and take \(\pm1\) with probability \(1/2\). Every moment and sharp-extremum statement holds for each finite \(n\ge2\), including both parities. The weak limit concerns \(n\to\infty\) with one fresh probe for each \(n\); it is not a finite-sample Gaussian approximation claim.

## Proof
**1. Electrical flow identity.** Orient path edges from \(j\) to \(j+1\) and write \(S_j=\sum_{i=1}^jz_i\). The projection \(b=z-(S_n/n)\mathbf1\) is mean zero, and its unique cumulative unit-resistance edge flow is \(f_j=S_j-jS_n/n\) (a global orientation sign is irrelevant). The path Laplacian energy identity gives
\[
 Z_n=b^\mathsf{T}L_n^\dagger b
 =\sum_{j=1}^{n-1}\left(S_j-\frac jn S_n\right)^2.\tag{1}
\]
Consequently \(Z_n=0\) precisely when each \(z_i=S_n/n\), i.e. the two constant sign vectors.

**2. Exact mean and variance.** Let \(H\) be the \((n-1)\)-by-\(n\) matrix with \(H_{ji}=\mathbf1_{\{i\le j\}}-j/n\). Identity (1) says \(B_n=H^\mathsf{T}H\). The covariance kernel of the centered partial sums is
\[
 (HH^\mathsf{T})_{jk}=\min(j,k)-\frac{jk}{n}.
\]
Elementary finite summation yields, with all terms displayed to fix normalization,
\[
\begin{aligned}
\operatorname{tr}B_n &=\sum_{j=1}^{n-1}\frac{j(n-j)}n=\frac{n^2-1}{6},\\
\operatorname{tr}(B_n^2)&=\sum_{j,k=1}^{n-1}\left(\min(j,k)-\frac{jk}{n}\right)^2
=\frac{(n^2-1)(2n^2+7)}{180},\\
(B_n)_{ii}&=\frac{(i-(n+1)/2)^2}{n}+\frac{n^2-1}{12n},\\
\sum_{i=1}^n(B_n)_{ii}^2&=\frac{(n^2-1)(2n^2-3)}{60n}.
\end{aligned}
\]
Independence and fourth moments of symmetric signs give \(\operatorname{Var}(z^\mathsf{T}B_nz)=4\sum_{i<j}(B_n)_{ij}^2=2\{\operatorname{tr}B_n^2-\sum_i(B_n)_{ii}^2\}\). Substitution proves the variance formula and relative-variance limit.

**3. A sharp all-sign maximum.** Fix the number \(k\) of positive coordinates with \(1\le k\le n-1\), list their locations as \(1\le i_1<\cdots<i_k\le n\), and denote their indicator vector by \(a\). Since \(z=2a-\mathbf1\) and \(B_n\mathbf1=0\), \(Z_n=4a^\mathsf{T}B_na\). The unit path has effective resistance \(R_{ij}=|i-j|\); double-centering its resistance matrix recovers \(B_n\). With
\[
\overline R_i=\frac1n\sum_{h=1}^n|i-h|
=\frac{(i-(n+1)/2)^2+(n^2-1)/4}{n},\qquad
\overline{\overline R}=\frac{n^2-1}{3n},
\]
we obtain
\[
 a^\mathsf{T}B_na
=k\sum_{j=1}^k\overline R_{i_j}
 -\sum_{1\le j<\ell\le k}(i_\ell-i_j)
 -\frac{k^2}2\overline{\overline R}.\tag{2}
\]
On the real order polytope \(1\le i_1\), \(i_{j+1}\ge i_j+1\), \(i_k\le n\), expression (2) is **strictly convex**, with positive quadratic coefficient \(k/n\) in each location. It therefore attains its maximum only at polytope vertices. Under \(y_j=i_j-j\), the polytope is \(0\le y_1\le\cdots\le y_k\le n-k\); its vertices have a prefix at zero and a suffix at \(n-k\). Thus maximizers can only have plus signs on a prefix of size \(p\) and a suffix of size \(q\), separated by \(r=n-k\) minus signs. Let \(p+q=k\). Directly summing (1) for these vertices gives
\[
 Z_{p,r,q}
 =\frac{2kr(2kr+1)}{3n}-\frac{4pqr^2}{n}.\tag{3}
\]
The last term is strictly negative whenever both end blocks are nonempty, so the maximum for fixed \(k\) is attained only at single-switch signs. With \(h=k(n-k)\), their energy is \(2h(2h+1)/(3n)\), strictly increasing in \(h\ge0\). The only maximizing block sizes are \(k=\lfloor n/2\rfloor\) or \(\lceil n/2\rceil\). Evaluating this expression proves both parity formulas and the exact equality classification. No finite enumeration is used to prove this infinite family.

**4. Distributional limit.** Donsker's invariance principle gives weak convergence of the centered, linearly interpolated partial-sum process
\[
 t\mapsto n^{-1/2}\left(S_{\lfloor nt\rfloor}-\frac{\lfloor nt\rfloor}{n}S_n\right)
\]
to standard Brownian bridge in the uniform topology (after piecewise-linear interpolation). Equation (1) makes \(n^{-2}Z_n\) the corresponding Riemann sum of squares. The continuous mapping theorem and convergence of these sums give the integral limit. The displayed Gaussian-series law is the classical Karhunen–Loève expansion of a Brownian bridge; neither that expansion nor Donsker's principle is asserted as a new result.

## Verification
Run `python verify.py` using Python 3.10 or later; it uses only the standard library. It constructs the exact rational path Green matrix, independently checks its trace, variance, every \(2^n\) sign energy, sharp extrema and their unique sign patterns for \(2\le n\le11\), and checks identity (3) in every integer configuration in those sizes. The 4092 enumerated sign configurations are finite diagnostics, not a proof for arbitrary \(n\). Equations (1)–(3) and the stated probabilistic convergence provide the analytic proof.

## Relationship to prior work
Hallman–Troester [1] give the standard Hutchinson estimator and general multilevel variance/concentration analysis; Chen–Hallman [2] develop Krylov-aware matrix-function trace estimation. Lu–Xu–Zhang [3] study pseudoinverse diagonals and Kirchhoff-index estimation in general graphs; van Mieghem–Devriendt–Cetinay [4] present path-Laplacian pseudoinverse formulas (Appendix C). These prior results provide tools and context but the inspected material does not give the combined **exact finite-path sign-probe variance and sharp extremizing sign-vector theorem**. The generic Rademacher variance formula, resistance double-centering, bridge limit, and classical sign-step rearrangement ideas are not claimed new individually. Exact equivalence to an older discrete Sobolev/rearrangement inequality remains a real literature-priority risk.

## Limitations
The result concerns a single unnormalized Rademacher quadratic form of the combinatorial path pseudoinverse, not normalized Laplacians, general graphs, or Lanczos/Krylov truncation error. Its exact mean and variance do not by themselves establish optimal confidence intervals. The sharp maximum is a worst-case event, potentially exponentially rare, and is not a typical-sample performance prediction. The Brownian-bridge distribution is classical. An exhaustive equivalence search across historical discrete rearrangement inequalities and numerical trace estimation is not claimed, and independent verification has not been performed.

## References
[1] E. Hallman and D. Troester, *A Multilevel Approach to Stochastic Trace Estimation*, arXiv:2103.10516, first posted 2021-03-18, https://arxiv.org/abs/2103.10516.

[2] T. Chen and E. Hallman, *Krylov-aware stochastic trace estimation*, arXiv:2205.01736, first posted 2022-05-03, https://arxiv.org/abs/2205.01736.

[3] Z. Lu, W. Xu, and Z. Zhang, *Diagonal of Pseudoinverse of Graph Laplacian: Fast Estimation and Exact Results*, arXiv:2310.05527, first posted 2023-10-09, https://arxiv.org/abs/2310.05527.

[4] P. Van Mieghem, K. Devriendt, and H. Cetinay, *Pseudoinverse of the Laplacian and best spreader node in a network*, Physical Review E 96, 032311 (2017), https://doi.org/10.1103/PhysRevE.96.032311.
