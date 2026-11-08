# Exact rank-one characteristic-polynomial fibers and Jordan dominance over finite fields

## Finding

Fix a finite field \(k=\mathbb F_q\), a positive integer \(n\), and a matrix \(A\in M_n(k)\). Its characteristic polynomial is \(\chi_A(t)=\det(tI-A)\). For each monic \(\theta\in k[t]\) of degree \(n\), define the ordered-vector fiber
\[
F_A(\theta)=\#\{(u,v)\in k^n\times k^n:\chi_{A+uv^{\mathsf T}}=\theta\}.
\]

Write the primary rational-canonical decomposition of \(A\) as
\[
k^n\cong\bigoplus_{f\mid\chi_A}\bigoplus_{j=1}^{s_f} k[t]/(f^{\lambda_{f,j}}),
\]
where \(f\) runs over **distinct monic irreducible** factors and \(\lambda_f=(\lambda_{f,1}\ge\dots\ge\lambda_{f,s_f}>0)\) is its partition. Define \(d_f=\deg f\), \(M_f=\sum_j\lambda_{f,j}\), and \(L_f=\lambda_{f,1}\). For every \(e\ge0\), set
\[
K_{f,e}=q^{d_f\sum_j\min(e,\lambda_{f,j})},\qquad K_{f,-1}=0.
\]
For \(h=\chi_A-\theta\), let \(\nu_f(h)\) be the exponent of \(f\) in nonzero \(h\), and put \(\nu_f(0)=\infty\). Define \(r_f=\max(0,M_f-\nu_f(h))\).

**The complete target-fiber theorem** is
\[
\boxed{F_A(\theta)=q^n\prod_{f\mid\chi_A}\left(\sum_{e=r_f}^{L_f}\frac{K_{f,e}-K_{f,e-1}}{q^{d_fe}}\right)}.
\tag{1}
\]
An empty local sum is zero. This holds for **every** prime power \(q\), every \(n\ge1\), every matrix \(A\), and every monic target polynomial of degree \(n\).

The multiplicity of **distinct nonzero rank-one update matrices** with output \(\theta\) is
\[
\boxed{N_A(\theta)=\begin{cases}
F_A(\theta)/(q-1),&\theta\ne\chi_A,\\
(F_A(\chi_A)-2q^n+1)/(q-1),&\theta=\chi_A.
\end{cases}}
\tag{2}
\]
No rank-one matrix is counted more than once in \(N_A\).

**Sharp dominance law.** If \(A\) and \(B\) have the same characteristic polynomial, and each partition \(\lambda_f(A)\) *dominates* \(\lambda_f(B)\), meaning
\[\sum_{j=1}^r\lambda_{f,j}(A)\ge\sum_{j=1}^r\lambda_{f,j}(B)\quad\text{for every }r\ge1,\]
then
\[
F_A(\chi_A)\le F_B(\chi_B),
\]
with **strict inequality** whenever any primary partition differs. In particular, for any fixed characteristic polynomial, the isospectral update count is minimized by choosing a single primary block for each irreducible factor, and maximized by choosing all primary blocks of size one. This conclusion applies equally to \(N_A(\chi_A)\) by (2).

**Irreducible and scalar extremes.** If \(\chi_A\) is irreducible, then
\[
F_A(\theta)=\begin{cases}2q^n-1,&\theta=\chi_A,\\q^n-1,&\theta\ne\chi_A.\end{cases}
\]
Thus **every other monic target is equally frequent**, whereas no nonzero rank-one update is isospectral. If \(A=\alpha I\), the only targets are \(\theta=(t-\alpha)^n-c(t-\alpha)^{n-1}\) for \(c\in k\); for \(c=0\) the fiber is \(q^n+(q^n-1)q^{n-1}\), and for each \(c\ne0\) it is \((q^n-1)q^{n-1}\). All other fibers vanish.

## Assumptions and scope

The transpose in \(uv^{\mathsf T}\) is an ordinary coordinate transpose, not a conjugate transpose. Vectors \(u\) and \(v\) are **ordered** and may be zero. Formula (1) counts vector **factorizations**, whereas (2) counts distinct rank-one matrices. These counts differ by the factor \(q-1\) for a nonzero rank-one matrix, while the zero matrix has \(2q^n-1\) vector factorizations. All statements are valid in arbitrary characteristic, including characteristic two; no division by field elements other than nonzero scalars occurs. The rational-canonical factors and partitions are understood over \(k\), not over an algebraic closure.

