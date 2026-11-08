# Sharp collision hierarchy for two equal Bargmann–Fock jet clusters

## Finding

For each integer \(m\geq1\), form two clusters of \(m\) orthonormal, covariantly normalized derivative-evaluation representers at distinct points of the standard Bargmann–Fock space. Let \(r>0\) be the Euclidean distance between the points, and let \(G_m(r)\) denote the \(2m\)-by-\(2m\) Gram matrix. Its spectrum is strictly positive, and its \(m\) eigenvalues below one have **\(m\) different sharp collision scales**. Label these eigenvalues in decreasing order as \(\lambda^-_{m,1}(r),\ldots,\lambda^-_{m,m}(r)\). As \(r\downarrow0\), for each \(1\leq p\leq m\),

\[
\lambda^-_{m,p}(r)=\frac{\gamma_{m,p}^2}{2}\,r^{4p-2}\bigl(1+O_m(r^2)\bigr),\qquad
\gamma_{m,p}=\frac{[(p-1)!]^2}{(2p-1)!(2p-2)!}
\sqrt{\frac{(m+p-1)!}{(m-p)!}}.
\]

In particular, the sharp smallest eigenvalue and spectral condition number satisfy

\[
\boxed{\lambda_{\min}(G_m(r))=
\frac{[(m-1)!]^4}{2(2m-1)![(2m-2)!]^2}\,r^{4m-2}
\bigl(1+O_m(r^2)\bigr)}
\]

and

\[
\boxed{\kappa_2(G_m(r))=
\frac{4(2m-1)![(2m-2)!]^2}{[(m-1)!]^4}\,
 r^{-(4m-2)}\bigl(1+O_m(r^2)\bigr)}.
\]

Thus the worst-case coefficient recovery becomes ill-conditioned at the explicit exponent \(4m-2\), with the exact leading factor, rather than at one common collision exponent for all derivative directions. The distinct rates and constants hold for every fixed integer multiplicity, not just a finite list of tested cases.

For example, at multiplicity two, the **exact** all-separation lower bound is

\[
\lambda_{\min}(G_2(r))=
1-\frac{e^{-r^2/2}}2\left(\sqrt{4+r^4}+r^2\right)
=\frac{r^6}{48}+O(r^8).
\]

At multiplicity three the corresponding leading term is \(r^{10}/8640\).

## Assumptions and scope

The standard Bargmann–Fock space consists of entire functions with norm

\[
\|f\|^2=\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z).
\]

Its orthonormal monomials are \(e_j(z)=z^j/\sqrt{j!}\), for integers \(j\geq0\). The Weyl translation by \(w\in\mathbb C\) is the unitary

\[
(D_w f)(z)=e^{z\overline w-|w|^2/2}f(z-w).
\]

Define the normalized jets \(u_{w,j}=D_we_j\), with \(0\leq j<m\). At each fixed \(w\), they are orthonormal. Their inner products with arbitrary \(f\) represent the covariantly normalized evaluations of derivatives through order \(m-1\). The two clusters are \((u_{a,j})_{0\leq j<m}\) and \((u_{b,j})_{0\leq j<m}\), where \(a,b\in\mathbb C\), \(a\neq b\), and \(r=|b-a|\). The Gram matrix \(G_m(r)\) is their coefficient Gram matrix; its eigenvalues are independent of the argument of \(b-a\) and the common center by Weyl unitary symmetries. The condition number is the ratio of its largest to smallest eigenvalue, not the condition number of its square root.

All asymptotics hold with \(m\) fixed and \(r\to0^+\); there is no uniformity asserted as \(m\to\infty\). Arbitrary unequal cluster multiplicities and generalized Fock weights are not covered.

## Proof

**1. Reduction to an orthogonal-projection leakage matrix.** Weyl translation and phase rotation reduce the two centers to \(0\) and positive real \(r\). Let \(P_m\) project onto \(E_m=\operatorname{span}\{e_0,\ldots,e_{m-1}\}\). The cross-Gram block is the \(m\)-by-\(m\) matrix of \(C_m(r)=P_mD_rP_m|_{E_m}\). Therefore

\[
G_m(r)=\begin{pmatrix}I&C_m(r)\\C_m(r)^*&I\end{pmatrix},
\quad \operatorname{spec}G_m(r)=\{1\pm\sigma_j(C_m(r)):1\leq j\leq m\}.
\]

