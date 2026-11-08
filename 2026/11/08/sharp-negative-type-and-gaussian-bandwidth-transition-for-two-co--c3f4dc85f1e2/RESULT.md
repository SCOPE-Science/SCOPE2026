# Sharp negative type and Gaussian bandwidth transition for two-column rank metrics

## Finding
Let \(q\ge2\) be a prime power, \(m\ge2\) an integer, and \(V=M_{m,2}(\mathbb F_q)\) with rank distance \(d(X,Y)=\operatorname{rank}_{\mathbb F_q}(X-Y)\). Put
\[
\alpha_q=\log_2(1+q^{-1}),\qquad N=q^{2m},\qquad N_1=(q^m-1)(q+1),\qquad N_2=(q^m-1)(q^m-q).
\]
For every real \(\alpha>0\), the powered distance \(d^\alpha\) is conditionally negative semidefinite if and only if \(0<\alpha\le\alpha_q\). It is strictly conditionally negative definite on nonzero real zero-sum coefficients for \(0<\alpha<\alpha_q\), whereas at \(\alpha=\alpha_q\) its zero-sum nullspace has dimension exactly \(N_2\). Consequently, the minimal Euclidean dimension realizing \(d^\alpha\) as *squared* Euclidean distances is \(N-1\) below the endpoint and \(N_1\) at the endpoint. At the endpoint there is also an explicit **optimal projective-line embedding**: for any nonzero representatives \(v_L\) of the \(q+1\) lines \(L\) in \(\mathbb F_q^2\),
\[
d(X,Y)^{\alpha_q}=\frac1q\sum_{L\in\mathbb P^1(\mathbb F_q)}\mathbf1_{Xv_L\ne Yv_L}.
\]
Thus the critical power is exactly a scaled Hamming sum of \(q+1\) projective restrictions, not merely a formally positive Fourier multiplier.

For real \(t>0\), define the real symmetric matrix
\[
K_{\alpha,t}(X,Y)=\exp\{-t\,d(X,Y)^\alpha\},\qquad X,Y\in V.
\]
If \(0<\alpha\le\alpha_q\), then \(K_{\alpha,t}\) is positive definite for every \(t>0\). If \(\alpha>\alpha_q\), set \(a=2^\alpha\) and let \(z_*(q,\alpha)\in(0,1)\) be the **unique interior root** of
\[
f_{q,a}(z)=1-(q+1)z+qz^a=0.
\]
Then \(K_{\alpha,t}\) is positive definite precisely when \(t>t_*=-\log z_*\), is positive semidefinite of rank \(1+N_1\) precisely when \(t=t_*\), and is indefinite for \(0<t<t_*\). The critical nullspace is the \(N_2\)-dimensional span of additive characters whose frequency matrices have rank two. At \(t=0\), independently of \(\alpha\), the kernel is the all-ones matrix of rank one. In particular, for the **unpowered** rank distance \(\alpha=1\), the exact positive-semidefiniteness threshold is \(t_*=\log q\), with the stated strictness and nullity at equality. All thresholds are independent of \(m\).

## Assumptions and scope
There are no assumptions on characteristic; \(q\) may be any prime power, including powers of two. The ambient group is additive \(V\) of size \(q^{2m}\). By convention, \(d(X,X)=0\), hence every kernel diagonal is one. For \(\alpha>1\), the power \(d^\alpha\) need not satisfy the triangle inequality, but its exponential kernel is still well defined. Conditional negative semidefiniteness (CND) means
\[
\sum_{X,Y\in V}c_Xc_Yd(X,Y)^\alpha\le0\quad\text{for every real }(c_X)_{X\in V}\text{ with }\sum_Xc_X=0.
\]
At the endpoint, “nullspace” refers to the restricted centered quadratic form or, equivalently, its zero-frequency-removed Fourier eigenmodes; this is not the nullspace of the uncentered distance matrix. Squared-Euclidean embedding dimension is the rank of the centered Gram matrix associated with the specified squared distances.

## Proof
**1. Character diagonalization.** Fix a nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C^\times\). Each \(A\in V\) labels \(\chi_A(X)=\psi(\operatorname{tr}(A^{\mathsf T}X))\). Nondegeneracy of the trace pairing means these are all \(N\) distinct additive characters. Translation-invariant real symmetric kernels are diagonalized by them, and positive semidefiniteness holds exactly when all Fourier multipliers are nonnegative.

