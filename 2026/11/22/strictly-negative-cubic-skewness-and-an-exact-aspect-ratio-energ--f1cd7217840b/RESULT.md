# Strictly negative cubic skewness and an exact aspect-ratio energy for random box shadows

## Finding
Let \(Q\subset\mathbb R^3\) be a right rectangular box with arbitrary positive edge lengths \(a,b,c\), let \(U\) be Haar-uniform on the sphere \(S^2\), and let \(B\) be the ordinary two-dimensional area of its orthogonal projection onto \(U^\perp\). Write \(V=abc\) and \(\kappa_3(B)=\mathbb E[(B-\mathbb EB)^3]\). Then the *complete exact cubic central-moment identity* is
\[
\boxed{\frac{\kappa_3(B)}{V^2}
=\frac{3(7\pi-22)}{4\pi}
-\frac{16-5\pi}{8\pi}
\left(\frac{(a-b)^2}{ab}+\frac{(b-c)^2}{bc}+\frac{(c-a)^2}{ca}\right).}
\]
Consequently every such random shadow-area distribution has **strictly negative skewness**, and
\[
\boxed{\kappa_3(B)\le\frac{3(7\pi-22)}{4\pi}V^2<0,}
\]
with equality in the first inequality if and only if \(a=b=c\). The exact inequality deficit measures the positive, dimensionless aspect-ratio energy shown in the first display; no unproved stability constant is hidden. The optimal normalized upper bound is approximately \(-0.0021131220325463\), attained by every cube.

This result concerns the third *central moment*, not the third raw moment, and its upper extremum is a negative quantity. It does not assert that the *standardized* skewness \(\kappa_3/\operatorname{Var}(B)^{3/2}\) is maximized at cubes.

## Assumptions and scope
The box is a full-dimensional Euclidean orthotope, its edge lengths satisfy \(a,b,c>0\), and the viewing plane is unoriented and Haar-distributed. Its orthogonal shadow is a planar convex polygon (almost surely a hexagon). All expectations are population expectations over the random plane, not empirical estimates. The volume \(V\) is the ordinary spatial volume. The stated optimality is at fixed volume, or equivalently for the normalized cubic moment, and is unaffected by rotation, translation, scale, or reordering the edges.

## Proof
**1. Exact shadow-area reduction.** The box has pairs of congruent opposite faces with areas \(bc,ac,ab\). For each direction \(U=(U_1,U_2,U_3)\in S^2\), Cauchy's brightness formula, or equivalently the planar zonotope mixed-area formula, gives
\[
B=bc\lvert U_1\rvert+ac\lvert U_2\rvert+ab\lvert U_3\rvert.
\]
This identity includes orientations with projected degeneracies, by continuity. Set \(x=bc\), \(y=ac\), \(z=ab\), \(s=x+y+z\), \(q=xy+yz+zx\), and \(r=xyz=(abc)^2=V^2\).

**2. Spherical absolute moments, including the third mixed moment.** Put \(X_i=\lvert U_i\rvert\). The squared coordinates of a uniform point on \(S^2\) have the Dirichlet law with all parameters \(1/2\), so for nonnegative exponents \(\alpha_i\),
\[
\mathbb E\prod_{i=1}^3X_i^{\alpha_i}
=\frac{\Gamma(3/2)}{\Gamma((3+\alpha_1+\alpha_2+\alpha_3)/2)}
\prod_{i=1}^3\frac{\Gamma((1+\alpha_i)/2)}{\Gamma(1/2)}.
\]
This identity follows directly by normalizing three independent standard Gaussian coordinates and applying the beta-gamma integral. In particular, for distinct indices \(i,j,k\),
\[
\mathbb EX_i=\tfrac12,\quad
\mathbb EX_i^2=\tfrac13,\quad
\mathbb EX_i^3=\tfrac14,\quad
\mathbb EX_iX_j=\tfrac2{3\pi},\quad
\mathbb EX_i^2X_j=\tfrac18,\quad
\mathbb EX_1X_2X_3=\tfrac1{4\pi}.
\]
The last two mixed moments matter: neither can be replaced by a product of lower moments, because the viewing coordinates are dependent.

**3. First three exact raw moments and centralization.** Expand \(B=xX_1+yX_2+zX_3\) and substitute the preceding sphere integrals. The result is
\[
\begin{aligned}
\mathbb EB&=\frac{s}{2},\\
\mathbb EB^2&=\frac{s^2}{3}+\left(\frac4{3\pi}-\frac23\right)q,\\
\mathbb EB^3&=\frac{s^3}{4}-\frac{3sq}{8}+\frac{3(4-\pi)}{8\pi}r.
\end{aligned}
\]
For example, the all-distinct term in the last line has coefficient \(6\mathbb EX_1X_2X_3=3/(2\pi)\) before conversion from monomials to elementary symmetric functions. The identity \(\kappa_3=\mathbb EB^3-3(\mathbb EB)(\mathbb EB^2)+2(\mathbb EB)^3\) gives, after exact cancellation of the \(s^3\)-terms,
\[
\boxed{\kappa_3(B)=\frac{3(4-\pi)}{8\pi}r-\frac{16-5\pi}{8\pi}sq.}
\]
This is a finite algebraic identity for every positive \(x,y,z\).

