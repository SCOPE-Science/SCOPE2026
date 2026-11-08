# An exact orthogonality wall for minimal-degree concentric cycles

## Finding
Fix an integer \(m\ge2\) and distinct radii \(0<r_1<\cdots<r_m\). Put
\[
F(s)=\prod_{j=1}^m(s-r_j^2),\qquad s=x^2+y^2.
\]
Let \(v=(v_1,v_2)\in\mathbb R^2\setminus\{0\}\), \(w=(w_1,w_2)\in\mathbb R^2\setminus\{0\}\), \(h=\|w\|>0\), and \(c>h r_m\). Consider the degree-\(2m\) polynomial flow
\[
\begin{aligned}
\dot x&=v_1F(x^2+y^2)+(c+w_1x+w_2y)y,\\
\dot y&=v_2F(x^2+y^2)-(c+w_1x+w_2y)x.
\end{aligned}
\tag{1}
\]
For each \(i=1,\ldots,m\), the circle \(\Gamma_i=\{x^2+y^2=r_i^2\}\) is a periodic orbit of exact physical-time period
\[
T_i=\frac{2\pi}{\sqrt{c^2-h^2r_i^2}}.
\]
Its transverse Floquet exponent per revolution (the natural logarithm of its positive transverse multiplier) is exactly
\[
\boxed{\Lambda_i=\frac{4\pi(v\cdot w)}{h^2}F'(r_i^2)
\left(1-\frac{c}{\sqrt{c^2-h^2r_i^2}}\right).}\tag{2}
\]
Consequently, **all \(m\) prescribed circles are hyperbolic limit cycles if and only if \(v\cdot w\ne0\)**. For positive \(v\cdot w\), the outermost circle attracts transversely and their stability alternates inward; for negative \(v\cdot w\), all those stabilities reverse. At precisely \(v\cdot w=0\), **each** \(\Gamma_i\) is contained in a two-sided annulus of nonisolated periodic orbits, and there is an explicit local real-analytic first integral regular across \(\Gamma_i\). No concentric invariant circles other than the \(\Gamma_i\) occur in (1).

This construction is degree-optimal: every nonzero real planar polynomial vector field with \(m\) distinct concentric **limit cycles** has degree at least \(2m\). This degree bound is classical; the quantitative result here concerns the simultaneous orthogonality transition, its analytically integrable wall, and the exact common-parameter dependence of the physical periods and multipliers.

## Assumptions and scope
The radii are arbitrary prescribed positive distinct numbers, \(m\ge2\), and \(c>\|w\|r_m\) ensures strictly monotone angular motion on all listed circles. All time, period and Floquet statements concern the original unrescaled continuous-time flow. The circle can attract or repel transversely without global convergence being claimed. A limit cycle means an isolated periodic trajectory; at \(v\cdot w=0\) the circles are periodic but are not limit cycles. The polynomial degree refers to the maximum total degree of its two right-hand sides.

## Proof
**1. Rotation and invariant circles.** Set \(\xi=(w_1x+w_2y)/h\) and \(\eta=(-w_2x+w_1y)/h\), an orientation-preserving rotation. Set \(\varepsilon=(v\cdot w)/h\) and \(\beta=(-w_2v_1+w_1v_2)/h\). In these coordinates, \(s=\xi^2+\eta^2\), \(C=c+h\xi\), and (1) becomes
\[
\dot\xi=\varepsilon F(s)+C\eta,\qquad
\dot\eta=\beta F(s)-C\xi.\tag{3}
\]
Thus \(\dot s=2F(s)(\varepsilon\xi+\beta\eta)\), so the \(m\) circles are invariant. On a circle, write \(\xi=r_i\cos\theta\), \(\eta=r_i\sin\theta\). Then \(\dot\theta=-(c+h r_i\cos\theta)<0\), and
\[
T_i=\int_0^{2\pi}\frac{d\theta}{c+h r_i\cos\theta}
=\frac{2\pi}{\sqrt{c^2-h^2r_i^2}}.
\]
If another centered circle were invariant, its fixed positive radius \(r\) would satisfy \(F(r^2)(\varepsilon\cos\theta+\beta\sin\theta)=0\) for all \(\theta\). Since \((\varepsilon,\beta)\ne(0,0)\), \(F(r^2)=0\), giving precisely the listed circles.

