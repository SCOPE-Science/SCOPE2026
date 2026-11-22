# Three-phase brightest-shadow geometry and exact endpoint tails of right rectangular pyramids

## Finding
For every \(a,b,h>0\), with \(a\le b\), let
\[
K(a,b,h)=\operatorname{conv}\bigl(\{(\pm a,\pm b,0)\}\cup\{(0,0,h)\}\bigr)\subset\mathbb R^3,
\]
and let \(B(U)\) be the ordinary area of its orthogonal projection onto the plane perpendicular to a uniformly distributed unit vector \(U\in S^2\). Put \(r=b/a\ge1\) and \(s=h/a>0\). Then the **exact largest projected area** is
\[
M=ab\max\left\{4,\sqrt{9+s^2},\sqrt{4+s^2+s^2/r^2}\right\}.
\]
All maximizing viewing directions, and the exact upper endpoint law, have the following sharp phase classification. Count distinct **oriented unit normals**; opposite normals represent the same unoriented projection plane.

* **Shorter aspect range:** if \(1\le r<\sqrt{7/5}\), put \(s_0=\sqrt{12r^2/(r^2+1)}\). The number \(k\) of maximizing oriented normals is \(2\) for \(s<s_0\), \(10\) at \(s=s_0\), and \(8\) for \(s>s_0\).
* **Longer aspect range:** if \(r>\sqrt{7/5}\), the two critical heights are \(s_1=\sqrt7\) and \(s_2=\sqrt5\,r\). The successive maximizing-normal counts are \(2,6,4,12,8\) across the five regimes \(s<s_1\), \(s=s_1\), \(s_1<s<s_2\), \(s=s_2\), \(s>s_2\).
* **Triple point:** when \(r=\sqrt{7/5}\), the only critical height is \(s=\sqrt7\). The counts are \(2,14,8\) below, at and above this height. In particular, exactly **fourteen distinct oriented directions** tie at the unique triple transition.

The directions themselves are explicit. For any nonzero vector \(v\), write \(\widehat v=v/\|v\|\). The axial family is \(\widehat{(0,0,\pm4)}\) (two); the one-sided family is \(\widehat{(\pm s,0,\pm3)}\) (four); the two-sided family is \(\widehat{(\pm s,\pm s/r,\pm2)}\) (eight). Every sign shown may be chosen independently. The maximizing set is exactly the union of the listed families whose norms realize the displayed maximum.

Moreover, for **every** such pyramid there is an explicitly computable \(q<M\) such that the upper-tail probability is **exactly linear** on the whole interval \(q\le t\le M\):
\[
\boxed{\displaystyle \mathbb P\{B(U)>t\}=\frac{k}{2}\left(1-\frac{t}{M}\right).}
\]
An explicit positive-length interval is provided in Assumptions and scope. Thus the exact tail slopes with respect to the normalized threshold \(t/M\), as the height increases, are \(1,5,4\) for the short-aspect range and \(1,3,2,6,4\) for the long-aspect range; the unique triple-point slope is \(7\). For \(N\) independent uniform views, if \(B_N^{\max}\) is the largest projected area, then for \(x\ge0\)
\[
\lim_{N\to\infty}\mathbb P\{N(M-B_N^{\max})>x\}
=\exp\bigl(-kx/(2M)\bigr).
\]

## Assumptions and scope
All lengths are Euclidean, all areas are unsigned Euclidean two-dimensional areas, and all parameters \(a,b,h\) are strictly positive. Interchanging \(a\) and \(b\) only relabels the first two coordinate axes. Oriented normals are used solely for counting; Haar-uniform unoriented planes yield the same area law because \(B(u)=B(-u)\).

