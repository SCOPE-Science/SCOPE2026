# Exact Cauchy-tail law for Gaussian-sketched Lanczos Galerkin inverses

## Finding

Let \(A\in\mathbb R^{n\times n}\) be symmetric positive definite and \(b\in\mathbb R^n\) a unit vector. Fix an integer \(2\le k<n\), and suppose that the first \(k\) Lanczos vectors \(v_1=b,\ldots,v_k\) exist without breakdown. Set \(V=[v_1,\ldots,v_k]\), \(T=V^{\mathsf T}AV\), and write the Lanczos relation
\[
AV=VT+\beta v_{k+1}e_k^{\mathsf T},\qquad \beta\ge0.
\]
If \(\beta=0\), the \(k\)-dimensional Krylov subspace is invariant and the sketched approximation below equals \(A^{-1}b\) almost surely. If \(\beta>0\), for **every finite sketch width** \(s\ge k\), let \(S\in\mathbb R^{s\times n}\) have independent \(N(0,1/s)\) entries and form the sketched Galerkin inverse approximation
\[
\widehat x_k=V\bigl((SV)^\dagger SAV\bigr)^{-1}e_1.
\]
The inverse exists almost surely. Let \(\nu=s-k+1\), \(c=e_k^{\mathsf T}T^{-1}e_1\ne0\), and \(\eta=\beta\lVert T^{-1}e_k\rVert_2>0\). The terminal Lanczos coordinate \(Q=e_k^{\mathsf T}V^{\mathsf T}\widehat x_k\) has the **exact law**
\[
Q\ \stackrel{\mathrm d}=\ \frac{c}{1+(\eta/\sqrt\nu)\,Z_\nu},
\]
where \(Z_\nu\) is standard Student-t with \(\nu\) degrees of freedom. Consequently, setting
\[
\rho_\nu=\frac{\Gamma((\nu+1)/2)}{\sqrt\pi\,\Gamma(\nu/2)\,\eta}\left(1+\frac1{\eta^2}\right)^{-(\nu+1)/2}>0,
\]
we have the **sharp unconditional upper-tail asymptotic**
\[
\lim_{R\to\infty}R\,\mathbb P\{|Q|>R\}=2|c|\rho_\nu>0.
\]
Thus \(\mathbb E|Q|^p<\infty\) holds precisely for \(0<p<1\), while, for **every** \(p\ge1\),
\[
\mathbb E\bigl\lVert\widehat x_k-A^{-1}b\bigr\rVert_2^p=\infty.
\]
These are unconditional statements about an unconditioned Gaussian sketch. They do not apply after conditioning on a certified sufficiently accurate subspace embedding, replacing the projection with a harmonic method, or adding a protective regularization.

## Assumptions and scope

The matrix and right-hand side are deterministic, real, and in exact arithmetic; \(A\) is positive definite; \(\lVert b\rVert_2=1\); Lanczos runs to \(k\) without an earlier breakdown, so \(T\) is an irreducible symmetric positive-definite tridiagonal matrix. The sketch is drawn independently of the deterministic Krylov basis, with all entries independent centered Gaussian with variance \(1/s\). The pseudoinverse and reduced inverse are exact. The choice \(k\ge2\) excludes the already familiar one-vector denominator. At \(\beta=0\) no \(v_{k+1}\) is needed; one may set the residual term to zero.

This is the sketched Petrov–Galerkin/FOM inverse for \(f(z)=1/z\), equivalent under any nonsingular change of Krylov coordinates to a sketched Arnoldi approximation. It is *not* the least-squares/sketched-minimal-residual or sketched harmonic projection. Although the motivating analysis discusses general matrix functions, the proven claim concerns the inverse function alone.

## Proof

