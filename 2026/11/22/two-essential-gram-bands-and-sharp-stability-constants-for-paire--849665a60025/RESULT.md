# Two essential Gram bands and sharp stability constants for paired Hardy composition operators

## Finding

Let \(H^2=H^2(\mathbb D)\) be the classical Hardy Hilbert space, let \(0<a<1\), and define the disk automorphism \(b_a(z)=(z-a)/(1-az)\), whose inverse is \(b_a^{-1}(z)=(z+a)/(1+az)\). For any \(t\in\mathbb C\), let
\[
T_{a,t}f=f\circ b_a+t\,f\circ(-b_a).
\]
Set
\[
u=|1+t|^2,\quad v=|1-t|^2,\quad
A_a=\frac{1+a^2}{1-a^2},\quad B_a=\frac{2a}{1-a^2},\quad
\eta_a=\frac{1-a^2}{1+a^2},
\]
and
\[
L_\pm=\frac{A_a(u+v)\pm\sqrt{A_a^2(u-v)^2+4B_a^2uv}}{2}.
\]
Then the essential spectrum of the positive Gram operator is exactly
\[
\boxed{\sigma_{\mathrm{ess}}(T_{a,t}^*T_{a,t})
=[L_-,\eta_a\min(u,v)]\ \cup\ [\eta_a\max(u,v),L_+].}
\]
The intervals may degenerate to points. They are separated by a nonempty open interval if and only if \(\operatorname{Re}t\ne0\); its exact width is \(4\eta_a|\operatorname{Re}t|\). The sharp operator and essential norms coincide:
\[
\boxed{\|T_{a,t}\|^2=\|T_{a,t}\|_{\mathrm e}^2=L_+.}
\]
The operator is invertible exactly for \(t\ne1,-1\), and in that case
\[
\boxed{\|T_{a,t}^{-1}\|^2=\|T_{a,t}^{-1}\|_{\mathrm e}^2=1/L_-.}
\]
For \(t=1\) or \(t=-1\), its kernel is infinite-dimensional, its range is closed, and zero lies in the essential Gram spectrum.

## Assumptions and scope

The Hardy norm is \(\|f\|_{H^2}^2=\sum_{n\ge0}|\widehat f(n)|^2\). Composition means \(C_\varphi f=f\circ\varphi\). The Fredholm essential spectrum is the Calkin-algebra spectrum, and the essential norm is distance to compact operators. No realness hypothesis on \(t\) is imposed. The theorem describes the essential spectrum, not the possible isolated gap eigenvalues of the Gram operator.

## Proof

**1. Poisson Gram identity.** For an inner function \(\varphi\), the pushforward of normalized circle measure under its boundary values is harmonic measure at \(\varphi(0)\): for positive integers \(k\), its moments \(\int_{\mathbb T}\varphi(\zeta)^k\,dm(\zeta)=\varphi(0)^k\) agree with the corresponding moments of the Poisson kernel, and conjugation gives the other moments. In particular, for \(\varphi=b_a\), first on polynomials and then by density and boundedness of the Poisson weight,
\[
\|C_{b_a} f\|^2=\int_{\mathbb T}|f(\zeta)|^2P_{-a}(\zeta)\,dm(\zeta),\qquad
 P_{-a}(\zeta)=\frac{1-a^2}{|\zeta+a|^2}.
\]
Its Fourier coefficients give the exact Gram matrix \(H_{mn}=(-a)^{|m-n|}\), \(m,n\ge0\). The same argument gives boundedness for \(C_{b_a^{-1}}\), with Poisson weight \(P_a\). Substitution in the two formulas for \(b_a\) and \(b_a^{-1}\) verifies both inverse identities, so \(C_{b_a}^{-1}=C_{b_a^{-1}}\).

**2. Parity and the block symbol.** Define \(D_t f(z)=f(z)+tf(-z)\), diagonal in Taylor coefficients with multipliers \(d_e=1+t\) on even indices and \(d_o=1-t\) on odd indices. Then \(T_{a,t}=C_{b_a}D_t\) and the Gram matrix is \(D_t^*HD_t\). Pairing the coefficients \((\widehat f(2j),\widehat f(2j+1))\), \(j\ge0\), gives a unitary onto vector-valued \(H^2\). In these coordinates the Gram is exactly the block Toeplitz compression with symbol
\[
M(e^{i\theta})=D^*F(e^{i\theta})D,\qquad D=\operatorname{diag}(d_e,d_o),
\]
\[
F(e^{i\theta})=\frac{1-a^2}{1-2a^2\cos\theta+a^4}
\begin{pmatrix}
1+a^2&-a(1+e^{i\theta})\\
-a(1+e^{-i\theta})&1+a^2
\end{pmatrix}.
\]
Indeed the diagonal series is \(\sum_{k\in\mathbb Z}a^{2|k|}e^{ik\theta}\); the even-row, odd-column series is \(\sum_{k\in\mathbb Z}(-a)^{|2k-1|}e^{ik\theta}\), which is \(-a(1-a^2)(1+e^{i\theta})/(1-2a^2\cos\theta+a^4)\); the remaining off-diagonal entry is its conjugate. Direct multiplication gives
\[
F(e^{i\theta})^{-1}=\frac1{1-a^2}
\begin{pmatrix}1+a^2&a(1+e^{i\theta})\\a(1+e^{-i\theta})&1+a^2\end{pmatrix}.
\]

