# Sharp small-aperture E-observability with two radial Zernike bands

## Finding
Let \(\mathcal P_2\) be the complex polynomial space \(\{p(t):\deg p\le2\}\), equipped with \(\|p\|^2=\int_0^1|p(t)|^2\,dt\). For \(0<q<1\), let \(\mathcal E_{2,q}\) consist of subsets of \([0,1]\) that are unions of at most two disjoint closed intervals with total length \(q\), and put
\[
\Lambda(E)=\min_{\substack{p\in\mathcal P_2\\\|p\|=1}}\int_E|p(t)|^2\,dt,
\qquad M_2(q)=\sup_{E\in\mathcal E_{2,q}}\Lambda(E).
\]
**Sharp two-band asymptotic:**
\[
\boxed{\lim_{q\downarrow0}\frac{M_2(q)}{q^3}=\frac{5+3\sqrt5}{2}.}
\]
The coefficient is attained asymptotically by two bands centered at
\[
x_* = \frac{1-5^{-1/4}}2,\qquad y_* = \frac{1+5^{-1/4}}2,
\]
with lengths \(q^2\) and \(q-q^2\), respectively. Conversely, every sequence of admissible two-band masks with \(\Lambda(E_q)/q^3\to(5+3\sqrt5)/2\) must, up to interchanging bands, have centers tending to \(x_*,y_*\) and a short-band length fraction tending to zero. In particular, an asymptotically optimal two-band observation is intrinsically *unbalanced*.

The explicit finite-area bound
\[
\boxed{M_2(q)\le\frac{5+3\sqrt5}{2}q^3+\frac94q^5}
\]
holds for all \(0<q<1\). For comparison, every single interval captures at most \(O(q^5)\) of the energy of some unit-norm quadratic polynomial; two separated bands improve the best attainable power of the smallest concentration eigenvalue from five to three.

## Assumptions and scope
The normalized unit-disk radial coordinate is \(t=|z|^2\), for which disk area probability pushes forward to uniform \(dt\) on \([0,1]\). Consequently \(\mathcal P_2\) is exactly the three-mode axisymmetric Zernike space \(\operatorname{span}\{1,\,2|z|^2-1,\,6|z|^4-6|z|^2+1\}\), with orthonormalized coefficients available through shifted Legendre polynomials. Each interval in \(t\) is a concentric disk or annulus; the short-band construction uses two annuli away from the center. The observation is continuous, noiseless area restriction, and the objective is the *smallest squared singular value* of that restriction operator, not its largest eigenvalue or determinant. The theorem is for fixed radial degree two as the total observed area fraction \(q\) tends to zero; it does not optimize general measurable masks or arbitrary nonradial Zernike modes.

## Proof
**1. A polynomial testing every two-band mask.** Write the two interval lengths as \(\ell_1,\ell_2\ge0\), their centers as \(a,b\in[0,1]\), and \(\ell_1+\ell_2=q\). For a single interval we may formally add an interval of zero length and assign its center arbitrarily. Consider the monic quadratic \(P_{a,b}(t)=(t-a)(t-b)\). Centered integration, including the degenerate-length case, gives the *exact* identity
\[
\int_E P_{a,b}(t)^2\,dt
=\frac{(a-b)^2}{12}(\ell_1^3+\ell_2^3)
+\frac1{80}(\ell_1^5+\ell_2^5).
\tag{1}
\]
Here and below complex coefficients cause no change to a real polynomial trial-vector upper bound. Its full norm is
\[
D(a,b)=\int_0^1(t-a)^2(t-b)^2\,dt.
\]
Every monic quadratic has squared norm at least \(1/180\), because the monic shifted Legendre polynomial \(t^2-t+1/6\) is orthogonal to the lower degrees and has exactly that norm. Therefore \(D(a,b)\ge1/180\).

