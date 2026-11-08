# Exact identity-trace variance and square-root rank transition for Gaussian tensor trains

## Finding

For Gaussian tensor-train (TT) query vectors with independent, unnormalized Gaussian cores, the variance of the single-probe trace estimate of the identity has an exact two-state transfer formula in every tensor order, mode dimension, and bond rank. Its long-chain relative variance undergoes a sharp transition when the bond rank has square-root growth in the tensor order. This is different from a general-purpose uniform trace-estimation guarantee, which need not be sharp on the identity.

Let \(d\ge2\), \(n\ge2\), and \(r\ge1\) be integers. Define \(e=1/n\), \(\eta=1/r\), and the real numbers
\[
U_1=1+2e\eta,\qquad V_1=e+\eta+e\eta.
\]
For each \(k=2,\ldots,d-1\), perform the recursion
\[
\begin{pmatrix}U_k\\V_k\end{pmatrix}
=\begin{pmatrix}1&2e\eta\\\eta&e(1+\eta)\end{pmatrix}
\begin{pmatrix}U_{k-1}\\V_{k-1}\end{pmatrix}.
\]
The recursion is empty if \(d=2\). For the TT query vector \(\omega\) defined below, the exactly normalized identity-trace risk is
\[
\boxed{\frac{\operatorname{Var}(\omega^T I_{n^d}\omega)}{\|I_{n^d}\|_F^2}
=n^d\bigl(U_{d-1}+2eV_{d-1}-1\bigr).}
\]

In the long-chain regime with a fixed mode dimension \(n\ge2\), and bond ranks \(r_d\) allowed to vary with \(d\), the following trichotomy is sharp:
\[
\lim_{d\to\infty}\frac{\operatorname{Var}(\omega^T I_{n^d}\omega)}{(\operatorname{tr}I_{n^d})^2}
=\begin{cases}
+\infty,&r_d/\sqrt d\to0,\\
\exp\!\bigl(2/((n-1)c^2)\bigr)-1,&r_d/\sqrt d\to c\in(0,\infty),\\
0,&r_d/\sqrt d\to\infty.
\end{cases}
\]
Thus \(\sqrt d\) is the exact bond-rank scale for bounded relative mean-square risk on the identity, rather than a claim about uniform control for all positive semidefinite matrices.

There is a second, complementary critical scaling. Fix \(d\ge2\), let \(n\to\infty\), and suppose \(r/n^{d-1}\to c\in(0,\infty)\). Then
\[
\boxed{\frac{\operatorname{Var}(\omega^T I_{n^d}\omega)}{\|I_{n^d}\|_F^2}
\longrightarrow 2+\frac4c.}
\]
The same limit equals \(2\) when \(r/n^{d-1}\to\infty\), and diverges when \(r/n^{d-1}\to0\). The baseline \(2\) is the familiar Gaussian-probe Frobenius variance constant; the additional \(4/c\) is the exact critical TT excess.

## Assumptions and scope

For all indices \(i_1,\ldots,i_d\in\{1,\ldots,n\}\), define the real Gaussian TT vector by
\[
\omega_{i_1,\ldots,i_d}
=r^{-(d-1)/2}\sum_{a_1,\ldots,a_{d-1}=1}^{r}
G^{[1]}_{i_1,a_1}\left(\prod_{j=2}^{d-1}G^{[j]}_{a_{j-1},i_j,a_j}\right)G^{[d]}_{a_{d-1},i_d}.
\]
Every scalar entry of every core is an independent \(\mathcal N(0,1)\) variable. The empty product for \(d=2\) equals one. The vectorization ordering is immaterial for the identity. The construction agrees with the normalized Gaussian TT distribution in Bujanović–Kressner–Olić (2026), Definition 1. This result concerns exact real arithmetic and the single quadratic estimator \(H=\omega^T I_{n^d}\omega=\|\omega\|_2^2\). Isotropy gives \(\mathbb EH=n^d\), and \(\|I_{n^d}\|_F^2=n^d\).

All finite-parameter identities are exact for integers \(d,n,r\) in the stated range. The long-chain limit fixes \(n\ge2\), whereas the large-mode limit fixes \(d\ge2\); the limits must not be interchanged without justification.

## Proof

