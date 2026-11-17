# The first mixed-degree reflection-fixed homology in polygon noncrossing-matching complexes

## Finding
Let \(\mathrm{NXM}_n\) denote the simplicial complex whose vertices are the chords (including sides) of a strictly convex regular \(n\)-gon and whose faces are the pairwise disjoint, pairwise noncrossing sets of chords. For \(n\ge3\), let \(\tau_k(i)=k-i\pmod n\) act on the polygon's labeled vertices \(i=0,\ldots,n-1\).

**Exact first two-degree fixed-homology transition.** Among all reflections of all polygons with \(3\le n\le12\), the first geometric reflection-fixed space with nonzero reduced integral homology in two different degrees occurs at \(n=12\), for the reflection \(\tau_1(i)=1-i\pmod{12}\) whose axis crosses two opposite sides. Its integral reduced homology is
\[
\widetilde H_j\bigl(|\mathrm{NXM}_{12}|^{\tau_1};\mathbb Z\bigr)\cong
\begin{cases}\mathbb Z^{4},&j=1,\\ \mathbb Z,&j=2,\\0,&\text{otherwise}.\end{cases}
\]
The other reflection class of the dodecagon, \(\tau_0(i)=-i\pmod{12}\), has only \(\widetilde H_1\cong\mathbb Z^{3}\). For every smaller regular polygon, every reflection-fixed complex has reduced homology supported in at most one degree. This is a statement about **integral homology**, not an assertion that the first space is a wedge of spheres.

## Assumptions and scope
The polygon is strictly convex with cyclically labeled distinct vertices, and chords are *closed* segments. Two chords conflict if they share an endpoint or their relative interiors intersect. The complex allows all side chords. The reflection action permutes vertices and hence chords; fixed points are taken in the *geometric realization*, not merely among individually fixed simplices or chords. For odd \(n\), all reflections are conjugate to \(\tau_0\); for even \(n\), reflections fall into two conjugacy classes represented by \(\tau_0\) (through opposite vertices) and \(\tau_1\) (through opposite side midpoints). The sharpness claim ranges over integer \(3\le n\le12\) and all such reflections.

## Proof
**Orbit-complex lemma.** For any \(n\ge3\) and \(k\), partition the chords into orbits of the order-two permutation induced by \(\tau_k\). Discard an orbit if it contains two conflicting chords. Retain an orbit otherwise. Form the graph \(\Gamma_{n,k}\) on retained orbits, joining two distinct orbits if any chord of one conflicts with a chord of the other. Then there is a canonical PL homeomorphism
\[
\bigl|\mathrm{Ind}(\Gamma_{n,k})\bigr|\ \cong_{\mathrm{PL}}\ |\mathrm{NXM}_n|^{\tau_k}.
\]
Indeed, a fixed point of a simplex has equal barycentric coordinates at the chords in each orbit. An orbit can receive a positive coordinate if and only if its entire collection of chords is a noncrossing matching. If \(c_O\) is the common barycentric coordinate for the chords in an admissible orbit \(O\), define \(\lambda_O=|O|c_O\). The coefficients \(\lambda_O\) are nonnegative and sum to one. Conversely the orbit barycenter \(|O|^{-1}\sum_{e\in O}e\) gives the corresponding fixed point. A family of orbit barycenters spans a simplex precisely when the orbits have no internal conflicts and no pairwise conflicts. These two affine constructions are inverse on simplices and agree on common faces, hence yield the stated PL homeomorphism.

**Exact finite combinatorics.** For distinct chords \((a,b)\) and \((c,d)\), with each endpoint pair put into increasing order, they cross in their interiors precisely if \(a<c<b<d\) or \(c<a<d<b\); any shared endpoint is also a conflict. This gives an exhaustive integer predicate. Construct all \(\binom n2\) chords, partition them into reflection orbits, apply the internal- and cross-orbit predicates, and enumerate all cliques of the complement of \(\Gamma_{n,k}\) by recursive vertex extension. For \((n,k)=(12,1)\), this yields exactly 21 admissible orbit vertices, 125 incompatible orbit pairs, and face numbers in dimensions \(0,1,2,3,4,5\) equal to
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(21,85,100,48,11,1).
\]

