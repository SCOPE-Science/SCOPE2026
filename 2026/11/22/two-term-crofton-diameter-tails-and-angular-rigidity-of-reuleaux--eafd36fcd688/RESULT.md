# Two-term Crofton diameter tails and angular rigidity of Reuleaux polygons

## Finding

Let \(K\subset\mathbb R^2\) be any **nondegenerate Reuleaux polygon** of Euclidean constant width \(1\), whose boundary consists of \(m\ge3\) circular arcs of radius \(1\), each of positive angular length \(\ell_j\), with arc centres at boundary vertices. Then \(m\) is odd, \(0<\ell_j\le\pi/3\), and \(\sum_{j=1}^m\ell_j=\pi\). Draw an unoriented affine line from Euclidean-motion-invariant measure \(d\phi\,dt\), \(0\le\phi<\pi\), conditioned on intersecting \(K\); let \(L\) be the length of its chord. For each *fixed* such polygon, as \(\varepsilon\downarrow0\),

\[
\boxed{\Pr\{L>1-\varepsilon\}=\frac{\varepsilon}{\pi}\left[m\log\frac1\varepsilon+m+2\sum_{j=1}^m\log(\sin\ell_j)\right]+o_K(\varepsilon).}
\]

Consequently, among the Reuleaux \(m\)-gons of unit width, the regular one uniquely maximizes the **second asymptotic coefficient**, and its long-chord probability is strictly greater than that of every fixed nonregular \(m\)-gon for all sufficiently small positive \(\varepsilon\). Precisely, if \(R_m\) is regular, then

\[
\lim_{\varepsilon\downarrow0}\frac{\Pr_{R_m}(L>1-\varepsilon)-\Pr_K(L>1-\varepsilon)}{\varepsilon}
=\frac2\pi\left[m\log\sin\frac\pi m-\sum_{j=1}^m\log\sin\ell_j\right]\ge0,
\]

with equality exactly for the regular \(m\)-gon. Near equal arc angles, the gap coefficient equals
\[
\frac{\csc^2(\pi/m)}{\pi}\sum_{j=1}^m(\ell_j-\pi/m)^2
+O_m\!\left(\sum_j|\ell_j-\pi/m|^3\right).
\]

The leading \(m/\pi\) coefficient for general odd \(m\) and the full shape-sensitive linear term refer to *invariant-line chords*, not independently sampled boundary or interior endpoints.

## Assumptions and scope

A Reuleaux \(m\)-gon here means the convex body of diameter and constant width \(1\) bounded by exactly \(m\) nonzero circular arcs of radius \(1\), each arc centred at a vertex of the boundary; all joins are genuine corners. It is the intersection of its finitely many unit disks centred at those vertices. Arc lengths are measured as central angles because the radii are one. The arc-centre/endpoint incidence is dual: when an arc centred at \(C\) ends at a corner \(Q\), the arc adjacent to \(C\) on the matching side is centred at \(Q\). This also follows directly from uniqueness of supporting contacts for a constant-width curve away from its corners. The total perimeter is \(\pi\) by Barbier's theorem. A line is represented by \(x=tu_\phi+sv_\phi\), with \(u_\phi=(\cos\phi,\sin\phi)\), \(v_\phi=(-\sin\phi,\cos\phi)\), and conditioned on a nondegenerate intersection with \(K\). Its total unnormalized line measure is the perimeter \(\pi\), by Cauchy's projection formula.

For a fixed polygon, all positive arc lengths and corner angles remain fixed as the chord deficit tends to zero; no uniformity is claimed for degenerating polygon families or \(m\to\infty\). Replacing strict \(>\) by \(\ge\) does not change the result, since each nontrivial chord-length level has zero invariant line measure.

## Proof

**1. Partition the diameter orientations.** A relative-interior point \(Q\) of an arc centred at a vertex \(C\) has the unique opposing diameter endpoint \(C\), since its exterior normal points along \(Q-C\). Hence the line through \(C,Q\) has length exactly \(1\). Conversely every diameter of a body of constant width has opposite supporting endpoints, and away from finitely many corner normal directions its smooth contact lies on exactly one arc and its opposite endpoint is its centre. Thus, modulo the negligible finite boundaries, the unoriented line directions split into \(m\) sectors of respective angular lengths \(\ell_1,\ldots,\ell_m\). Their lengths sum to \(\pi\). The arc's two endpoints are each at distance one from its centre, and their mutual distance does not exceed the body's diameter; hence \(2\sin(\ell_j/2)\le1\), giving \(\ell_j\le\pi/3\).

