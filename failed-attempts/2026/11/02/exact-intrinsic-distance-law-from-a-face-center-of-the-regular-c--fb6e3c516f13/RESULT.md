# Exact intrinsic distance law from a face center of the regular cube

## Finding
Let \(Q=[0,1]^3\), give its two-dimensional boundary \(\partial Q\) the intrinsic Euclidean shortest-path length metric \(d\), fix the center \(o=(1/2,1/2,1)\) of its upper face, and let \(X\) be uniformly distributed with respect to boundary surface area. Write \(R=d(o,X)\). The complete cumulative distribution \(F(r)=\Pr(R\le r)\) is the explicit piecewise elementary function
\[
F(r)=\frac{T(r)+4S(r)+B(r)}6,
\]
where \(T,S,B\) are the following normalized *areas of intrinsic radius-\(r\) balls in one top, side, or bottom unit-square face*. For \(r>0\) and \(0\le t\le r\), put
\[
H_r(t)=\frac{t\sqrt{r^2-t^2}+r^2\arcsin(t/r)}2.
\]
The top-face area is
\[
T(r)=\begin{cases}
0,&r<0,\\
\pi r^2,&0\le r\le1/2,\\
\pi r^2-4r^2\arccos(1/(2r))+2\sqrt{r^2-1/4},&1/2<r<1/\sqrt2,\\
1,&r\ge1/\sqrt2.
\end{cases}
\]
The side-face area is
\[
S(r)=\begin{cases}
0,&r\le1/2,\\
2[H_r(r)-H_r(1/2)],&1/2<r\le1/\sqrt2,\\
\sqrt{r^2-1/4}-1/2+2[H_r(r)-H_r(\sqrt{r^2-1/4})],&1/\sqrt2<r\le3/2,\\
\sqrt{r^2-1/4}-1/2+2[H_r(3/2)-H_r(\sqrt{r^2-1/4})],&3/2<r<\sqrt{5/2},\\
1,&r\ge\sqrt{5/2}.
\end{cases}
\]
For \(\sqrt{5/2}<r<2\) write \(s_r=(-1+\sqrt{2r^2-4})/2\). The bottom-face area is
\[
B(r)=\begin{cases}
0,&r\le3/2,\\
8[H_r(r)-H_r(3/2)],&3/2<r\le\sqrt{5/2},\\
8\bigl[s_r/2-s_r^2/2+H_r(r)-H_r(3/2+s_r)\bigr],&\sqrt{5/2}<r<2,\\
1,&r\ge2.
\end{cases}
\]
The expressions coincide at every branch boundary. The support is exactly \([0,2]\); its maximum \(2\) is attained only at the center of the opposite face.

Every even moment is rational and explicitly evaluable by a fixed finite polynomial integral. In particular,
\[
\mathbb E R^2=\frac{23}{18},\qquad
\mathbb E R^4=\frac{451}{180},\qquad
\mathbb E R^6=\frac{331}{56},\qquad
\mathbb E R^8=\frac{389423}{25200}.
\]
The upper-tail expansion is
\[
\Pr(R>2-\varepsilon)
=\frac23\varepsilon^2+\frac19\varepsilon^3+O(\varepsilon^4)
\quad (\varepsilon\downarrow0).
\]

## Assumptions and scope
The entire closed cube surface (including edges and vertices) carries the induced intrinsic length metric, not the ambient Euclidean chord metric and not the graph metric on the edges. The sampled target has the *normalized* area measure of all six faces, each of area one. The source is one chosen face center; cube isometries give the same result for each of the other five face centers. Formula boundaries include equality as specified; edge/vertex point sets have zero sampling measure and the intrinsic distance extends to them by continuity. All formulas refer to unit edge length; for edge length \(a>0\), the distance variable scales by \(a\), the even moment by \(a^{2k}\), and the upper-tail distance by \(a\).

