# Exact Lexell-area distribution and stochastic ordering for a uniform spherical apex

## Finding

Fix two points on the unit sphere at geodesic separation \(2\beta\), with \(0<\beta<\pi/2\). Sample a third point uniformly by spherical surface area, and join the three points by their unique minimizing great-circle arcs. Let \(S_\beta\in[0,2\pi]\) be the intrinsic, nonoriented spherical area (spherical excess) of this triangle. Define \(c=\cos\beta\). For every \(0\le t\le2\pi\), with \(a=t/2\), its **complete distribution** is

\[
\boxed{\mathbb P(S_\beta\le t)=\frac a\pi+
\frac{c\sin a}{\pi\sqrt{1-c^2\cos^2a}}\,
\arccos(-c\cos a).}
\]

The CDF equals zero for \(t<0\) and one for \(t>2\pi\). This law is **strictly stochastically increasing in the fixed base length** \(2\beta\): for every \(0<t<2\pi\), its CDF strictly decreases as \(\beta\) increases. One exactly observable probability recovers the base length:
\[
\boxed{\mathbb P(S_\beta\le\pi)=\frac{1+\cos\beta}{2}.}
\]
The two singular endpoint families have explicit limiting laws:
\[
\mathbb P\left(\frac{S_\beta}{2\beta}\le u\right)
\longrightarrow\frac{u}{\sqrt{1+u^2}}\quad(\beta\downarrow0,\ u\ge0),
\]
\[
S_\beta\Longrightarrow \operatorname{Uniform}[0,2\pi]
\quad(\beta\uparrow\pi/2).
\]
For each fixed nondegenerate base, both endpoints of the distribution have positive finite one-sided densities, expressed by
\[
\mathbb P(S_\beta\le t)\sim \frac{1+(\pi-\beta)\cot\beta}{2\pi}\,t
\quad(t\downarrow0),
\]
\[
\mathbb P(S_\beta>2\pi-t)\sim \frac{1-\beta\cot\beta}{2\pi}\,t
\quad(t\downarrow0).
\]

## Assumptions and scope

The sphere has unit radius and area measure normalized to total mass one. The two fixed vertices are distinct and non-antipodal, with their shortest great-circle distance strictly between \(0\) and \(\pi\). The third vertex is independent and exactly uniform over the entire sphere. Almost surely all three minimizing arcs are uniquely determined and form a proper oriented triangle; \(S_\beta\) is the absolute value of its signed spherical solid angle on the branch \((-2\pi,2\pi)\), not the Euclidean chord-triangle area. The degenerate side lengths \(0\) and \(\pi\) are limits, not members of the family. The small-side limit holds at each fixed \(u\); no uniform-in-parameter error rate is claimed.

## Proof

**1. The area coordinate and its range.** A rotation puts the two fixed endpoints at \(A=(c,-s,0)\) and \(B=(c,s,0)\), where \(s=\sin\beta>0\). Write the random apex \(C=(X,Y,Z)\). The standard oriented solid-angle identity for a shortest-arc spherical triangle is
\[
\Omega=2\operatorname{atan2}\bigl(\det(A,B,C),\ 1+A\cdot B+B\cdot C+C\cdot A\bigr).
\]
Substituting \(\det(A,B,C)=2csZ\) and \(1+A\cdot B+B\cdot C+C\cdot A=2c(c+X)\) gives
\[
\Omega=2\operatorname{atan2}(sZ,c+X),\qquad S_\beta=|\Omega|.
\]
The two-argument arctangent is essential: a principal one-argument arctangent would lose the near-\(2\pi\) branch. Reflection \(Z\mapsto-Z\) reverses the sign and preserves area measure.

**2. The exact level region.** For \(0<a<\pi\), condition on \(Z\ge0\), where \(\Omega/2\in[0,\pi]\). The event \(S_\beta\le2a\) is then exactly
\[
Z\ge0,\qquad (c+X)\sin a-sZ\cos a\ge0.
\]
Set \(L=\sqrt{1-c^2\cos^2a}\), \(n=(\sin a,0,-s\cos a)/L\), and \(h=-c\sin a/L\). This is the intersection of the northern hemisphere with the spherical cap \(n\cdot C\ge h\). Its boundary is a great-circle arc and a small-circle arc meeting at the two antipodes \((-c,\pm s,0)\) of the fixed vertices. Each interior corner angle equals \(a\): the inward unit normals to the two constraint curves have angle \(\pi-a\) within the tangent plane. The small-circle radius in its Euclidean supporting plane is \(\sqrt{1-h^2}=s/L\). The small-circle arc lying in the upper hemisphere subtends at its Euclidean circle center the angle \(2\arccos(-c\cos a)\), as follows either by projecting its two endpoints onto that plane or by using their common \(y\)-coordinates \(\pm s\). Its signed geodesic-curvature integral, with the region to the left, is consequently
\[
\int_{\mathrm{small\ arc}}k_g\,d\ell
=h\,2\arccos(-c\cos a).
\]
The great-circle arc contributes zero curvature. Gauss--Bonnet for this topological disk, including the two corner turns \(\pi-a\), yields its spherical area
\[
2\pi-2(\pi-a)-2h\arccos(-c\cos a)
=2a+\frac{2c\sin a}{L}\arccos(-c\cos a).
\]
The reflected event has the same area in the southern hemisphere. Divide twice this area by total sphere area \(4\pi\) to obtain the displayed CDF. Continuity proves the endpoint values.

