# The identifying-code polynomial of every two-corona, determined by closed-twin classes

## Finding

Let \(H\) be any finite simple connected graph on \(h\ge 2\) vertices. Obtain its *two-corona* \(G=H\circ_2\) by adjoining a private path \(v-u_v-w_v\) at each vertex \(v\) of \(H\). Two vertices of \(H\) are **closed twins** when their closed neighborhoods in \(H\) are identical. Let their equivalence classes be \(T_1,\ldots,T_c\), with \(t_i=|T_i|\).

An *identifying code* is a set \(C\subseteq V(G)\) for which all traces \(I_C(x)=N_G[x]\cap C\), over \(x\in V(G)\), are nonempty and pairwise distinct. Let its cardinality polynomial be
\[
\mathcal I_G(z)=\sum_{C\text{ identifying}}z^{|C|}.
\]

**Theorem.** For every such \(H\),
\[
\boxed{\displaystyle \mathcal I_{H\circ_2}(z)=z^{2h}\prod_{i=1}^{c}(1+z)^{t_i-1}(z+t_i+1).}
\]

More strongly, \(C\) is identifying if and only if the following three conditions hold simultaneously:

1. Every base vertex \(v\in V(H)\) belongs to \(C\).
2. At least one of \(u_v,w_v\) belongs to \(C\), for every base vertex \(v\).
3. In each closed-twin class \(T_i\), at most one vertex \(v\) has \(w_v\in C\) and \(u_v\notin C\).

In particular, exactly \(\prod_i(t_i+1)\) minimum identifying codes exist, all of cardinality \(2h\). Every cardinality from \(2h\) through \(3h\) occurs. The normalized polynomial is real-rooted: its zeros are \(-1\) with multiplicity \(h-c\) and \(-(t_i+1)\) for each class \(T_i\). Hence the polynomial determines the multiset of closed-twin-class sizes of \(H\). The total number of codes is \(2^{h-c}\prod_i(t_i+2)\).

For a connected core \(H\) with no closed twins (for example, any connected bipartite core of order at least three), the formula specializes to \(z^{2h}(z+2)^h\). For \(H=K_2\), it is \(z^4(z+1)(z+3)\); for \(H=K_3\), it is \(z^6(z+1)^2(z+4)\).

## Assumptions and scope

Graphs are finite, simple, and undirected. The core \(H\) is connected and has at least two vertices; no regularity, bipartiteness, or closed-twin-freeness assumption is imposed on \(H\). The two-corona here means *attaching a path of length two to each base vertex*, not the usual one-step corona product with a two-vertex graph.

All vertices are labeled, and the polynomial counts distinct subsets of the vertex set, not classes modulo automorphisms. An identifying code uses **closed** neighborhoods and requires nonempty traces. The exclusion of a one-vertex core is essential: it would give \(P_3\), whose local trace collisions do not obey the stated connected-core argument.

## Proof

Write \(B=V(H)\). For any code \(C\), the two vertices \(u_v,w_v\) have closed neighborhoods differing exactly by the base vertex \(v\): \(N_G[u_v]\triangle N_G[w_v]=\{v\}\). Consequently, distinguishing their traces forces \(v\in C\). Moreover, the leaf \(w_v\) has closed neighborhood \(\{u_v,w_v\}\), so domination forces \(C\cap\{u_v,w_v\}\ne\varnothing\). Conditions (1) and (2) are necessary.

Assume both conditions and put \(D_v=C\cap\{u_v,w_v\}\). Then \(D_v\ne\varnothing\), and the three kinds of trace are exactly
\[
I_C(w_v)=D_v,\quad I_C(u_v)=\{v\}\cup D_v,\quad
I_C(v)=N_H[v]\cup\bigl(\{u_v\}\text{ if }u_v\in C,\text{ else }\varnothing\bigr).
\]

Every base trace contains at least two base vertices: \(H\) is connected of order at least two, so \(|N_H[v]|\ge2\). Every support trace contains exactly one base vertex, its private \(v\), and every leaf trace contains none. Thus traces belonging to different kinds cannot coincide. Distinct support traces have different base vertices; distinct leaf traces contain disjoint, nonempty private-path sets. Only two distinct *base* traces might coincide.

