# Two sharp symmetry switches for quadratic spherical harmonics on a lune

## Finding

Let \(d\ge3\), and let \(\mathcal H_2(S^{d-1})\) be the complex space of restrictions of homogeneous harmonic quadratic polynomials on the unit sphere, with normalized spherical probability measure \(\sigma\). For \(0<L<\pi\), define the lune
\[
E_L=\{x\in S^{d-1}:\arg(x_1+i x_2)\in[-L/2,L/2]\}.
\]
The undefined argument on \(x_1=x_2=0\) is immaterial (a null set). This is the intersection of two hemispheres whose inward normals meet at angle \(\pi-L\). Let \(C_L:\mathcal H_2\to\mathcal H_2\) be the positive self-adjoint concentration operator characterized by
\[
\langle C_Lf,g\rangle=\int_{E_L}f\overline g\,d\sigma.
\]
Put
\[
p=\frac{L}{2\pi},\qquad s=\frac{\sin L}{2\pi},\qquad c=\cos L,\qquad \beta=\frac{d-2}{d}.
\]
Its **entire spectrum, with multiplicities**, consists of
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\ \hline
\lambda_{e,\pm}=p+s\left(\frac c2\pm\sqrt{\frac{c^2}{4}+\beta}\right)&1\text{ each}\\
\lambda_o=p-sc&1\\
\lambda_x=p+s&d-2\\
\lambda_y=p-s&d-2\\
\lambda_T=p&d(d-3)/2.
\end{array}
\]
The last multiplicity is zero when \(d=3\); coincidences among displayed eigenvalues are counted additively.

The **largest** eigenvalue changes symmetry once, at \(L_+(d)=\arccos(2/d)\): it is \(\lambda_{e,+}\) for \(0<L<L_+(d)\), and \(\lambda_x\) for \(L_+(d)<L<\pi\). At the threshold the two families tie, and the maximizing eigenspace has dimension \(d-1\). The **smallest** eigenvalue changes symmetry once, at \(L_-(d)=\arccos(-2/d)\): it is \(\lambda_y\) below \(L_-(d)\), and \(\lambda_{e,-}\) above \(L_-(d)\). At that threshold the minimizing eigenspace has dimension \(d-1\). Both switches are strict away from their thresholds, with \(L_+(d)<\pi/2<L_-(d)\).

Every eigenvalue lies strictly between zero and one for \(0<L<\pi\). Thus restriction \(R_L:f\mapsto f|_{E_L}\) is injective. Its exact squared singular-value condition number is the ratio of the two extremal eigenvalues just described. In particular,
\[
\kappa(C_L)\sim
6\left(\frac32+\sqrt{\frac54-\frac2d}\right)L^{-2},
\qquad L\downarrow0,
\]
and \(\kappa(R_L)=\sqrt{\kappa(C_L)}\). The determinant is
\[
\det C_L=
\left[p(p+sc)-\beta s^2\right](p-sc)
(p^2-s^2)^{d-2}p^{d(d-3)/2}.
\]

## Assumptions and scope

The dimension \(d\) is any integer at least three; the aperture \(L\) is any real number strictly between zero and \(\pi\). All concentration fractions use probability-normalized source surface measure, and the same restriction measure (not the conditional probability measure on the lune). The operator acts on the **pure degree-two** harmonic space, not the full space of degrees at most two. Complex coefficients are permitted. The spectral formulas refer to this precise normalization and to a lune cut out by two hemispheres, not a polar cap or a spherical shell.

## Proof

