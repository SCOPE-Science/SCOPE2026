# Sharp Sobolev embedding and bridge-driven localization on double-bouquet metric graphs

## Finding
Consider two bouquets of circles, with a single connecting interval. Let the left bouquet have circle lengths \(a_1,\ldots,a_r>0\) and the right bouquet lengths \(c_1,\ldots,c_s>0\), where \(r,s\ge1\). Let the connecting interval have length \(b>0\). Define
\[
A=\sum_{i=1}^r a_i,\quad C=\sum_{j=1}^s c_j,\quad L=A+C+b,\quad Q=\sum_i a_i^2+\sum_j c_j^2,\quad T=\sum_i a_i^3+\sum_j c_j^3,
\]
\[
J=\frac{LQ}{3}-\frac T6+\frac{b^3}3+b^2(A+C)+2ABC,\quad a_* =\max_i a_i,\quad c_* =\max_j c_j,
\]
and
\[
M_{\rm L}=\frac Q6+\frac{b^2}2+bC+\frac{a_*(L-a_*)}{4},\qquad
M_{\rm R}=\frac Q6+\frac{b^2}2+bA+\frac{c_*(L-c_*)}{4}.
\]
On this graph \(G\), equip the real mean-zero Sobolev space \(H=\{u\in H^1(G):\int_Gu\,dx=0\}\) with energy norm \(\|u\|_H=(\int_G |u'|^2dx)^{1/2}\). Its exact squared embedding norm into \(C(G)\) is
\[
\boxed{\|H\hookrightarrow C(G)\|^2=\frac{\max\{M_{\rm L},M_{\rm R}\}}L-\frac{J}{2L^2}.}
\]
Every norming evaluation point is exactly the antipode of a longest circle at a hub whose corresponding \(M\)-value equals the maximum. There are no norming points in the connecting interval or elsewhere on a circle. Every nonzero equality function is a scalar multiple of a mean-zero point-evaluation Green function at one of these points; signs and unit normalization give the unit-energy extremizers.

The competition between hubs is controlled by the affine bridge-length difference
\[
\boxed{M_{\rm L}-M_{\rm R}=\frac{(a_*-c_*)(A+C-a_*-c_*)}{4}+b\left(C-A+\frac{a_*-c_*}{4}\right).}
\]
It can change sign as \(b\) varies. For example, three circles of length \(3\) on the left and one of length \(2\) on the right give \(M_{\rm L}-M_{\rm R}=3/2-27b/4\): three left antipodes are norming for \(0<b<2/9\), four antipodes are norming at \(b=2/9\), and only the right antipode is norming for \(b>2/9\). When there is exactly one circle at each hub, the antipode on the **shorter** circle is norming whenever the lengths differ.

## Assumptions and scope
A circle is an interval of the specified positive length with its endpoints identified to a single hub vertex. Different circles in one bouquet intersect only at that hub; the two hubs are distinct and joined only by the interval of length \(b\). Length means one-dimensional arclength, with no point masses. Functions in \(H^1(G)\) are continuous on the graph and edgewise absolutely continuous with square-integrable derivatives, with the natural continuity matching at vertices. The measure for the zero-mean constraint is **unnormalized** arclength \(dx\), and the energy is also unnormalized. Every parameter is a positive real number, and all formulas include ties of circle lengths.

## Proof
First, mean-zero \(H\) is a Hilbert space: the connectedness of the graph makes derivative energy a norm on the mean-zero subspace, while elementary edgewise Poincaré estimates ensure point evaluations are continuous. Denote its evaluation representer at \(x\) by \(k_x\); thus \(u(x)=\langle u,k_x\rangle_H\). The effective electrical resistance, defined by
\[
R(x,y)=\sup_{\|u\|_H\le1}|u(x)-u(y)|^2,
\]
is \(\|k_x-k_y\|_H^2\). Put \(K(x,y)=\langle k_x,k_y\rangle_H\). Because every member of \(H\) has arclength mean zero, \(\int_Gk_y\,dy=0\) in \(H\). Expanding the resistance and averaging gives the **exact centered-resistance identity**
\[
K(x,x)=\frac1L\int_G R(x,y)\,dy-\frac1{2L^2}\int_G\!\int_G R(y,z)\,dy\,dz.
\]
It follows by Cauchy--Schwarz that the squared embedding norm is \(\max_x K(x,x)\), and equality at \(x\) holds only for scalar multiples of \(k_x\).

For a circle of length \(\ell\), the resistance between points of arclength separation \(t\in[0,\ell]\) is
\[
q_\ell(t)=\frac{t(\ell-t)}\ell.
\]
Indeed its two arcs, of resistances \(t\) and \(\ell-t\), are in parallel. A component attached at a single point carries no current in a two-terminal resistance measurement within the original component. Resistances across a cut vertex add in series. Thus, for example, two points in distinct left circles have resistance \(q_{a_i}(t_i)+q_{a_j}(t_j)\), while points in opposite bouquets have resistance \(q_{a_i}(t_i)+b+q_{c_j}(t_j)\). These statements also apply when a point is in the bridge.

The elementary integrals
\[
\int_0^\ell q_\ell(t)\,dt=\frac{\ell^2}{6},\qquad
\int_0^b\!\int_0^b |t-v|\,dt\,dv=\frac{b^3}{3}
\]
now evaluate the double resistance integral. Pairs within all left circles contribute \(AQ_{\rm L}/3-T_{\rm L}/6\), and similarly on the right. Pairs across the bridge and the two hubs give
\[
\int_{G^2}R(y,z)\,dy\,dz
=\frac{LQ}{3}-\frac T6+\frac{b^3}{3}+b^2(A+C)+2ABC=J.
\]
This counts ordered pairs, so no extra factor two is needed in the centered-resistance identity.

On a left circle of length \(a_i\), let \(t\in[0,a_i]\) measure position from its hub. The single resistance integral is exactly
\[
I_{\rm L,i}(t):=\int_G R(x_t,y)\,dy
=\frac Q6+\frac{b^2}2+bC+(L-a_i)q_{a_i}(t).
\]
It has its unique maximum at the antipodal point \(t=a_i/2\), because \(L-a_i>0\). Its maximum is the displayed expression with \(a_i(L-a_i)/4\). If \(a_i>a_j\), then
\[
a_i(L-a_i)-a_j(L-a_j)=(a_i-a_j)(L-a_i-a_j)>0,
\]
since the connecting bridge has strictly positive length. Hence **only** longest left circles can maximize within that bouquet. On a right circle the same argument gives the expression \(M_{\rm R}\) with \(c_j\).

At bridge coordinate \(t\in[0,b]\), measured from the left hub,
\[
I_{\rm bridge}(t)=\frac Q6+At+C(b-t)+\frac{t^2+(b-t)^2}{2}.
\]
It is a strictly convex quadratic. Its maximum is at one of the two hubs, but the antipode of any positive circle at that hub gives strictly larger \(I\). Thus every global maximum lies at one of the specified longest-circle antipodes, and its value is \(\max\{M_{\rm L},M_{\rm R}\}\). Substituting the computed \(J\) into the centered-resistance identity proves the sharp norm and its complete equality classification. Finally, subtraction of the two expressions for \(M\) and the factorization \(a_*(L-a_*)-c_*(L-c_*)=(a_*-c_*)(L-a_*-c_*)\) prove the affine hub-comparison formula and the explicit crossing example.

For an explicit normalization of the equality functions, let \(\mu=dx/L\), \(r(x)=\int_G R(x,z)d\mu(z)\), and \(\bar r=\int_G r(y)d\mu(y)\). Then
\[
k_x(y)=-\tfrac12\left[R(x,y)-r(x)-r(y)+\bar r\right]
\]
is the mean-zero Green function; it is the unique representer of evaluation in \(H\). Every unit-energy norming function is \(\pm k_x/\sqrt{K(x,x)}\) for a maximizing point \(x\).

## Verification
The accompanying self-contained Python checker independently solves the exact piecewise-quadratic Kirchhoff Green equation \(-u''=\delta_x-L^{-1}dx\) on a network in which every circle is represented by two parallel semicircle edges. It forms and inverts the exact rational weighted vertex Laplacian, includes the exact quadratic interior particular solution, and reconstructs the arclength mean. For 135 rational double-bouquet instances with one to three circles per side, it verifies every antipodal evaluation value (not just the maximum) against the closed formula. It also checks both sides and the exact tie at the bridge-length transition \(b=2/9\). Execute `python verify_double_bouquet.py` with SymPy installed. Finite checks corroborate but do not replace the proof.

## Relationship to prior work
Solomyak (2002) develops Sobolev approximation and embedding-operator estimates on general compact metric graphs; this supplies the longstanding function-space context but does not derive the present exact mean-zero point-evaluation constant or two-hub equality localization. Ilyin and Zelik (2013) develop sharp pointwise Sobolev inequalities through Green functions on manifolds and periodic domains; their abstract-level comparison does not establish the network-specific formula. Usman (2018) proves isoperimetric Sobolev inequalities on compact metric graphs, not this resistance-exact optimization. Faught, Kempton and Knudson (2020) calculate resistance and Kirchhoff indices for *cyclically assembled discrete flower graphs*; their inspected full text does not give a continuous-arclength mean-zero Sobolev norm or the bridge-induced switch derived here. The electrical resistance and Green-kernel identities are standard inputs, not claimed as inventions. The contribution is the explicit sharp constant and full localization/phase classification for all positive lengths in the specified two-hub bouquet family.

## Limitations
The theorem assumes two hubs, a single connecting bridge, loop bouquets and uniform arclength; general cactus networks, edgewise density changes, vertex atoms, additional connecting routes, nonlinear Sobolev exponents and independent certification are not covered. The result does not claim a new resistance identity for arbitrary graphs. Equivalent earlier specialized network formulas in unindexed references remain a possible originality risk.

## References
1. M. Solomyak, *On approximation of functions from Sobolev spaces on metric graphs*, arXiv:math/0206235, first publicly posted 23 June 2002 (primary MSC in the preprint 46E39).
2. A. A. Ilyin and S. V. Zelik, *Green's function asymptotics and sharp point-wise interpolation inequalities*, arXiv:1303.0957, first posted 5 March 2013.
3. M. Usman, *Sobolev type inequalities for compact metric graphs*, Journal of Inequalities and Applications 2018:271, DOI 10.1186/s13660-018-1872-y, published 5 October 2018.
4. N. Faught, M. Kempton and A. Knudson, *Resistance distance, Kirchhoff index, and Kemeny's constant in flower graphs*, arXiv:2007.03103, first posted 6 July 2020.
