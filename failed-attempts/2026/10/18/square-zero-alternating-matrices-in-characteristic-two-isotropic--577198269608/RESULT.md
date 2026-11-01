# Square-zero alternating matrices in characteristic two: isotropic-image stratification and exact rank counts

## Finding
For an even prime power \(q\) and \(n\ge1\), let \(\mathcal A_n(q)\) be the set of \(n\times n\) matrices over \(\mathbb F_q\) satisfying
\[
X^{\mathsf T}=X,\qquad X_{ii}=0\ (1\le i\le n),\qquad X^2=0.
\]
Set \(I_q(m,t)=0\) for \(t<0\) or \(t>m\), and for \(0\le t\le m\) set
\[
I_q(m,t)=\prod_{j=0}^{t-1}\frac{q^{2(m-j)}-1}{q^{t-j}-1}.
\]
For even \(r=2s\ge0\), put
\[
E_q(r)=q^{s(s-1)}\prod_{i=1}^{s}(q^{2i-1}-1).
\]
The exact rank fibers are
\[
\boxed{\#\{X\in\mathcal A_n(q):\operatorname{rank}X=r\}
=E_q(r)\begin{cases}
I_q((n-1)/2,r),&n\text{ odd},\\
I_q((n-2)/2,r-1)+q^r I_q((n-2)/2,r),&n\text{ even},
\end{cases}}
\]
when \(r\) is even; the count is zero for odd \(r\). The formulas include the zero matrix at \(r=0\). All even ranks \(0,2,\ldots,2\lfloor n/4\rfloor\) occur, and no others.

Beyond counting, there is a canonical bijection between rank-\(r\) matrices in \(\mathcal A_n(q)\) and pairs \((U,\beta)\), where \(U\subseteq\mathbb F_q^n\) is an \(r\)-dimensional totally isotropic subspace for the standard dot product and \(\beta\) is a nonsingular alternating bilinear form on the dual space \(U^*\). For even \(n\), the isotropic-image locus has two geometrically distinct strata, depending on whether \(U\) contains the canonical radical line of the isotropic hyperplane. The two summands in the even-dimensional formula count these strata separately.

For example, in \(\mathbb F_2\), the rank enumerators for sizes \(4,5,6,7,8\) are respectively
\[
1+3T^2,\quad1+15T^2,\quad1+75T^2,\quad1+315T^2,\quad1+1323T^2+3780T^4.
\]

## Assumptions and scope
An alternating matrix means a symmetric matrix **with every diagonal entry zero** in characteristic two. The distinction matters: the equation \(X^{\mathsf T}=-X\) alone would include all symmetric matrices and is not the condition here. Fields have order \(q=2^f\) with \(f\ge1\), and no restrictions are placed on \(n\). The word square-zero means exactly \(X^2=0\), rather than merely nilpotent.

Let \(V=\mathbb F_q^n\) and \(B(v,w)=v^{\mathsf T}w\). Its isotropic-vector hyperplane is \(H=\{v:\sum_i v_i=0\}\), because \(B(v,v)=(\sum_i v_i)^2\). Thus \(B|_H\) is alternating. If \(n=2m+1\) it is nondegenerate symplectic of dimension \(2m\); if \(n=2m+2\) its radical is the line \(R=\langle(1,\ldots,1)\rangle\), and \(H/R\) is nondegenerate symplectic of dimension \(2m\).

## Proof
**Step 1: image–form classification.** For every alternating \(X\), the associated bilinear form \(F_X(v,w)=B(v,Xw)\) is alternating. Symmetry and square-zero give \(B(Xv,Xw)=B(v,X^2w)=0\). Hence \(U=\operatorname{im}X\) is totally isotropic, \(\ker X=U^\perp\), and the induced alternating form \(\beta_X\) on \(V/U^\perp\) is nonsingular. The map \(\rho:V\to U^*\) given by \(\rho(v)(u)=B(v,u)\) is surjective with kernel \(U^\perp\), so \(\beta_X\) is equivalently a nonsingular alternating form on \(U^*\). Consequently \(r=\dim U\) must be even.

Conversely, fix a totally isotropic \(r\)-space \(U\) and a nonsingular alternating form \(\beta\) on \(U^*\). The relation \(B(v,Xw)=\beta(\rho(v),\rho(w))\) defines exactly one \(X\), by nondegeneracy of \(B\). The constructed \(X\) is symmetric with zero diagonal because the right-hand form is alternating; it has kernel \(U^\perp\) because \(\beta\) is nonsingular, image \(U\), and \(X^2=0\) because \(U\subseteq U^\perp\). These constructions are inverse, establishing a genuine bijection, not only an orbit parametrization.

**Step 2: the form factor.** In dimension \(r=2s\), every nonsingular alternating form is congruent to the symplectic form. Its stabilizer under the congruence action of \(\mathrm{GL}_{2s}(\mathbb F_q)\) is \(\mathrm{Sp}_{2s}(\mathbb F_q)\). The orbit–stabilizer ratio is
\[
\frac{|\mathrm{GL}_{2s}(\mathbb F_q)|}{|\mathrm{Sp}_{2s}(\mathbb F_q)|}
=q^{s(s-1)}\prod_{i=1}^{s}(q^{2i-1}-1)=E_q(2s).
\]
This factor is independent of the selected image \(U\).