**2. The two circular local branches.** Fix an arc centred at \(C=(0,0)\), with radial angles \(a\le\theta\le b\) and \(\ell=b-a\). Parametrize the lines parallel to \(u_\theta\) by their signed normal offset \(s\) from \(C\). The maximal chord at offset zero is \([C,C+u_\theta]\). Its terminal endpoint lies on the unit circle centred at \(C\). For positive offset, the near-centre endpoint lies on the adjacent unit circle centred at \(C+u_a\); for negative offset it lies on the unit circle centred at \(C+u_b\). These are exactly the dual incidence arcs at \(C\). With \(x=\theta-a\) or \(x=b-\theta\), respectively, and \(z=|s|\), the two resulting local chord functions are

\[
\Lambda(x,z)=\sqrt{1-z^2}-\cos x+\sqrt{1-(z+\sin x)^2},\quad 0\le x\le\ell,\quad z\ge0.
\]

This identity follows by solving the two unit-circle equations for the extreme longitudinal coordinates of the line. All other disk inequalities have slack on the interior of each contact sector. At its endpoints, any alternate active disk can affect the *noncritical* sign only within an angular strip of width \(O(z)\); there the corresponding root is \(O(\varepsilon)\), so this change alters the integrated measure by \(O(\varepsilon^2)\). The critical sign, with \(x\downarrow0\), remains in the displayed two-circle branch because its transverse shift enters the adjacent arc's interior. Consequently, using the displayed formula for both signs throughout their sectors changes the resulting long-chord line measure by \(o(\varepsilon)\). The assertion can also be seen locally from the strict exterior-angle gaps between the two incident circular tangents at each nondegenerate corner and compactness away from the finitely many joins.

Let \(q_\varepsilon(x)\) be the unique small nonnegative root of \(\Lambda(x,z)=1-\varepsilon\). Monotonicity near zero follows from the first nonzero terms below. The positive- and negative-offset widths in the sector are, up to an integrated \(o(\varepsilon)\) error, \(q_\varepsilon(\theta-a)\) and \(q_\varepsilon(b-\theta)\). The total unnormalized rare-chord line measure is therefore

\[
2\sum_{j=1}^{m}\int_0^{\ell_j}q_\varepsilon(x)\,dx+o(\varepsilon).
\]

**3. Universal matched asymptotics.** The exact function has the small-offset expansion, uniformly for bounded \(0\le x\le\pi/3\),

\[
1-\Lambda(x,z)=z\tan x+\tfrac12(1+\sec^3x)z^2+O(z^3),
\]

and near \((x,z)=(0,0)\),
\[
1-\Lambda(x,z)=(xz+z^2)\,[1+O(x^2+z)].
\]

Take the matching angle \(r=\varepsilon^{1/4}\). On \([r,\ell]\), a monotone-root estimate using the first expansion gives \(q_\varepsilon(x)=\varepsilon\cot x+O(\varepsilon^2\cot^3x)\). The integrated error is \(O(\varepsilon^2/r^2)=o(\varepsilon)\), and hence
\[
\int_r^\ell q_\varepsilon(x)\,dx
=\varepsilon[\log(\sin\ell)-\log r]+o(\varepsilon).
\]
On \([0,r]\), set \(x=\sqrt\varepsilon\,v\), \(z=\sqrt\varepsilon\,w\). The uniformly relative-accurate limiting equation is \(w^2+vw=1\), with upper solution \(w(v)=(\sqrt{v^2+4}-v)/2\). The relative error from the preceding local expansion times the logarithmic integral is \(o(1)\); the primitive
\[
\int_0^R w(v)\,dv=\tfrac14\left(R\sqrt{R^2+4}-R^2\right)+\operatorname{arsinh}(R/2)
=\log R+\tfrac12+o(1)
\]
as \(R\to\infty\) yields
\[
\int_0^r q_\varepsilon(x)\,dx
=\varepsilon\left[\log\frac r{\sqrt\varepsilon}+\tfrac12\right]+o(\varepsilon).
\]
Combining the two regions,
\[
\int_0^\ell q_\varepsilon(x)\,dx
=\varepsilon\left[\tfrac12\log(1/\varepsilon)+\log\sin\ell+\tfrac12\right]+o_\ell(\varepsilon).
\]
Substituting in the angular-sector decomposition and dividing by the invariant total line measure \(\pi\) gives the displayed two-term theorem.

**4. Angular rigidity.** Because \(\log\sin x\) is strictly concave on \((0,\pi/3]\) and \(\sum_j\ell_j=\pi\), Jensen gives \(\sum_j\log\sin\ell_j\le m\log\sin(\pi/m)\), with equality only when all arcs have the same angular length. By the classical characterization of regular Reuleaux polygons, this is exactly the regular \(m\)-gon (up to congruence). Taylor expansion of \(\log\sin x\) around \(\pi/m\), with its linear terms cancelling, proves the displayed quadratic stability expansion. The leading terms in the two long-chord laws coincide, while the second coefficient is strictly ordered, giving eventual strict probability ordering for each fixed nonregular competitor.

