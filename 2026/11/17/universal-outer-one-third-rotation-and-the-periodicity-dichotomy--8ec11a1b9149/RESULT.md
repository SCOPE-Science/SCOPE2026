# Universal outer one-third rotation and the periodicity dichotomy for a positive Somos-type QRT map

## Finding

Let \(a,b,c,d\) be arbitrary strictly positive real numbers. On the positive quadrant consider
\[
T(x,y)=\left(y,\frac{ay+b}{xy(cy+d)}\right).
\]
Define the conserved energy
\[
H(x,y)=d(x+y)+a\left(\frac1x+\frac1y\right)+cxy+\frac{b}{xy}.
\]
There is a unique positive equilibrium \((s,s)\), where \(s\) is the unique positive root of
\[
cs^4+ds^3-as-b=0.
\]
Put \(h_*=H(s,s)\). Every energy level \(H=h>h_*\) is a smooth simple closed curve, strictly convex in logarithmic coordinates, and the restriction of \(T\) is conjugate to a rigid circle rotation. Write its clockwise rotation number as \(\rho(h)\in(0,1/2)\). It is continuous for \(h>h_*\) and has the two exact endpoint limits
\[
\boxed{\lim_{h\downarrow h_*}\rho(h)=\frac{1}{2\pi}\arccos\left(\frac{\delta-1}{2}\right),\quad
\lim_{h\to\infty}\rho(h)=\frac13,\quad
\delta=\frac{s(ad-bc)}{(as+b)(cs+d)}.}
\]
Consequently, \(ad=bc\) if and only if \(T^3\) is the identity on the positive quadrant. In that case the equilibrium has least period one and every other point has least period three. If \(ad\ne bc\), then \(T\) has invariant ovals of every sufficiently large prime least period, and invariant ovals with irrational rotation; it is not globally periodic. The claim of all sufficiently large prime periods does **not** assert that every sufficiently large composite number is realized.

## Assumptions and scope

The four coefficients and the two initial coordinates are strictly positive. The theorem describes the two-dimensional ratio recurrence \(v_nv_{n+1}v_{n+2}=(av_{n+1}+b)/(cv_{n+1}+d)\), which arises in the positive-data sector of a bilinear two-sequence Somos-type system. It does not assert periodicity of either original sequence, whose amplitudes may grow. Clockwise orientation and rotation numbers refer to \((\log x,\log y)\) coordinates. No boundary coefficient, nonpositive ratio, singular complex orbit, or vanishing denominator is included.

## Proof

**1. First integral, positive diffeomorphism, and strict convexity.** Direct rational substitution gives \(H(T(x,y))=H(x,y)\). In logarithmic coordinates \(u=\log x\), \(v=\log y\), the map is
\[
F(u,v)=(v,-u-v+g(v)),\qquad
 g(v)=\log(ae^v+b)-\log(ce^v+d).
\]
Its Jacobian determinant is exactly one; its inverse is \(F^{-1}(U,V)=(-U-V+g(U),U)\). The energy becomes
\[
\mathcal H(u,v)=d(e^u+e^v)+a(e^{-u}+e^{-v})+c e^{u+v}+b e^{-u-v}.
\]
It is proper and strictly convex: the two coordinate terms supply a positive-definite diagonal Hessian, while the last two terms contribute positive-semidefinite rank-one Hessians. Its unique minimizer must lie on \(u=v\) by symmetry, and its stationary equation is precisely the displayed quartic. The coefficient sign sequence \((+,+,-,-)\), or strict convexity, gives the uniqueness of its positive root. Thus every regular superminimum level is a smooth strictly convex Jordan oval and is invariant under \(F\).

**2. Exact rotations, canonical orientation, and continuity.** Let \(J=\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\). The Hamiltonian vector field \(X=J\nabla\mathcal H\) travels clockwise around each oval and has nowhere-vanishing speed. Since \(F\) is symplectic and preserves \(\mathcal H\), \(F_*X=X\). Therefore \(F\) commutes with the Hamiltonian flow on each oval and acts as a fixed time-shift; parameterizing by Hamiltonian travel time divided by the full period gives a conjugacy to a rigid rotation.

For a global choice of clockwise rotation lift, translate the unique minimum to the origin. If \((p,q)=(u-\log s,v-\log s)\), the image displacement is \((q,-p+kq)\), with \(k=-1+[g(v)-g(\log s)]/(v-\log s)\) (and the derivative value at equality). Since
\[
g'(v)=\frac{ae^v}{ae^v+b}-\frac{ce^v}{ce^v+d}\in(-1,1),
\]
we have \(-2<k<0\). Their signed cross product is
\[
\det\begin{pmatrix}p&q\\q&-p+kq\end{pmatrix}
=-(p^2-kpq+q^2)<0.
\]
The quadratic form is strictly positive because \(|k|<2\). Hence each forward angular step is strictly clockwise by less than \(\pi\), consistently yielding \(0<\rho(h)<1/2\). Radial parameterizations of the nested convex ovals vary continuously; continuity of rotation numbers of orientation-preserving circle homeomorphisms gives continuity of \(\rho\).

