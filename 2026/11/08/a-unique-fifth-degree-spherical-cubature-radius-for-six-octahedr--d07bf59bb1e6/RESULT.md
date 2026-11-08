# A unique fifth-degree spherical cubature radius for six octahedral cap windows

## Finding

Let \(\sigma\) be normalized surface area measure on the unit sphere \(\mathbb S^2\subset\mathbb R^3\). For \(0<t<1\), define the multiplicity-weighted six-cap function
\[
w_t(x)=\sum_{j=1}^3\bigl(\mathbf1_{\{x_j\ge t\}}+\mathbf1_{\{x_j\le -t\}}\bigr)=\sum_{j=1}^3\mathbf1_{\{|x_j|\ge t\}},
\quad d\nu_t(x)=\frac{w_t(x)}{3(1-t)}\,d\sigma(x).
\]
Overlapping caps are counted separately. Thus \(\nu_t\) is a nonnegative probability measure for every \(0<t<1\), not the uniform measure on the union of six caps.

**Theorem.** Among \(0<t<1\), the integral of every real polynomial of total degree at most five is exactly preserved,
\[
\int_{\mathbb S^2}p\,d\nu_t=\int_{\mathbb S^2}p\,d\sigma \quad (\deg p\le5),
\]
if and only if \(t=t_*=\sqrt{3/7}\). The order is sharp: at this radius, the degree-six Legendre harmonic \(P_6(x_3)\) has nonzero error
\[
\int_{\mathbb S^2}P_6(x_3)\,d\nu_{t_*}=-\frac{11}{784}t_*(1+t_*)\ne0.
\]
The exact degree-four obstruction at every radius is
\[
\int_{\mathbb S^2}P_4(x_3)\,d\nu_t
=\frac7{96}\,t(1+t)(7t^2-3).
\]

There is an equivalent *sharp quadratic-harmonic stability interpretation*. Let \(\mathcal H_2\) be the five-dimensional real space of degree-two spherical harmonics, and let \(Q_t(f,g)=\int w_t fg\,d\sigma\). Its eigenvalues relative to the usual \(L^2(\sigma)\) inner product are
\[
\lambda_E(t)=\frac{3(1-t)}{16}(21t^4+21t^3-9t^2-9t+16),\qquad \text{multiplicity }2,
\]
\[
\lambda_T(t)=\frac{3(1-t)^2}{8}(7t^3+14t^2+11t+8),\qquad \text{multiplicity }3.
\]
The corresponding eigenspaces are the traceless diagonal quadratics and the off-diagonal quadratics, respectively. In particular,
\[
\lambda_E(t)-\lambda_T(t)=\frac{15}{16}t(1-t^2)(7t^2-3).
\]
Consequently \(Q_t\) has condition number one on \(\mathcal H_2\) at exactly the unique interior radius \(t_*\), when it equals \(3(1-t_*)\langle\cdot,\cdot\rangle_{L^2(\sigma)}\). Below this radius the diagonal sector has the smaller eigenvalue; above it the off-diagonal sector does. This condition number is the ratio of the larger to the smaller eigenvalue and is strictly greater than one elsewhere in \(0<t<1\).

## Assumptions and scope

The domain is the unit two-sphere with probability surface area measure. The six cap centers are the coordinate axes \(\pm e_1,\pm e_2,\pm e_3\), and all six cap angular half-widths are \(\arccos t\). Positive multiplicity weighting, not union indicators, is essential when caps overlap. We exclude the degenerate endpoint \(t=0\), where \(w_t=3\) almost everywhere and the construction is just the uniform measure, and \(t=1\), where the normalizer vanishes. Polynomial degree means ambient total degree restricted to the sphere; quadratic harmonics are real and homogeneous.

## Proof

**Cap moment formula.** For integers \(a,b,c\ge0\), denote \(M_{abc}(t)=\int x_1^a x_2^b x_3^c w_t\,d\sigma\). If any exponent is odd, \(M_{abc}(t)=0\) by coordinate-sign invariance. Otherwise, with \((a_i,b_i,c_i)\) any permutation putting the axial exponent first, the normalized measure over the two opposite caps on the corresponding axis gives
\[
M_{abc}(t)=\sum_{\mathrm{axes}\ i}\frac{(b_i-1)!!(c_i-1)!!}{(b_i+c_i)!!}\int_t^1 s^{a_i}(1-s^2)^{(b_i+c_i)/2}\,ds.
\]
We take \((-1)!!=0!!=1\). The angular coefficient comes from the uniform circle integral at fixed polar coordinate \(s\); the factor of two opposite caps cancels the half-density of \(s\in[-1,1]\). Setting all exponents to zero yields \(M_{000}=3(1-t)\), proving normalization.

**Reduction to one fourth-degree obstruction.** The measure \(\nu_t\) is invariant under every permutation and sign change of its three coordinates. Odd monomials vanish; degree-two moments satisfy \(\int x_i^2\,d\nu_t=1/3\) by symmetry and \(\sum_i x_i^2=1\). Hence all degrees up to three are exact. In degree four, the only possibly nonzero monomial types are \(x_i^4\) and \(x_i^2x_j^2\). They have common integrals \(a\) and \(b\) satisfying \(3a+6b=1\). Thus all degree-four moments are correct precisely when \(a=1/5\), equivalently \(\int P_4(x_3)\,d\nu_t=0\), where
\[
P_4(z)=\frac18(35z^4-30z^2+3).
\]
Antipodal invariance then makes every polynomial of degree five with odd total degree integrate to zero; the even-degree components through four were just handled.

