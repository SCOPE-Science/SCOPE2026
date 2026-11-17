# Four exact top triangle-area shells in regular \(3m\)-gons and a cubic near-tie

## Finding

For every integer \(m\ge3\), let \(N=3m\), and let \(P_N\) be the regular \(N\)-gon of circumradius one in the Euclidean plane. For each unordered set of three distinct polygon vertices, take its Euclidean triangle area. Among these \(\binom N3\) areas, the **four highest distinct values** \(A_1>A_2>A_3>A_4\) are attained by exactly the following unordered triples of positive cyclic arc gaps (measured as numbers of polygon sides between successive chosen vertices):

| Rank | Sorted gaps | Number of unordered vertex triangles |
| --- | --- | ---: |
| 1 | \((m,m,m)\) | \(N/3\) |
| 2 | \((m-1,m,m+1)\) | \(2N\) |
| 3 | \((m-1,m-1,m+2)\) | \(N\) |
| 4 | \((m-2,m+1,m+1)\) | \(N\) |

Set \(s=\sin(\pi/N)\) and \(c=\cos(\pi/N)\). The **exact consecutive gaps between these four area values** are
\[
\begin{aligned}
A_1-A_2&=\sqrt3\,s^2,\\
A_2-A_3&=2cs^2(\sqrt3\,c-s),\\
A_3-A_4&=4cs^3.
\end{aligned}
\]
In particular, \(A_1=3\sqrt3/4\), and the sharp third-to-fourth area separation satisfies
\[
A_3-A_4\sim \frac{4\pi^3}{N^3}\quad(N\to\infty,\ 3\mid N),
\]
whereas the two preceding separations have strictly positive quadratic leading orders \(\sqrt3\pi^2/N^2\) and \(2\sqrt3\pi^2/N^2\). Thus the two competing next-nearest shapes are closer by one asymptotic order than either is to the optimal levels.

## Assumptions and scope

Only **vertex-supported**, unordered, nondegenerate triangles are ranked. A continuous choice of vertices on the circumcircle is a different problem. The polygon has positive circumradius one; for another circumradius \(R>0\) all area levels and gaps are multiplied by \(R^2\). The restriction \(m\ge3\) makes all four listed cyclic gap triples positive. Distinct values means distinct real Euclidean areas, not different triangle congruence types. Rotations or reflections count as different vertex subsets if the subsets differ.

## Proof

**1. Exact area parametrization.** A triangle selected from distinct vertices in cyclic order has positive integer arc gaps \(a,b,d\) with \(a+b+d=N\). All such triples arise. Since the circumradius of the selected triangle is one and its consecutive chord lengths are \(2\sin(\pi a/N)\), \(2\sin(\pi b/N)\), \(2\sin(\pi d/N)\), the formula \(\operatorname{area}=uvw/(4R)\) gives
\[
F(a,b,d)=2\sin(\pi a/N)\sin(\pi b/N)\sin(\pi d/N).
\]
The area depends only on the unordered gap triple.

**2. Strict dominance.** The second derivative of \(f(x)=\log\sin(\pi x/N)\) is \(- (\pi/N)^2\csc^2(\pi x/N)<0\) on \(0<x<N\). Therefore \(\log F=\log 2+f(a)+f(b)+f(d)\) is strictly Schur-concave. In particular, among sorted triples \(a\le b\le d\) of common sum \(3m\), a triple with no larger minimum and no smaller maximum has strictly lower area unless the triples coincide: this is the strict three-coordinate majorization criterion.

**3. Exhaustive ordering reduction.** If \(a\ge m\), the sum constraint gives only \((m,m,m)\). If \(a=m-1\), then \(b+d=2m+1\) and \(m-1\le b\le d\); the only possibilities are \((m-1,m,m+1)\) and \((m-1,m-1,m+2)\). Finally, if \(a\le m-2\), then \(d\ge m+1\), because otherwise \(a+b+d\le(m-2)+2m<3m\). Hence every such sorted triple majorizes \((m-2,m+1,m+1)\). Strict concavity shows that this last triple uniquely maximizes area among all triples with \(a\le m-2\). The first and second triples are strictly above the third by the dominance criterion. The third and fourth are **incomparable by majorization**, so one exact comparison remains.

