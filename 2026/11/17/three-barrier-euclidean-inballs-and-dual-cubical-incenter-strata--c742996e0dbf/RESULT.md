# Three-barrier Euclidean inballs and dual cubical incenter strata of elementary split matroid polytopes

## Finding
Let \(n=h+s\), \(h,s\ge4\), and let integers \(r,u\) satisfy \(2\le r\le h-2\), \(2\le u\le s-2\). Put \(k=r+u\) and
\[P_{h,s;r,u}=\{x\in[0,1]^n:\sum_{i=1}^n x_i=k,\ \sum_{i=1}^h x_i\le r\}.\]
This is the full-dimensional base polytope of an elementary split (Schubert) matroid, in its standard Euclidean realization. Put
\[q=\sqrt{(n-1)/n},\quad p=\sqrt{hs/n},\quad
R_0=\frac{\min(k,n-k)}{nq},\quad R_L=\frac r{hq+p},\quad R_U=\frac{s-k+r}{sq+p}.\]
The exact intrinsic Euclidean inradius is \(R=\min(R_0,R_L,R_U)\). With \(t=qR\), *all* centers of maximal inscribed balls are exactly
\[\mathcal I=\{c:\sum_i c_i=k,\ t\le c_i\le1-t,\ \sum_{i=1}^h c_i\le r-pR\}.\]
If \(R_0\) is minimal, the center is uniquely the uniform vector \((k/n)\mathbf1\). If \(R_L<\min(R_0,R_U)\), all first \(h\) coordinates equal \(t\), and the last \(s\) coordinates form an \((s-1)\)-dimensional cube section. If \(R_U<\min(R_0,R_L)\), all last \(s\) coordinates equal \(1-t\), and the first \(h\) coordinates form an \((h-1)\)-dimensional cube section. If \(R_L=R_U<R_0\), the center is uniquely \((t\mathbf1_h,(1-t)\mathbf1_s)\). Every tie involving \(R_0\) also has a unique center. Thus the only positive-dimensional loci are the two genuine cube-section phases, not merely simplex degenerations.

A hyperplane \(x_i=0\) touches the maximal ball at center \(c\) exactly when \(c_i=t\); \(x_i=1\) touches exactly when \(c_i=1-t\); the additional split facet touches exactly when \(\sum_{i\le h}c_i=r-pR\). These statements give every contact at every incenter, including boundary strata.

In either strict cubical phase let \(m=s\), \(\alpha=(k-nt)/(1-2t)\) in the lower phase, or \(m=h\), \(\alpha=(k-s+(s-h)t)/(1-2t)\) in the upper phase. Then the locus is congruent to \((1-2t)\{y\in[0,1]^m:\sum_jy_j=\alpha\}\). Its exact vertex count is \(\binom m\alpha\) for integral \(\alpha\) (where this denotes the ordinary binomial coefficient), and \(m\binom{m-1}{\lfloor\alpha\rfloor}\) for nonintegral \(\alpha\). In the integral case the notation means \(\binom{m}{\alpha}\) with integer lower argument. Both non-simplex cube-section phases occur; for example \((n,k,h,r)=(9,4,4,2)\) is a lower-phase five-coordinate section with 30 vertices, while \((9,5,5,3)\) is an upper-phase five-coordinate section with 30 vertices.

## Assumptions and scope
All distances are intrinsic to the rank hyperplane \(\sum x_i=k\) using the ambient standard Euclidean metric. The parameter bounds ensure the cut is genuine and the polytope is full-dimensional; in particular, no coordinate bound is redundant. The notation \(\binom m\alpha\) above is used only when \(\alpha\) is an integer.

## Proof
Let \(H_0=\{v:\sum_i v_i=0\}\) and let \(\Pi\) denote orthogonal projection to \(H_0\). The projected normals of the coordinate facets have length \(\|\Pi e_i\|=q\); the projected normal of the additional split facet has length \(\|\Pi\mathbf1_{[h]}\|=p\). A ball of radius \(R\) is therefore contained in \(P_{h,s;r,u}\) precisely when its center satisfies the displayed eroded inequalities. Set \(t=qR\).

