# Complete multiple-illumination spectrum of convex pentagons

## Finding
Let \(P\) be a strictly convex Euclidean pentagon with five genuine vertices \(v_0,\ldots,v_4\), numbered counterclockwise. Let \(\beta_i\in(0,\pi)\) be its exterior turning angle at \(v_i\), with indices modulo five and \(\sum_i\beta_i=2\pi\). For every positive integer \(m\), let \(I^{(m)}(P)\) be the least number of planar directions, repetitions counted, such that every boundary point is illuminated from at least \(m\) of those directions, where a direction \(u\) illuminates \(x\) if \(x+tu\) enters the interior of \(P\) for some \(t>0\).

Then the entire integer multiplicity spectrum is exactly
\[
I^{(m)}(P)=
\begin{cases}
\lceil 5m/2\rceil,& \beta_i+\beta_{i+1}<\pi\text{ for all }i\pmod5,\\
3m,&\beta_i+\beta_{i+1}\ge\pi\text{ for at least one }i\pmod5.
\end{cases}
\]
The boundary of the first regime is strict: equality in any angle-pair test belongs to the second regime. The corresponding fractional illumination number, or equivalently the limit \(\lim_{m\to\infty}I^{(m)}(P)/m\), is \(5/2\) in the first regime and \(3\) in the second.

## Assumptions and scope
The polygon has five distinct extreme vertices, every interior angle strictly between zero and \(\pi\), and no consecutive collinear sides. Illumination directions are arbitrary nonzero vectors, counted as distinct occurrences in a multiset; choosing a direction on an edge-parallel critical ray cannot illuminate a vertex along that supporting edge because entry into the interior is strict. There is no restriction to vertex-only illumination: the definition covers the whole boundary. No metric normalization, symmetry, or relation among side lengths is imposed.

Write \(e_i=v_{i+1}-v_i\) for the oriented edge vectors. The counterclockwise turn from \(e_{i-1}\) to \(e_i\) is \(\beta_i\). For any generic or nongeneric vector \(u\), the vertex \(v_i\) is illuminated exactly when both
\[
\det(e_{i-1},u)>0,\qquad \det(e_i,u)>0.
\]
This follows from the strict inward conditions at its two incident supporting lines, since every other facet inequality is slack at the vertex. A direction illuminating a vertex points strictly inward across both adjacent edges, so it illuminates the relative interiors of those edges as well. Thus it suffices, for every multiplicity, to illuminate every vertex.

## Proof
**Pair compatibility.** For any two vertices, a common illuminating direction exists exactly when their incident oriented edge directions fit in an open circular semicircle: the allowable direction must be strictly to the left of every such oriented edge. Three consecutive oriented edges \(e_{i-1},e_i,e_{i+1}\) fit in an open semicircle exactly when \(\beta_i+\beta_{i+1}<\pi\). Indeed, the two individual turns are strictly below \(\pi\); the only potentially larger circular gap among these three directions is the complementary arc of length \(2\pi-\beta_i-\beta_{i+1}\), which must exceed \(\pi\). Therefore the adjacent pair \(v_i,v_{i+1}\) can be illuminated together exactly when
\[
A_i:\quad \beta_i+\beta_{i+1}<\pi.
\]
The incident edge directions of nonadjacent vertices \(v_i,v_{i+2}\) comprise four consecutive edges \(e_{i-1},e_i,e_{i+1},e_{i+2}\). They fit in an open semicircle exactly when their three-turn arc has length below \(\pi\), or equivalently when its complementary two-turn arc exceeds \(\pi\):
\[
B_i:\quad\beta_i+\beta_{i+1}+\beta_{i+2}<\pi
\quad\Longleftrightarrow\quad
\beta_{i+3}+\beta_{i+4}>\pi.
\]
These tests cover all pairs of distinct pentagon vertices. Equalities never confer simultaneous illumination.

**At most two failed adjacent-pair tests.** Put \(t_i=\beta_i+\beta_{i+1}\), and let \(S=\{i:t_i\ge\pi\}\). For every \(i\),
\[
t_i+t_{i+2}=2\pi-\beta_{i+4}<2\pi.
\]
Consequently \(S\) cannot contain two indices at cyclic distance two. It has cardinality zero, one, or two, and if it has two indices they are cyclically consecutive.

**Regime \(S=\varnothing\).** Every adjacent vertex pair is simultaneously illuminable. No nonadjacent pair is: by the preceding test, \(B_i\) would force \(t_{i+3}>\pi\), contradicting \(S=\varnothing\). Hence every direction illuminates at most two vertices, and any \(m\)-fold cover of five vertices requires at least \(\lceil5m/2\rceil\) directions. Conversely, for each of the five adjacent pairs select a direction illuminating both vertices. When \(m=2q\), take \(q\) copies of each selected direction: there are \(5q\) directions and each vertex is hit \(2q\) times. When \(m=2q+1\), additionally choose three pair-directions covering the five-cycle, for example the pairs \(\{v_0,v_1\}\), \(\{v_2,v_3\}\), and \(\{v_4,v_0\}\). There are \(5q+3=\lceil5m/2\rceil\) directions, attaining the lower bound.

