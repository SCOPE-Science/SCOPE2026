# Arithmetic nullities of principal Fourier sampling on two finite-field lines

## Finding
Fix a prime power \(q\), the field \(\mathbb F_q\), a nontrivial complex additive character \(\psi:\mathbb F_q\to\mathbb C\), and two linearly independent vectors \(u,v\in\mathbb F_q^2\). Write \(L_u=\{tu:t\in\mathbb F_q\}\), \(L_v=\{tv:t\in\mathbb F_q\}\), and \(E=L_u\cup L_v\), which has \(2q-1\) points. Consider the square principal Fourier matrix
\[
M_E=\bigl(\psi(x\cdot y)\bigr)_{x,y\in E},\qquad x\cdot y=x_1y_1+x_2y_2.
\]
Set \(A=u\cdot u\), \(B=v\cdot v\), and \(C=u\cdot v\). If \(ABC=0\), then \(M_E\) is nonsingular. Otherwise put \(\rho=C^2/(AB)\). The identity \(AB-C^2=\det[u,v]^2\ne0\) shows \(\rho\ne1\). If \(m\) is the multiplicative order of \(\rho\) in \(\mathbb F_q^\times\), then
\[
\boxed{\dim_{\mathbb C}\ker M_E=\frac{q-1}{m},\qquad
\operatorname{rank}_{\mathbb C}M_E=2q-1-\frac{q-1}{m}.}
\]
These statements hold in both odd and even characteristic, for every nontrivial additive character, and are invariant under rescaling either line generator. In particular, a nonorthogonal pair of nonisotropic lines always has a singular self-sampling Fourier matrix, while an orthogonal pair or any pair containing an isotropic line has a nonsingular one.

## Assumptions and scope
A field of characteristic \(p\) has \(q=p^r\) elements with \(r\ge1\). The dot product is the standard nondegenerate symmetric bilinear form, not an anisotropic Hermitian form. Two lines are distinct one-dimensional linear subspaces through the origin. The character \(\psi\) is any nontrivial additive homomorphism into the unit circle. The matrix uses the *same* set \(E\) as its row- and column-indexing set, including the intersection point exactly once. The rank and nullity are over \(\mathbb C\). The value \(m\) is defined only when \(A,B,C\ne0\). No statement about affine translates, more than two lines, or arbitrary different row and column sets is made.

## Proof
**Step 1: Encode the union without double-counting.** Let \(f:E\to\mathbb C\). Define functions \(h_1,h_2:\mathbb F_q\to\mathbb C\) by \(h_1(t)=f(tu)\) for all \(t\), by \(h_2(t)=f(tv)\) for nonzero \(t\), and by \(h_2(0)=0\). This defines a linear bijection between functions on \(E\) and pairs \((h_1,h_2)\) satisfying \(h_2(0)=0\).

Write the one-dimensional additive Fourier transforms \(H_j(z)=\sum_{t\in\mathbb F_q}h_j(t)\psi(zt)\). For any \(x\in\mathbb F_q^2\), the Fourier transform of \(f\) evaluated at \(x\) is \(H_1(x\cdot u)+H_2(x\cdot v)\). Thus \(M_E f=0\) is equivalent to the following two identities for *every* \(a\in\mathbb F_q\):
\[
H_1(Aa)+H_2(Ca)=0,\qquad
H_1(Ca)+H_2(Ba)=0. \tag{1}
\]
The character may have a nontrivial additive-field trace kernel, but additive Fourier inversion still holds and is the only fact about \(\psi\) required.

**Step 2: Remove degenerate bilinear pairings.** The Gram determinant satisfies
\[
AB-C^2=(u_1v_2-u_2v_1)^2\ne0, \tag{2}
\]
including characteristic two. If \(C=0\), then \(A\) and \(B\) are nonzero. From (1), \(H_1\) and \(H_2\) are constant functions. Fourier inversion gives \(h_2(0)=q^{-1}\sum_z H_2(z)=0\), so \(H_2=0\), then \(H_1=0\). If \(C\ne0\) and \(A=0\), the first equation in (1) makes \(H_2\) constant. The same origin constraint forces \(H_2=0\), and the second equation then forces \(H_1=0\). If \(C\ne0\) and \(B=0\), the second equation makes \(H_1\) constant; the first makes \(H_2\) constant, hence both vanish. Thus \(ABC=0\) implies trivial kernel.

