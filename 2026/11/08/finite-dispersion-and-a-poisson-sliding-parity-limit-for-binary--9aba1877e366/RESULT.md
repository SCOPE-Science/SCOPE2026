# Finite dispersion and a Poisson sliding-parity limit for binary burst-deletion spheres

## Finding
Let \(n\ge 2\) and \(1\le b\le n\). From a binary word \(x=x_0\cdots x_{n-1}\), delete exactly one contiguous block of \(b\) symbols, at any permitted starting position. Write \(B_b(x)\) for the number of **distinct** length-\(n-b\) outputs, counting repeated deletion histories only once.

Let \(X_0\) be an arbitrary binary random variable independent of i.i.d. flips \(\xi_1,\ldots,\xi_{n-1}\sim\operatorname{Bernoulli}(p)\), with \(X_j=X_{j-1}\oplus\xi_j\). Set \(N=n-b\) and \(a=1-2p\). Then, for every \(0\le p\le1\),
\[
\mathbb E B_b(X)=1+\frac N2(1-a^b),
\]
\[
\operatorname{Var}(B_b(X))=\frac N4(1-a^{2b})+\frac12\sum_{h=1}^{\min(b-1,N-1)}(N-h)(a^{2h}-a^{2b}),
\]
where an empty sum is zero. These formulas do not depend on the initial bit's distribution.

There is a non-Gaussian sparse-transition, macroscopic-burst limit. Fix \(\lambda>0\), \(0<\alpha<1\), and let \(p_n=\lambda/n\) and \(1\le b_n\le n\) with \(b_n/n\to\alpha\) (restrict to sufficiently large \(n\) so \(p_n\le1\)). Let \(\Pi\) be a rate-\(\lambda\) Poisson point process on \((0,1)\), \(T=1-\alpha\), and \(K=|\Pi|\). Then
\[
\frac{B_{b_n}(X)-1}{n}\ \xrightarrow{\ d\ }\ L_{\alpha,\lambda}:=\int_0^T\mathbf1\{\Pi((t,t+\alpha])\text{ is odd}\}\,dt.
\]
Equivalently, writing the random points as \(U_1,\ldots,U_K\),
\[
L_{\alpha,\lambda}=\operatorname{Leb}\Bigl(\mathop{\triangle}_{j=1}^{K}\bigl((U_j-\alpha,U_j]\cap[0,T]\bigr)\Bigr),
\]
where \(\triangle\) is symmetric difference and the symmetric difference of an empty collection is empty. Its mean and variance are exactly
\[
\mathbb E L_{\alpha,\lambda}=\frac T2(1-e^{-2\lambda\alpha}),
\qquad
\operatorname{Var}(L_{\alpha,\lambda})=\frac12\int_0^d(T-u)(e^{-4\lambda u}-e^{-4\lambda\alpha})\,du,
\]
with \(d=\min(\alpha,T)\). The variance integral can be evaluated using \(c=4\lambda\) as
\[
\frac12\left[\frac{T(1-e^{-cd})}{c}-\frac{1-(1+cd)e^{-cd}}{c^2}-e^{-c\alpha}\left(Td-\frac{d^2}{2}\right)\right].
\]
In particular the limit is nondegenerate and not Gaussian: \(\Pr(L_{\alpha,\lambda}=0)\ge e^{-\lambda}>0\), while \(\Pr(L_{\alpha,\lambda}>0)\ge\lambda e^{-\lambda}>0\). More precisely, conditional on \(K=1\), its law has density \(2\) on \((0,d)\) and an atom of mass \(|1-2\alpha|\) at \(d\) (when \(\alpha=1/2\), the atom has mass zero).

## Assumptions and scope
All words are binary and linear, not circular. Exactly one block of fixed length \(b\) is removed; deletion positions range from \(0\) through \(n-b\). The source is the symmetric two-state flip chain with independent edge flips, but its starting bit need not be stationary. The finite formulas are exact for all \(n\ge2\), \(1\le b\le n\), and \(p\in[0,1]\). The limit assumes \(\lambda>0\), \(0<\alpha<1\), and \(p_n=\lambda/n\), with no restriction on the starting-bit law.

## Proof
**1. Deterministic deletion-history identity.** For each starting position \(i\in\{0,\ldots,n-b\}\), let \(D_i=x_0\cdots x_{i-1}x_{i+b}\cdots x_{n-1}\) be the resulting word. Direct comparison of the common prefix and suffix shows that for \(i<j\),
\[
D_i=D_j\quad\Longleftrightarrow\quad x_t=x_{t+b}\text{ for every }i\le t<j.
\]
In particular, the list \(D_0,D_1,\ldots,D_{n-b}\) can revisit a word only within a consecutive constant block of this list. Therefore
\[
B_b(x)=1+\sum_{i=0}^{n-b-1}\mathbf1\{x_i\ne x_{i+b}\}.
\]
This is a cardinality identity, not just a count of distinct adjacent pairs.

