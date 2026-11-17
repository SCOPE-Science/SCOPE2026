# Homology recovery from intersection counts of random shortest geodesics on rectangular flat tori

## Finding

Let \(T=\mathbb R^2/(L_x\mathbb Z\oplus L_y\mathbb Z)\) be an orthogonal Euclidean flat two-torus, with arbitrary \(L_x,L_y>0\). Fix the embedded closed geodesic \(C_{p,q}\) of primitive integral homology \((p,q)\ne(0,0)\), with \(\gcd(|p|,|q|)=1\). Choose independent Haar-area-uniform points \(A,B\in T\), join them by the uniquely minimizing geodesic \(G_{A,B}\), and let \(N\) be its number of transverse interior intersections with \(C_{p,q}\). All choices are well-defined almost surely. Set \(a=\max(|p|,|q|)\), \(b=\min(|p|,|q|)\).

**Complete count law.** Let \(X,Y\) be independent uniform variables on \((-1/2,1/2)\), and let \(U\) be an independent uniform variable on \((0,1)\). Then
\[
N\ \overset{d}{=}\ \big|\lfloor U+qX-pY\rfloor\big|.
\]
Equivalently, conditional on \(W=|qX-pY|=w\), \(N\) takes the values \(\lfloor w\rfloor\) and \(\lfloor w\rfloor+1\) with probabilities \(1-\{w\}\) and \(\{w\}\), respectively. For \(b>0\), \(W\) has density
\[
g_{a,b}(w)=\begin{cases}
2/a,&0<w<(a-b)/2,\\
(a+b-2w)/(ab),&(a-b)/2<w<(a+b)/2,\\
0,&\text{otherwise}.
\end{cases}
\]
For \(b=0\), its density is \(2/a\) on \((0,a/2)\), zero elsewhere. Thus every atom of the complete count distribution is the integral of an explicit piecewise-linear hat function against \(g_{a,b}\), and is rational.

**Moments and inverse.** The first two raw moments are
\[
\boxed{\ \mu:=\mathbb EN=\frac{3a^2+b^2}{12a},\qquad
\nu:=\mathbb EN^2=\frac{a^2+b^2+2}{12}.\ }
\]
Neither moment nor the complete law depends on the metric aspect ratio \(L_x/L_y\). More strikingly, **the single exact mean \(\mu\) recovers the entire unordered primitive homology pair**: if \(d\) denotes the positive denominator of the reduced rational number \(12\mu\), then
\[
\boxed{a=d,\qquad b=\sqrt{d(12\mu-3d)}.}
\]
The first *two* moments also give a continuous algebraic recovery formula without rational-denominator extraction:
\[
\boxed{a=3\mu+\sqrt{9\mu^2-(12\nu-2)/2},\qquad b=\sqrt{12\nu-2-a^2}.}
\]
In particular, \(R=(12\nu-2)/\mu^2\) is independent of the overall homology magnitude and obeys the sharp bounds \(16\le R\le18\). Writing \(r=b/a\in[0,1]\), its exact profile is \(R=144(1+r^2)/(3+r^2)^2\), strictly increasing for \(0<r<1\). Thus the two moments continuously determine the magnitude ratio, whereas the one-moment inverse uses primitivity and exact arithmetic. Only coordinate signs, orientation, and interchange of the axes are invisible in this symmetric sampling experiment.

## Assumptions and scope

The torus has its intrinsic quotient Euclidean metric and orthogonal side periods \(L_x,L_y>0\). The closed target curve \(C_{p,q}\) is parametrized by \(t\mapsto(L_xpt,L_yqt)\bmod(L_x,L_y)\), \(0\le t<1\), and is embedded because \((p,q)\) is primitive. The arc endpoints are independent Haar-uniform points and joined by the shortest intrinsic geodesic. Non-uniqueness, tangencies, endpoints on the target curve, and endpoint collisions are null events. Intersection count refers to geometric transverse intersections in the open geodesic segment, not algebraic signed intersections. The measured mean is assumed exact in the one-moment inverse; noisy finite samples cannot recover integer denominators without additional assumptions. There is no claim for nonorthogonal lattices or other sampling laws.

## Proof

