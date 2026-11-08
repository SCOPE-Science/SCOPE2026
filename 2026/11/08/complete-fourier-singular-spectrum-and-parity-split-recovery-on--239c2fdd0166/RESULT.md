# Complete Fourier singular spectrum and parity-split recovery on an affine Veronese slice

## Finding
Let \(q\) be any prime power and \(d\ge1\), and let \(G\) be the additive group of symmetric \((d+1)\)-by-\((d+1)\) matrices over \(\mathbb F_q\). Put
\[
S=\{vv^{\mathsf T}:v=(1,w),\ w\in\mathbb F_q^d\},\qquad
(Tf)(X)=\sum_{Y\in S}f(X+Y).
\]
Thus \(S\) is precisely the rank-one symmetric affine slice with upper-left entry equal to one, and \(|S|=q^d\). Define the Gaussian coefficient \({d\brack r}_q=\prod_{j=0}^{r-1}(q^{d-j}-1)/(q^{r-j}-1)\), with empty products equal to one. Define
\[
U_{2k}(q)=q^{k(k+1)}\prod_{j=1}^{k}(q^{2j-1}-1),\qquad
U_{2k+1}(q)=q^{k(k+1)}\prod_{j=1}^{k+1}(q^{2j-1}-1),
\]
and \(V_{2s}(q)=q^{s(s-1)}\prod_{j=1}^{s}(q^{2j-1}-1)\). The complete **positive** singular-value multiset of \(T\), with no unlisted positive singular values, is:

* If \(q\) is odd, for every \(0\le r\le d\),
\[
\sigma_r=q^{d-r/2},\qquad M_r=q^{r+1}{d\brack r}_q U_r(q).
\]
* If \(q\) is even, for every \(0\le s\le\lfloor d/2\rfloor\),
\[
\sigma_{2s}=q^{d-s},\qquad M_{2s}=q^{d+2s+1}{d\brack 2s}_q V_{2s}(q).
\]

Here \(M_r\) is the multiplicity. The remaining \(q^{(d+1)(d+2)/2}-\sum M_r\) singular values are zero. Every listed level occurs, and \(T\) is non-invertible for all \(d\ge1\). Its condition number on the orthogonal complement of its kernel is exactly \(q^{d/2}\) for odd \(q\) and \(q^{\lfloor d/2\rfloor}\) for even \(q\).

There is also a sharp, characteristic-sensitive limiting law for the fraction \(\delta_{q,d}=\operatorname{rank}(T)/|G|\) of recoverable Fourier modes. If \(q\) is odd, then
\[
\lim_{d\to\infty}\delta_{q,d}=\frac{q}{q+1}.
\]
If \(q\) is even, write \(A_q=\prod_{j=1}^{\infty}(1-q^{-j})\) and \(O_q=\prod_{j=1}^{\infty}(1-q^{-(2j-1)})\). Then
\[
\lim_{k\to\infty}\delta_{q,2k}=\frac{1+A_qO_q}{2},\qquad
\lim_{k\to\infty}\delta_{q,2k+1}=\frac{1-A_qO_q}{2}.
\]
The two limits are strictly distinct because both infinite products are positive. In particular, recoverability oscillates with ambient dimension in characteristic two, whereas it converges without parity separation in odd characteristic.

## Assumptions and scope
The ambient group is \(G=\operatorname{Sym}_{d+1}(\mathbb F_q)\) under addition. Its characters are \(X\mapsto\psi(\sum_{0\le i\le j\le d}b_{ij}X_{ij})\), where \(\psi\) is any fixed nontrivial additive character of \(\mathbb F_q\) and the \(b_{ij}\) are arbitrary elements of \(\mathbb F_q\). This **coordinate pairing**, rather than the matrix-trace pairing, is essential in characteristic two. No restriction is imposed on the field extension degree. Singular values refer to the unnormalized convolution \(T\) on \(\ell^2(G)\); for averaging by \(q^{-d}T\), divide every listed singular value by \(q^d\). The result classifies the recoverable subspace of a singular operator, not full inversion.

