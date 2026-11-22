# A sharp ten-direction brightness bound and its complete tetrahedral equality family

## Finding
Let \(T\subset\mathbb R^3\) be any nondegenerate tetrahedron. Its orthogonal projection area \(B_T(u)\), with \(u\in S^2\) the oriented viewing normal, has **at most ten maximizing oriented directions**, or five unoriented viewing axes. This bound is sharp. Up to Euclidean rotation, common positive scaling of facet-area vectors, and relabeling, **every** equality tetrahedron belongs to the following one-parameter family. Choose unit vectors \(e,f\) making angle \(120^\circ\), a unit vector \(g\perp e,f\), and \(0<t<1\). Put \(w=e+f\), a unit vector, and define the outward area vectors
\[
F_1=e,\quad F_2=f,\quad
F_3=-tw+\sqrt{t(1-t)}\,g,\quad
F_4=-(1-t)w-\sqrt{t(1-t)}\,g.
\]
These four vectors are the facet areas times outward unit normals of a unique tetrahedron up to translation. Their maximal shadow area is \(1\), and the ten maximizing oriented directions are precisely the positive and negative unit vectors along
\[
F_1,\quad F_2,\quad F_1+F_2,\quad F_1+F_3,\quad F_1+F_4.
\]
For the symmetric member \(t=1/2\), and a uniformly random oriented direction \(U\in S^2\), the entire upper end of the brightness distribution is **exactly**
\[
\Pr\{B_T(U)>z\}=5(1-z),\qquad \sqrt{7/8}\le z\le1.
\]
The lower endpoint \(\sqrt{7/8}\) is sharp: this linear identity fails at every sufficiently close value below it. For arbitrary scale \(M>0\), replace each vector above by \(M F_i\) and replace \(z\) by \(z/M\).

## Assumptions and scope
An outward area vector is \(F_i=A_i n_i\), where \(A_i>0\) is the area of facet \(i\) and \(n_i\) its outward Euclidean unit normal. The four area vectors of a tetrahedron satisfy \(\sum_iF_i=0\) and span \(\mathbb R^3\). We count viewing normals \(u\) and \(-u\) separately, but they define the same projection plane. A maximizing direction means \(B_T(u)=\max_{v\in S^2}B_T(v)\). All probability statements use normalized surface-area measure on \(S^2\). The parameter \(t\) and \(1-t\) produce the same family after exchanging the two smaller faces; the theorem does not claim uniqueness of a parametrization without this equivalence.

## Proof
**1. Finite support representation.** Cauchy's projection formula for a polyhedron gives
\[
B_T(u)=\frac12\sum_{i=1}^{4}|\langle F_i,u\rangle|.
\]
Because \(\sum_iF_i=0\), the right side equals \(\max_{S\subseteq\{1,2,3,4\}}\langle\sum_{i\in S}F_i,u\rangle\). Complementary subsets give opposite vectors. Up to sign, every nonzero subset sum is one of the seven vectors
\[
F_1,F_2,F_3,F_4,F_1+F_2,F_1+F_3,F_1+F_4.
\]
Write \(M\) for their largest norm. The strict Cauchy--Schwarz equality condition shows that precisely those vectors of norm \(M\), normalized to unit length and with both signs, are the maximizing directions. All seven axes are nonzero and distinct: otherwise the four facet-area vectors would fail to span three dimensions.

**2. The sharp multiplicity bound.** Expanding squares and using \(F_1+F_2+F_3+F_4=0\) yields the identity
\[
\|F_1+F_2\|^2+\|F_1+F_3\|^2+\|F_1+F_4\|^2
=\sum_{i=1}^{4}\|F_i\|^2.
\]
Each of the three terms on the left is at most \(M^2\). If three or four singleton vectors attained \(M\), the right side would exceed \(3M^2\), a contradiction, since the remaining facet vectors are nonzero. Therefore at most two of four singleton axes and at most three pair-sum axes can maximize: at most five axes, or ten oriented directions.

**3. Necessity of the equality family.** Suppose five axes maximize. Relabel the two length-\(M\) singleton vectors \(F_1,F_2\). Then all three pair sums have norm \(M\). The identity above gives \(\|F_3\|^2+\|F_4\|^2=M^2\). Set \(e=F_1/M\), \(f=F_2/M\), and \(t=\|F_3\|^2/M^2\). Nonzero facet areas give \(0<t<1\); \(\|F_1+F_2\|=M\) gives \(e\cdot f=-1/2\), hence \(w=e+f\) is unit. The norm equations for \(F_1+F_3\) and \(F_2+F_3=-(F_1+F_4)\) imply \(e\cdot F_3=f\cdot F_3=-Mt/2\). Consequently \(F_3\) is orthogonal to \(e-f\), and its component along \(w\) equals \(-Mt\). Its remaining component is perpendicular to both \(e,f\), of magnitude \(M\sqrt{t(1-t)}\). Choosing its sign as the orientation of \(g\) gives exactly the displayed family, with \(F_4\) fixed by equilibrium.