**3. Band endpoints and gap.** If \(u,v>0\), set \(x=|\cos(\theta/2)|\in[0,1]\). The eigenvalues of \(M^{-1}\), in decreasing order, are
\[
\mu_\pm(x)=\frac12\left[A_a\left(\frac1u+\frac1v\right)\pm
\sqrt{A_a^2\left(\frac1u-\frac1v\right)^2+\frac{4B_a^2x^2}{uv}}\right].
\]
They remain positive since \(A_a^2-B_a^2=1\). The Gram-symbol eigenvalues \(\lambda_-(x)=1/\mu_+(x)\) and \(\lambda_+(x)=1/\mu_-(x)\) are respectively decreasing and increasing in \(x\). At \(x=0\) the symbol is diagonal, giving \(\eta_a\min(u,v)\) and \(\eta_a\max(u,v)\); at \(x=1\) its diagonal is \((A_a u,A_a v)\) and its off-diagonal entry has magnitude \(B_a\sqrt{uv}\), giving \(L_-,L_+\). If \(u=0\) or \(v=0\), the symbol eigenvalues are zero and \(\max(u,v)F_{11}(e^{i\theta})\). The latter ranges from \(\eta_a\max(u,v)\) to \(A_a\max(u,v)\), again giving the stated endpoints.

For continuous matrix-valued symbols the Toeplitz compression induces a unital homomorphism modulo compact operators: the product identity holds modulo finite rank for matrix trigonometric polynomials and extends by uniform approximation. For a real number outside the range of the symbol eigenvalues, compressing the inverse of the shifted symbol therefore gives an inverse modulo compacts. Conversely, if \(M(\zeta)v=\lambda v\) for a unit vector \(v\), the normalized Hardy kernels based at \(r\zeta\), multiplied by \(v\), form a weakly null approximate eigenvector sequence as \(r\uparrow1\). Indeed, the squared norm of the error is bounded by the Poisson average of \(\|(M-\lambda I)v\|^2\), which tends to zero at \(\zeta\) by continuity. Thus the Calkin spectrum is the union of the two symbol eigenvalue ranges. The distance between the two inner endpoints is \(\eta_a|u-v|=4\eta_a|\operatorname{Re}t|\).

**4. Sharp norms and invertibility.** The pointwise inequalities \(L_- I\le M\le L_+I\) persist under compression. Since both endpoints already belong to the essential Gram spectrum, they are also the extremal endpoints of the full Gram spectrum. By the norm identity for \(T^*T\) and its Calkin counterpart, the operator and essential norms squared of \(T_{a,t}\) both equal \(L_+\). When \(t\ne\pm1\), both parity multipliers are nonzero, so \(D_t\), and hence \(T_{a,t}\), is invertible. The inverse norm squared and its Calkin analogue are the reciprocals of the respective lower Gram endpoints, both \(1/L_-\). For \(t=\pm1\), \(D_t\) is twice a projection onto one parity subspace. Its kernel is infinite-dimensional, and the range of \(T_{a,t}\) is closed because \(C_{b_a}\) is invertible.

## Verification

The supplemental program `spectral_checks.py` checks the symbol and inverse product numerically, tests the claimed intervals against sampled symbol eigenvalues, and compares the extremal eigenvalues of representative finite sections to the predicted endpoints with finite tolerances. It does not examine every finite-section eigenvalue for gap membership and does not establish the infinite-dimensional formulas. See `VERIFICATION.md` for replay instructions.

## Relationship to prior work and limitations

The scalar Poisson Gram identity and the continuous matrix-valued Toeplitz principle are standard ingredients. Here the parity restriction gives an exact block symbol, and the inverse of that symbol yields both explicit monotone ranges and the sharp stability constants for this pair of composition operators. Charpentier and Zarouf study boundedness and Fourier criteria for single-symbol composition operators on weighted Beurling–Sobolev spaces; the present result concerns a different question on classical \(H^2\). The statement is specific to the two indicated symbols and \(0<a<1\); it does not classify arbitrary sums of composition operators or the full Gram spectrum inside the open gap. Complete historical priority over uncatalogued or inaccessible sources is not asserted.

## References

1. S. Charpentier and R. Zarouf, *Composition operators on weighted Beurling–Sobolev spaces*, arXiv:2611.17392, https://arxiv.org/abs/2611.17392.
2. B. R. Choe, H. Koo, M. Wang and J. Yang, *Compact linear combinations of composition operators induced by linear fractional maps*, revised 9 January 2015, https://doczz.net/doc/7661708/compact-linear-combinations-of-composition.
3. *Truncated Floquet–Bloch transform for computing the spectral properties of large finite systems of resonators*, Section 2, https://doi.org/10.1112/tlm3.70009.
4. *On the Norm of Certain Weighted Composition Operators on the Hardy Space*, 2009, https://doi.org/10.1155/2009/720217.
