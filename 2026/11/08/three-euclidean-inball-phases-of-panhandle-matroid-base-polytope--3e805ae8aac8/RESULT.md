# Three Euclidean inball phases of panhandle matroid base polytopes

## Finding

For integers \(3\le r<s\) and \(t\ge2\), let \(n=s+t\), and let \(P_{r,s,t}\subset\mathbb R^n\) be the base polytope of the panhandle matroid whose bases are the \(r\)-subsets of \([n]\) containing at most one element of \(\{s+1,\ldots,n\}\). The Euclidean metric is induced on the intrinsic hyperplane \(\sum_i z_i=r\) by the standard ambient inner product.

Put
\[
\delta=\sqrt{\frac{st}{n-1}},\qquad
u=\min\left\{\frac rn,\ \frac{1}{t+\delta},\ \frac{s+1-r}{s+\delta}\right\}.
\]
Then its exact intrinsic Euclidean inradius is
\[
\boxed{\rho(P_{r,s,t})=\sqrt{\frac{n}{n-1}}\,\nu.}
\]
All centers of balls with this radius form precisely the following convex set:
\[
\boxed{\begin{split}
\mathcal I_{r,s,t}=\{(x,y)\in\mathbb R^s\times\mathbb R^t:\ &\sum_i x_i+\sum_j y_j=r,\\
&\nu\le x_i\le 1-\nu\quad(1\le i\le s),\\
&y_j\ge\nu\quad(1\le j\le t),\\
&\sum_{j=1}^{t}y_j\le1-\delta\nu\}.\end{split}}
\]
The three barriers have genuinely different center geometry. If \(r/n\) is the unique minimum, the incenter is the unique uniform point \((r/n)\mathbf1_n\). If \(1/(t+\delta)\) is the unique minimum, every handle coordinate equals \(\nu\), and the pan coordinates form a nondegenerate \((s-1)\)-dimensional cube section. If \((s+1-r)/(s+\delta)\) is the unique minimum, every pan coordinate equals \(1-\nu\), and the handle coordinates form a \((t-1)\)-simplex. In either possible tie for the minimum, the incenter is unique. No tie of the first and third barriers can be minimal.

All three strict phases occur already for \(r\ge3\). Examples, written as \((r,s,t)\), are \((3,9,2)\) (uniform point), \((3,4,2)\) (three-dimensional cube section), and \((5,6,2)\) (line segment, i.e. a one-simplex). Both kinds of positive-dimensional center locus occur in arbitrarily high dimensions as the parameters vary.

At a relative-interior incenter, the numbers of tangent *facet hyperplanes* in the three strict regimes are respectively \(n\), \(t+1\), and \(s+1\). This is a statement about genuine facets, not redundant inequalities. The classification does not assert anything about the degenerate boundary cases \(r\le2\), \(s=r\), or \(t=1\).

## Assumptions and scope

Write \(z=(x_1,\ldots,x_s,y_1,\ldots,y_t)\). The complete base-polytope inequality description, proved in Hanely et al., Proposition 4.4, is
\[
P_{r,s,t}=\left\{(x,y)\in[0,1]^n:\sum_i x_i+\sum_j y_j=r,\quad\sum_j y_j\le1\right\}.
\]
Under \(3\le r<s\), \(t\ge2\), the nonredundant facets are exactly \(x_i=0\), \(x_i=1\), \(y_j=0\), and \(\sum_j y_j=1\). To see that each is genuinely a facet, impose its equality and choose all other defining inequalities strictly: for a pan lower facet choose handle sum \(\epsilon>0\) sufficiently small and distribute the remaining rank over \(s-1\) pan entries; for a pan upper facet distribute \(r-1-\epsilon\) over the other \(s-1\) pan entries; for a handle lower facet distribute a small positive handle sum among the others; for the handle-sum facet take \(y_j=1/t\), \(x_i=(r-1)/s\). These choices give relative-interior facet points. Individual upper handle inequalities are redundant because handle entries are nonnegative and their sum is at most one.

