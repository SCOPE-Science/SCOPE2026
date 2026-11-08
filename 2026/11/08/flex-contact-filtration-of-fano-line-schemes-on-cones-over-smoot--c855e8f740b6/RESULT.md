# Flex-contact filtration of Fano line schemes on cones over smooth plane curves

## Finding
Let \(C\subset\mathbb P^2_{\mathbb C}\) be a smooth plane curve of degree \(d\ge3\), let \(X\subset\mathbb P^3\) be its projective cone and \(F=F_1(X)\) its full Grassmannian Fano scheme of lines. For each \(p\in C\), denote by \(r_p=I_p(C,T_pC)\) the contact order of its tangent line (\(2\le r_p\le d\)). Then \(F_{\mathrm{red}}\cong C\). For the ruling line indexed by \(p\), the completed local ring of \(F\) is
\[
\widehat{\mathcal O}_{F,p}\cong\mathbb C[[t,u]]/(t^{r_p-2}u^2,t^{r_p-3}u^3,\ldots,tu^{r_p-1},u^{r_p}).
\]
The ideal is interpreted as \((u^2)\) for \(r_p=2\). If \(\mathcal N\) denotes the nilradical, then \(\mathcal N/\mathcal N^2\cong\mathcal O_C(d-2)\). At each inflection point \(p\), the skyscraper layer \(\mathcal N^j/\mathcal N^{j+1}\), for \(2\le j<r_p\), has length \(r_p-j\), with all such layers zero at ordinary points. Consequently the full Plücker Hilbert polynomial is
\[
P_F(n)=2dn+d+\sum_{p\in C\,\mathrm{flex}}\binom{r_p-1}{2}
       =2dn+d(3d-5)+\sum_{p\,\mathrm{hyperflex}}\binom{r_p-2}{2}.
\]
The sums are finite. In particular the cone over the Fermat curve \(X^d+Y^d+Z^d=0\) has \(3d\) tangent-contact points, all with contact order \(d\), and Plücker Hilbert polynomial
\[P_F(n)=2dn+d+3d\binom{d-1}{2}.\]
For the Fermat quartic, this is \(8n+40\), rather than the \(8n+28\) of a smooth plane quartic with only ordinary flexes.

## Assumptions and scope
Everything is over \(\mathbb C\). The plane curve is embedded by its complete degree-one linear system, smooth, and of degree at least three. The cone has its standard vertex; the Fano scheme is the scheme cut out by the restriction of the cone equation to the tautological line on \(\operatorname{Gr}(2,4)\), not merely its set of rulings. Contact order means the intersection multiplicity with the tangent line at a smooth point. The Plücker polarization restricts to \(\mathcal O_C(1)\) on the reduced curve. No statements for positive characteristic or singular plane curves are asserted.

## Proof
**(1) Underlying lines.** Projecting the cone from its vertex sends any line not passing through the vertex onto a line contained in \(C\). Since a smooth irreducible plane curve of degree \(d\ge3\) contains no line, every line in the cone is a ruling from the vertex to a unique \(p\in C\). Thus \(F_{\mathrm{red}}\cong C\), embedded linearly in the ruling-plane \(\mathbb P^2\subset\operatorname{Gr}(2,4)\).

