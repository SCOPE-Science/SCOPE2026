# Cycle packing bounds for online learning of proper three-colourings

## Finding

For a finite simple graph \(G=(V,E)\), let \(n=|V|\). Regard each proper three-colouring \(c:V\to\{0,1,2\}\) as a Boolean concept on \(V\times\{0,1,2\}\) by declaring \((v,a)\) positive exactly when \(c(v)=a\). Write \(\nu_{\mathrm{cyc}}(G)\) for the largest cardinality of a collection of pairwise vertex-disjoint cycles in \(G\). Then

\[
\operatorname{Ldim}(\mathcal C_3(G))\le |V|-\nu_{\mathrm{cyc}}(G).
\]

**Equality holds for every pseudoforest** (a graph whose connected components are trees or connected unicyclic graphs). Hence, if \(u(G)\) is the number of unicyclic components of a pseudoforest, then

\[
\operatorname{Ldim}(\mathcal C_3(G))=|V|-u(G).
\]

In particular, every tree on \(n\) vertices has dimension \(n\), every connected unicyclic graph has dimension \(n-1\), and \(\operatorname{Ldim}(\mathcal C_3(G))=|V|\) holds for an arbitrary graph if and only if it is a forest. The cycle-packing bound is sharp for all feasible \(n\) and packing numbers, by taking disjoint triangles and isolated vertices.

The distinction between cycle count and vertex-disjoint cycle count is substantive: two four-cycles joined at a single common vertex have seven vertices, cycle-packing number one, and exact Littlestone dimension six (the latter is a finite exhaustive computation; see Verification).

## Assumptions and scope

Graphs are finite, undirected, simple, and may be disconnected or empty. A proper three-colouring assigns different values in \(\{0,1,2\}\) across each edge. A query asks one yes/no equality to a *specified* colour, not the multiclass colour itself. Littlestone dimension is the maximum depth of a complete binary decision tree whose every root-to-leaf answer sequence is realised by a proper colouring; a concept class with at most one concept has dimension zero, including the empty class. A cycle has length at least three; a pseudoforest has at most one cycle in every component. These conventions matter for disconnected graphs, non-three-colourable graphs, and isolated vertices.

## Proof

**1. Elementary facts.** A complete binary mistake tree of depth \(d\) requires at least \(2^d\) distinct concepts. For a Cartesian product of two **nonempty** concept classes on disjoint query universes, Littlestone dimension is additive. To prove the latter, graft a complete tree for the second class at every leaf of a complete tree for the first, giving the lower bound. For the upper bound, induct on the number of concepts: every nontrivial binary split on the first factor has a child whose dimension is at least one below the factor dimension (by the defining recursion), while the corresponding product child satisfies the claimed bound by induction; queries on the second factor are symmetric. Also, taking a subclass cannot increase the dimension.

**2. Trees.** A tree on \(m\ge1\) vertices has exactly \(3\cdot2^{m-1}\) proper three-colourings, so its dimension is at most \(m\). Root the tree and first query whether the root has colour \(0\). On the positive branch, its colour is determined, and each of the other \(m-1\) vertices can be queried once in parent-before-child order, asking for one of the two colours different from its determined parent; either answer determines the child colour and can be extended. On the negative root branch, query whether the root has colour \(1\), which determines its colour from \(\{1,2\}\), and then similarly query \(m-2\) vertices, leaving one leaf unqueried. Both branches have a complete continuation of depth \(m-1\), so the overall depth is \(m\). For \(m=1\), a single equality query suffices. Thus \(\operatorname{Ldim}=m\).

**3. Cycles.** The number of proper three-colourings of the cycle on \(\ell\ge3\) vertices is

\[
\chi(C_\ell,3)=2^\ell+2(-1)^\ell.
\]

If \(\ell\) is odd this is below \(2^\ell\), precluding dimension \(\ell\). If \(\ell\) is even, global permutation symmetry of the colours makes each equality query positive for exactly \(\chi(C_\ell,3)/3\) concepts, strictly fewer than \(2^{\ell-1}\); therefore no depth-\(\ell\) mistake tree exists either. To attain depth \(\ell-1\), list vertices cyclically as \(v_1,\ldots,v_\ell\) and first query \((v_1,0)\). On the positive branch, \(v_1\) is fixed; query \(v_2,\ldots,v_{\ell-1}\) in order, each time choosing one of two colours permitted by its predecessor. The remaining vertex can always be coloured differently from its two neighbours using three colours. On the negative branch query \((v_1,1)\), fixing its colour, then query \(v_2,\ldots,v_{\ell-2}\), leaving the last two vertices to complete a length-three walk between prescribed endpoint colours. Such a walk exists with three colours for any prescribed endpoints. Both root branches support a continuation of depth \(\ell-2\), proving

