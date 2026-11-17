# Complete cubic-over-affine barycentric moduli of nonparallelogram trapezoids

## Finding
For every nonparallelogram convex trapezoid, all nonnegative generalized barycentric coordinate systems having one common strictly positive affine-linear denominator and polynomial numerators of total degree at most three form a **single closed projective interval**. The interval, its sharp positivity bounds, and every coordinate function admit explicit formulas.

Normalize the vertices by an invertible affine map to
\[
 v_1=(0,0),\qquad v_2=(a,0),\qquad
 v_3=(b,1),\qquad v_4=(0,1),\qquad a>b>0.
\]
Write \(k=a-b>0\) and \(L(y)=a-ky\). For any real pair \((A,B)\ne(0,0)\), define
\[
\begin{aligned}
q(x,y)&=(A+kB)L(y)+bBx,\\
p_1(x,y)&=(1-y)(L(y)-x)\left(A+kB+\frac{bB}{a}x\right),\\
p_2(x,y)&=\frac{x(1-y)}{a}\left(a(A+kB)+bB(x+ky)\right),\\
p_3(x,y)&=xy\left(A+B(x+ky)\right),\\
p_4(x,y)&=y(L(y)-x)\left(A+kB+Bx\right).
\end{aligned}
\]
Then the functions \(\alpha_i=p_i/q\) are well-defined, nonnegative generalized barycentric coordinates on the **entire closed** trapezoid if and only if
\[
\boxed{\quad A\ge0,\qquad A+(a+k)B\ge0,\qquad(A,B)\ne(0,0).\quad}
\]
Conversely **every** such system with a common strictly positive affine-linear denominator and numerator degrees at most three arises in this way, uniquely up to multiplication of \((A,B)\) by a positive scalar. Therefore the moduli space is exactly the projectivization of a pointed two-dimensional cone. Its two extreme rays are \((A,B)=(0,1)\) and \((A,B)=(a+k,-1)\). The unique system with numerator degree at most two occurs at \(B=0\) and is the Wachspress system. All other parameter classes have numerator degree exactly three, and all have reduced denominator degree exactly one.

## Assumptions and scope
A generalized barycentric coordinate system (GBC) for vertices \(v_1,\ldots,v_4\) consists of four functions \(\alpha_i\colon P\to[0,\infty)\) satisfying, for every \((x,y)\in P\),
\[
\sum_{i=1}^{4}\alpha_i(x,y)=1,\qquad
\sum_{i=1}^{4}v_i\alpha_i(x,y)=(x,y).
\]
Here \(P=\{(x,y):0\le y\le1,\ 0\le x\le L(y)\}\), with \(0<b<a\). All four numerators are real polynomials of total degree at most three; their common denominator is a real affine polynomial strictly positive on the closed polygon. The denominator is not assumed initially to be the Wachspress adjoint. A common positive scalar change of all numerator and denominator polynomials does not alter the coordinates. The theorem classifies these **functions**, not higher-degree representations or arbitrary higher-degree GBC systems. Every convex trapezoid with unequal base lengths is affinely equivalent to this model, and the polynomial degree bounds are affine invariant.

## Proof
**1. Boundary vanishing and the free numerator.** On an edge of a convex polygon, barycentric positivity and affine precision force the coordinates belonging to vertices outside that edge to vanish. For \(v_3=(b,1)\), its numerator therefore vanishes on the bottom edge \(y=0\) and the left edge \(x=0\). Since the common denominator is strictly positive and \(\deg p_3\le3\),
\[
p_3(x,y)=xy(A+Bx+Cy)
\]
for real \(A,B,C\). The vertex \(v_3\) needs positive weight at itself, so this polynomial is not identically zero.

**2. Solve the denominator by boundary interpolation.** Write \(q=d_0+d_1x+d_2y\). On the top edge \(y=1\), only \(v_3,v_4\) can have positive weights; hence \(p_3(x,1)/q(x,1)=x/b\). Comparing coefficients gives \(d_1=bB\). On the slanted edge \(x=L(y)\), only \(v_2,v_3\) can have positive weights; hence \(p_3(L(y),y)/q(L(y),y)=y\), or
\[
q(L(y),y)=L(y)\big(A+B L(y)+Cy\big).
\]
Because the left side is affine in \(y\), the coefficient \(-k(C-kB)\) of \(y^2\) on the right must vanish. Since \(k>0\), \(C=kB\), and then
\[
q(L(y),y)=L(y)(A+aB).
\]
Subtracting the already known term \(bB L(y)\) gives the unique affine polynomial
\[
q(x,y)=(A+kB)L(y)+bBx.
\]

**3. Affine precision forces every other numerator.** The three polynomial identities for normalization and affine precision read
\[
p_1+p_2+p_3+p_4=q,\qquad
ap_2+bp_3=xq,\qquad
p_3+p_4=yq.
\]
They force \(p_2=(xq-bp_3)/a\), \(p_4=yq-p_3\), and \(p_1=(1-y)q-p_2\). Direct factorization yields exactly the four displayed expressions. This proves algebraic exhaustiveness, without assuming the desired factorization in advance.

**4. The positivity cone is necessary and sufficient.** Necessity: at interior points arbitrarily near \((0,0)\), the sign of \(p_3/(xy)\) forces \(A\ge0\). At interior points approaching \((a,0)\), the sign of \(p_4/[y(L(y)-x)]\) forces \(A+(a+k)B\ge0\).

