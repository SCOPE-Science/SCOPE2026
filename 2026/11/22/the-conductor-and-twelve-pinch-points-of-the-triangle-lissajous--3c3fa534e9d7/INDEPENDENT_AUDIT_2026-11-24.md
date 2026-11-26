# Independent mathematical audit

## correctness

PASS

With B=C[y,z], the two conics give a smooth integral Laurent polynomial ring R, free of rank four over B. Writing C=y²+z²−2y²z² gives x²=C+2yzst. The basis coefficient matrix for 1,x,x²,x³ in 1,s,t,st has determinant 4y²z²(y²−z²), proving that the displayed monic quartic is minimal over Frac(B). Hence A is its monogenic B-order, with the same fraction field as R; R is finite by the monic s,t equations and normal by smoothness. For an independent conductor check, write M^∨ for the B-trace dual in this fraction field. The monogenic identity A^∨=F_x(x)⁻¹A follows by Lagrange interpolation: Tr(h(x)/F_x(x)) is the coefficient of x³ in the remainder of h modulo F, and the coefficient pairing on 1,x,x²,x³ is unimodular (unit antidiagonal and zeros before it). The two quadratic sign involutions similarly give R^∨=(4st)⁻¹R, with dual basis 1/4,1/(4s),1/(4t),1/(4st). Biduality shows that rR⊂A iff rA^∨⊂R^∨; since A⊂R and 1∈A this is exactly r∈F_x(x)R^∨. Now F_x(x)=4x(x²−C)=8xyzst, giving (xyz)R. Multiplying 2xyz by the basis of R recovers the four claimed generators in A. Away from the image of xyz=0 the normalization is an isomorphism, and the equation on each coordinate plane cuts out the stated two lines set-theoretically. To check all other points, not just generic ones, symmetry reduces to (x,y,z)=(z₀,0,z₀), z₀≠0. Choose s=√(1−y²) near y=0 with s=1 there. In that neighborhood F factors as the product of (x−zs)²−y²(1−z²) and (x+zs)²−y²(1−z²); the second factor is a unit. If z₀²≠1 the first factors into two independent smooth linear coordinates in x−zs and y using a nonvanishing analytic square root of 1−z². If z₀²=1, c=1−z² is a local coordinate and the first factor is exactly a²−b²c with a=x−zs and b=y. Symmetry yields the twelve distinct points. Near the origin both analytic square roots exist; x=±z√(1−y²)±y√(1−z²) gives four smooth graphs with the four distinct tangent planes. This independently checks all strata over C; the supplied symbolic script was inspected and not executed.

## originality

PASS

The sextic, its parametrization and irreducibility are credited to the primary literature. A separate same-day general Resultary theorem also covers this normalization and singular support and the generic crossing type. Another same-day theorem has twelve pinches on other phases, explicitly excluding this phase. The surviving supported contribution is the exact conductor in both rings and the exhaustive affine analytic refinement at the exceptional points of the phase-zero member in the cosine-phase convention. The inspected sources do not supply that refinement and ideal jointly or as mechanically implied statements; no relative priority among the same-day records is inferred.

## value

PASS

This is a standard small nonnormal example from the triangle Lissajous/Kuramoto setting, not an arbitrary specialization: at this phase all six singular lines meet at a single four-branch point. The exact conductor gives scheme-level gluing data beyond the known support and separates it from the Jacobian scheme. The exhaustive analytic description distinguishes pinching from transverse double crossing and the four-branch origin. These are useful geometric invariants within the stated affine scope; no claim is made about infinity or an entire family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
