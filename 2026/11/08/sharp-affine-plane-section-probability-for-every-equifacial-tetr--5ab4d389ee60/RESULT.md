# Sharp affine-plane section probability for every equifacial tetrahedron

## Finding
Let \(T\subset\mathbb R^3\) be any nondegenerate equifacial tetrahedron (all four triangular faces congruent). Choose a plane from the rotation- and translation-invariant measure on unoriented affine planes, conditioned on meeting \(T\). Write \(p_4(T)\) for the probability that its nondegenerate planar section is a quadrilateral. Then
\[
\boxed{\frac{2\pi}{\arccos(-1/3)}-3\;\leq\;p_4(T)\;<\;1.}
\]
The lower endpoint, approximately \(0.28853554307200385\), is attained **exactly** by regular tetrahedra, up to similarity, and the upper endpoint is sharp but unattained. In fact, the complete range on equifacial tetrahedra is precisely the indicated half-open interval.

Every equifacial tetrahedron is congruent to the convex hull of
\[
(a,b,c),\quad(a,-b,-c),\quad(-a,b,-c),\quad(-a,-b,c),\qquad a,b,c>0.
\]
Define \(q_i=a_i^{-2}/\sum_j a_j^{-2}\), with \((a_1,a_2,a_3)=(a,b,c)\), and define the opposite-edge-pair length and exterior dihedral angle by
\[
\ell_i=2\sqrt{\sum_{j\ne i}a_j^2},\qquad \beta_i=2\arccos\sqrt{q_i}.
\]
Then the complete exact probability formula is
\[
\boxed{p_4(T)=\frac{2\pi\sum_{i=1}^{3}\ell_i}{\sum_{i=1}^{3}\ell_i\beta_i}-3.}
\]
Along a flattened disphenoid with \(a\to0\), while \(b,c>0\) are fixed, the probability has the exact aspect-dependent limit
\[
\lim_{a\downarrow0}p_4(T_{a,b,c})=\frac{2\sqrt{b^2+c^2}}{b+c}-1.
\]
For fixed nonzero \(b,c\), these limiting values range from \(\sqrt2-1\) (at \(b=c\)) toward \(1\). If two axial parameters approach zero while the third stays positive, \(p_4\to1\).

## Assumptions and scope
The plane measure is the **motion-invariant** measure \(d\sigma(u)\,dt\) with a uniformly distributed unit normal \(u\in S^2\) and signed offset \(t\in\mathbb R\), conditioned on
\(\min_{x\in T}\langle u,x\rangle<t<\max_{x\in T}\langle u,x\rangle\).
Here \(\sigma\) is normalized surface area on \(S^2\); this produces a normal distribution biased by the directional width after conditioning. It is *not* the experiment that first samples a uniform normal and then a uniform offset given that normal. The representation with \(u\) and \(-u\) double-counts each unoriented plane by the same constant, which cancels under conditioning. Nongeneric planes through vertices or edges have measure zero. Every remaining section has three or four vertices.

## Proof
**Step 1: section probability from edge intersections.** Let \(N(u,t)\) count the edges of \(T\) properly crossed by the plane \(\langle u,x\rangle=t\). Each crossed edge contributes one vertex to the section, so \(N\in\{3,4\}\) almost surely and \(p_4=\mathbb E N-3\). For an edge vector \(e\), the set of offsets at which the plane crosses it has length \(|\langle u,e\rangle|\). Since \(\int_{S^2}|\langle u,e\rangle|d\sigma(u)=\|e\|/2\), and the measure of planes intersecting \(T\) equals its mean width \(\bar w(T)\),
\[
\mathbb E N=\frac{\frac12\sum_{e\text{ edge}}\|e\|}{\bar w(T)}.
\]
For every convex polyhedron in \(\mathbb R^3\), the classical edge form of the mean-width identity is \(\bar w(T)=(4\pi)^{-1}\sum_e\|e\|\beta_e\), where \(\beta_e\) is its *exterior* dihedral angle. In an equifacial tetrahedron, the six edges come in three opposite equal-length pairs. The displayed formula for \(p_4\) follows.

**Step 2: angles and the differential identity.** The face-normal directions are the four parity-compatible sign patterns of \((1/a,1/b,1/c)\), normalized. The scalar product of normals meeting along an edge in the \(i\)-th opposite pair equals \(2q_i-1\), so the exterior angle is \(\beta_i=\arccos(2q_i-1)=2\arccos\sqrt{q_i}\). Put \(R=\sum_j a_j^{-2}\) and \(Q=q_1q_2q_3\). Direct substitution gives
\[
\ell_i=\frac{2}{\sqrt{RQ}}\sqrt{q_i(1-q_i)},\qquad d\beta_i=-\frac{dq_i}{\sqrt{q_i(1-q_i)}}.
\]
Consequently the Euclidean Schläfli differential identity is verified **directly** in this family:
\[
\sum_{i=1}^3\ell_i\,d\beta_i=-\frac{2}{\sqrt{RQ}}\sum_i dq_i=0.
\]
Define \(S=\sum_i\ell_i\), \(B=\sum_i\ell_i\beta_i\), and the length-weighted exterior angle \(F=B/S\). Because the differential identity implies \(dB=\sum_i\beta_i\,d\ell_i\), the differential of \(F\) on any scale-normalized surface \(S=\mathrm{constant}\) is
\[
 dF=\frac1S\sum_i\beta_i\,d\ell_i.
\]
The map from the positive squared axial parameters to the squared edge-pair lengths is invertible: \(a^2=(\ell_2^2+\ell_3^2-\ell_1^2)/8\), and cyclically. Thus normalized \(\ell_i\) vary freely locally subject to \(\sum_i\ell_i=S\). At any interior stationary point of \(F\), all three \(\beta_i\) must be equal. Since \(\arccos\sqrt{q}\) is strictly decreasing, this forces \(q_1=q_2=q_3=1/3\), equivalently \(a=b=c\). Thus the regular tetrahedron is the **only interior stationary shape**.

