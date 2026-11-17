# Sharp projection-body volume in a twisted eight-normal spherical three-design family

## Finding
Let \(a=\sqrt{2/3}\), \(h=1/\sqrt3\), and for each real twist \(\phi\) and \(j\in\{0,1,2,3\}\) put
\[
 u_j^+=(a\cos(j\pi/2),a\sin(j\pi/2),h),\qquad
 u_j^-=(a\cos(j\pi/2+\phi),a\sin(j\pi/2+\phi),-h).
\]
These eight distinct unit vectors form a spherical \(3\)-design. Let \(P_\phi\) be the unique-up-to-translation convex polytope with these outward facet normals, each facet having area \(\pi/2\); thus \(P_\phi\) has surface area \(4\pi\). Its projection body \(\Pi P_\phi\) has support function equal to the area of the orthogonal projection of \(P_\phi\) perpendicular to the support direction.

Define \(d(\phi)=\operatorname{dist}(\phi,(\pi/2)\mathbb Z)\in[0,\pi/4]\). Then the **exact unrestricted three-dimensional volume** is
\[
 \boxed{\operatorname{vol}_3(\Pi P_\phi)=\frac{8\pi^3}{3\sqrt3}\bigl(1+\cos d(\phi)+\sin d(\phi)\bigr).}
\]
Consequently, within the entire square-ring twist family, its sharp minimum and maximum are
\[
 \frac{16\pi^3}{3\sqrt3}\quad\text{(only aligned rings, modulo quarter-turns)},\qquad
 \frac{8\pi^3}{3\sqrt3}(1+\sqrt2)\quad\text{(only half-step twists, modulo quarter-turns)}.
\]
The maximum-to-minimum volume ratio is exactly \((1+\sqrt2)/2\), a relative increase of \((\sqrt2-1)/2\). Against the volume \(4\pi^4/3\) of the projection body of the unit Euclidean ball, the sharp normalized interval is
\[
 \frac{4}{\pi\sqrt3}\le\frac{\operatorname{vol}_3(\Pi P_\phi)}{4\pi^4/3}
 \le\frac{2(1+\sqrt2)}{\pi\sqrt3}.
\]
The aligned endpoint has a nonzero one-sided linear volume increase under twist, whereas the half-step maximizer has a quadratic deficit: if \(0\le d\le\pi/4\) and \(C=8\pi^3/(3\sqrt3)\),
\[
 \operatorname{vol}(\Pi P_d)-\operatorname{vol}(\Pi P_0)=C(d+O(d^2)),\qquad
 \operatorname{vol}(\Pi P_{\pi/4})-\operatorname{vol}(\Pi P_d)
 =C\sqrt2\bigl(1-\cos(\pi/4-d)\bigr).
\]
This is a sharp example of a nonlinear projection invariant varying inside a family whose surface-normal moments through degree three all agree with those of the sphere.

## Assumptions and scope
The ambient space is Euclidean \(\mathbb R^3\). Every twist \(\phi\in\mathbb R\) is allowed. Projection-body volume is ordinary \(3\)-dimensional Lebesgue measure, not the volume of the original polytope. The surface-area normalization \(4\pi\) and equal facet areas \(\pi/2\) are essential for the displayed constants. The theorem optimizes **only over this natural one-parameter eight-normal family**, not over all spherical \(3\)-designs or all convex bodies of a fixed surface area. The source-date evidence is the August 11, 2026 public author upload of the motivating preprint.

## Proof
**Design and geometric existence.** Each of the two horizontal squares has vanishing first and third horizontal moments; its second horizontal moment is one half the identity in the horizontal plane. With the given latitude, averaging over all eight nodes yields \(\frac18\sum uu^T=I_3/3\). All total-degree-three moments vanish: purely horizontal cubic sums vanish on each square, terms containing a single \(z\) cancel between rings, terms with two \(z\)'s have zero horizontal mean, and the mean of \(z^3\) cancels. The degree-one moments vanish as well. These are the spherical moments through order three, so the nodes form a spherical \(3\)-design. Their positive equal weights balance at zero and their span is \(\mathbb R^3\), so Minkowski's discrete existence and uniqueness theorem supplies the asserted full-dimensional polytope and its eight facets.

**Projection-body representation.** Cauchy's formula for the projected area gives, for every \(v\in S^2\),
\[
 h_{\Pi P_\phi}(v)=\frac12\sum_{j=0}^3\frac\pi2\bigl(|v\cdot u_j^+|+|v\cdot u_j^-|\bigr)
 =\frac\pi4\sum_{j=0}^3\bigl(|v\cdot u_j^+|+|v\cdot u_j^-|\bigr).
\]
Hence the projection body is exactly the three-dimensional zonotope \(\sum_{u\in X_\phi}[-\pi u/4,\pi u/4]\). The zonotope determinant formula therefore yields
\[
 \operatorname{vol}_3(\Pi P_\phi)
 =\frac{\pi^3}{8}\sum_{\{i,j,k\}\subset X_\phi}|\det(u_i,u_j,u_k)|.
\]
No inverse construction of the original polytope is needed because its surface-area measure already determines this support function.

