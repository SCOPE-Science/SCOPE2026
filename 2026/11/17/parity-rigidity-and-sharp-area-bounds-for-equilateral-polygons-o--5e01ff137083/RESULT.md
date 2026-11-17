# Parity rigidity and sharp area bounds for equilateral polygons on a regular radial grid

## Finding
Let \(n\ge 3\) be an integer, \(\ell>0\), and \(\Delta=2\pi/n\). Suppose the vertices of a strictly convex counterclockwise \(n\)-gon, indexed cyclically, are
\[
 p_i=r_i(\cos(\theta_0+i\Delta),\sin(\theta_0+i\Delta)),\quad r_i>0,
\]
and every side has Euclidean length \(\ell\). Then \(r_{i+2}=r_i\) for every \(i\). Consequently, for odd \(n\), the polygon is the unique regular \(n\)-gon of side \(\ell\) on these prescribed rays. For even \(n\), every solution is a two-radius polygon, and all such solutions are parametrized exactly as follows. Set \(\kappa=\cos\Delta\), choose \(t\) in \((\kappa,\kappa^{-1})\) when \(n\ge6\), or \(t\in(0,\infty)\) when \(n=4\), and put
\[
 b=\frac{\ell}{\sqrt{t^2+1-2\kappa t}},\qquad a=tb,
\]
with \(r_{2j}=a\), \(r_{2j+1}=b\). These are all the strictly convex solutions, with no further constraints.

The area \(A\) of an even-order solution has the full sharp range
\[
 \frac{n\ell^2}{2}\cot\frac{2\pi}{n}<A\le\frac{n\ell^2}{4}\cot\frac{\pi}{n}.
\]
Equality on the right occurs only for the regular polygon; the left endpoint is the strict infimum and occurs only in the excluded weakly convex limit. For \(n=4\), the left endpoint is interpreted as zero. For odd \(n\), the area is exactly the regular-polygon value on the right. In the even case \(n\ge6\), the two boundary limits contract alternately onto regular \(n/2\)-gons of side \(2\ell\), with the other vertices at their edge midpoints.

## Assumptions and scope
The origin and the rays are fixed, with equal successive angular spacing \(2\pi/n\); vertex positions must have strictly positive radii, follow the indicated cyclic order, and form a strictly convex polygon. The side length \(\ell\) is fixed. No cyclicity (equal circumradii) or equiangularity of the polygon itself is assumed. A polygon having just the same *unoriented* set of directions, without an ordered correspondence, is not covered. The ray offset \(\theta_0\) only rotates the configuration.

## Proof
**1. Triangle-angle recurrence.** Work with the triangles \((0,p_i,p_{i+1})\), which are nondegenerate since \(0<\Delta<\pi\) and all radii are positive. Let \(\alpha_i\in(0,\pi-\Delta)\) denote the triangle angle at \(p_{i+1}\), opposite radius \(r_i\). The law of sines, with side \(\ell\) opposite \(\Delta\), gives
\[
 r_i=\frac{\ell\sin\alpha_i}{\sin\Delta},\qquad
 r_{i+1}=\frac{\ell\sin(\alpha_i+\Delta)}{\sin\Delta}.
\]
Matching two expressions for \(r_i\) yields \(\sin\alpha_i=\sin(\alpha_{i-1}+\Delta)\). Both angles lie in \((0,\pi)\), so at each vertex precisely one of the following holds (possibly both at their common value):
\[
 \mathrm R:\ \alpha_i=\alpha_{i-1}+\Delta,\qquad
 \mathrm F:\ \alpha_i=\pi-\Delta-\alpha_{i-1}.
\]
The interior angle of the polygon at \(p_i\) is \(\gamma_i=\pi-\Delta+\alpha_{i-1}-\alpha_i\). An R transition gives \(\gamma_i=\pi-2\Delta\), while an F transition gives \(\gamma_i=2\alpha_{i-1}\). In particular, any F transition in a strictly convex polygon has \(\alpha_{i-1}<\pi/2\).

