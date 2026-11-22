# A rank-three ceiling and a sharp five-path criterion for linear-forest extension ranks

## Finding

Let \(\mathcal{F}\) be the hereditary class of all finite simple undirected **linear forests**: every connected component is a path, and isolated vertices are permitted. In the exact one-point-extension rank of \(\mathcal{F}\), every finite or countable host \(X\in\sigma\mathcal{F}\) has rank at most three. Its rank is determined as follows:

\[
\operatorname{rk}(X)=
\begin{cases}
0,&X=\varnothing,\\
1,&X\ne\varnothing\text{ and either }|X|=2\text{ with an edge, or }X\text{ is edgeless, or }|X|=1,\\
2,&\text{there is an edge and }|X|\ge3\text{ but not the condition below},\\
3,&|X|\ge6\text{ and }X\text{ contains a five-vertex path}.
\end{cases}
\]

Precisely, \(\operatorname{rk}(X)\ge1\) exactly when \(X\ne\varnothing\); \(\operatorname{rk}(X)\ge2\) exactly when \(X\) has an edge and at least three vertices; and \(\operatorname{rk}(X)\ge3\) exactly when \(X\) has at least six vertices and a copy of the five-vertex path \(P_5\). Here every path is induced, because the host is a linear forest.

At the first feasible order six, exactly two isomorphism types have rank three: \(P_6\) and \(P_5\sqcup P_1\). For every order \(n\ge6\), the minimum edge number is four, attained uniquely up to isomorphism by \(P_5\sqcup(n-5)P_1\).

Writing \(R_n\) for the number of labelled rank-three linear forests on a fixed \(n\)-element vertex set, we obtain, for every \(n\ge6\),
\[
R_n=n!\,[z^n]\left[\exp\!\left(z+\frac{z^2}{2(1-z)}\right)
-\exp\!\left(z+\frac{z^2+z^3+z^4}{2}\right)\right].
\]
In particular, for a uniformly random labelled linear forest on \(n\) vertices, the exceptional probability of rank at most two satisfies
\[
\log\Pr\bigl(\operatorname{rk}(X)\le2\bigr)
=-\tfrac14 n\log n+O(n)\qquad(n\longrightarrow\infty).
\]
Thus almost all labelled linear forests have the maximal rank three, while the event of not containing a sufficiently long component is superexponentially rare.

## Assumptions and scope

The language consists solely of one symmetric irreflexive adjacency relation. Embeddings are induced embeddings. We permit \(X\) to be finite, empty, or countably infinite, provided every finite induced subgraph of \(X\) is a linear forest. The rank depends on the **specified hereditary class** \(\mathcal{F}\), not on the full class of graphs.

For a finite induced marked subgraph \(A\subseteq X\), define \(\operatorname{rk}_X(A)\ge0\). For each integer \(t\ge0\), define \(\operatorname{rk}_X(A)\ge t+1\) if, for **every** one-vertex abstract induced extension \(B\in\mathcal{F}\) of \(A\) (up to isomorphism fixing \(A\)), some realization \(A\cup\{v\}\subseteq X\) of \(B\) satisfies \(\operatorname{rk}_X(A\cup\{v\})\ge t\). Write \(\operatorname{rk}(X)=\operatorname{rk}_X(\varnothing)\). This is the finite-level restriction of the ordinal rank studied by López-Callejas and Navarro-Castillo; the proof below rules out level four even for countably infinite hosts.

For \(n\ge6\), the probability statement samples uniformly from all labelled linear forests on the fixed vertex set \(\{1,\ldots,n\}\). The finite-class restriction on allowed one-point extensions is essential.

## Proof

**1. Every independent marked triple has rank zero.** Let \(a,b,c\) be independent vertices in any linear-forest host. For each pair among \(\{a,b,c\}\), an abstract new vertex adjacent to precisely that pair, and not to the remaining vertex, is legal in \(\mathcal{F}\): it makes the path \(P_3\) plus an isolated vertex. If the triple had rank at least one, all three pair-neighbour types would be represented within \(X\). Hence \(a,b,c\) would be pairwise at graph distance two. But on each path, distance-two adjacency joins positions of the same parity and gives two disjoint (possibly finite or infinite) paths. It has no triangle. Vertices in different components have infinite distance. Therefore three vertices cannot be pairwise at distance two, a contradiction.