**1. Gaussian transfer of two Gram invariants.** Contract the first \(k\) cores without normalization to form an interface matrix \(L_k\in\mathbb R^{n^k\times r}\), for \(1\le k\le d-1\). Let \(M_k=L_k^TL_k\), and put \(u_k=\mathbb E(\operatorname{tr}M_k)^2\) and \(v_k=\mathbb E\operatorname{tr}(M_k^2)\). Initially, \(L_1\) is an \(n\times r\) standard Gaussian matrix. By Gaussian fourth moments,
\[
u_1=(nr)^2+2nr,\qquad v_1=nr(n+r+1).
\]
For \(2\le k\le d-1\), write the next core as independent standard Gaussian \(r\times r\) matrices \(B_1,\ldots,B_n\). Its Gram update is
\[
M_k=\sum_{j=1}^n B_j^T M_{k-1}B_j.
\]
Conditionally on any fixed real symmetric positive semidefinite \(M\), the \(nr\) diagonal column quadratic forms have mean \(\operatorname{tr}M\) and variance \(2\operatorname{tr}(M^2)\). Consequently,
\[
\mathbb E[(\operatorname{tr}M_k)^2\mid M_{k-1}=M]
=(nr)^2(\operatorname{tr}M)^2+2nr\operatorname{tr}(M^2).
\]
For \(\operatorname{tr}(M_k^2)\), each of the \(r\) diagonal entries has second moment \(n^2(\operatorname{tr}M)^2+2n\operatorname{tr}(M^2)\), while each of the \(r(r-1)\) ordered off-diagonal entries has second moment \(n\operatorname{tr}(M^2)\). Hence
\[
\begin{pmatrix}u_k\\v_k\end{pmatrix}
=\begin{pmatrix}(nr)^2&2nr\\n^2r&nr(r+1)\end{pmatrix}
\begin{pmatrix}u_{k-1}\\v_{k-1}\end{pmatrix}.
\]
Dividing both invariants at level \(k\) by \((nr)^{2k}\), and defining \(U_k=u_k/(nr)^{2k}\), \(V_k=v_k/(nr)^{2k}\), produces precisely the displayed two-state recursion and initial values.

**2. Exact risk.** The last core is an independent standard Gaussian matrix \(C\in\mathbb R^{r\times n}\). Conditional on \(L_{d-1}\), the unnormalized final contraction is \(L_{d-1}C\). Independence of the \(n\) Gaussian columns gives
\[
\mathbb E\bigl[\|L_{d-1}C\|_F^4\mid L_{d-1}\bigr]
=n^2(\operatorname{tr}M_{d-1})^2+2n\operatorname{tr}(M_{d-1}^2).
\]
Divide by \(r^{2(d-1)}\) to obtain \(\mathbb EH^2=n^{2d}(U_{d-1}+2eV_{d-1})\). Since \(\mathbb EH=n^d\), subtraction of its square proves the finite-parameter formula. As a check, \(d=2\) simplifies to
\[
\frac{\operatorname{Var}(H)}{\|I_{n^2}\|_F^2}
=\frac{2(2n+r+1)}r.
\]
For \(r=1\), the vector is an ordinary Gaussian tensor product and the formula reduces to
\[
\frac{\operatorname{Var}(H)}{(\mathbb EH)^2}=(1+2/n)^d-1.
\]

**3. Sharp long-chain transition.** For fixed \(n\ge2\), set \(\eta=1/r\). The transfer matrix is positive and its larger eigenvalue is
\[
\lambda_+(n,r)=\frac{1+e(1+\eta)+\sqrt{(1-e(1+\eta))^2+8e\eta^2}}2.
\]
It is strictly greater than one for every finite \(r\). As \(r\to\infty\), a Taylor expansion at the simple eigenvalue one yields
\[
\log\lambda_+(n,r)=\frac{2}{(n-1)r^2}+O_n(r^{-3}).
\]
The other eigenvalue tends to \(1/n\); the coefficient of the leading eigenmode in \(U_{d-1}+2eV_{d-1}\) tends to one. Thus, whenever \(r=r_d\to\infty\),
\[
\log\bigl(U_{d-1}+2eV_{d-1}\bigr)
=\frac{2d}{(n-1)r_d^2}(1+O_n(r_d^{-1}))+o(1),
\]
with the negligible second eigenmode accounted for. This proves the finite nonzero limit and the vanishing regime by comparing \(d/r_d^2\) with constants. If \(r_d=o(\sqrt d)\) without tending to infinity, use monotonicity of the exact recursion in \(\eta\): for every fixed \(R\), ranks at most \(R\) have at least the exponentially growing risk corresponding to \(R\). Along unbounded subsequences with \(r_d\to\infty\), the eigenvalue estimate gives the same divergence. The trichotomy follows.

