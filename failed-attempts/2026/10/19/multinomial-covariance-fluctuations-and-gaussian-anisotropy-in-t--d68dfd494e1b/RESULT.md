# Multinomial-covariance fluctuations and Gaussian anisotropy in twisted baker maps

## Finding
Fix an integer \(M\ge3\). For the \(M\)-dimensional twisted baker map of Saiki–Takahasi–Yorke, sample \(x\) from normalized Lebesgue measure. Let \(J_n(x)=D F^n(x)\) outside the null set of branch boundaries, and write its \(M\) singular values, with multiplicities and in arbitrary order, as \(2^{C_0(n)},\ldots,2^{C_{M-1}(n)}\). The integer exponents can be labeled so that their vector has the following *exact finite-time* probability-generating function:
\[
\mathbb E\prod_{r=0}^{M-1}z_r^{C_r(n)}
=e_0^{\mathsf T}\bigl(P\,\operatorname{diag}(z_0,\ldots,z_{M-1})\bigr)^n\mathbf1,
\qquad P_{r,s}=\tfrac12\bigl(\mathbf1_{s=r}+\mathbf1_{s\equiv r+1\ (\mathrm{mod}\ M)}\bigr).
\]
In particular the exponents need **not** have a multinomial law at finite time. Nevertheless they satisfy the exact *multinomial-covariance central limit law*
\[
\frac1{\sqrt n}\left(C(n)-\frac nM\mathbf1\right)
\ \Longrightarrow\ \mathcal N_M\left(0,\;\frac1M I_M-\frac1{M^2}\mathbf1\mathbf1^{\mathsf T}\right).
\]
The covariance is precisely the one arising from \(n\) independent uniform choices among \(M\) coordinates, although the actual coordinate choices are correlated. Consequently, if \(Z_1,\ldots,Z_M\) are independent standard normal variables, then the Euclidean Jacobian condition number satisfies
\[
\boxed{\quad
\frac{\log\kappa_2(J_n)}{(\log2)\sqrt n}
\ \Longrightarrow\ \frac{\max_j Z_j-\min_j Z_j}{\sqrt M}.
\quad}
\]
The mean has the corresponding sharp asymptotic:
\[
\lim_{n\to\infty}\frac{\mathbb E\log\kappa_2(J_n)}{(\log2)\sqrt n}
=\frac{\mathbb E(\max_jZ_j-\min_jZ_j)}{\sqrt M}>0.
\]
For the natural first higher-dimensional case \(M=3\), the right-hand constant is exactly \(\sqrt{3/\pi}\). Thus all asymptotic coordinate Lyapunov growth rates equal \((\log2)/M\), but a typical finite-time iterate retains logarithmic anisotropy of order \(\sqrt n\).

## Assumptions and scope
For \(M\ge3\), take \(X=[-1,1]\times[0,1]^{M-1}\) with its normalized Lebesgue probability measure. The *original* twisted baker map is
\[
F(x_1,\ldots,x_M)=\begin{cases}
(1+2x_1,x_2,\ldots,x_M),&x_1<0,\\
(1-2x_M,x_1,\ldots,x_{M-1}),&x_1\ge0.
\end{cases}
\]
The definition at partition boundaries may be taken from the right branch; the set of points hitting these boundaries has zero Lebesgue measure and does not affect the claim. The derivative uses the ordinary Euclidean inner product; the condition number is the ratio of largest to smallest singular value. The probability laws concern a Lebesgue-random initial point, not a fixed atypical orbit or a random composition of unrelated maps. The center of the Gaussian is \(0\), with the stated singular covariance supported on the hyperplane whose coordinate sum is zero.