## Proof
**1. Exact distance reduction.** On the top face, with coordinates \((x,y,1)\), the squared geodesic distance from \(o\) is \((x-1/2)^2+(y-1/2)^2\). On the side face \(x=0\), with coordinates \((0,y,z)\), it is \((y-1/2)^2+(3/2-z)^2\), and the other side faces follow by quarter-turn symmetry. On the bottom face, with coordinates \((x,y,0)\), it is the minimum of the squared Euclidean distances to the four unfolded source images
\[
(-3/2,1/2),\quad(5/2,1/2),\quad(1/2,-3/2),\quad(1/2,5/2).
\]
Each of these four candidate segments crosses, in order and within the square edges, the source face, one side face, and the bottom face, so is a genuine surface path. The side candidate similarly crosses exactly the top and side face.

For the reverse inequality, a shortest path cannot pass through a positively curved cube vertex in its interior and cannot visit a face twice (the elementary non-repetition property of shortest paths on convex polyhedra). Hence every path has a simple sequence of faces. Developing its successive faces gives an unfolded straight-segment length, which is a lower bound for the length of that path. The six-face adjacency graph has exactly \(28\) simple sequences from the top face to the bottom face and \(26\) from the top to a fixed side face. The accompanying exact-rational verifier enumerates all such sequences, generates their unfolded source images, and proves that each candidate's squared length is at least one of the four bottom candidates (or the direct side candidate), at **all points** of the target square. Indeed the difference of two squared distances from constant image points is an affine function of the target coordinates; checking its four corners with exact fractions proves it nonnegative everywhere. Since all possible simple face sequences are covered, this is an exhaustive finite certificate, not a test on finitely many sampled target points. It proves the claimed pointwise formulas for every target by continuity, including face boundaries.

**2. Face-area formula.** On the top square \([-1/2,1/2]^2\), the radius-\(r\) ball area is a disk-square intersection, giving \(T\). On any side square its target plane has \(u\in[-1/2,1/2]\) and \(t\in[1/2,3/2]\), and the squared distance is \(u^2+t^2\). Thus
\[
S(r)=2\int_{1/2}^{3/2}\min\{1/2,\sqrt{(r^2-t^2)_+}\}\,dt
\]
with the implicit restriction to \(t\le r\); solving the saturation threshold \(t=\sqrt{r^2-1/4}\) and integrating with primitive \(H_r\) gives the listed pieces. On the bottom square, the four-source distance is invariant under its dihedral group. In eight triangular sectors it reduces to
\[
(x+3/2)^2+(y-1/2)^2,
\quad 0\le x\le y\le1/2.
\]
Put \(s=x\) and \(t=1/2-y\); the sector becomes \(0\le s\le1/2\), \(0\le t\le1/2-s\). Consequently
\[
B(r)=8\int_0^{1/2}
\min\left\{1/2-s,\sqrt{(r^2-(3/2+s)^2)_+}\right\}ds.
\]
The integrand is zero when \(3/2+s>r\). For \(r\le\sqrt{5/2}\) the circular arc alone supplies the active bound; for larger \(r\) the switch with the triangular upper edge is at \(s=s_r\), obtained by equating their squares. The primitive \(H_r\) yields the stated \(B\) pieces. The six faces have area one, so the normalized CDF is \((T+4S+B)/6\). These integral derivations also show continuity at all transition radii.

**3. Moments, support, and tail.** For integer \(k\ge0\), exact integration gives
\[
\begin{aligned}
6\mathbb E R^{2k}={}&\int_{-1/2}^{1/2}\!\int_{-1/2}^{1/2}(u^2+v^2)^k\,du\,dv\\
&+4\int_{-1/2}^{1/2}\!\int_{1/2}^{3/2}(u^2+t^2)^k\,dt\,du\\
&+8\int_0^{1/2}\!\int_0^y\bigl((x+3/2)^2+(y-1/2)^2\bigr)^k\,dx\,dy.
\end{aligned}
\]
All integrands are rational-coefficient polynomials integrated over rational polytopes, proving rationality for every even moment. Expanding binomials and integrating monomials produces the four tabulated exact values; a stand-alone exact-fraction implementation is included. The maximum over the top face is \(1/\sqrt2\), the sides \(\sqrt{5/2}\), and the bottom \(2\), reached only where all four bottom source distances are \(2\), i.e., at the opposite face center.