**2. Exact optimization of the normalized separation factor.** Put \(a=1/2+s-h\) and \(b=1/2+s+h\), so \(|s|+|h|\le1/2\). Direct integration yields
\[
D(a,b)=\frac1{80}+\frac{s^2}{2}-\frac{h^2}{6}+(s^2-h^2)^2.
\tag{2}
\]
At each fixed \(z=h^2\in[0,1/4]\), (2) is nondecreasing in \(s^2\), since its derivative with respect to \(s^2\) is \(1/2+2(s^2-z)\ge0\), with strict positivity at the interior optimal \(z\). Thus the ratio \((a-b)^2/D(a,b)\) is largest at \(s=0\). There it equals
\[
R(z)=\frac{4z}{z^2-z/6+1/80}.
\]
The derivative of \(R\) has the sign of \(1/80-z^2\). The unique maximum on \([0,1/4]\) occurs at \(z=1/(4\sqrt5)\), and its value is
\[
\boxed{\max_{0\le a,b\le1}\frac{(a-b)^2}{D(a,b)}=30+18\sqrt5.}
\tag{3}
\]
Equality requires the unordered centers to be exactly \(\{x_*,y_*\}\).

**3. Uniform finite-area upper bound.** Insert the unit-normalized trial polynomial into the variational minimum. From (1), (3), \(\ell_1^3+\ell_2^3\le q^3\), \(\ell_1^5+\ell_2^5\le q^5\), and \(D\ge1/180\),
\[
\Lambda(E)\le\frac{30+18\sqrt5}{12}q^3+\frac{180}{80}q^5
=\frac{5+3\sqrt5}{2}q^3+\frac94q^5.
\]
The estimate holds for each admissible mask and hence for the supremum.

**4. Matching two-annulus construction.** Fix \(a=x_*\), \(b=y_*\), and define for sufficiently small \(q>0\)
\[
E_q=\left[a-\frac{q^2}{2},a+\frac{q^2}{2}\right]
\cup\left[b-\frac{q-q^2}{2},b+\frac{q-q^2}{2}\right].
\tag{4}
\]
Both intervals lie strictly inside \((0,1)\), are disjoint, and have total length \(q\). In the real orthonormal Legendre coefficient basis, set
\[
v(t)=\begin{pmatrix}1\\\sqrt3(2t-1)\\\sqrt5(6t^2-6t+1)\end{pmatrix},
\qquad G_q=\int_{E_q}v(t)v(t)^T\,dt.
\]
Because \(v(a)\) and \(v(b)\) are linearly independent, their common orthogonal complement is a line spanned by a unit vector \(n\), whose polynomial is \(P_{a,b}/\sqrt{D(a,b)}\). On \(U=\operatorname{span}\{v(a),v(b)\}\), centered Taylor expansion of the two integrals gives
\[
G_q|_U\succeq c q^2 I_U\quad\text{for some fixed }c>0,
\qquad \|P_U G_q n\|=O(q^3).
\]
(The first bound follows from the leading positive forms \((q-q^2)v(b)v(b)^T+q^2v(a)v(a)^T\); the second from symmetric integration, because the two point-evaluation contributions annihilate \(n\).) The Rayleigh quotient on \(n\), by (1), is
\[
n^T G_qn=\frac{(a-b)^2}{12D(a,b)}q^3+O(q^4)
=\frac{5+3\sqrt5}{2}q^3+O(q^4).
\]
The off-diagonal Schur correction to the least eigenvalue is at most \(O(q^6)/\Omega(q^2)=O(q^4)\). Equivalently, use the min-max characterization with the above orthogonal splitting. Thus
\[
\lambda_{\min}(G_q)=\frac{5+3\sqrt5}{2}q^3+O(q^4),
\]
which matches the uniform upper bound.

**5. Necessary unbalanced geometry.** Suppose \(E_q\) attains the sharp leading coefficient asymptotically. Using the unrelaxed test-polynomial bound (1) and dividing by \(q^3\) gives
\[
\frac{\Lambda(E_q)}{q^3}
\le\frac{1}{12}\frac{(a-b)^2}{D(a,b)}
\frac{\ell_1^3+\ell_2^3}{(\ell_1+\ell_2)^3}+O(q^2).
\]
The first factor has a unique maximizing unordered pair by (3), and the length factor is at most one, equaling one precisely when one fractional length is zero. Compactness therefore forces the claimed limiting centers and an asymptotically vanishing short-band fraction. The chosen construction satisfies these necessary conditions and realizes equality in the leading term.