**4. Sufficiency and geometric realization.** Conversely, the displayed vectors sum to zero, span \(\mathbb R^3\) for every \(0<t<1\), and have squared lengths \(1,1,t,1-t\). Their three pair sums with \(F_1\) each have squared length \(1\). Thus exactly five axes maximize. Applying Minkowski's existence-and-uniqueness theorem to the positive discrete surface-area measure with masses \(\|F_i\|\) at normals \(F_i/\|F_i\|\) gives a full-dimensional convex polytope with precisely four facets, hence a tetrahedron, unique up to translation.

**5. Sharp terminal brightness law at \(t=1/2\).** The ten maximizing unit vectors are the two signs of the five vectors in the Finding. Their five-by-five Gram matrix is
\[
\begin{pmatrix}
1&-1/2&1/2&3/4&3/4\\
-1/2&1&1/2&-3/4&-3/4\\
1/2&1/2&1&0&0\\
3/4&-3/4&0&1&1/2\\
3/4&-3/4&0&1/2&1
\end{pmatrix}.
\]
For any two distinct oriented maximizing vectors their inner product is at most \(3/4\), with equality attained. The two remaining subset vectors have norm \(1/\sqrt2\). Therefore, for \(z>1/\sqrt2\), the event \(B_T(U)>z\) is the union of ten spherical caps with angular radius \(\arccos z\). These caps are pairwise disjoint, up to measure-zero tangency, exactly for \(z\ge\sqrt{(1+3/4)/2}=\sqrt{7/8}\). Each cap has probability \((1-z)/2\), yielding \(5(1-z)\). Immediately below this threshold some two caps overlap in a nonempty open lens, while no shorter vector is active, so the union probability is strictly smaller than \(5(1-z)\). This proves sharpness.

## Verification
The standalone `verify.py` explicitly reconstructs tetrahedron edge vectors from the symmetric facet-area data and checks the three outward area normals. It also checks the balance and rank of the family, all seven candidate norms for five exact rational values of \(t\), the exact ten-center contact Gram matrix, and the sharp overlap threshold. It independently compares the finite-subset support formula with the Cauchy facet expression on 100 nondegenerate random vector configurations. A 250,000-direction deterministic-seed simulation checks the two endpoint-tail values as supplemental numerical evidence. Run `python verify.py` with Python 3, SymPy, and NumPy. The infinite assertion is proved above; sampling is not used as an infinite certificate.

## Relationship to prior work
Horváth (2020, Section 2.3) gives the Cauchy projection-body representation, Minkowski existence theorem, and the rhombic dodecahedral projection body of the **regular** tetrahedron. Abas (first public 2026-08-10, arXiv:2609.26202) develops polyhedral brightness distributions, including the regular tetrahedron's brightness law. A 2013 published mathematical discussion by Blue explicitly gives the **same sum-of-squares identity for the four ordinary and three pseudo-face areas**; that identity is credited, not claimed as novel. These sources establish the framework and a distinguished symmetric case, not the stated **universal sharp ten-direction bound, complete asymmetric equality family, or exact sharp terminal tail of that family**. The combinatorial subset-vector representation itself is standard and is not presented as a new principle.

## Limitations
The result concerns nondegenerate tetrahedra in three-dimensional Euclidean space. No classification of other numbers of maximizing directions, full random brightness distributions, or higher-dimensional analogue is claimed. The 2026 full text was not accessible during source comparison; the abstract and metadata were inspected, so historical priority remains provisional. The equality-family construction invokes the classical Minkowski existence theorem. Independent external mathematical audit has not been performed.

## References
- Á. G. Horváth, *On Convex Bodies that are Characterizable by Volume Function*, Arnold Mathematical Journal **6** (2020), 1–20, Section 2.3. https://doi.org/10.1007/s40598-020-00132-0
- Blue, answer to *Inequality for each a, b, c, d being each area of four faces of a tetrahedron*, Mathematics Stack Exchange, 2013-08-28, pseudo-face sum-of-squares identity. https://math.stackexchange.com/questions/477964/inequality-for-each-a-b-c-d-being-each-area-of-four-faces-of-a-tetrahedron
- O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202, first submitted 2026-08-10. https://arxiv.org/abs/2609.26202
