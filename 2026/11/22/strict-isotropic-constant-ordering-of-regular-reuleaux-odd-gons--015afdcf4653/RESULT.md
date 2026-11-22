# Strict isotropic-constant ordering of regular Reuleaux odd-gons

## Finding
For every odd integer \(n\ge3\) and every constant width \(w>0\), let \(K_n(w)\subset\mathbb R^2\) be the regular Reuleaux \(n\)-gon, centered at its dihedral center. Define
\[
L^2(K)=\frac{\sqrt{\det\operatorname{Cov}(X_K)}}{\operatorname{area}(K)},
\]
where \(X_K\) is area-uniform on \(K\). Then the *strict all-order ordering* holds:
\[
\boxed{L^2(K_n(w))>L^2(K_{n+2}(w))>\frac1{4\pi}.}
\]
The invariant is independent of \(w\). Therefore a measured exact value of \(L^2\) within this family identifies the odd polygon order uniquely; the limiting value \(1/(4\pi)\) belongs to the disk, not to any finite order.

Writing \(n\to\infty\) through odd integers, successive gaps have the sharp asymptotic
\[
\boxed{L^2(K_n)-L^2(K_{n+2})=\frac{2\pi^3}{45n^5}+O(n^{-6}).}
\]
The previously known individual-moment and individual-isotropic-constant formulas, reproduced below to establish the ordering, are **not** claimed as new. The new result is the global strict comparison between different odd orders and its consequent identification and spacing laws.

## Assumptions and scope
A regular Reuleaux odd-\(n\)-gon is the constant-width convex region with boundary comprising \(n\) equal-radius circular arcs, each centered at the opposite vertex of a regular odd-\(n\)-gon. The case \(n=3\) is included in the comparison, although the Reuleaux-triangle polar moment is classical.

Scale invariance permits \(w=1\). Put
\[
b=\frac\pi{2n},\qquad t=\tan b,\qquad R=\frac1{2\cos b}.
\]
The normalizing convention is \(L^4(K)=\det\operatorname{Cov}(X_K)/\operatorname{area}(K)^2\). The value of \(L^2\) for a disk is \(1/(4\pi)\).

The analytic proof actually establishes a stronger continuous statement: the function
\[
H(b)=\frac{b[4b(3+\tan^2 b)-\tan b(11+\tan^2 b)]}{(2b-\tan b)^2}
\]
is strictly increasing throughout \(0<b\le\pi/6\). The discrete theorem follows by substituting \(b=\pi/(2n)\).

## Proof
**Step 1: geometric reconstruction of the normalization.** For width one, each circular boundary arc can be rotated to
\[
x(u)=(R-\cos u,-\sin u),\quad \nu(u)=(-\cos u,-\sin u),\quad -b\le u\le b,
\]
with outward normal \(\nu\) and arclength differential \(du\). The divergence theorem, applied to \(x\) and \(\|x\|^2x\), gives respectively
\[
A=\frac n2\int_{-b}^{b}(1-R\cos u)\,du
=\frac{\pi-n\tan b}{2},
\]
\[
I=\int_{K_n(1)}\|x\|^2\,dx
=\frac n4\int_{-b}^{b}(R^2+1-2R\cos u)(1-R\cos u)\,du
=\frac{2\pi(3+t^2)-nt(11+t^2)}{16}.
\]
These formulas agree with the previously published regular-family moment formula. By rotational symmetry, \(\operatorname{Cov}(X)=I/(2A)\,I_2\), and consequently
\[
4\pi L^2(K_n)=H(b).
\]
In the disk limit \(b\downarrow0\), \(H(b)\to1\).

**Step 2: exact derivative reduction.** Set \(D=2b-t\), \(B=4b(3+t^2)-t(11+t^2)\), and \(z=b^2\), \(x=t/b\). Differentiating \(H=bB/D^2\) using \(dt/db=1+t^2\) gives
\[
D^3H'(b)=N(b,t)=b^2P(z,x),
\]
where
\[
\begin{aligned}
P(z,x)={}&2-13x+11x^2\\
&+z(16x-4x^2-16x^3+x^4)\\
&+z^2(16x^3-6x^4+x^5).
\end{aligned}
\]
The polynomial identity is checked independently with exact rational two-variable arithmetic in `verify.py`.

**Step 3: a global rational certificate.** Convexity of tangent gives \(1\le x=\tan b/b\le 2\sqrt3/\pi<7/6\) for \(0<b\le\pi/6\). Also \(0<z\le\pi^2/36<1/3\), and \(D=b(2-x)>0\).

Write the convergent tangent expansion
\[
\frac{\tan b}{b}=\sum_{k\ge0}a_k z^k,
\qquad a_0=1,\qquad
(2k+1)a_k=\sum_{j=0}^{k-1}a_ja_{k-1-j}\quad(k\ge1).
\]
The recurrence proves the **uniform coefficient bound** \(0<a_k\le2^{-k}\) by induction: if it holds below \(k\), then
\[
a_k\le\frac{k\,2^{-(k-1)}}{2k+1}\le2^{-k}.
\]
Let \(x_8(z)=\sum_{k=0}^8a_kz^k\). Summing this elementary geometric bound for \(0<z\le1/3\) gives the explicit rigorous tail
\[
0\le x-x_8(z)\le\frac{(z/2)^9}{1-z/2}\le Cz^9,
\qquad C=\frac3{1280}.
\]
For \(0\le z\le1/3\), \(1\le x\le7/6\), direct termwise estimation of the displayed polynomial yields \(|\partial P/\partial x|<90\). Hence
\[
\frac{|P(z,x)-P(z,x_8)|}{z^2}<90Cz^7\le\frac{90C}{3^7}<\frac1{100}.
\]

