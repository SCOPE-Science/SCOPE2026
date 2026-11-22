# Two essential Gram bands and sharp stability constants for paired automorphic composition

## Finding

Let \(H^2=H^2(\mathbb D)\) be the classical Hardy Hilbert space, let \(0<a<1\), and define the involutive disk automorphism \(b_a(z)=(z-a)/(1-az)\). For any \(t\in\mathbb C\), let
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
Then the essential spectrum of the positive Gram operator is *exactly*
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

The Hardy norm is \(\|f\|_{H^2}^2=\sum_{n\ge0}|\widehat f(n)|^2\). Composition means \(C_\varphi f=f\circ\varphi\). The Fredholm essential spectrum of a bounded operator is its Calkin-algebra spectrum. Operator essential norm means distance to compact operators. No hypothesis of real \(t\), positivity of coefficients, or smallness of \(|t|\) is imposed. This theorem describes the **essential** spectrum of the Gram operator, not its entire spectrum: isolated finite-multiplicity Gram eigenvalues may occur in the displayed open gap.

## Proof

**1. Poisson Gram identity.** Boundary composition by an inner map \(\varphi\) pushes normalized circle measure forward to harmonic measure at \(\varphi(0)\). Indeed its positive Fourier moments are \(\int_{\mathbb T}\varphi(\zeta)^k\,dm(\zeta)=\varphi(0)^k\), and conjugation gives the negative moments. By density of trigonometric polynomials, for every \(f\in H^2\),
\[
\|C_\varphi f\|^2=\int_{\mathbb T}|f(\zeta)|^2P_{\varphi(0)}(\zeta)\,dm(\zeta),\qquad
P_c(\zeta)=\frac{1-|c|^2}{|\zeta-c|^2}.
\]
Here \(b_a(0)=-a\), hence \(C_{b_a}^*C_{b_a}\) is the scalar Toeplitz operator with matrix \(h_{mn}=(-a)^{|m-n|}\), \(m,n\ge0\).

**2. The parity filter.** Define \(D_tf(z)=f(z)+tf(-z)\). It is diagonal in Taylor coefficients, with \(d_e=1+t\) on even indices and \(d_o=1-t\) on odd indices. As \(T_{a,t}=C_{b_a}D_t\), its Gram matrix is \(D_t^*HD_t\), where \(H_{mn}=(-a)^{|m-n|}\). Group the coefficients as \((\widehat f(2j),\widehat f(2j+1))\), \(j\ge0\). This is a unitary from \(H^2\) to \(H^2(\mathbb T;\mathbb C^2)\) in coefficient form. The resulting Gram operator is **exactly**, not just modulo compacts, a block Toeplitz compression with continuous Hermitian matrix symbol
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
For example the even-even Fourier series is \(\sum_{j\in\mathbb Z}a^{2|j|}e^{ij\theta}=(1-a^4)/(1-2a^2\cos\theta+a^4)\); the even-odd series is \(-a(1-a^2)(1+e^{i\theta})/(1-2a^2\cos\theta+a^4)\). These verify all four entries. Direct multiplication gives the simple exact inverse
\[
F(e^{i\theta})^{-1}=\frac1{1-a^2}
\begin{pmatrix}1+a^2&a(1+e^{i\theta})\\a(1+e^{-i\theta})&1+a^2\end{pmatrix}.
\]

**3. Band endpoints and strict gap.** Suppose first \(u,v>0\). Put \(x=|\cos(\theta/2)|\in[0,1]\). The two eigenvalues of \(M(e^{i\theta})^{-1}\), in decreasing order, are
\[
\mu_\pm(x)=\frac12\left[A_a\left(\frac1u+\frac1v\right)\pm
\sqrt{A_a^2\left(\frac1u-\frac1v\right)^2+\frac{4B_a^2x^2}{uv}}\right].
\]
They remain positive since \(A_a^2-B_a^2=1\). The two ordered Gram-symbol eigenvalues are \(\lambda_-(x)=1/\mu_+(x)\) and \(\lambda_+(x)=1/\mu_-(x)\). Consequently \(\lambda_-\) is decreasing and \(\lambda_+\) is increasing in \(x\), with endpoint values
\[
\lambda_-(0)=\eta_a\min(u,v),\quad\lambda_+(0)=\eta_a\max(u,v),\qquad
\lambda_\pm(1)=L_\pm.
\]
The last two values also follow by diagonalizing \(D^*F(1)D\), whose two eigenvalue formula is the quadratic expression defining \(L_\pm\). If \(u=0\) or \(v=0\), the two eigenvalues are identically zero and \(\max(u,v)F_{11}(\theta)\), with the latter ranging monotonically from \(\eta_a\max(u,v)\) to \(A_a\max(u,v)\); these are again precisely the stated formulas. By the continuous matrix-valued Toeplitz symbol theorem, the Calkin spectrum of this self-adjoint block Toeplitz operator is the union of the ranges of those two eigenvalue branches. Their open gap has width \(\eta_a|u-v|\), equal to \(4\eta_a|\operatorname{Re}t|\).

