# Wild normalization and embedded Jacobian defects of the characteristic-two Steiner quartic

## Finding

Over the finite field \(\mathbb F_2\), let \(X\subset\mathbb P^3\), with coordinates \([W:X:Y:Z]\), be the quartic defined by
\[
F=WXYZ+(XY+XZ+YZ)^2=0.
\]
The normalization is \(\mathbb P^2\), via the finite birational map
\[
\nu([a:b:c])=[a^2+b^2+c^2:bc:ac:ab].
\]
Its conductor, viewed as an ideal on the normalization, is \(\mathcal O_{\mathbb P^2}(-3)\), with reduced conductor divisor the coordinate triangle \(abc=0\).

The reduced singular locus consists precisely of the three coordinate lines \(L_X=V(Y,Z)\), \(L_Y=V(X,Z)\), and \(L_Z=V(X,Y)\), meeting at the triple point with three distinct tangent planes \(P_0=[1:0:0:0]\). On the normalization, each coordinate edge maps to its corresponding singular line by a separable degree-two map, with exactly one *wild* ramification point in characteristic two: \(P_X=[0:1:0:0]\), \(P_Y=[0:0:1:0]\), and \(P_Z=[0:0:0:1]\). These are the mod-two coalescences of the two characteristic-not-two branch values on each line; we do not identify their singularity germs with classical Whitney pinch points.

The projective Jacobian singular scheme is reduced at the generic points of all three lines and at \(P_0\), but has an embedded finite-length defect of length \(3\) at each of \(P_X,P_Y,P_Z\). More precisely, on the affine chart \(X=1\), writing \(w=W/X\), \(y=Y/X\), and \(z=Z/X\), its ideal is
\[
J=(yz,wy,wz,(y+z)^2)\subset k[w,y,z],
\]
while the reduced line has ideal \((y,z)\); the quotient \((y,z)/J\), supported at \((w,y,z)=(0,0,0)\), has length \(3\).