## Verification

The standalone `verify_reuleaux.py` calculates the chord *independently* as the intersection of the \(m\) Euclidean unit-disk line intervals, not from the two-circle local formula. It integrates the two offset roots over a fundamental direction sector for regular Reuleaux polygons of \(m=3,5,7,9\) at three thresholds per polygon. The observed residual divided by \(\varepsilon\) decreases to zero in all four cases; its largest value at \(\varepsilon=10^{-5}\) is \(0.00018189\). A separate numerical Jensen check probes unequal angle vectors without treating arbitrary positive vectors as realizable Reuleaux polygons. The 53 deterministic assertions pass. Computation corroborates finite special cases; the general asymptotic rests on the preceding exact local analysis and finite-sector estimates.

## Relationship to prior work

Sallee (1970) and Firey (1960) treat the geometry and isoperimetric areas of both regular and irregular Reuleaux polygons, not invariant random-chord terminal laws. Bäsel (2012) and Harutyunyan–Ohanyan (2009) give invariant random-chord distributions for **straight-edged** regular polygons. Craizer–Martini (2014) study constant-width polygons in normed planes and their involutes, not the Euclidean unit-circle arc endpoint asymptotics. A published Reuleaux-triangle theorem gives the \((3/\pi)\varepsilon\log(1/\varepsilon)+O(\varepsilon)\) leading tail for invariant random lines; the current \(m=3\) leading coefficient is therefore expressly **not claimed as new**. Published results for regular Reuleaux odd-gons with independently boundary-uniform endpoints use a distinct measure and do not imply this two-term invariant-line theorem. The new contribution is the full arbitrary Reuleaux polygon class, its explicit next coefficient dependent on the *individual arc angles*, and strict regularity extremality at that order. Gates (1987), which studies terminal chord densities for general planar convex bodies, was only accessible by abstract and remains a specific residual historical-priority risk.

## Limitations

The asymptotic is pointwise in each fixed nondegenerate Reuleaux polygon; none of its error estimates is uniform under collapsing arcs, increasing side count, or width tending to zero. The probability comparison is an eventual small-deficit result, not an ordering of full chord-length distributions. It does not cover smooth arbitrary constant-width ovals, arbitrary circular-arc intersections that lack constant width, or other chord sampling conventions. The numerical tests cover regular examples and do not independently prove the irregular case. A specialist historical article could not be inspected in full, so priority remains provisional. No independent mathematical audit has been performed.

## References

1. G. T. Sallee, *Maximal Areas of Reuleaux Polygons*, Canadian Mathematical Bulletin **13** (1970), 175–179, https://doi.org/10.4153/CMB-1970-037-1 (full article inspected).
2. W. J. Firey, *Isoperimetric ratios of Reuleaux polygons*, Pacific Journal of Mathematics **10** (1960), 823–830, https://msp.org/pjm/1960/10-3/pjm-v10-n3-p.pdf (historical construction and area benchmark).
3. M. Craizer and H. Martini, *Involutes of Polygons of Constant Width in Minkowski Planes*, arXiv:1406.3205v1, publicly posted 12 June 2014, https://arxiv.org/abs/1406.3205 (primary MSC 52A10; normed-plane geometry, different problem).
4. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707v1, publicly posted 12 April 2012, https://arxiv.org/abs/1204.2707 (straight-sided polygons).
5. H. S. Harutyunyan and V. K. Ohanyan, *The chord length distribution function for regular polygons*, Advances in Applied Probability **41** (2009), 358–366, https://doi.org/10.1239/aap/1246886615 (straight-sided polygons).
6. J. Gates, *Some properties of chord length distributions*, Journal of Applied Probability **24** (1987), 863–874, https://doi.org/10.2307/3214211 (abstract inspected; full text unavailable).
7. *A logarithmic terminal chord law for the Reuleaux triangle*, previously published research result, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-a-logarithmic-terminal-chord-law-for-the-reuleaux-triangle--bbcd3963fc69/RESULT.md (full text compared; only the leading \(m=3\) case).
8. *Two-term diameter tails and logarithmic endpoint marks for regular Reuleaux odd-gons*, previously published research result, https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-two-term-diameter-tails-and-logarithmic-endpoint-marks-for-regul--c7dc1d087471/RESULT.md (full text compared; independent boundary endpoints, not invariant lines).
