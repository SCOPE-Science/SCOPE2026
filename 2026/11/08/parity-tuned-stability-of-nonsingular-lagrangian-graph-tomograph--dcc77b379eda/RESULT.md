# Parity-tuned stability of nonsingular Lagrangian graph tomography over finite fields

## Finding
Let \(q\ge 2\) be any prime power and \(d\ge 2\) any integer. On the symplectic vector space \(V=\mathbb F_q^d\oplus\mathbb F_q^d\), sum functions over all affine graphs \(\{(x,Mx+c):x\in\mathbb F_q^d\}\), with \(c\in\mathbb F_q^d\) and \(M\) **invertible and symmetric**. Let \(R\) be the resulting counting-measure incidence operator. Define \(S_j(q)\) as the number of invertible symmetric \(j\times j\) matrices over \(\mathbb F_q\), with \(S_0(q)=1\). Its complete squared singular-value spectrum (the eigenvalues of \(R^*R\)) is:

| Squared singular value | Multiplicity | Fourier sector |
|---|---:|---|
| \(q^d S_d(q)\) | \(1\) | \((\alpha,\beta)=(0,0)\) |
| \(0\) | \(2(q^d-1)\) | exactly one of \(\alpha,\beta\) is zero |
| \(q^d S_{d-1}(q)\) | \((q^d-1)(q-1)q^{d-1}\) | \(\alpha,\beta\ne0\), \(\alpha\cdot\beta\ne0\) |
| \(q^{2d-1} S_{d-2}(q)\) | \((q^d-1)(q^{d-1}-1)\) | \(\alpha,\beta\ne0\), \(\alpha\cdot\beta=0\) |

The last two rows are combined when their values coincide. Thus
\[
\operatorname{rank}R=1+(q^d-1)^2,\qquad
\ker R=\{g(x)+h(y):\sum_x g(x)=\sum_y h(y)=0\}.
\]
After removal of the constant Fourier component, the nonzero singular values are **all equal if and only if \(d\) is odd**. If \(d\) is even, the sharp singular-value condition number on the mixed (nonconstant recoverable) component is
\[
\kappa_{\rm mixed}(R)=\frac{1}{\sqrt{1-q^{1-d}}}.
\]
On the entire recoverable subspace (including the constants), the sharp singular-value condition number is
\[
\kappa_{\rm visible}(R)=
\begin{cases}
\sqrt{q^d-1},&d\text{ odd},\\
q^{d/2},&d\text{ even}.
\end{cases}
\]
This gives an exact pseudoinverse by dividing each visible Fourier coefficient by its corresponding listed eigenvalue.

## Assumptions and scope
Fix the finite field \(F=\mathbb F_q\) and standard nondegenerate bilinear dot product on \(F^d\). The alternating form on \(V=F^d\oplus F^d\) is \(\langle(x,y),(x',y')\rangle=x\cdot y'-x'\cdot y\); the graphs \(y=Mx+c\) are affine Lagrangian when \(M=M^T\). Requiring \(M\) invertible makes the direction transverse to both coordinate Lagrangians. The family contains every such graph once. The operator is
\[
(Rf)(M,c)=\sum_{x\in F^d}f(x,Mx+c),
\qquad M\in\operatorname{Sym}_d(F)^\times,\ c\in F^d.
\]
Both input \(\ell^2(F^{2d})\) and output \(\ell^2(\operatorname{Sym}_d(F)^\times\times F^d)\) use **unnormalized counting measure**. No positivity or reality assumption is made on \(f\). Choose any fixed nontrivial additive character \(\psi:F\to\mathbb C^\times\), and index the mutually orthogonal input Fourier characters by \(\chi_{\alpha,\beta}(x,y)=\psi(\alpha\cdot x+\beta\cdot y)\). These character labels use the canonical identification of the vector space with its additive Pontryagin dual. The statements include characteristic two.

The symmetric-matrix counts have the closed forms
\[
S_{2m}(q)=q^{m(m+1)}\prod_{i=1}^m(q^{2i-1}-1),\qquad
S_{2m+1}(q)=q^{m(m+1)}\prod_{i=1}^{m+1}(q^{2i-1}-1),
\]
with empty products equal to one.

## Proof
**Fourier diagonalization.** For any \(M,c,\alpha,\beta\), additive-character orthogonality yields
\[
(R\chi_{\alpha,\beta})(M,c)
=q^d\,\mathbf 1_{\{M\beta=-\alpha\}}\,\psi(\beta\cdot c).
\]
Translation invariance implies that \(R^*R\) is diagonal in this Fourier basis. Directly computing the output norm and dividing by the input squared norm \(q^{2d}\) gives its eigenvalue
\[
\lambda(\alpha,\beta)=q^d\#\{M\in\operatorname{Sym}_d(F)^\times:M\beta=-\alpha\}.
\]
If \(\beta=0\), the count is \(S_d(q)\) for \(\alpha=0\) and zero otherwise. If \(\beta\ne0\), invertibility forces \(\alpha\ne0\).

**Prescribed image of a nonzero vector.** If \(\beta\ne0\), make an invertible change of basis using symmetric congruence \(M\mapsto P^TMP\) to send \(\beta\) to the first coordinate vector. The condition \(M\beta=-\alpha\) then prescribes the first column \((a,z)^T\), where \(a=-\alpha\cdot\beta\) and \(z\in F^{d-1}\). When \(a\ne0\), the Schur complement of \(a\) is an arbitrary invertible symmetric \((d-1)\)-matrix. Hence the count is \(S_{d-1}(q)\).

