# A sharp interior-lattice-point bound for integral twisted-cubic polytopes

## Finding
Let \(T\subset\mathbb Z\) consist of at least four distinct parameters, let \(a=\min T\), \(b=\max T\), and put \(L=b-a\ge3\). Define
\[
 C_3(T)=\operatorname{conv}\{(t,t^2,t^3):t\in T\}\subset\mathbb R^3.
\]
Then the number \(I(T)=|\operatorname{int}C_3(T)\cap\mathbb Z^3|\) satisfies the **sharp fixed-span inequality**
\[
 I(T)\ge 2\binom{L-1}{3}.
\]
For four-vertex configurations and \(L\ge4\), equality holds **exactly** for parameter sets \(\{a,a+1,a+2,b\}\) and \(\{a,b-2,b-1,b\}\). For \(L=3\), the unique set is four consecutive integers and equality gives zero. In particular, among all three-dimensional integral twisted-cubic polytopes, the only hollow ones are those with four consecutive integer parameters (up to integer translation of the parameter).

## Assumptions and scope
The parameters are distinct integers, \(|T|\ge4\). The lattice is exactly \(\mathbb Z^3\) in the standard monomial coordinates and interior is ordinary three-dimensional interior. The lower bound applies to arbitrarily many vertices; the complete equality classification asserted here is **only for four vertices**. The expression \(\binom{L-1}{3}\) has its standard value zero when \(L=3\).

## Proof
Write four chosen parameters as \(t_0<t_1<t_2<t_3\), let \(x=t_1-t_0\), \(y=t_2-t_1\), \(z=t_3-t_2\), and \(L=x+y+z\). Each gap is a positive integer. Integer translation \(t\mapsto t-t_0\) acts on the moment coordinates by a triangular integral unimodular affine transformation, so we may assume \(t_0=0\).

The established integral-cyclic-polytope Ehrhart identity gives
\[
 E_{C_3(T_4)}(m)=1+L m+A m^2+V m^3,
\]
where \(T_4\) denotes these four parameters, \(A\) is the area of the projected moment-curve quadrilateral and \(V\) is the volume of the tetrahedron. Direct shoelace and Vandermonde determinant evaluations yield
\[
 A=\frac{xy(x+y)+z(x+y)(x+y+z)}2,
 \qquad V=\frac{xyz(x+y)(y+z)(x+y+z)}6.
\]
Ehrhart reciprocity therefore gives the exact **interior-lattice-point identity**
\[
 I(T_4)=V-A+L-1.
\]
No sampling or interpolation is used to establish this identity.

It remains to prove the sharp inequality for positive integers \(x,y,z\). Let \(u=x-1\), \(v=y-1\), \(w=z-1\), all nonnegative integers, and define
\[
 D=6\left(I(T_4)-2\binom{L-1}{3}\right).
\]
An exact polynomial identity writes \(D=Q_0+vQ_1+v^2Q_2+v^3Q_3+v^4Q_4\), where
\[
\begin{aligned}
Q_0={}&uw(u^2w+3u^2+uw^2+9uw+11u+3w^2+11w+9),\\
Q_1={}&u^3w^2+4u^3w+3u^3+u^2w^3+12u^2w^2+33u^2w+13u^2\\
&+4uw^3+33uw^2+58uw+17u+3w^3+13w^2+17w+6,\\
Q_2={}&u^3w+u^3+3u^2w^2+15u^2w+12u^2+uw^3+15uw^2\\
&+48uw+25u+w^3+12w^2+25w+11,\\
Q_3={}&2(u^2w+u^2+uw^2+6uw+5u+w^2+5w+3),\\
Q_4={}&(u+1)(w+1).
\end{aligned}
\]
Every coefficient in every \(Q_j\) is strictly positive, except that the displayed \(Q_0\) has the explicit factor \(uw\). Thus \(D\ge0\), with equality precisely when \(v=0\) and \(uw=0\), i.e. \(y=1\) and either \(x=1\) or \(z=1\). At fixed span \(L\ge4\), these are exactly \((x,y,z)=(1,1,L-2)\) and \((L-2,1,1)\); both attain the stated bound. For \(L=3\) all gaps are one.

For arbitrary \(T\), choose any four of its points that include \(a\) and \(b\). Their tetrahedron is full-dimensional and lies in \(C_3(T)\), so its interior lattice points are also interior lattice points of \(C_3(T)\). Applying the preceding inequality gives \(I(T)\ge 2\binom{L-1}{3}\). If \(I(T)=0\), then \(L=3\); there are exactly four integers in \([a,b]\), so \(T\) must be all four consecutive integers. Conversely the four-consecutive-parameter tetrahedron has zero interior lattice points by the formula.

## Verification
Run `python verify.py` with SymPy installed. The checker reconstructs \(V,A,I,D\), checks the 48 nonzero monomial coefficients of the exact positive polynomial identity, proves the two equality branches symbolically, and independently counts strict interior integer points by exact adjugate barycentric inequalities for seven tetrahedra. It also enumerates every positive gap triple for each span from 3 to 11 and confirms the exact minimizers. These finite checks supplement, rather than replace, the all-integer symbolic proof.

## Relationship to prior work
Fu Liu's integral-cyclic-polytope Ehrhart coefficient formula is the essential prior starting point; the present result does not claim to rediscover that formula. Konoike's 2026 zonotope averaging theorem supplies a recent independent context and explicitly restates Liu's formula. The new extremal calculation optimizes the integer-point count at prescribed parameter span and characterizes all tetrahedral minimizers and all hollow three-dimensional configurations; the general Ehrhart coefficient theorem does not by itself state these inequalities or equality cases. General classifications of lattice-free polyhedra concern much larger classes and do not directly give this explicit span-sharp formula for integer-parameter twisted-cubic polytopes.

## Limitations
The theorem concerns precisely the standard integer monomial moment curve in dimension three. It does not classify sharp equality among configurations with more than four vertices, nor claim extensions to arbitrary rational parameters, other curves, or higher dimensions. Full-text access to the original older Liu paper could not be completed in this review; the relevant coefficient theorem was independently identified in the accessible Konoike paper and the finite examples were cross-checked geometrically. Unindexed literature or an unexamined special consequence of earlier general classification remains a possible priority risk.

## References
- Masato Konoike, *Ehrhart polynomials of cyclic polytopes as averages of zonotope Ehrhart polynomials*, arXiv:2609.28417, first submitted 2026-09-23, https://arxiv.org/html/2609.28417 .
- Fu Liu, *Ehrhart polynomials of cyclic polytopes*, arXiv:math/0409337, first submitted 2004-09-20, https://arxiv.org/abs/math/0409337 .
- Gennadiy Averkov, Christian Wagner, Robert Weismantel, *Maximal lattice-free polyhedra: finiteness and an explicit description in dimension three*, arXiv:1010.1077, https://arxiv.org/abs/1010.1077 .
- Matthias Beck, Jesús A. De Loera, Mike Develin, Julian Pfeifle, Richard P. Stanley, *Coefficients and Roots of Ehrhart Polynomials*, arXiv:math/0402148, https://arxiv.org/abs/math/0402148 .