The answer is an intrinsic Euclidean, not an affine-invariant, measurement. No conclusion is made for a different embedding or inner product.

## Proof

**Step 1: intrinsic distances.** The tangent vector space of the rank hyperplane is \(H_0=\{v:\sum_i v_i=0\}\). Let \(\Pi\) be orthogonal projection onto \(H_0\), and define
\[
q=\|\Pi e_i\|=\sqrt{\frac{n-1}{n}},\qquad
\beta=\left\|\Pi\sum_{j=1}^{t}e_{s+j}\right\|=\sqrt{\frac{st}{n}},\qquad
\delta=\frac\beta q=\sqrt{\frac{st}{n-1}}.
\]
The distances of an interior point to the pan lower and upper facets, to each handle lower facet, and to the handle-sum facet are, respectively, \(x_i/q\), \((1-x_i)/q\), \(y_j/q\), and \((1-\sum_jy_j)/\beta\). Consequently, an intrinsic ball of radius \(R\) is contained in the polytope exactly when its center satisfies the boxed constraints in the finding with \(\nu=qR\).

**Step 2: necessary barriers without assuming symmetry.** Summing all \(n\) coordinate lower inequalities gives \(n\nu\le r\). Summing the \(t\) handle lower inequalities and using the handle-sum inequality gives \((t+\delta)\nu\le1\). Summing the \(s\) pan upper inequalities with the handle-sum inequality and the rank equation gives \((s+\delta)\nu\le s+1-r\). Pan upper and lower inequalities also imply \(\nu\le1/2\), but this is automatically weaker than \(\nu\le1/(t+\delta)\), since \(t\ge2\) and \(\delta>0\). The three advertised barriers are therefore upper bounds for every possible radius, regardless of center.

**Step 3: sufficiency.** For every \(\nu\ge0\) below all three bounds, seek a center with constant pan coordinate \(a\) and constant handle coordinate \(b\). The rank equation gives \(a=(r-tb)/s\). The inequalities are feasible exactly when the intervals
\[
\max\left\{\nu,\frac{r-s+s\nu}{t}\right\}\le b\le
\min\left\{\frac{1-\delta\nu}{t},\frac{r-s\nu}{t}\right\}
\]
overlap. Comparing both lower endpoints with both upper endpoints yields precisely the three displayed barriers and \(\nu\le1/2\). The latter is redundant as above. Thus the maximal feasible value of \(\nu\) is the displayed minimum and the radius formula follows. The full incenter locus is exactly the intersection of the eroded facet inequalities at this value; no symmetry assumption was used for that description.

**Step 4: phase geometry.** If \(r/n=\nu\), the rank equation and all lower inequalities force every coordinate to equal \(\nu\); hence the center is unique. If \(1/(t+\delta)=\nu\), the handle lower bounds and handle-sum upper bound together force \(y_j=\nu\) for all \(j\). When this barrier is strictly smaller than the other two, the pan coordinate sum lies strictly between \(s\nu\) and \(s(1-\nu)\), so the pan center locus is a full \((s-1)\)-dimensional section of \([\nu,1-\nu]^s\). If \((s+1-r)/(s+\delta)=\nu\), the pan upper bounds and handle-sum upper bound must all be equalities. This forces \(x_i=1-\nu\) for all \(i\), \(\sum_j y_j=1-\delta\nu\), and gives the translated simplex \(y_j=\nu+w_j\) with \(w_j\ge0\), \(\sum_jw_j=1-(t+\delta)\nu\). When this barrier is strictly smallest, the latter total is strictly positive, so the dimension is \(t-1\). Either equality between the second barrier and a different minimizing barrier combines its forced equalities and makes the center unique. If the first and third could both minimize, the former would force \(x_i=\nu\) and the latter \(x_i=1-\nu\), giving \(\nu=1/2\); this contradicts \(\nu\le1/(t+\delta)<1/2\).

