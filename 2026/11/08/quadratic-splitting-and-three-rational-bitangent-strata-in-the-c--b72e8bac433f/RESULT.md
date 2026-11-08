# Quadratic splitting and three rational-bitangent strata in the Ciani quartic pencil

## Finding
Let \(q\) be any odd prime power and let \(\lambda\in\mathbb F_q\setminus\{-2,-1,2\}\). The smooth genus-three plane quartic
\[
C_\lambda:\quad X^4+Y^4+Z^4+\lambda(X^2Y^2+X^2Z^2+Y^2Z^2)=0
\]
has exactly \(28\) geometric bitangent lines (hyperflex lines included), and **every one is defined over \(\mathbb F_{q^2}\)**. Write \(\chi\) for the quadratic character of \(\mathbb F_q\); its arguments below are nonzero. The exact number of \(\mathbb F_q\)-rational geometric bitangent lines is
\[
B_q(\lambda)=4+12\,\mathbf 1_{\chi(-\lambda-1)=1}
 +12\,\mathbf 1_{\chi(-\lambda-1)=\chi(\lambda+2)=1}.
\]
Thus the only possible counts are \(4\), \(16\), and \(28\). The \(q\)-Frobenius on the set of geometric bitangents has cycle type, respectively, \(1^4 2^{12}\), \(1^{16}2^6\), or \(1^{28}\). More generally, all \(28\) bitangents are defined over \(\mathbb F_{q^n}\) when \(n\) is even, and exactly \(B_q(\lambda)\) when \(n\) is odd.

The criterion for **complete splitting over the ground field** is precisely
\[
\chi(-\lambda-1)=\chi(\lambda+2)=1.
\]

## Assumptions and scope
Throughout, \(\operatorname{char}(\mathbb F_q)\ne2\), and a geometric bitangent means a projective line whose intersection divisor with the quartic is twice an effective degree-two divisor over an algebraic closure; its two tangency points are allowed to coincide. A line is rational when its homogeneous coefficients can be scaled into \(\mathbb F_q\), independently of the field of its tangency points. No assertion is made for characteristic two or for the singular parameters \(\lambda\in\{-2,-1,2\}\).

The smoothness exclusion is exact. The partial derivatives are \(2X(2X^2+\lambda(Y^2+Z^2))\) and their two cyclic permutations. At a singular point with two nonzero coordinates, the resulting linear equations in their squares force \(\lambda^2=4\). At a singular point with three nonzero coordinates, their coefficient matrix has determinant \((2-\lambda)^2(2+2\lambda)\), forcing \(\lambda=2\) or \(\lambda=-1\). One nonzero coordinate cannot give a singular projective point. Hence the prescribed parameters are smooth over the algebraic closure.

## Proof
**Construction of all geometric bitangents.** Work over an algebraic closure of the coefficient field. There are three disjoint families of lines.

1. Four permanently defined lines arise by taking \(X+\epsilon Y+\delta Z=0\) for \(\epsilon,\delta\in\{\pm1\}\). On such a line the quartic restricts to \((\lambda+2)(Y^2+\epsilon\delta YZ+Z^2)^2\).

2. Twelve lines arise from the three distinguished-coordinate choices of \(X+t(Y+\epsilon Z)=0\), for \(\epsilon\in\{\pm1\}\) and \(t^2=-1/(\lambda+1)\). On the line \(X=-t(Y+Z)\), direct expansion gives
\[
F_\lambda\bigl(-t(Y+Z),Y,Z\bigr)=
\frac{\lambda+2}{(\lambda+1)^2}
\bigl(Y^2-(\lambda-1)YZ+Z^2\bigr)^2.
\]
Replacing \(Z\) by \(-Z\) gives the other sign. The twelve lines are distinct since \(t\ne0\) and \(t^2\ne1\).

3. Twelve coordinate-sparse lines arise from the three coordinate-pair choices of \(X+tY=0\), with \(t\) ranging over the four distinct roots of
\[
R_\lambda(T)=(\lambda+2)(T^4+1)+2\lambda T^2.
\]
Indeed, \(R_\lambda(t)=0\) implies
\[
F_\lambda(-tY,Y,Z)=
\left(Z^2+\frac\lambda2(1+t^2)Y^2\right)^2,
\]
because
\[
\lambda^2(1+t^2)^2-4(1+t^4+\lambda t^2)
=(\lambda-2)R_\lambda(t).
\]
The roots are \(t,-t,t^{-1},-t^{-1}\); they are all distinct because \(R_\lambda(0)=\lambda+2\), \(R_\lambda(\pm1)=4(\lambda+1)\), and \(R_\lambda(T)\equiv4\pmod{T^2+1}\).

The three line families are mutually disjoint: the third has a zero coefficient, the first and second do not, and a line in the first cannot lie in the second without \(t^2=1\). Thus they give \(4+12+12=28\) distinct geometric bitangents. A smooth plane quartic in characteristic different from two has exactly \(28\) distinct geometric bitangents, by the classical odd-theta-characteristic count. Accordingly these are **all** of them, not just a sample.