**1. Geodesic displacement and a phase map.** Identify \(T\) with normalized coordinates \(\mathbb R^2/\mathbb Z^2\), equipped with metric \(L_x^2dx^2+L_y^2dy^2\). By independence and Haar invariance, the minimizing displacement \((X,Y)\) of \(A\) to \(B\) has independent \(\operatorname{Unif}(-1/2,1/2)\) coordinates, independent of its starting point \(A\). This is because the centered rectangular Voronoi cell is the fundamental square in normalized coordinates for every positive pair of side lengths. The primitive target curve is exactly the zero set modulo one of the torus character
\[
\phi(x,y)=qx-py\pmod1.
\]
Primitivity ensures this zero set is one connected closed embedded geodesic. Since \(A\) is Haar-uniform and \((p,q)\ne(0,0)\), its phase \(U=\phi(A)\) is uniform on \((0,1)\) and independent of \((X,Y)\). As a minimizing arc is traversed, its lifted phase is \(U+t(qX-pY)\), \(0<t<1\). Each integer crossed gives exactly one transverse intersection with the zero phase curve, barring null degeneracies. The number is therefore \(|\lfloor U+qX-pY\rfloor|\), proving the exact distributional representation. For fixed positive or negative phase displacement of absolute size \(w\), averaging over its independent uniform initial phase yields the conditional two-point floor-plus-Bernoulli law stated above.

**2. Full density and rational masses.** The independent variables \(qX\) and \(pY\), up to signs, are centered uniforms of widths \(b\) and \(a\). Their convolution has constant height \(1/a\) on the central interval of radius \((a-b)/2\) and triangular linearly descending shoulders. Taking absolute values doubles the positive-half density, yielding precisely \(g_{a,b}\). The case \(b=0\) follows directly. More explicitly, for \(k=0\) define \(h_0(w)=(1-w)_+\) for \(w\ge0\). For every integer \(k\ge1\), define
\[
h_k(w)=\begin{cases}w-k+1,&k-1\le w\le k,\\k+1-w,&k\le w\le k+1,\\0,&\text{otherwise}.\end{cases}
\]
Then \(\Pr(N=k)=\int_0^{(a+b)/2}g_{a,b}(w)h_k(w)\,dw\). The integrand is piecewise quadratic with rational breakpoints and rational coefficients for integers \(a,b\), proving exact rationality of all masses. The support lies in \(\{0,\ldots,\lceil(a+b)/2\rceil\}\).

**3. The first moment.** Conditional on \(W=w\), the Bernoulli representation gives \(\mathbb E(N\mid W=w)=w\). To evaluate \(\mathbb EW\), first fix the narrower uniform summand \(V\in[-b/2,b/2]\) and average against the wider centered uniform summand \(Z\in[-a/2,a/2]\). Since \(|V|\le a/2\), exact one-dimensional integration gives
\[
\mathbb E_Z|Z+V|=a/4+V^2/a.
\]
Averaging \(V^2\) gives \(a/4+b^2/(12a)\), hence \(\mu=(3a^2+b^2)/(12a)\).

**4. The second moment.** Conditional on \(W=w\), the floor-plus-Bernoulli law gives
\[
\mathbb E(N^2\mid W=w)=w^2+\{w\}(1-\{w\}).
\]
Because at least one of \(p,q\) is a nonzero integer, the fractional part of the signed displacement \(qX-pY\) is uniform on the circle: one integer multiple of an independent unit-interval uniform variable is already Haar-uniform. The function \(t\mapsto\{t\}(1-\{t\})\) is invariant under \(t\mapsto-t\), so the fractional part of \(W=|qX-pY|\) has the same correction average \(\int_0^1t(1-t)dt=1/6\). Independently, \(\mathbb EW^2=(a^2+b^2)/12\). Adding yields \(\nu=(a^2+b^2+2)/12\).

