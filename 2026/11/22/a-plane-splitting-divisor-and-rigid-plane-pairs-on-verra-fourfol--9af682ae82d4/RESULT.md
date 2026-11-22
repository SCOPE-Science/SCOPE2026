# A plane-splitting divisor and rigid plane pairs on Verra fourfolds

## Finding

Fix the projection to the second factor of a smooth complex Verra fourfold. The condition that a fiber split into two planes defines an irreducible divisor in the parameter space of smooth bidegree-\((2,2)\) double covers. For a general member of this divisor the split fiber is unique, its two plane components are infinitesimally rigid, the quadric-fibration discriminant has an ordinary node, and the extra plane class produces a rank-four algebraic intersection lattice of determinant \(-16\).

More precisely, put
\[
B=\mathbb P^2_u\times\mathbb P^2_v,\qquad
\mathcal P=\mathbb P H^0(B,\mathcal O_B(2,2))\cong\mathbb P^{35}.
\]
Let \(\mathcal U\subset\mathcal P\) be the open subset parametrizing smooth branch divisors and set
\[
\mathcal D=\bigl\{[F]\in\mathcal U:\ \exists p\in\mathbb P^2_v,\ \ell\in H^0(\mathbb P^2_u,\mathcal O(1))\setminus\{0\},\ F(u,p)=\ell(u)^2\bigr\}.
\]
Here a nonzero square is understood projectively, so constant square factors are absorbed into \(\ell\). Then \(\mathcal D\) is a nonempty irreducible divisor in \(\mathcal U\). For general \([F]\in\mathcal D\) there is exactly one \(p\). The associated smooth double cover \(V\to B\) has precisely two components \(R_+,R_-\cong\mathbb P^2_u\) of multidegree \((1,0)\) above this \(p\), meeting along the ramification line \(\ell=0\).

For either component \(R\), its normal bundle \(N=N_{R/V}\) obeys
\[
0\longrightarrow N\longrightarrow\mathcal O_{\mathbb P^2}(1)\oplus\mathcal O_{\mathbb P^2}^{\oplus2}
\xrightarrow{(2\ell,-q_1,-q_2)}\mathcal O_{\mathbb P^2}(2)\longrightarrow0,
\]
with \(q_i=\partial_{v_i}F(u,p)\) in affine coordinates centered at \(p\). In particular
\[
(c_1(N),c_2(N))=(-H,2),\qquad
(h^0(N),h^1(N),h^2(N))=(0,1,0).
\]
Thus the two planes are isolated *reduced* points of their Hilbert scheme. The discriminant sextic of the projection \(V\to\mathbb P^2_v\) has an ordinary node at \(p\).

Writing \(H_u,H_v\) for the two pulled-back hyperplane divisors, the classes \(H_u^2,H_uH_v,H_v^2,[R]\) have intersection Gram matrix
\[
M=\begin{pmatrix}
0&0&2&1\\0&2&0&0\\2&0&0&0\\1&0&0&2
\end{pmatrix},\qquad\det M=-16,
\]
whose Smith invariants are \((1,1,2,8)\). Hence they span a rank-four sublattice of middle cohomology whose discriminant group is \(\mathbb Z/2\oplus\mathbb Z/8\).

## Assumptions and scope

Everything is over \(\mathbb C\). The branch divisor \(\{F=0\}\subset B\) is smooth. The statement about uniqueness, normal cohomology and ordinary nodal discriminant holds for a nonempty Zariski-open dense subset of the irreducible divisor \(\mathcal D\), rather than for every special member. The plane count refers only to plane surfaces on which \(H_u\) restricts to \(\mathcal O(1)\) and \(H_v\) to \(\mathcal O\), i.e. the chosen fibration's split-fiber planes; planes of any other numerical type are not classified.

## Proof