For every \(q=2^m\) with \(m\ge1\), the exact rational point count and Hasse–Weil zeta function are
\[
\#X(\mathbb F_q)=q^2+q+2,\qquad
Z(X,T)=\frac1{(1-T)^2(1-2T)(1-4T)}.
\]
Thus \(\#X(\mathbb F_q)=\#\mathbb P^2(\mathbb F_q)+1\) for every such \(q\).

## Assumptions and scope

All geometric assertions are after extension of scalars from \(\mathbb F_2\) to an arbitrary algebraically closed field \(k\) of characteristic \(2\). Singular *scheme* means the closed subscheme defined locally by \(F\) and its partial derivatives, not just its reduced support. The phrase “embedded defect of length \(3\)” refers to the coherent quotient of the radical ideal by the Jacobian ideal near each named special point. The zeta function is over the original \(\mathbb F_2\)-model, and the point-count identity holds for all finite extensions \(\mathbb F_{2^m}\).

## Proof

**Normalization and irreducibility.** Substituting the displayed parametrization gives \(XY+XZ+YZ=abc(a+b+c)\) and \(WXYZ=a^2b^2c^2(a^2+b^2+c^2)\), hence \(F\circ\nu=0\). The four homogeneous quadratic coordinates have no common zero in \(\mathbb P^2\), so \(\nu\) is a morphism and \(\nu^*\mathcal O_X(1)=\mathcal O_{\mathbb P^2}(2)\). It cannot contract a curve because its pullback of an ample line bundle has positive degree on every curve. A proper quasi-finite morphism is finite. On \(XYZ\ne0\), one recovers the parameter by \([a:b:c]=[YZ:XZ:XY]\); thus the morphism is birational. The polynomial \(F\) is irreducible: it is linear in \(W\), and the polynomials \(XYZ\) and \((XY+XZ+YZ)^2\) are coprime. Since \(\mathbb P^2\) is normal, the finite birational morphism is the normalization.

**Singular support and triple point.** The four homogeneous partial derivatives are \(XYZ\), \(WYZ\), \(WXZ\), and \(WXY\). If \(W\ne0\), all vanish precisely when at most one of \(X,Y,Z\) is nonzero. If \(W=0\), the equation requires \(XY+XZ+YZ=0\); together with \(XYZ=0\), this again forces at least two of \(X,Y,Z\) to vanish. This proves the three-line description. In the chart \(W=1\) at \(P_0\), the local equation has lowest homogeneous term \(XYZ\), a reduced product of three distinct planes; thus \(P_0\) has multiplicity three with three distinct plane components in its tangent cone. The local Jacobian ideal is \((XY,XZ,YZ)\), since \(XYZ\) and the square of \(XY+XZ+YZ\) already belong to this ideal.

**Conductor.** The inverse image of the nonnormal locus is the reduced coordinate triangle \(abc=0\). Away from that triangle \(\nu\) is an isomorphism. The finite morphism has \(\nu^*\mathcal O_X(1)=\mathcal O_{\mathbb P^2}(2)\). The quartic hypersurface has invertible dualizing sheaf \(\omega_X\simeq\mathcal O_X\), while \(\omega_{\mathbb P^2}\simeq\mathcal O_{\mathbb P^2}(-3)\). Finite duality identifies the conductor \(\operatorname{Hom}_{\mathcal O_X}(\nu_*\mathcal O_{\mathbb P^2},\mathcal O_X)\), as an ideal on the normalization, with \(\omega_{\mathbb P^2}=\mathcal O_{\mathbb P^2}(-3)\). Since its support is precisely the coordinate triangle, which has degree three, the conductor divisor is that triangle with reduced multiplicities.

**Wild ramification and Jacobian defects.** On the edge \(a=0\), the normalization map becomes \([0:b:c]\mapsto[b^2+c^2:bc:0:0]\). For \(t=b/c\) and \(bc\ne0\), the affine coordinate on \(L_X\) is \(\lambda=W/X=t+t^{-1}\). This defines a separable quadratic function-field extension with minimal polynomial \(t^2+\lambda t+1\). Its derivative with respect to \(t\) vanishes only at \(t=1\), where \(\lambda=0\). The ramification index is two, divisible by the characteristic. Cyclic permutation gives the other two special points.

On \(X=1\), \(F=wyz+(y+z+yz)^2\). Taking partial derivatives and including \(F\), the Jacobian ideal is precisely \(J=(yz,wy,wz,(y+z)^2)\). Modulo \(J\), \(yz=wy=wz=0\) and \(y^2=z^2\). All monomials in the ideal \((y,z)\) of degree at least three vanish; the classes of \(y,z,y^2=z^2\) are a \(k\)-basis of \((y,z)/J\), which therefore has length three. If \(w\ne0\), the Jacobian ideal is \((y,z)\). Cyclic permutations establish the complete statement and show there are no other embedded defects.

**Point counts and zeta function.** On the open subset \(XYZ\ne0\), choose the chart \(X=1\). There are \((q-1)^2\) choices of the nonzero pair \((Y,Z)\), and the equation gives a unique \(W\). All remaining points lie on the three rational coordinate lines, whose union has \(3(q+1)-2=3q+1\) points: three projective lines with exactly one common point. Therefore the point count equals \((q-1)^2+3q+1=q^2+q+2\). Taking the exponential generating series \(\exp(\sum_{m\ge1}\#X(\mathbb F_{2^m})T^m/m)\) yields the stated zeta function.

## Verification

The companion standard-library script `verify_steiner.py` enumerates normalized projective points over \(\mathbb F_2\), \(\mathbb F_4\), \(\mathbb F_8\), and \(\mathbb F_{16}\), verifies the defining equation, reduced singular support, rational-point count, and the relation between points and normalization fibers. The attached `verification_output.txt` is the output from a successful execution. The argument above, not finite-field sampling, establishes the formulas for arbitrary characteristic-two algebraically closed fields and all finite extensions.

## Relationship to prior work

The characteristic-not-two Steiner Roman surface, including the same quadratic parametrization, quartic equation up to signs, three double lines, triple point with three distinct tangent planes, and classical six pinch points, is prior knowledge (Coffman–Schwartz–Stanton, 1996; Coffman's exposition). Moving-plane approaches to singularity detection are developed by Chen–Wang (2009), and Fitting-ideal techniques for parametrized surfaces by Botbol–Busé–Chardin (2013). Wang–Chen (2012) specifically treats Steiner surfaces, so its inaccessible full text is a historical-priority risk. The claims assessed here are the **characteristic-two behavior**: one wild branch point on each conductor line, the three local length-three embedded Jacobian defects, and the uniform rational-point and zeta correction. No claim of novelty is made for the classical parametrization or quartic equation.

## Limitations

The result is specific to the stated mod-two integral model; it does not classify all characteristic-two quadratically parametrized quartics or deformations. The points called wild ramification points are not asserted to have classical Whitney-pinch analytic normal forms. The lack of full-text access to the directly related 2012 specialist paper leaves an explicit historical-priority uncertainty. No independent external review has been performed.

## References

- Coffman, A., Schwartz, A. J., and Stanton, C., “The algebra and geometry of Steiner and other quadratically parametrizable surfaces,” *Computer Aided Geometric Design* 13 (1996), 257–286; related exposition: https://users.pfw.edu/CoffmanA/steinersurface.html.
- Chen, F., and Wang, X., “Moving Planes and Singular Points of Rational Parametric Surfaces,” arXiv:0909.2810 (first version September 15, 2009), https://arxiv.org/abs/0909.2810.
- Wang, X., and Chen, F., “Implicitization, parameterization and singularity computation of Steiner surfaces using moving surfaces,” *Journal of Symbolic Computation* 47 (2012), 733–750, DOI:10.1016/j.jsc.2011.12.029.
- Botbol, N., Busé, L., and Chardin, M., “Fitting ideals and multiple-points of surface parameterizations,” arXiv:1310.4915 (2013), https://arxiv.org/abs/1310.4915.