For the tail, write opposite-face coordinates about the center and let \(m=\max(|u|,|v|)\), \(n=\min(|u|,|v|)\). Then \(R^2=(2-m)^2+n^2\). Writing \(n=mt\) with \(0\le t\le1\), the inequality \(R>2-\varepsilon\) is \(m<\rho_\varepsilon(t)\), where
\[
\rho_\varepsilon(t)=\frac{2-\sqrt{4-(1+t^2)(4\varepsilon-\varepsilon^2)}}{1+t^2}
=\varepsilon+\frac{t^2}4\varepsilon^2+O(\varepsilon^3).
\]
For sufficiently small positive \(\varepsilon\), this lies in the bottom-face sector, so the total tail area is \(4\int_0^1\rho_\varepsilon(t)^2dt\). Dividing by the entire surface area six gives precisely \((2/3)\varepsilon^2+(1/9)\varepsilon^3+O(\varepsilon^4)\).

## Verification
Run `python3 verify_cube_geodesic_law.py` using Python 3 and only its standard library. The checker independently builds the six-face adjacency graph and square developments; enumerates exactly \(28\) bottom-target and \(26\) side-target simple face sequences; certifies candidate dominance using exact rational four-corner inequalities; and evaluates even moments through order eight using exact fractions. It also probes the CDF on \(3001\) radii and compares it against \(180000\) reproducible random surface targets (maximum observed empirical CDF deviation approximately \(0.001375\)). Exhaustive finite path enumeration plus exact affine dominance, not the random sampling, supports the global shortest-path claim. The analytical integrations and asymptotic Taylor expansion are displayed above; numerical tests do not substitute for these arguments.

## Relationship to prior work
Goldstone, Roca and Suzzi Valli (2020, Section 4.3) **already prove** that from an opposite-face center every shortest path may be chosen to traverse three faces. That paper also gives the relevant unfolding image geometry. The pointwise shortest-path reduction is **not claimed novel here**. Their probabilistic question is the frequency of three-face versus four-face minimizers as the *source varies*, not the distribution of intrinsic **distance magnitude** to a target drawn uniformly over all six faces. Davis and collaborators (2015) investigate geodesic trajectories from vertices; Davis and Guo (2023) classify cut-locus types; and Davis (2023) determines the geodesic motion-planning complexity of the cube. None of their inspected statements evaluates this marked-face-center distance CDF, even-moment sequence, and sharp terminal-tail expansion. Mathai, Moschopoulos, and Pederzoli (1999) evaluate distributions of **ambient Euclidean distances** for assorted random point pairs in a cube, which is a different metric/endpoint model. Yang (2023) studies long-time geodesic flow equidistribution rather than shortest distances from a fixed source. Novelty is confined to the complete evaluated intrinsic-distance law and its moment/tail consequences.

## Limitations
The finding concerns a source fixed at a face center, not general sources, arbitrary pairs of random surface points, or noncubic rectangular boxes. Its exact shortest-path ingredients have substantial precedent. The comparison of the full accessible relevant papers and record searches supports—but cannot certify—historical priority for the integrated distribution; other earlier evaluations or unindexed sources could exist. The complete analytical proof of the distribution is self-contained modulo the standard non-repeated-face property, itself justified for shortest paths on convex polyhedra by elementary straightening. Independent external assessment has not been performed.

## References
- D. Davis, V. Dods, C. Traub, J. Yang, *Geodesic trajectories on regular polyhedra* (first posted 2015-08-12), https://arxiv.org/abs/1508.03546 .
- R. Goldstone, R. Roca, R. Suzzi Valli, *Shortest Paths on Cubes* (first posted 2020-03-13), https://arxiv.org/abs/2003.06096 .
- D. M. Davis, M. Guo, *Isomorphism classes of cut loci for a cube* (first posted 2023-01-26), https://arxiv.org/abs/2301.11366 .
- D. M. Davis, *Geodesic complexity of a cube* (first posted 2023-08-08), https://arxiv.org/abs/2308.04316 .
- A. M. Mathai, P. Moschopoulos, G. Pederzoli, *Distance between random points in a cube* (1999), https://doi.org/10.6092/issn.1973-2201/1104 .
- Y. Yang, *The distribution of geodesics on the cube surface* (2023), https://doi.org/10.1112/mtk.12188 .
