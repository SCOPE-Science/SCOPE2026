# Exact three-sheet inverse geometry of an absolute-value planar map

## Finding

Consider the planar map of Zhou, Li, Lu, Lei and Zhao (2021) in its dynamically studied negative-coupling sign regime:
\[
 F(x,y)=\bigl(x(a-k|y|),\,-h x-\tfrac54y\bigr),
 \qquad a,k,h>0.
\]
For an observed output \((u,v)\), let \(N(u,v)\) denote the number of distinct real one-step predecessors \((x,y)\) satisfying \(F(x,y)=(u,v)\). Put \(d=5/4\) and
\[
 K=\frac{da}{k},\qquad B(v)=-\frac{av}{h},\qquad
 L(v)=B(v)-\frac{(da-kv)^2}{4dkh},\qquad
 U(v)=B(v)+\frac{(da+kv)^2}{4dkh}.
\]
The map is onto and **every output has exactly one, two or three predecessors, never more**. The exact three-predecessor set is
\[
 \boxed{\begin{aligned}
 &v\le -K:\quad L(v)<u<B(v),\\
 &-K<v<K:\quad L(v)<u<U(v),\\
 &v\ge K:\quad B(v)<u<U(v).
 \end{aligned}}
\]
Every point on the two boundaries of each displayed nonempty interval has exactly two distinct predecessors; every other output has exactly one. In particular, for \(-K<v<K\), the three-sheet region *crosses the switching-image line* \(u=B(v)\); on that line the map has three **distinct** predecessors, with the crease predecessor generally nonsmooth (except at the origin). The origin has exactly the three regular predecessors
\[
 (x,y)=(0,0),\qquad
 (x,y)=\left(\frac{da}{kh},-\frac ak\right),\qquad
 (x,y)=\left(-\frac{da}{kh},\frac ak\right).
\]
The two smooth fold boundaries merge quadratically with the switching-image line at \(v=-K\) and \(v=K\): their vertical separations are exactly
\[
 B(v)-L(v)=\frac{k}{4dh}(K-v)^2,\qquad
 U(v)-B(v)=\frac{k}{4dh}(K+v)^2.
\]
At every regular output the signed inverse multiplicity is \(+1\): the three sheets have Jacobian orientations \(+,-,+\) in increasing predecessor \(y\)-order. This is a global backward-observation statement, not a claim about forward attraction or cryptographic safety.

## Assumptions and scope

All three parameters \(a,k,h\) are strictly positive and initial states and output targets range over the full real plane. The published map has coefficients \(b=-k<0\) and \(c=-h<0\), so it includes the negative-feedback regime emphasized in the original dynamical examples. A predecessor is counted once even if it is on a fold, on the nonsmooth line \(y=0\), or on the boundary between sheets. Here “regular” means that \(F\) is differentiable there and its Jacobian is nonsingular. The exact counts on boundaries are part of the claim; a two-sided derivative is not asserted at general points of \(y=0\).

## Proof

**1. Scalar inverse reduction.** Given \(v=-hx-dy\), necessarily \(x=-(v+dy)/h\). Substitution into the first output coordinate gives a continuous scalar function \(u=g_v(y)\), with
\[
 g_v(y)=\begin{cases}
 \displaystyle\frac{-av+(kv-da)y+dk y^2}{h},&y\ge0,\\
 \displaystyle\frac{-av-(da+kv)y-dk y^2}{h},&y\le0.
 \end{cases}
\]
Both branches agree at \(y=0\) with common value \(B(v)=-av/h\). Since \(g_v(y)\to-\infty\) as \(y\to-\infty\) and \(g_v(y)\to+\infty\) as \(y\to+\infty\), every output has at least one predecessor. Every root \(y\) produces exactly one plane predecessor using the displayed value of \(x\); there can be no extra plane solutions.

**2. Entire fold geometry and exact counts.** On the positive half-line the quadratic is strictly convex. Its vertex lies at
\[
 y_+=\frac{da-kv}{2dk}>0\quad\Longleftrightarrow\quad v<K,
\]
with minimum \(g_v(y_+)=L(v)\). If \(v\ge K\), that branch increases on \([0,\infty)\), starting at \(B(v)\). On the negative half-line the quadratic is strictly concave. Its vertex lies at
\[
 y_-=-\frac{da+kv}{2dk}<0\quad\Longleftrightarrow\quad v>-K,
\]
with maximum \(g_v(y_-)=U(v)\). If \(v\le-K\), that branch increases on \(( -\infty,0]\), ending at \(B(v)\).

