# Sharp production capacity and rigid extremizers of acyclic regular grammars

## Finding

Fix any nonempty finite alphabet \(\Sigma\). An acyclic right-regular grammar has productions of the form \(A\to wB\) or \(A\to w\), where \(w\in\Sigma^*\), and is charged one unit per distinct production, regardless of the length of \(w\). Let \(C(p)\) be the largest possible number of distinct generated words among all such grammars with at most \(p\ge1\) productions. Then

\[
C(p)=\begin{cases}
1,&p=1,\\
3^{p/3},&p\equiv0\pmod3,\\
4\cdot3^{(p-4)/3},&p\equiv1\pmod3,\quad p\ge4,\\
2\cdot3^{(p-2)/3},&p\equiv2\pmod3.
\end{cases}
\]

This bound is attained over the *unary* alphabet \(\{a\}\), with generated language exactly \(\{a^j:0\le j<C(p)\}\). Every grammar attaining \(C(p)\), after deleting unused nonterminals, has a chain of nonterminals with parallel productions between consecutive chain vertices and final terminal productions: its successive branching numbers \(r_1,\ldots,r_t\) sum to \(p\), multiply to \(C(p)\), and each choice of a full derivation spells a different word. Conversely, all these conditions suffice for equality. The optimal branching multisets consist of threes, supplemented by one two when \(p\equiv2\pmod3\), and either a four or two twos when \(p\equiv1\pmod3\); the case \(p=1\) consists of one rule. The order of the branching levels is arbitrary.

For the natural unary finite interval \(U_N=\{\varepsilon,a,\ldots,a^{N-1}\}\), \(N\ge1\), its **exact acyclic regular production-cover complexity** is

\[
g_{\{a\}}(U_N)=\min\{p\ge1:C(p)\ge N\} =\frac{3\log N}{\log3}+O(1).
\]

## Assumptions and scope

The grammar model allows empty terminal strings in productions and finite terminal blocks of arbitrary length; the nonterminal-dependency relation must be acyclic. The production set counts distinct rules, not symbols or individual letters on the right-hand sides. The empty word is accepted only through a finite derivation. A cover of a finite language is a finite generated superset, and no restriction forbids words outside the covered language. The maximum-cardinality theorem applies to every nonempty finite alphabet; the exact cover-complexity corollary concerns the unary *consecutive-length* language \(U_N\), not every unary language of the same size. The state graph is a directed multigraph: rules with different labels may share source and destination.

## Proof

**1. Path-capacity recurrence.** Replace every production \(A\to wB\) by a directed labeled edge from \(A\) to \(B\) and every terminal production \(A\to w\) by an edge from \(A\) to one common terminal vertex \(\bot\). Because the grammar is acyclic, this is an acyclic multigraph. Every derivation is a path from the start vertex to \(\bot\), and two paths can spell the same word. Thus the number of distinct generated words does not exceed the number of start-to-terminal paths.

Let \(M(0)=1\) be the bound for the *empty continuation* at \(\bot\), and let \(M(p)\) be the maximum number of start-to-terminal paths with at most \(p\ge1\) edges. If the start has \(r\) outgoing edges, then \(1\le r\le p\). Removing those \(r\) edges leaves at most \(p-r\) edges; every outgoing edge can be followed by at most \(M(p-r)\) suffix paths. Consequently

\[
M(p)\le \max_{1\le r\le p} rM(p-r).
\]

For any positive composition \(p=r_1+\cdots+r_t\), a chain with \(r_i\) parallel edges in layer \(i\) has \(\prod_i r_i\) paths. This yields the matching lower bound and the recurrence

\[
M(p)=\max_{\substack{t\ge1,\ r_i\ge1\\\sum_i r_i=p}}\prod_i r_i.
\]

The elementary sum-product optimization eliminates parts of size one except for \(p=1\), replaces every part at least five by a strictly better pair consisting of three and the remainder, and replaces three twos by two threes. This gives exactly the displayed formula for \(C(p)=M(p)\). In particular, \(M(p)>M(p-1)\) for every \(p\ge2\) (with \(M(0)=M(1)=1\)).

**2. Equality rigidity.** Let \(p\ge2\) and suppose a grammar with at most \(p\) rules generates \(M(p)\) distinct words. Since \(M(p)>M(p-1)\), all \(p\) rules occur in paths from the start to the terminal vertex, and the path count is exactly \(M(p)\); no two complete paths have the same word label. If the start has \(r\) outgoing edges, equality in the preceding bound requires \(M(p)=rM(p-r)\), and each of their heads must support exactly \(M(p-r)\) suffix paths. For \(p\ge2\), equality is impossible with \(r=1\) or \(p-r=1\): the first uses \(M(p-1)<M(p)\); the second has at most \(p-1<M(p)\) paths. Hence either \(p-r=0\), when all edges terminate at \(\bot\), or \(e=p-r\ge2\).

In the latter case, \(M(e)>M(e-1)\) forces **every** one of the \(e\) remaining edges to lie on a suffix path from each head: omitting any edge would give at most \(M(e-1)\) suffix paths. Two distinct heads with this property would each reach the other (through its necessarily existing outgoing edges), contradicting acyclicity. Thus all \(r\) edges point to the same next nonterminal. Repeat the argument on the remaining \(e\) edges. Induction forces a chain of parallel-edge layers, with branching numbers whose product is \(M(p)\). Conversely, a layered chain with a maximizing composition and pairwise distinct path labels clearly generates \(M(p)\) words. The integer-break characterization of maximizing compositions gives exactly the branching-factor classification stated above. This proves all equality cases, not merely existence.