**4. Incomparable-pair calculation.** Put \(\theta=\pi/N\), \(s=\sin\theta\), \(c=\cos\theta\); then \(m\theta=\pi/3\). For the third and fourth shapes the area formula gives
\[
\begin{aligned}
A_3&=2\sin^2(\pi/3-\theta)\sin(\pi/3+2\theta),\\
A_4&=2\sin(\pi/3-2\theta)\sin^2(\pi/3+\theta).
\end{aligned}
\]
Expanding \(\sin(\pi/3\pm\theta)=\sqrt3 c/2\pm s/2\), and \(\sin(\pi/3\pm2\theta)=\sqrt3(c^2-s^2)/2\pm cs\), and using \(c^2+s^2=1\), gives the exact identity \(A_3-A_4=4cs^3>0\). Thus there is no additional triangle at or above the fourth area level. Similarly \(A_1=3\sqrt3/4\) and \(A_2=\sqrt3(3/4-s^2)\), while direct expansion yields \(A_2-A_3=2cs^2(\sqrt3 c-s)>0\), since \(0<\theta\le\pi/9\). All three differences are strictly positive.

**5. Equality counts.** For a specified sorted gap multiset with \(r\) distinct orderings, choosing a starting polygon vertex gives \(Nr\) ordered-start records, and each unordered triangle is recorded exactly three times (once for each selected starting vertex). Thus its number of distinct vertex triangles is \(Nr/3\). Here \(r=1\) for rank one, \(r=6\) for rank two, and \(r=3\) for each of ranks three and four. This gives the exact counts above.

**6. Cubic separation.** Since \(\sin\theta\sim\theta\) and \(\cos\theta\to1\), the gap \(4cs^3\) is asymptotic to \(4\pi^3/N^3\). In contrast, the first and second differences are respectively asymptotic to \(\sqrt3\pi^2/N^2\) and \(2\sqrt3\pi^2/N^2\). This proves the claimed one-order separation.

## Verification

Running `python3 check_triangle_shells.py` reconstructs all triangles **independently from Euclidean Cartesian coordinates**, groups the top four areas, compares their exact predicted shapes and multiplicities, and checks the three trigonometric gap formulas numerically for every multiple of three from \(N=9\) through \(N=84\). A passing run examines 707,434 unordered triangles across 26 polygon orders. Its floating-point comparisons are only finite consistency checks; the analytical argument above establishes the infinite result.

## Relationship to prior work

Lee, Eom and Ahn (arXiv:2007.12330, first public July 24, 2020) analyze algorithms for largest inscribed triangles, including fixed-angle variants. Ismailescu, Kim and Wang (arXiv:2104.12172, first public April 25, 2021) develop sharp guarantees for maximal-area subpolygons of general convex polygons. Neither inspected manuscript gives the four ranked **vertex-triangle area shells** of the regular \(3m\)-gon or the cubic gap between the two incomparable third- and fourth-ranked shapes.

Huber's 2026 OEIS entry A400213 provides the same general sine-product parametrization and a classification of **equal** triangle areas for regular polygons. Those known ingredients are acknowledged. The contribution here is the global first-four *ordering* for every \(m\ge3\), equality multiplicities, and the exact positive \(4cs^3\) splitting and asymptotic scale; neither an area formula nor an equal-area count alone states these comparisons. The related Zenodo full text was not available for complete comparison; historical priority remains subject to that residual risk.

## Limitations

This is a theorem on the four largest **distinct** vertex-supported triangle areas, not the whole area spectrum, and not a statement about continuously variable triangles. It is not extended here to polygon orders not divisible by three. The originality comparison includes accessible full text of two earlier papers and the text of A400213; an inaccessible linked Zenodo manuscript may contain additional material. Numerical checker outputs supplement but do not substitute for the all-dimensions proof. Independent mathematical audit has not been performed.

## References

- S. Lee, T. Eom, H.-K. Ahn, *Largest triangles in a polygon*, arXiv:2007.12330 (first version July 24, 2020), https://arxiv.org/html/2007.12330v1.
- D. Ismailescu, M. J. Kim, E. Wang, *On the maximum area of inscribed polygons*, arXiv:2104.12172 (first version April 25, 2021), https://arxiv.org/abs/2104.12172.
- F. Huber, *Number of distinct areas of triangles formed by three vertices of a regular n-gon*, OEIS A400213 (October 2026), https://oeis.org/A400213, referring to *Equal Areas of Vertex Triangles in a Regular Polygon*, https://doi.org/10.5281/zenodo.23170951.