**2. All transitions are reflections.** For \(n=3,4\), the R value \(\pi-2\Delta\) is nonpositive, contradicting strict convexity. For \(n\ge5\), take a global minimum \(\alpha_j\) of the finite cyclic sequence. Its incoming transition cannot be R, as that would make its predecessor smaller. Thus it is F, and \(\alpha_j=\pi-\Delta-\alpha_{j-1}>\pi/2-\Delta\). Every \(\alpha_i\) is therefore greater than \(\pi/2-\Delta\). If any transition were R, its output would exceed \(\pi/2\). An F transition cannot start from such an output because its corresponding interior angle would be at least \(\pi\); hence the next transition must again be R. Inductively R transitions would continue forever, increasing the cyclic angle sequence by the strictly positive amount \(\Delta\), an impossibility. Therefore every transition is F. At any ambiguity where R and F coincide, its output is \(\pi/2\); the same next-step argument prohibits that ambiguity in a closed strictly convex configuration. Hence \(\alpha_{i+2}=\alpha_i\), and the sine-law formulas imply \(r_{i+2}=r_i\).

**3. Classification and convexity.** Odd cyclic length forces all radii equal. Since \(\ell=2r\sin(\pi/n)\), the radius is uniquely \(\ell/[2\sin(\pi/n)]\). At even length, write the alternating radii as \(a,b>0\). The cosine law on successive rays gives \(\ell^2=a^2+b^2-2\kappa ab\). The signed turn at a vertex of radius \(a\) is proportional to \(a-\kappa b\), and at radius \(b\) to \(b-\kappa a\): indeed the cross product of its incident directed edges equals \(2\sin\Delta\,b(a-\kappa b)\) at radius \(a\), with the analogous expression at radius \(b\). Therefore strict convexity is equivalent to \(a>\kappa b\) and \(b>\kappa a\). These conditions and the cosine law give the stated full parametrization. Because the positive radial vertices occur in angular order with gaps less than \(\pi\), their boundary is simple, and strictly positive local turns imply global strict convexity.

**4. Sharp area interval.** The shoelace formula gives \(A=(n/2)ab\sin\Delta\). In terms of \(t=a/b\),
\[
 A(t)=\frac{n\ell^2\sin\Delta}{2}\frac{t}{t^2+1-2\kappa t},\quad
 A'(t)=\frac{n\ell^2\sin\Delta}{2}\frac{1-t^2}{(t^2+1-2\kappa t)^2}.
\]
The unique maximum occurs at \(t=1\) and is \(n\ell^2\cot(\pi/n)/4\). For \(n\ge6\), the minimum is approached as \(t\downarrow\kappa\) or \(t\uparrow1/\kappa\), where its value is \(n\ell^2\cot\Delta/2\); for \(n=4\), the limiting value as \(t\to0\) or infinity is zero. Neither lower endpoint is attained under strict convexity. Continuity gives every intermediate area. At \(t=\kappa\) the smaller-radius vertices fall at the midpoints of the chords joining consecutive larger-radius vertices; those chords have length \(2\ell\), giving the asserted collapsed regular \(n/2\)-gon. The other limiting branch interchanges the two parities. This completes the proof.

## Verification
The accompanying `verify.py` independently computes consecutive edge lengths, every signed turn, signed polygon area, and the sharp area endpoints over many dimensions and admissible parameters. It also checks symbolic cosine-law and derivative identities with SymPy when installed. These checks test formulas and boundaries; the recurrence argument above is the proof for all integers \(n\).

## Relationship to prior work
Baumann, Biedl, Elashmawi, Fink, Saumell, and Schulz, *On Reconstructing a Convex Polygon from Partial Information* (arXiv:2607.01423v1, publicly released 2026-07-01), §D.3.3, discuss the difficulty of prescribing edge lengths and corner-ray directions together. Their hardness theorem concerns a different cylinder model; their discussion does not give the all-orders equal-length/equal-angular-ray classification or area range above. Other studied polygon rigidity conditions include the bicycle-polygon condition requiring equal neighbor diagonals, which is not implied by fixed radial directions. Search comparisons and residual priority risks appear in the separate review document.

## Limitations
The theorem assumes strict convexity and evenly spaced **vertex directions** measured from a fixed interior origin. It does not classify arbitrary length lists, unequally spaced rays, nonconvex chains, or degenerate limiting polygons. No computational complexity statement for general polygon reconstruction follows. Historical priority is provisional: differently phrased older literature on polar equilateral polygons might contain an equivalent assertion.

## References
1. A. Baumann, T. Biedl, M. Elashmawi, S. D. Fink, M. Saumell, A. Schulz, *On Reconstructing a Convex Polygon from Partial Information*, arXiv:2607.01423v1 (2026-07-01), especially Appendix D.3.3. https://arxiv.org/abs/2607.01423
2. *Equilateral polygon*, standard definitions and classical examples, https://en.wikipedia.org/wiki/Equilateral_polygon (background only; not evidence of originality).
