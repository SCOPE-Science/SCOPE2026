# Exact nodal walls and a bielliptic canonical model for a symmetric torus-sextic family

## Finding

Put \(G=XY-Z^2\) and \(H_\lambda=X^3+Y^3+\lambda Z^3\). For every \(\lambda\in\mathbb C^\times\) with \(\lambda^2\ne4\), and every \(s\in\mathbb C^\times\), the plane sextic
\[
C_{\lambda,s}:\quad G^3+sH_\lambda^2=0\quad\subset\mathbb P^2_{\mathbb C}
\]
is geometrically integral. Its six permanent singularities are ordinary cusps \(A_2\), situated at the six transverse intersections \(G=H_\lambda=0\). It has no other singularities except the following **complete list of ordinary nodes**:

1. At \(s=1/\lambda^2\), one node at \([0:0:1]\).
2. At \(s=-1/4\), three nodes at \([1:\zeta:0]\), where \(\zeta^3=1\).
3. At \(s=1/\lambda^2-1/4\), three nodes at \([-\lambda\zeta/2:-\lambda\zeta^{-1}/2:1]\), where \(\zeta^3=1\).

The three parameter values are pairwise distinct except when \(\lambda^2=-4\): the first two then coincide, yielding four nodes at \(s=-1/4\). If \(k\) is the number of nodes in this list (counting coincident parameter walls but disjoint geometric points), the normalization has
\[
g(\widetilde C_{\lambda,s})=4-k,\qquad \tau(C_{\lambda,s})=12+k.
\]
Thus generic members have normalization genus four, each isolated three-node wall gives genus one, the one-node wall gives genus three, and the crossing \(\lambda^2=-4,\ s=-1/4\) is an explicit geometrically integral *rational* sextic with basket \(6A_2+4A_1\).

In addition, for \(s\notin\{1/\lambda^2,-1/4,1/\lambda^2-1/4\}\), choose a square root of \(s\) and write \(c=1/\sqrt{s}\). The normalization is isomorphic to the smooth canonical complete intersection in \(\mathbb P^3_{[W:T:Z:R]}\)
\[
R^2=W^2+4T^2-4Z^2,\qquad
W^3+3W(T^2-Z^2)+\lambda Z^3-cT^3=0.
\]
The involution \(R\mapsto-R\) has a smooth plane cubic quotient and six simple branch points. Therefore this explicit genus-four family is bielliptic. The exact node-wall classification simultaneously determines all drops in normalization genus and in Jacobian-scheme Tjurina length.

## Assumptions and scope

All schemes and singularities are over \(\mathbb C\), hence characteristic zero. Parameters \(\lambda,s\) are nonzero complex numbers and \(\lambda^2\ne4\). The excluded \(\lambda^2=4\) regime has nontransverse base points and is **not** classified here; the excluded \(s=0\) member is a nonreduced triple conic. All three nodal walls are nonzero under the stated restrictions. Ordinary \(A_2\) denotes an analytic cusp \(u^3+v^2=0\); ordinary \(A_1\) denotes a nondegenerate planar quadratic node. The Tjurina number is the sum of local Tjurina lengths. The elliptic quotient claim applies only away from all nodal walls, when the genus-four canonical model is smooth. No statement is made about arithmetic or geometric Picard ranks, Mordell–Weil groups, or characteristic-positive fibers.

## Proof

### 1. Six transverse base cusps

The conic \(G=0\) is smooth and is parametrized by \([X:Y:Z]=[u^2:v^2:uv]\). Restricting \(H_\lambda\) to it yields
\[
u^6+\lambda u^3v^3+v^6=0.
\]
Since \(\lambda^2\ne4\), the quadratic \(a^2+\lambda a+1\) has two distinct nonzero roots. Each gives three cube roots \(u/v\); consequently the base intersection comprises six distinct transverse points. Local analytic coordinates \((G,H_\lambda)\) make the sextic equation \(G^3+sH_\lambda^2=0\), so each is exactly an \(A_2\) cusp with \(\delta=1\), Milnor number two and Tjurina number two.

### 2. Exhaustion of the affine outer singular locus

