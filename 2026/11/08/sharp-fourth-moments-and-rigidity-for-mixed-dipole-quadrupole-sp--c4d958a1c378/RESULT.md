# Sharp fourth moments and rigidity for mixed dipole–quadrupole spherical polynomials

## Finding

Let \(\sigma\) denote normalized rotationally invariant probability measure on \(\mathbb S^2\). The real eight-dimensional space \(\mathcal V=\mathcal H_1\oplus\mathcal H_2\) consists exactly of functions
\[
f(\omega)=v\cdot\omega+\omega^{\mathsf T}A\omega,
\qquad v\in\mathbb R^3,\quad A=A^{\mathsf T}\in\mathbb R^{3\times3},\quad\operatorname{tr}A=0.
\]
For every nonzero \(f\in\mathcal V\), the full **sharp** normalized fourth-moment interval is
\[
\boxed{\frac{45}{28}\ \le\ \frac{\int_{\mathbb S^2}f^4\,d\sigma}{\bigl(\int_{\mathbb S^2}f^2\,d\sigma\bigr)^2}\ \le\ \frac{375}{112}.}
\]
Every value in this interval occurs. The two endpoints have distinct, completely classified rigid geometries.

Put \(S_2=\operatorname{tr}(A^2)\), \(p=|v|^2/3\), \(q=2S_2/15\), and \(s=p+q=\|f\|_2^2\). The following exact, homogeneous, nonnegative **deficit identities** hold:
\[
\boxed{\int f^4\,d\sigma-\frac{45}{28}s^2
=\frac{48}{35}\left(p-\frac58s\right)^2+\frac{16}{35}|Av|^2,}
\tag{L}
\]
\[
\boxed{\frac{375}{112}s^2-\int f^4\,d\sigma
=\frac{192}{35}\left(p-\frac{15}{32}s\right)^2
+\frac{16}{35}\left(\frac23|v|^2S_2-|Av|^2\right).}
\tag{U}
\]
The last term in (U) is nonnegative by the trace-free eigenvalue inequality proved below.

The **lower** equality cases are precisely those with \(p=5s/8\), \(q=3s/8\), and \(Av=0\). Necessarily \(A\ne0\) has eigenvalues proportional to \((1,-1,0)\), and \(v\ne0\) lies on its zero-eigenspace. Equivalently, up to an orthogonal transformation of the sphere and nonzero real scaling, every lower extremizer is
\[
\omega\longmapsto \omega_1^2-\omega_2^2+\frac2{\sqrt3}\omega_3.
\]
The **upper** equality cases are precisely those with \(p=15s/32\), \(q=17s/32\), and \(A\) having eigenvalues proportional to \((-1,-1,2)\), with \(v\ne0\) parallel to the simple eigenvector (the eigenvector of maximal absolute eigenvalue). Equivalently, up to orthogonal transformation and nonzero real scaling, every upper extremizer is
\[
\omega\longmapsto 3\omega_3^2-1+\frac6{\sqrt{17}}\omega_3.
\]
The possible relative signs are included by the orthogonal transformations and real scaling, so these normal forms exhaust all cases.

## Assumptions and scope

All functions and matrices are **real**; the sphere has radius one; \(\sigma(\mathbb S^2)=1\); no constants (degree zero harmonics) belong to \(\mathcal V\). The trace-free condition ensures mean zero and identifies the exact degree-two harmonic component. The quotient is considered only for nonzero \(f\), and the statements include arbitrary orientations and all nonzero scales.

This solves the sharp \(L^2\)-to-\(L^4\) embedding of this particular mean-zero polynomial space, giving
\[
\sup_{0\ne f\in\mathcal V}\frac{\|f\|_4}{\|f\|_2}=\left(\frac{375}{112}\right)^{1/4},
\qquad
\inf_{0\ne f\in\mathcal V}\frac{\|f\|_4}{\|f\|_2}=\left(\frac{45}{28}\right)^{1/4}.
\]
The lower constant is a sharp reverse inequality *within this fixed subspace*, not a claim for arbitrary mean-zero functions.