**2. Exact Floquet exponent and stability.** Linearization of the exact radial equation for \(s\) at \(s_i=r_i^2\) gives \(\dot{\delta s}=2F'(s_i)(\varepsilon\xi_i(t)+\beta\eta_i(t))\delta s\). The normal coordinate \(s-s_i\) is valid in a tubular neighborhood, so this coefficient determines the nontrivial planar Floquet multiplier. Following one clockwise revolution yields
\[
\Lambda_i=2F'(s_i)r_i\int_0^{2\pi}
\frac{\varepsilon\cos\theta+\beta\sin\theta}
{c+h r_i\cos\theta}\,d\theta.
\]
The sine integral is zero by periodic differentiation of \(\log(c+h r_i\cos\theta)\), and direct algebra with the standard positive cosine-denominator integral gives
\[
\int_0^{2\pi}\frac{\cos\theta\,d\theta}{c+h r_i\cos\theta}
=\frac{2\pi}{h r_i}\left(1-\frac{c}{\sqrt{c^2-h^2r_i^2}}\right).
\]
Substitute \(\varepsilon=(v\cdot w)/h\) to get (2). The parenthesized term is strictly negative, while \(F'(r_i^2)=\prod_{j\ne i}(r_i^2-r_j^2)\) has sign \((-1)^{m-i}\). Therefore each exponent is nonzero exactly when \(v\cdot w\ne0\), and the prescribed alternating stability follows. Hyperbolic periodic orbits are isolated, so all \(\Gamma_i\) are limit cycles in this regime.

**3. Analytic periodic annuli at the simultaneous neutral wall.** Suppose \(v\cdot w=0\). Then \(\varepsilon=0\), and \(\beta\ne0\). On each component where \(F(s)\ne0\), the quantity
\[
H(s,\xi)=\int^s\frac{du}{F(u)}-\frac{2\beta}{h}\log(c+h\xi)
\tag{4}
\]
is a first integral wherever \(c+h\xi>0\): equations (3) give \(\dot s=2\beta\eta F(s)\) and \(\dot\xi=(c+h\xi)\eta\), so \(\dot H=0\). For an integral smooth across a particular circle, set \(s_i=r_i^2\), \(a_i=F'(s_i)\), and define the analytic function
\[
B_i(s)=\int_{s_i}^s\left(\frac{a_i}{F(u)}-\frac1{u-s_i}\right)du.
\]
The displayed integrand extends analytically across \(s_i\), since \(F\) has a simple zero there. Then
\[
J_i(s,\xi)=(s-s_i)e^{B_i(s)}(c+h\xi)^{-2\beta a_i/h}\tag{5}
\]
is a real-analytic first integral in a full neighborhood of \(\Gamma_i\): away from \(s=s_i\), the logarithmic derivative of \(J_i\) is \(a_i\dot H=0\), and continuity extends the identity across the circle. Since \(J_i\) equals \((s-s_i)\) times a strictly positive analytic factor, its gradient is nonzero normal to \(\Gamma_i\). Its sufficiently small nonzero level sets therefore are embedded circles on either side. Angular speed stays nonzero in a small tubular neighborhood by \(c>h r_m\); each level circle is consequently a periodic trajectory. This proves the two-sided period annulus and the equivalence between neutrality and local annular integrability.

**4. Degree optimality.** For any planar polynomial field \((P,Q)\) of degree \(n\) with these \(m\) distinct centered circular limit cycles, the radial polynomial \(R=xP+yQ\) vanishes on each circle, hence is divisible by \(\prod_i(x^2+y^2-r_i^2)\). If \(R\equiv0\), regular orbits lie on the entire family of centered circles and no centered circle is an isolated periodic orbit. Therefore \(R\ne0\). Since \(R(0,0)=0\) but \(F(0)\ne0\), the quotient \(R/F\) is a nonzero polynomial of degree at least one. Thus \(\deg R\ge2m+1\), whereas \(\deg R\le n+1\); hence \(n\ge2m\). In (1), \(v\ne0\) makes the degree exactly \(2m\), proving attainment.

## Verification
Run the standalone \(\texttt{verify.py}\) with Python, NumPy, SciPy and SymPy. It verifies the exact radial identity, the neutral first-integral derivative and Jacobian identities; quadrature versus closed Floquet exponents for 27 cases at two, three and four concentric circles; and direct two-dimensional monodromy for two cases. It also checks four neutral near-circle trajectories against one-turn closure. The finite tests support but do not replace the proof for arbitrary integer \(m\) and real parameters.

## Relationship to prior work
Jana and Sarkar (arXiv:2610.33226v1, 23 October 2026) give the general normal form for polynomial fields with concentric invariant circles (Theorem 2.5) and analyze low-degree circular limit-cycle bounds. Their Proposition 2.3 already gives the analogous nonzero inner-product hyperbolicity criterion for a **single** invariant circle in a quadratic field; the one-circle criterion is not claimed new. The degree-optimal bound itself is already known from Dolov and Pavlyuk (2003), as Jana and Sarkar explicitly note. This result instead isolates the first nonconstant affine angular-speed class **at the minimal degree** and determines an exact simultaneous hyperbolic-to-period-annulus boundary, every original-time period, and every transverse multiplier. Margalef-Bentabol and Peralta-Salas (2015, full open postprint inspected) construct polynomial fields realizing general configurations with individually prescribed periods, multiplicities and stabilities, at degree bounds not asserted sharp. That stronger realization result does not yield the exact minimal-degree affine-twist family, the one-inner-product simultaneous transition or analytic annuli at its wall. Previously published results on polar Dulac rigidity and homogeneous star-node cycles have different radial and angular structures and do not imply this multi-circle orthogonality criterion. Historical priority has not been independently certified.

## Limitations
There may be additional noncircular periodic orbits elsewhere in the phase plane; none is classified here. The simultaneous neutral-wall conclusion requires an affine nonconstant angular factor \(c+w\cdot(x,y)\), strictly nonzero on the relevant circles. No assertion is made for arbitrary higher-degree angular factors, for infinite sequences of circles, or for nonpolynomial forcing. The result is an explicit structural classification within a natural minimum-degree subfamily, not a general solution of Hilbert's sixteenth problem. The 2016 circular-cycle classification of Llibre, Ramírez, Ramírez and Sadovskaia could only be compared through accessible descriptions (while the 2015 realization paper was read in full), leaving a residual priority risk; independent scientific validation has not been performed.

## References
1. S. Jana and S. Sarkar, *Some remarks on polynomial vector fields in \(\mathbb R^2\)*, arXiv:2610.33226v1, publicly submitted 23 October 2026, https://arxiv.org/html/2610.33226v1, especially Theorem 2.5 and Section 3.
2. M. V. Dolov and Yu. V. Pavlyuk, *Invariant Algebraic Curves of Polynomial Dynamical Systems*, *Differential Equations* **39** (2003), 1091–1097, https://doi.org/10.1023/B:DIEQ.0000011281.74525.3b.
3. J. Llibre, R. Ramírez, V. Ramírez and N. Sadovskaia, *The 16th Hilbert problem restricted to circular algebraic limit cycles*, *Journal of Differential Equations* **260** (2016), 5726–5760, https://doi.org/10.1016/j.jde.2015.12.019.
4. J. Margalef-Bentabol and D. Peralta-Salas, *Realization problems for limit cycles of planar polynomial vector fields*, arXiv:1507.00698v1, publicly submitted 2 July 2015, https://arxiv.org/abs/1507.00698.
