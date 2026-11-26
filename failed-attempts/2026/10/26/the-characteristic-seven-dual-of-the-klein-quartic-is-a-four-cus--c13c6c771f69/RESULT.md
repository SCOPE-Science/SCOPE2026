# The characteristic-seven dual of the Klein quartic is a four-cuspidal quintic

## Finding
Over an algebraically closed field of characteristic \(7\), the projective dual of the plane Klein quartic \(K: X^3Y+Y^3Z+Z^3X=0\) is the integral plane quintic
\[
K^\vee:\quad A^3C^2-3A^2B^3+2B^2C^3=0.
\]
Its normalization is \(\mathbb P^1\), its singular locus consists of exactly four points, namely \([1:0:0]\), \([0:1:0]\), \([0:0:1]\), and \([2:4:1]\). The first three have unibranch local analytic type \(u^2-v^3\), and the last has type \(u^2-v^7\). Thus the respective \(\delta\)-invariants are \(1,1,1,3\), and the intrinsic Jacobian singular scheme has total length \(3\cdot2+7=13\). In contrast to the class \(12\) of a smooth characteristic-zero plane quartic, this characteristic-seven dual has degree \(5\).

## Assumptions and scope
The base field \(k\) is algebraically closed with \(\operatorname{char}(k)=7\). Dual coordinates \([A:B:C]\) represent lines \(AX+BY+CZ=0\) in the original plane. Local analytic type means completed local ring over \(k\). All assertions concern the reduced projective dual, the closure of tangent lines at smooth points; no claim is made about a flat integral family of dual schemes.

## Proof
Put \(h=S/T\). The following three homogeneous quartics in \([S:T]\), here displayed in the affine coordinate \(h\), have no common zero:
\[
P(h)=[4(h+3)^3(h-2):(h+3)(h-1)^3:2(h-1)(h-2)^3].
\]
Substitution gives \(X^3Y+Y^3Z+Z^3X=0\). Their derivatives have projective tangent cross product
\[
P(h)\times P'(h)=[2(h-2)^2(h-1)^3:-3(h+3)^2(h-2)^3:(h-1)^2(h+3)^3]=L(h).
\]
The three quintics in \(L\) have no common zero. The image of \(P\) is integral and nonconstant. As shown below, \(L\) is generically birational and represents the tangent map of \(P\); thus the generically finite map \(P\) itself must be birational, since the tangent map factors through the image of \(P\). Because the basepoint-free \(P\) is given by quartics, its irreducible image has degree \(4\) and therefore equals the plane quartic \(F=0\). It follows that \(F\) is irreducible and \(P\) its normalization; on its smooth locus the cross product represents the Gauss map.

Let \(G(A,B,C)=A^3C^2-3A^2B^3+2B^2C^3\). Direct substitution verifies \(G(L(h))=0\) in characteristic seven. Since \(L\) is basepoint-free of degree five and its image contains the three coordinate vertices, its image is not a line. The degree formula \(\deg(L)\deg(\operatorname{im}L)=5\), together with primality of five, gives \(\deg(L)=1\), \(\deg(\operatorname{im}L)=5\). Thus \(L:\mathbb P^1\to K^\vee\) is the normalization, and \(G\) is its reduced irreducible defining equation.

There are no collisions between distinct parameters. For two finite parameters \(r,t\), take the three projective cross-minors of \(L(r),L(t)\), divide by \(r-t\), and compute their reduced lexicographic Gröbner basis over \(\mathbb F_7\):
\[
\{r+3t^4+3t,\ t^6-2t^3+1\}.
\]
The second polynomial is \((t^3-1)^2\); at any zero, \(t^4=t\), hence the first forces \(r=t\). Moreover \(L(\infty)=[2:4:1]\) has no finite preimage, because \(\gcd(-3L_0-2L_1,L_0-2L_2)=1\) in \(\mathbb F_7[h]\).

For finite \(h\), the gcd of the three minors \(L_iL_j'-L_jL_i'\) is, up to a unit, \((h+3)(h-1)(h-2)\). Therefore the only finite normalization ramification parameters are \(-3,1,2\), mapping to the three coordinate vertices. In a local target chart, the two nonconstant coordinates at each have respective orders \(2,3\), yielding completed local equation \(u^2-v^3\). At \(\infty\), with \(t=1/h\), the homogeneous quintic components satisfy
\[
L_0-2L_2=t^5+2t^4-3t^2,\qquad L_1+3L_2=3t^5-2t^4-2t^2
\]
after reversal \(h\mapsto1/t\) and multiplication by \(t^5\). The local multiplicity is two; the parameterization is ramified there, so its image is singular. There are no other singularities: \(L\) is injective on geometric points and is immersive elsewhere. The arithmetic genus of the plane quintic is six. Each of the three ordinary cusps contributes \(\delta=1\), so the remaining cusp has \(\delta=3\). For a one-branch plane singularity of multiplicity two in characteristic different from two, completing the square yields equation \(u^2-f(v)\) with \(\operatorname{ord}_v f=2\delta+1=7\); absorbing a unit by a square root gives \(u^2-v^7\). This also verifies the exact local type independently of a formal expansion to order seven.

For \(u^2-v^m\) with \(m=3\) or \(7\) in characteristic seven, the quotient by the equation and its two partial derivatives has length \(m\) when \(m=7\), and length \(m-1=2\) when \(m=3\). Thus the four contributions are \(2,2,2,7\), giving length \(13\).

## Verification
Run `python CHECK.py` after installing the `requirements.txt` dependency. Exact modular polynomial identities, degree-five parametrization, gcd ramification, collision Gröbner basis, absence of finite preimages for the fourth cusp, and the original quartic Jacobian elimination are checked symbolically. The genus argument, irreducible-image degree formula and completed-local-ring classification are mathematical proof steps, not finite-field enumeration.

## Relationship to prior work
The Klein quartic and its exceptional characteristic-seven reduction have classical descriptions; the normalization and wild cusp of the original quartic are background facts, not new results here. Work on four-cuspidal rational quintics, including the unique complex \(A_6+3A_2\) quintic, supplies a close singularity-type analogue but does not by itself identify the polar dual in characteristic seven. The contribution isolated here is the explicit dual equation and normalized Gauss map together with the complete singular-scheme profile in this characteristic.

## Limitations
The result concerns only characteristic seven, the reduced dual and its intrinsic singular scheme. It does not establish that the equation or singularity basket is absent from all classical references. Literature coverage for older modular treatments of the Klein quartic, including full-text access to the cited survey, was incomplete; independent scholarly checking is recommended.

## References
- N. D. Elkies, *The Klein Quartic in Number Theory*, MSRI Publications 35 (1998), historical Klein-quartic geometry and modular arithmetic. Indexed public survey, full PDF not materially inspected in this review.
- N. Manolache and F.-O. Schreyer, *Moduli of (1,7)-polarized abelian surfaces via syzygies*, arXiv:math/9812121 (first posted 1998-12-19), geometric Klein-quartic context.
- J. Piontkowski, *On the Number of Cusps of Rational Cuspidal Plane Curves*, Experimental Mathematics 16 (2007), classification constraints for rational cuspidal quintics.