**Complete determinant sum.** Quarter-turn relabeling of the lower ring and a reflection reduce to \(0\le\phi\le\pi/4\). Write \(c=\cos\phi\), \(s=\sin\phi\), so \(1\ge c\ge s\ge0\) and \(c^2+s^2=1\). Factor \(a^2h=2/(3\sqrt3)\) out of each determinant, replacing upper vectors by \((\cos(j\pi/2),\sin(j\pi/2),1)\) and lower vectors by \((\cos(j\pi/2+\phi),\sin(j\pi/2+\phi),-1)\).

Among the \(\binom83=56\) triples, eight contain three nodes from one square, each with absolute scaled determinant \(2\): contribution \(16\). Sixteen contain an opposite pair from one square and a node from the other. For any fixed opposite pair, the four scaled absolute determinants are \(2s,2c,2s,2c\); there are four such opposite pairs across both rings, giving \(16(c+s)\). The remaining thirty-two triples contain two adjacent nodes from one square and one from the other. For each of the eight adjacent pairs, the four scaled absolute determinants are \(1+c+s\), \(1+c-s\), \(1-c+s\), and \(c+s-1\). All these are nonnegative on the stated interval because \(c+s\ge1\). Their sum is \(2(1+c+s)\), contributing \(16(1+c+s)\). Therefore the whole **absolute** determinant sum is
\[
 \sum_{\{i,j,k\}}|\det(u_i,u_j,u_k)|
 =a^2h\,[16+16(c+s)+16(1+c+s)]
 =\frac{64}{3\sqrt3}(1+c+s).
\]
Multiplying by \(\pi^3/8\) proves the formula. Since \(c+s\) increases strictly for \(0<\phi<\pi/4\), the sharp endpoint cases follow, including all equality cases under the symmetry reduction. The exact endpoint deficits follow by the identity \(c+s=\sqrt2\cos(\pi/4-\phi)\).

## Verification
A standalone `check.py` recomputes all 56 determinant minors using exact rational arithmetic at four algebraic twists, checks every monomial moment of total degree at most three for four independent twists, and independently obtains the zonotope volume as a three-dimensional convex hull of all \(2^8=256\) signed generator sums at five twists. The exact minor checks and independent hull comparisons passed. The exact identities and global quantifiers are justified by the symbolic determinant classification above, not inferred from finite experiments.

## Relationship to prior work
The 2026 preprint *Minkowski Polytopes of Spherical Designs: High-Order Isotropy and Quantitative Sphericity* provides the equal-area Minkowski realization, isotropic surface-tensor identities, Cauchy representation, and uniform approximation bounds for projection bodies. Its full accessible manuscript was inspected in the introduction and Sections 2, 3, 6 and the concluding discussion. It does not provide the exact volume law above for two twisted square latitude rings. The classical Cauchy and zonotope determinant formulas are inputs, not claimed as discoveries.

Other relevant mathematical results concern spherical covering by two twisted latitude rings, random-shadow variance for six-normal spherical designs, and brightness extrema for the aligned \(2n\)-normal latitude family. Those conclusions concern different invariants or only the aligned subfamily; none implies the whole twist-dependent determinant sum. The present result includes the aligned case only as one endpoint. Historical priority is provisional because some relevant indexed manuscripts were available only at abstract level, and equivalent formulas may be recorded under different terminology.

## Limitations
No claim is made about the full space of eight-point spherical \(3\)-designs, optimal original-polytope volume, other geometric projections, or any optimality across all equal-surface-area bodies. The derivation uses the exact equal-facet-area surface-area measure and does not recover explicit vertices of the original Minkowski polytopes. Some nearby published primary papers were available only through their abstracts or indexed summaries, leaving an ordinary literature-priority risk. No independent external mathematical audit has been performed.

## References
1. Congpei An, *Minkowski Polytopes of Spherical Designs: High-Order Isotropy and Quantitative Sphericity*, first author-uploaded August 11, 2026, arXiv:2608.11570 (August 12, 2026); accessible full manuscript: https://www.researchgate.net/publication/412115876_Minkowski_Polytopes_of_Spherical_Designs_High-Order_Isotropy_and_Quantitative_Sphericity.
2. D. Langharst, M. Roysdon and A. Zvavitch, *General measure extensions of projection bodies*, Proceedings of the London Mathematical Society 125 (2022), DOI: 10.1112/plms.12477. Cauchy's projection formula appears as Eq. (2.3).
3. G. M. Ziegler, *Lectures on Polytopes*, 1995, section on mixed volumes and zonotope determinant sums; see also E. Gover, *Congruence and Metrical Invariants of Zonotopes*, arXiv:1401.4749.
