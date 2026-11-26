# Sharp E-optimal two-site Hermite sampling of cubic Bargmann–Fock polynomials

## Finding

Among antipodal pairs of sites for recovering an analytic polynomial of degree at most three in the standard Gaussian Bargmann–Fock norm, the worst-case squared gain from a normalized value and covariant first derivative at each site is uniquely maximized, up to rotation, at squared radius \(x_*=1.51905535770046\ldots\). Precisely, \(x_*\) is the unique root in \((1.519055357,1.519055359)\) of
\[
Q(x)=x^6-10x^5+45x^4-111x^3+150x^2-108x+36.
\]
The optimal squared gain is
\[
e^{-x_*}\frac{8(x_*^2-3)}{(x_*-2)(x_*^2-6x_*+12)}
=0.48556146555597574\ldots.
\]
The worst-observed complex subspace at the optimum has dimension two: one even and one odd direction.

## Assumptions and scope

The space \(\mathcal P_3\) has basis \(z^j/\sqrt{j!}\), \(0\le j\le3\), orthonormal for the norm \(\|f\|^2=\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)\). For \(w\ne0\), let \(A_w f\in\mathbb C^4\) collect the functionals
\[
\ell_{\varepsilon,0}(f)=e^{-|w|^2/2}f(\varepsilon w),\qquad
\ell_{\varepsilon,1}(f)=e^{-|w|^2/2}\bigl(f'(\varepsilon w)-\varepsilon\overline w f(\varepsilon w)\bigr),\qquad \varepsilon\in\{+1,-1\}.
\]
The value-and-first-jet functionals at a single site have orthonormal representers in the full Fock space before restriction. The objective is \(\inf_{\|f\|=1}\|A_w f\|_2^2\), not the determinant or a condition-number ratio.

## Proof

After a unitary rotation take \(w=r>0\), \(x=r^2\). Direct evaluation on the basis gives \(A_r^*A_r=e^{-x}(E(x)\oplus O(x))\) in the degree order \(0,2,1,3\), where
\[
E(x)=\begin{pmatrix}2(x+1)&\sqrt2x(x-1)\\\sqrt2x(x-1)&x(x+(x-2)^2)\end{pmatrix},\quad
O(x)=\begin{pmatrix}2(x^2-x+1)&\frac{\sqrt6}{3}x(x^2-3x+3)\\\frac{\sqrt6}{3}x(x^2-3x+3)&\frac{x^2}{3}(x+(x-3)^2)\end{pmatrix}.
\]
Their trace and determinant pairs are
\[
T_E=x^3-3x^2+6x+2,\quad D_E=8x,\qquad
T_O=\tfrac13(x^4-5x^3+15x^2-6x+6),\quad D_O=\tfrac83x^3.
\]
Writing \(\lambda_E^-,\lambda_O^-\) for the smaller eigenvalues, the objective \(F(x)=e^{-x}\min(\lambda_E^-,\lambda_O^-)\) is bounded by \(h(x)=e^{-x}\lambda_O^-(x)\). The odd block has positive off-diagonal entry for \(x>0\), so its eigenvalues are simple. At an interior stationary point of \(h\), its underlying eigenvalue \(\lambda\) satisfies \(\lambda'=\lambda\). Differentiating \(\lambda^2-T_O\lambda+D_O=0\) and eliminating \(\lambda^2\) gives
\[
\lambda=\frac{2D_O-D'_O}{T_O-T'_O}=rac{8x^2(2x-3)}{x^4-9x^3+30x^2-36x+12}.
\]
The numerator's only positive zero \(3/2\) is not a zero of the denominator, so the division is valid at any positive stationary point. Substituting the quotient into the odd characteristic equation and multiplying by three times the denominator squared yields
\[
-8x^2(x^3-3x^2+6x-6)Q(x)=0.
\]
Exact rational Sturm variations, implemented in `CHECKER.py`, count two positive roots of \(Q\), one in each of \((1.519055357,1.519055359)\) and \((2.808203101,2.808203103)\), and one positive root of the cubic, in \((1.596071637,1.596071639)\). The denominator does not vanish on these intervals. The quotient minus \(T_O/2\) has sign negative throughout the first interval and positive throughout the other two. Thus any stationary point of \(h\) must be \(x_*\). Both endpoints have limit zero: at zero the odd block has zero determinant and positive trace, and at infinity the exponential dominates the polynomial entries. The positive continuous function \(h\) has an interior maximum, so \(x_*\) is its unique maximizer.

Set \(L(x)=8(x^2-3)/[(x-2)(x^2-6x+12)]\). For both parity blocks the identity is
\[
L(x)^2-T_{E/O}(x)L(x)+D_{E/O}(x)
=\frac{-8(x^2-2x+2)Q(x)}{(x-2)^2(x^2-6x+12)^2}.
\]
The denominator is nonzero at \(x_*\), and rational sign isolation gives \(L(x_*)<T_E(x_*)/2\) and \(L(x_*)<T_O(x_*)/2\). Thus both smaller eigenvalues equal \(L(x_*)\), so the upper bound \(F\le h\) is attained there. Since both block eigenvalues are simple at \(x_*\), their two lower eigenvectors span all worst-observed polynomials. The same block determinants give \(\det(A_w^*A_w)=64x^4e^{-4x}/3\), whose maximizing squared radius is \(1\), not \(x_*\).

## Verification

`python3 CHECKER.py` uses standard-library exact rational Sturm sequences for the root counts, intervals, polynomial identities and branch signs. Its floating-point output is a diagnostic, not a certificate of the last displayed decimal digits, and the proof of uniqueness uses exact branch and root comparisons. This addresses only antipodal sites and the prescribed norm and measurement channels; it does not optimize arbitrary pairs, channel weights or higher degrees.

## Relationship to other work

Escudero, Haimi and Romero develop density criteria for multiple sampling in weighted Fock spaces [1]. Gröchenig, Romero and Stöckler treat derivative sampling in shift-invariant and Gabor models [2]. Cruz, Massaneda and Ortega-Cerdà study polynomial sampling arrays with Bombieri norms [3]. The exact residue-block spectrum in [4] includes these same even and odd blocks at \(M=2\), up to an overall gain normalization, and yields the determinant optimum. Its optimization of a condition number as \(M\to\infty\) is a different objective. The contribution here is the finite cubic maximization of the lower frame bound, including which branch is active and the exact maximizing parity tie. Historical priority beyond the sources compared is not asserted.

## References

1. L. A. Escudero, A. Haimi and J. L. Romero, *Multiple sampling and interpolation in weighted Fock spaces of entire functions*, [arXiv:2004.12922](https://arxiv.org/abs/2004.12922).
2. K. Gröchenig, J. L. Romero and J. Stöckler, *Sharp Results on Sampling with Derivatives in Shift-Invariant Spaces and Multi-Window Gabor Frames*, [DOI:10.1007/s00365-019-09456-3](https://doi.org/10.1007/s00365-019-09456-3).
3. C. A. Cruz, X. Massaneda and J. Ortega-Cerdà, *Multiple sampling and interpolation in a space of polynomials*, [arXiv:2405.19945](https://arxiv.org/abs/2405.19945).
4. [*Sharp exponential conditioning barrier for first-jet circular Bargmann–Fock sampling*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-sharp-exponential-conditioning-barrier-for-first-jet-circular-ba--8c65d58f8940), exact cyclic singular spectrum and determinant theorem.