**4. Exact aspect-ratio energy and sharpness.** Since \(r=xyz\),
\[
\frac{sq-9r}{r}
=(x+y+z)\left(\frac1x+\frac1y+\frac1z\right)-9
=\sum_{i<j}\frac{(x_i-x_j)^2}{x_ix_j}
=\frac{(a-b)^2}{ab}+\frac{(b-c)^2}{bc}+\frac{(c-a)^2}{ca},
\]
where \((x_1,x_2,x_3)=(bc,ac,ab)\). Substituting \(sq=9r+(sq-9r)\) into step 3 gives the displayed theorem exactly. The elementary classical bounds \(\pi<22/7\) and \(\pi<16/5\) show respectively that \(7\pi-22<0\) and \(16-5\pi>0\). Therefore \(\kappa_3(B)<0\) for all positive sides. The energy vanishes if and only if all three sides agree, proving sharp cube equality. This proves *all* quantifiers without numerical extrapolation.

## Verification
Execute `python3 verify.py` with only the Python 3 standard library. The script compares the closed moment identity against the independently expanded raw-moment formula for five boxes, estimates the first three moments with 300,000 Haar samples for each of those boxes, and independently projects all eight vertices to the random viewing plane to compare the actual convex-hull area with the brightness formula on 360 further directions. The recorded replay produced both `BOX_SHADOW_CUBIC_SKEWNESS_CHECKS_OK` and `BOX_SHADOW_HULL_GEOMETRY_CHECKS_OK`. The maximum diagnostic discrepancy among the five normalized raw-moment sample comparisons was below \(0.003\). These are finite checks: the proof is the exact sphere-moment and algebraic argument, not Monte Carlo.

## Relationship to prior work
Vickers and Brown (2001), Sections 3(b) and 4(c), already derive the projected-area distribution for cuboids, including their exact brightness formula and examples; they credit Walters (1947) with a seven-part formula for the general cuboid distribution. These facts and the complete distribution are *not* claimed new. The Vickers–Brown full text describes extrema, PDFs and joint area–perimeter distributions; no all-box strict third-cumulant sign or sharp squared-aspect-ratio deficit was identified in the inspected sections. Finch (2012), Sections 2.2 and 5, examines mean and second shadow moments for a cube and explicitly cites the same older distribution literature, not this third-central-moment rigidity. Yan and Wang (2015) investigate general mixed brightness integrals and extremal inequalities for projection bodies, without specifying this cuboid cubic-cumulant identity.

The published result *Exact planar shadow-area moments for all orthotopes* (record `0d2368f94d4d`) determines first and second shadow-area moments for arbitrary dimensions; its full proof explicitly does not determine higher moments. The published result *Three perimeter moments reconstruct every rectangular box from unoriented random shadows* (record `be3a7e96608c`) uses *perimeter*, a different random variable. A cited published result *Sharp finite-moment tomography of orthotopes in every dimension* (record `cb0a2e3c75db`) reconstructs sides from moments of *hyperplane projected volume*, which in dimension three is the same raw shadow-area variable. This creates a real **moment-level overlap**: the third raw-moment coefficient may already be known from that study. The present novelty claim is deliberately restricted to the exact sharp *central-cumulant sign and aspect-ratio stability identity*; it does not claim new moment-based side reconstruction or the first three raw moments in isolation. The 1947 full cuboid PDF and any earlier treatment of its inequalities remain material priority risks.

## Limitations
The identity is specific to Haar-uniform plane orientations and right rectangular boxes in three dimensions; no result is asserted for biased directions, skew parallelotopes, arbitrary convex bodies, or higher dimensions. It is a theorem about the population cubic central moment, not the full distribution, estimation error, or standardized skewness. A known analytic distribution of projected cuboid areas implies in principle that all moments are integrable from existing formulae; the additional claimed content is the precise universal sign, optimal cube inequality, and equality/stability law. Their historical priority has not been independently certified. Numerical samples and source searches do not establish novelty.

## References
1. G. T. Vickers and D. J. Brown, *The distribution of projected area and perimeter of convex, solid particles*, Proceedings of the Royal Society A 457 (2001), 283–306, DOI: 10.1098/rspa.2000.0667, https://www.academia.edu/60865860/The_distribution_of_projected_area_and_perimeter_of_convex_solid_particles (full text inspected).
2. A. G. Walters, *The distribution of projected areas of fragments*, Proceedings of the Cambridge Philosophical Society 43 (1947), 343–347, DOI: 10.1017/S0305004100023574 (text not verified; its general cuboid formula is described by Vickers and Brown).
3. Steven R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1, first publicly posted 2012-03-12, https://arxiv.org/abs/1203.2464 (complete HTML text inspected).
4. Li Yan and Weidong Wang, *General \(L_p\)-mixed-brightness integrals*, Journal of Inequalities and Applications 2015:190, first published 2015-06-12, https://doi.org/10.1186/s13660-015-0708-2 (open HTML full text inspected).
5. *Exact planar shadow-area moments for all orthotopes*, published mathematical record `0d2368f94d4d`, 2026; full result inspected at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-planar-shadow-area-moments-for-all-orthotopes--0d2368f94d4d.
6. *Three perimeter moments reconstruct every rectangular box from unoriented random shadows*, published mathematical record `be3a7e96608c`, 2026; full result inspected at https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-three-perimeter-moments-reconstruct-every-rectangular-box-from-u--be3a7e96608c.
