# Divisor law and zero density for quasismooth anticanonical hypersurfaces on the first terminal layer
## Finding
For every integer \(r\ge2\), consider the first terminal layer next to the canonical/non-terminal wall
\[
X_{r,a}=\mathbb P(1^r,a,a+r-1),\qquad 1\le a\le2r-2.
\]
Every \(X_{r,a}\) has terminal singularities. Put
\[
D=r+a+(a+r-1)=2a+2r-1.
\]
A general weighted hypersurface \(Y_{r,a}\subset X_{r,a}\) of degree \(D\), equivalently a general anticanonical hypersurface, is quasismooth if and only if
\[
a\mid r\quad	ext{or}\quad a\mid(2r-2)\quad	ext{or}\quad a\mid(2r-1).
\]
Because \(a\le2r-2\), the third condition means that \(a\) is a proper divisor of \(2r-1\).

Writing \(	au(n)\) for the number of positive divisors of \(n\), the number of quasismooth anticanonical members on this layer is therefore
\[
N(r)=	au(r)+	au(2r-2)+	au(2r-1)-	au(\gcd(r,2))-2.
\]
The cumulative count has the asymptotic
\[
\sum_{r=2}^R N(r)
=3R\log R+\left(6\gamma+2\log2-rac{13}2ight)R+O(\sqrt R),
\]
where \(\gamma\) is Euler's constant. Since there are exactly
\[
\sum_{r=2}^R(2r-2)=R(R-1)
\]
ambient spaces in these layers, the cumulative proportion admitting a quasismooth anticanonical hypersurface is
\[
rac{3\log R}R+O\!\left(rac1Right),
\]
so this anticanonical quasismoothness condition has density zero along the first terminal layer.

## Assumptions and scope
The ground field is algebraically closed of characteristic zero. The notation \(1^r\) means that the weight \(1\) occurs \(r\) times. Quasismoothness means that the affine cone of the hypersurface is smooth away from its vertex. The anticanonical degree on \(\mathbb P(1^r,a,b)\) is the sum of the weights, here \(D=2a+2r-1\).

The statement is restricted to the codimension-one terminal layer \(b-a=r-1\) inside the two-heavy-weight family. It does not count quasismooth anticanonical hypersurfaces on all terminal \(\mathbb P(1^r,a,b)\).

## Proof
Write \(b=a+r-1\). First verify terminality directly in the two heavy affine charts. In the \(b\)-chart the cyclic action has weights \(1^r,a\). For \(1\le k<b\), its Reid--Tai age has numerator
\[
rk+(akmod b).
\]
Since \(a=b-(r-1)\), if \(b
mid(r-1)k\) this numerator is
\[
b+rk-((r-1)kmod b)>b,
\]
because \(((r-1)kmod b)\le(r-1)k\). If \(b\mid(r-1)k\), then \(rk=(r-1)k+k>b\). Hence every nonidentity element has age greater than \(1\).

In the \(a\)-chart the action has weights \(1^r,b\), so the age numerator is
\[
rk+((r-1)kmod a).
\]
If \((r-1)k<a\), the age equals \((2r-1)k/a>1\) because \(a\le2r-2\). If \((r-1)k\ge a\), then \(rk/a>(r-1)k/a\ge1\). Thus this chart is terminal as well, and the unit-weight charts are smooth.

Now specialize the standard monomial criterion for quasismooth weighted hypersurfaces. Any coordinate subset containing a unit-weight variable supports a pure monomial of degree \(D\), so only the subsets consisting of the two heavy variables \(y,z\), of weights \(a,b\), need to be checked.

For the singleton \(\{z\}\), one has \(D-1=2b\), so the monomial \(x_i z^2\) has degree \(D\); the condition is automatic. For \(\{y,z\}\), the same identity \(D-1=2b\) gives two monomials \(x_1z^2\) and \(x_2z^2\) with distinct outside unit variables, so this condition is automatic because \(r\ge2\).

For the singleton \(\{y\}\), the monomial criterion leaves exactly three possibilities: a pure power of \(y\), a monomial \(x_i y^m\), or a monomial \(z y^m\). Their degree conditions are respectively
\[
a\mid D,\qquad a\mid(D-1),\qquad a\mid(D-b).
\]
Using
\[
D=2a+2r-1,\qquad D-1=2a+2r-2,\qquad D-b=a+r,
\]
these become
\[
a\mid(2r-1),\qquad a\mid(2r-2),\qquad a\mid r.
\]
This proves the quasismoothness classification.

