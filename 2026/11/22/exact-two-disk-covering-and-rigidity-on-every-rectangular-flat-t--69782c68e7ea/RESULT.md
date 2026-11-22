# Exact two-disk covering and rigidity on every rectangular flat torus

## Finding
Let \(a\ge b>0\), let \(T_{a,b}=\mathbb R^2/(a\mathbb Z\times b\mathbb Z)\) carry the quotient Euclidean (intrinsic flat) metric, and let
\[
\rho_2(a,b)=\min_{p,q\in T_{a,b}}\max_{z\in T_{a,b}}
\min\{d(z,p),d(z,q)\}.
\]
Then the exact two-disk covering radius for *arbitrary* centers is
\[
\boxed{\rho_2(a,b)=\frac{a^2+b^2}{4a}.}
\]
**All optimal unordered center pairs** are translations of the pair
\(\{(0,0),(a/2,b/2)\}\) (coordinates are modulo the period lattice). For this pair, put
\[
R=\frac{a^2+b^2}{4a},\qquad h=\frac{a^2-b^2}{4a}.
\]
Its *complete* farthest-point set is
\[
\boxed{\{(R,0),(-R,0),(h,b/2),(-h,b/2)\}\pmod{(a,b)}.}
\]
There are four distinct farthest points when \(a>b\), but only two when \(a=b\).

At fixed torus area \(A=ab\), the **planar lift covering density** (two Euclidean disk areas counted with multiplicity per period cell, divided by \(A\)) is
\[
\delta_2=\frac{2\pi\rho_2(a,b)^2}{ab}
=\frac{\pi(t^2+1)^2}{8t^3},\qquad t=\frac ab\ge1.
\]
It has a **unique minimum** at the rectangular aspect ratio \(t=\sqrt3\), of value
\[
\boxed{\min_{t\ge1}\delta_2(t)=\frac{2\pi}{3\sqrt3}.}
\]
At this ratio the optimal two-site lift in the plane is an equilateral triangular lattice. The minimum density agrees with the classical optimal unrestricted planar congruent-circle covering density; the new rectangular-torus claim is the full exact aspect-ratio profile and uniqueness of its two-center optimizer.

## Assumptions and scope
The torus is the Euclidean quotient, **not** a curved embedded ring torus, and distances are shortest lengths among all lattice lifts. Both centers are unconstrained points on the torus. Equal-radius closed geodesic disks may overlap. The formula is for the complete torus, not a planar rectangle with boundary. The displayed density counts planar lifted disk areas and need not equal the actual sum of areas of *intrinsic torus* balls after they self-wrap. All inequalities include \(a=b\), and the farthest-point set is a set of torus points with repeated representatives identified.

For the standard metric circle \(C_L=\mathbb R/L\mathbb Z\), write \(d_L(u,v)=\min_{k\in\mathbb Z}|u-v+kL|\). The torus metric is
\[
d((x,y),(x',y'))^2=d_a(x,x')^2+d_b(y,y')^2.
\]
For a single disk the sharp radius is \(\rho_1(a,b)=\sqrt{a^2+b^2}/2\). Hence the first two covering-number transitions are exact: the unrestricted covering number is one for \(r\ge\rho_1\), exactly two for \(\rho_2\le r<\rho_1\), and at least three for \(0<r<\rho_2\). No lower-radius covering-number phases are asserted.

## Proof
**Step 1 (unrestricted lower bound by a transverse circle).** Translate an arbitrary candidate first center to \(c_0=(0,0)\). Look at the horizontal metric circle \(F=\{(x,b/2):x\in C_a\}\). Every point of \(F\) is at vertical distance \(b/2\) from \(c_0\). For \(r<b/2\), the first disk misses \(F\), while the second disk intersects \(F\) in an arc of length at most \(2r<a\). It cannot cover \(F\). Thus \(r\ge b/2\) is necessary.

For \(b/2\le r<R=(a^2+b^2)/(4a)\), we have \(r<a/2\) because \(R\le a/2\). The intersection of the first disk with \(F\) has arc half-length \(\sqrt{r^2-b^2/4}\). The second disk's intersection has half-length at most \(r\), regardless of its center. If the two disks covered the torus, their intersections would cover the circle of circumference \(a\), requiring
\[
\sqrt{r^2-b^2/4}+r\ge a/2.
\]
But \(r<a/2\) and squaring after rearrangement give the necessary inequality
\[
r\ge\frac{a^2+b^2}{4a}=R,
\]
a contradiction. Thus \(\rho_2(a,b)\ge R\) for arbitrary centers.