**2. The universal rank-three ceiling.** Every pair \(\{a,b\}\) of distinct nonadjacent marked vertices has the legal one-point extension of adjacency pattern \(00\): a new vertex isolated from both. This produces an independent triple. By Step 1, no realization of that extension has rank one. Thus no nonadjacent marked pair has rank at least two. In turn, the nonadjacent one-point extension of any marked singleton is legal, so no marked singleton has rank at least three. The unique one-vertex extension of the empty structure then shows \(\operatorname{rk}(X)\not\ge4\) for every host, including countably infinite hosts.

**3. Levels zero, one, and two.** The empty host realizes no one-point extension, while each nonempty host does; hence rank at least one is equivalent to nonemptiness. For a singleton \(\{u\}\), the two legal extensions attach either a neighbour or a nonneighbour. Therefore \(\operatorname{rk}(X)\ge2\) iff some vertex has at least one neighbour and at least one distinct nonneighbour. This requires an edge and at least three vertices. Conversely, if the host contains an edge and at least three vertices, an endpoint of an edge-component has a nonneighbour elsewhere, while an endpoint of a longer path has a nonneighbour at distance two. Such a vertex supplies the two extensions, proving the equivalence.

**4. The five-path obstruction is necessary for rank three.** If \(\operatorname{rk}(X)\ge3\), some marked singleton \(\{u\}\) has rank at least two. Applying its legal nonadjacent extension yields a distinct nonneighbour \(v\) such that \(\operatorname{rk}_X(\{u,v\})\ge1\). Because \(u,v\) are nonadjacent, all four abstract adjacency patterns \(00,10,01,11\) to \(\{u,v\}\) belong to \(\mathcal{F}\). Hence there are distinct outside witnesses for all four. The \(11\) witness is a common neighbour \(w\) of \(u,v\), and the \(10\) and \(01\) witnesses give additional neighbours \(x\) of \(u\) and \(y\) of \(v\). The vertices \(x,u,w,v,y\) form an induced \(P_5\), because the host is a linear forest. The \(00\) witness is a sixth, distinct vertex, so \(|X|\ge6\).

**5. The obstruction is sufficient.** Suppose \(x_0-x_1-x_2-x_3-x_4\) is an induced five-vertex path in \(X\), with some sixth vertex \(z\) outside it. Take the marked singleton \(\{x_1\}\). For the adjacent pair \(\{x_1,x_2\}\), the only legal new-point adjacency patterns within a linear forest are \(00,10,01\): the pattern \(11\) would close a triangle. These three patterns are witnessed by \(x_4,x_0,x_3\), respectively, so the pair has rank at least one. For the nonadjacent pair \(\{x_1,x_3\}\), all four patterns \(00,10,01,11\) are legal and are realized by \(z,x_0,x_4,x_2\), respectively. Indeed, \(x_1\) and \(x_3\) already have their two incident path edges and so cannot be adjacent to \(z\). This pair also has rank at least one. Thus the singleton has rank at least two and the empty structure has rank at least three. Together with Step 2 this proves the entire classification.

**6. Smallest witnesses and edge sharpness.** A five-vertex path uses four edges, and a rank-three host needs at least one more vertex. At six vertices the only possible component partitions containing a five-vertex path are \((6)\) and \((5,1)\), giving \(P_6\) and \(P_5\sqcup P_1\). At any \(n\ge6\), precisely four edges force that \(P_5\) is the sole nontrivial component, yielding the unique minimum-edge type.

**7. Exact labelled census.** On a specified \(k\)-element labelled vertex set, there is one path if \(k=1\) and \(k!/2\) undirected paths if \(k\ge2\). The labelled exponential formula therefore gives
\[
A(z)=\exp\!\left(z+\sum_{k\ge2}\frac{z^k}{2}\right)
=\exp\!\left(z+\frac{z^2}{2(1-z)}\right)
\]
for all linear forests and
\[
B(z)=\exp\!\left(z+\frac{z^2+z^3+z^4}{2}\right)
\]
for forests without a path component of size at least five. For \(n\ge6\), the classification identifies rank three precisely with the set difference, so \(R_n=n![z^n](A(z)-B(z))\). At size five the difference counts \(P_5\) but its rank is only two; that exceptional boundary is why the formula explicitly assumes \(n\ge6\).