## Proof

**Step 1: linearization of a characteristic polynomial.** Write \(g_u(t)\) for the monic generator of \(\{a(t)\in k[t]:a(A)u=0\}\), with \(g_0=1\), and let \(d_u=\deg g_u\). The matrix determinant lemma gives the polynomial identity
\[
\chi_{A+uv^{\mathsf T}}(t)=\chi_A(t)-v^{\mathsf T}\operatorname{adj}(tI-A)u.
\tag{3}
\]
Because \(g_u(A)u=0\), the vector-polynomial \(g_u(t)(tI-A)^{-1}u\) has coefficients in \(k^n\) and degree below \(d_u\). The coefficient vectors span the cyclic subspace \(k[A]u=\operatorname{span}\{u,Au,\ldots\}\) and are independent: expand the identity
\[
g_u(t)(tI-A)^{-1}u=\frac{g_u(t)-g_u(A)}{tI-A}u
\]
using polynomial division. Its coefficients are triangular combinations of \(u,Au,\ldots,A^{d_u-1}u\) with diagonal coefficients one. Hence the map
\[
\Psi_u:v\longmapsto v^{\mathsf T}\operatorname{adj}(tI-A)u
\]
has kernel \((k[A]u)^\perp\) and image **exactly**
\[
(\chi_A/g_u)\cdot k[t]_{<d_u}.
\tag{4}
\]
The image dimension is \(d_u\), and every polynomial in that image has exactly \(q^{n-d_u}\) inverse images \(v\). Formula (4) also holds for \(u=0\), interpreted as the zero image.

**Step 2: primary exponents.** The elementary divisor decomposition gives \(g_u=\prod_f f^{e_f(u)}\) with \(0\le e_f(u)\le L_f\). For the \(f\)-primary component, the number of vectors annihilated by \(f^e\) is exactly
\[
K_{f,e}=\#\ker f(A)^e\big|_{V_f}=q^{d_f\sum_j\min(e,\lambda_{f,j})}.
\]
Therefore exactly \(K_{f,e}-K_{f,e-1}\) primary vectors have exponent **exactly** \(e\), including the zero primary vector at \(e=0\). Primary choices are independent.

**Step 3: target divisibility and fibers.** In (3), the required difference \(h=\chi_A-\theta\) lies in the image (4) if and only if \(\chi_A/g_u\mid h\). By unique factorization this is equivalent, for every \(f\mid\chi_A\), to \(e_f(u)\ge M_f-\nu_f(h)\), equivalently \(e_f(u)\ge r_f\). For such \(u\) there are exactly \(q^{n-\sum_fd_fe_f(u)}\) suitable vectors \(v\). Summing the independent primary counts gives precisely (1). Every pair produces one target, so this also proves \(\sum_{\theta\text{ monic},\deg\theta=n}F_A(\theta)=q^{2n}\).

**Step 4: removal of repeated rank-one factorizations.** Each nonzero rank-one matrix has exactly \(q-1\) factorizations \(uv^{\mathsf T}\), related by \((u,v)\mapsto(cu,c^{-1}v)\). The zero update has exactly \(2q^n-1\) factorizations. This proves (2).

**Step 5: strict dominance at the unchanged target.** With \(\theta=\chi_A\), all lower limits \(r_f\) vanish. For fixed primary multiplicity \(M_f\), continue \(K_{f,e}\) to \(e=M_f\); there \(K_{f,M_f}=q^{d_fM_f}\), independent of the partition. Discrete summation by parts yields
\[
\sum_{e=0}^{M_f}q^{-d_fe}(K_{f,e}-K_{f,e-1})
=q^{-d_fM_f}K_{f,M_f}
+\sum_{e=0}^{M_f-1}(q^{-d_fe}-q^{-d_f(e+1)})K_{f,e}.
\tag{5}
\]
Every coefficient of \(K_{f,e}\) in the last sum is positive. Under dominance, the concavity of \(x\mapsto\min(e,x)\) gives \(\sum_j\min(e,\lambda_j(A))\le\sum_j\min(e,\lambda_j(B))\) for all \(e\). If the two partitions differ, strictness occurs for some \(1\le e<M_f\), because these partial-kernel dimensions determine the partition. Equation (5), multiplication over the primary factors, and positivity prove the strict inequality.

