# Truncated cycle-petal spectra in four-variable first-order logic

## Finding
Let \(\mathcal B\) be the family of finite simple undirected graphs obtained by identifying one vertex in each of at least two cycles of lengths at least three, with all other cycle vertices distinct. Write \(m_G(\ell)\) for the number of cycles of length \(\ell\) in this one-point bouquet decomposition. In the pure adjacency-and-equality language, without counting quantifiers and with unrestricted quantifier depth, for each integer \(k\ge4\),

\[
G\equiv_{\mathrm{FO}^{k}}H\quad\Longleftrightarrow\quad
\min\{m_G(\ell),k\}=\min\{m_H(\ell),k\}\quad\text{for every }\ell\ge3.
\]

For any fixed finite nonempty set \(L\subseteq\{3,4,\ldots\}\) of allowed cycle lengths, the subfamily with all petal lengths in \(L\) and at least two petals has exactly \((k+1)^{|L|}-|L|-1\) distinct \(\mathrm{FO}^{k}\) theories. Every equivalence class has a unique smallest representative up to isomorphism within \(\mathcal B\), retaining exactly \(\min\{m_G(\ell),k\}\) petals of each length. The hierarchy is strict at every step \(\mathrm{FO}^{k}\subsetneq\mathrm{FO}^{k+1}\), for \(k\ge4\), within \(\mathcal B\).

## Assumptions and scope
All structures are finite simple undirected graphs with equality and a single irreflexive symmetric adjacency relation \(E\). A bouquet has a specified construction from \(r\ge2\) cycles, each \(C_{\ell_i}\) with \(\ell_i\ge3\), identifying one vertex from every cycle and making no other identifications or edges. The identified vertex \(h\) is the unique vertex of degree at least three: its degree is \(2r\ge4\), while every other vertex has degree two. Thus \(h\), the remaining induced components, and their lengths are graph-intrinsic, not extra predicates or constants. Removing \(h\) leaves disjoint paths on \(\ell_i-1\) vertices, whose endpoints are precisely the neighbors of \(h\).

An \(\mathrm{FO}^{k}\) formula may reuse at most \(k\) distinct variable names arbitrarily often; quantifier depth is not bounded. All equivalences are relative to these two graphs, whereas the theory count and minimum representatives are relative to the stated bouquet family.

## Proof
**1. Four-variable recognition of the hub and of path distances.** Let \(U(x)\) express that \(x\) has three pairwise distinct neighbors:
\[
U(x):=\exists y\exists z\exists w\,\bigl(y\ne z\land y\ne w\land z\ne w\land E(x,y)\land E(x,z)\land E(x,w)\bigr).
\]
This uses only four variable names. On every bouquet, \(U\) holds exactly at \(h\). Put \(Q(x):=\neg U(x)\) and \(S(x,y):=Q(x)\land Q(y)\land(x=y\lor E(x,y))\). For each nonnegative integer \(d\), define \(R_d(x,y)\) expressing graph distance at most \(d\) in the subgraph induced by \(Q\): \(R_0(x,y):=Q(x)\land x=y\), \(R_1(x,y):=S(x,y)\), and for \(d\ge2\), choose positive integers \(a,b\) with \(a+b=d\) and set
\[
R_d(x,y):=\exists z\,\bigl(R_a(x,z)\land R_b(z,y)\bigr).
\]
The recursive subformulas may alpha-rename or shadow one of the three variables used by their caller; they have only their two displayed free variables. Therefore each \(R_d\) uses at most three variable names beyond the local four-variable definition of \(U\), and after substitution its total width is at most four. Induction on \(d\) proves that \(R_d\) captures distance at most \(d\) along the disjoint paths after deleting \(h\). In particular, \(R_d\) is false between distinct petal paths for every \(d\).

**2. Four-variable detection of any specified cycle length.** Define \(B(x):=Q(x)\land\exists y\,(U(y)\land E(x,y))\). On bouquets, \(B\) identifies the two endpoints of each path obtained after removing \(h\). Fix any pair of finite bouquets and choose an integer \(N\) not smaller than the maximum number of edges in any of their paths after deleting the hub. For every \(\ell\ge3\), let
\[
\begin{aligned}
P_{\ell,N}(x):=Q(x)\land\exists y\exists z\,[&B(y)\land B(z)\land y\ne z\land R_N(x,y)\land R_N(x,z)\\
&\land R_{\ell-2}(y,z)\land\neg R_{\ell-3}(y,z)].
\end{aligned}
\]
The endpoints of one petal path are at distance exactly \(\ell-2\) precisely when its original cycle has length \(\ell\). The two \(R_N\) conditions ensure that both endpoint witnesses are in the same path as \(x\). As all component diameters are at most \(N\), this formula holds exactly at the non-hub vertices of petals of length \(\ell\) in each of the two graphs. Every inserted subformula has at most two free variables and at most four distinct names after local renaming; the displayed formula uses at most four names overall.