**8. Rarity exponent.** Write \(a_n=[z^n]A(z)\) and \(b_n=[z^n]B(z)\). For \(n\ge2\), the single \(P_n\) component gives \(a_n\ge1/2\). Positivity and the Cauchy coefficient bound at \(r=1-n^{-1/2}\) give \(a_n\le A(r)r^{-n}=\exp(O(\sqrt n))\), so \(\log a_n=O(\sqrt n)\). Since \(B\) is entire with nonnegative coefficients, choosing \(r=n^{1/4}\) gives
\[
\log b_n\le\log B(n^{1/4})-\tfrac n4\log n
=-\tfrac n4\log n+O(n).
\]
For the reverse bound, write \(n=4m+s\), with \(0\le s<4\). A forest of \(m\) four-vertex paths and, for \(s>0\), one additional path on \(s\) vertices contributes at least \(c_s/(2^m m!)\) to \(b_n\), where \(c_s>0\) is an absolute constant. Stirling's formula gives \(\log b_n\ge-\tfrac n4\log n-O(n)\). For \(n\ge6\), \(\Pr(\operatorname{rk}(X)\le2)=b_n/a_n\), proving the claimed asymptotic logarithm.

## Verification

The included standalone `verify.py` uses Python 3 standard library only. Run `python verify.py` in the directory containing the extracted artifact. It first enumerates all 373 unlabelled component-size partitions through order thirteen and directly checks all abstract legal one-point extension masks for marked pairs. It also implements a second generic recursive rank predicate, comparing rank-three and rank-four outcomes over the 138 nonempty forest types through order ten. Both independent implementations agree with the proved criterion. The program separately computes the two exponential generating functions as exact rational coefficients and matches the labelled counts through order thirteen.

The output includes \(R_6=720\), \(R_7=7560\), \(R_8=84000\), \(R_9=1013040\), and ends with `ALL_CHECKS_OK`. The enumerations are finite corroboration only. The all-size and countably infinite rank assertions follow from Steps 1–6; the asymptotic follows analytically from Step 8, not from extrapolated data.

## Relationship to prior work

López-Callejas and Navarro-Castillo (arXiv:2604.14461v1) develop this exact one-point-extension rank for hereditary classes, establish rank unboundedness in the full graph class, and give ranks for finite and countable linear orders. Their full paper's sections on the rank, graphs, and open questions do not treat linear forests or give the finite ceiling or five-path obstruction above. The full-graph rank is not an upper bound in the restricted class: each induced-extension game uses the extensions *legal in its own hereditary age*. In particular, a triangle-extension pattern is legal for an adjacent pair in the full graph class but forbidden in the linear-forest class.

The published result “The 160 rank-three theories of finite linear forests and a sharp 23-vertex kernel” studies **ordinary first-order quantifier-rank-three equivalence**, using a three-round two-structure Ehrenfeucht–Fraïssé game. That is not the single-host one-point-extension rank here, and its 160 logical classes and 23-vertex representative bound neither imply the uniform rank-three ceiling nor yield the present path criterion. “Sharp rank-three onset and six-edge extremum for finite graphs” does compute one-point-extension rank, but in the full graph class; its seven-vertex six-edge threshold refers to a different family of permitted prime extensions and thus does not dominate the six-vertex four-edge phenomenon for linear forests. Both full public texts were inspected for this distinction.

The formula for labelled paths and the exponential formula for sets of components are standard enumeration tools; their use alone is not claimed as new. The claimed contribution is the structural extension-rank classification, with the exact and asymptotic censuses as consequences.

## Limitations

The classification depends on the hereditary age being **linear forests**. A given forest's rank may change if one instead allows arbitrary graph extensions. No claim is made for general forests with branching, cyclic maximum-degree-two graphs, directed paths, ordinary first-order quantifier rank, or the rank of a different extension system. Prior-art comparison used the cited full texts and meaning-based searches; unindexed earlier treatments or equivalent folklore may still exist. Independent mathematical audit is not claimed. The checker covers the stated finite ranges only.

## References

1. Carlos López-Callejas and Jareb Navarro-Castillo, “A rank function for Fraïssé classes and the rank property,” arXiv:2604.14461v1, first public 2026-04-15. https://arxiv.org/html/2604.14461v1
2. “The 160 rank-three theories of finite linear forests and a sharp 23-vertex kernel,” public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-160-rank-three-theories-of-finite-linear-forests-and-a-sharp--0afd59949e71
3. “Sharp rank-three onset and six-edge extremum for finite graphs,” public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-rank-three-onset-and-six-edge-extremum-for-finite-graphs--a3c35b6162f1
