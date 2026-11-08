# Two-prime determinant and sharp inversion constant for complementary finite-field sphere filters

## Finding
For every odd prime power \(q=p^e\), every odd integer \(d=2m+1\ge3\), every nondegenerate homogeneous quadratic form \(Q\) on \(V=\mathbb F_q^d\), and every pair of nonzero radii \(a,b\) satisfying \(\eta(ab)=-1\), define the integer matrix \(K\) by
\[
K_{x,y}=\mathbf 1_{\{Q(x-y)=a\}}-\mathbf 1_{\{Q(x-y)=b\}}\qquad(x,y\in V).
\]
Then \(K\) has exact absolute determinant and sharp extreme singular values
\[
\boxed{|\det K|=2^{q^d/p}q^{m q^d}},\qquad
\boxed{\sigma_{\min}(K)=2q^m\sin\!\left(\frac\pi{2p}\right),\quad \sigma_{\max}(K)=2q^m}.
\]
In particular \(K\) is invertible over \(\mathbb Q\), \(\mathbb R\), and \(\mathbb C\), and \(\kappa_2(K)=\csc(\pi/(2p))\); its reduction is invertible over every finite field of characteristic other than \(2\) or \(p\), and singular in these two characteristics.

## Assumptions and scope
Write \(q=p^e\), with \(p\ge3\) prime and \(e\ge1\). Write \(d=2m+1\) with \(m\ge1\). The form is \(Q(x)=x^{\mathsf T} Mx\), with \(M\) an invertible symmetric matrix over \(\mathbb F_q\). Fix \(a,b\in\mathbb F_q^\times\) with quadratic character \(\eta(a)=-\eta(b)\). The matrix is indexed by *all* \(q^d\) spatial points and uses unnormalized sphere indicators and ordinary Euclidean matrix singular values. No division by sphere cardinality occurs. The result is uniform over forms, radii, extension degrees, and all odd dimensions in this domain; no assertion is made for even dimensions, characteristic two, zero radius, or same-character radii.

## Proof
**1. Fourier eigenvalues.** Use \(\psi(u)=\exp(2\pi i\,\operatorname{Tr}_{\mathbb F_q/\mathbb F_p}(u)/p)\), the quadratic character \(\eta\), and the Gauss sum \(G=\sum_{u\ne0}\eta(u)\psi(u)\), for which \(G^2=\eta(-1)q\). Put \(Q^*(\xi)=\xi^{\mathsf T}M^{-1}\xi\). The character \(x\mapsto\psi(\xi\cdot x)\) is an eigenfunction of convolution by a sphere of radius \(r\). Orthogonality of additive characters and diagonalization of the quadratic Gauss sum give its eigenvalue
\[
\lambda_r(\xi)=q^{d-1}\mathbf1_{\{\xi=0\}}+
q^{-1}\eta(\det M)G^d \sum_{t\in\mathbb F_q^\times}\eta(t)
\psi\!\left(-rt-\frac{Q^*(\xi)}{4t}\right).
\tag{1}
\]
Every factor follows by completing the square in \(tQ(x)-\xi\cdot x\); the \(t=0\) contribution is \(q^{d-1}\mathbf1_{\{\xi=0\}}\).

**2. Salié evaluation.** For \(B\ne0\), the elementary quadratic Salié identity is
\[
\sum_{t\ne0}\eta(t)\psi(At+B/t)=\eta(B)G\sum_{v^2=4AB}\psi(v).
\tag{2}
\]
For completeness, take the additive Fourier transform in \(A\). The left side transforms to \(q\eta(u)\psi(B/u)\) when \(u\ne0\), and to zero when \(u=0\). On the right side, the constraint forces \(A=v^2/(4B)\), so its Fourier transform for \(u\ne0\) becomes
\[
\eta(B)G\sum_{v\in\mathbb F_q}\psi\left(v-\frac{uv^2}{4B}\right)
=\eta(B)G^2\eta\left(-\frac{u}{4B}\right)\psi(B/u)
=q\eta(u)\psi(B/u).
\]
For \(u=0\), the right transform is \(\eta(B)G\sum_v\psi(v)=0\). Fourier inversion proves (2), including \(A=0\) and every odd prime power.

Set \(C_Q=\eta((-1)^m\det M)\), and write \(s=Q^*(\xi)\). For \(s=0\), (1) and the Gauss identity imply
\[
\lambda_r(\xi)=q^{d-1}\mathbf1_{\{\xi=0\}}+C_Q\eta(r)q^m.
\tag{3}
\]
For \(s\ne0\), applying (2) with \(A=-r\) and \(B=-s/4\) gives
\[
\lambda_r(\xi)=
\begin{cases}
C_Q\eta(s)q^m\big(\psi(v)+\psi(-v)\big),&v^2=rs\ne0\text{ is solvable},\\
0,&\eta(rs)=-1.
\end{cases}
\tag{4}
\]
The two choices of \(v\) give the same value. Exactly one of the two radii \(a,b\) is active in (4) for each \(s\ne0\), because their quadratic characters are opposite. By (3), their difference on the \(s=0\) modes is \(\pm2q^m\). In particular every mode is nonzero: \(\psi(v)+\psi(-v)=2\cos(2\pi\operatorname{Tr}(v)/p)\ne0\) because \(p\) is odd.

