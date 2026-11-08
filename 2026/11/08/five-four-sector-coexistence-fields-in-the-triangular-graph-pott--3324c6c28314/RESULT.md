# Five four-sector coexistence fields in the triangular-graph Potts antiferromagnet

## Finding

Let \(T(6)=L(K_6)\) be the triangular graph whose fifteen vertices are the two-element subsets of \(\{0,1,2,3,4,5\}\); two vertices are adjacent precisely when their subsets intersect. Assign one of three **labeled** spin colors \(\{0,1,2\}\) independently to every vertex. For \(J>0\), \(h\in\mathbb R\), set
\[
H(\sigma)=J\sum_{\{e,f\}\in E(T(6))}\mathbf1_{\sigma_e=\sigma_f}-h\sum_{e\in V(T(6))}\mathbf1_{\sigma_e=0},\qquad x=h/J.
\]
The exact ground-state energy is
\[
\frac{E_0(h)}J=\min\{24,\ 12-3x,\ 12-6x,\ 18-9x,\ 36-12x,\ 60-15x\}.
\]
Its **only** coexistence fields are \(x=-4,0,2,6,8\). At every one, exactly four consecutive favored-color occupancy sectors have a common minimum. The successive open-field phases have favored-color occupancies \(0,3,6,9,12,15\) and labeled degeneracies \(1760,300,6180,120,120,1\). At the five coexistence fields, the respective total labeled degeneracies are \(9260,31590,25200,2220,331\). In particular the zero-field frustration minimum is twelve equal-color bonds, attained by \(31590\) configurations.

A structural strengthening is that the fixed-occupancy minimum in **every** sector \(s\in\{0,\ldots,15\}\) saturates the degree-convexity bound defined below, even though the three colors simultaneously partition the edges of one complete graph. In fact the proof gives an **if-and-only-if characterization of every sector ground state** by balanced incidence degrees and optimal color-class sizes.

## Assumptions and scope

The graph has fifteen labeled sites and sixty unordered bonds; the original six complete-graph points are labeled \(0,\ldots,5\). Each unordered edge of \(K_6\) is a site of \(T(6)\), and the site order is lexicographic:
\[
01,02,03,04,05,12,13,14,15,23,24,25,34,35,45.
\]
All three colors are distinguished. Ground-state counts include all labels and do not divide by graph automorphisms or color permutations. Couplings are homogeneous, antiferromagnetic, and strictly positive; the field couples only to color zero. No finite-temperature or thermodynamic-limit assertion is made.

For occupancy \(s\), let \(e_s\) be the smallest number of monochromatic bonds and let \(g_s\) count labeled configurations attaining it. The complete result is:

| \(s\) | \(e_s\) | \(g_s\) |
|---:|---:|---:|
| 0 | 24 | 1760 |
| 1 | 20 | 4680 |
| 2 | 16 | 2520 |
| 3 | 12 | 300 |
| 4 | 12 | 5580 |
| 5 | 12 | 19530 |
| 6 | 12 | 6180 |
| 7 | 14 | 15480 |
| 8 | 16 | 3420 |
| 9 | 18 | 120 |
| 10 | 24 | 900 |
| 11 | 30 | 1080 |
| 12 | 36 | 120 |
| 13 | 44 | 180 |
| 14 | 52 | 30 |
| 15 | 60 | 1 |

## Proof

**1. Exact energy reduction.** Represent a spin assignment as a three-color edge labeling of \(K_6\). Let \(d_c(v)\) be the number of incident edges of color \(c\) at the original point \(v\). Two distinct complete-graph edges share at most one endpoint, so their equal-color adjacency cost is exactly
\[
F(\sigma)=\sum_{v=0}^{5}\sum_{c=0}^2\binom{d_c(v)}2.
\]
For any color used on exactly \(t\) complete-graph edges, the six degrees sum to \(2t\). By discrete convexity of \(a\mapsto\binom a2\), their contribution is at least
\[
B(t)=(6-2r)\binom a2+2r\binom{a+1}2,
\qquad t=3a+r,\quad a\in\{0,\ldots,5\},\quad r\in\{0,1,2\}.
\]
Here the convention is \(\binom a2=0\) for \(a<2\). This bound is attained whenever \(2r\) of the six degree values are \(a+1\) and the others are \(a\). In a fixed favored-color occupancy \(s\), the remaining color occupancies are \(t\) and \(15-s-t\), hence
\[
F(\sigma)\ge L(s):=B(s)+\min_{0\le t\le 15-s}\{B(t)+B(15-s-t)\}.
\]
Direct finite evaluation of the displayed integer expression gives the exact sequence of sixteen \(e_s\) values in the table. To prove **attainability**, `sector_witnesses.tsv` supplies a specific fifteen-character ternary edge-color word for each \(s\). For each word, count its colors and the incident degrees along the stated edge order; each reaches \(F=L(s)\). Thus \(e_s=L(s)\) for all sixteen sectors, without relying on a numerical optimization hypothesis. Conversely, equality in the lower bound forces the six degrees of **each** color class to differ by at most one, and the number \(t\) of edges of color one must minimize \(B(t)+B(15-s-t)\). Consequently a coloring of favored occupancy \(s\) is a ground state **if and only if** both conditions hold. This is an exact structural characterization, not merely an existence bound.

