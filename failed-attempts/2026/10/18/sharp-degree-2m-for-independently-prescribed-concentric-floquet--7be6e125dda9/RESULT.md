# Sharp degree \(2m\) for independently prescribed concentric Floquet and period data

## Finding
For every integer \(m\ge1\), every collection of distinct radii \(0<r_1<\cdots<r_m\), every collection of physical periods \(T_i>0\), and every collection of positive, nonunit transverse Floquet multipliers \(\mu_i\in(0,\infty)\setminus\{1\}\), there exists a **real planar polynomial vector field of total degree exactly \(2m\)** having each circle
\[
C_i=\{(x,y)\in\mathbb R^2:x^2+y^2=r_i^2\}
\]
as a hyperbolic periodic trajectory of least physical period \(T_i\) and transverse Floquet multiplier exactly \(\mu_i\). The minimum possible polynomial degree among all such fields is exactly \(2m\), even without any symmetry assumption. The signs of the multipliers relative to one can be chosen independently, so adjacent specified circles can both attract or both repel.

**Scope of the existential statement:** the designated circles must occur with the specified data; **other periodic orbits or invariant sets are allowed**. The result is not a claim that they comprise the complete set of limit cycles, nor that a single global flow is complete in both time directions.

## Assumptions and scope
For a polynomial field \(X=(P,Q)\), its degree is \(\max\{\deg P,\deg Q\}\). The nontrivial Floquet multiplier of a hyperbolic planar periodic orbit is the positive derivative of its local transverse first-return map after one least period; attraction corresponds to \(0<\mu<1\), repulsion to \(\mu>1\). Radii must be strictly positive and distinct; the circles share center \((0,0)\). No restriction is placed on additional closed trajectories. The polynomial coefficients are permitted to be arbitrary real numbers depending on the supplied data.

