# Sharp quintic realization of uniform stability for three circular limit cycles with a concentric pair

## Finding
For **every** triple of pairwise disjoint circles in the plane whose centers include exactly one coincident pair, a real polynomial planar flow of degree **five** can realize all three circles as simultaneously hyperbolic attracting cycles; another degree-five flow makes all three repelling. No polynomial flow of degree at most four can realize either uniform sign pattern. All six nonuniform sign assignments are already attainable in degree at most four. Thus, within this geometrically natural prescribed-circle realization problem, the minimal degree for either uniform pattern is exactly five.

## Assumptions and scope
Apply an orientation-preserving Euclidean similarity to place the two concentric centers at the origin and the third center at \((1,0)\). Let the concentric radii be \(r_1>r_2>0\), and let the off-center radius be \(r_3>0\); assume the three circles are pairwise disjoint. Set
\[
f_1=x^2+y^2-r_1^2,\quad f_2=x^2+y^2-r_2^2,\quad f_3=(x-1)^2+y^2-r_3^2,\quad F=f_1f_2f_3.
\]
For real parameters \(\lambda,\alpha,\beta,\gamma,\eta\), put \(B=\lambda(x^2+y^2)+\alpha x+\beta y+\gamma\), \(H=\lambda f_1f_2-f_3B\), and
\[
V_4=(yH,\ \lambda f_1f_2-xH),\qquad
J(a,b)=(-b,a),\qquad V_{\lambda,\eta}=V_4+\eta J\nabla F.
\]
The subscript four refers to the quartic field, not an imposed degree bound on the perturbation. The perturbation \(J\nabla F\) has degree five and is tangent to every level set of \(F\), so the three circles remain invariant. Hyperbolicity and attraction/repulsion are meant in the ordinary planar Floquet/Poincaré sense; other possible periodic orbits are not classified.

## Proof
**Exact defining cofactors.** Direct differentiation (no approximation) gives
\[
\begin{aligned}
V_{\lambda,\eta}(f_1)&=2(\lambda-2\eta)yf_1f_2,\\
V_{\lambda,\eta}(f_2)&=2(\lambda-2\eta)yf_1f_2,\\
V_{\lambda,\eta}(f_3)&=2yf_3[B+2\eta(f_1+f_2)].
\end{aligned}
\]
Thus the invariant-circle cofactors are \(K_1=2(\lambda-2\eta)yf_2\), \(K_2=2(\lambda-2\eta)yf_1\), and \(K_3=2y[B+2\eta(f_1+f_2)]\). If \(x=r_i\cos\theta,y=r_i\sin\theta\) on circle \(i=1,2\), its angular velocity is \(W_i=f_3[B+2\eta f_{3-i}]\), where the notational \(f_{3-i}\) means \(f_2\) when \(i=1\) and \(f_1\) when \(i=2\). On the third circle, parameterized by \(x=1+r_3\cos\phi,y=r_3\sin\phi\), the angular velocity is \(W_3=(-\lambda+2\eta)f_1f_2\). These formulas follow by differentiating the polar angles; the third uses its own center.

**Quintic construction.** Let \(\Delta=r_1^2-r_2^2>0\). Choose
\[
\lambda=1,\quad\eta=-1,\quad\alpha=0,\quad\gamma=-\frac{r_1^2+r_2^2}{2},\quad0<|\beta|<\frac{3\Delta}{2r_1}.
\]
On the first circle \(B+2\eta f_2=-3\Delta/2+\beta y<0\), and on the second \(B+2\eta f_1=3\Delta/2+\beta y>0\). Pairwise circle disjointness ensures \(f_3\ne0\) on either. On the third circle \(W_3=-3f_1f_2\ne0\). Therefore all three circles are genuine periodic orbits, without stationary points.

**Exact characteristic-exponent signs.** For a planar invariant periodic curve \(f_i=0\) with smooth regular defining function and cofactor \(K_i\), its nontrivial Floquet multiplier equals \(\exp(\chi_i)\), where \(\chi_i=\int_0^{T_i}K_i(x(t),y(t))dt\). This follows by differentiating \(f_i\) along a transverse perturbation. On the first circle \(K_1=6\Delta y\), and on the second \(K_2=-6\Delta y\). The signs of their characteristic exponents can be decided without evaluating elliptic integrals. On either concentric circle the factor \(f_3\) is even under \(\theta\mapsto2\pi-\theta\) and has constant nonzero sign. If \(c\ne0\), \(|\beta|r<|c|\), and \(w(\theta)>0\) is even, then pairing \(\theta\) and \(2\pi-\theta\) gives
\[
\int_0^{2\pi}\!\frac{r\sin\theta\,w(\theta)}{|c+\beta r\sin\theta|}\,d\theta
=\int_0^{\pi}\!r\sin\theta\,w(\theta)\left[\frac1{|c+\beta r\sin\theta|}-\frac1{|c-\beta r\sin\theta|}\right]d\theta.
\]
The bracket has the constant strict sign \(-\operatorname{sgn}(c\beta)\). Here \(c_1=-3\Delta/2\), \(c_2=3\Delta/2\), and the extra negative sign in \(K_2\) cancels the second sign. Hence \(\operatorname{sgn}\chi_1=\operatorname{sgn}\chi_2=\operatorname{sgn}\beta\).

