# Complete exterior tangent-contact spectrum of a tangent-filling plane curve

## Finding

Let \(q\) be any prime power of characteristic \(p>3\), and let \(C_q\subset\mathbb P^2_{\mathbb F_q}\) be the integral plane curve
\[
X^{q-1}+Y^{q-1}+Z^{q-1}-3(X+Y+Z)^{q-1}=0.
\]
For a rational point \(P\) outside the smooth rational locus of \(C_q\), define the **tangent-contact multiplicity**
\[
m(P)=\#\{Q\in C_q^{\mathrm{sm}}(\mathbb F_q):P\in T_QC_q\}.
\]
Here different smooth contact points are counted separately even if their tangent lines coincide. Put \(e=\chi_q(-3)\in\{-1,1\}\), where \(\chi_q\) is the quadratic character of \(\mathbb F_q\). The exterior consists of the ordinary double point \(P_0=[1:1:1]\) and the union \(B\) of the four rational lines \(XYZ(X+Y+Z)=0\). Its complete multiplicity distribution is:

| Point stratum | Tangent-contact multiplicity | Number of rational points |
|---|---|---|
| The singular point \(P_0\) | \(q-6-e\) | \(1\) |
| \(B\) | \(q-5\) | \(2(q-6-e)\) |
| \(B\) | \(q-4\) | \(4(1+e)\) |
| \(B\) | \(q-3\) | \(2q+6-2e\) |

Zero-frequency rows are omitted when interpreting the table. Its three boundary frequencies sum to \(4q-2\), and the exterior has \(4q-1\) points. In particular the only rational point not covered by a tangent at a smooth rational point is \(P_0\) for \(q\in\{5,7\}\); all rational points are covered when \(q\ge11\) and \(p>3\). The exact total number of exterior contact incidences is
\[
\sum_{P\notin C_q^{\mathrm{sm}}(\mathbb F_q)}m(P)=4q^2-17q+20-e.
\]

## Assumptions and scope

All tangent lines are taken at *smooth rational contact points* of the specified plane model. By the point classification and singular-locus theorem of Asgarli and Ghioca [1],
\[
C_q^{\mathrm{sm}}(\mathbb F_q)
=\{[x:y:z]:xyz(x+y+z)\ne0\}\setminus\{[1:1:1]\},
\]
and \(P_0\) is the unique geometric singularity, an ordinary node. There are \((q-1)(q-2)\) smooth rational points. The four lines forming \(B\) are in general position because \(p>3\), so \(B\) has six vertices and \(4(q-2)\) other rational points. There is no assumption that distinct rational contact points determine distinct tangent lines. No claims are made in characteristics two or three or about geometric tangencies at non-rational contact points.

## Proof

Write \(s=x+y+z\). Every smooth rational contact point can be uniquely scaled so that \(s=1\). Differentiating the homogeneous equation, and using \(q-1=-1\) in \(\mathbb F_q\), shows that the tangent has coefficient vector
\[
\bigl(x^{-1}-3,\ y^{-1}-3,\ z^{-1}-3\bigr).
\]
Thus for \(P=[a:b:c]\) the condition that this tangent pass through \(P\) is
\[
\frac a x+\frac b y+\frac c z=3(a+b+c),
\qquad x+y+z=1,\quad xyz\ne0,\quad[x:y:z]\ne P_0. \tag{1}
\]

**Vertices of the four-line boundary.** Up to permutation of the three coordinates, the six vertices have types \([1:0:0]\) and \([0:1:-1]\). In the first case (1) gives \(x=1/3\), with \(y+z=2/3\). Among the \(q\) choices of \(y\), omit the two choices making \(y\) or \(z\) zero and the one giving \(P_0\), leaving \(q-3\). In the second case (1) gives \(y=z\), and \(x+2y=1\). The analogous three exclusions again leave \(q-3\).

**Nonvertex points on a coordinate line.** By permutation, write \(P=[0:t:1-t]\) with \(t\notin\{0,1\}\). Equation (1) is \(t/y+(1-t)/z=3\). Set
\[
U=3y-t,\qquad V=3z-(1-t).
\]
Then \(UV=t(1-t)\ne0\), and conversely each \(U\in\mathbb F_q^*\) determines \(V\) and hence a point with \(x=1-y-z\). From the \(q-1\) values of \(U\), remove \(U=-t\) (both \(y=0\) and \(z=0\)), remove the \(1+\chi_q(t^2-t+1)\) roots of \(U^2-2U+t(1-t)=0\) (giving \(x=0\)), and remove \(U=1-t\) (giving \(P_0\)). These exclusions are disjoint for \(p>3\). Thus
\[
m([0:t:1-t])=q-4-\chi_q(t^2-t+1). \tag{2}
\]

**Nonvertex points on the fourth line.** Write \(P=[a:b:c]\) with \(a+b+c=0\) and \(abc\ne0\). Equation (1), in homogeneous contact coordinates, becomes the nonsingular conic
\[
a yz+b xz+c xy=0.
\]
Its \(q+1\) rational points include the three coordinate vertices. Its intersection with the line \(x+y+z=0\) has \(1+\chi_q(a^2+ab+b^2)\) rational points: substituting \(z=-x-y\) gives a binary quadratic with discriminant \(4(a^2+ab+b^2)\). All these discarded points are distinct from the coordinate vertices. The point \(P_0\) also lies on this conic, distinct from the preceding exclusions. Therefore
\[
m([a:b:c])=q-4-\chi_q(a^2+ab+b^2).
\]
After scaling \(b=1\) and writing \(a=-t\), the parameter \(t\) ranges through \(\mathbb F_q\setminus\{0,1\}\) and the quadratic becomes \(t^2-t+1\). Thus (2) governs the nonvertices on **each** of the four boundary lines.

