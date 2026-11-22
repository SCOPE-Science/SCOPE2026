# A three-mode quartic phase-matching spectrum on complex spheres

## Finding

Let \(d\ge3\) be an integer and let \(\mathcal P_4(d)\) be the complex space of homogeneous holomorphic polynomials of degree four on \(S^{2d-1}\subset\mathbb C^d\), with Haar probability inner product. Define
\[
\Omega=\{z:\operatorname{Re}(z_1z_2\overline{z_3}^{\,2})>0\},\qquad
\langle T_\Omega f,g\rangle=\int_\Omega f(z)\overline{g(z)}\,d\sigma(z).
\]
The boundary has measure zero. With \(r=d-3\), the complete spectrum, written as paired levels \(\frac12\pm\delta\) with multiplicity for **each** sign, is

| Positive offset \(\delta\) | Multiplicity of each sign |
|---|---:|
| \(\sqrt{354}/64\) | \(1\) |
| \(\sqrt3/8\) | \(2\) |
| \(5\sqrt6/64\) | \(2\) |
| \(1/(2\sqrt6)\) | \(r\) |
| \(3/16\) | \(2r\) |
| \(1/(4\sqrt2)\) | \(r(r+1)/2\) |

There are additionally \(\binom{d+3}{4}-(d-1)(d+2)\) eigenvalues equal to \(1/2\). Multiplicities zero in a table row mean that that branch is absent. The largest and smallest eigenvalues are simple and equal to
\[
\lambda_{\max,\min}=\frac12\pm\frac{\sqrt{354}}{64}.
\]
For nonzero \(f\in\mathcal P_4(d)\), the sharp energy ratio satisfies
\[
\frac12-\frac{\sqrt{354}}{64}\le
\frac{\int_\Omega |f|^2d\sigma}{\int_{S^{2d-1}}|f|^2d\sigma}
\le\frac12+\frac{\sqrt{354}}{64}.
\]
The squared observation condition number is \(\kappa=(32+\sqrt{354})/(32-\sqrt{354})\), approximately \(3.8539594242\), in **all** dimensions \(d\ge3\).

## Assumptions and scope

The domain is a measurable half-phase region determined by the two-to-one phase-matching character \(z_1z_2\overline{z_3}^{\,2}\). We work with exact holomorphic degree four, not the direct sum of degrees through four and not the full real spherical-harmonic space. Every such holomorphic homogeneous polynomial is (complex-valued) harmonic in the underlying real coordinates. All integrals use probability-normalized surface measure. No claim is made for different polynomial degrees or non-Haar weights.

## Proof

For multiindices \(\alpha\in\mathbb N^d\) of total degree four, set \(\alpha!=\prod_j\alpha_j!\), \((d)_4=d(d+1)(d+2)(d+3)\), and
\[
 e_\alpha(z)=\sqrt{\frac{(d)_4}{\alpha!}}\,z^\alpha.
\]
These are an orthonormal basis: the squared moduli \((|z_1|^2,\ldots,|z_d|^2)\) have the Dirichlet distribution with all parameters one, and independent coordinate phases are uniform.

Put \(v=(1,1,-2,0,\ldots,0)\). For the phase variable \(\phi=\arg z_1+\arg z_2-2\arg z_3\), the Fourier coefficient of \(\mathbf1_{\{\cos\phi>0\}}\) is \(1/2\) at frequency zero, vanishes at nonzero even frequencies, and equals \((-1)^{(|j|-1)/2}/(\pi|j|)\) at odd frequencies \(j\). Therefore an off-diagonal matrix entry can be nonzero only when \(\alpha-\beta=jv\) for an odd integer \(j\). Degree four enforces \(|j|\le2\), so only \(j=\pm1\) occurs. For such pairs,
\[
\langle T_\Omega e_\alpha,e_\beta\rangle=
\frac1\pi\prod_{k=1}^d
\frac{\Gamma(1+(\alpha_k+\beta_k)/2)}{\sqrt{\alpha_k!\beta_k!}},
\]
with all diagonal entries \(1/2\). The displayed product follows by integrating phase and Dirichlet moments. The formula is independent of \(d\), including when exponents on unused coordinates agree.