**Step 2 (explicit sharp cover).** Set \(c_0=(0,0)\), \(c_1=(a/2,b/2)\), and \(r=R\). Direct algebra gives
\[
R\ge b/2,\quad R\le a/2,\quad
\sqrt{R^2-b^2/4}=h,\quad R+h=a/2.
\]
Choose any horizontal circle \(y=\text{constant}\); by reflection symmetry let \(0\le y\le b/2\). Its two disk intersections have horizontal half-widths
\[
f(y)=\sqrt{R^2-y^2},\qquad
f(b/2-y)=\sqrt{R^2-(b/2-y)^2}.
\]
The function \(f(u)\) is strictly concave wherever defined (and is continuous at endpoints). Hence \(f(y)+f(b/2-y)\) is strictly concave in \(0<y<b/2\), with endpoint value
\[
f(0)+f(b/2)=R+h=a/2.
\]
Thus the two half-widths sum to at least \(a/2\) for all \(y\). Their horizontal centers are antipodal on \(C_a\), and each half-width is at most \(a/2\). Consequently the two arcs cover every horizontal fiber, proving \(\rho_2(a,b)\le R\). The lower and upper bounds coincide.

**Step 3 (complete equality classification).** Suppose two disks of radius \(R\) cover. Translate one center to \(c_0=(0,0)\), and write the other \(c_1=(s,t)\). On \(F\), the two half-widths are at most \(h\) and \(R\), respectively, with sum at most \(a/2\). The total arc length is at most \(a\), so equality of both upper bounds is necessary. Since the second half-width equals \(R\) only at vertical separation zero, we have \(t=b/2\pmod b\).

If \(a>b\), then \(0<h<R<a/2\). The two arcs on \(F\) have lengths \(2h\) and \(2R\), adding to exactly \(a\). Covering requires their interiors to be disjoint and their endpoints to meet, which forces their center separation to be \(h+R=a/2\). Hence \(s=a/2\pmod a\).

For the square case \(a=b\), we have \(h=0\), \(R=a/2\), and the same fiber argument still forces \(t=b/2\). For any \(0<\varepsilon<b/2\), consider \(z_\varepsilon=(a/2,\varepsilon)\). Its distance from \(c_0\) is \(\sqrt{a^2/4+\varepsilon^2}>R\); therefore it must belong to the second disk. That disk's horizontal half-width on this fiber is \(\sqrt{a\varepsilon-\varepsilon^2}\), so
\[
d_a(s,a/2)\le\sqrt{a\varepsilon-\varepsilon^2}.
\]
Letting \(\varepsilon\downarrow0\) yields \(s=a/2\pmod a\). Thus, also at the square, every optimal pair is a translation of the displayed antipodal half-period pair. Interchanging the two centers does not change the unordered pair.

**Step 4 (exact deepest holes).** The strict concavity in Step 2 makes the arc half-width sum strictly exceed \(a/2\) on every intermediate horizontal fiber. Thus farthest points lie only on \(y=0\) or \(y=b/2\). At \(y=0\), the two arcs of half-widths \(R\) and \(h\) meet precisely at \(x=\pm R\pmod a\). At \(y=b/2\), they meet at \(x=\pm h\pmod a\). Each such meeting point has distance exactly \(R\) from both centers, giving the complete set. At \(a=b\), opposite representatives coincide in each fiber, and no other identifications occur.

**Step 5 (sharp area-normalized aspect ratio).** Put \(t=a/b\ge1\). The area-normalized squared radius is \((t^2+1)^2/(16t^3)\); the density formula follows. Its nonconstant factor is
\[
\frac{(t^2+1)^2}{t^3}=t+\frac2t+\frac1{t^3},\qquad
\frac{d}{dt}=\frac{(t^2-3)(t^2+1)}{t^4}.
\]
Therefore the unique positive aspect-ratio minimizer in \([1,\infty)\) is \(t=\sqrt3\), with density \(2\pi/(3\sqrt3)\). At this ratio the index-two site-lift lattice generated by \((a/2,b/2)\) and \((a/2,-b/2)\) has three equal shortest directions, so its Voronoi cells are regular hexagons and the disk arrangement is the classical triangular covering.