Introduce \(A_m(r)=(I-P_m)D_rP_m|_{E_m}\), a map from the \(m\)-dimensional polynomial space into its infinite-dimensional orthogonal complement. Unitarity gives the **exact identity**

\[
A_m(r)^*A_m(r)=I-C_m(r)^*C_m(r).
\]

Write the singular values of \(A_m(r)\) in decreasing order as \(s_{m,1}(r)\geq\cdots\geq s_{m,m}(r)\). Then the eigenvalues of \(G_m(r)\) below one, in decreasing order, are exactly

\[
\lambda^-_{m,p}(r)=1-\sqrt{1-s_{m,p}(r)^2},\qquad 1\leq p\leq m.
\]

For every \(r>0\), \(A_m(r)\) is injective: if \(D_rq\) were a polynomial for some nonzero polynomial \(q\), then \(e^{rz-r^2/2}q(z-r)\) would be a polynomial, an impossibility. Also \(C_m(r)\) is invertible for every \(r\): the factorization \(D_r=e^{-r^2/2}e^{rz}e^{-r\partial_z}\), compressed onto \(E_m\), is a product of two triangular matrices with diagonal one, times \(e^{-r^2/2}\). Hence \(\det C_m(r)=e^{-mr^2/2}\neq0\). Thus every leakage singular value lies strictly between zero and one, and \(G_m(r)\) is positive definite.

**2. Exact leading entries.** For row \(k\geq m\) and column \(0\leq j<m\), expansion of \(D_re_j\) in the orthonormal monomial basis yields

\[
\begin{aligned}
(A_m(r))_{kj}&=e^{-r^2/2}\sqrt{\frac{k!}{j!}}
\sum_{\ell=0}^{j}\binom j\ell\frac{(-r)^{j-\ell}r^{k-\ell}}{(k-\ell)!}\\
&=\sqrt{\frac{k!}{j!}}\frac{r^{k-j}}{(k-j)!}
+O_{k,j}(r^{k-j+2}).
\end{aligned}
\]

The remainder has the displayed parity because every summand has exponent \(k-j+2(j-\ell)\), and multiplication by \(e^{-r^2/2}\) preserves parity. Moreover \(A_m(r)\) depends real-analytically on \(r\) as an operator from a finite-dimensional space to Fock space; this controls all infinite-row tails in the exterior-power argument below.

**3. A unique leading exterior minor.** Fix \(1\leq p\leq m\). A \(p\)-by-\(p\) minor of \(A_m(r)\), using increasing row indices \(k_0<\cdots<k_{p-1}\) with \(k_i\geq m\) and increasing column indices \(j_0<\cdots<j_{p-1}\) with \(j_i<m\), has vanishing order at least

\[
\sum_{i=0}^{p-1}k_i-\sum_{i=0}^{p-1}j_i\ \geq\ p^2.
\]

Equality is possible at precisely the single pair of index sets

\[
(k_0,\ldots,k_{p-1})=(m,\ldots,m+p-1),
\quad(j_0,\ldots,j_{p-1})=(m-p,\ldots,m-1).
\]

For these indices, the leading coefficient is the determinant of the matrix with entries \(\sqrt{(m+i)!/(m-p+j)!}/(p+i-j)!\). Factoring the row and column factorials reduces the determinant to

\[
\det\left[\frac1{(p+i-j)!}\right]_{0\leq i,j<p}
=\prod_{i=0}^{p-1}\frac{i!}{(p+i)!}.
\]

Indeed, multiplication of row \(i\) by \((p+i)!\) makes its \(j\)-th entry the degree-\(j\) monic falling-factorial polynomial evaluated at \(p+i\); its determinant is the Vandermonde product \(\prod_{i=0}^{p-1}i!\). The one nonzero leading exterior coefficient is therefore

\[
 c_{m,p}=\sqrt{\prod_{i=0}^{p-1}\frac{(m+i)!}{(m-p+i)!}}
\prod_{i=0}^{p-1}\frac{i!}{(p+i)!}>0.
\]

Each other exterior matrix entry has at least one extra power of \(r\). If its row and column index sets both differ from the displayed extremal sets, it has at least two extra powers. The unique distinguished entry itself has a relative \(O_m(r^2)\) correction from the parity expansion. Block perturbation of this rank-one leading exterior operator, or its squared norm, therefore gives

\[
\|\bigwedge^p A_m(r)\|
=c_{m,p}\,r^{p^2}(1+O_m(r^2)).
\]

The operator norm of the \(p\)-th exterior power equals the product of the \(p\) largest singular values. Dividing the formula at \(p\) by that at \(p-1\) (and taking \(c_{m,0}=1\)) yields