Fix all exponents on coordinates \(4,\ldots,d\). The remaining three-coordinate monomials form disjoint connected chains under the step \(v\). If their total degree is four, exactly one chain has length three:
\[
 z_3^4\ \longleftrightarrow\ z_1z_2z_3^2\ \longleftrightarrow\ z_1^2z_2^2.
\]
In the corresponding ordered orthonormal basis, the centered block \(T_\Omega-\frac12I\) is
\[
B_0=\begin{pmatrix}0&a&0\\a&0&b\\0&b&0\end{pmatrix},\quad
 a=\frac{\sqrt3}{8},\quad b=\frac{9\sqrt2}{64},\quad
 s=\sqrt{a^2+b^2}=\frac{\sqrt{354}}{64}.
\]
Its eigenvalues are \(-s,0,s\). Normalized top and bottom eigenvectors are proportional to \((a,\pm s,b)\). The four remaining two-element chains of three-coordinate degree four have off-diagonal weights \(\sqrt3/8\) twice and \(5\sqrt6/64\) twice.

If exactly one quartic degree is used on coordinates \(4,\ldots,d\), there are \(r\) choices of that coordinate and the three-coordinate degree is three. Its three two-element chains have weights \(1/(2\sqrt6)\) once and \(3/16\) twice. If exactly two degrees are used outside the first three coordinates, there are \(\binom{r+1}{2}=r(r+1)/2\) external monomials, and the remaining degree-two chain has weight \(1/(4\sqrt2)\). All other monomials are isolated eigenvectors of eigenvalue \(1/2\). Counting gives \((d-1)(d+2)\) noncentral eigenvalues and the stated central multiplicity.

Finally, \(s^2=354/4096\) exceeds the square of every other listed offset. Thus the three-chain provides the unique maximal and minimal eigenlines, and their ratio yields the sharp condition number. All eigenvalues are strictly between zero and one because \(s<1/2\).

## Verification

The standalone `check.py` reconstructs the exact gamma-moment matrix from scratch, enumerates every connected exponent chain, diagonalizes each component symbolically, and checks the predicted complete spectrum for ambient dimensions three through seven. It also runs independent Gaussian-to-sphere Monte Carlo integration on the three-chain for ambient dimensions three, four, and six. The deterministic samples of size 160,000 per dimension yielded maximum entrywise errors approximately \(0.003553\), \(0.003759\), and \(0.004401\), respectively, against the exact three-chain matrix. These numerical tests illustrate rather than prove the general-dimension statement; the proof above is analytic.

Reproduce with `python check.py` using Python 3, NumPy and SymPy. The proof is standalone and does not depend on numerical sampling.

## Relationship to prior work

The structural use of torus characters and monomial moment formulas is classical. General Toeplitz descriptions for quasi-homogeneous symbols on complex projective spaces and balls appear in Morales-Ramos, Quiroga-Barranco and Sánchez-Nungaray (2017), especially their Theorem 19, and in Quiroga-Barranco (2021). Those references furnish general matrix-element machinery; the present claim is the evaluated complete quartic spectrum, first three-chain extremizing mode, all multiplicities, and sharp dimension-independent stability for the particular nonlinear phase-matching half-region. Unlike two-coordinate relative-phase windows or coordinate-modulus order cells, this mask couples three coordinates by character \((1,1,-2)\). The general formulas create a residual risk of an overlooked implicit equivalent; full historical novelty is not certified.

## Limitations

The theorem concerns exact quartic holomorphic polynomials, not all spherical harmonics of real degree four, arbitrary degree, arbitrary observation weights, or stability under geometric perturbations. The independent Monte Carlo checks have sampling error and are not proof. No external independent audit or comprehensive global-priority certification has been performed.

## References

1. R. Quiroga-Barranco, *Toeplitz operators, \(\mathbb T^m\)-invariance and quasi-homogeneous symbols*, first posted June 3, 2021, arXiv:2106.01980, https://arxiv.org/abs/2106.01980.
2. M. A. Morales-Ramos, R. Quiroga-Barranco and A. Sánchez-Nungaray, *Toeplitz Operators, Pseudo-Homogeneous Symbols, and Moment Maps on the Complex Projective Space*, Journal of Function Spaces (2017), Article 1730920, https://doi.org/10.1155/2017/1730920.
3. W. Bauer, R. Hagger and N. Vasilevski, *Algebras of Toeplitz operators on the \(n\)-dimensional unit ball*, first posted August 30, 2018, arXiv:1808.10372, https://arxiv.org/abs/1808.10372.
