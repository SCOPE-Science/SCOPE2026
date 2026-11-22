# Two-step pedal rigidity of centered spatial parallelepipeds

## Finding

Let \(B=A[-1,1]^3\subset\mathbb R^3\), where \(A\in\operatorname{GL}_3(\mathbb R)\), and let \(\mathcal D\) take the convex hull of perpendicular feet from the origin onto the *supporting hyperplanes of all facets* of its argument. Then

\[
\boxed{\mathcal D^2(B)\text{ is a parallelepiped}\quad\Longleftrightarrow\quad A^\mathsf T A\text{ is diagonal}.}
\]

Thus orthogonal rectangular boxes are precisely the centered spatial parallelepipeds whose second pedal remains a parallelepiped. There is also an exact sum-of-squares certificate measuring the failure of this condition. Put \(q_i=A^{-\mathsf T}e_i\), \(\kappa_i=\|q_i\|^2\), and \(C=A\operatorname{diag}(\kappa_1,\kappa_2,\kappa_3)\). For
\[
\eta_1=(1,1,1),\quad\eta_2=(1,-1,-1),\quad
\eta_3=(-1,1,-1),\quad\eta_4=(-1,-1,1),
\]
set \(s_j=\|C\eta_j\|^2\) and \(\overline{s}=(s_1+s_2+s_3+s_4)/4\). Then
\[
\boxed{\sum_{j=1}^{4}(s_j-\overline{s})^2
=16\sum_{1\le i<j\le3}\kappa_i^2\kappa_j^2\langle Ae_i,Ae_j\rangle^2.}
\]
The expression vanishes exactly for rectangular boxes. It is a *certificate of orthogonality*, not a claimed metric lower bound for distance to a family of shapes.

## Assumptions and scope

All parallelepipeds are full-dimensional, centrally positioned at the projection point \(0\), and obtained as the linear image of the cube as written. All feet are taken on whole supporting planes, not necessarily in the relative interior of the corresponding facets. A "parallelepiped" means a three-dimensional affine image of a cube, not merely a combinatorially cubical polytope. The statement is for real, not only rational, matrices and requires no small-shear or generic-position assumption.

## Proof

Write \(q_i=A^{-\mathsf T}e_i\) and \(\kappa_i=\|q_i\|^2>0\). The six facet planes of \(B\) are \(\langle q_i,x\rangle=\pm1\). Their perpendicular feet from the origin are \(\pm q_i/\kappa_i\). Hence
\[
\mathcal D(B)=W\,\operatorname{conv}\{\pm e_1,\pm e_2,\pm e_3\},\qquad
W=A^{-\mathsf T}\operatorname{diag}(\kappa_1^{-1},\kappa_2^{-1},\kappa_3^{-1}).
\]
This is a full-dimensional cross-polytope. Its eight facets have supporting planes \(\langle W^{-\mathsf T}\varepsilon,x\rangle=1\), one for each \(\varepsilon\in\{-1,1\}^3\). Since \(W^{-\mathsf T}=C=A\operatorname{diag}(\kappa_1,\kappa_2,\kappa_3)\), their feet are
\[
 v_{\varepsilon}=\frac{C\varepsilon}{\|C\varepsilon\|^2},\qquad
\mathcal D^2(B)=\operatorname{conv}\{v_{\varepsilon}:\varepsilon\in\{-1,1\}^3\}.
\]
These eight feet are distinct, occur in four antipodal pairs and have nonzero lengths because \(C\) is invertible.

Choose the four \(\eta_j\) above, which sum to zero and have rank three. Write \(v_j=v_{\eta_j}=C\eta_j/s_j\). Then
\[
\sum_{j=1}^{4}s_jv_j=C\sum_{j=1}^{4}\eta_j=0.
\]
This is the unique linear dependence, up to a scalar, among \(v_1,\dots,v_4\).

