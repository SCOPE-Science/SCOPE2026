# Isolation-sieve polynomials and forest-optimal locating codes on rook graphs

## Finding
For integers \(2\le m\le n\), let \(R_{m,n}=K_m\square K_n\) and let a **locating-total dominating set** \(S\subseteq[m]\times[n]\) be a set such that every cell has a neighbor in \(S\) and distinct cells outside \(S\) have distinct sets of neighbors in \(S\). Let an **ordinary locating-dominating set** require domination only for cells outside \(S\), while retaining the same locating condition.

Represent each selected cell \((i,j)\) by the edge \(ij\) of a labelled simple bipartite graph \(H_S\) on the \(m\) row vertices and \(n\) column vertices. Then:

1. \(S\) is locating-total dominating exactly when \(H_S\) has **at most one isolated vertex altogether** and **no component consisting of a single edge**.
2. \(S\) is ordinary locating-dominating exactly when \(H_S\) has at most one isolated vertex altogether and **at most one component consisting of a single edge**.
3. With \(F(x,y;z)=\sum_{a,b\ge0}(1+z)^{ab}x^ay^b/(a!b!)\), the complete labelled cardinality polynomials are

\[
L^{\mathrm{LTD}}_{m,n}(z)=m!n!\,[x^my^n]\,(1+x+y)e^{-x-y-xyz}F(x,y;z),
\]
\[
L^{\mathrm{LD}}_{m,n}(z)=m!n!\,[x^my^n]\,(1+x+y)(1+xyz)e^{-x-y-xyz}F(x,y;z).
\]
In particular, if the natural definition is extended to one-row graphs, their difference obeys the exact polynomial identity
\[
L^{\mathrm{LD}}_{m,n}(z)-L^{\mathrm{LTD}}_{m,n}(z)=mnz\,L^{\mathrm{LTD}}_{m-1,n-1}(z).
\]
4. The minimum locating-total domination number is
\[
\gamma_t^L(R_{m,n})=\max\!\left\{n-1,\left\lceil\frac{2(m+n-1)}3\right\rceil\right\}.
\]
Every minimum set has an **acyclic** selected-cell incidence graph after removing its possible isolated row or column vertex. Thus every optimum is encoded by a bipartite forest with components of at least three vertices. Define
\[
T(x,y;z)=\sum_{\substack{a,b\ge1\\a+b\ge3}}
\frac{a^{b-1}b^{a-1}}{a!b!}x^ay^bz^{a+b-1}.
\]
If \(g=\gamma_t^L(R_{m,n})\), the exact number of labelled minimum sets is
\[
m!n!\,[x^my^nz^g]\,(1+x+y)\exp T(x,y;z).
\]
5. Relative to the known ordinary locating-domination number of a rectangular rook graph, the totality requirement costs **exactly one additional selected cell** precisely when \(n\le2m\) and \(m+n\equiv0\pmod3\); otherwise the two minima agree.

For example,
\[
L^{\mathrm{LTD}}_{3,3}(z)=81z^4+117z^5+84z^6+36z^7+9z^8+z^9,
\]
while \(L^{\mathrm{LTD}}_{4,4}(z)\) begins \(672z^5+4480z^6+9424z^7\). The formula gives \(1800\) minimum codes on the labelled \(5\)-by-\(5\) rook graph.

## Assumptions and scope
All graphs are finite, simple and labelled. The standard rook graph joins distinct cells sharing a row or a column. Location compares **open** neighborhoods only for cells outside the code. For \(m=1\) the same incidence criterion and polynomial convention remain valid (and \(L^{\mathrm{LTD}}_{1,1}=0\)); the displayed minimum formula is claimed only for \(2\le m\le n\). Polynomial coefficient extraction is in formal power series; the displayed expressions are finite at every specified bidegree.

## Proof
**A. Neighborhood correspondence.** For a selected edge set \(E(H_S)\), the selected neighbors of an unselected cell \((i,j)\) are precisely the incident selected edges at row \(i\) or column \(j\). For a selected cell its number of selected neighbors is \(d_H(i)+d_H(j)-2\). Consequently, ordinary domination of unselected cells fails exactly when an isolated row and an isolated column coexist, while total domination additionally fails exactly when a selected edge has both endpoint degrees one, that is, it is a one-edge connected component.

**B. Complete location test.** Consider two different unselected cells. If they share a row, their selected-neighbor signatures coincide if and only if both corresponding columns are isolated vertices of \(H_S\). The same statement holds with rows and columns interchanged. If they lie in different rows and columns, say \((i,j)\) and \((k,\ell)\), equality forces every selected edge meeting row \(i\) or column \(j\), and every selected edge meeting row \(k\) or column \(\ell\), to lie among the two cross-corner edges \((i,\ell)\) and \((k,j)\). Any cross-corner edge present has both endpoints of degree one, and therefore is an isolated one-edge component. If neither cross-corner edge is present, both signatures are empty. If exactly one cross-corner edge is present and the signatures are equal, the opposite row and column are both isolated; if two are present, there are two isolated one-edge components. Conversely, two isolated one-edge components yield such an ambiguity by crossing their endpoints. Combined with ordinary domination and the shared-row/column cases, this proves the ordinary characterization; adding the total domination condition rules out all isolated edges and proves the first characterization.

**C. Full polynomial sieve.** In the two-sort labelled exponential formula, \(F(x,y;z)\) counts all simple bipartite graphs with an edge weight \(z\). Connected components that are isolated row vertices, isolated column vertices or isolated single edges have respective exponential series \(x\), \(y\), \(xyz\). Deleting all three component species multiplies \(F\) by \(e^{-x-y-xyz}\). Reinstating zero or one isolated vertex multiplies this by \(1+x+y\). Reinstating zero or one isolated single edge independently multiplies it by \(1+xyz\). This gives both series. Alternatively, a locating-dominating but not locating-total code has exactly one isolated selected edge, and deleting its row and column leaves a locating-total code on the smaller board; selecting those endpoints in \(mn\) ways proves the polynomial difference identity.