**4. Sharp norm and inverse stability.** For any positive continuous Hermitian block symbol \(M\), the Toeplitz compression satisfies \(\|T_M\|\le\max_\theta\|M(e^{i\theta})\|\), and normalized Hardy reproducing kernels with fixed polarized vectors approach the latter supremum, proving equality. The same kernels tend weakly to zero, so this norm equals the essential norm. Apply this to \(T_{a,t}^*T_{a,t}\) and take square roots. For \(t\ne\pm1\), both diagonal factors of \(D_t\) are nonzero, and \(C_{b_a}\) is invertible because \(b_a\circ b_a\) is the identity. The positive Gram operator has lower bound \(L_-I\), by compression of the symbol inequality; reproducing kernels show its lower spectral edge and essential spectral edge equal \(L_-\). It follows from \(\|T_{a,t}^{-1}\|^2=1/\inf\sigma(T_{a,t}^*T_{a,t})\) and the Calkin version that the inverse norms equal \(L_-^{-1}\). When \(t=\pm1\), the filter \(D_t\) is twice a projection onto one parity subspace: that kernel is infinite-dimensional and its range is closed, because \(C_{b_a}\) is an invertible map.

## Verification

The algebraic checks can be reproduced by running `python spectral_checks.py` with NumPy installed. They recompute the exact Gram coefficients and matrix symbol, compare closed-form endpoints to matrix eigenvalues, verify representative special cases, and compare the predicted bulk bands with finite sections. Their numerical scope is finite; the infinite-dimensional conclusions follow from the preceding exact Fourier and Toeplitz argument, not from numerical extrapolation.

## Relationship to prior work

Charpentier and Zarouf (arXiv:2611.17392v1, first posted 12 November 2026) study boundedness and Fourier-coefficient criteria for single-symbol composition operators between Beurling–Sobolev spaces. They motivate examining operator-matrix structure, but the paired-symbol essential Gram-band classification is a different question and is not a stated consequence of their boundedness characterization. Choe, Koo, Wang and Yang treat compactness rigidity of finite linear combinations of linear-fractional composition operators, not their exact Gram essential spectra or norm/inverse-norm constants. Continuous Hermitian matrix-valued Toeplitz essential-spectrum theory, here used as a classical ingredient, supplies the *general symbol principle* but not this concrete parity Gram symbol, endpoints or the explicit \(\operatorname{Re}t\) phase criterion. The 2025 Floquet–Bloch Toeplitz analysis cited below is a reference for that general principle. Related spectral-gap constructions for non-composition matrices do not imply the automorphic composition formula.

## Limitations

The result is for the classical Hardy Hilbert space, the paired symbols \(b_a\) and \(-b_a\), and \(0<a<1\); it does not classify arbitrary sums of composition operators or weighted Beurling–Sobolev spaces. It does **not** assert that the entire Gram spectrum consists of the two essential bands: boundary-localized isolated eigenvalues can lie in a band gap. No eigenvalue enumeration or finite-section outlier classification is claimed. The search for earlier implicit realizations of the same parity–Poisson Toeplitz formula cannot exclude every unpublished or uncatalogued source.

## References

1. S. Charpentier and R. Zarouf, *Composition operators on weighted Beurling–Sobolev spaces*, arXiv:2611.17392v1, 12 November 2026, https://arxiv.org/pdf/2611.17392.
2. B. R. Choe, H. Koo, M. Wang and J. Yang, *Compact linear combinations of composition operators induced by linear fractional maps*, revised 9 January 2015, https://doczz.net/doc/7661708/compact-linear-combinations-of-composition.
3. *Truncated Floquet–Bloch transform for computing the spectral properties of large finite systems of resonators*, Section 2 (continuous Hermitian matrix Toeplitz band functions), https://doi.org/10.1112/tlm3.70009.
4. *On the Norm of Certain Weighted Composition Operators on the Hardy Space*, 2009, https://doi.org/10.1155/2009/720217 (comparison for single weighted composition operators).