**6. Single-band comparison.** For a single interval centered at \(a\) of length \(q\), test with \((t-a)^2\); its observed squared energy is exactly \(q^5/80\), while its full squared norm has a positive minimum over \(a\in[0,1]\). Hence the best single-band smallest eigenvalue is \(O(q^5)\), versus the sharp two-band \(\Theta(q^3)\). This comparison establishes the improvement in *power*, without claiming an exact optimal single-band constant here.

## Verification
The standalone `verify.py` reconstructs the monic-quadratic moment and interval identities with SymPy, checks the exact radical maximizer and minimal monic norm, forms three-by-three concentration matrices through direct analytic polynomial antiderivatives, and tests the sharp two-annulus family with 65-digit mpmath arithmetic at seven decreasing areas. A fixed-seed sweep of admissible disjoint interval pairs checks the finite-area upper bound. It reports `TWO_BAND_RADIAL_CHECKS_PASS 195`. These are finite arithmetic checks, not a substitute for the all-parameter proof above.

## Relationship to prior work
Reuter and Schwabe (2023, first public 25 March 2023) analyze *D-optimal* bounded-density subsampling for quadratic regression, prove that its unconstrained support has at most three intervals, and explicitly identify extending their theory to E-optimality as a different direction (concluding remarks). Their determinant criterion and unrestricted support geometry do not provide a two-component, smallest-eigenvalue small-area constant or a vanishing-width satellite law. Huang (arXiv:2308.03543v1, first posted 7 August 2023) develops Slepian concentration for polynomial spaces on balls, primarily in the growing-polynomial-band regime, without this fixed-three-mode shrinking two-band minimax. The subsequent 2023/2024 annular Zernike work of Papadopoulos and colleagues develops annulus-adapted polynomial methods, not sharp two-window E-concentration.

The previously recorded thin-*single*-annulus Zernike calculation on the same radial polynomial space has a \(q^5\) least-eigenvalue order, not a universal two-band bound or satellite geometry. A separate low-degree radial-ball moment classification concerns a *two*-dimensional radial subspace and the *largest* concentration eigenvalue; neither statement implies the present three-dimensional least-eigenvalue design. The leading monic polynomial, Taylor expansion, and Schur complement are classical ingredients; originality is claimed only for their sharp synthesis into the explicitly constrained two-band result. An independently discovered equivalent in experimental-design or optical-mask literature remains possible.

## Limitations
Only the three axisymmetric disk Zernike modes and two connected radial observation components are treated. No claim is made that the construction is an exact maximizer at any fixed positive \(q\), nor that the optimal finite-\(q\) aperture has a unique shape. The vanishing satellite is a leading-order necessary feature, not a prescribed optimal rate for its length. No claim is made about general 2-D polynomial regression designs, E-optimality without the two-interval constraint, multiband higher radial degrees, or nonuniform noise. The proof assumes Lebesgue-normalized disk area and noiseless continuous observation. Historical originality is supported by the inspected comparisons, not independently certified.

## References
1. T. Reuter and R. Schwabe, *Optimal subsampling design for polynomial regression in one covariate*, Statistical Papers 64 (2023), 1095–1117, first published 25 March 2023. https://doi.org/10.1007/s00362-023-01425-0.
2. X. Huang, *Slepian concentration problem for polynomials on the unit Ball*, arXiv:2308.03543v1, first posted 7 August 2023. https://arxiv.org/html/2308.03543v1.
3. I. P. A. Papadopoulos, T. S. Gutleb, R. M. Slevinsky, and S. Olver, *Building hierarchies of semiclassical Jacobi polynomials for spectral methods in annuli*, arXiv:2310.07541, 11 October 2023. https://arxiv.org/abs/2310.07541.
4. D. Ramos-López, M. A. Sánchez-Granero, M. Fernández-Martínez, and A. Martínez-Finkelshtein, *Optimal sampling patterns for Zernike polynomials*, arXiv:1511.00449, 2015. https://arxiv.org/html/1511.00449v1.