## Proof

**Step 1: exact spherical moment identity.** For \(G\sim N(0,I_3)\), write \(G=R\omega\) with \(R\) independent of uniform \(\omega\in\mathbb S^2\). Then \(\mathbb E R^4=15\), \(\mathbb E R^6=105\), and \(\mathbb E R^8=945\). Define \(L=v\cdot G\) and \(Q=G^{\mathsf T}AG\). Standard Gaussian pairings (or expansion in an eigenbasis) give, for \(\operatorname{tr}A=0\),
\[
\mathbb E L^4=3|v|^4,\qquad
\mathbb E L^2Q^2=2|v|^2S_2+8|Av|^2,
\qquad
\mathbb E Q^4=12S_2^2+48\operatorname{tr}(A^4).
\]
Because \(A\) is trace-free symmetric of size three, Newton's identity gives \(\operatorname{tr}(A^4)=S_2^2/2\). Division by the corresponding independent radial moments, plus parity cancellation of odd powers of \(L\), yields
\[
\int f^2\,d\sigma=\frac{|v|^2}{3}+\frac{2S_2}{15}=p+q=s,
\]
\[
\int f^4\,d\sigma
=\frac{|v|^4}{5}+\frac4{35}|v|^2S_2+\frac{16}{35}|Av|^2+\frac4{105}S_2^2
=\frac95p^2+\frac{18}{7}pq+\frac{15}{7}q^2+\frac{16}{35}|Av|^2.
\tag{M}
\]
All the moments are with respect to normalized probability, so no area factor is hidden.

**Step 2: spectral boundary.** Let \(\lambda_1,\lambda_2,\lambda_3\) be the real eigenvalues of \(A\). Since \(\lambda_1+\lambda_2+\lambda_3=0\), for each \(i\) the Cauchy inequality gives
\[
\lambda_i^2=(\lambda_j+\lambda_k)^2\le2(\lambda_j^2+\lambda_k^2)
=2(S_2-\lambda_i^2).
\]
Consequently every \(v\) satisfies \(0\le|Av|^2\le(2/3)|v|^2S_2\). If \(A\ne0\), upper equality with \(v\ne0\) holds if and only if \(A\) has eigenvalue pattern \((-t,-t,2t)\) and \(v\) is parallel to its simple eigenvector. Lower equality \(|Av|^2=0\) with \(v\ne0\) means \(Av=0\); then the trace-free nonzero matrix has eigenvalue pattern \((t,-t,0)\), with \(v\) in the zero eigenspace.

**Step 3: sharp lower bound.** Substitute (M) and complete the square:
\[
\frac95p^2+\frac{18}{7}pq+\frac{15}{7}q^2
=\frac{45}{28}(p+q)^2+\frac{48}{35}\left(p-\frac58(p+q)\right)^2.
\]
This proves (L). Both terms vanish only if \(p=5s/8\) and \(Av=0\). Since \(s>0\), this enforces \(p,q>0\), so the spectral classification in Step 2 applies. The displayed lower normal form has \(|v|^2=4/3\) and \(S_2=2\), which indeed yield \(p:q=5:3\).

**Step 4: sharp upper bound.** Similarly,
\[
\frac95p^2+\frac{66}{7}pq+\frac{15}{7}q^2
=\frac{375}{112}(p+q)^2
-\frac{192}{35}\left(p-\frac{15}{32}(p+q)\right)^2.
\]
Since \((16/35)|Av|^2\le(16/35)(2/3)|v|^2S_2=(48/7)pq\), combining this equality with (M) gives (U). Simultaneous equality forces \(p=15s/32\), \(q=17s/32\), and the upper spectral equality in Step 2. The displayed upper normal form has \(|v|^2=36/17\), \(S_2=6\), which yield \(p:q=15:17\) exactly.