Work in \(Z=1\), set \(u=xy-1\) and \(v=x^3+y^3+\lambda\), and let \(f=u^3+sv^2\). Outside the six base points, a point of \(f=0\) satisfies \(uv\ne0\). Its two gradient equations imply
\[
x f_x-y f_y=6sv(x^3-y^3)=0,
\]
so \(x^3=y^3\). If either coordinate vanishes, both vanish, giving the central candidate \((0,0)\). There \(f=-1+s\lambda^2\), hence this is a point of the curve exactly for \(s=1/\lambda^2\). The quadratic term of \(f\) is \(3xy\), so it is an \(A_1\) node.

Otherwise, \(x,y\ne0\) and the order-three diagonal symmetry \((x,y)\mapsto(\zeta x,\zeta^{-1}y)\) carries the point to \(x=y=w\). Differentiation along that diagonal gives \(u^2+2svw=0\). Combining this with \(u^3+sv^2=0\), and using \(u,v,w\ne0\), gives \(v=2wu\). Comparing with \(u=w^2-1\) and \(v=2w^3+\lambda\) yields \(w=-\lambda/2\). Substitution then forces
\[
s=\frac1{\lambda^2}-\frac14.
\]
The orbit consists of three distinct points as asserted. The affine Hessian determinant at \(x=y=-\lambda/2\) on this wall is
\[
\det\operatorname{Hess}_{x,y}(f)=-\frac{27}{64}(\lambda^2-4)^3\ne0,
\]
proving that all three are ordinary nodes. The gradient argument exhausts all affine singularities outside the cusps.

### 3. Exhaustion at infinity

On \(Z=0\), in the chart \(X=1\), the binary sextic becomes
\[
F(1,y,0)=y^3+s(1+y^3)^2.
\]
Its repeated roots, for \(s\ne0\), occur precisely when \(s=-1/4\), in which case
\[
F(1,y,0)=-\tfrac14(y^3-1)^2.
\]
The derivative in the transverse \(Z\)-direction vanishes at \(Z=0\); hence these give exactly three projective singularities. At \([1:1:0]\), the Hessian in \((y,Z)\) is \(\operatorname{diag}(-9/2,-6)\), with determinant \(27\), so all three are \(A_1\) nodes by the diagonal symmetry. The point \([0:1:0]\) is not on the curve because \(s\ne0\). Thus the list in the Finding is complete.

### 4. Integrality and genus

The finite singular support shows the sextic is reduced: a repeated irreducible factor would create a positive-dimensional singular locus. If it were reducible, take a proper union of some components of degree \(d\), with complementary degree \(6-d\). Bézout gives at least \(d(6-d)\ge5\) intersections counted with multiplicity. But the six cusps are analytically unibranch and cannot be intersection points of different components; the only other singularities are at most four ordinary nodes, each contributing at most one intercomponent intersection. This contradicts Bézout. Thus the sextic is irreducible.

The arithmetic genus of an integral plane sextic is \(10\). Six cusps contribute \(\sum\delta=6\) and each additional node contributes one, proving \(g=10-6-k=4-k\). Since ordinary \(A_1\) and \(A_2\) singularities are weighted homogeneous, their local Tjurina numbers are respectively one and two, proving \(\tau=12+k\). The wall equations are distinct unless \(1/\lambda^2=-1/4\), i.e. \(\lambda^2=-4\). At this crossing the four nodes are geometrically distinct and \(g=0\), completing the rationality assertion.

### 5. Explicit canonical bielliptic model

Choose \(\sqrt{s}\) and, on the dense smooth open set where \(GH_\lambda\ne0\), define a degree-one projective rational coordinate
\[
T=-\sqrt{s}\,H_\lambda/G.
\]
The sextic equation gives \(G=-T^2\) and \(H_\lambda=cT^3\), where \(c=1/\sqrt{s}\). With \(W=X+Y\), \(R=X-Y\), direct expansion gives
\[
R^2=W^2+4T^2-4Z^2,
\quad H_\lambda=W^3+3W(T^2-Z^2)+\lambda Z^3.
\]
This yields the stated quadric-cubic intersection \(D\). Conversely its projection \([W:T:Z:R]\mapsto[(W+R)/2:(W-R)/2:Z]\) maps into the sextic and is generically one-to-one by the displayed formula for \(T\). Its center is disjoint from the quadric, so this is a morphism on \(D\). Since \(D\) is a pure complete intersection of degree six and the image is the integral degree-six curve, \(D\) is integral and birational to the sextic.