**Step 3: odd dimension.** When \(n=2m+1\), every totally isotropic \(U\) lies in the symplectic hyperplane \(H\). Counting \(r\)-dimensional totally isotropic subspaces by successively extending ordered isotropic frames, and dividing by ordered bases in an \(r\)-space, gives exactly \(I_q(m,r)\). Multiplying by \(E_q(r)\) proves the first case.

**Step 4: even dimension.** When \(n=2m+2\), the quotient \(H/R\) is symplectic of dimension \(2m\). If \(R\subseteq U\), its image \(U/R\) is an isotropic \((r-1)\)-space in \(H/R\), counted by \(I_q(m,r-1)\), and the inverse image determines \(U\) uniquely. If \(R\not\subseteq U\), projection gives an isotropic \(r\)-space \(W\subseteq H/R\), counted by \(I_q(m,r)\), and \(U\) is the graph of exactly one of \(q^r\) linear maps \(W\to R\). These strata are disjoint and exhaustive. Multiplying their sum by the factor from Step 2 establishes the second case.

**Step 5: sharp rank range.** Both symplectic isotropic-subspace factors are positive exactly on their indicated ranges. For odd \(n=2m+1\), rank \(r\) exists precisely when \(r\) is even and \(r\le m\); for even \(n=2m+2\), precisely when \(r\) is even and \(r\le m+1\). Both bounds are equivalently \(r\le2\lfloor n/4\rfloor\) for even \(r\), proving the full support statement. The bound uses existence of nondegenerate alternating forms in every even dimension.

## Verification
A pure-Python verifier enumerates every alternating matrix over \(\mathbb F_2\) through size six, over \(\mathbb F_4\) through size four, and over \(\mathbb F_8\) through size three, independently testing the matrix square and rank. A separate C++ enumerator checks size seven over \(\mathbb F_2\), size five over \(\mathbb F_4\), and size four over \(\mathbb F_8\). Polynomial-basis finite-field arithmetic is implemented directly; no floating-point approximations are used. Closed-form support is also checked in sizes two through sixteen for all three field orders. See the standalone files `verify.py` and `verify.cpp` and the verification report for exact commands and outputs. Computation does not constitute the proof for arbitrary size.

## Relationship to prior work
Buckhiester (1974) counted fixed-rank rectangular solutions to bilinear Gram-matrix equations over fields of characteristic two and analyzed the hyperplane associated with a nonalternating form. His incidence counts motivate the symplectic image stratification, but the rectangular matrices in that paper are not required to equal their transpose, have zero diagonal, and square to zero simultaneously. Brouwer–Gow–Sheekey (2014), Section 4.4, counted **symmetric nilpotent** matrices of every prescribed Jordan shape; their formulas do not separately impose the zero-diagonal condition, which is a proper extra restriction in characteristic two. Their Section 2 points to earlier counts of nilpotent skew-symmetric matrices of fixed rank (Lusztig, 1976), without restricting the nilpotency exponent to two. Xue's characteristic-two nilpotent-orbit work (arXiv:0808.2995) and the classical alternating-form orbit formula supply broader context. Fulman–Goldstein (2015) address unconstrained random alternating matrices, without the square-zero restriction. The specific joint constraint and its image-stratified rank enumerator are not established by the inspected statements. This is a comparative literature assessment, not a claim of absolute priority.

## Limitations
The theorem concerns even-characteristic finite fields, the *standard* dot product, and matrices required to be both zero-diagonal symmetric and square-zero. It does not count arbitrary symmetric nilpotents, all nilpotent alternating matrices, square-zero matrices without alternation, or similarity classes rather than individual matrices. The complete text of Lusztig's 1976 paper was not obtained; an equivalent count in older orthogonal-Lie-algebra literature is a residual bibliographic risk. No independent mathematical audit is represented by this document.

## References
1. Philip G. Buckhiester, “Rank \(r\) Solutions to the Matrix Equation \(XAX^{\mathsf T}=C\), \(A\) Nonalternate, \(C\) Alternate, over \(GF(2^y)\),” *Canadian Journal of Mathematics* 26 (1974), 78–90. DOI: 10.4153/CJM-1974-008-2.
2. A. E. Brouwer, R. Gow, J. Sheekey, “Counting Symmetric Nilpotent Matrices,” *Electronic Journal of Combinatorics* 21(2) (2014), P2.4. DOI: 10.37236/3810.
3. Ting Xue, “Nilpotent Orbits in Classical Lie Algebras over Finite Fields of Characteristic 2 and the Springer Correspondence,” arXiv:0808.2995v1, 2008-08-21.
4. G. Lusztig, “A Note on Counting Nilpotent Matrices of Fixed Rank,” *Bull. London Math. Soc.* 8 (1976), 77–80. DOI: 10.1112/blms/8.1.77.
5. J. Fulman, L. Goldstein, “Stein’s Method and the Rank Distribution of Random Matrices over Finite Fields,” *Annals of Probability* 43 (2015), 1274–1314. DOI: 10.1214/13-AOP889.
