# The characteristic-seven dual of Klein's quartic is a four-cuspidal quintic

## Finding
Let \(k=\overline{\mathbb F}_7\), and let \(C\subset\mathbb P^2_k\) be the coefficientwise reduction of the classical plane Klein quartic
\[
F=x^3y+y^3z+z^3x=0.
\]
In dual coordinates \([a:b:c]\), the closure of the tangent lines at smooth points of \(C\) is the **irreducible rational quintic**
\[
\boxed{C^\vee: \quad a^3c^2-3a^2b^3+2b^2c^3=0.}
\]
Its complete geometric singular locus comprises the three coordinate vertices, each a cusp with characteristic pair \((2,3)\) and delta invariant \(1\), and the point \([1:2:4]\), a unibranch cusp with characteristic pair \((2,7)\) and delta invariant \(3\). The arithmetic genus is \(6\), so these four cusps exhaust the genus defect. The normalization is \(\mathbb P^1_{\mathbb F_7}\). Since all cusps are rational and unibranch, for each integer \(m\ge1\),
\[
\#C^\vee(\mathbb F_{7^m})=7^m+1,
\qquad
Z(C^\vee/\mathbb F_7,T)=\frac{1}{(1-T)(1-7T)}.
\]

## Assumptions and scope
The *projective dual* means the Zariski closure of the image of the Gauss map from the smooth locus of the displayed, possibly singular, **plane model**. Dual coordinates \([a:b:c]\) represent lines \(ax+by+cz=0\). A characteristic pair means the valuations of a local parameter and a transverse coordinate on the normalization. All geometric classifications are over \(\overline{\mathbb F}_7\). The arithmetic formulas use the particular \(\mathbb F_7\)-model and all its finite extensions; they do not compute a stable reduction of the generic smooth Klein quartic.

## Proof
**1. Normalizing the plane quartic.** Introduce a parameter \(r\) on \(\mathbb P^1\), and define degree-four forms in its affine chart by
\[
\begin{aligned}
X(r)&=r^4+r^2-r-3,\\
Y(r)&=2r^4+r^2-2r+2,\\
Z(r)&=-3r^4+r^2+3r+1.
\end{aligned}
\]
Their degree-four homogenizations have no common projective zero. Exact arithmetic in characteristic seven gives \(F(X,Y,Z)=0\). The coefficient matrix of the six quadratic forms \(X^2,XY,XZ,Y^2,YZ,Z^2\) in powers \(r^0,\ldots,r^5\) has determinant \(6\) modulo seven. Hence there is no conic, and in particular no line, through the parametrized image. For a basepoint-free map given by quartics, the degree of the image times its generic mapping degree is \(4\). The image is therefore an irreducible quartic, and the map has degree one. Since the image lies on \(F=0\), this proves \(F\) irreducible and the parametrization is the normalization of \(C\).

One way to discover the forms is to project the quartic from \([1:2:4]\). Lines of slope \(t\) through that point yield, after removing the base double intersection, the quadratic
\[
 t u^2+(t^3-t-3)u-2t^2-2t+3=0,
\]
whose discriminant factors over \(\mathbb F_7\) as \((t+1)(t-3)^5\). The substitution \(t=(3r^2+1)/(r^2-1)\) rationalizes the resulting double cover; the displayed quartic forms give its basepoint-free projectivization. The identities and nondegeneracy checks above stand independently as a proof of the asserted parametrization.

**2. The exact Gauss image.** On the smooth locus the tangent-line coordinates are the cross product of the parameterized point and its derivative. Directly reducing the three cross products modulo seven gives
\[
\begin{aligned}
A(r)&=-3r^5+3r^3+2r^2+2r+1,\\
B(r)&=r^5+3r^3-3r^2+r+1,\\
C(r)&=2r^5+3r^3+r^2-3r+1.
\end{aligned}
\]
These three quintics have no common zero, including at infinity. The coefficient matrix in powers \(r^0,r^1,r^2\) has determinant \(4\) modulo seven; hence their image is not a line. They satisfy the explicit polynomial identity
\[
A^3C^2-3A^2B^3+2B^2C^3=0\quad\text{in }\mathbb F_7[r].
\]
As the three quintic forms define a basepoint-free map, the degree of its image times the map degree is \(5\). The image cannot be a line; therefore it is an irreducible quintic and the map has degree one. The displayed degree-five equation is its complete equation because its degree equals the degree of the irreducible image. In particular, this map normalizes the dual curve and the Gauss map is generically birational and separable.