**3. A unary mixed-radix realization.** Choose any maximizing composition \(p=r_1+\cdots+r_t\). Define \(W_i=\prod_{j>i}r_j\), taking the empty product as one. At the \(i\)-th layer, use exactly \(r_i\) productions labeled \(a^{dW_i}\), with \(d=0,1,\ldots,r_i-1\); for the final layer the rules terminate, and at earlier layers they continue to the next nonterminal. The total number of rules is \(p\). The generated exponents are precisely

\[
\sum_{i=1}^{t}d_i W_i,\qquad 0\le d_i<r_i.
\]

By uniqueness and completeness of mixed-radix representation these are exactly all integers from zero to \(\prod_i r_i-1=M(p)-1\), each once. Hence the maximal distinct-word count is achievable over a unary alphabet.

**4. The exact cover threshold.** Every finite language generated by at most \(p\) rules has at most \(M(p)\) words, so covering \(U_N\), which contains \(N\) words, requires \(M(p)\ge N\). The unary mixed-radix grammar at this threshold generates exactly \(U_{M(p)}\), which contains \(U_N\). Thus the lower and upper production budgets coincide. Finally \(\log M(p)=\tfrac{p}{3}\log3+O(1)\), and inversion gives the stated logarithmic law with bounded additive error.

## Verification

The first standalone script `verification/verify_capacity.py` independently computes the composition recurrence for \(1\le p\le24\), constructs unary mixed-radix word sets, verifies all expected exponents without collisions, checks the explicit closed form, and tests every inverse cover threshold \(1\le N\le1000\). The second `verification/verify_graphs.py` exhausts **all directed acyclic multigraphs with a fixed topological ordering, between two and five vertices, and between one and nine edges**, permitting parallel edges; it checks the path bound and verifies that every maximizer in this finite search is a parallel-edge chain. The accompanying `.out` files contain actual execution results. These finite tests corroborate, but do not replace, the all-parameter proof above; they do not enumerate graphs with more vertices or higher edge budgets.

Reproduce using `python3 verification/verify_capacity.py` and `python3 verification/verify_graphs.py` from a directory containing the embedded files. Both use only the standard Python library.

## Relationship to prior work

Hetzl and Shadman, *The Regular Cover Problem is NP-complete* (first public November 12, 2026), establish computational hardness for general finite languages and provide the exact acyclic regular-grammar model used here; their Theorems 3.7 and 4.6 concern decision complexity, not the maximum language cardinality per production budget or the exact unary-interval cover threshold. Hetzl and Wolfsteiner (2019), Lemma 7, quote the previously known universal estimate \(|L(G)|\le2^{p-1}\) for linear grammars with \(p\) productions. The present sharp capacity \(M(p)\) improves it considerably, for example from 32 to 9 at \(p=6\), and classifies equality graphs. Wolfsteiner's 2020 dissertation (p.54) attributes logarithmic-size regular descriptions of arbitrary finite unary languages to Bucher et al. (1981), but the inspected statement gives neither this sharp cardinality formula nor the exhaustive equality/cover classification.

Hajac, Pacheco, Kaczmarczyk and Lowiel (2026) study the maximum *total number of paths over all start/end vertices* in an acyclic connected digraph with a fixed edge budget. This is a different path-count functional from the designated start-to-terminal count used here; its all-endpoint maximal bound is not the asserted sharp bound for the latter. Full-text comparison of that work remains outstanding.

## Limitations

The production-cost model charges one unit for arbitrary-length terminal labels; the exact values can change for strictly regular, single-letter-rule or symbol-count measures. The covering corollary applies to consecutive unary exponents only. A cardinality lower bound cannot by itself determine the cover complexity of arbitrary finite languages with \(N\) words. The derivation graph classification is up to renaming nonterminals and deleting unused vertices; labelings are classified by the necessary-and-sufficient *distinct complete path labels* condition, not by a separate closed enumeration of every allowable labeling. The 1981 Bucher–Maurer–Culík–Wotschke primary paper and the 2026 all-path graph primary full text could not be materially compared; exact historical priority, in particular a possible stronger classical graph extremal result, remains uncertain. No independent external validation has been performed.

## References

1. S. Hetzl and P. Shadman, *The Regular Cover Problem is NP-complete*, arXiv:2611.16562v1, posted November 12, 2026, https://arxiv.org/html/2611.16562v1 .
2. S. Hetzl and S. Wolfsteiner, *On the cover complexity of finite languages*, Theoretical Computer Science **798** (2019), 109–125, Lemma 7, https://www.dmg.tuwien.ac.at/hetzl/research/oncovcomp.pdf .
3. S. P. Wolfsteiner, *Grammatical Complexity of Finite Languages*, doctoral dissertation, TU Wien, 2020, Chapter 4, https://www.dmg.tuwien.ac.at/hetzl/teaching/d_wolfsteiner.pdf .
4. W. Bucher, H. A. Maurer, K. Culík II and D. Wotschke, *Concise description of finite languages*, Theoretical Computer Science **14** (1981), 227–246, https://doi.org/10.1016/0304-3975(81)90044-X .
5. P. M. Hajac, E. A. Pacheco, Ł. Kaczmarczyk and M. Lowiel, *The maximal dimensions of path and graph algebras*, arXiv:2606.16095, June 15, 2026, https://arxiv.org/abs/2606.16095 .