Expand the *finite exact rational polynomial* \(P(z,x_8(z))=\sum_{k=0}^{42}c_kz^k\). Its coefficients satisfy
\[
c_0=c_1=0,\quad c_2=\frac{64}{45},\quad
c_3=\frac{128}{105},\quad c_4=\frac{2944}{4725},\quad
c_5=\frac{3968}{18711},\quad c_6=\frac{364864}{14189175}>0,
\]
and the exact finite coefficient comparison
\[
\sum_{\substack{k\ge7\\c_k<0}}(-c_k)3^{-(k-2)}
=\frac{21677472670147862}{118112958333460715625}<\frac1{1000}.
\]
The recurrence for \(a_k\), polynomial multiplication, the displayed identity, and both rational inequalities are recomputed from first principles by the supplied standalone standard-library verifier. They entail, for every real \(0<z\le1/3\),
\[
\frac{P(z,x)}{z^2}>
\frac{64}{45}-\frac1{1000}-\frac1{100}
=\frac{12701}{9000}>0.
\]
Thus \(N=b^2P(z,x)>0\), and since \(D>0\), \(H'(b)>0\) everywhere in the required interval.

**Step 4: discrete ordering and sharp spacing.** If \(n\) is odd, then \(\pi/(2(n+2))<\pi/(2n)\), proving \(L^2(K_{n+2})<L^2(K_n)\). The limit \(H(0)=1\) proves the strict disk inequality. The elementary tangent series yields
\[
H(b)=1+\frac{16}{45}b^4+\frac{416}{945}b^6+O(b^8).
\]
Substitute \(b=\pi/(2n)\) and take the adjacent odd-order difference; analyticity of this even series gives
\[
L^2(K_n)=\frac1{4\pi}+\frac{\pi^3}{180n^4}+O(n^{-6}),
\quad
L^2(K_n)-L^2(K_{n+2})=\frac{2\pi^3}{45n^5}+O(n^{-6}).
\]
The individual \(n^{-4}\) defect is prior-covered; strict monotonicity and the successive-gap consequence are the contributions here.

## Verification
Run `python3 verify.py` with Python 3 and no third-party dependencies. The verifier independently reconstructs the rational polynomial derivative identity, generates the first nine tangent-series coefficients from the differential equation, expands the exact degree-42 rational comparison, checks the coefficient-tail inequalities, and establishes the uniform positive margin. Supplementary midpoint quadrature independently checks the geometric area and polar-moment integrals for orders \(3,5,7,9,11,17,31,51\); finite-order numerical comparisons do not replace the all-order certificate. The verifier prints `PASS` on successful completion.

## Relationship to prior work
Chen, Chen and Jin (2023) motivate comparing regular Reuleaux shapes within the fixed-width class but optimize circumradius *at each fixed order*, not the isotropic constant *between orders*. A publicly available 2026 mathematical note, *Polar moment and isotropic constant of regular Reuleaux odd-gons*, already proves the exact formula for \(n\ge5\) used in Step 1, and its quadratic-to-quartic cancellation. Its explicit limitation states that **no monotonicity theorem over odd orders is claimed**. Consequently neither this moment identity nor its asymptotic alone proves the new strict cross-order inequalities. Classical engineering calculations already treat the order-three polar moment.

A distinct known monotonicity result for isotropic constants of regular polygons under Euclidean outer parallel rounding concerns \(P_n+tB\), not Reuleaux odd-gons built from *intersections* of disks; it has no order-comparison implication here. The general lower bound supplied by ellipses establishes at most the disk inequality for individual bodies, not the strict ordering. Targeted comparisons and equivalent-formulation searches are documented in the review metadata.

## Limitations
The classification is restricted to regular Reuleaux polygons of odd order, not irregular constant-width regions. It does not determine which Reuleaux polygon minimizes the isotropic constant among all width-one shapes at each fixed order, nor claim a general inclusion or Minkowski-monotonicity theorem. The exact inertia and \(n^{-4}\) defect are prior results. An unindexed earlier proof of strict cross-order monotonicity remains possible; independent priority and mathematical audit have not been performed.

## References
1. Q. Chen, B. Chen and H. Jin, *The circumradius of planar reduced convex bodies*, Journal of Geometry 114, article 6 (first published 2023-02-04), DOI: https://doi.org/10.1007/s00022-023-00667-5.
2. *Polar moment and isotropic constant of regular Reuleaux odd-gons*, public mathematical note, 2026-10-11, (exact family formula and quartic deficit previously established).
3. M. S. Razumov et al., *Stress calculation of moment transmitting roll with profile on the base of Reuleaux triangle*, Metallurgical and Mining Industry 3 (2014), 50–54 (order-three mechanical moment).
4. H. Jin, *Asymmetry of Reuleaux polygons*, Beiträge zur Algebra und Geometrie 58 (2017), 311–317, DOI: https://doi.org/10.1007/s13366-016-0318-2 (regular Reuleaux geometry, different invariant).