**Lanczos reduction.** Because \(V\) and \(v_{k+1}\) are orthonormal, the Gaussian matrices \(U=SV\in\mathbb R^{s\times k}\) and \(z=Sv_{k+1}\in\mathbb R^s\) have independent \(N(0,1/s)\) entries. Since \(s\ge k\), \(U\) has full column rank almost surely. Write \(W=U^{\mathsf T}U\). Direct substitution into the sketched Petrov–Galerkin equations gives
\[
(SV)^\dagger SAV=T+t e_k^{\mathsf T},\qquad t=\beta W^{-1}U^{\mathsf T}z.
\]
Let \(y=(T+t e_k^{\mathsf T})^{-1}e_1\), \(a=T^{-1}e_k\), \(c=e_k^{\mathsf T}T^{-1}e_1\), and \(D=a^{\mathsf T}t\). Multiplying the reduced equation by \(e_k^{\mathsf T}T^{-1}\) shows
\[
e_k^{\mathsf T}y=c-D(e_k^{\mathsf T}y),\qquad e_k^{\mathsf T}y=\frac{c}{1+D}.
\]
The matrix determinant lemma gives \(\det(T+t e_k^{\mathsf T})=\det(T)(1+D)\).

**Nonvanishing numerator.** Write the positive Lanczos subdiagonals of \(T\) as \(\gamma_1,\ldots,\gamma_{k-1}\). Cofactor expansion (or the irreducible tridiagonal inverse formula) yields
\[
c=(-1)^{k-1}\frac{\gamma_1\gamma_2\cdots\gamma_{k-1}}{\det T}\ne0.
\]
When \(\beta>0\), also \(\eta=\beta\lVert a\rVert_2>0\).

**Exact random law.** Write \(U=G/\sqrt s\) and \(z=g/\sqrt s\), where \(G\in\mathbb R^{s\times k}\) and \(g\in\mathbb R^s\) are independent standard Gaussian. Rotational symmetry permits a deterministic orthogonal change of coordinates in the \(k\) columns of \(G\) taking \(a/\lVert a\rVert_2\) to the first coordinate. Let \(g_1\) be the first column and \(G_2\) contain the remaining \(k-1\) columns. Conditional on \(G_2\), let \(P\) be the orthogonal projection onto \(\operatorname{range}(G_2)^\perp\), of dimension \(\nu=s-k+1\). Standard block elimination for least squares yields
\[
D\ \stackrel{\mathrm d}=\ \beta\lVert a\rVert_2\frac{g_1^{\mathsf T}Pg}{g_1^{\mathsf T}Pg_1}.
\]
Here \(\lVert Pg_1\rVert_2^2\sim\chi^2_\nu\), and conditionally on \(Pg_1\), the normalized dot product with the independent \(g\) is standard normal. Its conditional law is constant, hence this normal is independent of \(\lVert Pg_1\rVert_2\). We obtain \(D\stackrel{\mathrm d}=\eta Z_\nu/\sqrt\nu\). Its density at \(-1\) is precisely \(\rho_\nu\), strictly positive and finite, proving that the reduced matrix is almost surely nonsingular.

**Tail and moments.** Since \(Q=c/(1+D)\),
\[
\mathbb P\{|Q|>R\}=\int_{-1-|c|/R}^{-1+|c|/R}f_D(u)\,du,
\]
where \(f_D\) is the continuous Student density. Continuity at \(-1\) gives the asserted sharp tail constant. For \(p\ge1\), the integral of \(|1+u|^{-p}f_D(u)\) near \(u=-1\) diverges; for \(0<p<1\) it converges both near the pole and at infinity, so the coordinate moment cutoff is exact. Orthogonality gives \(\lVert\widehat x_k\rVert_2\ge|Q|\). Since \(A^{-1}b\) is deterministic and finite, the triangle inequality then implies infinite \(p\)-th absolute error moments for every \(p\ge1\).

**Invariant case.** If \(\beta=0\), then \(AV=VT\) and \(A^{-1}b=VT^{-1}e_1\). For every full-rank \(SV\), \((SV)^\dagger SAV=T\), hence \(\widehat x_k=A^{-1}b\). This completes the dichotomy.

## Verification