**2. Compute the two nontrivial rank-sphere transforms without a character table.** Every nonzero rank-one matrix is \(uv^{\mathsf T}\) with \(0\ne u\in\mathbb F_q^m\) and \(0\ne v\in\mathbb F_q^2\), represented exactly \(q-1\) times. For a frequency \(A\) of rank \(j\in\{0,1,2\}\), orthogonality in the \(u\) variable yields
\[
R_1(j)=\sum_{\operatorname{rank}X=1}\chi_A(X)
=\frac1{q-1}\sum_{0\ne v\in\mathbb F_q^2}\left(q^m\mathbf1_{Av=0}-1\right)
=\frac{q^m(q^{2-j}-1)-(q^2-1)}{q-1}.
\]
Thus \(R_1(0)=N_1\), \(R_1(1)=q^m-q-1\) and \(R_1(2)=-(q+1)\). The total character sum on \(V\) is \(N\) at \(A=0\) and zero at \(A\ne0\), so the rank-two transform is
\[
R_2(0)=N_2,\quad R_2(1)=q-q^m,\quad R_2(2)=q.
\]
Here \(N_1\) counts rank-one matrices and \(N_2\) counts ordered pairs of linearly independent columns. The identity \(1+N_1+N_2=N\) follows directly.

**3. The entire Gaussian spectrum.** Write \(z=e^{-t}\in(0,1)\), \(a=2^\alpha>1\). The convolution kernel is \(1\) on the zero matrix, \(z\) on rank-one matrices and \(z^a\) on rank-two matrices. By Step 2, its three Fourier eigenvalues, with multiplicities \(1,N_1,N_2\), are
\[
\begin{aligned}
\lambda_0(z)&=1+N_1z+N_2z^a>0,\\
\lambda_1(z)&=1+(q^m-q-1)z+(q-q^m)z^a\\
&=(1-z)+(q^m-q)(z-z^a)>0,\\
\lambda_2(z)&=1-(q+1)z+qz^a=f_{q,a}(z).
\end{aligned}
\]
The rank-one sector is therefore **never** the first obstruction to positive definiteness, regardless of \(m\). This is the dimension-independent spectral mechanism behind the result.