**(2) Exact Grassmannian equations.** Near a ruling with affine base point \(p=(1,a,c)\), write a neighboring line in coordinates \([W:X_0:X_1:X_2]\) as
\[
(W,X_0,X_1,X_2)=(s_1,s_0,a s_0+b s_1,c s_0+e s_1).
\]
Put \(f(x,y)=F(1,x,y)\) for a local defining polynomial of \(C\), choosing the chart so \(f_y\ne0\). The coefficients in the binary polynomial \(F(s_0,a s_0+b s_1,c s_0+e s_1)\) vanish exactly when the line lies on the cone. The first two coefficient conditions are \(f(a,c)=0\) and \(f_x(a,c)b+f_y(a,c)e=0\). By the implicit function theorem, \(c=\phi(a)\) and \(e=\phi'(a)b\) in the completed local ring. Write \(u=b\). The remaining coefficients are
\[
 u^j h_j(a),\quad 2\le j\le d,
\]
where \(h_j(a)\) is the coefficient of \(z^j\) in \(f(a+z,\phi(a)+\phi'(a)z)\).

**(3) Contact and monomial ideal.** Translate the coordinate \(a\) so the point is \(a=0\), and choose the tangent horizontal. If the tangent has intersection multiplicity \(r\), then \(\phi(a)=\gamma a^r+O(a^{r+1})\) with \(\gamma\ne0\). In \(\mathbb C[[a,y]]\), \(f(a,y)=U(a,y)(y-\phi(a))\) for a unit \(U\). Multiplication by this unit changes the full coefficient system by an invertible triangular transformation; it does not alter the generated ideal. The coefficient of \(z^j\), \(2\le j\le r\), is therefore a unit times \(a^{r-j}\), since its leading term is \(-\gamma\binom rj a^{r-j}\), nonzero in characteristic zero. For \(j>r\), the equations are redundant because \(u^r\) is already an equation. Hence the completed ideal is exactly
\[
(a^{r-2}u^2,a^{r-3}u^3,\ldots,au^{r-1},u^r).
\]
This includes \(r=2\), giving a generic double structure.

**(4) Global first nilpotent layer.** Let \(\ell\subset\mathbb C^3\otimes\mathcal O_C\) be the tautological line of the plane embedding, so \(\ell\cong\mathcal O_C(-1)\). Let \(M\subset(\mathbb C^3/\ell)\) be the line of tangent directions of \(C\) at its points. By definition \(T_C\cong\operatorname{Hom}(\ell,M)\), hence \(M\cong\ell\otimes T_C\). The first-order infinitesimal movement of the ruling vertex along the tangent direction is parametrized by \(M\), which is the normal line to \(C=F_{\rm red}\) in the first infinitesimal neighborhood of \(F\). Therefore \(\mathcal N/\mathcal N^2\cong M^\vee\cong\mathcal O_C(1)\otimes K_C\). By adjunction \(K_C\cong\mathcal O_C(d-3)\), so \(\mathcal N/\mathcal N^2\cong\mathcal O_C(d-2)\).

**(5) Higher layers and Hilbert polynomial.** In the completed ring of (3), \(\mathcal N=(u)\); for \(j\ge2\), the quotient \(\mathcal N^j/\mathcal N^{j+1}\) at the point has \(\mathbb C[[t]]\)-module \(\mathbb C[[t]]/(t^{r-j})\) for \(2\le j<r\), and zero otherwise. Its total finite length at \(p\) is \(\sum_{j=2}^{r-1}(r-j)=\binom{r-1}{2}\). The two one-dimensional graded layers \(\mathcal O_C\) and \(\mathcal N/\mathcal N^2\) contribute, by Riemann–Roch and the Plücker restriction, respectively \(dn+1-g\) and \(d(n+d-2)+1-g\), where \(g=(d-1)(d-2)/2\). Adding the finite lengths gives the first polynomial formula. The classical Hessian intersection divisor of a smooth complex plane curve has \(\sum_p(r_p-2)=3d(d-2)\), and \(\binom{r-1}{2}=(r-2)+\binom{r-2}{2}\), yielding the second formula.

**(6) Fermat example.** The Hessian of \(X^d+Y^d+Z^d\) is a nonzero multiple of \((XYZ)^{d-2}\). It meets the Fermat curve at exactly \(3d\) distinct points on the coordinate lines. Each of these has tangent contact order \(d\), as restricting the defining equation to its tangent leaves one coordinate to the \(d\)th power. The preceding general formula gives the stated polynomial, in particular \(8n+40\) when \(d=4\).

## Verification
The accompanying executable `artifacts/verify_cone.py` checks the exact tangent-jet coefficient ideals for local contact models of order \(2\) through \(10\), their finite nilpotent-filtration lengths, the Fermat Hessian identity for degrees \(3\) through \(9\), and consistency of the two Hilbert-polynomial expressions. Execute `python artifacts/verify_cone.py` using Python with SymPy installed. The independent-of-examples general proof is in the preceding section; the finite checks are consistency tests, not an exhaustive classification of all plane curves.

## Relationship to prior work
Eisenbud and Harris, *The Geometry of Schemes*, Section VI.2 and its discussion of Fano schemes, explicitly observe that the Fano scheme of lines on a cone over a plane curve is nonreduced. That general nonreducedness statement does not specify the completed local rings, the higher nilradical filtration, the conormal line bundle, or the hyperflex correction in the Plücker Hilbert polynomial. Ilten, *Fano Schemes of Lines on Toric Surfaces* (2014), completely classifies toric surface line schemes; the cones here for \(d\ge3\) are non-toric and not covered by his classification. The classical cubic-cone case is recovered at \(d=3\), while the higher-contact strata for arbitrary \(d\) and the quartic/higher Fermat polynomials require the general analysis above. Historical priority for the full contact-filtration formula is subject to further specialist comparison.

## Limitations
No result is asserted in positive characteristic; the characteristic-zero nonvanishing of binomial coefficients and Hessian formula are essential. The theorem classifies the scheme of lines on a cone, not the Hilbert scheme of arbitrary curves on the cone or the behavior of Fano schemes under deformations. No independent expert audit or formal proof certification has been performed. Published works may contain an equivalent expression under a different deformation-theoretic language.

## References
- D. Eisenbud and J. Harris, *The Geometry of Schemes*, Springer GTM 197, 2000, Sections IV.3 and VI.2 (online scholarly text: https://webhomes.maths.ed.ac.uk/~v1ranick/papers/eisenbudharris.pdf).
- N. Ilten, *Fano Schemes of Lines on Toric Surfaces*, arXiv:1411.3025v1, first posted 2014-11-11 (https://arxiv.org/html/1411.3025v1).
- Classical Plücker–Hessian inflection-point formula for smooth plane curves in characteristic zero.