**Regime \(S=\{i\}\).** The three vertices \(v_i,v_{i+1},v_{i+3}\) are pairwise incompatible: the first pair fails \(A_i\), the second would require \(t_{i+4}>\pi\), and the third would require \(t_{i+1}>\pi\). The last two requirements fail because \(S\) contains only \(i\). Since one direction illuminates at most one vertex of this triple, \(I^{(m)}(P)\ge3m\). The adjacent-pair directions for \(A_{i+1}\), \(A_{i+3}\), and \(A_{i+4}\) together illuminate all five vertices. Repeating these three directions \(m\) times proves the reverse inequality.

**Regime \(S=\{i,i+1\}\).** The vertices \(v_i,v_{i+1},v_{i+2}\) are pairwise incompatible. Both adjacent pairs fail their defining tests, and the nonadjacent pair \(v_i,v_{i+2}\) would require \(t_{i+3}>\pi\), which is false. Thus at least \(3m\) directions are required. Both \(A_{i+2}\) and \(A_{i+4}\) hold: their directions cover, respectively, \(\{v_{i+2},v_{i+3}\}\) and \(\{v_{i+4},v_i\}\). One further inward direction at \(v_{i+1}\) completes a three-direction cover. Repeat it \(m\) times to attain \(3m\). Every argument uses strict compatibility tests, so the equality cases \(t_i=\pi\) are included without perturbation.

**Fractional consequence.** In the first regime, the vertex-incidence bound gives fractional cost at least \(5/2\), attained by putting weight \(1/2\) on each of the five adjacent-pair directions. In the second regime, the incompatible triple gives fractional cost at least \(3\), attained by the three-direction cover. These values are also the limits of the established integer formulas divided by \(m\).

## Verification
The standalone Python 3 script `verify.py` uses exact integer angular coordinates; no trigonometric floating-point arithmetic or external packages are needed. It enumerates every positive rational five-turn fan with denominator \(Q\in\{5,6,\ldots,13\}\), with each angle strictly below \(\pi\) and total angle \(2\pi\). Across 26,277 fans it checks that the exact illuminated-vertex incidence cells give precisely the pair-compatibility formulas above, that the set of failed neighboring tests has the stated size and adjacency, and that an incompatible triple exists in the second regime. Among these examples are 12,120 equality-boundary cases. It groups the fans into 31 incidence profiles and independently solves the capped multicover problem for every profile at multiplicities one through four, confirming the formulas. Finally it tests an explicit asymmetric convex pentagon using integer cross products.

Run `python3 verify.py` beside this file; its output begins `PASS: 26277 exact rational-turn pentagons`. Finite enumeration is corroboration, not the proof of the unrestricted theorem, which is the preceding normal-fan and three-case argument.

For concrete geometric realizations, the regular pentagon has all turns \(2\pi/5\) and belongs to the first regime. The polygon with consecutive vertices \((0,0),(1,0),(3,1),(0,4),(-2,1)\) is strictly convex and has two consecutive failed adjacent-pair tests, so it belongs to the second regime.

## Relationship to prior work
K. Sriamorn's 2023 preprint introduces the multiple-illumination invariant and poses the determination for arbitrary convex polygons as an algorithmic problem. Its Lemma 3.1 includes the positive two-fold result for pentagons when neighboring exterior turns total less than \(\pi\), while its exact all-multiplicity formula concerns regular polygons. The present theorem retains those covered special cases; the new part is the sharp, strict classification for **every** convex pentagon and **every** multiplicity, particularly the incompatible-triple obstruction and the full \(3m\) branch when a neighboring angle pair reaches or exceeds \(\pi\).

Published results on arbitrary quadrilaterals, on even-sided polygons with paired antipodal normals, and on Cartesian products of equiangular pentagons concern distinct classes or different ambient dimensions. Their theorems do not cover arbitrary five-vertex normal fans. The central distinction here is a complete dichotomy between a five-cycle of admissible vertex pairs and a three-vertex incompatibility certificate.

## Limitations
This theorem treats planar polygons with exactly five genuine vertices and positive exterior turns. It does not classify all optimal direction multisets or establish a corresponding dichotomy for hexagons and higher polygons. The algorithmic verification covers finite rational turn grids and bounded multiplicities only. The priority comparison is relative to the inspected primary literature and published statements; it is not a claim that all unindexed or inaccessible manuscripts have been exhausted.

## References
1. K. Sriamorn, *On the multiple illumination numbers of convex bodies*, arXiv:2306.13517v1 (first submitted June 23, 2023), Section 3.3 and Conclusion. https://arxiv.org/abs/2306.13517
2. *Exact multiple illumination and parity rigidity for polygons with antipodal edge-normal fans*, published 2026, scientific result and proof at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-multiple-illumination-and-parity-rigidity-for-polygons-wit--f4e6962728dc
3. *Four-vertex rigidity of multiple and fractional polygon illumination*, published 2026, scientific result and proof at https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-four-vertex-rigidity-of-multiple-and-fractional-polygon-illumina--3c22813e8f15
4. *Eight directions for Cartesian products of equiangular pentagons*, published 2026, scientific result and proof at https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-eight-directions-for-cartesian-products-of-equiangular-pentagons--7596e2fa9478
