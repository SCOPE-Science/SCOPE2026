# Six \(A_2\) points and two \(\mathrm{IV}^{*}\) fibers in characteristic-three quartics

## Finding
Let \(k\) be algebraically closed of characteristic \(3\). In \(\mathbb P^3_k\) with coordinates \([x:y:z:w]\), consider
\[
X_{Q,G}:\quad F=z x^3+w y^3+x y Q(z,w)+G(z,w)=0,
\]
where \(Q\) is a binary quadratic and \(G\) is a binary quartic. Assume conditions (i)--(iv) below. Then \(X_{Q,G}\) is an irreducible normal quartic with exactly six rational double points of type \(A_2\), three above each of the two zeros of \(Q\). Its minimal resolution \(Y\) is a K3 surface. The residual-cubic pencil through the smooth line \(\ell=\{z=w=0\}\) induces a genus-one fibration on \(Y\) with precisely two reducible fibers of Kodaira type \(\mathrm{IV}^{*}\), each supported on a triple line and six exceptional curves, together with precisely six irreducible nodal fibers of type \(\mathrm I_1\). The restriction of this fibration to the strict transform of \(\ell\) is a purely inseparable morphism of degree \(3\).

## Assumptions and scope
Write \(q(t)=Q(t,1)\), \(g(t)=G(t,1)\), and let \(q'(t),g'(t)\) be formal derivatives. The hypotheses are:

(i) \(Q\) is separable, with two distinct roots \(r_1,r_2\in k\) of \(q\), neither equal to zero or infinity; equivalently, \(Q(0,1)Q(1,0)\ne0\) and \(q'(r_i)\ne0\).

(ii) \(G\) has four distinct roots on \(\mathbb P^1\), none at zero or infinity, and no root in common with \(Q\). Thus \(G(0,1)G(1,0)\ne0\), \(g\) is squarefree and \(g(r_i)\ne0\).

(iii) For each root \(r\) of \(q\), put \(\alpha_r^3=r\), \(\beta_r^3=g(r)\). The cubic
\[
h_r(T)=T^3-q'(r)\alpha_r T^2-q'(r)\beta_r T+g'(r)
\]
is separable, i.e. has exactly three simple roots in \(k\).

(iv) No further assumptions are made: in particular, the field is algebraically closed but need not be the closure of a finite field. These are explicit nonempty Zariski-open conditions on the coefficients. An exact nonemptiness witness over \(\mathbb F_3\) is
\[
Q=z^2+zw-w^2,\qquad G=z^4+zw^3+w^4.
\]

The statement concerns this open family, not arbitrary characteristic-three quartics containing a line or all six-cuspidal quartics. The generic residual cubic is smooth; no rational section is claimed for the genus-one fibration.

## Proof
**Singular points.** In characteristic \(3\), differentiation gives
\[
F_x=yQ,\quad F_y=xQ,\quad F_z=x^3+xyQ_z+G_z,\quad F_w=y^3+xyQ_w+G_w.
\]
Along \(\ell\), the final two derivatives are \(x^3,y^3\), so \(X\) is smooth there. At a point off \(\ell\) where \(Q\ne0\), singularity would force \(x=y=0\) and \(G=G_z=G_w=0\), impossible because \(G\) is squarefree. At a point with \(Q=0\), conditions (i) allow \(w=1,z=r\); the surface equation becomes
\[
y^3+r x^3+g(r)=(y+\alpha_r x+\beta_r)^3=0.
\]
Writing \(u=y+\alpha_r x+\beta_r\), the remaining nonautomatic derivative equation is precisely \(h_r(x)=0\). Euler's homogeneous identity makes \(F_w=0\) automatic on these solutions. Each of two roots \(r\) contributes exactly three distinct points, and there are no others.

**Local analytic type.** Fix a root \(x_0\) of \(h_r\). Set \(t=z-r\) in the chart \(w=1\), and use \(u=y+\alpha_r x+\beta_r\). There is an exact polynomial identity
\[
F=u^3+t\,s(t,x,u),\quad s(0,x,0)=h_r(x).
\]
Since \(h'_r(x_0)\ne0\), \((t,s,u)\) are formal local parameters at the point. Hence the completed local equation is \(ts+u^3=0\), the rational double point \(A_2\) in characteristic \(3\). In particular, every singularity is isolated and rational. The hypersurface is normal by \(R_1+S_2\); reducibility would force a positive-dimensional singular component, so it is geometrically irreducible. The minimal resolution is crepant, with trivial canonical divisor and \(H^1(\mathcal O_Y)=0\), hence a K3 surface.

**Residual genus-one pencil.** Any plane through \(\ell\) is \(z=r w\) or \(w=0\). Removing the fixed component \(\ell\) from its hyperplane section leaves, for finite \(r\), the plane cubic
\[
P_r(x,y,v)=r x^3+y^3+q(r)xyv+g(r)v^3,
\]
where \(v=w\) is the plane coordinate. If \(r\ne0\), \(q(r)g(r)\ne0\), and \(w\ne0\), its three partial derivatives are \(q(r)yv,q(r)xv,q(r)xy\). Their simultaneous vanishing would force a coordinate vertex, none of which lies on the cubic because \(r,g(r)\ne0\). The analogous argument handles the plane \(w=0\). Thus the generic cubic is smooth of genus one. The residual pencil defines the claimed genus-one morphism on the minimal resolution.

For \(r=r_i\) a root of \(q\), \(P_r=(y+\alpha_r x+\beta_r v)^3\). Its support is one projective line \(L_r\), with multiplicity three. Its three \(A_2\) points lie on \(L_r\) away from \(\ell\). Resolving the standard local germ \(ts+u^3=0\) adds at each point two \((-2)\)-curves in a chain, met by the strict transform of \(L_r\) at one end. The complete fiber graph is the extended Dynkin graph \(\widetilde E_6\), with central multiplicity \(3\) and three arms of multiplicities \(2,1\). This is Kodaira type \(\mathrm{IV}^{*}\), twice.

At each of the four simple roots of \(g\), with \(q(r)\ne0\), \(P_r\) has exactly one ordinary node at \([x:y:v]=[0:0:1]\), with nondegenerate quadratic part \(q(r)xy\). In the planes \(z=0\) and \(w=0\), the residual cubics have a single ordinary node respectively at \([1:0:0]\) and \([0:1:0]\), with local quadratic term a nonzero multiple of \(yv\) or \(xv\). These give six \(\mathrm I_1\) fibers. The derivative argument rules out any other singular fibers.

**Inseparable trisection.** The residual cubic in the plane \(z=r w\) meets \(\ell\) where \(r x^3+y^3=0\). Hence the map on \(\ell\cong\mathbb P^1\) is \([x:y]\mapsto[-y^3:x^3]\), the Frobenius map up to automorphism, purely inseparable of degree \(3\).

**Nonemptiness.** For the displayed \(\mathbb F_3\) witness, \(q(t)=t^2+t-1\) has two distinct roots in \(\mathbb F_9\), both nonzero. The polynomial \(g(t)=t^4+t+1\) has derivative \((t+1)^3\) and \(g(-1)=1\), hence is squarefree. For a root \(r\) of \(q\), \(g(r)=r\), and in \(\mathbb F_9\) the cubic simplifies to
\[
h_r(T)=T^3+rT^2+rT+2r.
\]
Its derivative is \(r(2T+1)\), with sole zero \(T=1\), where \(h_r(1)=1+r\ne0\). Thus each \(h_r\) is separable and all conditions hold.

## Verification
Run `python3 verify_char3.py` using Python 3; its output is stored in `verification_output.txt`. The verifier performs arithmetic in \(\mathbb F_9=\mathbb F_3[r]/(r^2+r-1)\), independently tests the witness assumptions and simple-root conditions, and exhaustively examines all \(820\) projective points in \(\mathbb P^3(\mathbb F_9)\) against the defining equation and its gradient. It returns `CHAR3_DEGENERATION_EXACT_CHECKS_PASSED`. The geometric count of six singular points is over an algebraic closure; they need not be \(\mathbb F_9\)-rational. In this witness no singular point is \(\mathbb F_9\)-rational. Finite-field enumeration is supplementary to the symbolic argument for all algebraically closed fields of characteristic three.

## Relationship to prior work
Rams and Schütt introduced and analyzed exactly this quartic equation as family \(\mathcal Z\) in their paper *On quartics with lines of the second kind* (arXiv:1303.1304, first posted 2013-03-06), Sect. 7, notably equation (7.2) and Proposition 7.1. Their results assume characteristic different from \(2,3\), and the general smooth family there has six \(\mathrm I_3\) and six \(\mathrm I_1\) fibers. The present theorem determines the characteristic-three behavior of the same defining family, including its six isolated surface singularities and the two triple-line fibers. It is not a corollary of a statement about smooth members in characteristics other than three.

Rams, *On quartics with three-divisible sets of cusps* (arXiv:math/0206040, 2002), and Barth–Rams, *Equations of low-degree Projective Surfaces with three-divisible Sets of Cusps* (arXiv:math/0112046, 2001), analyze cuspidal quartics over the complex numbers, not the reduction of \(\mathcal Z\) in characteristic three. Veniani, *Lines on K3 quartic surfaces in characteristic 3* (2021), Lemma 3.17, describes the **possible local fiber pattern** of a triple residual line of type \(\mathrm{IV}^{*}\); it does not establish its occurrence twice with six \(A_2\) surface points and six nodal residual fibers in this explicit coefficient family. The general Kodaira pattern is not claimed as new.

## Limitations
The theorem does not classify all degenerations of \(\mathcal Z\), compute the full Néron–Severi lattice or Mordell–Weil/Jacobian data, or assert the existence of a section. The geometric results depend on the stated nonempty open conditions; special coefficients may have larger singularities or different fibers. Wild contributions to discriminant multiplicities are not separately calculated. Historical priority is provisional because not all specialist sources are indexed or fully accessible; neither a failed database search nor the difference of characteristics proves uniqueness of this finding.

## References
1. S. Rams and M. Schütt, *On quartics with lines of the second kind*, arXiv:1303.1304 (2013), Sect. 7, https://arxiv.org/html/1303.1304v1.
2. S. Rams, *On quartics with three-divisible sets of cusps*, arXiv:math/0206040 (2002), https://arxiv.org/abs/math/0206040.
3. W. Barth and S. Rams, *Equations of low-degree Projective Surfaces with three-divisible Sets of Cusps*, arXiv:math/0112046 (2001), https://arxiv.org/abs/math/0112046.
4. D. C. Veniani, *Lines on K3 quartic surfaces in characteristic 3*, Manuscripta Math. 167 (2022), first online 2021-02-07, DOI:10.1007/s00229-021-01284-9, Sect. 3.
