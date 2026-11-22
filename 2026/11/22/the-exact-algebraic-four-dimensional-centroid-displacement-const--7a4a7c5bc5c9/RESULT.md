# The exact algebraic four-dimensional centroid-displacement constant

## Finding
For every full-dimensional compact convex body \(K\subset\mathbb R^4\) and every unit vector \(u\), let \(c(K)\) be the volume centroid, \(c(\partial K)\) the surface-area centroid, and \(w_K(u)\) the width. The optimal coefficient in
\[
|\langle c(\partial K)-c(K),u\rangle|\le D_4 w_K(u)
\]
is the following explicitly determined algebraic number. Let \(\rho\) be the unique positive root of
\[
Q(r)=7r^6+48r^5+53r^4+24r^3-3r^2-8r-1.
\]
Then
\[
\boxed{D_4=\frac{3(\rho^4+4\rho^3+10\rho^2+4\rho+1)}{20(\rho^2+\rho+1)(3\rho^2+2\rho+1)}=0.18934567240973057668\ldots.}
\]
Equivalently, \(D_4\) is the root near \(0.18934567241\) of the irreducible degree-six polynomial
\[
25000z^6-105000z^5+144000z^4-70300z^3+14160z^2-1152z+27=0.
\]
The maximizing affine profile in the one-dimensional variational formula is unique up to positive multiplication, and is \(\ell(t)=1+(\rho-1)t\) with \(\rho=0.44710556516275334942\ldots\). This yields an explicit sharp sequence of four-dimensional convex polytopes.

## Assumptions and scope
We use the optimal-width theorem and variational characterization proved by Myroshnychenko, Ryabogin, Tatarko and Yaskin (2026), which equates the best coefficient for the boundary-versus-volume centroid inequality in dimension \(n\) to
\[
D_n=\max_{\ell\ge0,\ \ell\ \mathrm{affine},\ \ell\not\equiv0}\left(\frac{I_2(\ell)}{I_1(\ell)}-\frac{I_1(\ell)}{I_0(\ell)}\right),\qquad I_j(\ell)=\int_0^1t^j\ell(t)^{n-2}\,dt.
\]
The contribution here is an exact algebraic determination, uniqueness of the maximizing profile, and the algebraic degree in dimension four, rather than a new proof of the cited general reduction theorem. The coefficient also governs the sharp difference between projected volume centroids from the earlier result of Myroshnychenko, Tatarko and Yaskin (2022).

## Proof
**Normalization and integration.** Positive scaling of \(\ell\) does not affect the objective. If \(\ell(0)>0\), normalize \(\ell(t)=1+(r-1)t\), where \(r=\ell(1)/\ell(0)\ge0\). The missing endpoint \(\ell(0)=0\) corresponds to \(r\to\infty\). In dimension four direct polynomial integration gives
\[
I_0=\frac{r^2+r+1}{3},\quad I_1=\frac{3r^2+2r+1}{12},\quad I_2=\frac{6r^2+3r+1}{30}.
\]
Consequently the variational objective is
\[
F(r)=\frac{3(r^4+4r^3+10r^2+4r+1)}{20(r^2+r+1)(3r^2+2r+1)}.
\]
**Unique global optimizer.** Exact differentiation yields
\[
F'(r)=-\frac{3Q(r)}{20(r^2+r+1)^2(3r^2+2r+1)^2}.
\]
The coefficients of \(Q\), in descending order, have exactly one sign change, so Descartes' rule gives at most one positive zero, counted with multiplicity. Since \(Q(0)=-1\) and \(Q(1)=120\), exactly one such zero \(\rho\) exists in \((0,1)\). For \(r>0\), \(Q\) is negative before \(\rho\) and positive afterwards, and hence \(F\) increases strictly before \(\rho\) and decreases strictly afterwards. At \(r=0\) the objective equals \(3/20\), and at the omitted endpoint it tends to \(1/20\); neither is optimal. This proves global uniqueness and the stated exact formula.