## Proof
**1. Affine parametrization.** For \(w=(w_1,\ldots,w_d)\), the symmetric matrix \((1,w)(1,w)^{\mathsf T}\) has \(X_{00}=1\), \(X_{0i}=w_i\), and \(X_{ij}=w_iw_j\). Conversely, any symmetric rank-one \(X\) with \(X_{00}=1\) satisfies \(X_{ij}=X_{i0}X_{0j}\), so the parametrization is bijective, even in characteristic two. The Fourier eigenvalue of \(T\) at coefficients \((a,b,c)\) therefore equals
\[
\Lambda(a,b,c)=\psi(a)\sum_{w\in\mathbb F_q^d}\psi(Q_c(w)+L_b(w)),
\quad Q_c(w)=\sum_{i\le j}c_{ij}w_iw_j,\quad L_b(w)=\sum_i b_iw_i.
\]

**2. The exact quadratic-sum criterion.** Let \(\mathcal B_Q(w,z)=Q(w+z)-Q(w)-Q(z)\) be the polar form, and let \(R\) be its radical of dimension \(t=d-r\). The change of variables \(z=y-w\) in the squared absolute value gives the identity
\[
\left|\sum_w\psi(Q(w)+L(w))\right|^2
=q^d\sum_{z\in R}\psi(Q(z)+L(z)).
\]
Indeed, the inner sum over \(w\) is \(q^d\) if \(z\in R\) and zero otherwise. The map \(z\mapsto\psi(Q(z)+L(z))\) restricts to an additive character on \(R\), because \(\mathcal B_Q\) vanishes there. Consequently its sum is either zero or \(|R|=q^t\). The absolute value of the original sum is therefore precisely zero or \(q^{d-r/2}\).

For fixed \(Q\), exactly \(q^r\) of the \(q^d\) linear forms \(L\) yield the nonzero alternative. To see this without assuming odd characteristic, the assignment \(L|_R\mapsto\psi\circ L|_R\) is a bijection from the \(q^t\) field-linear functionals on \(R\) onto its \(q^t\) additive characters: injectivity follows since a nonzero field-linear functional has image all of \(\mathbb F_q\), and \(\psi\) is nontrivial. The fixed character \(\psi\circ Q|_R\) therefore has exactly one cancelling restriction; there are \(q^{d-t}=q^r\) extensions. The independent constant coefficient \(a\) supplies another factor of \(q\).

**3. Rank census, odd characteristic.** When \(q\) is odd, the correspondence \(Q\mapsto\mathcal B_Q\) is a bijection between homogeneous quadratic forms and symmetric bilinear forms. For a form of rank \(r\), choose its radical of dimension \(d-r\) in \({d\brack r}_q\) ways and a nondegenerate form on the quotient in \(U_r(q)\) ways. The displayed products for \(U_r\) follow by the standard general linear/orthogonal orbit-stabilizer count (equivalently, Gaussian elimination by rank and type). Multiplying by the \(q^{r+1}\) compatible linear and constant coefficients proves the odd-characteristic multiplicities.

**4. Rank census, characteristic two.** The polar form of a homogeneous quadratic form is alternating and therefore has even rank \(2s\). The number of alternating forms with rank \(2s\) is \({d\brack2s}_q V_{2s}(q)\). This follows by choosing the radical and then using \(|\mathrm{GL}_{2s}(q)|/|\mathrm{Sp}_{2s}(q)|=V_{2s}(q)\) to count nonsingular alternating forms. For a fixed alternating polar form, all \(d\) square-term coefficients of the quadratic form are free, giving exactly \(q^d\) quadratic forms with that polar form. The factors \(q^{2s}\) and \(q\) from Step 2 give the stated even-characteristic multiplicities. In particular, the missing odd-rank bands are forced structurally, not an artefact of cancellation.

**5. Exact nullity and condition number.** The characters are a complete orthogonal basis of \(\ell^2(G)\); convolution is diagonal in that basis, and its singular values are the eigenvalue moduli in Step 2. The formulas count every possible quadratic form and compatible affine term, so all remaining characters lie in the kernel. In both characteristics there are incompatible affine terms for \(d\ge1\), so the kernel is nontrivial. The largest singular value occurs at rank zero and equals \(q^d\). The smallest positive value occurs at the largest possible polar rank, namely \(d\) in odd characteristic and \(2\lfloor d/2\rfloor\) in characteristic two; this gives the sharp condition numbers.

