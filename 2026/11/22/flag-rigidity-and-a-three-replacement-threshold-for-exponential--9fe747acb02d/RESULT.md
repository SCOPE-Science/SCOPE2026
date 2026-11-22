# Flag rigidity and a three-replacement threshold for exponential domination in the Tutte–Coxeter graph

## Finding

Let \(G\) be the thirty-vertex Tutte–Coxeter graph, the point–line incidence graph of the generalized quadrangle \(\mathrm{GQ}(2,2)\). For a source set \(S\subseteq V(G)\) and a vertex \(u\notin S\), define its nonporous exponential influence by

\[
 w_S(u)=\sum_{s\in S}2^{1-d_{G-(S\setminus\{s\})}(u,s)},
\]

where a disconnected distance contributes zero. A set is exponentially dominating if every unselected vertex receives influence at least one; sources are deemed covered by definition.

**Theorem.** The exponential domination number is \(\gamma_e(G)=4\), and the exactly \(45\) minimum exponential dominating sets are indexed bijectively by the \(45\) incident point–line flags \((r,\ell)\) of \(\mathrm{GQ}(2,2)\):

\[
 S(r,\ell)=\bigl((\ell\cap P)\setminus\{r\}\bigr)
 \;\cup\;\bigl((\{m\in L:r\in m\})\setminus\{\ell\}\bigr).
\]

Here \(P\) and \(L\) respectively denote point and line vertices, so \(S(r,\ell)\) has the other two points of \(\ell\) and the other two lines through \(r\). The \(45\) sets form one orbit under permutations of the six symbols in the duad–syntheme model. For each such set, its \(26\) unselected vertices have the **exact nonporous influence profile** \(16\) vertices of weight \(9/8\), \(8\) of weight \(21/16\), and \(2\) of weight \(3\). In particular all optima have a strict \(1/8\) influence margin.

Define the \(k\)-replacement graph on these optimal sets by joining distinct sets whenever at most \(k\) selected vertices must be replaced simultaneously, with the resulting set again optimal. The sharp connectivity threshold is \(k=3\): the one- and two-replacement graphs have \(45\) isolated vertices, whereas the three-replacement graph is connected, \(20\)-regular, has \(450\) edges and diameter and radius \(2\).

## Assumptions and scope

Work with a fixed six-symbol set, say \(\{0,1,2,3,4,5\}\). A *duad* is a two-symbol subset; a *syntheme* is a partition into three duads. There are \(15\) of each. The graph has these \(30\) objects as vertices, with incidence when a duad is a member of a syntheme. The graph is cubic, bipartite, has girth eight and diameter four. Every vertex has graph-distance spheres of sizes \((1,3,6,12,8)\) at distances zero through four. No arbitrary graph of the same degree, order or diameter is covered by the theorem.

For the *porous* version, use ordinary graph distances instead of distances that avoid other selected sources, and write \(w_S^*(u)\). Always \(w_S(u)\le w_S^*(u)\). A nonporous set must therefore pass every porous necessary condition, but passing the porous test alone is not generally sufficient for nonporous domination.

## Proof

**1. No solution with at most three sources.** Three sources on the point shore hit at most nine of the fifteen line vertices, so an untouched line receives porous influence \(3/4\), below one; the dual case is the same. With two point sources and one line source \(m\), there are eight lines disjoint from \(m\). Each chosen point is on at most two of these eight lines, so some such line is incident with neither point source. Its porous influence is \(2(1/4)+1/8=5/8\). The dual argument excludes one point and two line sources. Thus no three-source porous solution exists. By monotonicity of porous influence, no smaller set works either.

**2. Four sources cannot be entirely on one shore.** The graph on the fifteen duads, with adjacency when two duads are disjoint, is strongly regular with parameters \((15,6,1,3)\). For four selected duads, an unselected duad collinear with \(c\) selected duads has porous influence \((4+3c)/8\). Coverage would require \(c\ge2\) at all eleven unselected duads. If the selected four induce \(e\) edges of the collinearity graph, summing the eleven neighbor counts gives \(24-2e\ge22\), hence \(e\le1\).

When \(e=1\), every unselected duad would have exactly two selected neighbors, giving \(\sum\binom{c}{2}=11\). Counting instead over the six selected pairs, one adjacent and five nonadjacent, yields \(1+5\cdot3=16\), a contradiction. When \(e=0\), the eleven neighbor counts must all be at least two and sum to twenty-four. They are therefore either nine twos and two threes, or ten twos and one four; in these cases \(\sum\binom{c}{2}\) equals fifteen or sixteen. But all six selected pairs are nonadjacent and each has three common neighbors outside the selected set, requiring eighteen. Contradiction. Point–line duality excludes four sources solely on the line shore.

**3. A three–one split fails.** If the four sources consist of three points and one line \(m\), each point is on at most two of the eight lines disjoint from \(m\). Hence some line disjoint from \(m\) is incident with none of the three chosen points, and has porous weight \(3(1/4)+1/8=7/8\). Duality excludes one point and three lines. Thus every four-source solution has two point and two line vertices.

**4. The two–two split forces a unique flag.** Let the two selected duads be \(p,q\). Every other duad that meets both \(p\) and \(q\) must belong to one of the two selected synthemes: otherwise that duad would be at distance four from both selected points and distance three from both selected lines, giving porous influence \(2(1/8)+2(1/4)=3/4\).