Write \(m=d-2\), \(r^2=x_1^2+x_2^2\), \(\phi=\arg(x_1+i x_2)\), and \(z=(x_3,\ldots,x_d)\). Rotational invariance gives independent, uniform \(\phi\in[0,2\pi)\) and a transverse direction \(u=z/|z|\in S^{m-1}\), while \(r^2\) has beta distribution with parameters \((1,m/2)\). In particular,
\[
\mathbb E[r^2]=\frac2d,\qquad
\mathbb E[r^4]=\frac8{d(d+2)},\qquad
\operatorname{Var}(r^2)=\frac{4m}{d^2(d+2)}.
\]
For the angular indicator of the lune,
\[
\mathbb E[\mathbf1_{E_L}]=p,\qquad
\mathbb E[\cos(2\phi)\mathbf1_{E_L}]=s,\qquad
\mathbb E[\cos(4\phi)\mathbf1_{E_L}]=sc.
\]
All corresponding sine averages vanish, by reflection symmetry.

The harmonic quadratic space decomposes orthogonally over the full sphere into the following invariant sectors: the two-dimensional even sector spanned by \(h_0=r^2-2/d\) and \(h_c=x_1^2-x_2^2=r^2\cos(2\phi)\); the one-dimensional odd axial sector spanned by \(h_s=2x_1x_2=r^2\sin(2\phi)\); the two mixed sectors spanned respectively by \(x_1z_j\) and \(x_2z_j\) for \(1\le j\le m\); and the traceless transverse quadratic sector in \(z\), of dimension \(m(m+1)/2-1=d(d-3)/2\). The transverse sector is absent for \(m=1\). Each basis element is harmonic: the trace terms in \(h_0\) cancel because \(h_0=(m/d)(x_1^2+x_2^2)-(2/d)|z|^2\) on the sphere.

The two full-sphere norms required for the even block are
\[
\|h_0\|_2^2=\frac{4m}{d^2(d+2)},\qquad
\|h_c\|_2^2=\frac4{d(d+2)},
\]
and \(\mathbb E[h_0r^2]=\|h_0\|_2^2\). Consequently, in the normalized basis \((h_0/\|h_0\|_2,h_c/\|h_c\|_2)\), the restricted Gram block is
\[
\begin{pmatrix}p&\sqrt{m/d}\,s\\\sqrt{m/d}\,s&p+sc\end{pmatrix}.
\]
Its two eigenvalues are exactly \(\lambda_{e,+}\) and \(\lambda_{e,-}\). Angular orthogonality gives \(\lambda_o=p-sc\). Each mixed sector has eigenvalue \(p+s\), respectively \(p-s\), because \(2\mathbb E[\cos^2\phi\,\mathbf1_{E_L}]=p+s\) and \(2\mathbb E[\sin^2\phi\,\mathbf1_{E_L}]=p-s\). A transverse traceless quadratic depends on \(\phi\) only through the independent radius, so its concentration is \(p\). Orthogonality between all listed sectors follows from transverse rotational symmetry and reflection in \(x_2\). The multiplicities sum to \(\dim\mathcal H_2=d(d+1)/2-1\), proving that the spectrum is exhaustive.

For \(0<L<\pi\) we have \(s>0\) and \(-1<c<1\). The axial odd level satisfies \(\lambda_y<\lambda_o<\lambda_x\), while \(\lambda_{e,-}<p<\lambda_{e,+}\). Therefore only \(\lambda_{e,+}\) and \(\lambda_x\) can be largest, and only \(\lambda_{e,-}\) and \(\lambda_y\) can be smallest. The differences, divided by \(s\), are respectively
\[
\frac{\lambda_{e,+}-\lambda_x}{s}
=\frac c2+\sqrt{\frac{c^2}{4}+\beta}-1,
\qquad
\frac{\lambda_{e,-}-\lambda_y}{s}
=\frac c2+1-\sqrt{\frac{c^2}{4}+\beta}.
\]
In the first expression, the right-hand side changes sign precisely at \(c=1-\beta=2/d\); in the second it changes sign precisely at \(c=\beta-1=-2/d\). Squaring is reversible because \(1\mp c/2>0\) on \((-1,1)\). Strict monotonicity of cosine on \((0,\pi)\) proves the stated switches and their uniqueness. At each crossing, a simple even-block eigenvalue joins one of the \(m\)-fold mixed sectors, giving multiplicity \(m+1=d-1\).