**Step 3: Reduce the nondegenerate case to multiplicative orbits.** Suppose \(A,B,C\ne0\). From the first equation of (1), for all \(z\in\mathbb F_q\),
\[
H_1(z)=-H_2\bigl((C/A)z\bigr). \tag{3}
\]
Insert (3) into the second equation, and reparameterize its variable using \(B\ne0\). One obtains
\[
H_2(\rho z)=H_2(z)\quad\hbox{for all }z\in\mathbb F_q,
\qquad \rho=\frac{C^2}{AB}. \tag{4}
\]
Conversely, any function \(H_2\) satisfying (4), together with \(H_1\) defined by (3), satisfies both equations in (1). Fourier inversion takes this pair to \((h_1,h_2)\). By inversion, the requirement \(h_2(0)=0\) is exactly
\[
\sum_{z\in\mathbb F_q} H_2(z)=0. \tag{5}
\]
Because \(u,v\) are independent, (2) implies \(\rho\ne1\); also \(\rho\ne0\). The group \(\langle\rho\rangle\) has order \(m\), and its multiplication action partitions \(\mathbb F_q^\times\) into precisely \((q-1)/m\) orbits, each of cardinality \(m\). Equation (4) says that \(H_2\) is arbitrary and constant on each such orbit, while its value at zero is another free scalar. Equation (5) is one independent linear equation, uniquely determining that zero value from the orbit constants. Therefore the solution space has dimension \((q-1)/m\). The correspondence through (3) and Fourier inversion is injective, proving the rank formula.

**Step 4: Eliminate dependence on chosen generators.** If \(u\) is replaced by \(\alpha u\) and \(v\) by \(\beta v\), where \(\alpha,\beta\in\mathbb F_q^\times\), then \(A\) is multiplied by \(\alpha^2\), \(B\) by \(\beta^2\), and \(C\) by \(\alpha\beta\). Thus the zero/nonzero cases and \(\rho=C^2/(AB)\) are unchanged. The geometric statement depends only on the two lines, not on their parametrization. \(\square\)

## Verification
A standalone, pure-Python exact-arithmetic checker is included as `two_line_fourier_checker.py`. Run `python3 two_line_fourier_checker.py` with Python 3.8 or newer; it requires no third-party packages. It constructs explicit line unions and their Fourier matrices over finite fields of orders \(2,3,4,5,7,8,9,11,13,16\), then computes exact matrix ranks in auxiliary prime fields containing the relevant roots of unity. It checks every unordered pair of distinct lines, \(436\) pairs in total, against the proven order formula. The checker exercises nonzero isotropic and orthogonal pairings, odd- and even-characteristic fields, prime and extension fields, and the arithmetic resonance cases.

Reduction modulo an auxiliary prime is **only a consistency check**, not a substitute for the complex-rank proof: modular ranks can differ from complex ranks. The proof above uses characteristic-zero additive Fourier inversion and exact algebra over \(\mathbb F_q\), valid for all prime powers without any finite-search assumption. The checker may be rerun from the enclosed source; expected output ends with `PASS`.

## Relationship to prior work
Bonami and Ghobber (arXiv:1003.5060, first posted 2010-03-26) analyze equality cases of Fourier uncertainty on finite abelian groups and finite-field plane structures, providing relevant context but not, in the inspected complete text, this two-line self-indexed principal-minor nullity formula. Biswas, Dasgupta, Jacob, and Mudumbai (EUSIPCO 2015) analyze spark under two-dimensional Fourier sampling; their inspected full conference paper treats rectangular sampling patterns and line-selected rows against a full ambient collection of columns, rather than the same union of two intersecting lines on both sides. Closest indexed related research includes a graph-theoretic criterion for *basis partners* of a distinct two-line-plus-one-point support and exact arithmetic nullities for two-view sampling of finite conics. Neither abstract statement implies the explicit order-of-\(\rho\) self-sampling classification proved here. The latter indexed reports were available only in short summaries, not full text; see limitations.

## Limitations
The mathematical result concerns only unions of two distinct one-dimensional *linear* subspaces in \(\mathbb F_q^2\), sampled on themselves with the standard dot-product pairing. It does not classify affine-shifted configurations, arbitrary bilinear forms, unequal row/column patterns, or unions of three or more lines. The numerical tests cover ten small finite fields but cannot verify the infinite classification independently. The originality assessment is bounded by inspected literature and accessible indexed summaries; equivalent forms in older finite-plane spectral-set literature or inaccessible full papers remain a residual risk. Independent mathematical audit and validation have not been performed.

## References
1. A. Bonami and S. Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060v1 (first public posting 2010-03-26), https://arxiv.org/abs/1003.5060.
2. A. Biswas, A. Dasgupta, M. Jacob, and R. Mudumbai, *Spark Under 2-D Fourier Sampling*, EUSIPCO (2015), DOI:10.1109/EUSIPCO.2015.7362899.
3. Related indexed finding, *A unicyclic graph criterion for basis partners of the two-line Riesz family*, identifier `2026/10/4/SCOPE-a-unicyclic-graph-criterion-for-basis-partners-of-the-two-line-r--6ede33f195c7`; full text not inspected.
4. Related indexed finding, *Exact arithmetic nullities in two-view Fourier tomography of finite-field conics*, identifier `2026/10/11/SCOPE-exact-arithmetic-nullities-in-two-view-fourier-tomography-of-fin--75a75df79dd1`; full text not inspected.