**2. Exact finite moments.** Write \(\eta_j=(-1)^{\xi_j}\), so \(\mathbb E\eta_j=a\). Let \(Z_i=\prod_{j=i+1}^{i+b}\eta_j\), and \(I_i=(1-Z_i)/2\). The deterministic identity gives \(B_b(X)=1+\sum_{i=0}^{N-1}I_i\). Independence of flips yields \(\mathbb EZ_i=a^b\), \(\mathbb EZ_iZ_{i+h}=a^{2h}\) for \(1\le h<b\), and \(\mathbb EZ_iZ_{i+h}=a^{2b}\) for \(h\ge b\). Thus
\[
\operatorname{Var}(I_i)=\frac14(1-a^{2b}),\quad
\operatorname{Cov}(I_i,I_{i+h})=\begin{cases}\frac14(a^{2h}-a^{2b}),&1\le h<b,\\0,&h\ge b.\end{cases}
\]
Summing the \(N\) variances and the \(N-h\) covariances for each lag gives the two stated moment formulas. The \(N=0\) case reduces to the deterministic value \(B_b=1\).

**3. Sparse-transition point-process convergence.** Place a point at \(j/n\) whenever \(\xi_j=1\), for \(1\le j<n\). Their counting measure \(\Pi_n\) converges in distribution to a homogeneous Poisson process of rate \(\lambda\) on \((0,1)\): disjoint interval counts are independent binomials with rare-event means converging to their interval lengths times \(\lambda\). The parity identity rewrites the normalized deletion-sphere size as
\[
\frac{B_{b_n}(X)-1}{n}=\frac1n\sum_{i=0}^{n-b_n-1}\mathbf1\{\Pi_n((i/n,(i+b_n)/n])\text{ is odd}\}.
\]
Conditional on any fixed finite number of distinct, interior points, the sum is a Riemann approximation to the displayed integral for \(L_{\alpha,\lambda}\): the parity integrand changes only when the left or right endpoint of a moving window meets one of the points. With \(K\) points, at most \(2K\) jump locations occur, so the mesh discrepancy vanishes; changing the window length by \(|b_n/n-\alpha|\) changes the integral by at most \(K|b_n/n-\alpha|\), up to a vanishing endpoint term. Tightness of the number of points and absence of Poisson atoms at fixed boundaries justify the mapping theorem. This proves convergence in distribution. The same parity is odd exactly on the symmetric difference of the displayed intervals, proving that representation.

**4. Limiting moments and non-Gaussianity.** For a Poisson interval of length \(\alpha\), the expected sign \((-1)^{\Pi}\) equals \(e^{-2\lambda\alpha}\). Two windows shifted by \(u\) have symmetric difference of length \(2\min(u,\alpha)\), so their parity-indicator covariance is \(\frac14(e^{-4\lambda\min(u,\alpha)}-e^{-4\lambda\alpha})\), zero for \(u\ge\alpha\). Integration over the square \([0,T]^2\), grouping pairs by \(|t-s|\), gives the stated variance. Elementary integration gives the closed form. The random variable is bounded by \(T\), so weak convergence also implies convergence of its first two moments.

With no Poisson points, \(L=0\). With one point \(U\), \(L=\operatorname{Leb}((U-\alpha,U]\cap[0,T])>0\) almost surely. Given \(K=1\), \(U\) is uniform on \((0,1)\); this intersection length increases linearly from \(0\) to \(d\), stays at \(d\) for an interval of length \(|1-2\alpha|\), then decreases linearly to \(0\). Hence its conditional density is \(2\) on \((0,d)\), plus the stated possible atom. This establishes nondegeneracy and excludes a normal law.

## Verification
The standalone `checker.py` uses independent deletion-output enumeration and exact rational probabilities. It verifies the cardinality identity for all \(8192\) binary source/burst instances with \(2\le n\le9\). It separately enumerates flip histories for three rational transition probabilities across \(132\) parameter combinations and reproduces the mean and variance formulas exactly. Numerical asymptotic sanity checks at \((\alpha,\lambda)=(0.4,1.7)\) and \((0.7,2)\) were consistent with the limiting moment integrals. These are finite checks and not substitutes for the general proof.

## Relationship to prior work
Ye and Ge's October 2026 work introduces improved codes for bounded substring edits and burst deletions; those are construction and redundancy questions, not the sparse-transition source law claimed here. Classical burst-deletion literature supplies the channel setting, while Lu and Zhang study the different operation of deleting a block and inserting symbols. The established telegraph-process literature studies single-time occupation functionals; the present limit uses **lagged two-time parity** of a Poisson flip process. Published results on covariance for overlapping corrupted windows offer related techniques, but do not by their stated parameters imply this deletion-ball law. These comparisons identify the intended increment, not an assertion of absolute historical priority.

## Limitations
Only the symmetric binary flip chain is analyzed; no non-symmetric or higher-alphabet Markov theorem is claimed. The burst length must be exactly specified and its asymptotic fraction must lie strictly between zero and one. The limiting distribution is given as a Poisson functional and a conditional one-point component, not a full elementary closed-form density for every Poisson count. The result does not construct optimal error-correcting codes or give capacities. Historical originality is assessed against accessible literature; independent scientific validation has not been carried out.

## References
- Z. Ye and G. Ge, *Substring Edit Correcting Codes and Optimal Single Burst-Deletion Correcting Codes*, arXiv:2610.05696, initial public posting 5 October 2026. https://arxiv.org/abs/2610.05696
- Z. Lu and Y. Zhang, *t-Deletion-s-Insertion-Burst Correcting Codes*, arXiv:2201.10259, initial public posting 25 January 2022. https://arxiv.org/abs/2201.10259
- L. Bogachev and N. Ratanov, *Occupation time distributions for the telegraph process*, Stochastic Processes and their Applications 121 (2011), 1816–1844. https://eprints.whiterose.ac.uk/id/eprint/74927/
