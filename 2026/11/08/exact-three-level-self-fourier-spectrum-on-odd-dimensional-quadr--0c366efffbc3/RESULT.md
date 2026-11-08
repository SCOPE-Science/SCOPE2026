# Exact three-level self-Fourier spectrum on odd-dimensional quadratic cones

## Finding
For every odd prime power \(q\), integer \(m\ge 1\), scalar \(a\in\mathbb F_q^\times\), and nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C^\times\), put
\[
V=\mathbb F_q^{2m+1},\qquad Q(u_1,v_1,\ldots,u_m,v_m,w)=\sum_{j=1}^{m}u_jv_j+aw^2,
\]
let \(C=\{x\in V:Q(x)=0\}\) **include the origin**, and let \(B(x,y)=Q(x+y)-Q(x)-Q(y)\). Form the square, unnormalized Fourier matrix
\[
H=\bigl(\psi(B(x,y))\bigr)_{x,y\in C}.
\]
There are \(N=q^{2m}\) rows and columns. Define \(P=(q^{2m}-1)/(q-1)\) and \(r=(q^{2m}-1)/(q^2-1)\). The **entire singular-value multiset** is
\[
\begin{array}{c|c}
\text{Singular value}&\text{Multiplicity}\\\hline
q^{m+1/2}&r\\
q^{m}&N-P\\
q^{m-1/2}&P-r.
\end{array}
\]
In particular, \(H\) is invertible, and its sharp spectral (Euclidean) condition number is \(\kappa_2(H)=q\). Both the singular values and the multiplicities are independent of \(a\) and of the choice of \(\psi\).

## Assumptions and scope
The characteristic of \(\mathbb F_q\) is odd. The underlying vector space has **odd** dimension \(2m+1\ge3\), the quadratic form is nondegenerate and has Witt index \(m\), and the frequency and spatial index sets are *the same complete zero cone*, including its vertex. In odd dimension over a finite field, every nondegenerate quadratic form has the displayed shape for some \(a\ne0\), so this encompasses all such quadratic cones. Here singular values are for the standard unweighted complex \(\ell^2(C)\) norm and the stated unnormalized matrix, not for normalized surface measures.

Write \(\eta:\mathbb F_q\to\{0,\pm1\}\) for the quadratic character, extended by \(\eta(0)=0\). Set \(s=\eta(-a)\). The polar form is
\[
B(x,y)=\sum_{j=1}^m(u_jv_j'+u_j'v_j)+2aww'.
\]

## Proof
**1. Exact cone Fourier coefficient.** For every \(v\in V\), Gaussian summation and additive orthogonality give
\[
\sum_{z\in C}\psi(B(v,z))=q^{2m}\mathbf1_{\{v=0\}}+\eta(a)q^m\eta(Q(v)).\tag{1}
\]
Indeed, writing \(\mathbf1_{Q(z)=0}=q^{-1}\sum_{t\in\mathbb F_q}\psi(tQ(z))\), the \(t=0\) term gives \(q^{2m}\mathbf1_{\{v=0\}}\). For each \(t\ne0\), completing the square contributes \(q^m\eta(ta)G\psi(-Q(v)/t)\), where \(G=\sum_{u\ne0}\eta(u)\psi(u)\). Summing over \(t\ne0\), then using \(G^2=\eta(-1)q\), yields the second term in (1). Taking \(v=0\) also proves \(|C|=q^{2m}\).

**2. Gram reduction.** Define the real symmetric \(N\times N\) matrix \(K\) by \(K_{x,y}=\eta(B(x,y))\). Since \(Q(x-y)=-B(x,y)\) for \(x,y\in C\), equation (1) yields
\[
H^*H=q^{2m}I+s q^m K.\tag{2}
\]

**3. Quadratic-character radial decomposition.** Define \(R_{x,y}=\eta(t)\) when \(x=ty\ne0\) for some unique \(t\in\mathbb F_q^\times\), and \(R_{x,y}=0\) otherwise. Let \(W\) consist of functions on \(C\) satisfying \(f(tx)=\eta(t)f(x)\) for nonzero \(t\), with \(f(0)=0\). Every nonzero cone ray contributes one free coordinate, hence \(\dim W=P\). Directly, \(R\) acts by \(q-1\) on \(W\) and by zero on \(W^\perp\). The matrix \(K\) maps into \(W\) and annihilates \(W^\perp\).