When \(v<-K\), the left branch is one-to-one and the right branch has two inverse values exactly when \(L(v)<u<B(v)\). Its two right-side preimages coexist with one left-side preimage, giving three. The two transition levels have two distinct preimages each. The analogous right-hand outer region \(v>K\) has three preimages exactly when \(B(v)<u<U(v)\). When \(-K<v<K\), both half-lines have an interior turning point: below \(B(v)\) there are two right-side and one left-side roots, above \(B(v)\) two left-side and one right-side roots, and at \(u=B(v)\) there are the root \(y=0\) and exactly two additional nonzero roots (one on each side). Thus precisely \(L(v)<u<U(v)\) yields three preimages. At the exact threshold \(v=\pm K\), the corresponding vertex coalesces with \(y=0\), and the strict intervals in the theorem still give the correct counts, including exactly two on their endpoints. These cases exhaust all targets and show that no four-sheet region can occur.

The two explicit quadratic differences between the vertex value and \(B(v)\) are the displayed fold–switching separation identities. Their strict positive signs away from \(v=\pm K\) prove the claimed quadratic tangency and show that the three-sheet region is nonempty for every parameter choice.

**3. The origin and orientations.** Set \(u=v=0\) in the two branch quadratics. Their roots are \(y=0\) and \(y=\pm a/k\), with \(x=-dy/h\), giving exactly the three displayed real predecessors. At \(y=0,x=0\), the derivative is the matrix with diagonal entries \(a,-d\), hence determinant \(-ad<0\); differentiability follows from \(x|y|=o(\sqrt{x^2+y^2})\) at the origin. At each nonzero predecessor, direct evaluation of the smooth-branch Jacobian gives determinant \(+ad>0\); all three are regular.

For \(y\ne0\), direct Jacobian differentiation, together with \(x=-(v+dy)/h\), yields
\[
 \det DF(x,y)=h\,g_v'(y).
\]
At three distinct regular inverse roots, the scalar graph crosses the target horizontal line with slope signs \(+,-,+\) in increasing \(y\)-order, so their Jacobian determinant signs are \(+,-,+\). At a regular one-root output the unique slope is positive and its determinant is positive. Thus the signed number of regular preimages is always \(+1\). This orientation statement does not assign a determinant to a nonsmooth crease point.

## Verification

The companion `check.py` implements the exact piecewise quadratic root equations with rational parameters, independently substitutes each reconstructed precursor into both original map coordinates, checks representative one-, two- and three-sheet targets including all fold endpoints, and checks Jacobian determinants at the three origin predecessors. Execute `python3 check.py` using only Python's standard library; expected message `FOLD_CREASE_VERIFY_OK`. This is regression evidence; the proof above establishes the continuum and boundary cases without extrapolating finite tests.

## Relationship to prior work

Zhou et al. (2021) introduced this piecewise-smooth planar map, computed its fixed points and discussed amplitude control, Lyapunov exponents and coexisting attractors. The observed output's exact number of distinct antecedent states, its global fold–switching sheets, their quadratic merger and the signed inverse count are separate questions not supplied by the inspected original article. Results about forward escape and invariant measures in this same family do not imply these one-step inverse multiplicities: in particular, forward-diverging dynamics can still be globally three-to-one on a nonempty open output set. Related published exact inverse-count calculations for other sine, quadratic and cubic maps concern different defining equations and cannot be substituted for this map's root analysis.

## Limitations

The claim concerns one backward step on the full real plane with \(a,k,h>0\), not forward attractors or symbolic dynamics; other coefficient-sign sectors are outside the theorem. Singular fold boundaries and nonsmooth switching points are counted as distinct solutions but no differentiable inverse theorem is claimed there. A possible equivalent treatment outside the inspected primary literature and mathematical indexes remains a novelty risk. The fact that three states can share one output is not, by itself, a measure of predictability or information security.

## References

1. X. Zhou, C. Li, X. Lu, T. Lei and Y. Zhao, *A 2D Hyperchaotic Map: Amplitude Control, Coexisting Symmetrical Attractors and Circuit Implementation*, Symmetry **13** (2021), 1047, publicly published 10 June 2021, https://doi.org/10.3390/sym13061047 . Source equations (1)–(5) and Sections 2–4.
2. M. Hénon, *A two-dimensional mapping with a strange attractor*, Communications in Mathematical Physics **50** (1976), 69–77, https://doi.org/10.1007/BF01608556 . General context for the contrast between noninvertible and invertible plane maps, not a source of the present formula.
