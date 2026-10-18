# Planar Barker–Larman rigidity for centered ellipses
## Finding
Let \(r>0\), and let
\[
E_A=\{x\in\mathbb R^2:x^{\mathsf T}Ax\le1\},
\]
where \(A\) is a real symmetric positive-definite \(2\times2\) matrix satisfying
\[
r^2\lambda_{\max}(A)<1.
\]
Thus the closed disk \(rB_2\) is contained in the interior of \(E_A\).

For every \(e\in S^1\), let
\[
H_e=\{x\in\mathbb R^2:e\cdot x=r\}
\]
be the support line of \(rB_2\) with outward normal \(e\), and define
\[
L_A(e)=\operatorname{length}(E_A\cap H_e).
\]
Then the full tangent-chord function determines the centered ellipse:
\[
L_A(e)=L_B(e)\quad\text{for every }e\in S^1
\qquad\Longrightarrow\qquad
A=B.
\]

In particular, within the complete family of origin-centered ellipses containing a prescribed centered disk, the planar Barker–Larman reconstruction problem has a global affirmative answer. No closeness-to-the-disk or bounded-eccentricity hypothesis is needed.

## Assumptions and scope
The inner body is the Euclidean disk \(rB_2\) centered at the origin, with known radius \(r>0\). The outer body is restricted to an origin-centered ellipse. Every such ellipse has a unique representation
\[
E_A=\{x:x^{\mathsf T}Ax\le1\}
\]
with \(A\) symmetric positive definite.

The strict containment condition
\[
rB_2\subset\operatorname{int}E_A
\]
is equivalent to
\[
r^2\lambda_{\max}(A)<1.
\]
It guarantees that every support line of the inner disk cuts a nondegenerate chord from the outer ellipse.

The theorem is global within this centered quadratic family. It does not claim reconstruction of an arbitrary planar convex body, and it does not claim the corresponding statement for an ellipse whose center is unknown and not fixed at the center of the inner disk.

## Proof
Fix \(e\in S^1\), and let \(v\) be the unit vector obtained by rotating \(e\) through \(\pi/2\). In the orthonormal basis \((e,v)\), write
\[
\gamma=e^{\mathsf T}Ae,
\qquad
\eta=e^{\mathsf T}Av,
\qquad
\alpha=v^{\mathsf T}Av,
\qquad
D=\det A.
\]
A point of the tangent line \(H_e\) has the form
\[
x=re+tv.
\]
The boundary equation \(x^{\mathsf T}Ax=1\) becomes
\[
\alpha t^2+2r\eta t+r^2\gamma-1=0.
\tag{1}
\]
Because \((e,v)\) is orthonormal,
\[
\alpha\gamma-\eta^2=D.
\tag{2}
\]
The discriminant of (1) is therefore
\[
4\bigl(\alpha-r^2D\bigr).
\]
The strict disk-containment hypothesis makes this quantity positive. The distance between the two roots of (1), which is exactly the chord length, is
\[
L_A(e)
=
\frac{2\sqrt{\alpha-r^2D}}{\alpha}.
\tag{3}
\]
Hence
\[
\frac{L_A(e)^2}{4}
=
\frac{\alpha-r^2D}{\alpha^2}.
\tag{4}
\]

Now suppose \(L_A=L_B\). For a unit tangent direction \(v\), put
\[
\alpha(v)=v^{\mathsf T}Av,
\qquad
\beta(v)=v^{\mathsf T}Bv,
\qquad
D=\det A,
\qquad
E=\det B.
\]
Equation (4) gives
\[
\frac{\alpha-D r^2}{\alpha^2}
=
\frac{\beta-E r^2}{\beta^2}.
\tag{5}
\]
Let
\[
s(z)=z_1^2+z_2^2
\]
and regard \(\alpha\) and \(\beta\) as homogeneous quadratic polynomials in \(z=(z_1,z_2)\). Homogenizing (5) gives the polynomial identity
\[
P(z)
=
\alpha\beta(\beta-\alpha)
+r^2s\bigl(E\alpha^2-D\beta^2\bigr)
\equiv0.
\tag{6}
\]
Indeed, (6) holds on the real unit circle by (5), and both sides are homogeneous of degree six, so it holds for all real \(z\), hence as a polynomial identity over \(\mathbb C\).

Assume first that \(\alpha\) is not proportional to \(s\), equivalently \(E_A\) is not a circle. Since \(A\) is positive definite, \(\alpha\) factors over \(\mathbb C\) into two distinct conjugate linear factors. Neither factor is isotropic for \(s\): if one were a factor of \(s=(z_1+iz_2)(z_1-iz_2)\), reality of the coefficients would force both isotropic factors and hence \(\alpha\) would be proportional to \(s\).

