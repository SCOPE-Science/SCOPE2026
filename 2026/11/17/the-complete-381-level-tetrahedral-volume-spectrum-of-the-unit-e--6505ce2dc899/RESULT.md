# The complete 381-level tetrahedral volume spectrum of the unit-edge truncated icosahedron

## Finding

Let \(P\) be the regular truncated icosahedron with unit edge length and \(V(P)\) its 60-vertex set. For each four-element subset \(S\subset V(P)\), let \(v(S)\) be the ordinary Euclidean volume of its convex hull; thus coplanar selections have volume zero. There are exactly \(\binom{60}{4}=487635\) such subsets. Put \(\varphi=(1+\sqrt5)/2\).

**Complete exact classification.** These 487635 volumes occupy exactly **381 distinct levels**. The attached `spectrum.tsv` is the complete, decreasing exact volume-level table: a row with integer entries `det_phi_a`, `det_phi_b`, `multiplicity` gives the volume \((a+b\varphi)/48\) and its exact frequency. Every level is represented once; all rows together enumerate every four-element subset.

The first three decreasing levels, including their multiplicities, are

| Volume | Multiplicity |
|---|---:|
| \((25+41\varphi)/12\) | 120 |
| \((25+40\varphi)/12\) | 120 |
| \((6+10\varphi)/3\) | 60 |

The first level and its multiplicity were determined previously. The exact **second** level, its count, and the complete 381-level table are the additions. The sharp gap between the maximum and all strictly smaller vertex-supported volumes is \(\varphi/12\). Within each of the first two levels, all tetrahedra are mutually congruent (their unordered six-edge squared-distance data agree up to permutation of four vertices).

As a global consistency identity, the unnormalized determinant coefficients \((a,b)\) obey
\[
\sum_{(a,b,m)\in\mathrm{spectrum}}m(a+b\varphi)^2
=480000(10+9\varphi)^3.
\]
This is a separately derived Cauchy–Binet moment identity, not a fitted numerical check.

## Assumptions and scope

Take the twelve regular-icosahedron vertices
\[
I=\{(0,\pm1,\pm\varphi),(\pm1,\pm\varphi,0),(\pm\varphi,0,\pm1)\},
\]
whose original edges have length \(2\). For every ordered pair \((u,v)\) of adjacent original vertices, take \((2u+v)/2\). The convex hull of these 60 points is a regular truncated icosahedron with unit edge length: the one-third truncation \((2u+v)/3\) has edge length \(2/3\), subsequently scaled by \(3/2\).

A tetrahedral selection consists of four *distinct polytope vertices*, not arbitrary points inside the solid. Coplanar selections are counted in the zero-volume level. This finite classification is not an inequality for every freely inscribed tetrahedron, and it does not claim that the nonmaximal freely inscribed tetrahedra have a positive gap.

## Proof

Represent the quadratic integer \(a+b\varphi\) as \((a,b)\in\mathbb Z^2\), using \(\varphi^2=\varphi+1\). Addition and multiplication are
\[
(a,b)+(c,d)=(a+c,b+d),\qquad
(a,b)(c,d)=(ac+bd,ad+bc+bd).
\]
An exact sign comparison uses \(2(a+b\varphi)=2a+b+b\sqrt5\), with integer-squared comparison when the summands have opposite signs.

The included checker constructs all twelve original vertices and finds exactly 30 unordered original edges by squared Euclidean distance \(4\) in this integer ring. Both orientations of these edges yield exactly 60 distinct doubled unit-edge truncated-icosahedron vertices \(q=2p=2u+v\) in \(\mathbb Z[\varphi]^3\). For any four indices \(i<j<k<\ell\), set
\[
D_{ijk\ell}=\left|\det(q_j-q_i,q_k-q_i,q_\ell-q_i)\right|.
\]
Because the actual vertices are \(q/2\), the volume equals \(D_{ijk\ell}/48\). Each determinant belongs to \(\mathbb Z[\varphi]\). The checker visits **every** one of the \(\binom{60}{4}=487635\) possible index quadruples without pruning; it calculates all determinants and groups their exact absolute values, compares the 381 groups in the ordered quadratic field, and matches the multiplicity of each row of the supplied table. This finite exhaustive calculation, using only explicit integer operations, constitutes the certificate for the complete classification.