## Proof
**1. Binary coding and the monomial derivative.** The source establishes that every prescribed length-\(n\) itinerary of the two branches \(L,R\) has normalized Lebesgue measure \(2^{-n}\) (its property (P4), Section 2.2). Therefore the successive right-branch indicators \(S_1,\ldots,S_n\) are independent Bernoulli variables with probability \(1/2\). The two branch Jacobians are
\[
A_L=\operatorname{diag}(2,1,\ldots,1),\qquad
A_R e_j=\begin{cases}e_{j+1},&j<M,\\-2e_1,&j=M.\end{cases}
\]
These are signed monomial matrices. Put \(R_0=0\) and \(R_j=(S_1+\cdots+S_j)\pmod M\), with residues \(0,\ldots,M-1\). By tracking the column acted on by each factor, the multiset of Euclidean singular values of \(A_{S_n}\cdots A_{S_1}\) equals \(\{2^{C_r(n)}:0\le r<M\}\), where
\[
C_r(n)=\sum_{j=1}^{n}\mathbf1_{\{R_j=r\}},\qquad
\sum_r C_r(n)=n.
\]
The physical input-coordinate labels amount to a fixed cyclic reversal of the residue labels, which leaves all singular values unchanged as a multiset. The residue chain has transition matrix \(P=(I+\mathsf S)/2\), where \(\mathsf S\) cyclically advances one residue. Starting from residue zero, accumulating a variable \(z_r\) on arriving at state \(r\) gives the displayed exact generating function by the elementary transfer-matrix identity.

**2. A bounded-coboundary martingale identity.** Set \(f_i(r)=\mathbf1_{\{r=i\}}-1/M\). Choose a function \(g_i\) on the cyclic residues by \(g_i(0)=0\) and
\[
g_i(r)-g_i(r+1)=2f_i(r),\qquad r\pmod M.
\]
It exists because \(\sum_r f_i(r)=0\). Its oscillation is exactly \(2(M-1)/M\): traversing the cycle, it makes \(M-1\) equal small upward increments and one compensating downward increment. Since \((I-P)g_i=f_i\), and with \(\epsilon_j=1-2S_j\), the exact martingale difference is
\[
\xi_{j,i}:=g_i(R_j)-(Pg_i)(R_{j-1})
=\epsilon_j f_i(R_{j-1}).
\]
Summing \(f_i(R_j)=g_i(R_j)-(Pg_i)(R_j)\) and telescoping yields
\[
C_i(n)-\frac nM
=\sum_{j=1}^{n}\xi_{j,i}+(Pg_i)(R_0)-(Pg_i)(R_n).
\]
In particular, **for every itinerary, every \(n\), and every coordinate \(i\)**, the difference from the displayed martingale sum has absolute value at most \(2(M-1)/M<2\). This is a uniform finite-time control, not merely a distributional approximation.

**3. Conditional covariance and the multivariate CLT.** The vector increments \(\xi_j\) are bounded martingale differences relative to the branch filtration. Their conditional covariance is
\[
\mathbb E[\xi_{j,i}\xi_{j,k}\mid S_1,\ldots,S_{j-1}]
=f_i(R_{j-1})f_k(R_{j-1}).
\]
The finite-state chain \(P\) is irreducible and aperiodic and has the uniform stationary law. Its ergodic theorem gives, almost surely,
\[
\frac1n\sum_{j=1}^{n}f_i(R_{j-1})f_k(R_{j-1})
\longrightarrow\frac1M\sum_{r=0}^{M-1}f_i(r)f_k(r)
=\frac{\mathbf1_{i=k}}M-\frac1{M^2}.
\]
The bounded-increment martingale central limit theorem (or its Cramér–Wold scalar form) now yields the stated centered Gaussian vector limit for the martingale. The uniformly bounded endpoint terms vanish upon division by \(\sqrt n\). This proves the complete covariance statement. Since \(\log\kappa_2(J_n)/(\log2)=\max_r C_r(n)-\min_r C_r(n)\), continuity of the range functional gives the Gaussian-range limit. A Gaussian vector with the displayed covariance has the same law as \(((Z_i-\overline Z)/\sqrt M)_{i=1}^M\), and its range is exactly \((\max Z_i-\min Z_i)/\sqrt M\).

