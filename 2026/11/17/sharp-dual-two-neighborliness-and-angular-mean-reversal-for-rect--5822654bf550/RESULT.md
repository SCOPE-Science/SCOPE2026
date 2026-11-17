# Sharp dual two-neighborliness and angular mean reversal for rectangular matching polytopes

## Finding
For integers \(p,q\ge2\), let \(\mathcal M_{p,q}\subset\mathbb R^{p\times q}\) be the convex hull of all \(0\)-\(1\) matrices having at most one nonzero entry in each row and column, endowed with the ordinary Frobenius Euclidean metric. It has \(F=pq+p+q\) facets. Define
\[
 B=pq\mathbf 1_{\{q=2\}}+pq\mathbf 1_{\{p=2\}}+\binom p2\mathbf 1_{\{q=2\}}+\binom q2\mathbf 1_{\{p=2\}},\qquad R=\binom F2-B.
\]
The total number of ridges is exactly \(R\). All pairs of facets form a ridge except: (a) a zero-entry facet and its incident row facet if \(q=2\); (b) a zero-entry facet and its incident column facet if \(p=2\); (c) two different row facets if \(q=2\); (d) two different column facets if \(p=2\). Consequently, the polar about any interior point is \(2\)-neighborly if and only if \(p,q\ge3\).

The complete multiset of **interior** ridge dihedral angles is:

| Angle | Number of ridges |
|---|---:|
| \(\arccos(1/\sqrt q)\) | \(pq\mathbf 1_{\{q\ge3\}}\) |
| \(\arccos(1/\sqrt p)\) | \(pq\mathbf 1_{\{p\ge3\}}\) |
| \(\pi-\arccos(1/\sqrt{pq})\) | \(pq\) |
| \(\pi/2\) | \(R-pq(1+\mathbf1_{\{q\ge3\}}+\mathbf1_{\{p\ge3\}})\) |

When two displayed angles coincide, their multiplicities are added. A uniformly chosen ridge angle \(\Theta_{p,q}\) consequently satisfies
\[
\mathbb E\Theta_{p,q}=\frac\pi2+\frac{pq}{R}\left[\arcsin\frac1{\sqrt{pq}}-\mathbf1_{\{q\ge3\}}\arcsin\frac1{\sqrt q}-\mathbf1_{\{p\ge3\}}\arcsin\frac1{\sqrt p}\right].
\]
The mean is obtuse exactly in the exceptional \((p,q)=(2,2)\) case, when \(\mathbb E\Theta_{2,2}=\pi/2+\pi/27\); it is strictly acute for every other pair \(p,q\ge2\). In the square sequence, \(n^{5/2}(\pi/2-\mathbb E\Theta_{n,n})\to4\).

## Assumptions and scope
The Euclidean inner product is \(\langle X,Y\rangle=\sum_{i=1}^p\sum_{j=1}^q X_{ij}Y_{ij}\), with no normalization. A ridge means a face of dimension \(pq-2\). Two facets that intersect in a lower-dimensional face do not contribute a ridge. All row and column bounds are at most \(1\); there are no prescribed positive margins. The statement concerns the full-dimensional *partial* matching polytope, not the fixed-cardinality assignment or doubly stochastic face.

## Proof
By the integral bipartite-matching formulation, equivalently Proposition 3.4 and Corollary 3.5 of Heuer--Striker, the following are all the irredundant facet inequalities:
\[
 Z_{ij}:X_{ij}\ge0,\qquad A_i:\sum_{j=1}^qX_{ij}\le1,\qquad B_j:\sum_{i=1}^pX_{ij}\le1.
\]
The origin and all single-entry matrices show full dimension. In this section each asserted ridge is certified by a point making its two defining inequalities equalities and all other facet inequalities strict. Such a point has an open relative neighborhood in their two-hyperplane intersection and hence gives a face of dimension \(pq-2\). All pairs of different facet normals are independent.

Two zero-entry facets are certified by assigning both specified entries zero and all remaining entries the same sufficiently small positive value \(\varepsilon\). For \(Z_{ab}\) and a nonincident row facet \(A_i\), \(a\ne i\), put \(1/q\) in every entry of row \(i\), put zero at \((a,b)\), and put \(\varepsilon\) elsewhere. The analogous construction handles a nonincident column facet.

If \(q\ge3\), the pair \(Z_{ij},A_i\) has a strict witness with \(X_{ij}=0\), every other entry in row \(i\) equal to \(1/(q-1)\), and every other entry \(\varepsilon>0\). Similarly \(Z_{ij},B_j\) has a strict witness when \(p\ge3\). If \(q=2\), however, \(Z_{ij},A_i\) forces the only other entry in row \(i\) to equal \(1\), consequently also forcing the corresponding column facet to be tight. Its normal is independent of the selected normals because \(p\ge2\). Thus this intersection has codimension at least three. The \(p=2\) column statement is symmetric.