**1. Irreducible divisor and a unique split fiber.** Evaluation at a fixed \(p\in\mathbb P^2_v\) maps the \(36\)-dimensional vector space of bidegree-\((2,2)\) forms onto the six-dimensional space of ternary quadrics in \(u\). Nonzero squares of linear forms constitute the affine cone over the irreducible Veronese \(\nu_2(\mathbb P^2)\subset\mathbb P^5\), of codimension three in the six-dimensional target. Thus the projective incidence of pairs \(([F],p)\) with square or zero evaluation is irreducible of dimension \(35-3+2=34\). The zero-evaluation part has dimension at most \(35-6+2=31\), and does not affect the general point. Moreover zero evaluation cannot occur for a smooth branch: if \(F(u,p)\equiv0\), its two transverse base derivatives are homogeneous quadratic forms on \(\mathbb P^2_u\) with a common zero by Bézout, making the branch singular there. Thus the nonzero square locus is closed relative to the smooth-branch open set.

For distinct \(p,q\), simultaneous evaluation at \(p\) and \(q\) is surjective onto two copies of the six-dimensional space of ternary quadrics: \(\mathcal O_{\mathbb P^2_v}(2)\) separates two points. Therefore the incidence of forms with a square at both \(p,q\) has dimension at most \(35-6+4=33\). It follows that the incidence projection is generically one-to-one and its image has dimension \(34\), giving the irreducible divisor and its unique general \(p\). Smooth branch forms occur on this divisor: the explicit smooth example in Galluzzi--van Geemen, Proposition 1.3, has \(F(u,[0:0:1])=u_2^2\), and the smooth locus is open.

**2. Plane pair and exact normal sequence.** Locally trivialize \(\mathcal O_B(1,1)\) over a base chart centered at \(p\), and write \(V\) as \(w^2=F(u,v)\) in its total space \(W=\operatorname{Tot}\mathcal O_B(1,1)\). The two planes are the graphs \(w=\pm\ell(u),v=p\), meeting in the line \(\ell=0\). Conversely, any plane of the specified multidegree projects isomorphically onto \(\mathbb P^2_u\) over some constant \(p\) and defines such a splitting; so there are exactly two for general \(F\in\mathcal D\).

Over either plane the ambient normal bundle fits into a split exact sequence with terms \(\mathcal O(1)\) (vertical movement) and \(\mathcal O^{\oplus2}\) (base movement); the extension splits because \(H^1(\mathbb P^2,\mathcal O(1))=0\). The defining hypersurface has normal line bundle \(\mathcal O(2)\). Differentiating \(w^2-F\) gives the displayed surjective map; surjectivity holds because \(V\) is smooth. Therefore
\[
c(N)=\frac{1+H}{1+2H}=1-H+2H^2.
\]
The map on global sections has source dimension five and target dimension six. Modulo the image \(\ell H^0(\mathcal O(1))\), its last two columns are the binary quadrics \(\bar q_i=q_i|_{\ell=0}\). They are independent for general \(F\in\mathcal D\) (an explicit witness appears below). Thus the map has rank five, and the long exact cohomology sequence proves \((h^0,h^1,h^2)(N)=(0,1,0)\). A finite-type Hilbert scheme has Zariski tangent space \(H^0(N)\) at a local complete-intersection surface: vanishing forces its local ring to be the reduced residue field, proving isolation and reducedness.

**3. Ordinary discriminant node.** The quadric-surface fiber has equation \(w^2-u^{\mathsf T}A(v)u=0\), with \(A(v)\) a symmetric \(3\times3\) matrix of quadratic forms in \(v\). At \(p\), \(A(p)\) has rank one, its kernel is the two-plane \(\{\ell=0\}\) in the \(u\)-coordinates, and \(\det A(v)\) has order at least two. If \(s,t\) are local coordinates at \(p\), its degree-two initial form is a nonzero scalar multiple of
\[
\det\bigl(s\,Q_1+t\,Q_2\bigr),
\]
where \(Q_i\) are the symmetric binary-quadratic matrices for \(q_i|_{\ell=0}\). For a general pair this degree-two form has distinct linear factors, and hence the sextic is nodal at \(p\).

Nonemptiness of the required open conditions is witnessed by the explicit smooth branch polynomial in Proposition 1.3 of Galluzzi--van Geemen:
\[
\begin{aligned}
F={}&(u_0^2+2u_0u_1)v_0^2+2u_2^2v_0v_1+(2u_0u_2+u_1^2)v_0v_2\\
 &+(2u_0u_2+u_1^2)v_1^2+(-u_0^2+2u_0u_1)v_1v_2+u_2^2v_2^2.
\end{aligned}
\]
For \(p=[0:0:1]\) and \(\ell=u_2\), the two base derivatives restrict to \(q_1|_{u_2=0}=u_1^2\), \(q_2|_{u_2=0}=-u_0^2+2u_0u_1\). These are independent, have no common zero in \(\mathbb P^1\), and their pencil determinant is \(-t(s+t)\), a squarefree quadratic. Their independence and nonzero discriminant are open conditions; this verifies both generic claims.