\[
\operatorname{Ldim}(\mathcal C_3(C_\ell))=\ell-1.
\]

**4. Connected unicyclic graphs.** Let the unique cycle have length \(\ell\), and let the graph contain \(m\) additional vertices in attached trees. Its proper three-colourings number \((2^\ell+2(-1)^\ell)2^m\). For odd \(\ell\), this is less than \(2^{\ell+m}\), giving an upper bound \(\ell+m-1\). For even \(\ell\), every root equality query has positive branch of size \((2^\ell+2)2^m/3<2^{\ell+m-1}\), giving the same upper bound. For the lower bound, start with the depth-\(\ell-1\) complete tree for the cycle from Step 3. At each leaf select one consistent full cycle colouring. Extend that leaf by querying the \(m\) attached-tree vertices in parent-before-child order. Since the parent colour is fixed, each query has two feasible answers corresponding to the two other colours; either extends to a full proper colouring. This appends \(m\) levels at every leaf, yielding exact dimension \(\ell+m-1\).

**5. General graphs and pseudoforests.** Take \(r=\nu_{\mathrm{cyc}}(G)\) vertex-disjoint cycles and form a spanning subgraph \(H\) consisting of exactly these cycles and all remaining isolated vertices. Every proper colouring of \(G\) is also one of \(H\). By monotonicity, additivity, and Steps 2–3,

\[
\operatorname{Ldim}(\mathcal C_3(G))\le \operatorname{Ldim}(\mathcal C_3(H))
=\sum_{i=1}^{r}(|C_i|-1)+\bigl(n-\sum_i|C_i|\bigr)=n-r.
\]

For a pseudoforest, each component is a tree or is unicyclic. Additivity and Steps 2, 4 give equality, since the number of unicyclic components is the maximum number of disjoint cycles. A forest attains dimension \(n\); any graph containing a cycle satisfies the strictly smaller bound \(n-1\). The family of \(r\) disjoint triangles and \(n-3r\) isolated vertices shows sharpness for each \(0\le r\le\lfloor n/3\rfloor\).

## Verification

The accompanying `check_cycle_packing.py` enumerates proper three-colourings, computes exact finite Littlestone dimensions by the binary-split recurrence, finds vertex-disjoint cycle packings, and checks the general upper bound and pseudoforest equality. It covers all graphs through four vertices, all five-vertex graphs with at least four edges, and additional cycles, paths, stars, and pendant-cycle instances through eight vertices. It also checks the two-square seven-vertex boundary graph. The executable checker is a finite corroboration; the unrestricted theorem is established in the preceding proof. Run `python3 check_cycle_packing.py` with the Python standard library. The archived `checks_output.txt` reports the successful run.

## Relationship to prior work

Chudnovsky, Goedgebeur, Schaudt, and Zhong (2017) study three-colouring and list-colouring obstructions for forbidden induced-subgraph classes. This supplies the natural partial-colouring setting but does not address binary equality-query Littlestone dimension or vertex-disjoint cycle packing. Manurangsi and Rubinstein (2017) establish general complexity barriers for calculating VC and Littlestone dimensions; their results do not identify this exact graph family invariant. The isolated exact cycle case is an antecedent special case and is independently reproved above; the present theorem additionally handles arbitrary graphs by a cycle-packing bound and gives equality for every pseudoforest. These are comparisons of mathematical statements, not claims about absolute historical priority.

## Limitations

The cycle-packing upper bound need not be an equality for arbitrary graphs; equality is proved for pseudoforests only. A graph with no proper three-colouring has an empty concept class and dimension zero. The results concern Boolean vertex-colour equality queries, not online multiclass predictions or sequential algorithms constructing a proper colouring. The exact two-square boundary value is finite and established by a complete recursive enumeration, not by a general bicyclic formula. Earlier results under alternative graph-homomorphism or teaching-dimension terminology may affect historical attribution; independent review remains necessary.

## References

1. M. Chudnovsky, J. Goedgebeur, O. Schaudt, M. Zhong, *Obstructions for three-coloring and list three-coloring H-free graphs*, initial arXiv public release 2017-03-16, https://arxiv.org/abs/1703.05684 .
2. P. Manurangsi, A. Rubinstein, *Inapproximability of VC Dimension and Littlestone's Dimension*, initial arXiv public release 2017-05-26, https://arxiv.org/html/1705.09517v1 .