**6. Limit in odd characteristic.** Put \(u=q^{-1}\), \(E_t=\prod_{j=1}^t(1-u^j)\), and \(O_q=\prod_{j\ge1}(1-u^{2j-1})\). For a uniformly random homogeneous quadratic form on \(\mathbb F_q^d\), let \(t\) be the nullity of its polar form. Its probability is
\[
\Pr_d(t)=u^{t(t+1)/2}
\frac{\prod_{j=d-t+1}^{d}(1-u^j)}{E_t}
\prod_{j=1}^{\lceil(d-t)/2\rceil}(1-u^{2j-1}).
\]
For fixed \(t\), this converges to \(O_qu^{t(t+1)/2}/E_t\). A form of nullity \(t\) has a fraction \(u^t\) of compatible linear terms. Since these probabilities have uniform superexponentially small tails, dominated convergence applies. The elementary Euler product identity
\[
\sum_{t\ge0}\frac{u^{t(t-1)/2}z^t}{E_t}=\prod_{j\ge0}(1+zu^j)
\]
gives \(\lim\delta_{q,d}=O_q\prod_{j\ge2}(1+u^j)=(1-u)/(1-u^2)=q/(q+1)\).

**7. Two limits in characteristic two.** For a uniformly random alternating polar form, its nullity \(t\) has the same parity as \(d\) and its exact probability is
\[
\Pr_d(t)=u^{t(t-1)/2}
\frac{\prod_{j=t+1}^{d}(1-u^j)}{\prod_{j=1}^{(d-t)/2}(1-u^{2j})}.
\]
For each fixed \(t\) along the appropriate parity, this tends to \(O_qu^{t(t-1)/2}/E_t\). After multiplying by the compatible-linear-term fraction \(u^t\), the even- and odd-\(t\) limiting sums have sum \(O_q\prod_{j\ge1}(1+u^j)=1\) and difference \(O_q\prod_{j\ge1}(1-u^j)=O_qA_q\), by Euler's identity with \(z=\pm u\). Solving gives the displayed two limits. The same superexponential tail bound justifies passage to the limit; all Euler products are positive for \(0<u<1\).

## Verification
The standalone script `verify_stdlib.py` uses only Python's standard library. It constructs finite-field arithmetic (including extensions of degrees two and three), enumerates **every** character of \(G\) for thirteen small parameter choices, evaluates each Fourier coefficient directly from the \(q^d\)-point slice, and checks the claimed multiplicities, zero counts, spectral levels, and Parseval identity. The verified parameters include \(q=2\) with \(d\le4\), \(q=3\) with \(d\le3\), \(q=5\) with \(d\le2\), \(q=4\) with \(d\le2\), and one-dimensional examples over \(\mathbb F_8\) and \(\mathbb F_9\). It additionally checks finite-dimensional rank fractions against the asserted limits. Run `python3 verify_stdlib.py` from a directory containing the script. Fourier exponentials are evaluated numerically, while field operations and predicted multiplicities are exact integers. This finite verification is supplementary to the proof.

## Relationship to prior work
The general Fourier diagonalization of translation operators and quadratic Gauss-sum magnitudes are classical. Schmidt's 2014 analysis of symmetric bilinear forms and 2018 generalization to all characteristics develop much broader association-scheme rank and character-sum machinery. They are not credited here as proving the present affine-slice singular multiplicities or their dimension-parity Euler-product limits. The present set fixes one rank-one matrix coordinate and is not an entire general-linear rank orbit. Published Fourier frame work on the full Veronese cone likewise treats restriction of selected characters, not convolution by this fixed affine rank-one slice. A separate exact convolution classification for normalized rectangular rank-one matrices concerns bilinear rather than quadratic sums and does not yield the characteristic-two alternation. These comparisons limit the claim to the stated sliced operator; no priority claim is made for the underlying Gaussian-sum facts.

## Limitations
The assertion is about **singular values** and rank; the complete complex eigenvalue phase distribution in odd characteristic is not classified. The operator is never fully invertible. The asymptotic formulas keep \(q\) fixed while \(d\to\infty\), and do not address simultaneous growth of dimension and field size. The new synthesis uses established quadratic-form enumeration and Gauss-sum machinery; an undiscovered explicit specialization or a stronger published formula might subsume the classification. The checker is finite and does not supply an independent proof or historical priority certification.

## References
1. K.-U. Schmidt, *Symmetric bilinear forms over finite fields with applications to coding theory*, arXiv:1410.7184v1, first submitted 2014-10-27, https://arxiv.org/abs/1410.7184.
2. K.-U. Schmidt, *Quadratic and symmetric bilinear forms over finite fields and their association schemes*, arXiv:1803.04274v1, first submitted 2018-03-12, https://arxiv.org/abs/1803.04274.
3. Standard finite-field orthogonal and symplectic orbit counts and Euler's finite \(q\)-binomial theorem are used explicitly in the proof above; no new theorem about these ingredients is asserted.