For the exact count, let \(A,B,C\) be the allowed divisor sets coming from \(r\), \(2r-2\), and the proper divisors of \(2r-1\). Their pairwise greatest common divisors are
\[
\gcd(r,2r-2)=\gcd(r,2),\qquad \gcd(r,2r-1)=1,\qquad \gcd(2r-2,2r-1)=1.
\]
Inclusion--exclusion therefore gives
\[
|A\cup B\cup C|=	au(r)+	au(2r-2)+	au(2r-1)-	au(\gcd(r,2))-2.
\]

For the summatory asymptotic, let
\[
T(x)=\sum_{n\le x}	au(n)=x\log x+(2\gamma-1)x+O(\sqrt x),
\]
the elementary Dirichlet-divisor estimate. The identity
\[
	au(2n)=2	au(n)-\mathbf 1_{2\mid n}	au(n/2)
\]
gives
\[
\sum_{n\le x}	au(2n)=2T(x)-T(\lfloor x/2floor).
\]
Likewise the sum over odd integers is
\[
\sum_{\substack{n\le x\n	ext{ odd}}}	au(n)
=T(x)-2T(\lfloor x/2floor)+T(\lfloor x/4floor).
\]
Applying these with \(x=R-1\) and \(x=2R-1\), and subtracting
\[
\sum_{r=2}^R	au(\gcd(r,2))=(R-1)+\lfloor R/2floor
\]
and the constant term \(2(R-1)\), yields
\[
\sum_{r=2}^R N(r)
=3R\log R+\left(6\gamma+2\log2-rac{13}2ight)R+O(\sqrt R).
\]
Dividing by \(R(R-1)\) gives the density statement.

## Verification
The accompanying script `verify_terminal_layer.py` performs three independent finite replays. First, for \(2\le r\le8\), it evaluates Fletcher's full subset criterion over every nonempty coordinate subset and compares it with the divisor law. Second, for \(2\le r\le400\), it checks every Reid--Tai group element in both heavy charts, evaluates the reduced three-stratum quasismoothness test, and verifies the exact divisor count. Third, for every \(2\le R\le5000\), it compares the direct cumulative count with the closed summatory identities built from the divisor summatory function. The script returns `VERIFY_OK`.

The finite replay is a regression check only; the all-dimensional statements are proved above.

## Relationship to prior work
Fletcher's weighted-complete-intersection framework gives a general monomial criterion for quasismooth hypersurfaces. Kasprzyk gives general terminal and canonical criteria for weighted projective spaces. Paemurru develops classification methods for quasismooth weighted del Pezzo hypersurfaces and illustrates how arithmetic conditions on weights control existence. These sources provide the ambient criteria, but the inspected statements do not isolate the all-dimensional terminal layer \(b-a=r-1\), do not give the three-divisor classification above, and do not derive its exact divisor-function count or the zero-density asymptotic.

A prior record for the same two-heavy-weight ambient family treated quasismooth anticanonical hypersurfaces only on the canonical but non-terminal boundary. The present statement is on the adjacent terminal layer and its main enumerative conclusion is the divisor law and summatory density, so it is not implied by that earlier boundary classification.

## Limitations
The originality search cannot rule out an equivalent arithmetic specialization hidden in older weighted-hypersurface tables or unpublished computations. Fletcher's criterion is sufficiently general that the local quasismoothness reduction is a specialization of known machinery; the new content claimed here is the exact terminal-layer divisor classification together with the closed count and summatory asymptotic. No claim is made about the remaining terminal layers \(b-a\le r-2\).

## References
- E. Paemurru, *Del Pezzo Surfaces in Weighted Projective Spaces*, arXiv:1301.5430, first posted 2013-01-23.
- A. M. Kasprzyk, *Classifying terminal weighted projective space*, arXiv:1304.3029, first posted 2013-04-10.
- A. R. Fletcher, *Working with Weighted Complete Intersections*, MPI/89-35 (1989), especially the hypersurface quasismoothness criterion.
