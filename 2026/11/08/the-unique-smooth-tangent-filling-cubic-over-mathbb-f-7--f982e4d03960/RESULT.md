# The unique smooth tangent-filling cubic over \(\mathbb F_7\)

## Finding
A plane curve over \(\mathbb F_7\) is *tangent-filling* when the tangent lines at all of its rational smooth points cover every point of \(\mathbb P^2(\mathbb F_7)\). The smooth cubic
\[
 C:\quad XY^2-X^2Z-2YZ^2=0
\]
is tangent-filling. Among **geometrically smooth** plane cubic curves over \(\mathbb F_7\), every tangent-filling cubic is projectively equivalent to \(C\) over \(\mathbb F_7\). Consequently the minimum degree of any geometrically irreducible tangent-filling plane curve over \(\mathbb F_7\) is exactly \(3\). The unique smooth cubic class has \(12\) rational points and **no rational flexes**. Its twelve distinct rational tangent lines have incidence spectrum \(1^{36},2^9,3^9,5^3\) on the \(57\) rational ambient points.

## Assumptions and scope
All curves and projective equivalences are defined over \(\mathbb F_7\), while smoothness and geometric irreducibility mean after extending to the algebraic closure. A rational tangent is the tangent at a smooth \(\mathbb F_7\)-rational point; tangents at nonrational points do not count. The uniqueness assertion concerns **smooth** plane cubics, not arbitrary singular irreducible cubic models. The finite census is one exact component of a proof, based on a complete system of normal forms justified below.

## Proof

### Explicit smoothness and coverage
For \(F=XY^2-X^2Z-2YZ^2\) the three partial derivatives are
\[
 F_X=Y^2-2XZ,\qquad F_Y=2XY-2Z^2,\qquad F_Z=-X^2-4YZ.
\]
A common projective zero of these derivatives with \(Z=0\) would have \(X=Y=0\). If instead \(Z=1\), the equations give \(XY=1\) and \(Y^2=2X\), hence \(Y^3=2\). The third equation gives \(X^2=-4Y\); multiplying by \(Y^2\) and using \(XY=1\) gives \(Y^3=-1/4=5\) in \(\mathbb F_7\), a contradiction. The same argument over the algebraic closure establishes geometric smoothness.

Write \(S=\{1,2,4\}\) and \(N=\{3,5,6\}=-S\) for the nonzero squares and nonsquares in \(\mathbb F_7\). Direct substitution and differentiation at the twelve rational curve points yield precisely the following twelve different rational tangent lines:
\[
 Z=0,\quad X=0,\quad Y=0,\quad X+sZ=0\ (s\in S),\quad Y+nZ=0\ (n\in N),\quad X+sY=0\ (s\in S).
\]
Every point on a coordinate line is covered. For a point with all coordinates nonzero set \(x=X/Z\), \(y=Y/Z\). If \(x\in N\), it is on \(X+sZ=0\) for \(s=-x\in S\); if \(y\in S\), it is on \(Y+nZ=0\) for \(n=-y\in N\). In the remaining case \(x\in S,\ y\in N\), the ratio \(-x/y\) lies in \(S\), hence the point lies on \(X+sY=0\) for \(s=-x/y\). Thus all \(57\) rational points are covered. Counting incidences independently gives \(36\) points on one of these tangent lines, \(9\) on two, \(9\) on three, and \(3\) on five.