Let \(\ell\) be either complex zero line of \(\alpha\). On \(\ell\), identity (6) reduces to
\[
-r^2sD\,\beta^2=0.
\]
Here \(r>0\), \(D>0\), and \(s\) is nonzero on every nonzero point of \(\ell\). Thus \(\beta\) vanishes identically on \(\ell\). This holds for both zero lines of \(\alpha\), so the two linear factors of \(\alpha\) divide \(\beta\). Since both forms have degree two,
\[
\beta=k\alpha
\]
for some real \(k>0\). Consequently \(E=k^2D\), and (6) becomes
\[
k(k-1)\alpha^3\equiv0.
\]
Therefore \(k=1\), so \(\beta=\alpha\) and \(B=A\).

It remains to treat the circular case \(\alpha=a s\). If \(\beta\) were noncircular, the preceding argument applied with \(A\) and \(B\) interchanged would force \(\alpha\) to be proportional to \(\beta\), a contradiction. Hence \(\beta=b s\) as well. On unit directions, (4) then reduces to
\[
\frac{L_A^2}{4}=\frac1a-r^2,
\qquad
\frac{L_B^2}{4}=\frac1b-r^2.
\]
Equality of the chord functions gives \(a=b\), and again \(A=B\).

This proves global injectivity of the tangent-chord data on origin-centered ellipses.

## Verification
The accompanying `verify.py` uses only the Python standard library and exact rational polynomial arithmetic. It reconstructs the cross-multiplied form of (5), verifies that its homogeneous degree-six form is exactly (6), and independently verifies the decisive proportional-case factorization
\[
P=k(k-1)\alpha^3.
\]
It also checks representative rational positive-definite matrices against the direct quadratic-root chord formula.

The finite examples are regression checks only. The universal theorem is established by the factor-divisibility proof above, not by enumeration or numerical sampling.

## Relationship to prior work
Barker and Larman formulated the general reconstruction problem in which one knows the section volumes of an outer convex body by all support hyperplanes of a fixed inner convex body. Their 2001 paper treats the unit-ball setting and gives partial results, but its published abstract leaves uniqueness as a conjecture.

Makai and Martini later proved local positive results for sufficiently small \(C^2\)-perturbations of the inner body. Their full text also records the planar theorem of Santaló that a convex body whose chords tangent to a centered disk all have one constant length must be a concentric circle. Thus part of the centered-ellipse family sufficiently close to the disk is already covered locally, and the constant-chord circle branch is classical. The theorem here is different: it gives global injectivity for arbitrary directional tangent-chord data throughout the entire centered-ellipse family, including arbitrarily eccentric ellipses compatible with containing the prescribed disk.

A 2023 survey restates the exact planar equal-tangent-chord question and says that the general problem remains unknown even near the unit ball without the extra regular perturbative hypotheses. A recent published research record proves global Barker–Larman rigidity for ellipsoids in dimensions \(n\ge3\), even without assuming a common center. Its stated theorem excludes dimension two, so it neither contains nor implies the planar theorem proved here; conversely, the centered planar result does not imply the higher-dimensional theorem.

Targeted searches under tangent-chord, sectional-volume, centered-ellipse, quadratic-form, and Barker–Larman terminology did not locate a previous global planar theorem for two arbitrary centered ellipses.

## Limitations
The center of the outer ellipse is assumed to coincide with the center of the prescribed disk. The proof does not reconstruct an arbitrarily translated ellipse, and it does not settle the general planar Barker–Larman problem for nonquadratic convex bodies.

The original 2001 Barker–Larman full text was not available in the lawful public sources inspected here, so no whole-document absence claim is made about that paper. The comparison instead uses its published abstract, the detailed 2016 full-text survey of its partial results, and the 2023 full-text statement of the still-open planar problem. An unindexed older special-case result for centered ellipses remains a residual bibliographic risk.

## References
1. J. A. Barker and D. G. Larman, *Determination of convex bodies by certain sets of sectional volumes*, Discrete Mathematics 241 (2001), 79–96. DOI: 10.1016/S0012-365X(01)00111-X.
2. E. Makai, Jr. and H. Martini, *Unique local determination of convex bodies*, arXiv:1602.00959v1, 2 February 2016; Acta Mathematica Hungarica 150 (2016), 176–193. DOI: 10.1007/s10474-016-0640-z.
3. M. Angeles Alfonseca, F. Nazarov, D. Ryabogin, and V. Yaskin, *Analysis and geometry near the unit ball: proofs, counterexamples and open questions*, in *Harmonic Analysis and Convexity*, De Gruyter, 2023, 445–468. DOI: 10.1515/9783110775389-011.
4. *Global Barker–Larman rigidity for ellipsoids*, public research record 75abc96cf1f6, 4 October 2026.