For two row facets \(A_i,A_k\), if \(q\ge3\) put \(1/q\) in each entry of those two rows and \(\varepsilon\) elsewhere; every column sum is then strictly less than one for sufficiently small \(\varepsilon\). If \(q=2\), the two rows exhaust the total column capacity of two, forcing both column constraints to be tight (and all other rows to vanish), so the intersection has codimension at least three. The two-column case is the transpose with condition \(p\ge3\).

For a row facet \(A_i\) and column facet \(B_j\), choose \(0<t<1\), set \(X_{ij}=t\), set \(X_{i\ell}=(1-t)/(q-1)\) for \(\ell\ne j\), set \(X_{kj}=(1-t)/(p-1)\) for \(k\ne i\), and set the other entries to a sufficiently small positive \(\varepsilon\). Only \(A_i\) and \(B_j\) are tight. This completes the exhaustive ridge-pair classification and the formula for \(B\) and \(R\).

The **outward** normal vectors of these facets are respectively \(-e_{ij}\), \(\sum_j e_{ij}\), and \(\sum_i e_{ij}\), with squared lengths \(1,q,p\). For an actual ridge, its interior angle equals \(\pi\) minus the angle between the outward normals. Their only nonzero scalar products are \(-1\) for an incident zero-entry/row pair, \(-1\) for an incident zero-entry/column pair, and \(+1\) for a row/column pair. Those products yield the three non-right rows of the angle table; all other permitted ridge pairs are right. Each of the first two types exists for exactly \(pq\) choices when its side-length condition holds, and there are always \(pq\) row/column pairs. This gives the complete multiplicities and the expectation formula.

For \((p,q)=(2,2)\), no acute pair remains, \(F=8\), \(R=18\), and exactly four ridges have angle \(2\pi/3\). Hence the mean is \(\pi/2+\pi/27\). If exactly one side has size two, the mean shift is a positive factor times \(\arcsin(1/\sqrt{pq})-\arcsin(1/\sqrt{\max\{p,q\}})<0\). If both sides have size at least three, its shift is a positive factor times \(\arcsin(1/\sqrt{pq})-\arcsin(1/\sqrt q)-\arcsin(1/\sqrt p)<0\). Finally, for \(p=q=n\), \(R=\binom{n^2+2n}{2}\), and \(\arcsin z=z+O(z^3)\) implies \(n^{5/2}(\pi/2-\mathbb E\Theta_{n,n})\to4\).

## Verification
The standalone \(\texttt{geometry_checker.py}\) enumerates every partial matching vertex and every pair of facet equalities for eight cases \((p,q)\in\{(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,3),(4,4)\}\). It calculates affine face dimension via exact modular Gaussian elimination over the prime field of order \(1000003\), checks all predicted ridge/nonridge cases, and checks signed normal products and squared cosines exactly as rational numbers. In particular, a modular rank of \(pq-2\) certifies the existence of that many rationally independent face directions. The checker prints \(\texttt{MATCHING_RIDGE_EXACT_PASS cases=8}\). The full infinite-parametric result is established by the preceding explicit witnesses and forced extra equalities, not by finite enumeration.

## Relationship to prior work
The full facet inequality system, polytope dimension, and vertex/total-facet enumerations are established background (Heuer--Striker, Section 3), not new claims. Cao--Chen study the face lattice of square doubly substochastic polytopes, a closely related preexisting combinatorial theory; their full text was not accessible for this comparison. Such results could independently imply the ridge *incidence* criterion in square cases. The asserted contribution here is the unified rectangular ridge-pair metric spectrum, its exact multiplicities, the polar neighborliness boundary, and the mean-angle sign reversal with its square asymptotic. None of these is a consequence of the published facet-count formula alone, and no checked accessible source provided the angle data. Priority remains provisional because the full Cao--Chen paper and possible unindexed equivalent work were not inspected.

## Limitations
The polar neighborliness assertion refers to ordinary combinatorial \(2\)-neighborliness, not higher-order neighborliness. The angular spectrum is tied to the unscaled Frobenius metric and need not survive general affine transformations. The computer checks cover only the stated finite cases; the formula is proved for all integer \(p,q\ge2\). No external or independent mathematical audit has been conducted; historical-priority verification remains incomplete for the unavailable Cao--Chen full text.

## References
1. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901, first public 2020-12-17, Section 3, especially Proposition 3.4 and Corollary 3.5. https://arxiv.org/abs/2012.09901
2. L. Cao and Z. Chen, *Faces of the polytope of doubly substochastic matrices*, Linear Algebra and its Applications 637 (2022), 59--81, https://doi.org/10.1016/j.laa.2021.11.012 (abstract inspected; full article inaccessible for this comparison).