When \(a=0\) and \(z\ne0\), choose an invertible basis change in the last \(d-1\) coordinates to normalize the first off-diagonal row to \((1,0,\ldots,0)\). The resulting matrix has block form
\[
\begin{pmatrix}
0&1&0\\1&b&u^T\\0&u&C
\end{pmatrix},
\]
whose determinant equals \(-\det C\), independently of \(b\in F\) and \(u\in F^{d-2}\). There are exactly \(q^{d-1}S_{d-2}(q)\) invertible choices. If \(a=0=z\), the prescribed image is zero, impossible for invertible \(M\). Thus the count depends only on whether \(\alpha\cdot\beta\) vanishes, with the stated two nonzero cases.

**The symmetric-matrix count.** Partition all invertible symmetric matrices according to whether their first diagonal entry is nonzero. There are \((q-1)q^{d-1}S_{d-1}(q)\) of the first type, by the first Schur-complement argument. In the zero-diagonal case the remaining prescribed first-column vector can be any of \(q^{d-1}-1\) nonzero vectors, each allowing \(q^{d-1}S_{d-2}(q)\) completions. Therefore
\[
S_d(q)=(q-1)q^{d-1}S_{d-1}(q)+(q^{d-1}-1)q^{d-1}S_{d-2}(q),
\]
with \(S_0(q)=1\) and \(S_1(q)=q-1\). Substitution verifies the displayed closed forms inductively for every prime power, including even characteristic.

**Multiplicities, kernel, and stability.** There are \(q^d-1\) choices of nonzero \(\beta\). For each one, \(\alpha\cdot\beta=0\) holds for exactly \(q^{d-1}\) vectors, of which one is zero. The remaining nonorthogonal \(\alpha\)'s number \((q-1)q^{d-1}\). The two one-zero sectors each have \(q^d-1\) vectors. This gives every multiplicity and the exact rank. Fourier inversion identifies their direct sum as the displayed additive-separable kernel; the sum-zero normalization makes its representation unique.

The count formulas give
\[
\frac{q^{d-1}S_{d-2}(q)}{S_{d-1}(q)}
=\begin{cases}1,&d\text{ odd},\\(1-q^{1-d})^{-1},&d\text{ even}.
\end{cases}
\]
Hence for odd \(d\) the two mixed sectors have identical squared singular values, and for even \(d\) their ratio is \((1-q^{1-d})^{-1}\). The constant squared singular value dominates both mixed sectors. Using additionally
\[
\frac{S_d(q)}{S_{d-1}(q)}
=\begin{cases}q^d-1,&d\text{ odd},\\q^d,&d\text{ even},\end{cases}
\]
proves the two full-visible condition numbers. All inequalities are strict where claimed. The Moore–Penrose inverse is explicitly \((R^*R)^\dagger R^*\): its Fourier coefficients vanish on the kernel and equal the corresponding coefficients of \(R^*\) divided by the positive eigenvalues above. This is exact for every \(d\ge2\).

## Verification
The standalone `checker.py` uses exact modular symmetric-matrix enumeration and a separate incidence-matrix construction. It verifies the full numerical Fourier eigensystem for \((q,d)=(2,2),(2,3),(3,2)\); checks all frequency image counts by enumeration for \((q,d)=(2,4),(3,3)\); and checks the closed-form recurrence and parity ratios algebraically for seven small prime-power orders and dimensions through seven. Successful execution prints `NONSINGULAR_SYMMETRIC_LAGRANGIAN_RADON_CHECKS_PASS`. It uses Python 3 with NumPy. These computations corroborate the finite examples and do not constitute the all-dimensional proof, which is the preceding argument.

## Relationship to prior work
Brent and McKay study the enumeration of invertible symmetric matrices by symmetric Gaussian elimination. The present count \(S_d(q)\) is classical; the additional prescribed-vector count and its use in the **partial finite-field Lagrangian Radon spectrum** are the substantive steps here. Koh studies finite-field X-ray and Radon transforms and sharp endpoint estimates for full direction families, not the present restricted direction set. Marmo, Michor and Neretin treat the Lagrangian Radon transform with all affine Lagrangian planes in real symplectic space; the different field and restricted direction family do not imply the finite counting and parity statements. The finite Radon-transform Fourier literature also contains general Fourier diagonalization methods, which are acknowledged as a standard ingredient. No claim is made that Fourier-slice theory or symmetric-matrix enumeration is new.

## Limitations
The result concerns only **all** invertible symmetric graph directions and **all** their translates, not arbitrary direction subsets, noisy or missing individual measurements, or Lagrangian planes not transverse to the two selected polarizations. The full transform is never injective on all functions; only the mixed-coordinate component and constants are recoverable. The condition numbers refer to counting-measure \(\ell^2\) norms and are not normalized by the number of views. The results do not give a nonlinear phase-retrieval theorem. Historical priority cannot be certified from a bounded literature search, and independent review has not been performed. Scarabotti's closely related finite Radon Fourier decomposition was identified by abstract but a complete accessible text was not obtained; possible broader implicit coverage remains a concrete priority risk.

## References
1. R. P. Brent and B. D. McKay, *On determinants of random symmetric matrices over Z_m*, arXiv:1004.5440v1, first public 2010-04-30. https://arxiv.org/abs/1004.5440
2. D. Koh, *Sharp endpoint estimates for the X-ray transform and the Radon transform in finite fields*, arXiv:1209.1215v1, first public 2012-09-06. https://arxiv.org/abs/1209.1215
3. G. Marmo, P. Michor and Y. Neretin, *The Lagrangian Radon Transform and the Weil representation*, arXiv:1212.4610v1, first public 2012-12-19. https://arxiv.org/abs/1212.4610
4. F. Scarabotti, *Fourier Analysis of a Class of Finite Radon Transforms*, SIAM Journal on Discrete Mathematics (2003), DOI:10.1137/S0895480102416398. Full text not inspected. https://doi.org/10.1137/S0895480102416398
