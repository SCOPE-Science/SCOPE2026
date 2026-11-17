# Threefold ambiguity of two Euclidean distance moments for planar circular sectors

## Finding
Let \(S_{R,\theta}=\{r(\cos\phi,\sin\phi):0\le r\le R,\,-\theta/2\le\phi\le\theta/2\}\), where \(R>0\) and \(0<\theta\le2\pi\). Let \(X,Y\) be independent, area-uniform points of this planar circular sector and let \(D=\|X-Y\|_2\). For **every** \(m>0\) and every \(k\in(9/5,39/20)\), there are three pairwise noncongruent sectors with exactly
\[
\mathbb E D^2=m,\qquad \mathbb E D^4=k m^2.
\]
Their respective angles can be chosen in the three disjoint intervals \((0,\pi/2)\), \((\pi/2,\pi)\), and \((\pi,3\pi/2)\). Thus the second and fourth Euclidean random-pair distance moments cannot determine the opening angle or even distinguish a convex sector from a nonconvex one. The claimed fiber has *at least* three members; no global upper bound on its multiplicity is asserted.

## Assumptions and scope
The sector is the literal subset of the Euclidean plane specified above; the two straight radial boundary segments are not glued together. The distance is the ambient Euclidean straight-line distance, **not** the intrinsic metric of a conical quotient. Sampling is independent, normalized two-dimensional Lebesgue area. In particular, the random radial coordinate has density \(2r/R^2\), and the polar angle is independent and uniform on the specified angular interval. The convexity assertions concern the ordinary planar sectors with opening angles strictly below and strictly above \(\pi\).

## Proof
Write \(c_1(\theta)=\sin(\theta/2)/(\theta/2)\) and \(c_2(\theta)=\sin\theta/\theta\). For a unit-radius sector, independent radial coordinates \(U,V\) obey \(\mathbb E U^j=2/(j+2)\); independent angles \(\Phi,\Psi\) obey
\[
\mathbb E\cos(\Phi-\Psi)=c_1(\theta)^2,\qquad
\mathbb E\cos^2(\Phi-\Psi)=(1+c_2(\theta)^2)/2.
\]
Expanding \(D^2=U^2+V^2-2UV\cos(\Phi-\Psi)\) and its square gives, for every \(R>0\) and \(0<\theta\le2\pi\),
\[
\begin{aligned}
\mathbb E D^2&=R^2F_2(\theta),& F_2(\theta)&=1-\frac89c_1(\theta)^2,\\
\mathbb E D^4&=R^4F_4(\theta),&F_4(\theta)&=\frac53-\frac{32}{15}c_1(\theta)^2+\frac12c_2(\theta)^2.
\end{aligned}
\]
Since \(F_2(\theta)>0\), the scale-free moment ratio is the continuous function \(K(\theta)=F_4(\theta)/F_2(\theta)^2\). Taylor expansions at zero show \(\lim_{\theta\downarrow0}F_2(\theta)=1/9\), \(\lim_{\theta\downarrow0}F_4(\theta)=1/30\), hence \(\lim_{\theta\downarrow0}K(\theta)=27/10\).

The three needed evaluations are
\[
\begin{aligned}
K(\pi/2)&=\frac{5/3-226/(15\pi^2)}{(1-64/(9\pi^2))^2}<\frac95,\\
K(\pi)&=\frac{5/3-128/(15\pi^2)}{(1-32/(9\pi^2))^2}>\frac{39}{20},\\
K(3\pi/2)&=\frac{5/3-226/(135\pi^2)}{(1-64/(81\pi^2))^2}<\frac95.
\end{aligned}
\]
These strict inequalities are certifiable by rational bounds on \(\pi\); a standalone exact rational checker is supplied. Therefore, for each \(9/5<k<39/20\), continuity and the intermediate value theorem furnish distinct roots \(\theta_1\in(0,\pi/2)\), \(\theta_2\in(\pi/2,\pi)\), and \(\theta_3\in(\pi,3\pi/2)\) of \(K(\theta)=k\). Choosing
\[
R_i=\sqrt{m/F_2(\theta_i)}
\]
realizes both prescribed moments exactly for all three sectors. Their different opening angles imply pairwise noncongruence, as each sector has a uniquely identifiable circular boundary arc and apex. The first two sectors are convex and the third is nonconvex. This proves the claimed open threefold ambiguity.

## Verification
Run `python3 check_sector.py` with Python 3 standard library, from the directory containing this file and the checker. The checker uses the Machin arctangent identity and alternating-series rational enclosures for \(\pi\) to certify the three strict comparisons above without relying on floating-point inequalities. It also checks bracketed numerical roots and independent Monte Carlo evaluations of the derived moments. The expected terminal marker is `CIRCULAR_SECTOR_TRIPLE_MOMENT_AMBIGUITY_OK`. Only the exact rational signs and analytical derivation are needed for the existence proof; Monte Carlo is non-probative for the existence of all real-parameter roots.

## Relationship to prior work
Classical circular-sector line picking provides special-angle **mean** distances, not this two-moment inverse fiber. General forward-distance approaches for triangles (Tong, Ahmadi and Pan) and for polygons (Tong and Pan), and moment formulas for regular polygons (Bäsel), address different shape families and do not entail this explicit open family of sector moment collisions. Existing results about threefold ambiguity of intrinsic distances on flat conical disks concern a different metric space: the angular boundary is identified and shortest paths can wrap, whereas this theorem uses Euclidean distance within an unglued sector. This mathematical distinction precludes inferring the sector statement merely by relabelling the conical result. No claim of a general uniqueness classification, first discovery of moment formulas, or quantitative inverse stability is made.

## Limitations
The proof guarantees at least three noncongruent sectors for an explicit open set of two-moment data, not exactly three; it does not prove whether higher moments resolve the ambiguity. The sector-to-shape map is a special two-parameter family, not all convex domains. Historical priority remains provisional because full coverage of historical line-picking literature is not possible; some accessible sources supply tables rather than general inverse analyses. Numerical examples are checks, not an infinite proof.

## References
1. Tong, Ahmadi and Pan, *Random Distances Associated with Arbitrary Triangles: A Systematic Approach between Two Random Points* (first public arXiv posting 2013-11-29), https://arxiv.org/abs/1312.2498.
2. Tong and Pan, *Random Distances Associated with Arbitrary Polygons: An Algorithmic Approach between Two Random Points* (2016), https://arxiv.org/abs/1602.03407.
3. Bäsel, *The moments of the distance between two random points in a regular polygon* (2021), https://arxiv.org/abs/2101.03815.
4. Weisstein, *Circular Sector Line Picking*, https://mathworld.wolfram.com/CircularSectorLinePicking.html.
5. Lew, Frauenthal and Keyfitz, *On the Average Distances in a Circular Disc*, SIAM Review 20 (1978), https://doi.org/10.1137/1020073 (abstract examined; not used for a full-text exclusion).