Orient each face by increasing orbit indices. Over \(\mathbb Z\), the standard signed simplicial boundary maps \(\partial_d:C_d\to C_{d-1}\) have Smith normal forms with ranks
\[
(\operatorname{rank}\partial_1,\ldots,\operatorname{rank}\partial_5)
=(20,61,38,10,1),
\]
and **every nonzero Smith diagonal entry is 1**. This is not a numerical approximation: the standalone algorithm builds each integer boundary matrix and performs exact integer Smith reduction. The algorithm also asserts \(\partial_{d-1}\partial_d=0\) at every relevant degree. Therefore the reduced Betti numbers are \(4\) in degree 1 and \(1\) in degree 2, with zero elsewhere. Because each image \(\operatorname{im}\partial_d\) is primitive in its free chain group, each homology quotient is torsion-free. In particular, these ranks determine the integral homology groups, not merely rational dimensions.

**Sharpness and other reflection class.** The same complete generator, integer boundary reduction and Smith-factor check for every conjugacy class with \(3\le n<12\) gives the following table of all nonzero *reduced* integral Betti numbers, written as \(j:b_j\) (blank means no nonzero reduced homology):

| \(n\) | \(\tau_0\) | \(\tau_1\), when even |
|---:|:---|:---|
| 3 | — | — |
| 4 | 0:1 | 0:1 |
| 5 | 0:1 | — |
| 6 | 0:1 | 0:1 |
| 7 | 0:1 | — |
| 8 | 1:1 | 1:1 |
| 9 | 1:1 | — |
| 10 | 1:4 | 1:4 |
| 11 | 1:4 | — |
| 12 | 1:3 | 1:4, 2:1 |

All nonzero Smith factors of every boundary in these 15 cases are 1. Completeness follows from the exhaustive generation of all edge orbits, all compatibility pairs and all faces: the finitely many cases cover all reflection conjugacy classes at each \(n\) in the stated range. This proves both the exact dodecagon calculation and its minimality.

## Verification
Run `python noncrossing_reflection_verify.py` using the dependency specified in `requirements.txt`. The deterministic program checks the polygon crossing predicate against a separately implemented cyclic-interleaving test on 6,006 chord pairs; builds all 15 conjugacy-class orbit complexes for \(3\le n\le12\); verifies all simplicial boundary compositions; computes their exact integral Smith forms; and asserts the complete face, rank and homology certificates for the dodecagon. The expected summary and all case records are in `noncrossing_reflection_verification.txt`. No random seeds, external network, or approximate floating-point calculations occur. The result is a computer-assisted **finite exact proof**, not an extrapolation of finitely many trials to larger polygons.

## Relationship to prior work
Jakob Jonsson's *Simplicial Complexes of Graphs* (2007 first publicly available print edition), Section 16.3, introduces the same noncrossing-matching complex and gives its ordinary homological structure; Theorem 16.9 puts the nonzero ambient homology of \(\mathrm{NXM}_{12}\) only in degree \(3\). It neither computes geometric reflection-fixed spaces nor implies their integral homology: a nonequivariant homology classification does not determine fixed-point topology. The complex of **all** noncrossing diagonals (without the pairwise-disjoint matching restriction) in Braun–Ehrenborg is a different complex and its associahedral sphere statement does not cover this claim. Reflection-fixed results for ordinary matching complexes on graph strips and cyclic graphs likewise concern other vertex sets or compatibility relations. The contribution here is the exact first occurrence of *two different homology degrees in one geometric reflection-fixed locus* for the polygon noncrossing-matching complex, together with a self-contained exhaustive integer certificate.

## Limitations
The explicit homology and sharpness theorem is restricted to \(3\le n\le12\); it does not assert a formula for all \(n\), nor a homotopy wedge decomposition or presentation of the fundamental group. The argument identifies the fixed space with an exact finite PL orbit complex, and the Smith computations certify integral homology only. Published-priority comparison is limited to inspected texts and indexed sources and may miss equivalent older or unindexed treatments. No independent mathematical validation has been performed.

## References
1. Jakob Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer, print edition published 15 November 2007; Section 16.3, Theorems 16.7–16.9. DOI: https://doi.org/10.1007/978-3-540-75859-4 .
2. Benjamin Braun and Richard Ehrenborg, *The Complex of Non-Crossing Diagonals of a Polygon* (first public preprint 10 February 2008), https://arxiv.org/abs/0802.1320 . Different underlying complex; comparison only.