**3. Multiplicities and the cyclotomic product.** For each \(s\ne0\), apply additive-character orthogonality to the equation \(Q^*(\xi)=s\), diagonalize its quadratic Gauss sums, and evaluate \(\sum_{t\ne0}\eta(t)\psi(-ts)=\eta(-s)G\). This gives the number of frequencies on the dual sphere:
\[
N(s)=\#\{\xi:Q^*(\xi)=s\}=q^{d-1}+C_Q\eta(s)q^m,
\qquad N(0)=q^{d-1}.
\tag{5}
\]
Here \(\eta(\det M^{-1})=\eta(\det M)\), so the same \(C_Q\) appears. Consequently the constant multiplicities for the two opposing square classes satisfy \(N_a+N_b=2q^{d-1}\), where \(N_r=q^{d-1}+C_Q\eta(r)q^m\). Let \(P\) be the product of \(|\psi(v)+\psi(-v)|\) over all unordered nonzero pairs \(\{v,-v\}\subset\mathbb F_q\). As the trace map is surjective, each element of \(\mathbb F_p\) has \(q/p\) preimages. With \(\zeta=\exp(2\pi i/p)\),
\[
2P^2=\prod_{v\in\mathbb F_q}\big(\psi(v)+\psi(-v)\big)
=\left(\prod_{t\in\mathbb F_p}(\zeta^t+\zeta^{-t})\right)^{q/p}=2^{q/p}.
\tag{6}
\]
Indeed \(\prod_{t\in\mathbb F_p}(\zeta^t+\zeta^{-t})=\prod_t(1+\zeta^{2t})=2\), obtained by evaluating \(X^p-1\) at \(X=-1\). Thus \(P=2^{(q/p-1)/2}\). Each radius class traverses all unordered nonzero \(\{v,-v\}\) once as \(s=v^2/r\) varies; (5) makes the frequency multiplicity constant on that class. The \(q^{d-1}\) zero-dual-radius eigenvalues supply a factor \((2q^m)^{q^{d-1}}\). The remaining modes supply \(q^{m(q^d-q^{d-1})}P^{N_a+N_b}\). Hence
\[
|\det K|=q^{m q^d}2^{q^{d-1}}\left(2^{(q/p-1)/2}\right)^{2q^{d-1}}
=q^{m q^d}2^{q^d/p}.
\]
Because \(K\) has integer entries, the determinant formula also proves exactly which prime characteristics yield an invertible reduction.

**4. Sharp singular-value bounds.** The Fourier characters form an orthogonal basis; \(K\) is real symmetric, and its singular values are absolute values of the differences in (3) and (4). Each is at most \(2q^m\), and the bound is attained on the zero-dual-radius modes. For every nonzero \(v\in\mathbb F_q\), the nonzero value \(v^2/a\) is represented by \(Q^*\) in dimension at least three: a nondegenerate quadratic form in at least three variables over an odd finite field contains a hyperbolic plane (existence of a nonzero isotropic vector follows, for example, from the quadratic Chevalley–Warning count), and such a plane represents every scalar. Therefore every value \(2q^m|\cos(2\pi t/p)|\) with \(t\ne0\) occurs among the singular values: choose nonzero \(v\) with \(\operatorname{Tr}(v)=t\) and realize \(v^2/a\) as the dual norm. The largest value \(2q^m\) occurs independently on the zero-dual-radius modes. Among integer residues \(t\), the minimum absolute cosine is \(\sin(\pi/(2p))\) and its maximum is one. This proves the exact extremes and condition number. \(\square\)

## Verification
The standalone Python checker `CHECK.py` uses integer fraction-free elimination to verify the complete \(27\times27\) and \(125\times125\) determinants exactly in dimensions three over \(\mathbb F_3\) and \(\mathbb F_5\). Independently, it directly evaluates all Fourier eigenvalues and checks predicted extreme singular values and logarithmic determinant for \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\), plus a form with nonsquare discriminant. A direct \(729\)-frequency test over \(\mathbb F_9\) checks two quadratic forms and both claimed scalar identities. These are finite consistency checks; the unrestricted theorem follows from steps (1)–(6).

## Relationship to prior work
Pham and Xue (2026) prove sharp sphere Fourier-extension estimates in odd-dimensional finite fields, with separate quadratic-character cases. Iosevich and Koh (2007) develop the explicit spherical Fourier-transform formula underlying (1). Brittenham and Pakianathan (2024) study individual distance-graph adjacency spectra, the Euclidean association scheme, and its Kloosterman sums. These important prior works provide the Fourier and association-scheme context. The assertion here is different: an explicit arithmetic determinant, prime-divisor rigidity, and a sharp, dimension-uniform inversion condition number for the **signed difference of two complementary sphere convolutions**. The cited individual spectral formulas are not themselves claimed new.

## Limitations
This is a statement about the unnormalized signed adjacency difference, not about either individual sphere's conditioning or about an arbitrary linear combination. No claim is made for characteristic two, even ambient dimension, radius zero, or equal quadratic classes. Exact publication priority for this particular determinant and condition-number identity has not been independently established; it may have a previously unnoticed equivalent in association-scheme or Salié-sum literature. Neither the numerical tests nor the successful search establishes novelty by itself.

## References
1. Thang Pham and Boqing Xue, *Sharp spherical \(L^p\to L^4\) extension estimates over finite fields in odd dimensions* (2026), arXiv:2610.29664, https://arxiv.org/abs/2610.29664.
2. Charles Brittenham and Jonathan Pakianathan, *Random walks and the “Euclidean” association scheme in finite vector spaces*, Canadian Journal of Mathematics (first online 2024), https://doi.org/10.4153/S0008414X24000518.
3. Alex Iosevich and Doowon Koh, *Extension Theorems for Spheres in the Finite Field Setting* (2007 preprint), arXiv:0712.1627, https://arxiv.org/abs/0712.1627.