The rank equality and the coordinate bounds give \(nt\le k\le n(1-t)\), i.e. \(R\le R_0\). The split inequality combined with the lower bounds on the first \(h\) coordinates gives \(ht\le r-pR\), i.e. \(R\le R_L\). Combining the upper bounds on the last \(s\) coordinates with the rank equality and split inequality gives \(k-s(1-t)\le r-pR\), i.e. \(R\le R_U\). These bounds hold for **every** center.

Conversely, under all three bounds there is a permissible value for the first-block sum \(X\) in
\[\max\{ht,k-s(1-t)\}\le X\le \min\{h(1-t),k-st,r-pR\}.\]
Indeed, the six pairwise comparisons of the two lower endpoints with the three upper endpoints reduce exactly to the three displayed barriers and \(t\le1/2\); the latter follows from \(nt\le\min(k,n-k)\). Choosing constant coordinates \(X/h\) and \((k-X)/s\) on the two blocks constructs a feasible center. The claimed radius is attained.

If \(R=R_0\), summing the coordinates that attain the lower or upper box bounds forces all coordinates to be \(k/n\). If \(R=R_L\), the first-block lower-sum inequality and the split inequality must both be equalities, so every coordinate in the first block is \(t\). If \(R=R_U\), the second-block upper-sum inequality and the split inequality must be equalities, forcing every second-block coordinate to be \(1-t\). Under a strict second or third barrier, the remaining block sum lies strictly between its box extremes, giving a full \((m-1)\)-dimensional cube section. If both block barriers tie, their forced equalities determine the unique stated center. Equalities involving \(R_0\) also yield uniqueness. The eroded inequalities characterize every boundary-stratum tangency by equality.

Finally, a vertex of a nonintegral cube section has exactly one fractional coordinate; choosing this coordinate and the \(\lfloor\alpha\rfloor\) unit coordinates proves the vertex formula. At integral \(\alpha\), precisely the zero-one points with \(\alpha\) ones are vertices. This also proves the claimed counts. For \((9,4,4,2)\), \(\alpha\approx2.735\), giving \(5\binom42=30\); for \((9,5,5,3)\), \(\alpha\approx2.265\), giving the same number.

## Verification
The included `verify_inball.py` independently solves the unrestricted Chebyshev linear program for every 2,380 admissible parameter quadruples within \(8\le n\le21\). It confirms all three radius branches and constructs an independent explicit block-constant feasibility witness. Run `python verify_inball.py` with Python, SciPy. The expected exact output prefix is `ELEMENTARY_SPLIT_INBALL_PASS cases=2380`. These numerical checks are finite corroboration; the general proof above is analytic.

## Relationship to prior work
The single-split description of the Schubert elementary split matroid polytope is established in the split-matroid literature and is not new. Hanely et al. (2022) study Ehrhart and paving-matroid truncations. The earlier geometric classification of **panhandle matroid** inballs treats the one-sided capacity-one case, where the upper-regime incenter is a simplex, not a general cube section. Here both block capacities are strictly interior and both types of potentially high-complexity cube sections occur; none of the inspected result statements gives these general four-parameter radii and all-incenter classifications. These relationships limit the scope of the originality claim; an earlier general Euclidean-center theorem might imply the formulas.

## Limitations
This concerns a single integral split cut, with the stated genuinely two-sided parameters; it does not address arbitrary intersections of multiple split inequalities. The numbers of incenter-locus vertices are conditional on the explicit real level \(\alpha\), not asserted to be distinct for all parameters. Historical priority is not independently established. No independent audit has been performed.

## References
1. D. Hanely et al., *Ehrhart Theory of Paving and Panhandle Matroids*, arXiv:2201.12442, first publicly posted 2022-01-28. https://arxiv.org/abs/2201.12442
2. M. Joswig and B. Schröter, *Matroids from hypersimplex splits*, arXiv:1607.06291, first posted 2016-07-21. https://arxiv.org/abs/1607.06291
3. L. Ferroni and B. Schröter, *Face enumeration for split matroid polytopes*, Cambridge Core full text, especially Section 2.2 and equation (1). https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/face-enumeration-for-split-matroid-polytopes/8AB800A4A0AAB1AEF4720C07899107AF
4. *Three Euclidean inball phases of panhandle matroid base polytopes*, public mathematical research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-euclidean-inball-phases-of-panhandle-matroid-base-polytope--3e805ae8aac8
