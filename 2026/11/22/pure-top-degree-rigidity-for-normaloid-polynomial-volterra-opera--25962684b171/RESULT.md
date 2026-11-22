# Pure-top-degree rigidity for normaloid polynomial Volterra operators on super-Gaussian power-Fock space

## Finding
For each real \(\alpha>2\), let \(\mathcal F_\alpha^2\) be the Hilbert space of entire functions with
\[
\|f\|_\alpha^2=\int_{\mathbb C}|f(z)|^2e^{-2|z|^\alpha}\,dA(z).
\]
For every polynomial \(g\), set \(V_g f(z)=\int_0^z f(w)g'(w)\,dw\). The operator is bounded exactly when \(g\) is constant or \(\deg(g-g(0))\le\alpha\). For a **nonzero bounded** operator, the following are equivalent:

1. \(V_g\) is normaloid, meaning \(\|V_g\|=r(V_g)\).
2. \(V_g\) is hyponormal, meaning \(V_g^*V_g\ge V_gV_g^*\).
3. \(V_g\) is subnormal, meaning it admits a normal extension.
4. \(\alpha=d\) is an integer \(d\ge3\), and \(g(z)=c+a_dz^d\) for \(a_d\ne0\).

Moreover, if \(g(z)=c+a_dz^d+\sum_{j=1}^{d-1}a_jz^j\) with \(a_d\ne0\), then
\[
\sigma(V_g)=\{\lambda\in\mathbb C:|\lambda|\le|a_d|\}.
\]
If the lower-degree part is nonzero and \(q=\max\{j<d:a_j\ne0\}\), put \(\ell=d-q\). For appropriately phase-aligned unit vectors \(F_n\in\operatorname{span}\{e_n,e_{n+\ell}\}\),
\[
\|V_gF_n\|^2-|a_d|^2
=|a_da_q|\,q\,d^{-q/d}n^{q/d-1}+o(n^{q/d-1}).\tag{1}
\]
This is positive for all sufficiently large \(n\), establishing the strict norm-versus-spectral-radius gap for every nontrivial lower-degree perturbation.

## Assumptions and scope
The parameter \(\alpha\) is an arbitrary fixed real number greater than two; \(g\) is any complex polynomial; no nonpolynomial symbols are classified. We adopt ordinary planar area measure \(dA\), and the normalization of that measure does not change operator weights. For \(g\) constant the Volterra operator is zero and is omitted from the nonzero equivalence. A compact nonzero bounded operator in this family is not normaloid. The claim concerns normaloidity, hyponormality, and subnormality, not all possible weaker operator-normality notions.

## Proof
**(i) Exact coefficients and boundedness.** The monomials are orthogonal and complete. Their squared norms are
\[
M_n=\frac{2\pi}{\alpha}2^{-(2n+2)/\alpha}
\Gamma\left(\frac{2n+2}{\alpha}\right),\qquad
 e_n(z)=z^n/M_n^{1/2},\quad n\ge0.
\]
For every integer \(j\ge1\), direct integration gives
\[
V_{z^j}e_n=w_{n,j}(\alpha)e_{n+j},\qquad
w_{n,j}(\alpha)=\frac{j}{n+j}\sqrt{\frac{M_{n+j}}{M_n}}
\sim j\alpha^{-j/\alpha}n^{j/\alpha-1}.
\tag{2}
\]
The asymptotic follows by the gamma-ratio formula \(\Gamma(x+t)/\Gamma(x)\sim x^t\) with \(x=(2n+2)/\alpha\). A finite polynomial sum is therefore bounded if all its nonconstant degrees are at most \(\alpha\), and compact if each degree is strictly below \(\alpha\). Conversely, if any degree \(j>\alpha\) is present, its divergent coefficient contributes an orthogonal coordinate to each \(V_ge_n\), forcing unboundedness. When \(\alpha\) is not an integer, every bounded nonzero polynomial symbol produces a compact operator.

**(ii) Spectral radius.** Every \(V_g\) strictly increases the lowest nonzero Taylor degree of any nonzero entire input, so \(V_g\) has no eigenvalue \(\lambda\ne0\). For compact \(V_g\), compact spectral theory implies \(\sigma(V_g)=\{0\}\). If \(\alpha=d\) is an integer and the leading term is \(a_dz^d\), equation (2) gives \(w_{n,d}(d)\to1\); hence \(V_g-a_dS^d\) is compact, where \(Se_n=e_{n+1}\). For \(|\lambda|>|a_d|\), \(V_g-\lambda I\) is a Fredholm operator of index zero by compact perturbation of the invertible \(a_dS^d-\lambda I\); having no kernel, it is surjective and invertible. For \(|\lambda|<|a_d|\), the Fredholm index is \(-d\) (the index of \(a_dS^d-\lambda I\)), precluding invertibility. Closedness of the spectrum establishes the entire claimed disk. Consequently \(r(V_g)=|a_d|\).

**(iii) All mixed symbols fail normaloidity.** Assume \(\alpha=d\), \(a_d\ne0\), and at least one lower coefficient is nonzero. Let \(q\) be the highest such degree and \(\ell=d-q\). Write \(u_n=V_ge_n\), \(v_n=V_ge_{n+\ell}\). Formula (2) and the orthogonality of basis monomials give
\[
\langle u_n,v_n\rangle
=\overline{a_d}a_q\,w_{n,d}(d)w_{n+\ell,q}(d)
+o(n^{q/d-1}),
\]
using the convention linear in the second variable for this displayed inner product. The sole degree-collision with maximal exponent comes from the top-degree output of \(e_n\) and degree-\(q\) output of \(e_{n+\ell}\); every other collision has strictly smaller sum of polynomial degrees. Since \(w_{n,d}(d)=1+O(n^{-1})\) and \(w_{n+\ell,q}(d)\sim qd^{-q/d}n^{q/d-1}\), the cross term has absolute value
\[
|\langle u_n,v_n\rangle|=|a_da_q|q d^{-q/d}n^{q/d-1}+o(n^{q/d-1}).
\]
Each column obeys \(\|u_n\|^2=|a_d|^2+O(n^{-1})+O(n^{2q/d-2})\), and the same holds for \(v_n\). Both errors are \(o(n^{q/d-1})\). Choosing \(\zeta_n\in\mathbb C\) with \(|\zeta_n|=1\) to make the cross term positive and setting \(F_n=(e_n+\zeta_ne_{n+\ell})/\sqrt2\) gives precisely (1). Thus \(\|V_g\|>|a_d|=r(V_g)\), with no smallness assumption on the lower coefficients. If \(g\) has degree less than \(\alpha\), its compact quasinilpotent operator likewise has positive norm but zero spectral radius.

**(iv) Subnormality of the pure critical case.** Suppose \(\alpha=d\ge3\) is an integer and \(g(z)=c+a_dz^d\). Equation (2) simplifies exactly to
\[
w_{n,d}(d)^2=\frac{(n+1)(2n+d+2)}{2(n+d)^2}.
\tag{3}
\]
The operator \(V_{z^d}\) decomposes into \(d\) reducing unilateral weighted shifts along residues \(r\in\{0,\ldots,d-1\}\). For any such \(r\) define
\[
A_r=\frac{r+1}{d},\quad B_r=A_r+\frac12,\quad C_r=\frac rd+1.
\]
At the \(k\)-th step, the squared weight is \((k+A_r)(k+B_r)/(k+C_r)^2\). Because \(C_r-A_r=1-1/d>0\) and \(C_r-B_r=1/2-1/d>0\), independent random variables
\[
U_r\sim\operatorname{Beta}(A_r,C_r-A_r),\qquad
W_r\sim\operatorname{Beta}(B_r,C_r-B_r)
\]
are well defined. Their product \(X_r=U_rW_r\) lies in \((0,1)\) and satisfies
\[
\mathbb E[X_r^k]=\frac{(A_r)_k(B_r)_k}{(C_r)_k^2}
=\prod_{h=0}^{k-1}w_{r+hd,d}(d)^2
\quad(k\ge0).
\]
A rotation-invariant measure on the disk with squared radial coordinate distributed as \(X_r\) makes analytic monomials have precisely these norms. Multiplication by the coordinate on its ambient \(L^2\) space is a normal extension of the corresponding unilateral weighted shift. Taking the direct sum and multiplying by \(a_d\) gives a normal extension of \(V_g\). In particular \(V_g\) is subnormal and hence hyponormal and normaloid. Finally, every hyponormal bounded Hilbert-space operator is normaloid, so parts (ii)–(iv) prove all equivalences.

## Verification
The standalone `check_mixed.py` recomputes rational squared-weight identities and beta-product moments for multiple integer orders, tests the exact gamma-ratio coefficients, and checks representative phase-aligned two-monomial norm witnesses. It reports 285 passing finite diagnostics. Those computations do not prove the arbitrary-order assertions; the exact equations and asymptotic error estimates above provide the infinite-dimensional argument.

## Relationship to prior work
Constantin–Persson (2015) already proves the full generalized-Fock spectral disk and quasinilpotent compact case, including invariance under lower polynomial terms; these spectral assertions are background, not claimed as new. Mengestie–Ueki (2018) and Yang–Zhou (2022) treat Volterra boundedness and compactness on generalized Fock spaces. Mengestie–Takele (2023) discusses structural questions for fast radial Fock-type weights. Mengestie (2026) proves normaloid/hyponormal/subnormal equivalence for the **classical quadratic Gaussian Fock weight**, which is outside the present \(\alpha>2\) family. The substantive extension here is a complete mixed-polynomial classification for every super-Gaussian exponent, with the explicit positive norm-versus-radius asymptotic. Monomial critical subnormality and its beta moments are used here as premises and are not presented as a new standalone contribution.

## Limitations
This is a statement for polynomial symbols on the exact power weight \(e^{-2|z|^\alpha}\); it does not classify all holomorphic symbols or arbitrary radial fast weights. The witness is asymptotic and does not give a uniform finite-index bound as coefficients vary. The general theory of normaloid weighted shifts and an inaccessible relevant 2022 paper pose residual historical-priority risk. Numerical diagnostics are finite; no independent audit or external validation has been performed.

## References
1. O. Constantin and A.-M. Persson, *The spectrum of Volterra-type integration operators on generalized Fock spaces*, arXiv:1509.01401 (first submitted 4 September 2015), https://arxiv.org/abs/1509.01401
2. T. Mengestie and S.-I. Ueki, *Integral, differential and multiplication operators on generalized Fock spaces*, arXiv:1807.03394, first submitted 9 July 2018. https://arxiv.org/abs/1807.03394
3. Z.-C. Yang and Z.-H. Zhou, *Generalized Volterra-type operators on generalized Fock spaces*, DOI:10.1002/mana.202000014. https://doi.org/10.1002/mana.202000014
4. T. Mengestie and M. H. Takele, *Integral and Weighted Composition Operators on Fock-type Spaces*, Bull. Malays. Math. Sci. Soc. 46 (2023), article 80. https://doi.org/10.1007/s40840-023-01476-4
5. T. Mengestie, *Normality properties of Volterra-type integral operators on the Fock space*, published online 21 October 2026. https://doi.org/10.1007/s43036-026-00541-6