## Verification
The proof is analytic; no computational enumeration is used to infer an all-aspect-ratio or all-center conclusion. Run `python3 checker.py` with only the standard Python library. It checks the exact rational identities for nine aspect ratios, the complete proposed farthest-point contacts, an exact rational \(33\times33\) torus grid per ratio (\(9,801\) point tests), and the density-derivative factorization. The discrete point tests only corroborate the global fiber proof. Full source is included in the accompanying package.

## Relationship to prior work
The metric-product and ball-covering framework was recently formulated by K. Cieliebak and M. Cieliebak, *Covering numbers of metric spaces*, arXiv:2611.15599v1, first public 11 November 2026. Its primary results concern products with the sum metric and small-scale covering inequalities; its full HTML text has no exact rectangular-torus two-center computation. The present theorem concerns the intrinsic Euclidean product metric and exactly two disks.

A. Joós, *On covering the square flat torus by congruent discs*, Australasian Journal of Combinatorics 75(1) (2019), Theorem 1 and its proof, established \(\rho_2(1,1)=1/2\). That is exactly the square endpoint of the present result, and is **not** claimed new. The source does not treat nonsquare rectangular flat tori or equality rigidity.

A previously published mathematical result, *Sharp two-disk covering of all well-rounded flat tori* (published-finding corpus identifier `2026/11/1/SCOPE-sharp-two-disk-covering-of-all-well-rounded-flat-tori--559d72822a1a`, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-two-disk-covering-of-all-well-rounded-flat-tori--559d72822a1a), proves \(\rho_2=L/2\) for well-rounded planar period lattices. Its full `RESULT.md` was inspected. An orthogonal period lattice with \(a>b\) has only one shortest-vector direction and therefore is *not well-rounded*. The earlier theorem and this one overlap at the square only. The present all-aspect-ratio formula is strictly greater than the systolic bound \(b/2\) when \(a>b\), and its equality-location and fixed-area conclusions are not implied by the earlier theorem.

Brandt et al., *Optimal Packings of Two to Four Equal Circles on Any Flat Torus*, arXiv:1708.05395, solve **packing**, not unrestricted equal-disk covering. Classical planar triangular disk-covering optimality supplies the universal density lower bound but not the explicit constrained-radius profile or center rigidity for each fixed rectangular torus.

## Limitations
The classification is only for *rectangular* period lattices, exactly two equal geodesic disks, and the intrinsic quotient Euclidean distance. It does not solve arbitrary oblique flat-torus shapes, any number of disks greater than two, or disk coverings of an ordinary bounded rectangle. The classical triangular density minimum is contextual and not asserted as a new planar covering theorem. The searched prior literature and indexed findings do not certify absolute historical priority; unindexed treatments of two-point periodic coverings remain a specific residual risk. The provided finite checks are not a substitute for the all-center proof.

## References
1. K. Cieliebak and M. Cieliebak, *Covering numbers of metric spaces*, arXiv:2611.15599v1 (first public 2026-11-11), https://arxiv.org/html/2611.15599v1.
2. A. Joós, *On covering the square flat torus by congruent discs*, Australasian Journal of Combinatorics 75(1) (2019), 113–126, https://ajc.maths.uq.edu.au/pdf/75/ajc_v75_p113.pdf.
3. *Sharp two-disk covering of all well-rounded flat tori*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-two-disk-covering-of-all-well-rounded-flat-tori--559d72822a1a.
4. M. Brandt, W. Dickinson, A. Ellsworth, J. Kenkel, H. Smith, *Optimal Packings of Two to Four Equal Circles on Any Flat Torus*, arXiv:1708.05395 (first public 2017-08-17), https://arxiv.org/abs/1708.05395.
5. D. Protasov, A. Tolmachev, V. Voronov, *Optimal partitions of the flat torus into parts of smaller diameter*, arXiv:2402.03997 (first public 2024-02-06), https://arxiv.org/abs/2402.03997.