**Step 6: extreme classes.** For irreducible \(\chi_A\), the primary type has one block with \(d_f=n\) and \(M_f=L_f=1\). For \(\theta\ne\chi_A\), the difference has degree less than \(n\) and cannot be divisible by \(f\), hence \(r_f=1\), giving \(F_A(\theta)=q^n-1\). At \(\theta=\chi_A\), add the contribution \(u=0\), obtaining \(2q^n-1\). For a scalar matrix, the primary partition is \((1,\ldots,1)\), the characteristic polynomial is \((t-\alpha)^n\), and (4) shows that the only possible differences are scalar multiples of \((t-\alpha)^{n-1}\). Counting the nonzero cyclic vectors and their compatible covectors gives the scalar formulas.

## Verification

The standalone file `verify_isospectral.py` tests the theorem by direct polynomial determinants, not by relying on (1). It exhausts all matrices of sizes \(2\) and \(3\) over \(\mathbb F_2\), all size-\(2\) matrices over \(\mathbb F_3\), and selected deterministic size-\(3\) and size-\(4\) matrices. Ten explicit rational-canonical types are checked against the primary-product formula; **all monic targets** are checked for each of these ten types. A separate numerical check exhausts 696 partition-dominance comparisons at small field sizes. The embedded text `verify_output.txt` records the exact observed results and the final success marker `ALL_RANK_ONE_SPECTRAL_FIBER_CHECKS_PASS`.

The finite checks are not a proof over arbitrary fields or dimension; Steps 1–6 provide that proof.

## Relationship to prior work

Ran and Wojtylak (arXiv:1104.0618v1, 2011), especially Proposition 2.2 and its resolvent identity, study the characteristic polynomials and eigenvalue trajectories under rank-one perturbations over the complex numbers. Farrell (arXiv:1508.07633v1, 2015) bounds the number of distinct eigenvalues after perturbation. Merzel, Mináč, Muller, Pasini and Nguyen (arXiv:2111.10624v1, 2021) give an existence characterization for prescribed rank-one spectral changes, and Merzel, Mináč, Nguyen and Pasini (arXiv:2306.10253v1, 2023) extend existence to higher update rank over arbitrary fields. The Kalman pole-placement formulation for a fixed input vector, including the characterization of its assignable characteristic polynomials, is also classical and is reviewed by Carriegos and Trobajo (2022). The fixed-input rank of the coefficient map is **not** claimed as new. These identities and existence conditions are **not** claimed as new. The present theorem counts across **all input vectors** via exact primary-partition multiplicities, giving the full finite-field **number of witnesses at each individual target**, including the characteristic-preserving count and its strict primary-partition dominance law. The support/zero-versus-nonzero classification follows in particular from the later existence theorem, so only the multiplicities and monotonicity are assessed as potential additions.

## Limitations

The result concerns unconstrained rank-one additive updates; it does not give similarity-class distributions of the updated matrices, higher-rank update fibers, or spectral distributions for symmetric-only updates. The counting law is an exact finite-field theorem, but no claim of comprehensive historical priority or independent verification is made. A broader published fiber-enumeration theorem not located in the accessible literature could cover it.

## References

- A. C. M. Ran and M. Wojtylak, *Eigenvalues of rank one perturbations of unstructured matrices*, first posted 2011-04-04, arXiv:1104.0618v1, https://arxiv.org/html/1104.0618v1 .
- P. E. Farrell, *The number of distinct eigenvalues of a matrix after perturbation*, first posted 2015-08-30, arXiv:1508.07633v1, https://arxiv.org/abs/1508.07633 .
- J. Merzel, J. Mináč, L. Muller, F. W. Pasini and T. T. Nguyen, *Spectral perturbation by rank one matrices*, first posted 2021-11-20, arXiv:2111.10624v1, https://arxiv.org/abs/2111.10624 .
- J. Merzel, J. Mináč, T. T. Nguyen and F. W. Pasini, *Spectral perturbation by rank-m matrices*, first posted 2023-06-17, arXiv:2306.10253v1, https://arxiv.org/abs/2306.10253 .
- M. V. Carriegos and M. T. Trobajo, *Kalman reduced form and pole placement by state feedback for multi-input linear systems over Hermite rings*, first online 2022-03-18, https://onlinelibrary.wiley.com/doi/full/10.1002/mma.8240 .