The exact admissible endpoint \(q\) is a finite expression, not an implicit existence claim. With \(s=h/a\), \(r=b/a\), define the following finite set of **eighteen** vectors (all displayed signs independent):
\[
\mathcal V=\{(0,0,\pm4)\}\cup\{(\pm s,0,\pm3)\}\cup
\{(0,\pm s/r,\pm3)\}\cup\{(\pm s,\pm s/r,\pm2)\}.
\]
Put \(L=\max_{v\in\mathcal V}\|v\|\), \(\mathcal W=\{v\in\mathcal V:\|v\|=L\}\), \(k=|\mathcal W|\), and
\[
\lambda=\max\bigl(\{\|v\|:v\in\mathcal V\setminus\mathcal W\}\cup\{0\}\bigr),\qquad
\eta=\max\left(\left\{\sqrt{\frac{L^2+v\cdot w}{2}}:v,w\in\mathcal W,\ v\ne w\right\}\cup\{0\}\right).
\]
Then \(M=abL\) and \(q=ab\max\{\lambda,\eta\}\). This always satisfies \(q<M\), even at every transition, because there are finitely many distinct vectors, nonmaximizing norms are smaller, and distinct equal-norm vectors have scalar product strictly smaller than \(L^2\). The provided \(q\) is a **certified endpoint**, not a claim that the linear interval cannot extend farther.

## Proof
**1. Exactly compute the brightness function.** The base face has area-normal vector \((0,0,-4ab)\). The four triangular side faces have outward area-normal vectors \((\pm bh,0,ab)\) and \((0,\pm ah,ab)\). By the classical Cauchy projection formula, for every unit \(u=(u_x,u_y,u_z)\),
\[
B(u)=\tfrac12\Bigl(4ab|u_z|+|ab u_z+bh u_x|+|ab u_z-bh u_x|
+|ab u_z+ah u_y|+|ab u_z-ah u_y|\Bigr).
\]
The elementary identity \(|x+y|+|x-y|=2\max\{|x|,|y|\}\) gives the pointwise formula
\[
\boxed{B(u)/(ab)=2|u_z|+\max\{|u_z|,s|u_x|\}+\max\{|u_z|,(s/r)|u_y|\}.}\tag{1}
\]
This formula can also be verified without Cauchy's theorem by taking the convex hull of the five orthogonally projected vertices and evaluating its planar shoelace area; the attached independent checker implements that calculation.

**2. Reduce the global optimization to eighteen vectors.** Expand each maximum in (1) into its two possible linear terms, and each absolute value into its two signed linear terms. This yields, identically for every unit \(u\),
\[
B(u)/(ab)=\max_{v\in\mathcal V}u\cdot v.\tag{2}
\]
Since \(\max_{\|u\|=1}u\cdot v=\|v\|\), finite maxima commute:
\[
M/(ab)=\max_{v\in\mathcal V}\|v\|.
\]
The four families of vector norms are \(4\), \(\sqrt{9+s^2}\), \(\sqrt{9+s^2/r^2}\), and \(\sqrt{4+s^2+s^2/r^2}\). The third is no larger than the second; for \(r>1\) it is strictly smaller, and for \(r=1\) both are still below the maximum because the two-sided family overtakes them before they can overtake the axial family. This proves the formula for \(M\) and excludes all other maximizing families. Equality in Cauchy--Schwarz shows that a direction maximizing (2) is **necessarily and sufficiently** \(\widehat v\) for some \(v\in\mathcal W\), with no other directions possible.

**3. Classify all height and aspect transitions.** Compare the squares of the three relevant candidate norms:
\[
4^2=9+s^2\iff s^2=7,\qquad
9+s^2=4+s^2+s^2/r^2\iff s^2=5r^2,
\]
\[
4^2=4+s^2+s^2/r^2\iff s^2=\frac{12r^2}{r^2+1}.
\]
The order of these crossings reverses at \(r^2=7/5\). For \(r^2<7/5\), the one-sided norm is **strictly below** the maximum at every positive height, and the axial and two-sided norms exchange global dominance directly at \(s_0\). For \(r^2>7/5\), the axial norm dominates below \(\sqrt7\), the one-sided norm dominates until \(\sqrt5\,r\), and the two-sided norm dominates thereafter. For equality \(r^2=7/5\), all three relevant norms tie only at \(s=\sqrt7\). The three families contain \(2,4,8\) distinct vectors for positive \(s,r\), so their unions have exactly the counts asserted, including \(2+4+8=14\) at the triple point. This establishes both the global maximum and the full equality classification, with no reliance on sampled orientations.