**Algebraic degree.** Put \(A(r)=r^2+r+1\), \(B(r)=3r^2+2r+1\) and \(N(r)=r^4+4r^3+10r^2+4r+1\). Eliminating \(r\) between \(Q(r)=0\) and \(20zA(r)B(r)-3N(r)=0\), their integer resultant is
\[
1769472000\bigl(25000z^6-105000z^5+144000z^4-70300z^3+14160z^2-1152z+27\bigr).
\]
The degree-six polynomial in parentheses is irreducible modulo \(113\), with unchanged leading degree; therefore it is irreducible over \(\mathbb Q\). This proves that \(D_4\) has algebraic degree six, not merely that it satisfies a polynomial of degree six. The same modular test proves \(Q\) irreducible over \(\mathbb Q\).

**Sharpness witnessed by polytopes.** Let \(\ell(t)=1+(\rho-1)t\) and, for \(\varepsilon>0\), define
\[
K_\varepsilon=\{(t,y,z)\in\mathbb R\times\mathbb R^2\times\mathbb R:0\le t\le1,\ \|y\|_\infty\le\varepsilon\ell(t),\ 0\le z\le\varepsilon^2t\}.
\]
This is a full-dimensional convex polytope and has width one in the \(t\)-direction. Direct slicing gives \(\langle c(K_\varepsilon),e_1\rangle=I_2/I_1\). Its two dominant faces, at \(z=0\) and \(z=\varepsilon^2t\), have asymptotic surface centroid \(I_1/I_0\); the other faces contribute a vanishing relative amount. Therefore the absolute difference of the first centroid coordinates approaches \(D_4\). This is the explicit four-dimensional instance of the sharpness construction in the cited 2026 work. Since \(\operatorname{diam}K_\varepsilon\to1\), the same coefficient is sharp for the diameter comparison.

## Verification
`verify.py` reproduces all three exact moments, the reduced rational objective, its derivative, the sextic root isolation, the resultant polynomial, and mod-113 irreducibility tests, then prints high-precision values. In particular the rational numbers \(4471055651627/10^{13}\) and \(4471055651628/10^{13}\) give opposite signs of \(Q\), isolating \(\rho\). The exact polynomial proof, rather than the decimal approximation, establishes the global statement. The executable depends on Python 3 and SymPy.

## Relationship to prior work
The 2022 projection-centroid paper gives a one-parameter formula for \(D_n\) and explicitly solves dimension three; its Section 4, Step 5 explains why higher-dimensional algebraic equations obstruct a general closed form. The November 8, 2026 boundary-centroid paper proves the sharp inequality in every dimension, identifies the same \(D_n\), and records \(D_2\), \(D_3\), and the limiting constant. It supplies both the variational reduction and the general polytope sharpness construction used above. Neither of these two inspected papers states the dimension-four sextic, the exact algebraic value, uniqueness of its profile, or algebraic degree six. Thus the new determination is an exact natural invariant within the established geometric theorem, not an independent proof of that theorem.

## Limitations
No new universal inequality beyond the two cited general theorems is asserted. Global uniqueness is proved for the normalized affine profile, not for all convex-body sequences that asymptotically attain the sharp constant. Algebraic irreducibility is checked by a reproducible finite-field computation, and the analytic proof includes the sign argument needed independently of numerical root finding. Historical priority of this explicit specialization is provisional pending wider literature examination.

## References
1. S. Myroshnychenko, D. Ryabogin, K. Tatarko and V. Yaskin, *The sharp bound on the distance between the centers of mass of a convex body and its boundary*, arXiv:2611.11635, first public November 8, 2026. https://arxiv.org/abs/2611.11635
2. S. Myroshnychenko, K. Tatarko and V. Yaskin, *How far apart can the projection of the centroid of a convex body and the centroid of its projection be?*, arXiv:2212.14456, first public December 29, 2022. https://arxiv.org/abs/2212.14456
