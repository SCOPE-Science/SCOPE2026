# Eighteen Nauru locating codes and a sharp five-sensor exchange threshold

## Finding

Let \(H=GP(12,5)\), the Nauru graph, and let \(\mathcal L(H)\) comprise its minimum ordinary locating-dominating vertex sets. Then
\[
\gamma_{LD}(H)=8,\qquad |\mathcal L(H)|=18.
\]
Writing subscripts modulo twelve, the eighteen sets are exactly the twelve sets
\[
 A_i=\{a_{i+4},a_{i+6},a_{i+9},a_{i+11}, b_i,b_{i+1},b_{i+2},b_{i+3}\},\quad 0\leq i<12,
\]
and the six sets
\[
 B_{r,s}=\{a_j: j\equiv r\pmod 3\}\cup\{b_j:j\equiv s\pmod 3\},\quad r,s\in\{0,1,2\},\ r\ne s.
\]
Every optimum is independent and meets each of the outer and inner vertex shores in four vertices. Every omitted vertex has one or two selected neighbors: eight omitted vertices have one, and eight have two. The bipartite incidence graph between the eight selected sensors and the eight doubly covered omitted vertices is precisely a disjoint union of two eight-cycles. The eighteen optima lie in one orbit under graph automorphisms, though the standard dihedral subgroup preserves the two displayed families.

The intersection distribution for unordered distinct minimum-code pairs is
\[
 \#\{\{S,T\}\subseteq\mathcal L(H): |S\cap T|=h\}
 =\begin{cases}27&h=0,\\36&h=2,\\72&h=3,\\18&h=4,\\0&\text{otherwise}.\end{cases}
\]
For an integer \(q\geq1\), join two optima by a *batch exchange of size at most* \(q\) when one may delete at most \(q\) selected vertices and add the same number in one step, retaining a minimum locating-dominating set after the step. No feasibility constraint is imposed on intermediate, partially exchanged sets. The resulting graphs satisfy
\[
 \mathcal R_q(H)\cong
 \begin{cases}
 18K_1,&1\leq q\leq3,\\
 3C_6,&q=4,
 \end{cases}
\]
while \(\mathcal R_5(H)\) is connected, ten-regular on eighteen vertices, has ninety edges, and has diameter two. In particular, five simultaneous replacements are necessary and sufficient to connect the optimum configuration space. All optima are frozen under ordinary one-sensor replacement.

## Assumptions and scope

The graph is the simple undirected graph with twenty-four labelled vertices \(a_i,b_i\), for \(i\in\mathbb Z/12\mathbb Z\), and precisely the edges
\[
 a_i a_{i+1},\qquad a_i b_i,\qquad b_i b_{i+5} \quad (i\in\mathbb Z/12\mathbb Z).
\]
Each vertex has degree three. A *locating-dominating set* \(S\subseteq V(H)\) satisfies: for every vertex \(v\notin S\), the open-neighborhood trace \(N(v)\cap S\) is nonempty, and all sixteen traces for omitted vertices (when \(|S|=8\)) are pairwise distinct. In particular, traces of selected vertices are not constrained. This is different from *open locating domination*, which additionally compares signatures of selected vertices. All counts use labelled vertices. The minimum-code exchange moves compare only valid configurations of equal cardinality.

## Proof

**Lower bound.** Let \(S\) be any locating-dominating set of cardinality \(k\), with \(t=24-k\) omitted vertices. At most \(k\) omitted vertices have a singleton signature, because all nonempty traces must be distinct. If \(s\) omitted vertices have singleton traces, the number of incidences between \(S\) and its complement is at least \(s+2(t-s)=2t-s\geq48-3k\), yet at most \(3k\) by cubic degree. Thus \(k\geq8\). At equality \(k=8\), every inequality is an equality: \(S\) is independent, precisely eight omitted vertices have singleton traces, and all eight remaining omitted vertices have distinct doubleton traces. This recovers the observed local rigidity without assuming the classification.

**Exact classification.** The finite, reproducible exhaustive lemma is as follows: among all \(\binom{24}{8}=735471\) eight-vertex subsets, exactly eighteen satisfy the defining condition, and these eighteen subsets coincide with the displayed \(A_i\) and \(B_{r,s}\). The complete lemma is certified by `check_all_masks.cpp`: it loops through every mask of cardinality at most eight (1,271,626 masks altogether), computes the twenty-four open-neighborhood bit masks using precisely the displayed edge definition, rejects a candidate if an omitted vertex has zero trace or if two omitted traces are equal, checks that no surviving candidate has size below eight, and asserts set equality of all survivors with the explicitly generated eighteen formulas. This exhausts all possible subsets in the claimed size range, rather than sampling them or extrapolating a finite experiment. The two formulas therefore also provide explicit existence witnesses for the lower bound.

**Geometric structure.** The independent checker `verify_nauru.py` builds the same graph from its three edge classes and tests every one of the \(\binom{12}{4}^2=245025\) subsets with four outer and four inner vertices. It recovers the same eighteen formula sets. For each it independently verifies the independence condition and the eight singleton/eight doubleton signature counts. The degree-two induced incidence graph between sensors and double-covered omitted vertices has sixteen vertices and two components, each of order eight; hence each is a cycle of length eight. These tests independently reproduce this finite structural assertion. To exhibit the merger of the displayed cyclic families under full graph automorphisms, map the vertex indices \(0,\ldots,23\), ordered \(a_0,\ldots,a_{11},b_0,\ldots,b_{11}\), by

