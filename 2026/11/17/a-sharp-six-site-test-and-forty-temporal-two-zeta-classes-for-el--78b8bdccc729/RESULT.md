# A sharp six-site test and forty temporal-two zeta classes for elementary cellular automata

## Finding

For each Wolfram elementary binary cellular-automaton rule \(r\in\{0,\ldots,255\}\), let \(F_{r,n}:\{0,1\}^n\to\{0,1\}^n\) be its synchronous update on an indexed cyclic ring of \(n\ge1\) sites. A *primitive temporal two-cycle* means a pair \(x\ne F_{r,n}(x)\) with \(F_{r,n}^2(x)=x\); spatial rotations are **not** identified.

**Sharp universal finite-witness theorem.** A rule has a primitive temporal two-cycle on any finite cyclic ring if and only if it has one at some length \(1\le n\le6\). The upper bound six cannot be decreased. Across all 256 rules, the distribution of their least qualifying ring length is

| Least \(n\) | None | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Number of rules | 107 | 64 | 48 | 6 | 17 | 2 | 12 |

The twelve rules attaining six are `26,82,90,154,164,165,166,167,180,181,210,218`. For example, Rule 90 on the six-site ring has \(101000\mapsto000101\mapsto101000\), but no primitive two-cycle at any smaller ring length.

**Exact all-length census.** There are explicitly constructible Boolean adjacency matrices \(A_r\) of size \(4\times4\) and \(B_r\) of size \(16\times16\), respectively, such that for every \(n\ge1\)

\[
\#\operatorname{Fix}(F_{r,n})=\operatorname{tr}(A_r^n),\qquad
\#\operatorname{Fix}(F_{r,n}^{2})=\operatorname{tr}(B_r^n).
\]

The primitive temporal two-cycle count, as unoriented time orbits of labelled configurations, is exactly

\[
C_r(n)=\frac{\operatorname{tr}(B_r^n)-\operatorname{tr}(A_r^n)}2.
\]

