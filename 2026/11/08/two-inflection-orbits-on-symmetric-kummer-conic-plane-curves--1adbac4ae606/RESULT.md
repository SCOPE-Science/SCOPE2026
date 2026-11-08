# Two inflection orbits on symmetric Kummer–conic plane curves

## Finding
For every integer \(n\ge3\), the complex projective plane curve
\[
C_n:\quad x^{2n}+y^{2n}+z^{2n}+x^ny^n+x^nz^n+y^nz^n=0
\]
is smooth of degree \(2n\). Its entire set of inflection points splits into exactly two orbits under the coordinatewise roots-of-unity symmetries and coordinate permutations:

* Precisely \(6n\) points on the coordinate axes; at each, the tangent has exact intersection multiplicity \(n\).
* Precisely \(6n^2\) points off the coordinate axes; at each, the tangent has exact intersection multiplicity \(3\).

In particular, if \(n=3\), all \(72\) points are ordinary flexes, whereas for \(n\ge4\) the \(6n\) axis points are higher-order flexes. No other inflection points occur. The off-axis set is a single free orbit under \((\mu_n)^2\rtimes S_3\), and the axis set is also a single orbit.

The off-axis points are explicit: under \(\pi([x:y:z])=[x^n:y^n:z^n]\), their images are the six permutations of the roots of
\[
T^3-T^2+T+\frac{3(n-1)}{5n-1}=0,
\]
normalized by \(X+Y+Z=1\). Every one of these six base points has exactly \(n^2\) lifts.

## Assumptions and scope
All arguments are over \(\mathbb C\), with \(n\in\mathbb Z\) and \(n\ge3\). A point is an inflection point when its tangent line has local intersection multiplicity at least three. The inflection weight is this multiplicity minus two. The group \((\mu_n)^2\) consists of coordinatewise multiplication by \(n\)-th roots of unity modulo common scalars, and \(S_3\) permutes the coordinates. This theorem concerns tangent lines in the displayed plane embedding, not osculating conics or other embeddings.

## Proof
**Step 1: Smoothness.** Set
\[
Q(X,Y,Z)=X^2+Y^2+Z^2+XY+XZ+YZ
\]
and \(F(x,y,z)=Q(x^n,y^n,z^n)\). The Hessian matrix of \(Q\) has determinant \(4\), hence \(Q=0\) is a nonsingular conic. The finite map \(\pi\) is étale away from the coordinate axes, so \(C_n\) is smooth there. The restriction of \(Q\) to any coordinate axis has two distinct nonzero roots (the ratio satisfies \(T^2+T+1=0\)). Consequently, \(C_n\) meets each coordinate axis at \(2n\) distinct points with nonzero derivative along that axis. Thus all of \(C_n\) is smooth. A smooth positive-degree plane curve is irreducible.

**Step 2: Factor the Hessian.** Put \(X=x^n\), \(Y=y^n\), \(Z=z^n\) and write \(Q_i\) for the partial derivatives of \(Q\). The chain rule, followed by diagonal conjugation on the dense coordinate torus and polynomial continuation, gives
\[
\det(\operatorname{Hess}F)=n^3(xyz)^{n-2}R_n(x^n,y^n,z^n),
\]
where
\[
R_n=\det\!\left((n-1)\operatorname{diag}(Q_X,Q_Y,Q_Z)
+n\operatorname{diag}(X,Y,Z)\operatorname{Hess}Q\right).
\]
With \(e_1=X+Y+Z\), \(e_2=XY+XZ+YZ\), and \(e_3=XYZ\), exact determinant expansion yields
\[
R_n=2(n-1)^2(2n-1)e_1^3
 +(n-1)(2n-1)(4n-1)e_1e_2
 +(2n-1)^2(5n-1)e_3.
\]
Since \(Q=e_1^2-e_2\), the residual condition on the conic becomes
\[
R_n|_{Q=0}=(2n-1)^2\bigl(3(n-1)e_1^3+(5n-1)e_3\bigr).
\]

**Step 3: The residual intersections.** A common point of \(Q=0\) and \(R_n=0\) cannot have \(e_1=0\): then \(e_2=e_3=0\), impossible for a nonzero projective triple. Normalize \(e_1=1\). The conditions are \(e_2=1\) and \(e_3=-3(n-1)/(5n-1)\). Therefore \(X,Y,Z\) are the three roots of
\[
P_n(T)=T^3-T^2+T+\frac{3(n-1)}{5n-1}.
\]
Its discriminant is
\[
\operatorname{disc}(P_n)=-\frac{48(11n^2-16n+6)}{(5n-1)^2},
\]
which is nonzero for every integer \(n\ge3\); all roots are also nonzero. The six permutations of these distinct roots are therefore six distinct points of \(Q\) in the coordinate torus. They are simple intersections: locally the symmetric coordinate map \((X,Y,Z)\mapsto(e_1,e_2,e_3)\) has Jacobian a nonzero Vandermonde product, and the equations \(e_2=e_1^2\), \(e_3=-3(n-1)e_1^3/(5n-1)\) cut out the six projective points transversely. Equivalently, Bézout's intersection degree of the conic and residual cubic is six, so the six distinct points each have multiplicity one. The power map has \(n^2\) étale lifts over each, yielding \(6n^2\) simple zeros of the Hessian on \(C_n\). By the characteristic-zero Hessian flex criterion, their tangent contact is exactly three.

