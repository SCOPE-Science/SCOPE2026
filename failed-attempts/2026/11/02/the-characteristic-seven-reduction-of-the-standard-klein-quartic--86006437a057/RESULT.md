# The characteristic-seven reduction of the standard Klein quartic has one wild cusp

## Finding
Let \(C\) be the plane quartic \(x^3y+y^3z+z^3x=0\) over \(\mathbb F_7\). Its only geometric singularity is \(P=[1:2:4]\); it is geometrically unibranch, has one Puiseux pair \((2,7)\), and has delta invariant \(3\). The normalization is the projective line over \(\mathbb F_7\). In particular, for every integer \(m\ge1\),
\[
\#C(\mathbb F_{7^m})=7^m+1,\qquad Z(C/\mathbb F_7,T)=\frac{1}{(1-T)(1-7T)}.
\]
The result is about the reduction of the displayed integer-coefficient equation, not stable reduction of a smooth model over a ramified extension.

## Assumptions and scope
Work over \(k=\overline{\mathbb F}_7\). A geometric branch means a branch in the completed local ring after extending scalars to \(k\). The delta invariant is the length of the quotient of the normalization by the local curve ring. The formula applies to the reduced scheme defined by the displayed quartic and all its finite extensions.

## Proof
Write \(f=x^3y+y^3z+z^3x\). Its homogeneous partial derivatives are \(f_x=3x^2y+z^3\), \(f_y=x^3+3y^2z\), \(f_z=y^3+3z^2x\). If a projective critical point has a zero coordinate, the partial equations force all coordinates to vanish, an impossibility. Thus \(x\ne0\); put \(x=1,y=a,z=b\). The derivative equations give \(b=2a^{-2}\) and \(a^7=2\). Since \(a^7-2=(a-2)^7\) in characteristic seven, the unique geometric solution is \(a=2,b=4\). Euler's identity \(4f=xf_x+yf_y+zf_z\) ensures it lies on \(C\). Therefore the geometric singular support consists of this one rational point.

Set \(a=2+u\) and \(b=4+t\). An exact expansion modulo seven gives
\[
f(1,2+u,4+t)=u^3t-3u^3-u^2t+3u^2-2ut+t^3-2t^2.
\]
Make the polynomial coordinate change \(u=5t+3t^2+2t^3+\ell\). The transformed equation is exactly
\[
\begin{aligned}
f={}&\ell^3t-3\ell^3-\ell^2t^4-2\ell^2t^3+2\ell^2t^2+3\ell^2t+3\ell^2\\
 &-2\ell t^7+t^{10}-2t^9-t^8+t^7.
\end{aligned}
\]
Assign weights \(\operatorname{wt}(t)=2\), \(\operatorname{wt}(\ell)=7\). Its terms of minimum weight fourteen are \(3\ell^2+t^7\), and every other monomial has strictly greater weight. The Newton-Puiseux criterion for a Weierstrass polynomial with coprime Newton intercepts \((2,7)\), valid in characteristic different from two, gives precisely one geometric branch with multiplicity two and characteristic pair \((2,7)\). Equivalently, formal Weierstrass preparation and completion of the square give a unit times \(L^2+t^7u(t)\), where \(u(0)\ne0\); adjoining a seventh root of the unit in the algebraically closed completed coefficient field gives the branch parametrization. Its delta invariant is \((2-1)(7-1)/2=3\).

The singularity is unibranch, so \(C\) cannot have distinct geometric irreducible components: any two positive-degree plane components meet, and such an intersection creates at least two local branches at a geometric singular point. Hence \(C\) is geometrically integral. The plane quartic has arithmetic genus three. The genus formula then gives geometric genus \(3-3=0\) for its normalization \(\widetilde C\). The unique preimage of \(P\) is rational because the branch is unique and \(P\) is rational, so the smooth projective genus-zero curve \(\widetilde C\) is \(\mathbb P^1_{\mathbb F_7}\).

The finite normalization morphism is bijective on geometric points: it is an isomorphism outside \(P\) and has one geometric point above \(P\). Since the singular point and its preimage are rational, this bijection respects Frobenius and gives \(\#C(\mathbb F_{7^m})=\#\mathbb P^1(\mathbb F_{7^m})=7^m+1\) for all \(m\ge1\). The displayed zeta function follows from its exponential definition.

## Verification
The singular derivatives reduce to \(b=2a^{-2}\), \(a^7=2\). Exact symbolic expansion on the affine chart produces the two polynomials displayed in the proof. Their lowest weighted part is \(3\ell^2+t^7\). Direct enumeration of \(\mathbb P^2(\mathbb F_7)\) gives \(8\) points, agreeing with the all-extension argument for \(m=1\). The reproducibility script independently evaluates the polynomial expansions and the \(\mathbb F_7\) point count, but a finite check alone is not the proof of the general statement.

## Relationship to prior work
Elkies's 1998 treatment of the Klein quartic explicitly discusses its potential good reduction at seven and a smooth hyperelliptic model after ramified base extension; those statements concern a different integral model and do not entail that the unmodified integer equation defines a smooth special fiber. The present computation gives the singularity type and normalization of the *particular standard plane equation* modulo seven. The distinction between an integral plane model and potentially good stable reduction is essential. An equivalent old coordinate-level computation could exist outside the inspected materials; no assertion of historical priority is made.

## Limitations
The special fiber just studied is not the good stable model after extension of the discrete valuation ring. Its point counts do not compute the local Euler factor of the generic Klein quartic at the bad prime. The exact singularity classification does not describe the full stable reduction configuration or its monodromy.

## References
Noam D. Elkies, *The Klein Quartic in Number Theory*, in *The Eightfold Way*, MSRI Publications 35 (1998), pp. 51–102, especially the characteristic-seven discussion, https://library.slmath.org/books/Book35/files/elkies.pdf. Dolgachev–Kondō, arXiv:1008.4104 (first posted 2010-08-24), for an independently dated archival reference to characteristic-dependent Klein-quartic geometry.
