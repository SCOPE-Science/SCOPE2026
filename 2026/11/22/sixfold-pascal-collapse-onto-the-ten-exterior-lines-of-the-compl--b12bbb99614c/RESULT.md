# Sixfold Pascal collapse onto the ten exterior lines of the complete \(\mathbb F_5\)-conic

## Finding
Let \(K\subset\mathbb P^2_{\mathbb F_5}\) be any smooth conic and let \(H=K(\mathbb F_5)\) be its six rational points. The 60 unoriented cyclic orderings of the six points, modulo rotation and reversal, define 60 Pascal lines. The resulting map from the 60 hexagons to the dual projective plane has precisely ten distinct images: **exactly the ten \(\mathbb F_5\)-lines disjoint from \(H\)**. Each image occurs for exactly six hexagons. The natural \(\operatorname{PGL}_2(\mathbb F_5)\)-action has three orbits of sizes \(30,20,10\), and each of the ten image lines receives \(3,2,1\) hexagons from those orbits, respectively.

Let \(D\subset\mathbb P^2_{\mathbb F_5}\) be the *reduced* union of these ten lines. Its pairwise crossings consist of fifteen ordinary nodes and ten ordinary triple points, all rational. For every integer \(n\ge1\), writing \(Q=5^n\),
\[
 \#D(\mathbb F_Q)=10Q-25,\qquad
 \#(\mathbb P^2\setminus D)(\mathbb F_Q)=Q^2-9Q+26.
\]
Consequently
\[
 Z(D,T)=\frac{(1-T)^{25}}{(1-5T)^{10}},\qquad
 Z(\mathbb P^2\setminus D,T)=\frac{(1-5T)^9}{(1-25T)(1-T)^{26}}.
\]

## Assumptions and scope
All lines and points are in the projective plane over \(\mathbb F_5\), unless the extension field is explicitly indicated. A smooth conic with a rational point is projectively equivalent to \(XZ=Y^2\); every smooth conic over a finite field has a rational point. Write \(P_t=(t^2:t:1)\) for \(t\in\mathbb F_5\) and \(P_\infty=(1:0:0)\). Label these points by \(0,1,2,3,4,5\), with label 5 for infinity.

An *unoriented cyclic hexagon* is a permutation \((a,b,c,d,e,f)\) of these labels, modulo the dihedral group of order twelve (six rotations and reversal). Its Pascal line is the line through \(P_aP_b\cap P_dP_e\) and \(P_bP_c\cap P_eP_f\). Pascal's theorem places the third point \(P_cP_d\cap P_fP_a\) on the same line. Multiplicity six means the cardinality of a **combinatorial preimage**; it does not assert a sixfold nonreduced line scheme.

## Proof
1. In the model \(XZ=Y^2\), normalize each nonzero projective vector by scaling its first nonzero coordinate to 1. A line \(AX+BY+CZ=0\) contains the point \(P_t\) exactly when \(At^2+Bt+C=0\), and contains \(P_\infty\) when \(A=0\). It is disjoint from the six rational conic points precisely when \(A\ne0\) and \(B^2-4AC\) is a nonsquare in \(\mathbb F_5\), namely 2 or 3. There are exactly ten such lines: after normalizing \(A=1\), for each \(B\in\mathbb F_5\) exactly two values of \(C\) give nonsquare discriminant. These exterior lines correspond to unordered Frobenius-conjugate pairs in \(\mathbb P^1(\mathbb F_{25})\setminus\mathbb P^1(\mathbb F_5)\), so \(\operatorname{PGL}_2(\mathbb F_5)\) acts transitively on them.
2. The projective group \(\operatorname{PGL}_2(\mathbb F_5)\) has order 120. Its action on the 60 unoriented cyclic hexagons has exactly three orbits, represented by

   | Hexagon representative | Orbit size | Pascal line \((A:B:C)\) | Nonsquare discriminant |
   | --- | ---: | --- | ---: |
   | \((0,1,2,3,4,5)\) | 30 | \((1:1:1)\) | 2 |
   | \((0,1,2,4,3,5)\) | 20 | \((1:0:3)\) | 3 |
   | \((0,1,2,4,5,3)\) | 10 | \((1:3:4)\) | 3 |

   These data are verified by enumeration of the 120 fractional linear transformations on the six labels, followed by direct chord cross products over \(\mathbb F_5\); the full exhaustive checker and its output are included. Equivariance of Pascal's construction and transitivity on the exterior lines imply that each displayed orbit maps surjectively to the set of ten exterior lines. The orbit fibers therefore have constant sizes \(30/10=3\), \(20/10=2\), \(10/10=1\). This proves all the image and multiplicity claims. The standalone checker also independently computes all 60 Pascals directly, agreeing with the orbit argument.