**D. Minimum and forest rigidity.** Suppose the nontrivial selected-edge components contain \(r\) row vertices and \(c\) column vertices, and number \(k\). Each contains at least one vertex of either type and at least three vertices in total, so
\[
k\le\min\!\left\{r,c,\left\lfloor\frac{r+c}{3}\right\rfloor\right\}.
\]
Every component with \(v\) vertices has at least \(v-1\) edges; hence
\[
|S|\ge r+c-k\ge\max\!\left\{r,c,\left\lceil\frac{2(r+c)}3\right\rceil\right\}=:f(r,c).
\]
This bound is sharp for all \(r,c\ge1\) with \(r+c\ge3\): put \(k=\min\{r,c,\lfloor(r+c)/3\rfloor\}\), start \(k\) components with one row and one column vertex each, give each component at least one further vertex, then distribute all remaining row and column vertices arbitrarily among the components and connect each as a bipartite tree. A complete bipartite graph on each component's two nonempty vertex parts supports such a tree. Each resulting component contains at least three vertices, and the total edge count is \(r+c-k=f(r,c)\).

The first characterization allows supports \((r,c)\) of precisely \((m,n)\), \((m-1,n)\), or \((m,n-1)\). The function \(f\) is monotone in each argument and, since \(m\le n\), one has \(f(m,n-1)\le f(m-1,n)\) (both have the same sum, and the largest support coordinate is smaller in the former). Thus the optimum is attained by \((m,n-1)\) and equals the displayed formula. For any optimum code, its edge count must attain the sharp lower bound for its actual support sizes. Equality in the component edge bound forces each nontrivial component to be a tree, proving optimum forest rigidity.

The number of bipartite trees with fixed labelled parts of sizes \(a,b\ge1\) is \(a^{b-1}b^{a-1}\), by the matrix-tree theorem for the complete bipartite graph. Excluding the two-vertex single-edge tree and taking a set of such components gives \(\exp T\). Reinstating at most one isolated vertex gives \((1+x+y)\exp T\). Because every minimum code is a forest, extracting its optimum edge-degree coefficient counts precisely all minimum codes.

**E. Totality penalty.** Junnila, Laihonen and Lehtilä's known ordinary rook locating-domination formula is \(n-1\) for \(n\ge2m\), and \(\lceil2(m+n)/3\rceil-1\) for \(m\le n<2m\). Comparing it with the minimum just proved gives a difference of one exactly for \(n\le2m\) with \(m+n\) divisible by three; the other congruence/aspect-ratio cases give zero.

## Verification
Compile and run `verify_exhaustive.cpp` using a C++17 compiler, run `verify_locating.cpp` likewise, and run `verify_coefficients.py` with Python 3. These independently check open-neighborhood predicates, the two isolation conditions, full size distributions on manageable boards, exact exponential-formula coefficients, the isolated-edge polynomial difference, and stated minimum sizes. The saved validation runs returned `EXHAUSTIVE_OK`, `LD_OK`, `COEFFICIENTS_OK`, , `LOCATING_DIFFERENCE_OK`, and `FOREST_CENSUS_OK`. All infinite-family assertions are justified by the preceding symbolic arguments, not inferred from finite tests.

## Relationship to prior work
Chakraborty–Foucaud–Hakanen–Henning–Wagler (2022) motivate locating-total domination in general graph families. Junnila–Laihonen–Lehtilä (2018) give the ordinary locating-domination minimum for rook graphs and work with stronger locating codes, but the exact two-polynomial component sieve and forest-optimal census are distinct claims. Mertens (2024) determines ordinary rook domination polynomials; Carballosa–Wisby (2020) study total multiple-domination without location signatures. A separately indexed result determines locating-total polynomials for the two-row subfamily \(K_2\square K_n\); that subfamily is prior coverage and is included here only as a consistency specialization. The claimed new contribution is the unified all-rectangles incidence criterion, paired all-cardinality enumerators, polynomial difference bijection, and forest-optimal enumeration.

## Limitations
This result assumes rectangular products of exactly two complete graphs and single-vertex open-neighborhood location. It does not cover ordinary Cartesian grids made from paths, higher-factor Hamming graphs, or locating every vertex including selected ones. The computer checks cover finite board sizes only. Publication-priority clearance is necessarily provisional, particularly for inaccessible full texts or unindexed tabulations; an independent mathematical audit has not been performed.

## References
- D. Chakraborty, F. Foucaud, A. Hakanen, M. A. Henning and A. K. Wagler, *Progress towards the two-thirds conjecture on locating-total dominating sets*, arXiv:2211.14178v1 (2022-11-25), https://arxiv.org/abs/2211.14178.
- V. Junnila, T. Laihonen and T. Lehtilä, *On regular and new types of codes for location-domination*, Discrete Applied Mathematics 247 (2018), 225–241, https://doi.org/10.1016/j.dam.2018.03.050.
- S. Mertens, *Domination Polynomial of the Rook Graph*, arXiv:2401.00716 (2024), https://arxiv.org/abs/2401.00716.
- W. Carballosa and J. Wisby, *Total k-domination in Cartesian product of complete graphs*, arXiv:2001.07850 (2020), https://arxiv.org/abs/2001.07850.
- M. A. Henning and N. Jafari Rad, *Locating-total domination in graphs*, Discrete Applied Mathematics 160 (2012), 1986–1993, https://doi.org/10.1016/j.dam.2012.04.004.