**3. Necessity of the clipped profile.** For any \(\ell\ge3\) and \(1\le t\le k\), there is an \(\mathrm{FO}^{k}\) sentence asserting the existence of at least \(t\) distinct petals of length \(\ell\): choose representatives \(x_1,\ldots,x_t\) satisfying \(P_{\ell,N}(x_i)\), and require \(\neg R_N(x_i,x_j)\) for every \(i<j\). The auxiliary variables in each \(P\) or \(R\) subformula can locally shadow other representative names, so the sentence uses at most \(\max\{4,t\}\le k\) names. Thus if the clipped multiplicities differ at some \(\ell\), choose a threshold \(t\le k\) lying strictly between the two actual counts; this sentence separates the graphs.

**4. Sufficiency by an indefinite pebble strategy.** Suppose all clipped multiplicities agree. In the \(k\)-pebble game, Duplicator always maps hub to hub, and maintains a length-preserving partial matching between the petal paths currently holding pebbles. For each matched pair of paths, she fixes an arbitrary path isomorphism and sends pebbles through it. Whenever Spoiler moves a pebble into an as-yet-unoccupied path of length \(\ell-1\), remove the old position of that pebble first. At most \(k-1\) petal paths then hold pebbles. If fewer than \(k\) petals of length \(\ell\) exist, their multiplicities agree exactly; otherwise each graph has at least \(k\) such petals. In either case a previously unused matching path is available. If an occupied path loses its last pebble, its assignment may be released. This maintains equality and adjacency, including edges to the hub, indefinitely. Therefore the graphs satisfy the same \(\mathrm{FO}^{k}\) sentences at every quantifier depth.

**5. Enumeration, minimization and strictness.** Restrict petal lengths to a finite set \(L\) of size \(s\ge1\). Each multiplicity truncation has \(k+1\) possible values \(0,1,\ldots,k\). Exactly \(1+s\) of the \((k+1)^s\) vectors are inadmissible because they encode zero or exactly one petal. This yields \((k+1)^s-s-1\). For any admissible vector, the graph with exactly the truncated number of petals of each length has \(1+\sum_{\ell\in L}(\ell-1)\min(m_G(\ell),k)\) vertices and is the unique smallest bouquet in its equivalence class. Finally, a bouquet of \(k\) triangles and a bouquet of \(k+1\) triangles have the same width-\(k\) clipped profile but differing width-\((k+1)\) profiles; the hierarchy is strict at every \(k\ge4\).

## Verification
Run `python3 verify_cycle_bouquets.py` using a standard Python 3 interpreter. The standalone finite checker constructs bouquets, recovers their petal lengths by removing their unique high-degree hub, and uses stabilization of non-counting tuple colors (sets of replacement colors, not counting multisets) to compare selected three- and four-variable theories. It checks 95 structural constructions, 13 game comparisons, and 12 direct evaluations of the theory-count formula; the recorded output ends with `ALL_FINITE_CHECKS_PASSED`. These computations are finite corroborations only, and the above proof supplies the unrestricted statement.

## Relationship to prior work
Brown and Hoshino (2007) analyze bounded-round Ehrenfeucht–Fraïssé games for single paths and cycles, not the unrestricted variable-width theories of one-point unions of an arbitrary multiset of cycles. Pikhurko and Verbitsky (2010/2011) survey graph logical width and bounded-treewidth methods, including the different counting-logic setting, without stating the above exact bouquet spectrum. Dawar and Holm (2012) provide a general finite-variable pebble-game framework rather than a class-specific classification. The independent graph-theoretic characterization of cactus graphs and the modular homomorphism-counting dichotomy for cactus targets concern different invariants. In particular, classification of disjoint unions of cycles does not directly classify the glued connected bouquets: the unique hub and paths obtained by removing it must be handled without a named center.

## Limitations
The result is relative to finite simple undirected cycle bouquets having at least two petals and to the pure adjacency language without counting quantifiers. It proves the exact classification for variable widths \(k\ge4\); it makes no claim about the full one-, two-, or three-variable spectra, arbitrary cactus graphs, directed cycles, or enriched signatures. The formulas distinguishing a given graph pair can depend on their maximum finite petal length, so no uniform bounded quantifier-depth claim is made. Finite verification is not an infinite proof. Historical priority remains conditional on uninspected broader decomposition theorems or terminology-based equivalents.

## References
1. J. Brown and R. Hoshino, *The Ehrenfeucht–Fraïssé Game for Paths and Cycles*, Ars Combinatoria 83 (2007), 193–212. https://combinatorialpress.com/ars-articles/volume-083-ars-articles/the-ehrenfeucht-fraisse-game-for-paths-and-cycles/ (publisher gives public date 2007-04-30).
2. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865 (first submitted 2010-03-25), Contemporary Mathematics 558 (2011), 129–179. https://arxiv.org/abs/1003.4865.
3. A. Dawar and B. Holm, *Pebble games with algebraic rules*, arXiv:1205.0913 (first submitted 2012-05-04). https://arxiv.org/abs/1205.0913.
4. A. Göbel, L. A. Goldberg and D. Richerby, *Counting Homomorphisms to Cactus Graphs Modulo 2*, STACS 2014, 350–361. https://doi.org/10.4230/LIPIcs.STACS.2014.350.