`[4,5,17,12,0,1,13,20,8,9,21,16,3,6,22,19,11,2,18,15,7,10,14,23]`.

The checker verifies this is an edge-preserving permutation and sends \(A_0\) to \(B_{0,1}\); rotations and reflections of indices are graph automorphisms transitive within each of the two displayed families. Hence there is one full-automorphism orbit.

**Intersection and relocation.** For distinct \(A_i,A_j\), the overlap size depends on \(d=j-i\pmod {12}\); for \(d=1,\ldots,11\), the values are respectively

`3,4,2,0,3,0,3,0,2,4,3`.

Among the 72 mixed \(A\)-\(B\) pairs, 48 have intersection three and 24 have intersection two. Among the fifteen \(B\)-\(B\) pairs, six have intersection four and nine have intersection zero. Together with the 66 \(A\)-\(A\) pairs these yield the stated complete 153-pair intersection distribution. A permitted batch exchange is exactly the inequality \(|S\cap T|\geq8-q\), because \(|S|=|T|=8\). At \(q=4\) the only exchanges among \(A\)-sets connect \(A_i\) with \(A_{i\pm2}\), yielding two six-cycles; the six \(B\)-sets yield a third six-cycle and there are no mixed exchanges. At \(q=5\), directly applying this intersection rule to the eighteen explicit masks gives ten neighbors per mask and graph diameter two, as checked from every source by complete breadth-first search in `verify_nauru.py`. The \(q\leq3\) cases have no edges since distinct minima overlap in at most four vertices.

## Verification

Two standalone, standard-library-only certificates are included. For the independent exhaustive classifier, compile `check_all_masks.cpp` using `c++ -O3 -std=c++17 check_all_masks.cpp -o check_all_masks` and execute `./check_all_masks`; expected output: `VERIFY_FULL_OK tested=1271626 minima=18`. For the independent structural and relocation checker run `python3 verify_nauru.py`; expected output: `VERIFY_OK 245025_BALANCED_CANDIDATES 18_MINIMUM_CODES 3C6_THRESHOLD4 CONNECTED_THRESHOLD5_DIAMETER2`. Both commands were executed against the included file contents and produced their expected outputs. The enumerations cover the stated finite graph and the entire minimum-size search domain; no unbounded extrapolation is made.

## Relationship to prior work

The general cubic locating-domination bound, including \(\gamma_{LD}(H)\geq8\), is already implied by known order-and-degree inequalities; it is included for completeness, not claimed as new. Published work gives exact ordinary locating-domination results for generalized Petersen graphs with inner step two and selected step-four ranges, but does not cover the inner step five graph considered here. An earlier result on *open locating domination* treats all generalized Petersen graphs but imposes a stronger signature condition on every vertex and therefore neither counts the ordinary locating-dominating eight-sets nor determines their exchange graph. The new finite content is the complete eighteen-code classification, structural geometry, and sharp multi-token mobility threshold.

## Limitations

This is a theorem about the one graph \(GP(12,5)\), not a family-wide bound. The finite exhaustive certificate is a complete search of the stated domain, but there is no independent external mathematical audit and no guarantee that all obscure or unpublished sources have been identified. General one-step reconfiguration and fixed-batch replacement are different rules; the latter allows simultaneous deletion and insertion. The case \(q\geq5\) is connected by monotonicity, but further diameters and graph isomorphism types at higher batch budgets are not determined here.

## References

- A. K. Abdul Gafur and S. W. Saputro, *On Locating-Dominating Set of Regular Graphs*, Journal of Mathematics (2021), DOI: [10.1155/2021/8147514](https://doi.org/10.1155/2021/8147514) (first published 2021-09-25). Addresses dense regular graph classes, not cubic Nauru.
- N. Bousquet et al., *Locating-dominating sets: From graphs to oriented graphs*, [arXiv:2112.01910](https://arxiv.org/abs/2112.01910) (2021-12-03). Definitions and general degree lower bounds.
- S. Hayat, A. Khan, M. J. F. Alenazi and S. Wang, *On the binary locating-domination number of regular and strongly-regular graphs*, Journal of Mathematical Inequalities 17 (2023), 1597–1623, [DOI:10.7153/jmi-2023-17-105](https://doi.org/10.7153/jmi-2023-17-105). Specific generalized Petersen results for steps two and four.
- Z. Maksimović, M. Bogdanović, J. Kratica and A. Savić, *Open-locating-dominating number of generalized Petersen graphs*, SYM-OP-IS 2018 proceedings, [repository record](https://research.matf.bg.ac.rs/handle/123456789/2144). A distinct stronger sensor predicate.
- B. Bjorkman et al., *Power domination reconfiguration*, [arXiv:2201.01798](https://arxiv.org/abs/2201.01798) (2022-01-05). Reconfiguration framework for a different domination invariant.
- T. Křišťan and J. Svoboda, *Reconfiguration Using Generalized Token Jumping*, [arXiv:2411.12582](https://arxiv.org/abs/2411.12582) (2024-11-19). General simultaneous-replacement framework, without the graph-specific exact calculation.
- E. W. Weisstein, *Nauru Graph*, [MathWorld](https://mathworld.wolfram.com/NauruGraph.html). Canonical graph identification.