**4. Prove the exact endpoint distribution.** Equation (2) implies for each \(t\in[q,M]\) that
\[
\{B(U)>t\}=\bigcup_{v\in\mathcal V}\{ab\,v\cdot U>t\}.
\]
No nonwinner contributes, because \(ab\,v\cdot U\le ab\|v\|\le ab\lambda\le q\) when \(v\notin\mathcal W\). For two distinct winners \(v,w\), if both inequalities hold, then
\[
2t<ab\,(v+w)\cdot U\le ab\,\|v+w\|
=2ab\sqrt{(L^2+v\cdot w)/2}\le 2q\le2t,
\]
a contradiction. Thus the \(k\) winning spherical caps are disjoint on this range (including boundaries up to probability zero). For Haar-uniform \(U\in S^2\), each cap has area fraction
\[
\mathbb P\{ab\,v\cdot U>t\}=\frac12\left(1-\frac{t}{abL}\right)=\frac12(1-t/M).
\]
Summing proves the exact linear tail on a **strictly positive-length interval**. Substituting \(t=M-x/N\) and taking the \(N\)-fold independent maximum yields
\[
\lim_{N\to\infty}(1-kx/(2MN))^N=e^{-kx/(2M)}.
\]
This proves the stated extreme-value consequence.

## Verification
The accompanying standalone `verify.py` reconstructs each orthogonal projection from its five three-dimensional vertices, constructs an independent two-dimensional basis, builds a planar convex hull by monotone chain and measures its area by shoelace formula. It tests the analytic brightness identity against 14,400 independently computed projected areas across twelve aspect-height cases, including all four boundary-transition cases and the unique fourteen-normal triple point. It also checks the vector norm envelope, exact maximizing-normal counts, positive cap window, and every pairwise spherical-cap separation bound. Execute `python3 verify.py` using Python's standard library; it requires no external package. Finite tests are diagnostic and **not** a substitute for the quantified proof above.

## Relationship to prior work
Cauchy's projection formula and the projection-body/zonotope representation are classical. Omri Abas's *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability* (2026) explicitly develops these tools, including a general spherical co-area method, but its inspected treatment does not give a maximizing-area phase diagram for right rectangular pyramids. The present argument specializes the classical representation to this five-faced family and classifies the exact competition of its three projection-body vertex families.

An earlier public *Exact five-vertex shadow law and unique height optimum for right rectangular pyramids* (October 2026) treats the **number of vertices of a random silhouette**, rather than the **greatest projected area** or its near-maximum probability. The complete result was compared in full. The published *An exact upper-tail law for random planar shadows of cross-polytopes* (November 2026) supplies a cap-based high-tail method for a **different polytope family** and projection problem; the full result was read and the cap method is credited rather than claimed independently new. A sharp brightest-shadow transition is also known for right **circular cones**, where rotational symmetry creates an oblique latitude circle, not the rectangle-dependent \(2\)-to-\(4\)-to-\(8\) families and fourteen-normal concurrence here.

The original contribution claimed is the all-positive-parameter rectangular-pyramid **extremal phase diagram**, equality-direction multiplicities and their exact near-maximum tail coefficients, conditional on the surveyed literature. It is not a claim to have invented projection bodies, spherical caps, or the classical orientation-integral method.

## Limitations
This theorem is about centered-apex **right rectangular pyramids**, orthographic projected **area**, and Haar-uniform three-dimensional viewing directions. It does not give the full bulk distribution below \(q\), a sharp maximal linearity interval, results for oblique pyramids, or analogous classifications for nonrectangular bases. The finite checker corroborates the analytic identities but cannot establish exhaustive correctness or historical novelty. Although the motivating and most relevant indexed published works were compared, unindexed specialized earlier geometry calculations might imply the claimed classification. No independent audit has been performed.

## References
1. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202, earliest displayed public date 2026-08-10; especially Sections 2.4--3.1. https://arxiv.org/abs/2609.26202 .
2. *Exact five-vertex shadow law and unique height optimum for right rectangular pyramids*, public mathematical record dated 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-five-vertex-shadow-law-and-unique-height-optimum-for-right--2273575e8a0a .
3. *An exact upper-tail law for random planar shadows of cross-polytopes*, public mathematical record dated 2026-11-01. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-an-exact-upper-tail-law-for-random-planar-shadows-of-cross-polyt--24c55f635442 .
4. *A sharp global brightness-direction switch for right circular cones*, public mathematical record dated 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-global-brightness-direction-switch-for-right-circular-co--19c34891a8b8 .
5. R. J. Gardner, *Geometric Tomography*, 2nd ed., Cambridge University Press (2006), Chapter 4, for the classical Cauchy projection formula.
