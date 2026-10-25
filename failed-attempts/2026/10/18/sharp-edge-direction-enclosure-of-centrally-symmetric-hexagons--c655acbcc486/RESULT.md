# Sharp edge-direction enclosure of centrally symmetric hexagons

## Finding
For every centrally symmetric convex hexagon \(H\) with six genuine vertices, let \(q_{\mathrm{ch}}(H)\) be the least area of a convex containing polygon with at most four sides, each parallel to a segment connecting two vertices of \(H\). Let \(E(H)\) be the least area of a circumscribed parallelogram whose two edge directions occur among the three edge directions of \(H\). Then
\[
q_{\mathrm{ch}}(H)\le E(H)\le\frac43\operatorname{area}(H),
\]
with equality in the second inequality if and only if \(H\) is affine-regular. The first inequality is **not** asserted to be equality in general. The constant \(4/3\) for \(q_{\mathrm{ch}}\) is sharp, and \(q_{\mathrm{ch}}(H)=4\operatorname{area}(H)/3\) if and only if \(H\) is affine-regular.

The exact optimizer and anisotropy law are as follows. Represent \(H\), up to translation, by the planar zonotope
\[
H=[-u/2,u/2]+[-v/2,v/2]+[-w/2,w/2],
\]
with three nonzero pairwise nonparallel vectors in cyclic order of edge directions. Put
\[
D_{uv}=|\det(u,v)|,\quad D_{uw}=|\det(u,w)|,\quad D_{vw}=|\det(v,w)|,
\]
and sort these three positive values as \(\alpha\le\beta\le\gamma\). Write \(S=\alpha+\beta+\gamma\). Then
\[
\boxed{E(H)=S+\frac{\alpha\beta}{\gamma},\qquad
\frac43-\frac{E(H)}{S}=\frac{\gamma S-3\alpha\beta}{3\gamma S}.}
\]
A minimizing edge-direction pair is exactly a pair attaining determinant magnitude \(\gamma\); ties give all minimizers. Thus this is a complete sharp formula and optimizer classification for this natural direction-restricted enclosure invariant.

## Assumptions and scope
A genuine centrally symmetric hexagon has exactly three nonparallel edge directions; the three vectors \(u,v,w\) are the corresponding oriented edge vectors, each taken once from opposite pairs. Translation of \(H\) does not affect any quantity. Areas are ordinary positive Euclidean areas. A chord connects two vertices, so each edge direction is automatically a chord direction. No claim is made for arbitrary nonsymmetric hexagons, polygons with more than six vertices, or a formula for unrestricted minimal circumscribed quadrilaterals.

The same sharp chord bound holds for every planar convex *one-fold translative tile*: by Fedorov's classification such a tile is a parallelogram (for which \(q_{\mathrm{ch}}=S\)) or a centrally symmetric hexagon. This is a corollary of the single hexagonal enclosure theorem, not a separate assertion of novelty.

## Proof
**1. Zonotope and area.** A centrally symmetric convex hexagon has three pairs of equal and parallel opposite edges. Taking one edge vector from each pair gives the displayed Minkowski-sum representation, up to translation. Tiling this zonotope by the three pairwise generator parallelograms, or applying the shoelace identity to the six vertices, gives
\[
\operatorname{area}(H)=D_{uv}+D_{uw}+D_{vw}=S.
\]
All three determinant magnitudes are positive because \(H\) has six genuine vertices.

**2. Exact area for prescribed edge directions.** Fix \(u,v\). Express \(w=s u+t v\). Then
\[
|s|=D_{vw}/D_{uv},\qquad |t|=D_{uw}/D_{uv}.
\]
In the basis \((u,v)\), the zonotope has coordinate widths \(1+|s|\) and \(1+|t|\). The unique smallest containing parallelogram with sides parallel to \(u,v\) is its coordinate bounding box, of area
\[
E_{uv}=D_{uv}(1+|s|)(1+|t|)
=S+\frac{D_{uw}D_{vw}}{D_{uv}}.
\]
This box is centrally located at the symmetry centre, and all four boundary lines support \(H\). Its four edge directions are edge (hence chord) directions of \(H\). Cyclically permuting \(u,v,w\) gives all three permitted pairs. Let \(T=D_{uv}D_{uw}D_{vw}\). For a pair with determinant value \(D\), the excess is \(T/D^2\); the minimum therefore occurs precisely when \(D=\gamma\). It equals \(T/\gamma^2=\alpha\beta/\gamma\), proving the exact formula and all optimizer directions.