**Step 5: no other equality cases, complete range.** Every condition used in the two deficit identities is necessary as well as sufficient for equality. Their spectral conditions and fixed positive energy fractions give precisely the normal forms stated above. The real \(L^2\)-unit sphere of the eight-dimensional space is connected; the fourth moment is continuous on it, and its sharp endpoints are attained. By the intermediate value theorem its image is the entire closed interval between the endpoints.

## Verification

The included standalone `verify_mixed_sphere.py` uses only the Python standard library. It directly integrates monomials against the exact uniform spherical moment formula
\[
\mathbb E[\omega_1^{2a}\omega_2^{2b}\omega_3^{2c}]
=\frac{(2a-1)!!(2b-1)!!(2c-1)!!}{(2(a+b+c)+1)!!},
\]
with \((-1)!!=1\), and checks the invariant fourth-moment formula on 150 seeded rational coefficient choices. It independently checks both exact endpoint values and two numerical sphere grids for the extremal witnesses. These computations are consistency checks; the universal, continuous-parameter theorem is proved analytically above. Run the script with `python3 verify_mixed_sphere.py`.

## Relationship to prior work

The general study of norm comparison for spherical polynomial spaces appears in Marzo and Ortega-Cerdà (2007), but their results concern uniform norm comparison and sampling over varying polynomial degree, not the exact fourth-moment range and equality structure for \(\mathcal H_1\oplus\mathcal H_2\). Sogge and Zelditch (2010) study fourth moments of individual Laplace eigenfunctions and of bases, rather than mixed-degree sharp finite-dimensional constants. Dai, Feng and Tikhonov (2014) determine sharp *asymptotic orders* of reverse Hölder ratios on the single-degree harmonic spaces; these do not imply the stated degree-mixed two-sided constants.

A published exact result on the space \(\mathcal H_2\) alone identifies the normalized real degree-two fourth moment on \(\mathbb S^2\) as \(15/7\). This is the \(v=0\) case of (M), but does not control the mixed cross term \(|Av|^2\). Both new sharp endpoints are attained with \(v\ne0\), and they lie strictly below and strictly above \(15/7\). The two orientation patterns are new to the degree-mixed setting relative to the cited fixed-degree results.

## Limitations

Only real, mean-zero harmonics of degree one **plus** degree two on \(\mathbb S^2\) are covered. Constants, complex-valued functions, higher spherical dimensions, higher-degree mixed spaces, and other exponents are not addressed. There is no claim that the algebraic formulas are new as invariant moment identities; the finding is the optimized sharp two-sided inequality, exact remainders and full extremizer classification. Historical literature could contain an equivalent result under dipole–quadrupole or multipole terminology.

## References

1. J. Marzo and J. Ortega-Cerdà, “Equivalent norms for polynomials on the sphere,” arXiv:math/0703588v1 (first posted 2007-03-20), later *International Mathematics Research Notices* (2008).
2. C. D. Sogge and S. Zelditch, “Concerning the \(L^4\) norms of typical eigenfunctions on compact surfaces,” arXiv:1011.0215v1 (first posted 2010-10-31).
3. F. Dai, H. Feng and S. Tikhonov, “Reverse Hölder's inequality for spherical harmonics,” arXiv:1408.1877v1 (first posted 2014-08-06), later *Proceedings of the American Mathematical Society* (2016).
4. R. J. Stanton and A. Weinstein, “On the \(L^4\) norm of spherical harmonics,” *Mathematical Proceedings of the Cambridge Philosophical Society* **89** (1981), 343–358, DOI 10.1017/S0305004100058229.
5. “Sharp \(L^4/L^2\) norm and extremizers for degree-two spherical harmonics,” published research record, published-finding corpus identifier `d4106097159f` (2026); comparison limited to the exact degree-two subspace.