**Rationality of the second family.** Since the singled-out coefficient is \(1\), a line in this family is \(\mathbb F_q\)-rational exactly when \(t\in\mathbb F_q\). The two roots of \(t^2=-1/(\lambda+1)\) lie in \(\mathbb F_q\) exactly when \(\chi(-\lambda-1)=1\). In that case all twelve lines occur; otherwise none do.

**Rationality of the third family.** For a root \(t\ne0\) of \(R_\lambda\), division by \(t^2\) yields
\[
(t+t^{-1})^2=\frac4{\lambda+2},\qquad
(t-t^{-1})^2=\frac{-4(\lambda+1)}{\lambda+2}.
\]
If \(t\in\mathbb F_q\), both \(\lambda+2\) and \(-\lambda-1\) must be nonzero squares. Conversely, if both are squares, choose \(a,b\in\mathbb F_q\) with \(a^2=4/(\lambda+2)\) and \(b^2=-4(\lambda+1)/(\lambda+2)\). Because \(a^2-b^2=4\), the element \(t=(a+b)/2\) is nonzero, has inverse \((a-b)/2\), and satisfies \(R_\lambda(t)=0\). All four roots lie in \(\mathbb F_q\) by the reciprocal symmetry. Thus this family contributes either twelve or zero rational lines, with the stated criterion.

**Extension fields and Frobenius.** Every nonzero element of \(\mathbb F_q\) becomes a square in \(\mathbb F_{q^2}\). Applying the just-proved criteria over the quadratic extension shows that all twenty-eight lines are defined there. Frobenius consequently has order dividing two on this finite set. Its fixed-point count is the displayed formula, giving precisely the three stated cycle types and all extension-degree counts. This completes the proof.

## Verification
The standalone file `verify_symbolic.py` checks the square identities, the reduction by \(R_\lambda\), the required noncollision identities, and the Jacobian-matrix determinant over rational polynomial rings using exact SymPy arithmetic. The independent file `verify_prime_fields.py` enumerates every line in \(\mathbb P^2(\mathbb F_p)\), restricts the quartic, and tests whether the binary quartic is a scalar multiple of a square for every smooth parameter over twelve prime fields \(p=3,5,7,11,13,17,19,23,29,31,37,41\). Its \(201\) cases all satisfy the predicted count. The independent file `verify_quadratic_fields.py` performs analogous exhaustive checks for all eligible parameters over \(\mathbb F_9\) and \(\mathbb F_{25}\) (\(29\) cases). These computations supplement, but do not replace, the algebraic proof for all odd prime powers.

Run all three files with Python 3; `verify_symbolic.py` additionally requires SymPy (tested with version 1.14.0). The expected terminal markers are `VERIFY_SYMBOLIC_OK`, `VERIFY_PRIME_FIELDS_OK`, and `VERIFY_QUADRATIC_FIELDS_OK`.

## Relationship to prior work
The Ciani pencil and its four common bitangents were described classically, including by Edge [3]. Janasz–Pokora–Zieliński [1] study its complex bitangent arrangement, involutions, and quadruple intersections, without an arithmetic square-class classification over finite fields. Bethea–Brazelton [2] identify the \(S_4\)-set structure \(4+12+12\) of the geometric bitangents of the generic complex octahedral member. Their result explains the sizes of the three families, but does not state or imply the explicit two-character rationality criterion, since it does not specify the finite-field Frobenius action on either twelve-element orbit. Their supplementary tables give numerical bitangents for selected complex curves, not a family-wide finite-field criterion. Betten–Kaplan–Karaoglu [4] provide finite-field classifications and tables for certain individual small fields; these do not supply a formula uniform in all odd prime powers and parameters. The present theorem is an exact arithmetic splitting refinement, not a new count of geometric bitangents or a new complex automorphism classification.

## Limitations
The curve may have extra geometric automorphisms at special smooth parameters, but the three-family proof still applies. Rational bitangent lines are counted whether or not their tangency points are individually rational. The theorem gives no formula for rational tangency points, no description in characteristic two, and no assertion for the three singular parameters. Existing historical formulas for Ciani quartics could conceivably be specialized to recover the square-character criterion; historical priority beyond the inspected sources is not independently certified.

## References
[1] M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, first posted August 31, 2023, arXiv:2308.16514, §3, https://arxiv.org/abs/2308.16514.

[2] C. Bethea, T. Brazelton, *Bitangents to symmetric quartics*, first posted October 11, 2024, arXiv:2410.09242, Theorem 1.1 and §4.4, https://arxiv.org/abs/2410.09242. Supplementary selected numerical examples: https://tbrazel.github.io/supplementary/lines.pdf.

[3] W. L. Edge, *A plane quartic curve with twelve undulations*, Edinburgh Mathematical Notes 35 (1945), 10–13, DOI:10.1017/S0950184300000197.

[4] A. Betten, N. Kaplan, F. Karaoglu, *Classification of Quartic Curves Over Small Finite Fields*, October 29, 2021, https://www.math.colostate.edu/~betten/mathdata/quartic_curves.html.
