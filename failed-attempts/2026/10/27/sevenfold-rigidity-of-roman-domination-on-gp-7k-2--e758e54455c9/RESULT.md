# Sevenfold rigidity of Roman domination on \(GP(7k,2)\)

## Finding

For every integer \(k\geq1\), put \(n=7k\) and let \(G=GP(n,2)\). There are **exactly seven** minimum-weight Roman dominating functions on the vertex-labelled graph \(G\). They are the seven cyclic translates of the following seven-column pattern, repeated \(k\) times:

\[
\begin{array}{c|rrrrrrr}
 i\pmod 7&0&1&2&3&4&5&6\\\hline
 f(v_i)&2&0&1&0&0&1&0\\
 f(u_i)&0&0&0&2&2&0&0
\end{array}
\]

Every minimum has weight \(8k\). For any two *distinct* minimum functions \(f,g\), their vertexwise Hamming distance is exactly
\[
|\{x\in V(G):f(x)\neq g(x)\}|=8k.
\]
In particular, the number of minimum functions stays seven as the graph grows, and no pair of minima differs at fewer than eight vertices.

## Assumptions and scope

The generalized Petersen graph has vertices \(v_i,u_i\) for \(i\in\mathbb Z_n\), and edges \(v_iv_{i+1}\), \(v_iu_i\), \(u_iu_{i+2}\) (all indices modulo \(n\)). The \(v\)-vertices form the outer cycle; the \(u\)-vertices form the inner circulant. A Roman dominating function (RDF) is a map \(f:V(G)\to\{0,1,2\}\) for which every vertex labelled zero has a neighbour labelled two. Its weight is \(w(f)=\sum_{x\in V(G)}f(x)\). All vertex indices are distinguished; functions are counted before quotienting by graph automorphisms. The parameter range is exactly \(n=7k\geq7\), not every \(n\).

## Proof

**An optimum exists in each of seven translates.** The displayed period-seven assignment satisfies the RDF condition: at each zero-labelled outer vertex, either an adjacent outer vertex or its spoke neighbour has value two; the same holds for each zero-labelled inner vertex using the two inner neighbours and its spoke. Directly checking residues \(0,\ldots,6\) establishes this even when the period is wrapped cyclically. Each period has three labels two and two labels one, hence weight eight. The seven rotations are distinct because the pattern has least period seven.

**Exact finite-state reduction.** Write a column as the digit \(q_i=3f(v_i)+f(u_i)\in\{0,\ldots,8\}\), with outer label \(\lfloor q_i/3\rfloor\) and inner label \(q_i\bmod3\). Form a directed graph \(T\) whose \(9^4=6561\) states are ordered four-tuples \((a,b,c,d)\) of digits. There is an arc
\[
 (a,b,c,d)\longrightarrow(b,c,d,e)
\]
precisely when the **central column \(c\)** is Roman-dominated by columns \(a,b,c,d,e\): if its outer label is zero, at least one of the outer labels of \(b,d\) or its own inner label equals two; if its inner label is zero, at least one of the inner labels of \(a,e\) or its own outer label equals two. Give the arc integer cost
\[
 C(a,b,c,d,e)=7\bigl(\lfloor e/3\rfloor+(e\bmod3)\bigr)-8.
\]
For every \(n\geq5\), cyclic sequences of \(n\) columns are RDFs if and only if their overlapping four-column states form length-\(n\) closed walks in \(T\); the total arc cost is exactly \(7w(f)-8n\). The sliding-window correspondence is bijective on cyclic vertex-labelled sequences. It neither identifies rotations nor assumes distinct symbols in consecutive columns.

**Finite potential-and-cycle lemma.** The accompanying executable `critical_cycle.cpp` constructs the entire graph \(T\), checks **48,681** admissible arcs, and calculates an integer potential \(h\) on every state. Initialize all \(h\)-values to zero and repeatedly apply \(h(t)\leftarrow\min\{h(t),h(s)+C(s,t)\}\) over all arcs. The relaxation stabilizes after four complete changing passes, followed by a pass with no changes. Direct verification of every arc establishes
\[
 C(s,t)+h(s)-h(t)\geq0.
\]
Thus every closed walk has nonnegative total cost. The subgraph of zero-slack arcs has **14,744** arcs and **6,555** strongly connected components. Exactly one component contains a directed cycle; it has seven states and seven internal arcs, with indegree and outdegree one internally at every state. Its ordered column-pair word is
\[
 (0,0),(1,0),(0,2),(0,2),(1,0),(0,0),(2,0),
\]
where the pair means (outer label, inner label). This is a cyclic shift of the displayed template. The exhaustively checked inequalities and the strongly connected component assertion are a finite lemma, rather than an inference from a bounded list of graph orders. The exact state encoding, comparison tests, relaxation, and component search are all present in the standalone code; `independent_critical.py` separately reconstructs the same finite lemma without graph-library dependencies.