**3. The four cusp singularities.** The dual equation has zero gradient at \([1:0:0]\), \([0:1:0]\), \([0:0:1]\), and \([1:2:4]\). In affine charts at the respective coordinate vertices, its lowest-weight terms have the forms
\[
 w^2-3v^3,\qquad -3u^2+2w^3,\qquad 2v^2+u^3,
\]
with the other terms of strictly higher weight, so these are ordinary \((2,3)\) cusps, each of delta invariant one (characteristic seven is prime to two and three).

For the fourth point, the quintic parametrization has leading-coefficient ratio \([A:B:C]=[4:1:2]=[1:2:4]\) at \(r=\infty\). The polynomials \(B-2A\) and \(C-4A\) have greatest common divisor one over \(\mathbb F_7[r]\), so no finite parameter maps to that point. Write \(s=1/r\) and local coordinates \(u=b/a-2\) and \(v=c/a-4\). Exact formal expansion in \(\mathbb F_7[[s]]\) gives
\[
 u=s^2+2s^4+s^5+\cdots,
 \qquad
 v-3u-3u^2-5u^3=3s^7+O(s^8).
\]
Thus the unique branch has characteristic pair \((2,7)\) and delta invariant three. (Because two is invertible, replacing \(s\) by a formal parameter whose square is \(u\) justifies the standard two-generator semigroup argument even in characteristic seven.)

The arithmetic genus of an integral plane quintic is \((5-1)(5-2)/2=6\). The displayed four unibranch cusps contribute \(1+1+1+3=6\), the entire genus defect because the normalization has genus zero. Therefore there are **no further geometric singularities**. Every singular point has one geometric normalization preimage, all defined over \(\mathbb F_7\), giving the stated extension-field point counts and zeta function.

## Verification
Run `python3 verify_klein7_dual.py` with SymPy installed. The script checks all polynomial identities over \(\mathbb F_7\), the basepoint-free conditions, rank witnesses preventing lower-degree images, the Gauss map, the implicit quintic, the four singular-point Jacobian equations, the absence of a second preimage at the exceptional point, and the local \((2,7)\) valuation certificate. Exact ranks and polynomial identities are finite proofs of the stated computational subclaims. The geometric conclusions about irreducibility, normalization, cusps and exhaustion use the algebraic arguments above, not finite point-count extrapolation. The verifier ends with `VERIFY_OK`.

## Relationship to prior work
Elkies establishes the classical Klein quartic and discusses its exceptional behavior at seven; he also distinguishes coefficientwise models from potentially good reduction after ramified extension. Bauer–Di Rocco–Harbourne–Huizenga–Seceleanu–Szemberg explicitly analyze the *Klein line configuration* in characteristic seven, rather than the dual of the singular Klein plane quartic. Pokora and Roé analyze the gradient map, Hessian and dual of the **smooth complex** quartic, where the geometry is different. Dolgachev and Martin record that the classical quartic equation fails smoothness at seven. None of the inspected material states the displayed degree-five dual equation or its four characteristic-seven cusps. The known singular normalization of the original plane quartic and its Hessian intersection do not, by themselves, provide the explicit dual quintic and its complete singularity profile.

## Limitations
This result concerns only the coefficientwise plane-model reduction at seven, not the canonical smooth reduction over a ramified base change. It does not assert priority over all historical work on modular dual curves, and an implicit appearance of the same quintic in older literature remains possible. The proof uses exact arithmetic in the specified coordinate system; the equation is not asserted to be characteristic-independent.

## References
N. D. Elkies, *The Klein Quartic in Number Theory*, in *The Eightfold Way* (1999), pp. 51–102, open-access text at https://library.slmath.org/books/Book35/files/elkies.pdf.

T. Bauer, S. Di Rocco, B. Harbourne, J. Huizenga, A. Seceleanu and T. Szemberg, *Negative curves on symmetric blowups of the projective plane, resurgences and Waldschmidt constants*, arXiv:1609.08648v1, first posted 2016-09-27, especially §§2.4 and 9.

P. Pokora and J. Roé, *The 21 reducible polars of Klein's quartic*, arXiv:1803.06411v2 (2018), particularly the discussion of the characteristic-zero gradient and dual maps.

I. Dolgachev and G. Martin, *Automorphisms of del Pezzo surfaces in odd characteristic*, Journal of the London Mathematical Society (2024), theorem on the Klein plane quartic in odd characteristic.