The complete intersection \(D\) has arithmetic genus four, and its normalization has genus four whenever no nodal wall is met (by Step 4). Therefore its total normalization genus defect vanishes and \(D\) is smooth on that open parameter set. Adjunction gives \(K_D\simeq\mathcal O_D(1)\), hence these are canonical genus-four curves on the smooth rank-four quadric.

Projection \([W:T:Z:R]\mapsto[W:T:Z]\) is a degree-two map from \(D\) to the plane cubic
\[
E:\quad W^3+3W(T^2-Z^2)+\lambda Z^3-cT^3=0,
\]
with deck involution \(R\mapsto-R\). Its gradient equations are
\[
W^2+T^2-Z^2=0,\qquad T(2W-cT)=0,\qquad Z(-2W+\lambda Z)=0.
\]
Eliminating by the cases \(T=0\), \(Z=0\), and \(TZ\ne0\), a singular cubic can occur only if \(\lambda^2=4\), \(s=-1/4\), or \(s=1/\lambda^2-1/4\). These are excluded here. Thus \(E\) is smooth of genus one. The quadratic relation branches exactly on \(E\cap\{W^2+4T^2-4Z^2=0\}\), a degree-six divisor. Since \(D\) is smooth, it is reduced, and Riemann–Hurwitz gives six simple branch points. Therefore \(D\) is bielliptic, as claimed.

## Verification

The standalone `check.py` script uses symbolic exact arithmetic with SymPy. It tests the six-cusp discriminant, the affine gradient-elimination identity, the full discriminant of the diagonal sextic, the three outer-node Hessians, the complete-intersection substitution identities, the cubic-gradient formulas, and parameter-wall samples including the four-node rational crossing. Run `python check.py` with SymPy installed. The script is an algebraic consistency certificate, not a replacement for the geometric Bézout, genus, and irreducibility arguments above. The complete derivation of nonexistence of further singularities is in Steps 2–3.

## Relationship to prior work

Dimca and Sticlaru (arXiv:2601.08583v1, first public 2026-01-13, primary MSC 14H50) study the Jacobian algebra, graded Betti numbers and Tjurina invariants of reduced plane curves. The present result determines the exact Tjurina jumps and geometric normalization of a concrete symmetric torus-type sextic family, rather than deriving a general Betti-number formula.

Oka and Pho (arXiv:math/0201035v1) classify global singularity configurations for irreducible torus-type sextics. Their Table 1 explicitly lists the baskets \(6A_2+A_1\), \(6A_2+3A_1\), and \(6A_2+4A_1\); these baskets and their arithmetic genera are **not claimed as new**. Their classification does not, in the sections inspected, determine the three exact nodal parameter divisors of this two-parameter normal form, their exceptional crossing, or the displayed smooth bielliptic canonical model.

Cogolludo-Agustín and Elduque (arXiv:2507.15814v1) examine fundamental groups of complements of generic fibers of component-free pencils; their topological generic-fiber theorem does not supply the special-fiber singularity or normalization census of this pencil.

## Limitations

The classification excludes \(\lambda=0\), \(\lambda^2=4\), and \(s=0\); no assertion about these limits is required. The exact source-level novelty judgment is qualified by the risk of an equivalent but differently parameterized classical torus-sextic normal form, and by incomplete indexing of older literature. A mathematical proof and reproducible algebraic checks do not constitute independent peer review. The bielliptic canonical description is asserted only on the no-node parameter locus. The rationality conclusion at the four-node crossing is geometric over \(\mathbb C\), with no assertion about rational points over smaller fields.

## References

- A. Dimca and G. Sticlaru, *Graded Betti numbers of the Jacobian algebra and total Tjurina numbers of plane curves*, arXiv:2601.08583v1 (2026-01-13), https://arxiv.org/abs/2601.08583.
- M. Oka and D. T. Pho, *Classification of sextics of torus type*, arXiv:math/0201035v1 (2002-01-07), https://arxiv.org/abs/math/0201035, especially Sections 2 and 6 and Table 1.
- J. I. Cogolludo-Agustín and E. Elduque, *The fundamental group of the complement of a generic fiber-type curve*, arXiv:2507.15814v1 (2025-07-21), https://arxiv.org/abs/2507.15814.