If \(p,q\) intersect, after renaming symbols write \(p=ab\) and \(q=ac\). The four other duads meeting both are \(ad,ae,af,bc\). The first three pairwise intersect, so no syntheme can contain two of them. Two selected synthemes cannot cover all three. Thus \(p,q\) are disjoint, say \(p=ab\), \(q=cd\), with remaining symbols \(e,f\). The four duads meeting both are exactly \(ac,ad,bc,bd\). Each syntheme can cover at most two, and the only way for two synthemes to cover all four is to choose

\[
 \{ac,bd,ef\},\qquad \{ad,bc,ef\}.
\]

The third syntheme through \(ef\) is \(\ell=\{ab,cd,ef\}\). Thus the proposed set is precisely \(S(ef,\ell)\). Every disjoint duad pair fixes one such flag, and there are \(15\cdot6/2=45\) disjoint duad pairs. Consequently every four-source solution, if feasible, must be one of the claimed \(45\) sets.

**5. These sets really dominate under blocked-source distances.** Permutations of the six symbols act transitively on the \(45\) flags. It is enough to check one: take point sources \(01,23\) and line sources \(\{02,13,45\}\), \(\{03,12,45\}\). Computing breadth-first distances after deleting the other three sources separately for each influence term gives exactly the outside-source weight multiset

\[
 \{(9/8)^{[16]},\ (21/16)^{[8]},\ 3^{[2]}\}.
\]

Here square-bracket superscripts indicate multiplicity, not powers. In particular the minimum is \(9/8\). The two independent exact checkers supplied with this result compute these blocked-source distances on independently constructed graphs. Together with Steps 1–4, this proves the minimum and the full classification.

**6. The exchange threshold.** Two distinct optimal sets share at most one vertex. Sharing their two point sources determines the line containing both and hence the omitted third point; sharing their two line sources determines their intersection and the omitted third line. Sharing a point source and a line source also determines the flag uniquely, by the generalized-quadrangle axiom giving the unique line through the point meeting the chosen line. Thus no distinct optimizers admit a one- or two-vertex replacement.

Each of the thirty base vertices occurs in exactly six optimal sets (three incident flags, two choices of the omitted point or line within each), and no two optimal sets can share two vertices. Therefore each optimum has \(4(6-1)=20\) neighbors when three replacements are allowed, and the three-replacement graph has \(45\cdot20/2=450\) edges. A complete exact breadth-first search on these \(45\) flag-indexed configurations, reproduced by both scripts, proves connectivity and diameter two. This is a finite exhaustive conclusion on a fully specified \(45\)-vertex exchange graph, not an inference from sample paths.

## Verification

Run `python3 verify_duads.py` and `python3 verify_symplectic.py` using only a Python 3 standard library. The first constructs all duads and synthemes, enumerates every \(k\)-subset with \(0\le k\le4\) (in particular all \(\binom{30}{4}=27405\) four-sets), establishes porous counts \((0,0,0,0,45)\), matches all flags, calculates every nonporous influence exactly as a rational number, verifies the full symbol-permutation orbit and computes the exchange graph. The second independently builds the generalized quadrangle from totally isotropic binary two-spaces in a four-dimensional symplectic vector space, repeats all counts and computes blocked-source influence and reconfiguration directly. Both terminate with assertions and print `PASS` only on successful completion.

These programs supply independently constructed finite checks of the classification, distance normalization, and the only finite graph-diameter calculation. They do not claim an independent human audit.

## Relationship to prior work

Dankelmann, Day, Erwin, Mukwembi and Swart introduced nonporous and porous exponential domination and established general diameter/order bounds. Bessy, Ochem and Rautenbach developed general exponential-domination bounds and bounds and methods for subcubic graphs, motivated in part by girth and cages; their general results do not give the exact Tutte–Coxeter optimizer family or the three-replacement threshold. The duad–syntheme graph representation and its six-symbol symmetry are classical; Baez's 2015 exposition explicitly describes them. The new content here is the exact nonporous optimum classification, the strict influence profile and the optimizer reconfiguration geometry, not the definitions or the graph itself. Other graph-domination, contagion, burning, and edge-matching invariants on this graph do not imply this weighted blocked-source claim.

## Limitations

The theorem is for a single canonical thirty-vertex graph; it is not asserted for all generalized quadrangles, all cubic cages or arbitrary cubic graphs. The two implementations are exhaustive finite mathematical certificates, not substitutes for independent scholarly review. The priority comparison covered the directly relevant original and subcubic literature, geometric graph references, related later exponential-domination work, and available indexed claims; an unindexed older enumeration or equivalent structural characterization cannot be excluded categorically.

## References

- P. Dankelmann, D. Day, D. Erwin, S. Mukwembi, H. C. Swart, *Domination with exponential decay*, Discrete Mathematics 309 (2009), 5877–5883. https://doi.org/10.1016/j.disc.2008.06.040 . Author-uploaded text: https://www.academia.edu/765944/Domination_with_exponential_decay .
- S. Bessy, P. Ochem, D. Rautenbach, *Bounds on the Exponential Domination Number*, first arXiv version 29 October 2015, https://arxiv.org/abs/1510.08749 .
- S. Bessy, P. Ochem, D. Rautenbach, *Exponential Domination in Subcubic Graphs*, first arXiv version 4 November 2015, https://arxiv.org/abs/1511.01398 ; journal DOI https://doi.org/10.37236/5711 .
- J. Baez, *Tutte–Coxeter Graph*, 15 August 2015, https://blogs.ams.org/visualinsight/2015/08/15/tutte-coxeter-graph/ .
- B. Atay Atakul, *Stability and domination exponentially in some graphs*, AIMS Mathematics 5 (2020), 5063–5075, https://doi.org/10.3934/math.2020325 .