The standalone script `verify.py` requires only the Python standard library. Execute `python verify.py`. It reconstructs exactly, using rational arithmetic, \(1{,}767\) full-rank Gaussian-sketch-geometry instances for unreduced tridiagonal positive-definite matrices with \(k=2,3,4\) and varying \(s\). It checks the reduced matrix, determinant lemma, terminal coefficient, and Sherman–Morrison vector identity. An additional \(12\) numerical density integrations compare the exact Student density at the pole with the predicted \(R^{-1}\) asymptotic. The expected success marker is `VERIFY_OK`. Rational inputs test the identities, not a claim that rational sketches follow the Gaussian law. Distributional statements and moment divergence follow from the analytic arguments above.

For an explicit well-conditioned instance take \(A=\begin{psmallmatrix}3&1&0\\1&3&1\\0&1&3\end{psmallmatrix}\), \(b=e_1\), \(k=2\). Its condition number \((3+\sqrt2)/(3-\sqrt2)<3\). Here \(T=\begin{psmallmatrix}3&1\\1&3\end{psmallmatrix}\), \(\beta=1\), \(c=-1/8\), \(\eta=\sqrt{10}/8\), so the theorem applies for every \(s\ge2\) with \(\nu=s-1\). No ill-conditioning of the original system is necessary.

## Relationship to prior work

The sketched Arnoldi/FOM inverse in this theorem is the inverse-function specialization of the sketched Petrov–Galerkin formula (11) in Güttel, Liu and Nyman (2026). Their theorem conditions on a suitable subspace embedding, and their sketched harmonic method is distinct; the present unconditional Gaussian-tail result does not invalidate those conditional guarantees. Timsit, Grigori and Balabanov (2023) analyze quasi-optimality and observe spikes for randomized orthogonal projections; their conditional estimates do not specify this exact \(k\)-dependent Student law or the unconditional moment cutoff. Palitta, Schweitzer and Simoncini analyze rank-one modifications and the role of outlying Ritz values, including some functions for which such effects can be mild; their analysis does not establish this inverse-function moment dichotomy. Grigori, Kressner, Shao and Simunec (2026) study a similarity-restoring modification that recovers the standard Arnoldi approximation; that repaired construction is outside the present random projection. The distributional step uses classical Gaussian regression and Student-t facts; the claimed new component is the universal Lanczos linkage, exact tail coefficient, and invariant-versus-noninvariant classification for the inverse computation.

## Limitations

Unconditional Gaussian sketching, fixed deterministic initial data, no restart, one \(k\)-step sketched Galerkin inverse, and exact arithmetic only. A certified embedding event may exclude the problematic near-pole outcomes. Conditioning on such an event or regularizing the reduced inverse changes the law. The theorem does not assert that individual runs are inaccurate, that restarted algorithms diverge, that sparse sign sketches share this law, or that sketched harmonic, least-squares/minimal-residual, or similarity-restored variants have divergent moments. The theorem proves no complete vector-valued \(0<p<1\) moment classification. Independence or novelty beyond the inspected literature is not externally certified.

## References

1. S. Güttel, J. Liu, L. Nyman, *Sketch-and-Restart: Randomized Sketching in Quadrature-Based Restarting for Matrix Functions*, arXiv:2607.10354v1, first publicly posted 2026-07-11, Sections 2.2 and 4–5. https://arxiv.org/html/2607.10354v1
2. E. Timsit, L. Grigori, O. Balabanov, *Randomized Orthogonal Projection Methods for Krylov Subspace Solvers*, arXiv:2302.07466v3, 2023, Sections 3 and 5. https://arxiv.org/html/2302.07466v3
3. D. Palitta, M. Schweitzer, V. Simoncini, *Sketched and Truncated Polynomial Krylov Methods: Evaluation of Matrix Functions*, Numerical Linear Algebra with Applications (2025), doi:10.1002/nla.2596, Sections 2.3, 5–7. https://doi.org/10.1002/nla.2596
4. L. Grigori, D. Kressner, N. Shao, I. Simunec, *Restoring similarity in randomized Krylov methods with applications to eigenvalue problems and matrix functions*, arXiv:2601.10248v1, 2026. https://arxiv.org/html/2601.10248v1