For distinct \(v,v'\in B\), their base traces coincide exactly when \(N_H[v]=N_H[v']\) and neither \(u_v\) nor \(u_{v'}\) is in \(C\). By condition (2), omission of \(u_v\) is equivalent to taking only \(w_v\) from that private pair. Therefore distinct base traces are guaranteed precisely by condition (3). This proves both necessity and sufficiency of the complete classification, including domination and every pairwise trace comparison.

In one closed-twin class of size \(t\), if no path takes the leaf-only choice, each path offers the choices middle-only (weight \(z\)) or both (weight \(z^2\)), contributing \(z^t(1+z)^t\). If exactly one path takes the leaf-only choice, its position has \(t\) possibilities and the remaining paths independently contribute \(z(1+z)\), giving \(t z^t(1+z)^{t-1}\). The class contribution is therefore
\[
z^t(1+z)^{t-1}(z+t+1).
\]
All \(h\) base vertices are mandatory and contribute \(z^h\). Multiplying the independent class contributions proves the boxed formula.

The minimum exponent is \(2h\), with coefficient \(\prod_i(t_i+1)\); the maximum exponent is \(3h\), with coefficient one. Every factor \((z+t_i+1)\) and every factor \((1+z)\) has a positive constant and positive linear coefficient, so there is no missing intermediate cardinality. The factorization gives the stated root multiset and allows recovering every class size from each non-\(-1\) root \(-(t_i+1)\). Evaluation at \(z=1\) gives \(2^{h-c}\prod_i(t_i+2)\). A connected triangle-free graph of order at least three has no closed-twin pair: adjacent closed twins would have a shared neighbor unless the entire connected graph were \(K_2\). This proves the bipartite specialization.

As an additional exact reliability consequence, if every possible sensor vertex is included independently with probability \(p\), the probability of obtaining an identifying code is \(p^{2h}\prod_i(1+t_i(1-p))\); this follows by weighting the three local states by their Bernoulli probabilities in the same class decomposition.

## Verification

The accompanying standalone `verify.py` builds the graphs and, independently of the theorem, checks every nonempty closed-neighborhood trace directly for every vertex subset. It compares this to the classified local choices and to polynomial coefficients multiplied from the proposed class factors. It exhausts all connected labeled cores of orders two through four and six additional connected cores of orders five and six. Its successful execution reports:

`VERIFY_OK base_graphs=49 direct_subsets=583744 identifying_codes=4805 characterization=PASS full_polynomial=PASS minimum_multiplicities=PASS`

These finite computations are reproducibility checks, **not** the proof for unbounded core order or arbitrary core structure; the proof above is uniform in \(H\).

## Relationship to prior work

Foucaud and Lehtilä, *Revisiting and improving upper bounds for identifying codes* (first arXiv submission April 11, 2022), prove in Proposition 9 that \(\gamma^{\mathrm{ID}}(H\circ_2)=2h\) for every connected core \(H\) of order at least two. They also give explicit constructions and, in Theorem 10, characterize the bipartite graphs attaining their extremal identification-number bound. We **do not** claim the minimum-cardinality value or the two-corona construction as new. The contribution is the necessary-and-sufficient characterization of **all** identifying codes (especially the closed-twin obstruction), the entire cardinality polynomial for arbitrary cores, its minimum-code multiplicity and root-spectrum consequences.

Canoy and Malacas, *Differentiating-Dominating Sets in Graphs Under Binary Operations* (2015), use an ordinary corona operation in which each core vertex is joined to every vertex of a separate factor graph; that differs from attaching a pendant two-edge path. Their differentiating-domination results for the ordinary corona cannot be substituted for the present two-corona statement. Results for identifying-*open* and total dominating identifying codes use different trace or domination requirements.

## Limitations

The counting theorem is limited to the specific two-edge pendant-path construction and connected cores of order at least two. It does not give an enumerator for arbitrary corona products or other lengths of attached paths. The mathematical proof is internal and has not undergone independent expert audit. Although the inspected prior statements do not imply the polynomial, an equivalent result in unindexed or uninspected literature cannot be excluded.

## References

- F. Foucaud and T. Lehtilä, *Revisiting and improving upper bounds for identifying codes*, SIAM J. Discrete Math. 36 (2022), 2619–2634, DOI `10.1137/22M148999X`; arXiv `2204.05250`, v1 publicly posted 2022-04-11; especially Proposition 9 and Theorem 10. Full text: `https://arxiv.org/pdf/2204.05250`.
- S. Canoy and C. Malacas, *Differentiating-Dominating Sets in Graphs Under Binary Operations*, Tamkang Journal of Mathematics 46 (2015), 51–60, DOI `10.5556/j.tkjm.46.2015.1553`; full text `https://pdfs.semanticscholar.org/df42/141bcd8c51dbc977ec62443bfefdb80da10f.pdf`.