**4. Fixed-order large-mode transition.** For fixed \(d\), direct induction on the normalized two-state recursion gives, with \(n,r\to\infty\),
\[
U_{d-1}+2eV_{d-1}-1
=2n^{-d}+4(nr)^{-1}
+O_d\bigl((n^2r)^{-1}+(nr^2)^{-1}\bigr).
\]
Multiplication by \(n^d\) gives the claimed \(2+4/c\) critical limit, and the Gaussian limit \(2\) above the critical rank. Below it, conditioning on the first TT core \(G^{[1]}\) yields
\[
\mathbb E[H\mid G^{[1]}]=\frac{n^{d-1}}r\|G^{[1]}\|_F^2,
\]
and total variance gives the exact lower bound \(\operatorname{Var}(H)/n^d\ge2n^{d-1}/r\), proving divergence. No appeal to Monte Carlo sampling is needed for any limit.

## Verification

The self-contained `verify_tt_identity.py` uses exact rational arithmetic to check the recursion against independent two- and three-core closed formulas, the product-Gaussian rank-one identity, and strict monotonicity in bond rank for a broad finite grid. It also compares the two critical asymptotic formulas with finite parameters and performs seeded, optional Gaussian-core simulations directly from the defining contractions. Its final output on the bundled run was `VERIFY_OK 1510 exact/simulation checks`.

These finite checks corroborate algebraic specialization and normalization; the stated universal identities, limits, and phase transitions are proved by the conditional Gaussian and spectral arguments above.

## Relationship to prior work

Bujanović, Kressner and Olić (2026) define this precise Gaussian TT distribution, establish moment upper bounds and dimension-independent trace-scale concentration with sufficient TT rank, and give a lower bound showing that Frobenius-scale variance can be large even for \(A=I\). Their identity example yields \(\operatorname{Var}(H)/\|I\|_F^2\ge2n^{d-1}/r\), but not an exact finite-order identity or the square-root long-chain transition proved here. Their general moment bound \(3(1+2/r)^{d-1}-1\) on trace-normalized variance is not sharp for the identity in the critical \(r\asymp\sqrt d\) regime.

Meyer and Avron (2023) derive an exact partial-trace and partial-transpose variance law for a product of independent Gaussian vectors, the \(r=1\) case. That result does not determine the contractions and inter-core correlations at higher TT bond rank \(r>1\), nor the two-state transfer spectrum. Random matrix-product-state literature provides related ensembles, but often with Haar/isometric or already normalized cores, rather than the specified independent raw Gaussian cores. No general novelty claim is made for fourth-moment techniques themselves.

## Limitations

The result concerns the identity as a test operator, not an optimum over all positive semidefinite matrices, not a relative-error tail probability, and not a general subspace-embedding theorem. A finite variance threshold alone does not imply a matching sample-complexity lower bound for every concentration criterion. TT cores are independent Gaussian variables without orthogonalization or random normalization; changing that distribution may change the constants and exponents. Proof and checks use exact real Gaussian moments, not floating-point error analysis. Historical mathematical priority remains subject to possible equivalent formulas in tensor-network or random-matrix-product-state literature.

## References

1. Z. Bujanović, D. Kressner, H. Olić, *Stochastic trace estimation with tensor train random vectors*, arXiv:2606.15679v1 (first public posting 2026-06-14), especially Definition 1, Section 3 and the identity variance example in Section 4. https://arxiv.org/abs/2606.15679 ; https://arxiv.org/html/2606.15679
2. R. A. Meyer, H. Avron, *Hutchinson's Estimator is Bad at Kronecker-Trace-Estimation*, arXiv:2309.04952 (2023), Theorem 1 on the rank-one product-Gaussian variance. https://arxiv.org/abs/2309.04952
3. S. Garnerone, T. R. de Oliveira, S. Haas, P. Zanardi, *Statistical properties of random matrix product states*, Physical Review A **82**, 052312 (2010), for related but differently constructed random matrix-product-state ensembles. https://doi.org/10.1103/PhysRevA.82.052312