**3. Inner rotation endpoint.** The unique equilibrium has log-coordinate differential
\[
B=\begin{pmatrix}0&1\\-1&\delta-1\end{pmatrix},
\qquad \delta=\frac{s(ad-bc)}{(as+b)(cs+d)}.
\]
The above difference of fractions gives \(-1<\delta<1\), so \(-2<\operatorname{tr}B<0\), and the eigenvalues are \(e^{\pm i\alpha}\), where \(\alpha=\arccos((\delta-1)/2)\in(\pi/2,\pi)\). The positive-definite Hessian is preserved by \(B\), so the map induced by \(B\) on the limiting quadratic ellipse rotates clockwise by angle \(\alpha\). Rescaling regular levels by \((h-h_*)^{-1/2}\) makes their boundaries and maps converge uniformly to this quadratic model. Rotation-number continuity gives the first endpoint formula.

**4. Outer rotation endpoint.** Put \(R=\log h\), and on logarithmic coordinates rescale by \(1/R\). The log-sum-exp identity proves, uniformly on compact sets,
\[
\frac1R\log\mathcal H(RU,RV)\longrightarrow
\Phi(U,V)=\max\{U,V,-U,-V,U+V,-U-V\}.
\]
The compact convex level \(\Phi=1\) is the hexagon with vertices
\[
(1,0),(1,-1),(0,-1),(-1,0),(-1,1),(0,1).
\]
Because \(g\) is bounded on the entire real line (all four coefficients are positive),
\[
R^{-1}F(RU,RV)=\big(V,-U-V+g(RV)/R\big)
\longrightarrow A(U,V)=(V,-U-V)
\]
uniformly. The normalized ovals converge in the radial topology to the hexagon, so the induced circle homeomorphisms converge uniformly to \(A\) on that hexagon. The map \(A\) has order three and moves \((1,0)\) clockwise through two of the six sides to \((0,-1)\). Its clockwise rotation number is \(1/3\); by continuity of circle rotation number, the second endpoint formula follows.

**5. Sharp global periodicity dichotomy.** As \(g\) is constant exactly when \(ad=bc\), in that case the recurrence becomes \(v_nv_{n+1}v_{n+2}=a/c=b/d\), so \(T^3=\mathrm{id}\). Conversely, \(\delta=0\) exactly when \(ad=bc\). When \(ad\ne bc\), the two endpoint rotation numbers differ: \(\arccos((\delta-1)/2)/(2\pi)\ne1/3\). By continuity, the range of \(\rho\) contains a nonempty open interval. Every sufficiently large prime \(q\) admits an integer \(1\le p<q\) with \(p/q\) in that interval. The corresponding oval is conjugate to the rational rotation \(p/q\), so every point on it has least period \(q\). Choosing irrational numbers in the interval similarly produces invariant ovals with dense, uniquely ergodic orbits.

## Verification

The accompanying `verify.py` independently simplifies \(H(T(x,y))-H(x,y)\) to zero, checks the logarithmic Jacobian determinant and the exact order-three outer linear map, and compares numerical winding estimates at small and large energy for three positive coefficient choices. Its successful output begins with `CASE` lines and ends with `VERIFY_OK`. The finite checks are corroborative only; the uniform-rotation limits and existence of infinitely many periods follow from the analytical arguments above. Run `python verify.py` with Python 3.11+ and SymPy installed.

## Relationship to prior work

Svinin (2026), equations (0.2), (1.4), and (1.5), establishes the bilinear recurrence, Möbius ratio reduction, and invariant, and proves Laurent properties; these are used rather than claimed new. Hamad, Hone, van der Kamp, and Quispel (2018) treat general multiplicative QRT maps, Laurentifications, and degree growth, and their general formula contains this ratio map as a coefficient specialization. Standard QRT integrability already predicts elliptic level dynamics. The contribution here is the global **strictly positive** phase portrait for this four-positive-coefficient specialization, the two exact energy-boundary rotation limits, and the all-parameter determinant dichotomy implying all sufficiently large prime periods. Bastien and Rogalski (2014) treat a homographic positive QRT system corresponding to the lower-degree boundary with the coefficient of \(xy\) in the first integral equal to zero; their published abstract describes conjugacy and periods, not the present strictly four-positive-coefficient outer hexagon limit. Historical priority for the boundary law remains subject to verification of additional specialized QRT literature.

## Limitations

No monotonicity of \(h\mapsto\rho(h)\) is proved or claimed. The theorem is about the positive **ratio map**, not absolute growth or asymptotics of the original bilinear-sequence coordinates. It requires \(a,b,c,d>0\); when one coefficient vanishes, the outer Newton polygon and rotation limit may change. Rotations are classified individually on each invariant oval; this does not provide a closed expression for \(\rho(h)\) at finite energy. The circle homeomorphism, convexity, and boundary-limit arguments are analytical; a finite checker alone cannot validate them.

## References

1. A. K. Svinin, *On a certain system of discrete equations with the Laurent property*, arXiv:2611.02309v1 (first posted 2026-11-01), especially equations (0.2), (1.4), (1.5), and the conclusion. https://arxiv.org/abs/2611.02309
2. K. Hamad, A. N. W. Hone, P. H. van der Kamp, and G. R. W. Quispel, *QRT maps and related Laurent systems*, Advances in Applied Mathematics 96 (2018), 216–248, arXiv:1702.07047, especially equation (5) and Section 3. https://arxiv.org/abs/1702.07047
3. G. Bastien and M. Rogalski, *A QRT-system of two order one homographic difference equations: conjugation to rotations, periods of periodic solutions, sensitiveness to initial conditions*, arXiv:1407.0918 (2014), abstract consulted. https://arxiv.org/abs/1407.0918