At relative-interior incenters the only tight inequalities are exactly those claimed in the finding, establishing the tangent-facet counts. To see unbounded phase dimensions, fix \(t=2\), take \(s\) large and \(r=\lfloor s/2\rfloor\); then the second barrier is strictly smallest and \(s-1\to\infty\). Conversely, take \(s=4t+4\), \(r=s-1\), and \(t\to\infty\); the third barrier is strictly smallest and \(t-1\to\infty\). Taking \(r=3,t=2,s\to\infty\) gives the unique-center phase. Thus all phase types are substantive, not artifacts of a tiny finite example.

## Verification

The accompanying `check_panhandle.py` independently solves the full unsymmetrized Chebyshev linear program for each of 495 parameter triples with \(4\le s\le13\), \(2\le t\le10\), and \(3\le r<s\). It compares the optimum with the exact formula and constructs a symmetric feasible center from the proven endpoint interval. It additionally checks genuine facets and vertices in small parameter cases by enumeration and convex-hull rank. Representative test triples include all three strict regimes, the exact first/second barrier tie \((3,8,2)\), and the second/third tie \((149,154,22)\). The execution prints `PANHANDLE_INBALL_TESTS_PASSED`. Dependencies are `numpy` and `scipy`; run `python check_panhandle.py`.

These finite experiments only corroborate the general analytic proof; they are not an exhaustive verification for unbounded parameters. Distances, the three upper bounds, the feasibility equivalence, and the dimensional classifications are analytically proved above.

## Relationship to prior work

Hanely, Martin, McGinnis, Miyata, Nasr, Vindas-Meléndez, and Yin introduced the panhandle matroid framework used here and give its complete base-polytope description in Proposition 4.4; the facet description is not claimed as new. Deligeorgaki, McGinnis, and Vindas-Meléndez study the Ehrhart theory of these same polytopes. Benedetti-Velásquez, Knauer, and Valencia-Porras study lattice-path matroid polytopes, including their alcoved triangulations and enumerative geometry. These inspected works provide different invariants, not an intrinsic inball phase classification.

A published exact Euclidean inradius result for *rank-two* matroid base polytopes covers the excluded case \(r=2\). Other nearby results for ordinary hyperplane slices of boxes do not include the extra handle-sum truncation; results on minimum-enclosing spheres solve a different optimization problem. The present claim is confined to \(r\ge3\), \(s>r\), \(t\ge2\), with no assertion of priority in the overlapping rank-two cases.

## Limitations

The formulas use the standard Euclidean realization and the stated nondegenerate parameters. The result is a complete classification only within this domain; it does not derive John or Löwner ellipsoids, an Ehrhart polynomial, or global extremality among all matroids. Targeted literature searches do not prove absolute novelty; a general Chebyshev-center theorem in the broader generalized-permutohedron literature could conceivably imply the result. Independent mathematical audit has not been performed.

## References

1. D. Hanely, J. L. Martin, D. McGinnis, D. Miyata, G. D. Nasr, A. R. Vindas-Meléndez, and M. Yin, *Ehrhart Theory of Paving and Panhandle Matroids*, arXiv:2201.12442, first posted 2022-01-28, especially Definition 4.1 and Proposition 4.4. https://arxiv.org/abs/2201.12442
2. D. Deligeorgaki, D. McGinnis, and A. R. Vindas-Meléndez, *Ehrhart Bounds for Panhandle and Paving Matroids Through Enumeration of Chain Forests*, arXiv:2311.01640, first posted 2023-11-02. https://arxiv.org/abs/2311.01640
3. C. Benedetti-Velásquez, K. Knauer, and J. Valencia-Porras, *On Lattice Path Matroid Polytopes: Alcoved Triangulations and Snake Decompositions*, freely available manuscript. https://www.ub.edu/comb/koljaknauer/Ehrhart_Theory_of_Lattice_Path_Matroid_Polytopes-2.pdf
4. *Exact Euclidean inradius of connected rank-two matroid base polytopes*, public research record (rank-two case only). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-euclidean-inradius-of-connected-rank-two-matroid-base-poly--04d0301093d4