On the third circle all expressions in \(B-2(f_1+f_2)\) except \(\beta y\) are even under \(\phi\mapsto2\pi-\phi\). Therefore
\[
\chi_3=\frac{2\beta r_3^2}{3}\int_0^{2\pi}\frac{\sin^2\phi}{|f_1f_2|}\,d\phi,
\]
which is nonzero with sign \(\operatorname{sgn}\beta\). Thus all three exponents have the same strict sign: negative for \(\beta<0\) and positive for \(\beta>0\). They are hyperbolic cycles and hence isolated. The polynomial field is degree five: its degree-five homogeneous part comes from the nonzero term \(-J\nabla F\), while \(V_4\) has degree at most four.

**Degree-four lower bound.** The complete degree-at-most-four normal form of Cao and Llibre for precisely this configuration identifies the field \(V_4\), and its cofactor signs for hyperbolic circular cycles are
\[
\operatorname{sgn}\chi_1=-\operatorname{sgn}(\lambda\beta s_1),\quad
\operatorname{sgn}\chi_2=\operatorname{sgn}(\lambda\beta s_2),\quad
\operatorname{sgn}\chi_3=\operatorname{sgn}\beta,
\]
where \(s_i=\operatorname{sgn}(\lambda r_i^2+\gamma)\), and \(|\lambda r_i^2+\gamma|>r_i\sqrt{\alpha^2+\beta^2}\), \(\lambda\beta\ne0\). If \(s_1=s_2\), the first two exponents have opposite signs. If \(s_1=-s_2\), their ordering with \(r_1^2>r_2^2\) forces \(s_1=\operatorname{sgn}\lambda\), so both first two exponents have sign opposite to that of \(\chi_3\). Three equal stability signs are impossible at degree four or below.

**All other assignments.** In the same quartic normal form set \(\lambda=1\), \(\alpha=0\), and fix sufficiently small nonzero \(\beta\). Varying \(\gamma\) to make \((s_1,s_2)=(+,+),(-,-),(+,-)\) is possible with the strict angular-speed inequalities. Choosing either sign of \(\beta\) realizes respectively all six nonuniform triples; the fourth sign pair \((-,+)\) is impossible from the ordering of radii. Thus the two uniform triples are exactly the missing sign assignments at degree four, and the quintic construction supplies them.

## Verification
The attached `CHECK.py` symbolically verifies all three cofactor identities and the angular-speed identities with exact rational coefficients for a disjoint-circle example \((r_1,r_2,r_3)=(2/5,1/5,1/5)\), and numerically integrates the cofactor exponents for both signs of \(\beta=1/100\). The independent scalar sign proof above establishes the universal claim without depending on numerical sampling.

## Relationship to prior work
Cao and Llibre (2026) prove the complete quartic normal form for a pairwise-disjoint three-circle arrangement with two concentric members, including its characteristic multiplier formulas. This work uses those results for the **lower bound**, but the degree-five Hamiltonian perturbation and its uniform-sign construction are distinct new statements. Jana and Sarkar (2026) investigate broader invariant-circle normal forms and give sharp quartic bounds, not this prescribed quintic stability construction. Previous degree-minimal realizations for **two fully concentric circles** concern different geometry and, in some cases, stronger prescribed multipliers and periods; they do not imply the three-circle claim.

## Limitations
No claim is made about the number or character of additional cycles of the quintic vector field, prescribed nontrivial Floquet-multiplier magnitudes, or independence of the mathematical review. The quartic impossibility uses the complete normal-form theorem of the cited primary work, while the quintic existence and sign calculations are explicit here. Broad historical priority beyond inspected literature remains provisional.

## References
- C. Cao and J. Llibre, *Quartic polynomial differential systems with three disjoint invariant circles*, arXiv:2611.05696v1 (2026), especially Theorem B and Section 4.
- S. Jana and S. Sarkar, *Some remarks on polynomial vector fields in R2*, arXiv:2610.33226v1 (2026).
- C. Christopher, *Polynomial vector fields with prescribed algebraic limit cycles*, Geometriae Dedicata 88 (2001).
- J. Margalef-Bentabol and D. Peralta-Salas, *Realization problems for limit cycles of planar polynomial vector fields* (2016).
