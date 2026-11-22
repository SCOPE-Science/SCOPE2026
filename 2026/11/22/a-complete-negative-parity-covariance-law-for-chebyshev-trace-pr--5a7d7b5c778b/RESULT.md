# A complete negative-parity covariance law for Chebyshev trace probes on finite paths

## Finding
Let \(n\ge2\), let \(A_n\) be one half of the ordinary adjacency matrix of the \(n\)-vertex path, and let \(z\in\{-1,+1\}^n\) have independent uniform coordinates. For the first-kind Chebyshev polynomials \(T_j\), set \(Z_j=z^{\mathsf T}T_j(A_n)z\). For all integers \(1\le j,k\le n\), the **entire exact covariance matrix** is
\[
\operatorname{Cov}(Z_j,Z_k)=
\begin{cases}
 n-1,&j=k\text{ and }j\text{ odd},\\
 n-2,&j=k\text{ and }j\text{ even},\\
 -2,&j\ne k\text{ and }j\equiv k\pmod2,\\
 0,&j\not\equiv k\pmod2.
\end{cases}
\]
In particular, every pair of distinct degrees of the same parity is **negatively correlated**, not independent. The covariance spectrum is exactly one zero eigenvalue, one eigenvalue \(1\), \(\lfloor n/2\rfloor-1\) eigenvalues \(n\), and \(\lceil n/2\rceil-1\) eigenvalues \(n+1\), omitting classes with zero multiplicity.

For arbitrary real coefficients \(c_1,\ldots,c_n\), this yields the complete single-probe trace-risk identity
\[
\operatorname{Var}\!\left(\sum_{j=1}^n c_j Z_j\right)
=(n+1)\sum_{j\,\mathrm{odd}}c_j^2+n\sum_{j\,\mathrm{even}}c_j^2
-2\left[\left(\sum_{j\,\mathrm{odd}}c_j\right)^2+\left(\sum_{j\,\mathrm{even}}c_j\right)^2\right].
\]
Both sums range only over \(1\le j\le n\). The one-dimensional nullspace corresponds exactly to
\[
\sum_{1\le j\le n,\ j\equiv n\ (\mathrm{mod}\ 2)} T_j(A_n)
=\begin{cases}0,&n\text{ odd},\\-\tfrac12 I_n,&n\text{ even}.\end{cases}
\]
The zero variance follows from a full matrix identity, not merely a numerical coincidence.

## Assumptions and scope
The graph has vertices \(1,\ldots,n\) and undirected unit edges only between consecutive vertices. Precisely, \((A_n)_{ab}=1/2\) when \(|a-b|=1\) and is zero otherwise. This is **half-adjacency**, not the random-walk degree-normalized adjacency (which differs at endpoints). The sample signs are independent and unbiased; all \(Z_j\) reuse the *same* sample vector. The degree window is \(1\le j\le n\); no claim is made for higher degrees, other graphs, non-Rademacher probes, or independent probes used separately for each degree.

## Proof
**1. Exact reflected kernel.** Put \(N=n+1\). For \(1\le s\le n\) let \(\theta_s=s\pi/N\). The normalized discrete-sine eigenvectors of \(A_n\) are \(\sqrt{2/N}\sin(a\theta_s)\) and its eigenvalues are \(\cos\theta_s\). Thus for \(1\le m\le n\),
\[
[T_m(A_n)]_{ab}=\frac2N\sum_{s=1}^n\sin(a\theta_s)\sin(b\theta_s)\cos(m\theta_s).
\]
For every integer \(\ell\), the finite trigonometric sum \(\sum_{s=1}^{N-1}\cos(\ell s\pi/N)\) equals \(N-1\) if \(2N\mid\ell\), equals \(-1\) if \(\ell\) is even but \(2N\nmid\ell\), and equals \(0\) if \(\ell\) is odd. Expanding the three-factor sine-cosine product into four cosines, the common background \(-1\) terms cancel. Checking the possible multiples of \(2N\) in the stated ranges yields, for all \(1\le a,b\le n\),
\[
2[T_m(A_n)]_{ab}
=\mathbf1_{|a-b|=m}-\mathbf1_{a+b=m}-\mathbf1_{a+b=2N-m}.
\tag{1}
\]
The three indicators in (1) never overlap for \(m\in\{1,\ldots,n\}\). This identity includes diagonal entries and boundary reflections.

**2. Fourth moments and pair counting.** For any symmetric matrices \(B,C\), independence of the Rademacher coordinates gives
\[
\operatorname{Cov}(z^{\mathsf T}Bz,z^{\mathsf T}Cz)=4\sum_{1\le a<b\le n}B_{ab}C_{ab}.
\tag{2}
\]
For each unordered pair \(a<b\), (1) gives one positive off-diagonal entry at degree \(d=b-a\), and either one negative entry at the strictly larger degree \(h=\min\{a+b,2N-a-b\}\), if \(h\le n\), or no negative entry if \(a+b=N\). Both degrees \(d,h\) have the same parity. The gap \(h-d\) is positive and even.

