# Sharp counting-free finite-variable theories of Hamming graphs

## Finding

For integers \(d\ge1\) and \(q\ge2\), let \(H(d,q)\) be the simple undirected graph with vertex set \(\{0,\ldots,q-1\}^{d}\), in which distinct vertices are adjacent precisely when their coordinate words differ in exactly one position. All logical statements below use only equality and the binary adjacency relation \(E\); there are **no counting quantifiers**. Write \(G\equiv_{\mathrm{FO}^{k}}G'\) when the two graphs agree on every first-order sentence using at most \(k\) distinct variable names, allowing those names to be requantified without any restriction on quantifier depth.

**Theorem (all widths and both Hamming parameters).** For \(d,e\ge1\), \(q,r\ge2\), and \(k\ge1\):

1. At \(k=1\), all the graphs \(H(d,q)\) have the same theory.
2. At \(k=2\), \(H(d,q)\equiv_{\mathrm{FO}^{2}}H(e,r)\) if and only if either \(d=e=1\), or \(d,e\ge2\). Thus there are exactly two theories.
3. For every \(k\ge3\),
   \[
   H(d,q)\equiv_{\mathrm{FO}^{k}}H(e,r)
   \quad\Longleftrightarrow\quad
   d=e\ \text{ and }\ \min(q,k)=\min(r,k).
   \]

Consequently, for each \(k\ge3\) and each fixed dimension \(d\), there are precisely \(k-1\) theories, one for each truncated alphabet size \(2,\ldots,k\). The unique smallest graph (by vertex count) representing the theory of \(H(d,q)\) **within this Hamming family** is \(H(d,\min(q,k))\), with exactly \((\min(q,k))^d\) vertices. The least variable width separating a given \(H(d,q)\) from all nonisomorphic members of this family is exactly \(q+1\), **independent of the dimension**. The variable-width hierarchy on the family is strict at each transition.

The quantifiers in this theorem range over all the finite Hamming graphs with the stated parameters. It is a relative classification of their theories, not a statement that these graphs can be defined among all finite graphs with \(q+1\) variables.

## Assumptions and scope

A graph is a nonempty finite simple undirected structure for the signature \(\{E,=\}\). Dimensions \(d\) and \(e\) are positive; alphabet sizes \(q\) and \(r\) are at least two. Different alphabet symbols are not named by constants or unary predicates; coordinate places are not named or ordered in the logical language. There is no ability to count neighbors directly. The theory equivalence concerns arbitrary quantifier nesting, rather than equivalence truncated to a finite quantifier rank. A *relative defining width* is the smallest \(k\) for which no nonisomorphic graph of this Hamming family shares the specified graph's \(\mathrm{FO}^{k}\) theory.

## Proof

**A. Coordinatewise invariant for arbitrary width.** Fix a dimension \(d\ge1\) and an integer \(k\ge2\). Suppose the two alphabets have sizes \(q,r\ge k\). In the usual \(k\)-pebble equivalence game, Duplicator maintains the following invariant: for every coordinate index \(j\in\{1,\ldots,d\}\), and for every pair \(a,b\) of occupied pebble labels,
\[
  v_a(j)=v_b(j)\quad\Longleftrightarrow\quad w_a(j)=w_b(j).
\]
Here \(v_a,w_a\) denote the vertices carrying corresponding pebble labels. This condition is vacuous before the first move. When a pebble moves, erase its old occurrences; at most \(k-1\) labels survive. In each coordinate \(j\), the surviving vertices use at most \(k-1\) different alphabet symbols. If Spoiler's new symbol is equal to a surviving symbol, use the corresponding symbol on the other side. Otherwise choose a symbol distinct from every surviving one, which exists because that alphabet has at least \(k\) symbols. Choose the response independently in each coordinate. The invariant is restored in both directions of play.

This invariant preserves whether any two pebbled vertices are equal (all coordinate entries equal) and whether they are adjacent (different in precisely one coordinate). It therefore preserves every atomic statement, including all repetitions of a variable. This is a permanent, not a bounded-round, winning strategy. By the standard pebble-game characterization, the two graphs agree on all \(\mathrm{FO}^{k}\) sentences. If \(q=r<k\), they are already isomorphic, so the same conclusion holds whenever \(\min(q,k)=\min(r,k)\).

**B. Three variables can see the entire dimension.** Graph distance in \(H(d,q)\) equals Hamming distance between words, so its diameter is exactly \(d\). For every fixed nonnegative integer \(t\), the predicate \(\operatorname{dist}(x,y)\le t\) has a first-order definition using only the three variable names \(x,y,z\). Start with \(\delta_0(x,y):=(x=y)\) and recursively express
\[
\delta_{t+1}(x,y):=\delta_t(x,y)\ \lor\ \exists z\bigl(E(x,z)\land\delta_t(z,y)\bigr).
\]
At each expansion, rename bound occurrences cyclically among \(x,y,z\), so the two displayed free names are never captured; this uses no fourth name. The corresponding sentences \(\forall x\forall y\,\delta_t(x,y)\) distinguish a graph of diameter at most \(t\) from one of greater diameter. Thus when \(k\ge3\), graphs of different dimensions cannot be equivalent, irrespective of alphabet sizes.

**C. The clique obstruction detects every alphabet size below \(k\).** The clique number of \(H(d,q)\) is exactly \(q\). A coordinate line, consisting of all words differing only in a fixed coordinate, is a clique of size \(q\). Conversely, fix a vertex \(v\) in any clique of at least three vertices. Every other vertex in that clique differs from \(v\) in one coordinate; two such neighbors corresponding to different coordinates would differ in two coordinates and would be nonadjacent. Hence the whole clique is contained in one coordinate line. The existence of a clique of any specified size \(s\le k\) is expressible by an existential sentence using \(s\) different variables. If \(\min(q,k)\ne\min(r,k)\), then one alphabet size, say \(q\), is smaller than \(k\) and the other is at least \(q+1\). The sentence asserting a \((q+1)\)-clique separates the graphs. This combines with A and B to prove part 3.

**D. The one- and two-variable boundary.** In the one-variable language, an atomic formula is either \(x=x\) (always true) or \(E(x,x)\) (always false). Every graph here is nonempty; thus all have the same \(\mathrm{FO}^{1}\) theory. At two variables, the class \(d=1\) consists of complete graphs on at least two vertices. Duplicator maintains equality or adjacency between at most two occupied pebbles, which is always possible on any two such complete graphs. For \(d\ge2\), every vertex has at least one distinct neighbor (change one coordinate) and at least one distinct nonneighbor (change two coordinates). Hence, against any other graph of this latter class, when one pebble moves, Duplicator can match exactly one of the three atomic possibilities relative to the remaining pebble: equality, adjacency, or distinct nonadjacency. No other binary atomic relations exist. This is a permanent two-pebble strategy. Finally, the two classes are separated by the two-variable sentence \(\exists x\exists y\,(x\ne y\land\neg E(x,y))\), which holds precisely when \(d\ge2\). This proves parts 1 and 2.

**E. Theory counts, minimum representatives, and sharp width.** For each \(k\ge3\), part 3 assigns the ordered pair \((d,\min(q,k))\) uniquely to an equivalence class. With \(d\) fixed, the second entry takes exactly \(k-1\) values \(2,\ldots,k\); for varying dimensions there are countably infinitely many classes. Among representatives of a given class, both \(d\) and the truncated alphabet are fixed, and the vertex number \(q^d\) is increasing in \(q\). This proves the minimum-representative statement. For a particular \(H(d,q)\), every \(k\le q\) fails to distinguish it from \(H(d,q+1)\): this is immediate from the one/two-variable cases and from part 3 for \(k\ge3\). At \(k=q+1\), dimension and the exact alphabet size \(q\) are distinguishable from all other parameters, establishing the relative width \(q+1\). Strictness at width one-to-two is witnessed by \(H(1,2)\) versus \(H(2,2)\); at two-to-three by \(H(1,2)\) versus \(H(1,3)\); and at width \(k\ge3\) by \(H(1,k)\) versus \(H(1,k+1)\), which become distinguishable at \(k+1\).

## Verification

The standalone Python program `check_hamming_logic.py` constructs orbit representatives for each \(k\)-tuple of vertices, taking the multiset of coordinatewise equality partitions as the orbit invariant under coordinate and alphabet permutations. For each orbit it explicitly enumerates all possible one-pebble replacements. It refines the resulting finite transition systems by atomic adjacency/equality colors and successor-color *sets* (not multisets, since this is counting-free logic) until stabilization. To compare two graphs it colors both systems in a common refinement, rather than comparing independently assigned color names.

The accompanying `logic_check_output.json` records 14 positive and negative sample comparisons with zero disagreements against the theorem, including the genuine upper-threshold checks at widths three and four. This method checks the finite samples only; the unrestricted conclusion is proved in paragraphs A–E. The verification needs only Python's standard library. Run `python check_hamming_logic.py` and compare its standard output to the accompanying JSON file.

## Relationship to prior work

Klavžar and Peterin's *Characterizing subgraphs of Hamming graphs* (published online 8 April 2005) treats Cartesian-product representations, embeddings, edge labelings and induced/isometric subgraphs; its available author preprint was examined, especially Sections 1, 3, and 4. Its stated theorems do not classify counting-free fixed-variable elementary theories.

Pikhurko and Verbitsky's *Logical complexity of graphs: a survey* (arXiv 2010) gives the graph-language and pebble-game framework, including the general three-variable graph-distance formula and results about graph identification. Its inspected discussion does not provide this joint dimension/alphabet classification.

Adler, Benediktsson and Macpherson's *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs* (first arXiv 2020, published 2022) studies model-theoretically motivated neighborhood set systems of precisely these graph families. Its fully accessible accepted manuscript, including Section 4, determines VC-dimension and VC-density, not \(\mathrm{FO}^{k}\) equivalence at unbounded quantifier rank.

Kotek and Makowsky's *Connection Matrices and the Definability of Graph Parameters* (arXiv 2013) studies Feferman–Vaught-style composition and connection matrices for graph operations. The inspected product results concern relational product constructions and definability of parameters; no exact unrestricted \(k\)-variable equivalence criterion for Hamming graph Cartesian powers was found there. More general composition theorems remain a priority risk.

The special case \(d=2\) is the square rook-graph case and is already covered by an earlier rectangular rook-graph classification based on the same coordinatewise technique. No novelty is asserted for \(d=2\). The full theorem covers **arbitrary and variable dimension**, identifies its exact logical visibility, and gives a dimension-independent minimal defining width. No checked source was found that states or logically implies this complete two-parameter result. A still-unidentified general Cartesian-product composition theorem could subsume it; originality is provisional pending independent literature review.

## Limitations

The result is relative to \(H(d,q)\) with uniform alphabet size on every coordinate, \(d\ge1\), \(q\ge2\). It does not automatically classify Cartesian products with unequal factor sizes, arbitrary induced subgraphs of Hamming graphs, graphs with named coordinates or color predicates, the counting-quantifier extension of first-order logic, or minimum defining width among **all** finite graphs. The witness formulas may be extremely long as dimension grows; no optimal quantifier-rank or formula-length bounds are asserted. Exhaustive literature priority is not established. The computational evidence is finite and is not independent certification of the universal theorem.

## References

1. S. Klavžar and I. Peterin, “Characterizing subgraphs of Hamming graphs,” *Journal of Graph Theory* 49 (2005), 302–312. DOI:10.1002/jgt.20084. Public online 2005-04-08. Author full text: https://mp.feri.um.si/osebne/peterin/clanki/JGT5672.pdf.
2. O. Pikhurko and O. Verbitsky, “Logical complexity of graphs: a survey,” arXiv:1003.4865 (first submitted 2010-03-25), https://arxiv.org/abs/1003.4865.
3. I. Adler, B. G. Benediktsson and D. Macpherson, “Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs,” arXiv:2007.16042 (first submitted 2020-07-31); *Discrete Applied Mathematics* 312 (2022), 29–44. Author accepted manuscript: https://eprints.whiterose.ac.uk/178584/1/Adler_Benediktsson_Macpherson.pdf.
4. T. Kotek and J. A. Makowsky, “Connection Matrices and the Definability of Graph Parameters,” arXiv:1308.3654 (first submitted 2013-08-16), https://arxiv.org/abs/1308.3654.