For \(j=1,2\), the corresponding spatial dynamical zeta series are \(\zeta_{j,r}(z)=\exp(\sum_{n\ge1}\#\operatorname{Fix}(F_{r,n}^{j})z^n/n)\), with exact rational expressions

\[
\zeta_{1,r}(z)=\frac1{\det(I-zA_r)},\qquad
\zeta_{2,r}(z)=\frac1{\det(I-zB_r)}.
\]

The 256 rules realize exactly **23 distinct first-iterate zeta denominators**, **40 distinct second-iterate denominators**, and **51 distinct ordered denominator pairs**. Exactly 107 rules have identical first- and second-iterate denominator polynomials, which is equivalent to having no primitive temporal two-cycle on any finite cyclic ring. The accompanying `rule_table.csv` provides both denominator polynomials for each rule and its least two-cycle witness length.

## Assumptions and scope

The convention for a three-bit neighborhood is \(f_r(a,b,c)=\lfloor r/2^{4a+2b+c}\rfloor\bmod2\). For a cyclic word \(x\), its image at position \(i\) is \(f_r(x_{i-1},x_i,x_{i+1})\), indices being modulo \(n\). When \(n=1\) or \(n=2\), repeated neighbor positions are allowed by this definition; no distinct-neighbor convention is imposed. The theorem concerns **finite spatially periodic configurations**, not necessarily all temporally periodic bi-infinite configurations. The zeta variable \(z\) is formal, and the two-step periodicity condition includes fixed configurations, which are removed when counting primitive temporal two-cycles.

## Proof

**1. Four-state fixed-point graph.** Let the vertices of \(A_r\) be all ordered binary pairs \(ab\). Place an edge from \(ab\) to \(bc\) precisely when \(f_r(a,b,c)=b\). Closed walks of length \(n\), with their starting position distinguished, correspond bijectively to indexed cyclic \(n\)-words fixed by \(F_{r,n}\): the consecutive overlapping pairs recover the unique word, and the edge conditions enforce every coordinate. This remains true at lengths one and two. Hence the first trace formula.

**2. Sixteen-state second-iterate graph.** Let the vertices of \(B_r\) be all ordered binary four-tuples \(abcd\). Place an edge from \(abcd\) to \(bcde\) precisely when

\[
f_r\bigl(f_r(a,b,c),f_r(b,c,d),f_r(c,d,e)\bigr)=c.\]

A cyclic closed walk corresponds bijectively to a word fixed by two iterations. This proves the second trace formula, as well as the orbit count after subtracting fixed points and dividing by two. The standard formal identity \(\exp(\sum_{n\ge1}\operatorname{tr}(T^n)z^n/n)=\det(I-zT)^{-1}\) proves both zeta formulas.

**3. Exact test for a genuine temporal oscillation.** Mark every permitted edge \(abcd\to bcde\) of the sixteen-state graph for which \(f_r(b,c,d)\ne c\). A closed walk is a primitive temporal two configuration precisely when it contains a marked edge. A finite directed graph has a closed walk containing a designated edge if and only if its endpoints lie in the same strongly connected component. Thus a finite, *all-spatial-length* decision procedure is: construct the sixteen-state graph, find its strongly connected components, and test for an internally contained marked edge. This criterion rules out arbitrarily long primitive temporal two-cycles for every negative rule; inspecting short rings alone would not suffice.

**4. Exact complete enumeration.** `verify_scc.py` implements the component test without third-party packages, independently enumerates all configurations on rings of lengths one through six, and compares the two decisions for each of the 256 rules. The resulting tally is exactly \(107,64,48,6,17,2,12\) for the listed length classes, with twelve explicit length-six witnesses in its output. Because *every* rule found positive by the graph test has an exhibited witness of length at most six, and every rule found negative is excluded for all lengths by the graph criterion, the six-site theorem is proved. The twelve rules whose first witness is at six establish sharpness. The finite, fully specified graph and exhaustive program form the complete classification certificate, rather than a statistical sample.

**5. Exact polynomial classification.** `verify_zeta.py` constructs \(A_r\) and \(B_r\), computes their integer characteristic polynomials using exact algebra, removes factors belonging to zero eigenvalues, and records the reversed nonzero coefficient lists as the coefficients of \(\det(I-zA_r)\) and \(\det(I-zB_r)\), in increasing powers of \(z\). Set cardinalities of the distinct polynomial tuples over all 256 rules are respectively 23, 40, and 51. Comparison of the two exact polynomials yields 107 identical pairs. Equality of the polynomials forces equality of traces for every positive power; conversely, a primitive temporal two-cycle creates a strictly positive trace difference at its ring length and so unequal polynomials. Together with step 3 this proves the claimed relationship between no cycles and polynomial equality.

## Verification

The reproducible certificate consists of `verify_scc.py` (Python 3 standard library), `verify_zeta.py` (Python 3 with SymPy), `rule_table.csv` (the full 256-rule polynomial and least-witness table), and two captured output files. `verify_scc.py` checks all 256 strongly connected component tests against all rings of lengths one through six. `verify_zeta.py` compares the trace sequences from exact characteristic-polynomial coefficients with independently evaluated bitwise updates for all 256 rules and spatial lengths one through nine (2,304 rule-length comparisons). These finite checks support the exact transfer-graph proof; the nine-length experiment itself is **not** used to infer any all-length assertion. Both scripts terminate with `PASS` on the recorded run. The table uses semicolon-separated coefficients with the constant term first; the value `none` records absence of a two-cycle at any spatial length, justified by the graph criterion.

## Relationship to prior work

Wolfram's 1983 treatment establishes the elementary binary rule framework. Banks and Djirar (1992) provide a graph-based method for cellular-automaton fixed points and shift cycles. Epperlein's 2015/2017 classification computes topological invariants, including temporal periodic-point structure, for the elementary rules; these results are highly relevant but do not state the present sharp six-site first-witness distribution or the tabulated forty exact second-iterate zeta polynomials. Koller and Hudcová (2025) study transfer-matrix trajectory-counting and entropy for elementary automata; they do not present this all-rule exact finite-ring temporal-two classification. Previous exact zeta analyses of individual rules, including Rules 18 and 73, cover special cases and are not rebranded here as new transfer techniques. The present contribution is the *sharp global finite-witness cutoff and complete joint two-iterate rational-zeta census*.

## Limitations

This is a computer-assisted finite classification resting on explicit 4-state and 16-state graph equivalences and exhaustive analysis of 256 rule tables. The scripts are not a formal proof assistant certificate or independent human validation. It does not assert a six-site test for temporally recurrent configurations of arbitrary bi-infinite spatial sequences, higher temporal periods, or cellular automata with larger neighborhoods. The small transfer-matrix method is classical; historical priority of the 256-rule numerical census is qualified by possible preexisting unpublished or unindexed tables and by the partial inspection of some older literature. The earliest verified public source used for the research direction is the 1983 Wolfram publication; this is **not** a claimed publication date for the finding.

## References

1. Stephen Wolfram, “Statistical mechanics of cellular automata,” *Reviews of Modern Physics* **55** (1983), 601–644. Published July 1, 1983. DOI: https://doi.org/10.1103/RevModPhys.55.601.
2. S. P. Banks and S. Djirar, “Fixed Points and Shift Cycles in Cellular Automata,” ACSE Research Report 459, University of Sheffield (1992), https://eprints.whiterose.ac.uk/id/eprint/79286/.
3. Jeremias Epperlein, “Topological Conjugacies Between Cellular Automata,” dissertation, TU Dresden (2017), Chapter 6 (describing results presented at Automata 2015), https://files01.core.ac.uk/download/pdf/236376428.pdf.
4. Cédric Koller and Barbora Hudcová, “Counting Short Trajectories in Elementary Cellular Automata using the Transfer Matrix Method,” preprint arXiv:2508.09768 (2025), https://arxiv.org/abs/2508.09768.
5. Published mathematical-record comparison, “Exact temporal-two orbit census and spatial zeta for elementary cellular automaton 18,” https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-temporal-two-orbit-census-and-spatial-zeta-for-elementary--752b17859ec3.