**4. Convergence of the mean and the three-dimensional coefficient.** Martingale orthogonality and bounded differences give \(\mathbb E\|\sum_{j\le n}\xi_j\|_2^2=n(1-1/M)\) exactly: for each residue, \(\sum_i f_i(r)^2=1-1/M\). The endpoint error has Euclidean norm bounded by \(2\sqrt M\). The range of a vector is at most twice its Euclidean norm after centering. Consequently the normalized ranges have bounded second moments and hence are uniformly integrable; their expectations converge to the expectation of the Gaussian range. For three independent standard normals, symmetry and a one-variable Gaussian integration give \(\mathbb E\max(Z_1,Z_2,Z_3)=3/(2\sqrt\pi)\). Therefore \(\mathbb E(\max Z_i-\min Z_i)/\sqrt3=\sqrt{3/\pi}\).

## Verification
Run `python verify_twisted.py` with Python 3 and the standard library. The checker reconstructs the literal branch derivative matrices, enumerates all binary words of lengths \(1\) through \(8\) for dimensions \(2\) through \(6\), and compares the squared column norms to the predicted exact powers of four. It independently verifies the cyclic Poisson equation and the martingale endpoint identity using exact rational arithmetic, the exact transition generating-function distribution through dynamic programming, and the exact covariance identity for dimensions \(2\) through \(8\). It prints `VERIFY_OK` only when every assertion succeeds. These finite checks support, but do not replace, the infinite-time martingale proof.

As a quick nontrivial contrast with a multinomial finite law, for \(M=3,n=2\) the generating polynomial is
\[
\frac14\bigl(z_0^2+z_0z_1+z_1^2+z_1z_2\bigr),
\]
whereas two independent uniform coordinate choices would give \((z_0+z_1+z_2)^2/9\). The matching covariance is **asymptotic**, not an assertion of finite-time independence.

## Relationship to prior work
Saiki, Takahasi and Yorke introduced the twisted baker map and proved the branch-word coding, mixing and dense real/nonreal periodic spectra; they also observed itinerary-dependent geometric distortion and nonuniform expansion on periodic points. Those results supply the Bernoulli coding used here, but do not specify the distribution of finite-time Euclidean singular-value exponents, an exact martingale decomposition, their Gaussian covariance, or the limiting condition-number range law.

A subsequent public note, *Exact real-spectrum residue law for the twisted baker map*, gives a complete residue criterion and exact counts for **eigenvalues at periodic points**. That concerns complex-versus-real algebraic eigenvalue spectra and does not yield the above **singular values on Lebesgue-typical nonperiodic trajectories**, particularly not the higher-dimensional Gaussian range. The planar periodic-return multiplier distribution is likewise a different statistic; the present theorem is stated for \(M\ge3\) to make the new higher-dimensional fluctuation explicit. General finite-state Markov additive-functional central limit theorems are established tools; the substantive calculation here is the special, exact multinomial covariance and its transfer to the twisted-baker singular-value cocycle.

## Limitations
The theorem is for each fixed integer dimension \(M\ge3\), not a simultaneous growing-dimension limit. It is measure-theoretic and says nothing about a deterministic orbit on a branch boundary, the law under a singular invariant measure, finite-time independence of coordinate exponents, or eigenvalue distributions of typical nonperiodic iterates. The central limit law is an asymptotic distribution rather than a uniform error bound, and it does not claim that the condition number grows deterministically at rate \(\exp(c\sqrt n)\) along every orbit. Source searching cannot exclude a differently named earlier application of the general finite-state Markov CLT to this exact singular-value cocycle.

## References
1. Y. Saiki, H. Takahasi and J. A. Yorke, *The twisted baker map*, arXiv:2202.04304, first publicly posted 9 February 2022; *Nonlinearity* **36** (2023), 1776–1788, DOI: 10.1088/1361-6544/acb4d3. In particular the defining map, Section 2.1 on derivatives, Section 2.2 property (P4), and Sections 3.2–3.3 on distortion and Bernoulli coding.
2. *Exact real-spectrum residue law for the twisted baker map*, public mathematical research note, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-real-spectrum-residue-law-for-the-twisted-baker-map--f1bd1c74fb3b/RESULT.md . This note concerns periodic **eigenvalues**, not finite-time singular values.
3. P. Hall and C. C. Heyde, *Martingale Limit Theory and Its Application*, Academic Press, 1980 (standard bounded-martingale central limit theorem).