At degree \(m\), there are exactly \(n-m\) pairs with \(d=m\), and exactly \(2\lfloor(m-1)/2\rfloor\) pairs with \(h=m\). Since every nonzero off-diagonal entry of \(T_m(A_n)\) is \(\pm1/2\), equation (2) proves
\[
\operatorname{Var}(Z_m)=n-m+2\lfloor(m-1)/2\rfloor
=\begin{cases}n-1,&m\text{ odd},\\n-2,&m\text{ even}.\end{cases}
\]
For any distinct same-parity degrees \(j<k\), there are exactly **two** pairs having \(d=j,h=k\):
\[
(a,b)=\left(\frac{k-j}{2},\frac{k+j}{2}\right),\qquad
(a,b)=\left(N-\frac{k+j}{2},N-\frac{k-j}{2}\right).
\]
Their products of entries of the two Chebyshev matrices are both \(-1/4\). Hence the covariance is \(-2\). If the degrees have different parities, no pair contributes to (2), so covariance is zero. This proves the claimed full matrix for every \(n\ge2\).

**3. Spectrum, risk, and nullspace.** Separate odd and even degree indices. The odd block is \((n+1)I-2\mathbf1\mathbf1^{\mathsf T}\) of size \(\lceil n/2\rceil\); the even block is \(nI-2\mathbf1\mathbf1^{\mathsf T}\) of size \(\lfloor n/2\rfloor\). Direct diagonalization gives the stated eigenvalues, including exactly one zero eigenvalue and one eigenvalue \(1\). Expanding the corresponding quadratic form gives the risk formula. If \(n\) is odd, the identity \(\sum_{j=0}^{(n-1)/2}\cos((2j+1)\theta)=\sin((n+1)\theta)/(2\sin\theta)\) vanishes at every \(\theta_s\). If \(n\) is even, \(\sum_{j=1}^{n/2}\cos(2j\theta)=\sin((n+1)\theta)/(2\sin\theta)-1/2\), which equals \(-1/2\) at all eigenangles. Spectral functional calculus proves the matrix identities and exactly identifies the nullspace. \(\square\)

## Verification
The standalone `verify_path_chebyshev_covariance.py` uses integer arithmetic for \(2T_j(A_n)\). It compares all recurrence entries with (1) for \(2\le n\le30\), compares the covariance Gram sums with the formula for all degrees in the same range, and verifies the polynomial matrix identity. For \(2\le n\le8\) it also enumerates **all** Rademacher sign vectors and recomputes every covariance using exact rational arithmetic. Its successful run reports 216224 entry checks, 9454 direct covariance checks, 203 full sign-space covariance enumerations, and 9454 polynomial-identity entry checks. These finite checks are supplementary; the spectral and pair-count proofs above establish the universal result.

## Relationship to prior work
Han–Malioutov–Avron–Shin (2017) develop stochastic Chebyshev approximation for traces of matrix functions; Hallman (2021) reduces matrix-vector cost through a Chebyshev product identity; Hallman–Troester (2021) analyze multilevel Chebyshev trace estimators and their variance/cost allocation. Their inspected results give general algorithms and bounds, not the full path-specific cross-degree covariance matrix or its exact one-dimensional nullspace. Noschese–Pasquini–Reichel (2013) examine tridiagonal Toeplitz spectra and Chebyshev Krylov bases, but do not analyze this stochastic trace covariance. A cyclic half-adjacency model has a different, positive complementary-degree aliasing covariance structure; it does not imply the reflected Dirichlet-path negative-parity law.

## Limitations
The covariance formula concerns the first \(n\) positive Chebyshev degrees only and depends on the precise half-adjacency scaling and shared independent-sign vector. The deterministic null combination is a known type of finite spectral-polynomial identity and is **not by itself** claimed as an independent new algorithm. The result supplies a canonical exact covariance benchmark and possible guidance about reuse of random probes, not a speedup guarantee or a theorem about arbitrary sparse matrices. An older formulation in discrete-sine-transform, Toeplitz-plus-Hankel, or polynomial moment literature could predate the explicit covariance law; publication priority requires external expert confirmation.

## References
1. E. Hallman, *Faster Stochastic Trace Estimation with a Chebyshev Product Identity*, first posted January 1, 2021, arXiv:2101.00325. https://arxiv.org/abs/2101.00325
2. E. Hallman and D. Troester, *A Multilevel Approach to Stochastic Trace Estimation*, first posted March 18, 2021, arXiv:2103.10516. https://arxiv.org/abs/2103.10516
3. I. Han, D. Malioutov, H. Avron, and J. Shin, *Approximating Spectral Sums of Large-scale Matrices using Stochastic Chebyshev Approximations*, arXiv:1606.00942; SIAM Journal on Scientific Computing 39 (2017), A1558–A1585. https://arxiv.org/abs/1606.00942
4. S. Noschese, L. Pasquini, and L. Reichel, *Tridiagonal Toeplitz Matrices: Properties and Novel Applications*, Numerical Linear Algebra with Applications 20 (2013), 302–326. https://doi.org/10.1002/nla.1811
