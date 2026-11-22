# Complete torsion-zero phase diagram for meridional-dominant torus knots

## Finding
Let \(1\le p<q\) be coprime positive integers and \(R>1\). On the standard unit-tube torus take the embedded closed curve
\[
\gamma(t)=((R+\cos(qt))\cos(pt),(R+\cos(qt))\sin(pt),\sin(qt)),\qquad t\in\mathbb R/(2\pi\mathbb Z).
\]
Set \(x=(q/p)^2\), \(R_-=1+x\) and \(R_+=(1+2x)/(x-1)\). A **regular torsion zero** is a parameter for which curvature is nonzero and the Frenet torsion is zero. Count distinct parameter points, not algebraic multiplicity. Then the exact number is
\[
\boxed{N(R)=2q\bigl({\mathbf{1}}_{R>R_-}+{\mathbf{1}}_{R<R_+}\bigr)+q\,{\mathbf{1}}_{R=R_+}.}
\]
All regular zeros away from \(R=R_+\) are simple. At \(R=R_+\), the \(q\) additional points with \(\cos(qt)=1\) are quadratic (multiplicity two) torsion zeros; all other zeros remain simple. The parameter \(R=R_-\) is different: the curve has exactly \(q\) points of *vanishing curvature* at \(\cos(qt)=-1\), where Frenet torsion is undefined; these are not included in \(N\).

Since \(x\) is rational while \(1+\sqrt3\) is irrational, the two radii are always distinct. For \(1<x<1+\sqrt3\), \(R_-<R_+\), and the open-regime counts are respectively \(2q,4q,2q\) as \(R\) passes the thresholds; for \(x>1+\sqrt3\), \(R_+<R_-\), and the counts are \(2q,0,2q\). At the outer-rim threshold \(R_+\), the count is \(3q\) in the first case and \(q\) in the second. At \(R_-\) the displayed indicator formula counts only *regular* zeros, with the \(q\) zero-curvature points separately excluded.

For the trefoil \((p,q)=(2,3)\), the thresholds are \(13/4\) and \(22/5\); there are six, twelve, and six regular torsion zeros across the three open intervals, and nine distinct zeros at \(R=22/5\) (six simple, three quadratic).

## Assumptions and scope
The ambient metric is the usual Euclidean metric on \(\mathbb R^3\). Parameters are exactly \(R>1\) and coprime integers \(1\le p<q\); no self-intersecting torus, open curve, or equal-winding case is claimed. Frenet torsion is defined only where \(\gamma'\times\gamma''\ne0\). The count is over one primitive period, and geometric zero points are distinct because the curve is embedded under the coprimality assumption.

## Proof
Put \(c=\cos(qt)\), \(s=\sin(qt)\) and \(v=R+c\). In the positively oriented moving frame \((e_r,e_\theta,e_z)\) with azimuth \(pt\), the first three derivatives are
\[
\begin{aligned}
\gamma'&=(-qs,pv,qc),\\
\gamma''&=(-q^2c-p^2v,-2pqs,-q^2s),\\
\gamma'''&=(q(q^2+3p^2)s,-p^3v-3pq^2c,-q^3c).
\end{aligned}
\]
Their scalar triple product is \(p^5qF_{R,x}(c)\), with
\[
F_{R,x}(c)=(1-x)c^3+2R(1+2x)c^2+[R^2(1-x)+2x(x+2)]c-Rx(x+2).
\]
The cross product has first component \(pq^2s(c-R)\). As \(R>1\), it can vanish only when \(s=0\). At \(c=1\), the second component equals \(-q[q^2+p^2(R+1)]\ne0\). At \(c=-1\), all three components vanish precisely when \(R=1+x\). There are exactly \(q\) such points on a primitive period, proving the curvature clause without relying on the earlier literature.

For every \(-1\le c\le1\),
\[
F''_{R,x}(c)=6(1-x)c+4R(1+2x)>10+2x>0,\qquad F_{R,x}(0)=-Rx(x+2)<0.
\]
Direct endpoint factorization yields
\[
\begin{aligned}
F_{R,x}(-1)&=(R-R_-)[R(x-1)+1+2x],\\
F_{R,x}(1)&=(R+1+x)[1+2x-R(x-1)].
\end{aligned}
\]
Strict convexity and the negative central value imply there is exactly one root in \((-1,0)\) iff \(R>R_-\), and exactly one root in \((0,1)\) iff \(R<R_+\). These roots are necessarily simple: by convexity the left one is crossed with negative derivative and the right one with positive derivative. Any interior \(c\)-root gives precisely \(2q\) distinct parameter values with \(\cos(qt)=c\). The only endpoint root at \(c=1\) arises at \(R=R_+\), with \(q\) parameter values; \(F'(1)>0\) there, hence \(F(\cos(qt))\) has quadratic vanishing in \(t\) at those points. The root at \(c=-1\) arises at \(R=R_-\), but at exactly those points curvature vanishes and Frenet torsion is not defined. Summing gives the claimed formula and multiplicities.

Finally, \(R_-<R_+\) is equivalent to \(x^2-2x-2<0\), or \(1<x<1+\sqrt3\); equality cannot occur for the rational \(x=(q/p)^2\). The stated phase cases and trefoil specialization follow.

## Verification
The standalone script `verify_torus_torsion.py` (Python 3 with SymPy and NumPy) independently checks the moving-frame scalar triple product, exact endpoint factorizations, strict-convexity derivative, direct Cartesian first-three-derivative determinant at twenty independent numerical parameter points, and numerical real-root counts in five coprime winding families. Execute `python verify_torus_torsion.py`. The reported outputs are `TORUS_KNOT_TORSION_PHASE_CHECKS_OK 5 families, 30 parameter checks` and `DIRECT_CARTESIAN_DETERMINANT_OK 20`. These finite numerical tests corroborate, but do not replace, the symbolic proof for all admissible parameters.

## Relationship to prior work
Costa (1990), Proposition 1 and its proof, establishes the existence/nonexistence of torsion zeros on torus curves via a related cubic and derives the nowhere-zero-torsion window, with a specific separate note on the diagonal winding case. Its criterion implies the *zero-count* case in the middle window, but not the complete cardinalities, distinct-zero multiplicities, or the \(4q\) re-entrant region stated here. The cubic mechanism is therefore pre-existing and explicitly acknowledged: the claimed contribution is its complete root-count and collision classification for coprime \(p<q\). Fuller (1998), Theorem 2.1, independently identifies the \(q\) zero-curvature points at the inner equator on a single torus; this matches, but is not itself the torsion-zero count. There is no claim to rediscover either older theorem.

## Limitations
The classification is for this canonical circular-torus parametrization and coprime meridional-dominant winding numbers only. A different torus embedding, perturbation of the curve, or the opposite winding order may have a different phase law. Exact counts here do not imply a topological invariant of the underlying knot type. The historical literature search may miss an older explicit count obtained from Costa's cubic. Independent mathematical assessment is not provided. The public date recorded for the supporting 1998 arXiv source is the verified first-posted day; Costa's earlier 1990 issue was inspected but its exact public release day was not verified.

## References
- S. I. Rodrigues Costa, *On Closed Twisted Curves*, Proceedings of the American Mathematical Society **109** (1990), 205–214, Proposition 1 and its proof. DOI: https://doi.org/10.2307/2048380 ; readable source https://www.academia.edu/8114429/On_Closed_Twisted_Curves .
- E. J. Fuller Jr., *Torus Curves With Vanishing Curvature*, arXiv:math/9803021, first posted 1998-03-06, especially Theorem 2.1. https://arxiv.org/abs/math/9803021 .