**Step 3: the boundary is strictly below the regular angle.** Normalize \(a^2+b^2+c^2=1\) and consider the compact nonnegative closure. At a boundary point with \(a=0\) and \(b,c>0\), \(\beta_1\to0\) and \(\beta_2,\beta_3\to\pi\), while \((\ell_1,\ell_2,\ell_3)\to(2\sqrt{b^2+c^2},2c,2b)\). Therefore
\[
F\longrightarrow \frac{\pi(b+c)}{\sqrt{b^2+c^2}+b+c}
\leq\pi(2-\sqrt2).
\]
The same holds by symmetry on every open boundary edge. At a corner where two axial parameters vanish, the remaining two nonvanishing edge-pair lengths become equal, their exterior angles sum to \(\pi\), and the third edge length vanishes; hence \(F\to\pi/2\), independent of the approaching path. Thus \(F\) extends continuously to the closed parameter simplex and its entire boundary has \(F\leq\pi(2-\sqrt2)\). At the regular tetrahedron, \(F_*=\arccos(-1/3)\), which is strictly larger: indeed \(F_*>3\pi/5>\pi(2-\sqrt2)\). By compactness a maximum of \(F\) exists; it lies in the interior, where the unique stationary shape is regular. Hence \(F\leq F_*\), with equality only for \(a=b=c\). Since \(p_4=2\pi/F-3\), the sharp lower bound and equality condition follow.

**Step 4: the exact range and endpoint behavior.** For every nondegenerate tetrahedron there is a positive-measure set of intersecting planes cutting off a small triangular cap at a vertex; hence \(p_4<1\). The family \(a=b=\varepsilon\), \(c=1\) tends to a segment and satisfies \(F\to\pi/2\), so \(p_4\to1\). The connected positive-parameter shape space, continuity of \(p_4\), and attainment of its lower bound show that every value in the half-open interval occurs. The one-coordinate flattening limit follows by inserting the boundary formula for \(F\) above into \(p_4=2\pi/F-3\).

## Verification
A standalone Python checker, `disphenoid_section_check.py`, computes both the exact edge-normal expression and independent direct counts of crossed tetrahedral edges. It samples 280,000 affine-plane offsets at each of five shapes (1,400,000 plane samples altogether), with width-weighting to implement the invariant conditioned plane measure. It also checks 100,000 additional random shapes against the sharp inequality, probes the one-coordinate boundary formula, and tests the two-coordinate degenerating limit. The checker prints `AFFINE_DISPHENOID_SECTION_OK` after all assertions pass. These finite tests do not certify the all-parameter inequality; that follows from the proof above.

## Relationship to prior work
Finch (2011) analyzes mean widths of regular polyhedra, including the regular tetrahedron; the classical edge formula for mean width is an input here, not claimed new. Affentranger and Schneider (1992) treat orthogonal **projections** of regular simplices, which are distinct from randomly translated **sections**. A published shape diagram for **central** planes through equifacial tetrahedra concerns a different probability distribution: restricting every plane to a fixed center is not equivalent to conditioning motion-invariant affine planes on intersecting the body. The present result concerns global optimization of the full affine-plane section-type probability over every equifacial tetrahedron, not just its regular value.

## Limitations
The theorem does not optimize over all tetrahedra; the equal-opposite-edge constraint is essential. The ambient plane law is translation- and rotation-invariant and conditioned on meeting the body; other sampling laws can give other probabilities. The checker uses finite floating-point experiments and is not a substitute for the analytical proof. Priority over all inaccessible historical mathematical literature has not been independently established.

## References
1. Steven R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671v1, publicly submitted 2011-10-04; https://arxiv.org/abs/1110.0671.
2. Steven R. Finch, *Mean Width of a Regular Simplex*, arXiv:1111.4976v1, publicly submitted 2011-11-21; https://arxiv.org/abs/1111.4976.
3. F. Affentranger and R. Schneider, *Random projections of regular simplices*, Discrete & Computational Geometry 7 (1992), 219–226; DOI:10.1007/BF02187839.
4. T. Andreescu and M. Tetiva, *A Tetrahedron Whose Faces Have Equal Area Is “Equifacial”*, Mathematical Reflections 1 (2021); accessible online text at https://studylib.net/doc/27926774/mr-1-2021-equifacial-tethraedra.
5. R. Schneider, *Inequalities for random flats meeting a convex body*, Journal of Applied Probability (1985), abstract at https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/inequalities-for-random-flats-meeting-a-convex-body/4B74C56ADA001BED13D7E22973FEDB75.