Suppose \(\mathcal D^2(B)\) is a parallelepiped. It must have eight vertices, so every listed foot is a vertex. It is centrally symmetric about zero, and its four antipodal vertex pairs are exactly \(\{\pm v_j\}\). Every centrally symmetric parallelepiped has the following elementary body-diagonal relation: after selecting appropriate orientations of the four antipodal pairs, their four representatives sum to zero. Indeed, if the edge half-vectors are \(a,b,c\), the representatives can be chosen as \(a+b+c\), \(a-b-c\), \(-a+b-c\), and \(-a-b+c\). Thus there are signs \(\delta_j\in\{\pm1\}\) with \(\sum_j\delta_jv_j=0\). Uniqueness of the preceding linear dependence forces \(\delta_j=t s_j\) for some nonzero real \(t\). All \(s_j\) are positive, so the signs are all equal and the four \(s_j\) are equal.

Let \(c_i=Ce_i\) and \(g_{ij}=\langle c_i,c_j\rangle\). Direct expansion gives
\[
 s_1=T+2(g_{12}+g_{13}+g_{23}),\quad
 s_2=T+2(-g_{12}-g_{13}+g_{23}),
\]
\[
 s_3=T+2(-g_{12}+g_{13}-g_{23}),\quad
 s_4=T+2(g_{12}-g_{13}-g_{23}),\qquad
 T=\sum_{i=1}^3\|c_i\|^2.
\]
These four sign triples are mutually orthogonal as columns of a four-row Hadamard matrix, so \(\overline{s}=T\) and
\[
\sum_{j=1}^4(s_j-\overline{s})^2
=16(g_{12}^2+g_{13}^2+g_{23}^2)
=16\sum_{i<j}\kappa_i^2\kappa_j^2\langle Ae_i,Ae_j\rangle^2.
\]
Equality of the four \(s_j\) implies all three cross inner products of columns of \(A\) vanish. Therefore \(B\) is an orthogonal box.

Conversely, if the columns of \(A\) are orthogonal, the columns of \(C\) are orthogonal and \(\|C\varepsilon\|^2=T\) is independent of sign vector. Hence
\[
 \mathcal D^2(B)=\frac{1}{T}C[-1,1]^3,
\]
which is a rectangular parallelepiped. The same calculation proves the claimed certificate identity without the assumption that the second pedal is a parallelepiped. \(\square\)

## Verification

The bundled `check_pedal.py` independently constructs both pedal layers from facet normals over exact rational arithmetic and checks the unique dependence and the sum-of-squares identity for five explicitly displayed nonsingular rational matrices. Run `python check_pedal.py` with SymPy installed. The rectangular case yields zero obstruction; four skew cases yield strictly positive exact rational obstructions. The analytic proof covers all real nonsingular \(3\times3\) matrices; these finite tests are consistency checks only.

For example, for \(A=\begin{psmallmatrix}1&1&0\\0&1&0\\0&0&1\end{psmallmatrix}\), one gets \((s_1,s_2,s_3,s_4)=(11,3,3,11)\) and the obstruction is \(64\), so the second pedal cannot be a parallelepiped.

## Relationship to prior work

Zwierzyński's 2026 paper proves the four-step homothetic return for centered **rectangular** boxes in every dimension and treats second-pedal return for polytopes possessing concentric inscribed and circumscribed spheres. Those results neither classify oblique parallelepipeds nor imply that a nonorthogonal spatial parallelepiped must lose parallelepiped geometry at the second step. The current result is a converse/rigidity boundary for the rectangular-box example, derived from the unique dependence among the four antipodal vertex rays and an exact norm-variance identity. The polar-rectification operation in other polytope studies is different from taking feet of supporting planes.

## Limitations

No classification is asserted in dimensions above three. The second pedal of a skew parallelepiped may still have cubical combinatorial type, and this theorem makes no claim about its full facet structure, eventual periodicity, four-step similarity, or projection feet lying inside facets. No independent external mathematical audit or exhaustive historical-priority certification has been performed. Earlier work under different terminology for facet-foot or pedal constructions could bear on priority.

## References

1. M. Zwierzyński, *When Pedal Shapes Come Back: a Complex Story*, arXiv:2611.01247v1, publicly posted October 31, 2026. https://arxiv.org/html/2611.01247v1 , especially Section 4, Propositions 4.1–4.2.
2. Standard convex-polar geometry: facet equations for a linear image of the cross-polytope, as used explicitly in the proof above.
