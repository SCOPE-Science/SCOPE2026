# Rational nodes and cusps in a plane-filling pencil

## Finding
Let \(q\) be any odd prime power and \(k\in\mathbf F_q\). Consider the degree-\(q+3\) plane-filling curve
\[
C_k:\quad X^2(X^qY-XY^q)+Y^2(Y^qZ-YZ^q)+(Z^2+kX^2)(Z^qX-ZX^q)=0
\]
over \(\mathbf F_q\). Every \(\mathbf F_q\)-rational singular point is uniquely of the form
\[
P_t=[t:1:t^3],\qquad t\in\mathbf F_q^\times,\qquad t^7+kt^3-1=0.
\]
Every such point is geometrically an **ordinary node** if \(4t^7\ne1\), and an **ordinary cusp** (analytically \(v^2+u^3=0\)) if \(4t^7=1\). For a node, the two geometric tangent branches are individually rational over \(\mathbf F_q\) precisely when \(1-4t^7\) is a nonzero square in \(\mathbf F_q\); otherwise the two branches are conjugate over the quadratic extension.

For the distinguished member \(k=0\), there are exactly \(\gcd(7,q-1)\) rational singular points. They are all cusps in characteristic three and all nodes in every other odd characteristic. In particular, \(C_0\) has seven rational ordinary cusps when \(q=3^{6m}\) with \(m\ge1\), and seven rational nodes when \(q\equiv1\pmod7\) and the characteristic is not three. In the latter case the nodes are split exactly when \(-3\) is a square in \(\mathbf F_q\).

The complete cusp-containing parameter set can be read off arithmetically: put \(g=\gcd(7,q-1)\). If \(4^{-1}\) is not a seventh power in \(\mathbf F_q^\times\), there are no rational cusps. Otherwise the equation \(t^7=4^{-1}\) has exactly \(g\) solutions. In characteristic different from three these give \(g\) **distinct** parameters \(k=3/(4t^3)\), each bearing exactly one rational cusp; in characteristic three they all occur on \(k=0\).

## Assumptions and scope
The base field is a finite field of odd cardinality \(q=p^e\), and all point counts and cusp-containing parameters in the theorem refer to \(\mathbf F_q\)-rational points and parameters. Node/cusp descriptions refer to the completed geometric local curve germ after extension to an algebraic closure. The assertion makes **no claim** that the listed rational points exhaust the singular locus over the algebraic closure, and does not settle the geometric smoothness conjecture for the pencil. No irreducibility or global normalization hypothesis is needed for the local conclusions.

## Proof
Because \(a^q=a\) for \(a\in\mathbf F_q\), every rational projective point lies on \(C_k\). At a rational point the homogeneous partial derivatives of the displayed polynomial are
\[
F_X=-X^2Y+Z^3+kX^2Z,\quad
F_Y=X^3-Y^2Z,\quad
F_Z=Y^3-Z^2X-kX^3.
\]
These equations hold in every odd characteristic, including characteristic three. If any of \(X,Y,Z\) vanishes and all derivatives vanish, then all coordinates vanish, impossible in projective space. Thus put \(Y=1\); the middle equation gives \(Z=X^3\). The last equation is \(1-X^7-kX^3=0\), and the first equation then vanishes automatically. This proves the complete rational singular-point parametrization, with \(t=X\ne0\).

Use affine coordinates \(Y=1\) near \(P_t\), writing \(X=t+u\), \(Z=t^3+v\). Frobenius powers change only in degree \(q\) in the increments. Since \(q\ge3\), the quadratic Taylor part is obtained by replacing \(X^q\) and \(Z^q\) by \(t\) and \(t^3\). Specifically, set
\[
h(X,Z)=tX^2-X^3+Z-t^3+(Z^2+kX^2)(t^3X-tZ).
\]
Using \(k=(1-t^7)/t^3\), its Hessian evaluated at \((t,t^3)\) is
\[
H_t=\begin{pmatrix}
-4t^8&2(2t^7-1)/t\\[2pt]
2(2t^7-1)/t&-4t^4
\end{pmatrix},\qquad
\det H_t=\frac{4(4t^7-1)}{t^2}.
\]
Thus the quadratic tangent cone is nondegenerate exactly when \(4t^7\ne1\), proving the ordinary-node assertion. Its binary quadratic discriminant is
\[
\Delta_t=-\det H_t=\frac{4(1-4t^7)}{t^2}.
\]
As the field has odd characteristic, the two distinct tangent directions are individually rational precisely when \(1-4t^7\) is a square.