Its first levels are \((100+164\varphi)/48\), \((100+160\varphi)/48\), and \((96+160\varphi)/48\), of respective frequencies 120, 120 and 60. The strict difference of the two largest values is \(4\varphi/48=\varphi/12\); ordering is verified by the exact sign comparator for all 381 levels.

For the two highest groups, the checker independently traverses all quadruples once more and computes the six squared edge lengths. It minimizes their six-tuple over all 24 relabelings of each tetrahedron. In both groups there is precisely one canonical six-distance signature. Six pairwise distances determine a Euclidean tetrahedron up to congruence, establishing the claim about shapes.

As an algebraic cross-check, the sixty doubled-coordinate vectors are centered, have equal squared length \(10+9\varphi\), and satisfy \(\sum_i q_iq_i^{\mathsf T}=20(10+9\varphi)I_3\). By Cauchy–Binet applied to the 60-by-4 matrix whose rows are \((1,q_i)\),
\[
\sum_{i<j<k<\ell}D_{ijk\ell}^2
=\det\begin{pmatrix}60&0\\0&20(10+9\varphi)I_3\end{pmatrix}
=480000(10+9\varphi)^3.
\]
The separately computed table satisfies this identity exactly in \(\mathbb Z[\varphi]\).

## Verification

Execute `python3 check_spectrum.py spectrum.tsv` with Python 3.10 or later; only the standard library is used. It reconstructs all coordinates, checks the edge graph, enumerates all 487635 subsets, performs exact determinant and ordering arithmetic, compares every one of the 381 supplied rows, checks the exact second moment, and tests congruence of each of the two highest groups. The completion marker is `SOCCER_TETRAHEDRON_SPECTRUM_PASS`. In addition, the initial vertex norm and covariance calculations match the independently tabulated unit-edge circumradius of the truncated icosahedron.

## Relationship to prior work

Murphy and Weed, *Face embeddings of Archimedean solids* (first public 2024-04-23), give the classical one-third truncation construction of the soccer-ball Archimedean polyhedron but do not tabulate tetrahedral volume multiplicities. MathWorld records its geometric normalization, circumradius and volume; these are input geometric facts, not new discoveries.

The published *A sharp tetrahedral-volume polynomial and sixty movable-apex families in truncated icosahedra* proves the sharp maximum for the whole one-parameter icosahedral truncation family, including the 120 maximizing soccer-ball vertex quadruples and their continuous moving-apex degeneracies. In particular the maximum \((25+41\varphi)/12\) is **already known**. Its full text was compared with this claim: its results address the maximum and equality locus, rather than the complete 381-level frequency table, exact next volume level and sharp **discrete** gap. No priority is claimed for the maximum or the general determinant method.

## Limitations

The numerical classification is finite but exhaustive, under the exact given coordinates; there is no claim of a closed formula for the spectrum of all edge-truncated icosahedra at arbitrary truncation parameters, nor a general theorem for other Archimedean solids. The second-largest volume statement applies **only to vertex-supported tetrahedra**; continuously variable contained tetrahedra can approach the maximal volume arbitrarily closely. The certificate relies on explicit, inspectable deterministic code and the complete exact table, not on a symbolic human reduction of all 381 rows. A historical-priority search can miss equivalent sources. Independent auditing has not been performed.

## References

1. T. Murphy and D. Weed, *Face embeddings of Archimedean solids*, arXiv:2404.15142, first public 2024-04-23. https://arxiv.org/abs/2404.15142
2. E. W. Weisstein, *Truncated Icosahedron*, MathWorld. https://mathworld.wolfram.com/TruncatedIcosahedron.html
3. *A sharp tetrahedral-volume polynomial and sixty movable-apex families in truncated icosahedra*, published research note (2026-10-18). https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-a-sharp-tetrahedral-volume-polynomial-and-sixty-movable-apex-fam--696e60954f6d/RESULT.md
