# Sharp E-optimal two-site Hermite sampling of cubic Bargmann–Fock polynomials

## Finding
For a cubic analytic polynomial in the standard Gaussian Bargmann–Fock norm, the unique symmetric pair of sites that maximizes the worst-case squared recovery gain from one value and one covariant first derivative at each site has squared radius
\[
x_*=1.51905535770046\ldots.
\]
The exact optimizer is the unique root in \((1.519055357,1.519055359)\) of
\[
Q(x)=x^6-10x^5+45x^4-111x^3+150x^2-108x+36=0.
\]
The sharp gain is
\[
\max_{w\ne0}\inf_{\|f\|=1}\|A_w f\|_2^2
=e^{-x_*}\frac{8(x_*^2-3)}{(x_*-2)(x_*^2-6x_*+12)}
=0.4855614655559759\ldots.
\]
It has a two-dimensional complex worst-observed subspace: one even and one odd polynomial. All sites with the indicated modulus are equivalent under rotation.

## Assumptions and scope
Let \(\mathcal P_3\) consist of analytic polynomials of degree at most three, with the Gaussian Bargmann–Fock norm
\[
\|f\|^2=\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z).
\]
The monomials \(e_k(z)=z^k/\sqrt{k!}\), \(0\le k\le3\), are orthonormal. For nonzero \(w\in\mathbb C\), define \(A_w f\in\mathbb C^4\) by the four functionals
\[
\ell_{\varepsilon,0}(f)=e^{-|w|^2/2}f(\varepsilon w),\qquad
\ell_{\varepsilon,1}(f)=e^{-|w|^2/2}\bigl(f'(\varepsilon w)-\varepsilon\overline w f(\varepsilon w)\bigr),
\quad \varepsilon\in\{+1,-1\}.
\]
These form an orthonormal value-and-first-jet pair at each site in the full Fock space, before restriction to \(\mathcal P_3\). The objective is the smallest squared singular value of \(A_w\) and **not** the determinant, largest eigenvalue, or a free choice of four sample nodes. This is the minimal two-site Hermite interpolation problem for cubic polynomials. Directly, the Gram determinant equals \(64x^4e^{-4x}/3\), so determinant-optimal sampling instead has \(x=1\); the present stability-optimal radius differs from this classical volume objective.

## Proof
By a unitary rotation it suffices to take \(w=r>0\) and \(x=r^2\). Directly evaluating the orthonormal monomial basis and splitting it into even degrees \(\{0,2\}\) and odd degrees \(\{1,3\}\) yields
\[
A_r^*A_r=e^{-x}\bigl(E(x)\oplus O(x)\bigr),
\]
where the order of basis vectors is \(0,2,1,3\), and
\[
E(x)=\begin{pmatrix}
2(x+1)&\sqrt2 x(x-1)\\
\sqrt2 x(x-1)&x\bigl(x+(x-2)^2\bigr)
\end{pmatrix},
\]
\[
O(x)=\begin{pmatrix}
2(x^2-x+1)&\frac{\sqrt6}{3}x(x^2-3x+3)\\
\frac{\sqrt6}{3}x(x^2-3x+3)&\frac{x^2}{3}\bigl(x+(x-3)^2\bigr)
\end{pmatrix}.
\]
Write \(\lambda_E^-\) and \(\lambda_O^-\) for their smaller eigenvalues. The trace and determinant pairs are
\[
T_E=x^3-3x^2+6x+2,\quad D_E=8x,\qquad
T_O=\frac{x^4-5x^3+15x^2-6x+6}{3},\quad D_O=\frac{8x^3}{3}.
\]
Thus the objective \(F(x)=e^{-x}\min\{\lambda_E^-(x),\lambda_O^-(x)\}\) is bounded above by \(h(x)=e^{-x}\lambda_O^-(x)\).

The odd off-diagonal entry is positive for every \(x>0\), so its eigenvalues are simple. If \(h'(x)=0\), implicit differentiation of \(\lambda^2-T_O\lambda+D_O=0\) gives
\[
\lambda=\frac{2D_O-D_O'}{T_O-T_O'}
=\frac{8x^2(2x-3)}{x^4-9x^3+30x^2-36x+12}.
\]
The numerator and denominator on the first fraction never vanish simultaneously at a positive \(x\). Substitution into the characteristic equation, clearing the nonzero denominator, gives the exact factorization
\[
-8x^2(x^3-3x^2+6x-6)Q(x)=0.
\]
Exact rational Sturm sequences show that \(Q\) has precisely two positive real roots, isolated in \((1.519055357,1.519055359)\) and \((2.808203101,2.808203103)\); the cubic factor has precisely one positive real root in \((1.596071637,1.596071639)\). At the first root the stationary eigenvalue lies below \(T_O/2\); at both other positive roots it lies above \(T_O/2\). These sign claims, and nonvanishing of their denominators, are verified exactly in `CHECKER.py`. Therefore the first root \(x_*\) is the **only** stationary point of the lower odd eigenvalue multiplied by \(e^{-x}\). Since \(h(x)\to0\) as \(x\downarrow0\) and as \(x\to\infty\), it is its unique global maximum.

Finally put
\[
L(x)=\frac{8(x^2-3)}{(x-2)(x^2-6x+12)}.
\]
Clearing the denominator in either parity characteristic polynomial evaluated at \(L(x)\) yields the identical identity
\[
L(x)^2-T_{E/O}(x)L(x)+D_{E/O}(x)
=-\frac{8(x^2-2x+2)Q(x)}{(x-2)^2(x^2-6x+12)^2}.
\]
At \(x_*\), exact rational sign isolation shows \(L(x_*)<T_E(x_*)/2\) and \(L(x_*)<T_O(x_*)/2\). Hence both parity **smaller** eigenvalues equal \(L(x_*)\). The upper bound \(F(x)\le h(x)\) becomes equality at precisely \(x_*\). This proves sharpness, uniqueness of squared radius, and the two-dimensional equality space. The even/odd lower eigenvectors of the two displayed matrices give all equality polynomials.

## Verification
Run `python3 CHECKER.py` (Python 3.10+, standard library only). It implements exact fraction-arithmetic Sturm variations, certifies all positive root counts and the three rational isolating intervals, verifies the cleared characteristic identities, and determines lower-versus-upper branches by exact rational signs. It also checks the displayed value and representative additional radii numerically. Numerical sampling alone is not used as proof of uniqueness.

## Relationship to prior work
Escudero, Haimi and Romero introduced sharp density criteria for multiple sampling and interpolation in weighted Fock spaces [1]. Their results do not supply the finite four-functional E-optimal lower frame bound or its parity crossing. Gröchenig, Romero and Stöckler studied sharp density conditions for derivative sampling in shift-invariant/Gabor models [2], a distinct function space and asymptotic criterion. Cruz, Massaneda and Ortega-Cerdà [3] treat arrays of polynomials with Bombieri norms and asymptotic geometric criteria rather than the finite Gaussian cubic two-jet extremum. The present result is an exact minimal finite instance motivated by that broader sampling theory. More directly, maximizing the determinant of this same four-functional matrix gives squared radius \(x=1\) whereas maximizing its least singular value gives \(x_*\), demonstrating why determinant criteria do not settle the stability design.

## Limitations
The statement optimizes only antipodal sites and the explicitly chosen full-Fock-normalized value/covariant-derivative measurements; it does not compare arbitrary pairs, freely weighted channels, higher polynomial degrees, or complex-phase retrieval. The root certificates establish only the claimed algebraic optimizers and their branches. Although close literature was checked, unindexed finite Hermite design formulae may exist; independent priority assessment is still needed. No independent mathematical audit has been performed.

## References
[1] L. A. Escudero, A. Haimi, J. L. Romero, *Multiple sampling and interpolation in weighted Fock spaces of entire functions*, arXiv:2004.12922, first submitted 2020-04-27; DOI: https://doi.org/10.1007/s11785-020-01065-4.

[2] K. Gröchenig, J. L. Romero, J. Stöckler, *Sharp Results on Sampling with Derivatives in Shift-Invariant Spaces and Multi-Window Gabor Frames*, 2019, DOI: https://doi.org/10.1007/s00365-019-09456-3.

[3] C. A. Cruz, X. Massaneda, J. Ortega-Cerdà, *Multiple sampling and interpolation in a space of polynomials*, arXiv:2405.19945, DOI: https://doi.org/10.1007/s00041-025-10228-w.