**Exact polynomial and uniqueness.** The zonal averaging identity for any degree \(\ell\) Legendre polynomial is
\[
\int_{\mathbb S^2}P_\ell(x_3)\,\mathbf1_{\{x\cdot v\ge t\}}\,d\sigma(x)
=\frac12 P_\ell(v_3)\int_t^1P_\ell(s)\,ds.
\]
For even degrees, adding opposite caps and summing over the three axes yields
\[
\int P_\ell(x_3)\,d\nu_t=\frac{1+2P_\ell(0)}{3(1-t)}\int_t^1P_\ell(s)\,ds.
\]
Substitute \(P_4\) and integrate: the degree-four obstruction is exactly \(7t(1+t)(7t^2-3)/96\). In the open interval \((0,1)\), it vanishes only at \(t=\sqrt{3/7}\), giving the if-and-only-if claim.

**Degree-six obstruction.** With
\[
P_6(z)=\frac1{16}(231z^6-315z^4+105z^2-5),
\]
the same cap identity gives the exact formula
\[
\int P_6(x_3)\,d\nu_t=\frac{t(1+t)(33t^4-30t^2+5)}{128}.
\]
Substituting \(t_*^2=3/7\) gives \(-11t_*(1+t_*)/784\ne0\). So the exactness cannot extend to all degree-six polynomials.

**Sharp quadratic-harmonic spectrum.** The signed-permutation symmetry decomposes the real quadratic harmonic space orthogonally as the diagonal traceless sector \(E=\operatorname{span}\{x_1^2-x_2^2,\ 2x_3^2-x_1^2-x_2^2\}\), of dimension two, and the off-diagonal sector \(T=\operatorname{span}\{x_1x_2,x_1x_3,x_2x_3\}\), of dimension three. The restricted cap form is scalar on each sector, and cross-terms vanish by coordinate parity. Since
\[
\int(x_1^2-x_2^2)^2\,d\sigma=\frac4{15},\qquad \int x_1^2x_2^2\,d\sigma=\frac1{15},
\]
its two eigenvalues are the ratios
\[
\lambda_E=\frac{15}{4}\left(2M_{400}-2M_{220}\right),\qquad \lambda_T=15M_{220}.
\]
Substitution of the cap moment formula and integration of the displayed elementary polynomials gives the two factored eigenvalue expressions in the theorem; subtraction yields \(15t(1-t^2)(7t^2-3)/16\). Both eigenvalues are strictly positive on \((0,1)\) because the cap weight is positive on an open set and a nonzero real spherical harmonic cannot vanish on that set. At their unique interior crossing they equal the common weighted trace average \(3(1-t_*)\). The strict eigenvalue ordering elsewhere follows from the sign of the difference. This proves both the exact spectrum and optimal conditioning assertion.

## Verification

Execute `python3 check.py` from the extracted research package. It performs exact calculations over the quadratic number field \(\mathbb Q(\sqrt{3/7})\), checks the full list of 56 monomials of total degree at most five, verifies normalization and the degree-six obstruction, and checks the quadratic-harmonic equalities at the unique radius. Independent symbolic calculation of the general-radius quadratic-sector eigenvalues uses the same polar-coordinate moment integral; both factored expressions and their difference were re-expanded exactly. It also verifies the general-radius eigenvalue expressions, their difference and trace, and the Legendre obstructions by exact rational polynomial coefficient comparison. The universal proof, uniqueness, and no-sixth-degree assertion are analytic; these checks establish polynomial identities rather than rely on numerical sampling.

## Relationship to prior work

The spherical harmonic concentration framework of Simons, Dahlen and Wieczorek gives general finite-dimensional spatial-band eigenproblems, including polar caps (arXiv:math/0408424, first posted 2004-08-31). The present theorem specializes to six *simultaneous, multiplicity-weighted* octahedral caps, calculates the complete quadratic sector spectrum, and identifies the unique nontrivial exact positive cubature radius of order five. Existing general concentration theory alone does not state the radius, the polynomial obstruction, or the crossover. Brauchart and Dick study spherical numerical quadrature based on discrete nodes (arXiv:1101.5450, first posted 2011-01-28); the present positive *continuous cap-window* cubature is a different object. Keast and Diaz discuss fully symmetric formulas with discrete nodes (SIAM J. Numer. Anal. 20 (1983), DOI 10.1137/0720029); their full text was not accessible for a decisive comparison. The known discrete octahedral point configuration itself is not a fifth-degree exact rule; the new ingredient is the exact cap-window width. Full equivalence to an unindexed historical continuous-window identity cannot be completely excluded.

## Limitations

The theorem requires six equal, antipodally paired, coordinate-axis cap windows on \(\mathbb S^2\) and uses the *sum* of overlapping cap indicators. It does not give a point-node cubature rule, nonnegative uniform-on-union rule, a statement for unequal windows, or a high-degree/general-dimensional analogue. The spectral calculation concerns real degree-two spherical harmonics only. An older inaccessible paper on symmetric integration formulas leaves a limited residual originality risk.

## References

- F. J. Simons, F. A. Dahlen, M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424v1 (2004-08-31), https://arxiv.org/abs/math/0408424; SIAM Review 48 (2006), 504–536.
- J. S. Brauchart, J. Dick, *Quasi-Monte Carlo rules for numerical integration over the unit sphere*, arXiv:1101.5450v1 (2011-01-28), https://arxiv.org/abs/1101.5450.
- P. Keast, J. C. Diaz, *Fully Symmetric Integration Formulas for the Surface of the Sphere in S Dimensions*, SIAM Journal on Numerical Analysis 20 (1983); https://doi.org/10.1137/0720029 (abstract/metadata accessible; full text not inspected).