**Equality forces the template.** For \(n=7k\), the constructed RDF has \(7w(f)-8n=0\). The potential inequality shows that no RDF can have lower weight. For any RDF having this exact weight, every traversed arc has zero slack, since the slacks are nonnegative integers whose cyclic sum is zero. Every closed walk in the zero-slack subgraph lies in a cyclic strongly connected component. Its only cyclic component is the single directed seven-cycle above. Consequently the column sequence is the stated seven-periodic word up to cyclic shift; since the graph has distinguished indices, exactly seven different functions occur.

**Pairwise distance.** For each of the six nonzero shifts of the seven-column template, direct comparison of its fourteen vertex labels gives eight discrepancies. Every length-\(7k\) sequence consists of \(k\) copies of that comparison, so the Hamming distance is \(8k\).

## Verification

Compile and run the standalone C++17 certificate with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic critical_cycle.cpp -o critical_cycle && ./critical_cycle`. Its checked output includes `states=6561 admissible_arcs=48681`, `tight_arcs=14744 total_scc=6555 cyclic_scc=1 cyclic_vertices=7 cyclic_arcs=7`, and `PASS`. The finite lemma is also reimplemented in `independent_critical.py` (standard-library Python 3). The programs were executed from the included source and their outputs compared with the included `.out` files.

An independent full search over possible two-labelled vertex sets in `independent_bruteforce.cpp` verifies that the minima at \(n=7\) and \(n=14\) have weight eight and sixteen, respectively, with precisely seven minimizers in each case. It also checks \(n=8\), where there are 104 minima; this is a useful reminder that the rigidity assertion is not claimed outside the specified congruence class. The finite small-order search is corroboration only: the proof for every \(k\) is the transfer-potential lemma and its equality analysis.

## Relationship to prior work

Wang, Xu, Yang and Ji established the already-known exact weight \(\gamma_R(GP(n,2))=\lceil8n/7\rceil\) and supplied a periodic construction attaining it. The known value and exhibited construction alone do not classify all minimizers. Their full preprint includes a discharging proof and detailed local lemmas but does not state a count of exactly seven minimizers at multiples of seven. The present claim is the **exhaustiveness and rigidity of all equality cases**, together with the exact distance between distinct minima; it does not re-claim the domination-number formula.

Zhang, Shao and Xu developed the general closed-walk transfer description for Roman domination of generalized Petersen graphs and computed the \(P(n,3)\) regime. Their 2014 Theorem 2 already covers the general correspondence between functions and weighted closed walks, including \(P(n,2)\); that correspondence is expressly credited here. Their paper does not identify the zero-excess critical subgraph or establish uniqueness up to seven shifts for \(P(7k,2)\). Thus only the new equality-component calculation and its classification are attributed to this finding.

## Limitations

The uniqueness proof uses a finite, explicitly replayable 6,561-state certificate; it is not presented as a handwritten case-free classification. No independent external audit is implied by the executable checks. The result applies to ordinary Roman domination on \(GP(7k,2)\), not to double, weak, total, or signed Roman domination, and it does not classify minima for other residue classes of \(n\). An unindexed published solution with an equivalent enumeration cannot be ruled out solely by literature searching.

## References

1. H. Wang, X. Xu, Y. Yang and C. Ji, *Roman domination number of Generalized Petersen Graphs \(P(n,2)\)*, arXiv:1103.2419v1 (first posted 2011-03-12), https://arxiv.org/html/1103.2419v1 ; *Ars Combinatoria* **112** (2013), 479–492.
2. Z. Zhang, Z. Shao and X. Xu, *On the Roman Domination Numbers of Generalized Petersen Graphs*, *Journal of Combinatorial Mathematics and Combinatorial Computing* **89** (2014), 311–320, https://combinatorialpress.com/article/jcmcc/Volume%20089/vol-089-paper%2023.pdf .
3. E. J. Cockayne, P. A. Dreyer, S. M. Hedetniemi and S. T. Hedetniemi, *Roman domination in graphs*, *Discrete Mathematics* **278** (2004), 11–22 (foundational definition; cited in [1]).