Let
\[
s_i=r_i^2,\quad F(s)=\prod_{i=1}^m(s-s_i),\quad
\omega_i=\frac{2\pi}{T_i},\quad \ell_i=\log\mu_i.
\]
Every \(F'(s_i)\) is nonzero. Select a real number \(K>0\) satisfying
\[
K>\max_{1\le i\le m}
\frac{|\ell_i|\omega_i}{4\pi r_i|F'(s_i)|},
\]
and put
\[
w_i=-\frac{\ell_i\omega_i}{4\pi K r_iF'(s_i)},
\quad
\alpha_i=\omega_i\frac{1+w_i^2}{1-w_i^2},
\quad
\beta_i=\frac{2\omega_i w_i}{r_i(1-w_i^2)}.
\]
Here \(|w_i|<1\). Let \(A,B\in\mathbb R[s]\) be the Lagrange interpolation polynomials of degree at most \(m-1\) with \(A(s_i)=\alpha_i\) and \(B(s_i)=\beta_i\). These data explicitly determine the field
\[
\boxed{
\begin{aligned}
\dot x&=K F(x^2+y^2)-y\bigl(A(x^2+y^2)+xB(x^2+y^2)\bigr),\\
\dot y&=x\bigl(A(x^2+y^2)+xB(x^2+y^2)\bigr).
\end{aligned}}
\]

## Proof
**1. Algebraic degree and the invariant circles.** Write \(s=x^2+y^2\). Because \(\deg F=m\) and \(\deg A,\deg B\le m-1\), both Cartesian components have total degree at most \(2m\). On \(y=0\), the first component equals \(KF(x^2)\), whose highest-degree term is \(Kx^{2m}\). Thus the field has total degree **exactly** \(2m\), not merely at most that degree.

For \(r>0\), set \(x=r\cos\theta\), \(y=r\sin\theta\). Direct differentiation gives
\[
\dot r=K F(r^2)\cos\theta,
\qquad
\dot\theta=A(r^2)+r\cos\theta B(r^2)
-\frac{KF(r^2)}r\sin\theta.
\]
On the circle \(r=r_i\), the radial velocity vanishes, while
\[
\dot\theta=\alpha_i+r_i\beta_i\cos\theta.
\]
The definitions imply
\[
\alpha_i>r_i|\beta_i|,\qquad
\alpha_i^2-r_i^2\beta_i^2=\omega_i^2.
\]
Hence the angular speed is strictly positive, the circle is a regular periodic orbit traversed once per turn, and the classical integral
\[
\int_0^{2\pi}\frac{d\theta}{a+b\cos\theta}
=\frac{2\pi}{\sqrt{a^2-b^2}}
\quad(a>|b|)
\]
gives its **least physical period** exactly \(2\pi/\omega_i=T_i\).

**2. Exact transverse multiplier.** Linearize the scalar radial equation with \(\theta\) as independent variable. Since \(F(r_i^2)=0\), the derivative of the angular denominator does not enter the first radial variation. The logarithm of the transverse return derivative is
\[
\begin{aligned}
\Lambda_i
&=2Kr_iF'(s_i)
 \int_0^{2\pi}\frac{\cos\theta\,d\theta}
 {\alpha_i+r_i\beta_i\cos\theta}\\
&=\frac{4\pi K F'(s_i)}{\beta_i}
 \left(1-\frac{\alpha_i}{\omega_i}\right)\\
&=-\frac{4\pi K r_i^2 F'(s_i)\beta_i}
 {\omega_i(\alpha_i+\omega_i)}.
\end{aligned}
\]
The middle expression is interpreted by its continuous limit when \(\beta_i=0\); in the stipulated hyperbolic case \(\ell_i\ne0\), so in fact \(\beta_i\ne0\). Substituting the displayed interpolation data simplifies exactly to
\[
\Lambda_i=-\frac{4\pi K r_iF'(s_i)}{\omega_i}w_i
=\ell_i=\log\mu_i.
\]
Consequently the transverse multiplier is \(e^{\Lambda_i}=\mu_i\ne1\). Each specified circle is hyperbolic, and therefore an isolated periodic orbit. This construction establishes the upper bound and all independent data prescriptions.

**3. Universal lower degree bound.** Suppose conversely that a real polynomial field \((P,Q)\) of degree \(d\le2m-1\) has all these circles as nonstationary periodic orbits. Its radial polynomial
\[
R(x,y)=xP(x,y)+yQ(x,y)
\]
vanishes on every prescribed circle and satisfies \(\deg R\le2m\) and \(R(0,0)=0\).

Here is an elementary proof of the required divisibility, avoiding any genericity assumption. Fix \(i\) and divide \(R\) by the monic polynomial \(y^2+x^2-s_i\) in \(\mathbb R[x][y]\):
\[
R(x,y)=(y^2+x^2-s_i)S(x,y)+U(x)y+V(x).
\]
For each \(x\) in \((-r_i,r_i)\), both \(y=\pm\sqrt{s_i-x^2}\) lie on the circle. Since \(R\) vanishes there, subtraction of the two resulting equations forces \(U(x)=0\) on an open interval, and addition then forces \(V(x)=0\) there. Thus \(U=V=0\) as polynomials and \(y^2+x^2-s_i\) divides \(R\). These factors for different \(i\) are pairwise coprime because they differ by nonzero constants. Their product \(F(x^2+y^2)\), of degree \(2m\), consequently divides \(R\). Therefore \(R=cF(x^2+y^2)\) for some constant \(c\); evaluating at the origin, where \(F(0)\ne0\), forces \(c=0\). Hence
\[
xP+yQ\equiv0.
\]
This identity makes every origin-centered circle invariant. Because the prescribed circle is a nonstationary periodic orbit, its continuous angular velocity is everywhere nonzero and has fixed sign. Compactness and continuity then give an entire annulus of nearby circles with the same nonzero angular-velocity sign. All those nearby circles are periodic, so the prescribed orbit is not isolated and cannot be hyperbolic: contradiction. Thus \(d\ge2m\).

Combined with the constructive upper bound, the minimum degree equals \(2m\).

## Verification
The standalone standard-library program `verify.py` constructs the interpolants for ten independent data cases with \(1\le m\le5\), including alternating and all-attracting Floquet signs. It expands both Cartesian polynomial components and checks their highest nonzero expanded monomial degree numerically, circle invariance by independent Cartesian evaluation, angular speeds, periods and Floquet exponents by numerical quadrature. For two neighboring attracting cycles it also integrates the **nonlinear** radial Poincaré equation through a complete turn and checks the observed return derivatives against the prescribed multipliers. Run `python verify.py` in the directory containing this file. Expected output:

`VERIFY_OK: 30 period, Floquet and circle conditions; 10 polynomial degree checks; 2 nonlinear Poincare returns`

The universal degree obstruction and arbitrary-real-data interpolation are proved algebraically above; bounded examples and numerical quadrature do **not** certify those universal statements.

## Relationship to prior work
Christopher (2001) already gives a **degree-equal-to-algebraic-curve-degree** construction of limit cycles for nonsingular curves. In the present case the product of the circle equations has degree \(2m\), so achieving that degree **without** prescribing temporal or transverse data is not new. The distinct claim here is exact, independent control of the numerical least periods and nonunit Floquet multipliers **at the same sharp degree**, together with the elementary lower-degree obstruction for this particular geometry. The accessible Christopher abstract does not state such parameter control; its full proof was not available for comparison.

Llibre and Rodríguez (2004) construct general finite configurations. Margalef-Bentabol and Peralta-Salas (2015 preprint; 2016 journal) prescribe periods and hyperbolicity with degree below \(2(n+r)\), and separately prescribe arbitrary stabilities with a larger bound; their stronger **whole-limit-set realization** requirement is different from the present containment requirement. Theorem 2.1 specializes to degree at most \(2m+1\) for nested circles. Theorem 4.2 gives an upper bound below \(2(3m+1)\) for prescribed periods and stability types when the specified circles are exactly the limit cycles. Neither theorem states arbitrary **numerical Floquet multipliers** with total degree \(2m\). Nicklason (2016), Sections 5–6, treats related concentric invariants in generalized-cubic families; it does not establish this all-size, all-Floquet-data optimal degree theorem. The radial-factorized/equivariant constructions in Fei (2026 preprint) impose a symmetry restriction absent here.

## Limitations
Additional attracting or repelling periodic orbits may occur between or outside the designated circles; indeed, adjacent specified attracting circles may force additional intervening dynamics. No claim is made about the number, location or period of unprescribed orbits. The theorem addresses centered **circles**, not arbitrary disjoint ovals, arbitrary centers, or chosen multiplicities of nonhyperbolic cycles. Coefficients may be transcendental. The originality assessment is based on inspected primary literature and available searchable records, and does not establish historical uniqueness; a missing detailed earlier calculation could overlap with the result.

## References
1. C. Christopher, *Polynomial Vector Fields with Prescribed Algebraic Limit Cycles*, Geometriae Dedicata 88 (2001), 255–258, DOI: 10.1023/A:1013171019668.
2. J. Llibre and G. Rodríguez, *Configurations of limit cycles and planar polynomial vector fields*, Journal of Differential Equations 198 (2004), 374–380, DOI: 10.1016/j.jde.2003.10.008.
3. J. Margalef-Bentabol and D. Peralta-Salas, *Realization problems for limit cycles of planar polynomial vector fields*, arXiv:1507.00698v1 (first public 2015-07-02), Theorems 2.1, 4.2 and 5.2; Journal of Differential Equations 260 (2016), 3844–3859.
4. G. R. Nicklason, *Homogeneous-Like Generalized Cubic Systems*, International Journal of Differential Equations (2016), Article 7640340, DOI: 10.1155/2016/7640340, Sections 5–6.
5. S. Fei, *Algebraic Synthesis of Polynomial Vector Fields with Prescribed Invariant Spheres*, preprint posted 2026-09-21, doi unavailable; https://www.preprints.org/manuscript/202609.1834.