**5. Arithmetic and continuous homology inversion.** By primitivity, \(\gcd(a,b)=1\). From \(12\mu=(3a^2+b^2)/a\), the numerator is coprime to \(a\), because \(\gcd(3a^2+b^2,a)=\gcd(b^2,a)=1\). The reduced denominator of \(12\mu\) is exactly \(a\); the mean then directly determines \(b^2=a(12\mu-3a)\), with \(b\ge0\). For the continuous two-moment formula set \(S=12\nu-2=a^2+b^2\). The moment identity gives \(2a^2-12\mu a+S=0\). Its larger root equals \(a\) (the discriminant's square root is \((a^2-b^2)/(4a)\)), and then \(b=\sqrt{S-a^2}\). Finally, \(S/\mu^2=144(1+r^2)/(3+r^2)^2\) has derivative \(288r(1-r^2)/(3+r^2)^3>0\) for \(0<r<1\), and endpoint values \(16,18\). This proves all bounds and recovery statements. \(\square\)

## Verification

The accompanying standalone `verification/check_intersections.py` performs independent exact-rational integration of all count masses for integral nonzero directions with both absolute coordinates at most 12, checks their normalization and nonnegativity, evaluates both moments, and verifies both algebraic reconstructions for those samples. Independent random endpoint simulations with 240,000 samples per specified primitive slope confirm the target moments for strongly disparate displayed torus aspect ratios. A separate geometrical checker explicitly intersects lifted open line segments with integer translates of a fundamental primitive closed-loop segment and matches the character count for 200 samples in each of six slopes, including a mixed-sign slope. Examples include \((\Pr(N=0),\Pr(N=1),\Pr(N=2))=(23,24,1)/48\) at slope \((2,1)\) and \((\Pr(N=0),\Pr(N=1),\Pr(N=2),\Pr(N=3))=(47,71,25,1)/144\) at slope \((3,2)\). This finite evidence is corroborative: the proof is the exact phase-crossing argument and the preceding integrals.

## Relationship to prior work

Artzrouni (arXiv:0712.1477v1, 2007) investigates crossings of independent fixed-length random-direction planar motion steps. Its planar two-moving-path event neither fixes an embedded closed homology curve on a torus nor determines the complete count law and exact-homology inverse in this theorem. Herrera Jaramillo (2015) studies intersection-number tails and asymptotic self-intersections of closed geodesics on negatively curved closed surfaces, rather than shortest arcs and fixed primitive classes on orthogonal flat two-tori. Glorieux and Yarmola (2020, arXiv:2003.08190v1) derive null-homotopy probabilities for random three-vertex geodesic triangles on flat tori; that article's full text concerns a three-copy Voronoi overlap invariant, not this fixed-target intersection count. The publicly available *Sharp crossing probability for independently sampled shortest geodesics on flat two-tori* establishes two independently random open-arc crossing probabilities, with a determinant integral and a sharp lattice-shape extremum. Neither its two-random-segment observable nor its theorem implies the fixed-primitive-target marked count law or arithmetic first-moment inverse. These comparisons exclude the identified closest statements, not all conceivable unindexed classical Crofton/Buffon formulations.

## Limitations

The closed target is primitive and embedded; the torus lattice must be rectangular (orthogonal); the sampled open arc must minimize intrinsic length. The count law and inversions apply to exact ideal data. Sign, orientation and coordinate interchange cannot be recovered by the symmetric sampling scheme. A continuous two-moment inversion is algebraic but becomes ill-conditioned at the endpoint ratio \(b/a=1\); the exact one-moment rational-denominator inverse is not statistically stable without a sampling budget and an a priori bound on homology magnitude. The proof is self-contained but final historical priority against uncatalogued integral geometry is provisional. No independent mathematical validation is claimed.

## References

1. M. Artzrouni, *Crossing paths in 2D Random Walks*, arXiv:0712.1477v1, first public 2007-12-10, https://arxiv.org/abs/0712.1477.
2. Y. A. Herrera Jaramillo, *Intersection numbers of geodesic arcs*, *Revista Colombiana de Matemáticas* 49 (2015), 307–319, DOI:10.15446/recolma.v49n2.60450, first public date verified 2015-07-01, https://revistas.unal.edu.co/index.php/recolma/article/view/60450.
3. O. Glorieux and A. Yarmola, *Random triangles on flat tori*, arXiv:2003.08190v1, first public 2020-03-18, https://arxiv.org/html/2003.08190v1.
4. *Sharp crossing probability for independently sampled shortest geodesics on flat two-tori*, public full-result record, 2026-11-01, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-sharp-crossing-probability-for-independently-sampled-shortest-ge--72270b2f5a6b/RESULT.md.
5. *Mathematics Subject Classification 2020*, 53C22, geodesics.
