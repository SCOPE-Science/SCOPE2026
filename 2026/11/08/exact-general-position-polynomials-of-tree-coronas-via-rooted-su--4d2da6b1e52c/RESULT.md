# Exact general-position polynomials of tree coronas via rooted-subtree recursions

## Finding
Let \(T\) be any finite tree of order \(n\ge3\). Form its corona \(W(T)=T\circ K_1\) by adding a private leaf \(v'\) adjacent to each \(v\in V(T)\). A set is in general position when no three chosen vertices occur on a common shortest path. Its counting polynomial is \(\psi(W(T);z)=\sum_S z^{|S|}\), summed over all general-position sets, including the empty set.

For a nontrivial connected induced subtree \(H\subseteq T\), let \(\ell(H)\) be its number of degree-one vertices, and put \(h=|V(H)|\). Then
\[
\boxed{\psi(W(T);z)=1+2nz+nz^2+\sum_{\substack{H\subseteq T\\H\text{ connected},\ h\ge2}}(2z)^{\ell(H)}(1+z)^{h-\ell(H)}.}
\]
(The symbol \(H\subseteq T\) means a vertex-induced subtree, each counted once.) The formula is evaluable by an exact rooted-tree recursion. Fix any root and write \(\mathrm{ch}(v)\) for the children of \(v\). In postorder define
\[
Q_v=\prod_{u\in\mathrm{ch}(v)}(1+F_u),\qquad L_v=\sum_{u\in\mathrm{ch}(v)}F_u,
\]
\[
F_v=2z+(1+z)(Q_v-1),\qquad
R_v=2z(1+L_v)+(1+z)(Q_v-1-L_v).
\]
For leaves, the empty product is \(1\), the empty sum is \(0\). Then
\[
\boxed{\psi(W(T);z)=1+nz^2+\sum_{v\in V(T)}R_v.}
\]
This computes every coefficient by polynomial arithmetic in time polynomial in \(n\); naive dense polynomial operations give a conservative \(O(n^4)\) arithmetic-operation bound. In particular, if \(\ell(T)\) is the number of leaves of \(T\), then \([z^n]\psi(W(T);z)=2^{\ell(T)}\), and every highest-cardinality set has size \(n\).

A companion formula applies to every finite simple connected graph \(G\) of order \(n\ge3\). Let \(e_G(U)\) count the vertices \(v\in U\) which do not belong to any geodesic between two other distinct vertices of \(U\). Then
\[
\boxed{\psi(G\circ K_1;z)=nz^2+\sum_{U\subseteq V(G)}2^{e_G(U)}z^{|U|}.}
\]
Consequently \([z^n]\psi(G\circ K_1;z)=2^{s(G)}\), where \(s(G)\) is the number of simplicial vertices of \(G\), and for every \(n\ge3\),
\[
[z^3]\psi(G\circ K_1;z)=4\binom n3+4[z^3]\psi(G;z).
\]

## Assumptions and scope
All graphs are finite, undirected, and simple. Connectedness and \(n\ge3\) are assumed for the graph-corona projection; the tree result assumes \(T\) is a tree of order \(n\ge3\). Every original vertex has exactly one private pendant vertex in the corona. The distance is the ordinary unweighted graph distance. A simplicial vertex is one whose open neighborhood is a clique; degree-one vertices are simplicial. The displayed tree recursion is not claimed to determine whether the resulting coefficient sequence is always unimodal.

## Proof
**1. Projection of general-position sets.** In \(G\circ K_1\), no general-position set can contain \(v,v'\) and a third vertex: the unique pendant edge forces \(v\) onto a geodesic from \(v'\) to every third vertex. The \(n\) forbidden-to-extend pairs \(\{v,v'\}\) themselves are valid and contribute \(nz^2\). Every remaining general-position set chooses at most one representative from each pair. Record the roots with a representative by \(U\subseteq V(G)\). Any triple of distinct chosen roots projects geodesics in the corona to geodesics in the core, because pendant edges merely add fixed endpoint distances. A selected pendant representative is never interior to such a geodesic, whereas a selected core representative \(v\) is interior exactly when \(v\) lies on a core geodesic between two other chosen roots. Thus the roots forbidden from being core representatives are precisely \(U\setminus E_G(U)\), where \(E_G(U)\) is the set of geodesically extreme chosen roots. For each extreme root either representative is permitted independently; for each non-extreme root only its pendant is permitted. There are exactly \(2^{e_G(U)}\) choices. This proves the graph-corona formula, including \(U=\varnothing\) and singleton roots.

**2. Tree hulls.** For a nonempty subset \(U\subseteq V(T)\), let \(H=\operatorname{hull}_T(U)\) be the unique minimal connected subtree spanning \(U\). Its degree-one vertices are all in \(U\). If \(|V(H)|\ge2\), a chosen root \(v\in U\) is geodesically extreme among \(U\) exactly when \(v\) is a leaf of \(H\): a leaf cannot lie between other roots, while for an internal \(v\in U\), minimality gives selected roots in at least two different components of \(H-v\), whose geodesic runs through \(v\). Conversely, fixing a connected subtree \(H\) with \(h\ge2\), the root subsets with hull exactly \(H\) are precisely those containing every leaf of \(H\) and an arbitrary subset of the internal vertices. Every subtree leaf supplies two representative choices (weight \(2z\)); each internal vertex is either absent or represented by its pendant (weight \(1+z\)). The contribution is \((2z)^{\ell(H)}(1+z)^{h-\ell(H)}\). Singleton hulls each contribute \(2z\). Adding the \(nz^2\) same-root pairs and the empty set proves the subtree expansion.

**3. Rooted recursion.** Classify each connected induced subtree by its unique vertex nearest to the chosen root. For a rooted branch whose parent is present, \(F_v\) counts all subtree choices inside the descendants of \(v\) that include \(v\), with each subtree vertex assigned \(2z\) when it has exactly one neighbor in the final subtree (a leaf) and \(1+z\) otherwise. If no child branch is present then \(v\) is a leaf, contributing \(2z\). If at least one child branch is present then \(v\) has degree at least two because its parent is also present, contributing \(1+z\). Hence \(F_v=2z+(1+z)(Q_v-1)\). For a topmost vertex \(v\), zero or one selected child branch makes \(v\) a leaf (or a singleton) and contributes \(2z(1+L_v)\); two or more branches make \(v\) internal and contribute \((1+z)(Q_v-1-L_v)\). Thus \(R_v\) counts the properly weighted nonempty subtree configurations with highest vertex \(v\), including a singleton weighted \(2z\). Summation over \(v\), plus the same-root pairs and the empty set, proves the recurrence. No subtree appears twice.

**4. Extreme coefficients.** A general-position set chooses at most one representative per pair once its cardinality exceeds two, so the maximum size is at most \(n\), attained by the \(n\) pendants. At size \(n\), all roots occur. A vertex of \(G\) fails to be an interior point of any shortest path joining other vertices precisely when its neighborhood is a clique: any two nonadjacent neighbors yield a length-two geodesic via it, while an interior geodesic supplies nonadjacent predecessor and successor. Therefore \(e_G(V(G))=s(G)\). The coefficient \(2^{s(G)}\) follows; for a tree its simplicial vertices are exactly its leaves (as \(n\ge3\)). For three distinct chosen roots, either all three are geodesically extreme, giving weight \(8\), or exactly one lies on a geodesic between the other two, giving weight \(4\). Every size-three root subset that is in general position in \(G\) is in the former case. This proves the cubic identity.

## Verification
The accompanying standalone `verify.py` uses only the Python standard library. It constructs corona graphs and their all-pairs distances from adjacency lists, exhaustively tests the general-position condition for each vertex subset, and separately evaluates the rooted-subtree recurrence. It checks **all labeled trees** of orders \(3,4,5\), five additional larger tree instances, and four non-tree graphs using the independent graph-corona root-projection formula and simplicial leading coefficient. The executed result is:

`VERIFY_OK graph_cases=153 enumerated_vertex_subsets=293568 tree_corona_recurrence=PASS root_projection=PASS top_simplicial=PASS`

Run `python3 verify.py`. Exact integer arithmetic is used throughout. Exhaustive finite checks corroborate the proof but do not establish the unrestricted infinite statements; those depend on Steps 1–4.

## Relationship to prior work
Iršič, Klavžar, Rus, and Tuite (2024), *General Position Polynomials*, defined the invariant and determined the corona-of-a-path case (the comb), and raised a corona-unimodality question. These established results are not claimed as new. Rather (2026), *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, examined further classes and corona-unimodality phenomena. Wang (2026), *A Complete Multipartite Counterexample to Corona-Unimodality of General Position Polynomials*, gave specialized formulas for complete-multipartite coronas and counterexamples; these do not provide an arbitrary-tree subtree recurrence. The published result *Strict log-concavity for complete-graph coronas* covers the special case of a complete core and is not presented as new. The present result counts all general-position sets of every tree corona with a local polynomial recursion and determines the leading coefficient for every connected core.

## Limitations
The theorem assumes one leaf attached to each original vertex and is not extended to longer or unequal pendant paths. The recurrence counts sets but does not settle unimodality, log-concavity, or real-rootedness for all tree coronas. An equivalent recurrence outside the inspected literature may exist; publication priority is not independently certified. The software checks finite cases only; no independent mathematical audit has been performed.

## References
1. V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, Results in Mathematics 79 (2024), Article 110, arXiv:2401.05696 (first public 11 January 2024), https://arxiv.org/abs/2401.05696, https://doi.org/10.1007/s00025-024-02133-3.
2. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials* (2026), arXiv:2603.06930, https://arxiv.org/abs/2603.06930.
3. X. Wang, *A Complete Multipartite Counterexample to Corona-Unimodality of General Position Polynomials* (2026), publicly accessible research manuscript, https://www.researchgate.net/publication/405328607_A_Complete_Multipartite_Counterexample_to_Corona-Unimodality_of_General_Position_Polynomials.
4. *Strict log-concavity for complete-graph coronas*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-strict-log-concavity-for-complete-graph-coronas--cc76f1cb7642.