### Exhaustiveness of the smooth cubic classification
Every geometrically smooth cubic over \(\mathbb F_7\) has an \(\mathbb F_7\)-point by the Hasse bound \(\#C(\mathbb F_7)\ge8-2\sqrt7>0\). Choosing a rational origin makes it an elliptic curve. Since the characteristic is neither \(2\) nor \(3\), it has a short Weierstrass form
\[
 E_{a,b}:\quad y^2=x^3+ax+b,\qquad a,b\in\mathbb F_7,\quad 4a^3+27b^2\ne0.
\]
For a degree-three plane embedding the pullback of a line is a rational divisor class of degree \(3\). The rational isomorphism \(\operatorname{Pic}^3(E)(\mathbb F_7)\cong E(\mathbb F_7)\) identifies this class uniquely with \(2O+T\) for some \(T\in E(\mathbb F_7)\). Any degree-three line bundle on an elliptic curve is very ample, and changing the basis of its three global sections changes the plane model by a rational projective transformation.

For \(T=O\), the basis \(1,x,y\) yields the usual homogeneous Weierstrass cubic. If \(T=(u,v)\ne O\), the basis
\[
 1,\quad x,\quad w=\frac{y+v}{x-u}
\]
of \(H^0(E,\mathcal O_E(2O+T))\) gives the cubic
\[
 (X-uZ)Y^2-2vYZ^2-(X^2+uXZ+(u^2+a)Z^2)Z=0.
\]
The denominator in \(w\) cancels at \(-T\), with the expected divisor behavior also for rational two-torsion, and the sections have the required pole bounds at \(O,T\). Consequently these are *all* smooth plane cubic models, up to rational projective change of coordinates.

There are exactly \(42\) nonsingular parameter pairs \((a,b)\). Enumerating each \(T\in E_{a,b}(\mathbb F_7)\) including \(O\) produces \(336\) complete-series models, with redundancies allowed. The standalone exact integer-arithmetic script `verify_cubic_census.py` exhausts all such pairs, points, gradients, distinct tangent lines and ambient coverage. Its **only** covering entries are
\[
 (a,b)=(0,1),\qquad T\in\{(0,1),(0,6),(1,3),(1,4),(2,3),(2,4),(4,3),(4,4)\}.
\]
There are no other smooth tangent-filling cubic models because every possible one is covered by the complete-series normal forms. This is an exhaustive finite classification, not an extrapolation from sampled coefficients.

The elliptic group \(E_{0,1}(\mathbb F_7)\) has \(12\) elements and full rational two-torsion \(\{O,(3,0),(5,0),(6,0)\}\); hence its group structure is \(\mathbb Z/6\mathbb Z\oplus\mathbb Z/2\mathbb Z\), and \(3E_{0,1}(\mathbb F_7)\) is precisely its four rational two-torsion points. The eight listed \(T\)'s are its complement, i.e. the two nonzero classes in \(E(\mathbb F_7)/3E(\mathbb F_7)\cong\mathbb Z/3\mathbb Z\). Translation by a rational point changes the degree-three class by a multiple of three; inversion exchanges the two nonzero classes. Hence all eight covering models are \(\operatorname{PGL}_3(\mathbb F_7)\)-equivalent. A rational flex occurs exactly when there is a rational \(P\) such that \(3P\sim2O+T\), equivalently \(T\in3E(\mathbb F_7)\); thus the filling class has no rational flex.

### Minimality
A line can cover only its own rational points, so degree one is impossible. A geometrically irreducible smooth conic over \(\mathbb F_7\) has rational points not on any rational tangent (the classical *internal points*: \(7\cdot6/2=21\) of them), so cannot be tangent-filling. A degree-two \(\mathbb F_7\)-irreducible conic that becomes reducible over the algebraic closure has no smooth rational points, so it also cannot fill. This excludes every geometrically irreducible plane curve of smaller degree.

## Verification
From the directory containing the files run `python3 verify_explicit_tangents.py` and `python3 verify_cubic_census.py`; both require Python 3 standard library only. The first independently reconstructs the explicit point/tangent sets and incidence spectrum; the second tests every smooth short-Weierstrass model and every rational degree-three line-bundle class, and reports the complete list of the eight covering representatives. The direct square/nonsquare coverage and the elliptic group argument are mathematical proofs independent of finite output. The completeness of the census is supplied by the Picard classification above; the script alone would not establish completeness without it.

## Relationship to prior work
Asgarli–Ghioca introduce the tangent-filling condition, ask for minimum irreducible degree in their Question 1.5, and construct degree-\(q-1\) examples for sufficiently large \(q\). Their Remark 3.7 explicitly notes that their characteristic-seven degree-six specialization fails to be tangent-filling. The present explicit cubic, its no-rational-flex structure, and the complete smooth cubic equivalence classification answer their minimum-degree question at \(q=7\) and do not follow from those published constructions. The nearby published classifications for \(\mathbb F_3\) and the negative smooth-cubic case over \(\mathbb F_5\) concern different fields. Targeted searches and inspected primary literature found no earlier implication of the full characteristic-seven statement; this does not prove global historical priority.

## Limitations
The claim is for the prime field \(\mathbb F_7\), not for extensions or other characteristics. Classification of singular degree-three tangent-filling plane curves is not attempted. The uniqueness is among smooth cubic plane models only, and the eight enumerated normal forms are not asserted to be distinct projective classes. Externally unindexed finite-geometric constructions could predate this account. The enumerator is a finite mathematical certificate together with the normal-form proof, not a machine-verified foundational proof. No independent mathematical audit or validation has occurred.

## References
Asgarli, Shamil, and Dragos Ghioca. *Tangent-filling plane curves over finite fields*. arXiv:2302.13420, first public February 26, 2023; Bulletin of the Australian Mathematical Society **109** (2024), 301–315. In particular Introduction/Question 1.5 and Remark 3.7. https://arxiv.org/abs/2302.13420

Standard elliptic-curve facts used: Hasse's rational point bound, the degree-three Picard parameterization, very ampleness of positive-degree line bundles of degree at least three on elliptic curves, and the flex criterion for degree-three embeddings. These standard facts are restated where used.