A nonzero harmonic polynomial is real analytic and cannot vanish on a nonempty open set, so both \(E_L\) and its complement have strictly positive \(L^2\)-mass for every nonzero harmonic. Hence \(0<C_L<I\). The product of all displayed eigenvalues gives the determinant. Finally, \(p-s=L^3/(12\pi)+O(L^5)\), while
\[
\lambda_{e,+}=\frac{L}{2\pi}
\left(\frac32+\sqrt{\frac54-\frac2d}\right)+O(L^3).
\]
The small-aperture extremal branches established above give the claimed sharp condition-number asymptotic.

## Verification

The accompanying standalone `check_lune_spectrum.py` forms full-sphere and lune Gram matrices **without inserting the proposed spectral blocks**. It uses a fourth-moment-exact cubature on the transverse sphere (a mixture of axial points and hypercube corners), a second-degree-exact radial rule, and 64-point angular Gauss-Legendre quadrature. Generalized Gram eigenvalues were compared with the closed formulas for dimensions \(3,4,5,6,8\) and six distinct apertures, with the largest absolute error below \(2\times10^{-11}\). The checker also examines extremal branches, dimension counts, trace, and degeneracies at both transition angles. It reports `LUNE_QUADRATIC_CUBATURE_CHECKS_PASS 656`. Numerical quadrature supports but does not replace the all-dimensional proof.

## Relationship to prior work

Michel, Plattner and Seibert (arXiv:2103.14650, first public March 26, 2021) develop a general spin-weighted spherical Slepian eigenproblem and commuting operators for polar caps. Their general-region matrix includes scalar functions as an abstract case, but the inspected statements do not give the present *pure quadratic* lune spectrum, its two angular crossing thresholds, or its condition-number law. Aslam and Khalid (arXiv:2010.07266, first public October 14, 2020) develop spatial-Slepian transforms and general-region concentration matrices on \(S^2\), not this all-dimensional explicit classification. Roddy and McEwen (arXiv:2106.02023, first public June 3, 2021) construct Slepian wavelets for incomplete spherical regions; only the abstract and bibliographic material were available for this comparison, so an unobserved equivalent specialization is an acknowledged residual risk.

The novelty asserted here is **not** the finite-dimensional Slepian formulation, the standard spherical moment identities, or the separability of spherical coordinates. It is the full explicit pure-quadrupole lune eigenvalue classification for all \(d\ge3\), including the distinct sharp maximizing/minimizing symmetry switches and their multiplicities. General concentration matrices supply a way to calculate the answer, but do not by themselves state these parameter-dependent sharp transitions. Literature priority remains provisional pending an independent expert comparison.

## Limitations

The result addresses one connected lune formed by two hemispheres, pure scalar degree-two harmonics, and exact continuous measurements. It does not establish optimality among arbitrary observation regions, formulas for higher degrees or mixed-degree low-pass spaces, or noise-robust finite-sampling guarantees. The separate cubature is a finite check and cannot exclude an unlocated equivalent result in older spherical harmonic or geometric eigenfunction literature. No independent mathematical audit or validation has been performed.

## References

1. V. Michel, A. Plattner and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650, first posted March 26, 2021. https://arxiv.org/abs/2103.14650
2. A. Aslam and Z. Khalid, *Spatial-Slepian Transform on the Sphere*, arXiv:2010.07266, first posted October 14, 2020. https://arxiv.org/html/2010.07266v1
3. P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on the Sphere*, arXiv:2106.02023, first posted June 3, 2021. https://arxiv.org/abs/2106.02023
4. F. A. Dahlen and F. J. Simons, *Spectral estimation on a sphere in geophysics and cosmology*, Geophysical Journal International 174 (2008), 774–807, for background on spherical Slepian concentration.