**3. Strict stochastic order and identifiability.** For fixed \(a\in(0,\pi)\), write \(q=c\cos a\) and \(L=\sqrt{1-q^2}\). Differentiation gives
\[
\frac{\partial}{\partial c}\left(\frac{c\sin a}{L}\arccos(-q)\right)
=\frac{\sin a}{L^3}\left[\arccos(-q)+q\sqrt{1-q^2}\right]>0.
\]
Indeed the bracket is zero at \(q=-1\), and its derivative is \(2\sqrt{1-q^2}>0\) on \((-1,1)\). Since \(c=\cos\beta\) strictly decreases in \(\beta\), the claimed strict stochastic increase follows. Setting \(a=\pi/2\) gives the half-area identity and injective recovery of \(\beta\).

**4. Singular bases and endpoint densities.** For \(a=\beta u\) and \(\beta\downarrow0\), the relations \(L\sim\beta\sqrt{1+u^2}\), \(c\sin a\sim\beta u\), and \(\arccos(-c\cos a)\to\pi\) yield the stated limiting CDF \(u/\sqrt{1+u^2}\). This is a proper continuous CDF on \([0,\infty)\), so it gives weak convergence. As \(\beta\uparrow\pi/2\), \(c\to0\) and the correction term vanishes uniformly for \(a\in[0,\pi]\), leaving \(a/\pi\), the uniform law. For fixed \(\beta\), expanding at \(a=0\) and \(a=\pi\) respectively gives the two stated one-sided density coefficients; both are positive since \(0<\beta<\pi/2\) and \(\tan\beta>\beta\).

## Verification

The independent deterministic numerical check `checks/lexell_area_checker.py` evaluates the CDF by conditioning on the uniformly distributed spherical coordinate \(X\) and integrating the conditional arcsine law of \(Z\). This is separate from the Gauss--Bonnet derivation, and agrees at 35 interior parameter/threshold pairs to the prescribed tolerance. It also verifies the half-area identity, monotonicity, and the small-base limit. Run `python checks/lexell_area_checker.py` with Python, NumPy and SciPy. Numerical checks corroborate but do not prove the analytic identity.

## Relationship to prior work

Euler--Lexell's theorem characterizes the fixed-base, fixed-area apex locus as a small-circle arc; it does not supply the area distribution induced by uniform surface sampling, a strict distributional comparison across base lengths, or the two singular weak limits. Papadopoulos's full historical and geometric discussion of Lexell's theorem in arXiv:1409.4736, Sections 5--6, was examined for these distinctions. The 2017 study by Maehara and Martini concerns further forms and proofs of Lexell's theorem; its abstract was checked, but the full text was unavailable. A separate published result on pole-anchored triangles with two random latitude-circle vertices fixes a different vertex and sampling mechanism, and does not imply this fixed-base uniform-apex CDF. The same distinctions were checked against semantic search results for spherical-excess and random-apex formulations. Novelty is supported only by these comparisons, not by the absence of matching search hits alone.

## Limitations

No claim of independent novelty certification is made. The area formula assumes full-sphere uniform sampling of the third vertex and fixed nonantipodal endpoints; it does not apply as stated to latitude-restricted sampling, arbitrary point densities, curved nonround ambient surfaces, or an exactly antipodal pair. Full access to Maehara--Martini (2017) was unavailable; the overlap risk is retained. The limiting laws do not include a uniform convergence rate.

## References

1. A. Papadopoulos, *On the works of Euler and his followers on spherical geometry*, arXiv:1409.4736, first posted 2014-09-16, especially Sections 5--6. https://arxiv.org/abs/1409.4736
2. H. Maehara and H. Martini, *On Lexell's Theorem*, American Mathematical Monthly 124 (2017), 337--344, https://doi.org/10.4169/amer.math.monthly.124.4.337 (abstract inspected; full text not obtained).
3. *Exact equatorial bifurcation and universal marked area law for pole-anchored spherical triangles*, published-finding corpus published result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-equatorial-bifurcation-and-universal-marked-area-law-for-p--5a49e2ae2252 (distinct random-latitude sampling).