3. The ten exterior lines have 45 unordered pairs. Their pairwise intersections are 25 distinct rational points, with precisely 15 lying on two lines and ten lying on three: \(15\binom22+10\binom32=45\). This is checked by exact enumeration of normalized cross products and incidences among all 31 rational points; no higher multiple intersections occur. Each of the remaining six rational plane points is on the conic and on none of the ten exterior lines. All 25 crossings remain distinct over every extension field.
4. As a reduced divisor, \(D\) is the union of ten rational projective lines, and its only multiple intersections are those in step 3. Inclusion-exclusion gives \(10(Q+1)-15-2\cdot10=10Q-25\). Subtracting from \(\#\mathbb P^2(\mathbb F_Q)=Q^2+Q+1\) yields the complement count. Applying the exponential definition \(Z(V,T)=\exp(\sum_{n\ge1}\#V(\mathbb F_{5^n})T^n/n)\) gives the displayed zeta functions.

## Verification
Run `python3 verify_pascal.py` using Python 3 with no third-party packages. Its JSON standard output must be byte-identical to `certificate.json`. It reconstructs all six conic points, all 60 hexagons, 120 projectivities, 31 rational lines and points, the three orbits and representatives, all 60 Pascal images, the ten exterior lines, all 45 pairwise intersections and the complete incidence histogram. All projective coordinates are computed exactly modulo five, without numerical tolerance. The certificate records each of the 60 input hexagons and its line. The displayed extension-field counts follow from the proved rational incidence decomposition; they are not extrapolated merely from finite tests.

## Relationship to prior work
Chipalkatti's *On the coincidence of Pascal lines* studies pair coincidences for six points on a **complex** conic, identifying involution and ricochet loci. Chipalkatti–Da Silva's *Degenerations of Pascal Lines* studies collision of marked conic points and resolution of the Pascal map; in the present theorem the six marked points remain distinct. The group-theoretic 60-to-10 collapse in characteristic five is not a corollary of these complex-classification statements. The ten exterior lines and their Desargues configuration of ten internal triple points are classical (Edge, discussed and explicitly tabulated by Innamorati); **their existence and intersection profile are not claimed as new**. The additional result here is their canonical appearance as *all* sixty Pascals with six-to-one fibers and the orbitwise decomposition \(3+2+1\). A previously published arithmetic Pascal–Kirkman result for generic sextuples in characteristic at least seven has disjoint hypotheses and does not address this complete characteristic-five sextuple.

## Limitations
The statement concerns the full set of six rational points on a conic over \(\mathbb F_5\), not arbitrary sextuples or arbitrary characteristic-five extensions with other selections of six points. Only the reduced ten-line divisor is counted in the zeta formulas. No assertion is made about the scheme-theoretic multiplicity of a flat 60-line family, the resolution of Pascal maps in characteristic five, or other hexagrammum-mysticum points and lines. The checked literature and databases may omit an unindexed equivalent computation in classical finite projective geometry.

## References
- J. Chipalkatti, *On the coincidence of Pascal lines*, arXiv:1407.1447v1 (2014-07-06), https://arxiv.org/abs/1407.1447.
- J. Chipalkatti and S. Da Silva, *Degenerations of Pascal Lines*, arXiv:2202.12975v1 (2022-02-25), https://arxiv.org/abs/2202.12975; DOI 10.1007/s13366-022-00655-x.
- A. Abdesselam and J. Chipalkatti, *On the reconstruction problem for Pascal lines*, arXiv:1608.05056v1 (2016-08-17), https://arxiv.org/abs/1608.05056.
- S. Innamorati, *Note on Discovering Doily in PG(2,5)*, Mathematics 11 (2023), 2210, https://doi.org/10.3390/math11092210; cites W. L. Edge, *31-point Geometry* (1955).
- Published arithmetic Pascal–Kirkman flag result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-frobenius-orbit-spectra-and-rational-incidence-obstructions-for--1e6ef0f36929 (generic sextuples, characteristic at least seven).