**4. Exact phase boundary.** For \(0<z<1\), \(f''_{q,a}(z)=qa(a-1)z^{a-2}>0\), while \(f(0)=1\), \(f(1)=0\), and \(f'(1)=qa-(q+1)\). When \(a\le1+q^{-1}\), strict convexity gives \(f(z)>0\) throughout \((0,1)\). When \(a>1+q^{-1}\), the derivative at one is positive, so \(f\) is negative just below one; strict convexity, the positive value at zero, and the single minimum give one and only one interior crossing \(z_*\). The sign of \(f\) is positive for \(0<z<z_*\), zero at \(z_*\), and negative for \(z_*<z<1\). The exact positive-definiteness, semidefiniteness and indefiniteness claims follow by Step 3. For \(\alpha=1\), \(f_{q,2}(z)=(1-z)(1-qz)\), proving \(z_*=q^{-1}\) and \(t_*=\log q\).

**5. CND and minimal Euclidean embedding dimension.** For \(D_\alpha(X,Y)=d(X,Y)^\alpha\), the Fourier multipliers on the two nontrivial character sectors are
\[
\begin{aligned}
\mu_1&=R_1(1)+2^\alpha R_2(1)=-1+(q^m-q)(1-2^\alpha)<0,\\
\mu_2&=R_1(2)+2^\alpha R_2(2)=-(q+1)+q2^\alpha.
\end{aligned}
\]
The zero-sum condition removes exactly the constant character, so \(D_\alpha\) is CND if and only if \(\mu_2\le0\), i.e. \(\alpha\le\log_2(1+q^{-1})\). Below the endpoint both nontrivial eigenvalues are strictly negative; at equality only the \(N_2\) rank-two characters enter the zero-sum nullspace. Finally, if \(H=I-N^{-1}\mathbf1\mathbf1^{\mathsf T}\), the centered Gram matrix \(-\frac12HD_\alpha H\) is positive semidefinite exactly in the CND range and its rank equals the minimum Euclidean embedding dimension for squared distances. Its rank is \(N-1\) below the endpoint and \(N_1\) at equality.

**6. Explicit optimal Hilbert embedding and subcritical interpolation.** For a nonzero difference \(\Delta=X-Y\), the kernel of the map \(v\mapsto\Delta v\) contains exactly one projective line if \(\operatorname{rank}\Delta=1\), and none if \(\operatorname{rank}\Delta=2\). Hence the number of projective directions with \(\Delta v_L\ne0\) is respectively \(q\) and \(q+1\), proving the displayed projective-line identity. Let \(\sigma:\mathbb F_q^m\to\mathbb R^{q^m-1}\) be any regular simplex embedding with squared mutual distance one. The map
\[
\Phi(X)=q^{-1/2}\bigoplus_{L\in\mathbb P^1(\mathbb F_q)}\sigma(Xv_L)
\]
realizes exactly \(d^{\alpha_q}\) as squared Euclidean distance in dimension \(N_1=(q+1)(q^m-1)\), which Step 5 proves optimal. Furthermore, for \(0<\alpha<\alpha_q\), put \(c=q(2^\alpha-1)\in(0,1)\). Then the exact identity
\[
d(X,Y)^\alpha=(1-c)\mathbf1_{X\ne Y}+c\,d(X,Y)^{\alpha_q}
\]
gives a direct strictly-negative-type decomposition into a positive discrete-metric component and the endpoint projective-Hamming metric. This geometric interpretation explains both the critical exponent and the abrupt drop in minimum Hilbert embedding dimension.

## Verification
The companion standalone Python checker `check_rank_kernel.py` independently enumerates rank-one and rank-two matrix spheres and all Fourier frequencies for \((q,m)=(2,2),(3,2),(2,3),(4,2)\). It checks each individual rank-sphere character sum against the proof's formulas (417 total frequency checks, including an extension field), tests the powered-kernel transform at several exponents and bandwidths, and checks the closed-form \(\alpha=1\) threshold and endpoint inequality for six field sizes. Run `python3 check_rank_kernel.py`; expected final line: `ALL_TWO_COLUMN_RANK_KERNEL_CHECKS_OK`. These finite checks are not used as proof for arbitrary \(m,q,\alpha,t\); the character-orthogonality and convexity argument above supplies that proof.

## Relationship to prior work
Delsarte's bilinear-form association scheme and its generalized Krawtchouk character table already determine the rank-one and rank-two Fourier-sphere coefficients. Gadouleau and Yan's rank-metric MacWilliams identity supplies another well-established route to those coefficients. The present contribution does **not** claim those transforms as new. Rather, it applies them to the specific conditionally-negative-type and Gaussian-kernel positivity questions for the two-column rank metric and obtains the sharp power threshold, the complete finite-bandwidth transition, the critical nullspace, and the corresponding minimal squared-Euclidean dimensions, uniformly in the number of rows. Meckes' general negative-type/positive-definiteness equivalence explains the functional-analytic relationship but does not provide these field-size-dependent constants. These conclusions should be viewed as an exact, natural specialization rather than an improvement to the classical association-scheme character table.

## Limitations
The formulas apply to **two-column** full matrix spaces, not to arbitrary column counts or rank-metric subcodes. Character eigenvalues are calculated without normalizing by the group order; changing Fourier normalization scales eigenvalues but not signs, nullities or thresholds. The case \(t=0\) is explicitly exceptional. Although literature searches and full-text comparisons were undertaken, an older unlocated classification of Gaussian positive-definiteness for bilinear-forms graphs could make the phase diagram previously known. An independent review has not been performed.

## References
1. P. Delsarte, “Bilinear Forms over a Finite Field, with Applications to Coding Theory,” *Journal of Combinatorial Theory, Series A* 25 (1978), 226–241, DOI: 10.1016/0097-3165(78)90015-8; especially Section 2 and Appendix, Theorem A2.
2. M. Gadouleau and Z. Yan, “MacWilliams Identity for the Rank Metric,” arXiv:cs/0701097, first public version 2007-01-16; Sections II–III.
3. M. W. Meckes, “Positive Definite Metric Spaces,” arXiv:1012.5863, Section 3 (especially Theorem 3.3), original preprint 2010.