The key exact *quadratic matrix identity* is
\[
K^2=q^{2m-1}(q-1)R+s q^{m-1}(q-1)^2K.\tag{3}
\]
To verify (3), fix \(x,y\in C\). If one is zero, every relevant entry vanishes. If \(x=ty\ne0\), its \((x,y)\) entry on the left equals \(\eta(t)\) times the number of \(z\in C\) for which \(B(y,z)\ne0\). Exactly \(q^{2m-1}\) cone points are orthogonal to the nonzero isotropic \(y\), so that number is \(q^{2m-1}(q-1)\). If \(x,y\) are independent and \(B(x,y)=0\), extend their totally isotropic plane to two hyperbolic pairs. For each prescribed nonzero pair \((B(x,z),B(y,z))=(u,v)\), the number of cone points \(z\) is \(q^{2m-2}\); therefore summing \(\eta(uv)\) gives zero. Finally, if \(b=B(x,y)\ne0\), the plane spanned by \(x,y\) is hyperbolic, and its orthogonal complement is a \((2m-1)\)-dimensional quadratic space with \(m-1\) hyperbolic pairs and anisotropic scalar \(a\). The number of points \(z\) with prescribed \(u=B(x,z)\), \(v=B(y,z)\), and \(Q(z)=0\) is
\[
q^{2m-2}+\eta(a)q^{m-1}\eta(-uv/b).
\]
Multiplying by \(\eta(uv)\) and summing over \(u,v\) gives \(s q^{m-1}(q-1)^2\eta(b)\). These cases prove (3) entrywise. The isotropic hyperplane count and the odd-dimensional quadratic-value count used above follow by the same character-orthogonality calculation as (1), in dimensions \(2m+1\) and \(2m-1\), respectively.

**4. Eigenvalues and multiplicities.** On \(W\), identity (3) is a quadratic equation with two distinct roots
\[
\lambda_A=s q^m(q-1),\qquad \lambda_B=-s q^{m-1}(q-1).
\]
On \(W^\perp\) the eigenvalue is zero. Since \(K_{x,x}=\eta(B(x,x))=\eta(0)=0\), \(\operatorname{tr}K=0\). The multiplicities of \(\lambda_A\) and \(\lambda_B\) thus solve \(n_A+n_B=P\) and \(n_A\lambda_A+n_B\lambda_B=0\), giving \(n_A=P/(q+1)=r\) and \(n_B=P-r\). Substitution into (2) gives Gram eigenvalues \(q^{2m+1}\), \(q^{2m-1}\), and \(q^{2m}\), with the stated multiplicities. Taking square roots finishes the proof; all three numbers are positive.

## Verification
Run `python check_cone.py` with Python 3 and NumPy. The checker constructs the cone, evaluates the polar form and character sums, validates the integer identity (3) and complex Gram identity (2), and compares all singular values with the formula. It passed eleven cases involving prime fields \(q=3,5,7,11\), the extension field \(q=9\), two dimensions \(2m+1=3,5\), and both square and nonsquare \(a\), with several distinct nontrivial additive characters. The largest observed absolute singular-value discrepancy was below \(2\times10^{-13}\). These tests are finite corroboration; the proof above handles every odd prime power and every \(m\ge1\).

## Relationship to prior work
Iosevich and Koh (2008, arXiv:0804.4505v1) develop Fourier extension estimates for **nonzero-level quadratic surfaces** \(Q(x)=j\ne0\). Koh (2012, arXiv:1212.5298v1) studies Fourier restriction inequalities for radial test functions in finite fields. Koh and Yeom (2016, arXiv:1601.07677v1, Lemma 4.1) give the Fourier transform of the **zero cone** and obtain restricted averaging bounds; their odd-dimensional Fourier coefficient is compatible with (1) after normalization and change of quadratic coordinates. The present result does not claim (1) or standard Gauss identities as new. Its distinct conclusion is the complete spectrum and exact conditioning of the operator restricted **on both axes** to that cone, via the signed polar-character identity (3). The checked works do not state this full self-restricted singular spectrum. A broader, unlocated association-scheme theorem may imply part or all of this result; historical priority is not asserted absolutely.

## Limitations
Only odd characteristic, odd ambient dimension, and the full **zero** cone including its vertex are covered. The identity does not directly determine the spectrum when the vertex is removed, for nonzero quadratic levels, or in characteristic two. Nothing is claimed about phase retrieval or optimal nonlinear reconstruction. Finite numerical checks alone do not prove the universal statement. Exhaustive literature priority review and independent mathematical validation are outstanding.

## References
1. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1 (first public version 2008-04-28), https://arxiv.org/abs/0804.4505.
2. D. Koh, *Restriction operators acting on radial functions on vector spaces over finite fields*, arXiv:1212.5298v1 (first public version 2012-12-20), https://arxiv.org/abs/1212.5298.
3. D. Koh and S. Yeom, *Restriction of averaging operators to algebraic varieties over finite fields*, arXiv:1601.07677v1 (first public version 2016-01-28), https://arxiv.org/abs/1601.07677.