**2. Full field envelope and multiplicities.** At field ratio \(x\), the best energy in occupancy sector \(s\) is \(J(e_s-sx)\). The points \((s,e_s)\) have lower convex hull vertices
\[
(0,24),(3,12),(6,12),(9,18),(12,36),(15,60).
\]
Every nonvertex point lies on one of the five displayed consecutive hull segments, whose slopes are \(-4,0,2,6,8\), strictly increasing. Therefore only the stated six affine energy branches can be stable on open intervals. At each common slope all four integer occupancy points on the corresponding segment minimize, with no further sectors. Summing \(g_s\) over the appropriate one or four minimizers yields precisely the phase and coexistence counts stated above.

**3. Exact counting certificate.** The numbers \(g_s\) come from finite, exhaustive integer enumeration of all \(3^{15}=14348907\) spin words. Three standalone programs implement independently checkable encodings: direct ternary words and six degree triples, a red-edge-mask/blue-submask partition of all edges, and direct evaluation of sixty line-graph bonds. Each checks the complete sixteen-sector table against the displayed integers. The degree-convexity proof already supplies all minima; enumeration is used for exact multiplicities only. Since the sampled space is the entire finite configuration space, this is an exhaustive calculation, not statistical sampling.

## Verification

From the directory containing the embedded files, with a C++17 compiler, run:

```bash
c++ -std=c++17 -O3 verify_ternary.cpp -o verify_ternary && ./verify_ternary
c++ -std=c++17 -O3 verify_masks.cpp -o verify_masks && ./verify_masks
c++ -std=c++17 -O3 verify_adjacency.cpp -o verify_adjacency && ./verify_adjacency
```

The expected final markers are `VERIFY_TERNARY_OK`, `VERIFY_MASKS_OK`, and `VERIFY_ADJACENCY_OK`. The first code prints a witness for each occupancy; the second prints an independently obtained table; the third explicitly tests the sixty physical bonds. `sector_witnesses.tsv` records the first word encountered in the specified low-order-digit-first ternary enumeration for each sector. No input file or external scientific software is needed.

## Relationship to prior work

Zaslavsky's gain-graph treatment explains generalized Potts spin satisfaction and the role of zero-frustration colorings; its proper-coloring enumerator does not count minimum **positive** frustration on this graph. Shrock and Xu derive generalized-field Potts partition functions and evaluate path, complete, and wheel families, not the line graph of a complete six-point graph at three colors and its exact positive-frustration field envelope. These foundational general definitions are not new.

The triangular graph \(T(6)\) is the **complement** of the two-subset Kneser graph \(\mathrm{KG}(6,2)\). For each coloring, with color-class sizes \(n_c\), one has
\[
F_{T(6)}(\sigma)+F_{\mathrm{KG}(6,2)}(\sigma)=\sum_{c=0}^{2}\binom{n_c}2.
\]
Thus a previously evaluated minimum on the Kneser complement does **not** imply the present minimum: the latter would require the complement's **maximum** frustration at specified individual color-class sizes, not only its minimum at one favored-color occupancy. The present all-sector convex-bound attainment, positive-frustration minima, multiplicities, and five-field diagram are the claimed content.

## Limitations

The result is restricted to the single fifteen-vertex labeled graph, three spin colors, homogeneous positive \(J\), and zero temperature. It makes no uniqueness claim for its mathematical ideas across all possible unpublished calculations or indexing systems. Counts at some extreme sectors may independently occur in preexisting edge-coloring or Ramsey tables; the new claim is the integrated exact field classification with all sector counts, not exclusive priority for every isolated number. All checks are finite exact proofs or exhaustive calculations; no independent external scientific audit was performed.

## References

1. T. Zaslavsky, *Totally frustrated states in the chromatic theory of gain graphs*, first public arXiv submission 1 September 2006, https://arxiv.org/abs/math/0609048.
2. R. Shrock and Y. Xu, *Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings*, arXiv:1009.1182, first public 7 September 2010, https://arxiv.org/abs/1009.1182.