**4. Intersection sublattice.** The degree-two finite cover gives \(H_u^2H_v^2=2\). All other degree-four intersections among \(H_u^2,H_uH_v,H_v^2\) vanish except \((H_uH_v)^2=2\). Restricting to \(R\cong\mathbb P^2_u\) gives \(H_u|_R=H\), \(H_v|_R=0\), and thus \(R\cdot H_u^2=1\), \(R\cdot H_uH_v=R\cdot H_v^2=0\). Finally the self-intersection formula gives \(R^2=\int_R c_2(N)=2\). These determine \(M\); direct integer row-column operations yield Smith normal form \(\operatorname{diag}(1,1,2,8)\). Since \(\det M\ne0\), the span has rank four.

## Verification

Run the standalone exact-symbolic checker:

```bash
python verification/check_verra_planes.py
```

It reconstructs the displayed source polynomial, its two first base derivatives, the binary pencil determinant, the rank-five global-section map, the Chern expansion, and the integral Gram determinant and Smith normal form. The incidence dimension argument, the global geometric smoothness of the cited example, the genericity statements and the Hilbert tangent criterion are proved mathematically above, not inferred from finite symbolic tests.

## Relationship to prior work

Galluzzi--van Geemen, *Some families of birational cubic and Verra fourfolds*, arXiv:2611.15908v1, Proposition 1.3, explicitly exhibit a split plane fiber in one smooth Verra fourfold and calculate the universal rank-three ambient lattice. The same paper already observes that the relevant sextic is nodal in their particular example. Camere--Kapustka--Kapustka--Mongardi, *Verra Four-Folds, Twisted Sheaves, and the Last Involution* (2017), Proposition 6.3, also identify plane components of a reducible quadric fiber in special symmetric Verra families. Neither is being claimed as new here.

The contribution is the *generic global divisor and uniqueness statement*, coupled with the precise normal bundle, infinitesimal rigidity, and the explicit rank-four cycle-intersection sublattice for the general plane-splitting family. The nearby literature on associated twisted K3 surfaces and derived categories in Jacovskis--Meinsma--Moschetti (arXiv:2610.32952) and Kapustka--Kapustka--Moschetti (arXiv:1712.06958v2) was checked for possible stronger coverage; it does not state this combined family-and-normal-bundle theorem in the inspected text.

## Limitations

The theorem classifies only the planes in a specified fiberwise multidegree for one projection, not all planes on a Verra fourfold. It does not assert the rank-four sublattice is saturated in integral middle cohomology, nor that it is the full algebraic-cycle lattice. It does not classify special members with multiple rank-one fibers, more complicated discriminant singularities or nonreduced Hilbert components. Absence of a found equivalent claim is not a proof of publication priority, and there has been no independent mathematical audit.

## References

- F. Galluzzi and B. van Geemen, *Some families of birational cubic and Verra fourfolds*, arXiv:2611.15908v1 (11 November 2026), Sections 1.2--1.4, Proposition 1.3. https://arxiv.org/html/2611.15908v1
- A. Jacovskis, R. Meinsma and R. Moschetti, *The Verra involution on special cubic fourfolds*, arXiv:2610.32952v1 (23 October 2026), Sections 2 and 5. https://arxiv.org/abs/2610.32952
- G. Kapustka, M. Kapustka and R. Moschetti, *Equivalence of K3 surfaces from Verra threefolds*, arXiv:1712.06958v2 (2018), Sections 2--4. https://arxiv.org/html/1712.06958v2
- C. Camere, G. Kapustka, M. Kapustka and G. Mongardi, *Verra Four-Folds, Twisted Sheaves, and the Last Involution*, 2017 preprint, Proposition 6.3; International Mathematics Research Notices, 2019. https://doi.org/10.1093/imrn/rnx327