Suppose instead that \(4t^7=1\), so \(k=3/(4t^3)\). The nonzero quadratic part is the square \(-2t^4(v+t^2u)^2\). Hence the unique tangent direction is \(v=-t^2u\). For \(q\ge5\), all Frobenius-increment terms have order at least five, so the cubic coefficient on this tangent can be computed from \(h\):
\[
[u^3]h(t+u,t^3-t^2u)=\frac{4t^7+1}{2}=1.
\]
For the only remaining case \(q=3\), the equation \(4t^7=1\) forces \(t=1\) and \(k=0\). Direct substitution into the **full** affine equation gives
\[
F(1+u,1,1-u)=u^3+2u^5\quad\text{in }\mathbf F_3[u].
\]
Thus the cubic term along the unique tangent remains nonzero, even though the Frobenius terms can first contribute in degree three. In either case, the germ has a rank-one nonzero quadratic term and exact tangent-contact order three. By completing the square in the transverse coordinate and applying Weierstrass preparation (valid in odd characteristic), it is formally equivalent over the algebraic closure to \(v^2+u^3=0\), an ordinary cusp.

For \(k=0\), the rational singularity equation is \(t^7=1\). The cyclic group \(\mathbf F_q^\times\) contains exactly \(\gcd(7,q-1)\) seventh roots of unity. On these \(t\), the cusp test \(4t^7=1\) reduces to \(4=1\), equivalent to characteristic three. For other odd characteristics the node-splitting expression is \(1-4t^7=-3\). Since \(3\) has multiplicative order six modulo seven, \(7\mid(3^e-1)\) exactly when \(6\mid e\). This proves the distinguished arithmetic family statements.

Finally, the equation \(t^7=4^{-1}\) is solvable in a cyclic group of order \(q-1\) if and only if \(4^{-1}\) belongs to the seventh-power subgroup, and then has exactly \(g\) roots. For such a root the singularity equation forces \(k=3/(4t^3)\). If \(p\ne3\) and two of these parameters coincide, the ratio of the corresponding roots has both seventh and third power one, hence is one. If \(p=3\), the parameter is necessarily zero. These are all the rational cusp-containing members by the local classification.

## Verification
The companion \(\texttt{verify.py}\) proves the Hessian determinant and tangent cubic coefficient as exact rational-function identities in a symbolic parameter. It separately evaluates the complete characteristic-three, \(q=3\) local cubic expansion. It also enumerates every rational projective point and every parameter for the prime fields of orders \(3,5,7,11,29\), checking directly that the gradient-zero locus coincides with the parametrized set. These finite checks corroborate the algebraic proof but are **not** used as a substitute for its all-prime-power argument.

Replay with \(\texttt{python verify.py}\), with SymPy installed. Expected last line: \(\texttt{ALL_CHECKS_PASS}\).

## Relationship to prior work
Asgarli and Ghioca, *Plane-filling curves of small degree over finite fields* (arXiv:2307.03072v1, July 6, 2023), define exactly this pencil in equation (1). Their Theorem 1.2 determines when its members have rational singular points, and their Conjecture 1.5 addresses geometric smoothness. Their proof does not specify rational singularity analytic types, splitting of nodal branches, or the cusp-bearing parameter locus. The present theorem refines the singular **side** of their rational smoothness criterion; it neither re-proves a stronger result already present there nor resolves Conjecture 1.5. Asgarli and Ghioca, *Smoothness in pencils of hypersurfaces over finite fields* (arXiv:2203.07169v1), concerns existence and discriminant avoidance in general linear systems, not these local arithmetic classifications.

## Limitations
Only rational singularities are classified; nonrational singularities may occur. The curves are not asserted to be irreducible, and no global genus or normalization point count is deduced. The result is local and arithmetic, not a resolution of the open geometric smoothness conjecture. Originality checks covered the relevant accessible primary text and targeted published-record searches, not an exhaustive catalogue of all equivalent work.

## References
1. S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072v1 (first public version July 6, 2023), especially equation (1), Theorem 1.2, and Section 4. https://arxiv.org/pdf/2307.03072
2. S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169v1 (March 14, 2022), especially the discriminant discussion in Section 2. https://arxiv.org/pdf/2203.07169