**Step 4: Axis contact and completeness.** On \(x=0\), take the affine chart \(z=1\). At a point \(P=(0,y_0,1)\) of \(C_n\), the number \(\tau=y_0^n\) is a root of \(\tau^2+\tau+1=0\), so \(1+\tau\ne0\). Since \(F_x(P)=0\) and \(F_y(P)\ne0\), the tangent is \(y=y_0\). Its restriction is
\[
F(x,y_0,1)=x^{2n}+(1+\tau)x^n,
\]
so its exact contact multiplicity is \(n\). Coordinate permutations give \(6n\) axis points. On the conic the residual factor is nonzero at these base-axis intersections: \(e_3=0\) while \(e_1\ne0\), so the displayed residual restriction is nonzero. Thus the Hessian orders there are exactly \(n-2\). All Hessian zeros are accounted for by the factorization; there are no further flexes.

**Step 5: Orbits and independent global count.** The base six-point set consists of all coordinate permutations of one ordered triple of distinct roots. Its lifts form a free orbit of size \(6n^2\) under \((\mu_n)^2\rtimes S_3\). For the axis points, permutations of axes together with swapping the two roots of \(T^2+T+1\) and the deck action make one orbit of size \(6n\). The total inflection weight is
\[
6n(n-2)+6n^2=12n(n-1)=3(2n)(2n-2),
\]
in agreement with the complete Hessian intersection degree for a smooth plane curve of degree \(2n\).

## Verification
The companion `verify_flex.py` is a standalone SymPy script requiring no files other than SymPy itself. Execute it with `python verify_flex.py`. It checks the general symbolic determinant identity and cubic discriminant, direct Hessian identities for degrees corresponding to \(n=3,4,5\), and squarefreeness of the residual cubic for six integer values of \(n\). The recorded output is `verify_output.txt`, terminating in `ALL_CHECKS_PASSED`. The general argument is the proof above; finite checks are corroborative, not a proof by enumeration.

## Relationship to prior work
Arakelian and Borges study the general plane family \(Q(x^n,y^n,z^n)=0\) in *Frobenius nonclassicality with respect to linear systems of curves of arbitrary degree*, arXiv:1409.8549 (first public 2014-09-30), particularly Section 4 and Proposition 4.2. That proposition proves existence of an order-\(n\) tangent at a coordinate point; this individual contact phenomenon is **not** claimed as new. Their results address finite-field Frobenius classicality, conic osculation, and point counts, not the complete complex-line flex divisor or its symmetry orbits.

Hidalgo, Kontogeorgis, Leyton-Álvarez, and Paramantzoglou treat hyperosculation in a different complete-intersection embedding of generalized Fermat covers in *Automorphisms of the Generalized Fermat curves*, arXiv:1409.3063 (2014-09-10), especially Theorem 17. Its projective osculation calculation does not imply the stated plane-embedding inflection distribution. The new statement is the **uniform complete two-orbit flex classification for this fixed symmetric subfamily**, not smoothness, the Kummer construction, or the previously known existence of order-\(n\) tangencies.

## Limitations
The theorem is restricted to characteristic zero, the displayed symmetric conic, and tangent lines in this plane embedding; it does not describe arbitrary coefficient choices, positive characteristic, or non-line osculation. The historical-priority assessment is based on targeted literature and semantic research-record searches, not a proof that no equivalent account exists. No independent scientific audit has been performed.

## References
1. N. Arakelian and H. Borges, *Frobenius nonclassicality with respect to linear systems of curves of arbitrary degree*, arXiv:1409.8549, 2014-09-30; Sections 3–5, Proposition 4.2. https://arxiv.org/abs/1409.8549
2. R. Hidalgo, A. Kontogeorgis, S. Leyton-Álvarez, and R. Paramantzoglou, *Automorphisms of the Generalized Fermat curves*, arXiv:1409.3063, 2014-09-10; Sections 2 and 3.3, Theorem 17. https://arxiv.org/abs/1409.3063
3. Classical characteristic-zero Hessian criterion for flexes of smooth plane curves, as applied with the explicit determinant in the proof.