**3. Sharp inequality and rigidity.** Since \(0<\alpha\le\beta\le\gamma\),
\[
\gamma(\alpha+\beta+\gamma)
\ge\beta(\alpha+2\beta)
\ge3\alpha\beta.
\]
The first equality forces \(\gamma=\beta\); the second forces \(\beta=\alpha\). It follows that \(E(H)/S\le4/3\), with equality exactly when the three determinant magnitudes are equal. If they are equal, make an invertible linear change of coordinates sending \(u,v\) to the coordinate unit vectors. The remaining vector \(w\) has two coordinate magnitudes equal to one, so the resulting zonotope is an affine image of the standard regular hexagon. Conversely, that standard hexagon has three equal determinant magnitudes.

**4. Sharpness for chord quadrilaterals.** An affine-regular hexagon admits the edge-direction parallelogram of area \(4S/3\). For the reverse inequality it suffices by affine invariance to use the six vertices
\[
(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1),
\]
of area \(S=3\). These vertices have six unoriented chord directions and hence twelve outward support-line normals. Every chord triangle or quadrilateral containing this hexagon can be moved inward one supporting side at a time without increasing area, until each side is a support line. Thus it suffices to check all \(\binom{12}{3}+\binom{12}{4}=715\) sets of three or four support halfplanes. The supplied `verify_hexagon.py` carries out this complete finite verification using rational arithmetic, intersecting each candidate with the fixed square \([-100,100]^2\). The smallest clipped area is exactly \(4\). The square contains the hexagon, and clipping can only decrease area, so every bounded chord quadrilateral or triangle has area at least \(4\). The constructed edge-direction parallelogram has area exactly \(4\); hence \(q_{\mathrm{ch}}=4=4S/3\). Affine invariance transfers this equality to every affine-regular hexagon. Combining with the strict inequality of Step 3 gives the claimed if-and-only-if equality classification.

## Verification
Run `python3 verify_hexagon.py` using the included standalone standard-library script. It reports the twelve exact support normals, checks all 715 candidate support systems by fractional polygon clipping, and confirms the sharp area \(4\) of the reference hexagon of area \(3\). The exhaustive finite check is used only for this fixed six-vertex reference configuration. The all-hexagon formula, bound, and equality implication are proved algebraically in Steps 1–3, not extrapolated from samples. The finite certificate is independently replayable with no network or nonstandard Python packages.

## Relationship to prior work
V. Vígh's 2026 chord-conjecture paper defines \(q_{\mathrm{ch}}\), formulates its \(3/\sqrt5\) bound for all polygons, proves the general \(\sqrt2\) chord-quadrilateral estimate and the pentagon case, and notes \(q_{\mathrm{ch}}=4S/3\) at the affine-regular hexagon. It does not prove this sharp inequality for all centrally symmetric hexagons or the complete edge-direction determinant profile. C. M. Petty's earlier theorem, as cited in the full texts of Vígh and Fodor–Grundbacher, bounds the minimum **unrestricted-direction** circumscribed parallelogram of any centrally symmetric convex body by \(4S/3\); the classic result does not itself impose chord directions. The additional discrete-direction restriction, exact optimizer selection, and strict determinant deficit are the distinct statements here. Fodor and Grundbacher discuss the unrestricted quadrilateral problem and quote Petty's equality classification.

## Limitations
This is a sharp special case of the chord conjecture for centrally symmetric hexagons and planar one-fold translative tiles; it does not prove the all-polygon conjecture. The formula concerns **edge-direction parallelograms**, not the unrestricted or full chord-quadrilateral optimum for arbitrary hexagons; that distinction is essential. The classical 1955 paper of Petty was not available for direct full-text comparison, so older equivalent edge-constrained statements remain a literature risk. The mathematical claim has undergone self-review only; no independent scientific audit has been performed.

## References
1. V. Vígh, *A note on Kuperberg's quadrilateral conjecture*, arXiv:2610.08168v1, first public 6 October 2026, https://arxiv.org/html/2610.08168v1 (Sections 1–2, 4–5).
2. F. Fodor and F. Grundbacher, *On the minimal area of quadrangles circumscribed about planar convex bodies*, arXiv:2506.05185, https://arxiv.org/html/2506.05185 (Introduction and section 2).
3. C. M. Petty, *On the geometry of the Minkowski plane*, Riv. Mat. Univ. Parma 6 (1955), 269–292 (historical result quoted by references 1–2; original full text not inspected).
4. Q. Yang and C. Zong, *Multiple Translative Tilings in Euclidean Spaces*, arXiv:1711.02514 (background on Fedorov's planar classification).