For sufficiency let these two inequalities hold, with \((A,B)\ne(0,0)\). If \(B\ge0\), then \(A+kB>0\) and all displayed bracket factors are nonnegative throughout \(P\), because \(x\ge0\) and \(x+ky\ge0\). If \(B<0\), the second inequality implies
\[
A+aB=\big(A+(a+k)B\big)-kB>0,\qquad
A+kB=\big(A+(a+k)B\big)-aB>0.
\]
Since \(0\le x\le a\), \(0\le x+ky\le a\), every bracket in \(p_1,p_2,p_3,p_4\) is again nonnegative. In both cases the four vertex values of the affine denominator are
\[
a(A+kB),\quad a(A+aB),\quad b(A+aB),\quad b(A+kB),
\]
which are strictly positive. Therefore \(q>0\) on the entire convex polygon. The identities in Step 3 prove GBC normalization and precision. Hence the inequalities are also sufficient, including both extreme rays.

**5. Parameter uniqueness and degree rigidity.** For a second pair \((A',B')\), with corresponding \(q'\), the following polynomial identity holds:
\[
\begin{aligned}
 &(A+B(x+ky))q'-(A'+B'(x+ky))q\\
 &\hspace{6mm}=k(1-y)(L(y)-x)(AB'-BA').
\end{aligned}
\]
In the polygon interior all factors except the projective determinant are nonzero. Equality of the rational coordinates \(\alpha_3\) implies \(AB'-BA'=0\). Since both denominators are strictly positive, the proportionality factor is positive. This proves that no projective classes are identified.

When \(B=0\), each numerator is quadratic and \(q=A L(y)\), giving the standard Wachspress coordinates. When \(B\ne0\), \(p_3\) has a nonzero cubic part. A constant denominator cannot occur in the displayed solution unless \(A=B=0\), since the coefficient of \(x\) in \(q\) is \(bB\), while \(k>0\) makes \(q\) nonconstant when \(B=0,A\ne0\). There is also no common linear factor to cancel. Indeed \(p_3=xyM\) with \(M=A+B(x+ky)\). Since \(q\) is strictly positive even on the edges \(x=0\) and \(y=0\), it cannot be proportional to \(x\) or \(y\). For \(B=0\), the remaining factor \(M=A\) is constant. For \(B
e0\), proportionality to \(M\) would require \(q=bM\) from the \(x\)-coefficients, but \(q-bM=k(A+aB)(1-y)
e0\), because the admissible cone implies \(A+aB>0\). Thus \(\gcd(q,p_3)=1\) and every listed system has reduced denominator degree one. The feasible cone is precisely the nonnegative span of \((0,1)\) and \((a+k,-1)\); dividing by positive scales gives a closed projective interval. This completes the classification.

## Verification
The included `verification.py` performs exact SymPy checks of the three affine-precision identities for arbitrary symbolic \(a,b,A,B\), reconstructs the unique parameter family from all boundary identities, verifies projective injectivity, and recovers the published concrete non-Wachspress example exactly. It also tests positivity and normalization on rational grids for four distinct trapezoids and several interior and endpoint cone parameters. The algebraic proof above, not the finite grids, establishes the theorem for all real \(a>b>0\) and all permitted parameter pairs. Run `python verification.py` with SymPy available.

## Relationship to prior work
Baumbach and Winter, *Rational barycentric coordinates and low degree adjoints* (arXiv:2611.02110v1; 2026-11-01), Theorem 1.1 and Sections 2–3, establish the basic theory, the uniqueness of minimum-numerator-degree Wachspress coordinates, and the obstruction to polynomial GBCs on nonparallelogram quadrilaterals. Their Appendix Example A.3 explicitly supplies **one** degree-three-numerator, degree-one-denominator non-Wachspress system on \((a,b)=(2,1)\). It is the ray \((A,B)=(0,2)\) in the formulas here. They explicitly identify determination of the space of intermediate-degree GBCs as an interesting problem in Section 3.3. The present theorem proves a complete sharp classification of that space **under the stated affine-denominator constraint**, for every nonparallelogram trapezoid. It does not claim the existence of cubic alternatives as novel, nor solve the unrestricted higher-degree problem.

The published polygon denominator-degree theorem *Wachspress denominators have minimum degree on every convex polygon* (2026-11-08) implies that the minimal denominator degree for these noncentrally symmetric trapezoids is one. It neither supplies the above one-dimensional moduli space nor the positivity cone and endpoint classification. Standard treatments of Wachspress and other generalized barycentric coordinates supply constructions, not the exact classification under this combined degree constraint.

## Limitations
The result assumes a nonparallelogram trapezoid with strict base inequality and a **common denominator affine polynomial positive on the closed polygon**. It does not classify coordinate systems whose numerators have degree at least four, or different denominators per vertex. It is an algebraic classification and does not assert superior conditioning, finite-element approximation rates, or a wider polygon classification. The known source example and minimum-denominator results are credited rather than treated as new. Historical priority for a complete equivalent classification remains provisional because differently named older interpolation formulations may exist.

## References
1. T. Baumbach and M. Winter, *Rational barycentric coordinates and low degree adjoints*, arXiv:2611.02110v1, first posted 2026-11-01. Particularly Sections 2.1–2.3, 3.3, and Appendix Example A.3. https://arxiv.org/html/2611.02110v1
2. *Wachspress denominators have minimum degree on every convex polygon*, published mathematical research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-wachspress-denominators-have-minimum-degree-on-every-convex-poly--7b4aad67706d
3. M. S. Floater, *Generalized barycentric coordinates and applications*, Acta Numerica **24** (2015), 161–214; background survey of standard constructions. https://doi.org/10.1017/S0962492914000129
4. J. Warren, *On the uniqueness of barycentric coordinates*, Contemporary Mathematics **334** (2003), 93–100; classical minimum numerator-degree rigidity, discussed in Reference 1.