\[
 s_{m,p}(r)=\frac{c_{m,p}}{c_{m,p-1}}r^{2p-1}(1+O_m(r^2))
=\gamma_{m,p}r^{2p-1}(1+O_m(r^2)).
\]

The last equality follows by direct factorial cancellation. This establishes the separate \(m\) collision scales and their exact constants.

**4. Gram eigenvalues, condition number and exact two-jet check.** Since \(1-\sqrt{1-s^2}=s^2/2+O(s^4)\), substituting the preceding singular-value asymptotics proves the formula for every \(\lambda^-_{m,p}\). The largest eigenvalue of \(G_m(r)\) tends to two. Taking \(p=m\) and dividing yields the two boxed asymptotics, including the condition-number coefficient.

For \(m=2\), direct computation gives

\[
C_2(r)=e^{-r^2/2}\begin{pmatrix}1&-r\\r&1-r^2\end{pmatrix}.
\]

Its larger singular value is \(e^{-r^2/2}(\sqrt{4+r^4}+r^2)/2\). This proves the exact two-jet expression and its \(r^6/48\) leading term, independently of the exterior asymptotic argument.

## Verification

`CHECK.py` (requires `mpmath>=1.3.0`) computes the cross-Gram block via finite generalized Laguerre polynomials and independently via coefficients of displaced monomials. It checks the identity \(I-C_m^*C_m=A_m^*A_m\) using a convergent Fock-basis tail, the paired eigenvalues of the full Gram matrix, leading factorial minors and the sharp small-separation constants for multiplicities one through five. It also checks the exact two-jet spectral formula at several separations. In the saved package this yielded 717 high-precision finite-dimensional assertions, all passing. **Those numerical checks are not the proof of the statement for arbitrary \(m\)**; that proof is the exterior-minor argument above.

## Relationship to prior work

Alpay, De Martino and Diki (first posted April 24, 2026) develop a complex RKHS representer theorem and Fock-space interpolation examples, supplying a natural motivation for computing quantitative conditioning of structured Fock interpolation. Their Sections 3–4 concern representers and value-sampling/superoscillations; they do not state the all-multiplicity, sharp two-jet collision hierarchy or its constants. Haimi and Romero (2020) characterize multiple sampling and interpolation in weighted Fock spaces through density conditions, not the present sharp singular-value asymptotics for two colliding finite jets. Borichev, Hartmann, Kellay and Massaneda (2015) address geometric conditions and multiplicity, not this spectral hierarchy. Earlier quantum-optical literature on displaced Fock states supplies related matrix elements; those standard identities are not claimed as new. The mathematical contribution claimed here is the **complete sharp all-order collision spectrum**, rather than the displacement formula or the general RKHS representer theorem.

## Limitations

The weights, Weyl normalization, both multiplicities and the ambient Bargmann–Fock Hilbert norm are fixed explicitly. The rates are local as \(r\to0^+\) for each fixed multiplicity, not uniform in the multiplicity, not global two-point optimality results, and not a theorem about infinite sampling lattices. The exact general finite-separation Gram spectrum is not expressed in elementary radicals; it is determined by a finite singular-value problem. Equivalent asymptotics in older coherent-state, Hermite interpolation or quantum-optical literature remain a publication-priority risk; no external independent audit has been performed.

## References

1. N. Alpay, A. De Martino and K. Diki, *Representer theorem in complex reproducing kernel Hilbert spaces with applications to Fock and Hardy spaces and superoscillations*, arXiv:2604.22165, first publicly submitted 2026-04-24, https://arxiv.org/abs/2604.22165; full text https://arxiv.org/html/2604.22165v2 (especially Sections 2–4).
2. A. Haimi and J. L. Romero, *Multiple sampling and interpolation in weighted Fock spaces of entire functions*, Complex Analysis and Operator Theory 2020, https://doi.org/10.1007/s11785-020-01065-4.
3. A. Borichev, A. Hartmann, K. Kellay and X. Massaneda, *Geometric conditions for multiple sampling and interpolation in the Fock space*, arXiv:1508.03932, https://arxiv.org/abs/1508.03932.
4. A. Wünsche, *Displaced Fock states and their connection to quasiprobabilities*, Quantum Optics 3 (1991), 359, https://doi.org/10.1088/0954-8998/3/6/005. The accessible abstract concerns displaced-state identities and does not suffice to certify absence of related asymptotics in its unavailable full text.