**Counting the boundary strata.** The discriminant of \(D(t)=t^2-t+1\) is \(-3\ne0\), so exactly \(1+e\) elements of \(\mathbb F_q\) are roots. Moreover
\[
\sum_{t\in\mathbb F_q}\chi_q(D(t))=-1.
\]
Indeed the conic \(v^2=D(t)\) is equivalent to \((v-t+1/2)(v+t-1/2)=3/4\), which has precisely \(q-1\) affine rational solutions. Since \(D(0)=D(1)=1\), on the \(q-2\) admissible parameters \(t\notin\{0,1\}\), the counts of quadratic-character values \(+1,0,-1\) are respectively
\[
\frac{q-6-e}{2},\qquad1+e,\qquad\frac{q-e}{2}.
\]
Multiply these frequencies by four and add the six vertices to the \(-1\)-character case to obtain the three boundary rows of the table.

**The singular point.** With \(P=P_0\), clearing denominators in (1) gives the projective cubic
\[
K(x,y,z)=(x+y+z)(xy+yz+zx)-9xyz=0.
\]
In the affine chart \(z=1\), put \(u=x-1\), \(v=y-1\). Its equation is
\[
K=u^2v+uv^2+2(u^2-uv+v^2).
\]
Projecting from its rational double point \((u,v)=(0,0)\), lines of slope \(t=v/u\) meet the cubic, away from the double point, at
\[
u=-\frac{2(t^2-t+1)}{t(t+1)}.
\]
The slopes \(t=0,-1,\infty\) produce distinct third intersections on \(z=0\), rather than finite values of \(u\). The only slopes with *no* third point distinct from the double point are the \(1+e\) roots of \(t^2-t+1\). Every rational cubic point other than the node determines a unique rational slope. Consequently \(K(\mathbb F_q)\) has \(q+1-e\) points. Of these, exactly six lie on \(xyz(x+y+z)=0\): the three coordinate vertices and the three intersections of \(x+y+z=0\) with a coordinate line. The node itself is another excluded point. Hence
\[
m(P_0)=(q+1-e)-6-1=q-6-e.
\]
The formula for total exterior contact incidences follows by summing the four rows, and the coverage assertions follow because every smooth rational point lies on its own tangent.

## Verification

The standalone `verify_tangent.py` implements prime fields and nonsplit quadratic extensions with explicit arithmetic tables. It enumerates every rational projective point, every smooth rational contact point, and every tangent incidence on the entire exterior, independently of the character formula. It checks the pointwise formula and the complete multiplicity histogram for \(q=5,7,11,13,17,19,23,29,31,25,49,121\). The full output ends with `ALL_EXTERIOR_TANGENT_CONTACT_TESTS_PASSED`. These finite checks are corroborative; the proof above establishes the formulas for all prime powers of characteristic greater than three.

## Relationship to prior work

Asgarli and Ghioca [1], in Theorem 1.3 and Sections 3.1–3.4, supply the curve, its rational smooth-point characterization, its unique singularity, and qualitative tangent-filling for \(q\ge11\). Their Section 3.4 uses a conic to prove the existence of a tangent through \(P_0\), but does not give the full pointwise exterior incidence formula or its uniform character histogram.

The prior *Exact rational bitangent counts for a tangent-filling plane curve* [2] determines how many **distinct tangent lines** have one or two smooth rational contact points (the fibres of the rational Gauss map). It does not classify, for each **exterior primal point**, how many rational smooth contact points have a tangent passing through it; neither its line-fibre cardinalities nor its total number of distinct tangents determines this point-side distribution. The earlier *An eighteen-tangent projective triangle on the first Asgarli–Ghioca curve* [3] gives a covering subset and a distinct-tangent-line histogram only at \(q=11\), not the asserted all-field contact incidence distribution. The study [4] of the associated degree-two del Pezzo tangent map concerns its branch and singular geometry rather than the point-side contact spectrum. These are separate arithmetic incidence questions.

## Limitations

The theorem counts contact *points*, not necessarily distinct rational tangent *lines* passing through an exterior point; a bitangent rational line can contribute twice. It treats the exterior of the smooth rational locus only, not the incidence histogram on all smooth rational points. It does not determine the curve's geometric dual zeta function or tangent intersections over non-rational contact fields. Priority is subject to possible unindexed equivalent computations, and independent mathematical validation has not been performed.

## References

1. Shamil Asgarli and Dragos Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420v1, first publicly submitted 2023-02-26; https://arxiv.org/html/2302.13420v2 .
2. *Exact rational bitangent counts for a tangent-filling plane curve*, public research record; https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-rational-bitangent-counts-for-a-tangent-filling-plane-curv--51fb2a9a947e/RESULT.md .
3. *An eighteen-tangent projective triangle on the first Asgarli–Ghioca curve*, public research record; https://github.com/published-finding corpus/2026/blob/main/2026/10/13/SCOPE-an-eighteen-tangent-projective-triangle-on-the-first-asgarli-ghi--6ed9d400dac8/RESULT.md .
4. *The four-nodal double plane behind the tangent map of the Asgarli–Ghioca curve*, public research record; https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-the-four-nodal-double-plane-behind-the-tangent-map-of-the-asgarl--7693cabfbd09/RESULT.md .
