# Induced-cycle canonical implications and factorial direct-basis separation in graphic closures

## Finding
For every finite simple undirected graph \(G=(V,E)\), consider the closure on the **edge set** defined by
\[
\varphi_G(S)=\{uv\in E:\text{the vertices }u,v\text{ are joined by an }S\text{-edge path}\},\qquad S\subseteq E.
\]
The empty path gives no edges. Its Duquenne--Guigues (DG) canonical implication basis is exactly
\[
\boxed{\Sigma_{\mathrm{DG}}(G)=\{E(C)\setminus\{e\}\to\{e\}: C\text{ is a chordless cycle of }G,\ e\in E(C)\}.}
\]
Here *chordless* means that the cycle induces its entire vertex subgraph. In particular, the pseudo-intents are **precisely** these rooted induced-cycle paths, and there are no additional pseudo-intents. No two of the displayed premises coincide with different consequents. Every sound complete nontrivial implication basis, even with multiple conclusions, must contain one implication with each displayed premise and the displayed missing edge in its conclusion. Thus this canonical basis has the minimum possible cardinality, and after removal of redundant conclusion elements it is the unique minimum basis. Its number of rules is
\[
\boxed{b_{\mathrm{DG}}(G)=\sum_{C\text{ chordless cycle}}|E(C)|.}
\]
For one-pass (simultaneous antecedent testing) direct-unit bases, the unique minimum collection of rooted implications instead uses **all simple cycles**, including chorded cycles:
\[
\boxed{\Sigma_{\mathrm{dir}}(G)=\{E(C)\setminus\{e\}\to\{e\}:C\text{ any simple cycle},\ e\in E(C)\}.}
\]
Its minimum cardinality is \(b_{\mathrm{dir}}(G)=\sum_{C\text{ simple cycle}}|E(C)|\). The DG basis is itself one-pass direct **if and only if** every simple cycle of \(G\) is chordless. Moreover \(G\) is chordal if and only if the canonical basis contains only premises of cardinality at most two (forests have no implications).

For the complete graph \(K_n\), \(n\ge3\),
\[
\boxed{b_{\mathrm{DG}}(K_n)=3\binom n3,\qquad b_{\mathrm{dir}}(K_n)=\frac{n!}{2}\sum_{j=0}^{n-3}\frac1{j!}\sim\frac{e}{2}n!.}
\]
Therefore the graph-specific canonical vs one-pass direct gap is factorial versus cubic. For a wheel with rim length \(r\ge4\), the DG basis has exactly \(4r\) implications: the \(r\) triangles and the rim cycle. Its largest premise has \(r-1\) edges.

## Assumptions and scope
All graphs are finite, undirected, simple, possibly disconnected, and have distinct edges. Edge subsets serve as formal attributes; the family of graphically closed edge sets is the extent of a formal context with those closed sets as objects and edges as attributes. The closure is the graphic-matroid closure. A pseudo-intent \(P\subseteq E\) is a nonclosed set such that for every **proper** pseudo-intent \(Q\subsetneq P\), one has \(\varphi_G(Q)\subseteq P\). A sound implication \(A\to B\) has \(B\subseteq\varphi_G(A)\); trivial conclusion elements in \(A\cap B\) are omitted for minimality. A basis is complete if forward chaining computes \(\varphi_G\). Direct means that for every \(S\subseteq E\) the simultaneous one-step closure \(S\cup\bigcup\{B:(A\to B),A\subseteq S\}\) equals \(\varphi_G(S)\). A direct-unit basis has singleton heads.

## Proof
**1. Rooted induced paths are minimal nonclosed sets.** Let \(C\) be an induced cycle and let \(P=E(C)\setminus\{e\}\). Its edges form a path connecting the endpoints of \(e\), so \(e\in\varphi_G(P)\). No other missing edge belongs to \(\varphi_G(P)\), since the only nontrivial connected component of \((V,P)\) is the vertex set of \(C\) and the subgraph induced on those vertices has exactly the cycle edges. Hence \(\varphi_G(P)=P\cup\{e\}\). Every strict subset \(Q\subsetneq P\) is closed: its nontrivial connected components are vertex intervals of the induced cycle, with no additional induced edges in the graph; the omitted edge \(e\) cannot join endpoints of one component. Therefore \(P\) is a pseudo-intent. Distinct induced-cycle rooted paths cannot share the same premise: the unique added edge is determined by \(\varphi_G(P)\setminus P\).

**2. They generate the entire closure.** Let \(S\subseteq E\) and \(e=uv\in\varphi_G(S)\setminus S\). Choose a simple \(u\)-\(v\) path \(P\subseteq S\). The cycle \(P\cup\{e\}\) may contain chords. Prove by induction on \(|P|\) that induced-cycle implications derive \(e\) from \(P\). If the cycle is induced, its rooted rule applies. Otherwise choose a chord \(f\) between two nonconsecutive cycle vertices. In particular either (a) the chord connects vertices of the path \(P\), yielding a strictly shorter subpath of \(P\) whose endpoints are joined by \(f\), or (b) the chord is an edge already accounted for as \(e\), which is excluded by choosing a chord not belonging to the cycle. By the induction hypothesis, \(f\) is derivable from the proper subpath. Replace that subpath by \(f\); the resulting \(u\)-\(v\) walk has length strictly less than \(|P|\), and its simplification is a shorter path, so the induction hypothesis derives \(e\). Thus all edge closures are generated.

**3. No other pseudo-intents.** Let \(P\) be nonclosed. Because the induced-cycle rules generate its closure, a nontrivial induced-cycle rule has premise \(Q\subseteq P\) and its root \(e\notin P\) (consider the first nontrivial forward step from \(P\)). By step 1, \(Q\) is a pseudo-intent. If \(P\) is not itself one of the induced-cycle premises, then \(Q\subsetneq P\), yet \(\varphi_G(Q)\nsubseteq P\). The recursive definition therefore excludes \(P\) from the pseudo-intents. This establishes completeness of the classification and the DG formula.

**4. Minimum and uniqueness.** For any induced-cycle rooted path \(Q\) from step 1, every strict subset of \(Q\) is closed. A sound implication with antecedent properly included in \(Q\) cannot add any edge outside \(Q\). Since the complete closure of \(Q\) adds \(e\), any complete implication system must have at least one rule with antecedent exactly \(Q\) and consequent containing \(e\). Soundness permits no other new edge at \(Q\). Each distinct \(Q\) forces a separate rule. The DG rules meet all these lower bounds simultaneously. At minimum cardinality no other rules exist, and deleting trivial conclusion elements yields the unique displayed collection.

**5. Direct-unit basis.** For every edge \(e\in\varphi_G(S)\setminus S\), some simple path \(P\subseteq S\) connects its endpoints; \(P\cup\{e\}\) is a simple cycle, so the rooted all-cycle rule fires in one simultaneous step. Conversely fix a simple cycle \(C\) and \(e\in E(C)\), and put \(P=E(C)\setminus\{e\}\). In any sound direct-unit basis, a one-pass derivation of \(e\) from \(P\) requires a rule with conclusion \(e\) and antecedent contained in \(P\). If this antecedent is a proper subset of \(P\), its edges do not connect the endpoints of \(e\) because \(P\) is a simple path. Hence soundness forces the antecedent to equal \(P\). This proves all the all-cycle rules are forced. A DG rule can derive \(e\) from \(P\) in one pass only if \(P\) itself is its induced-cycle premise. Thus the DG basis is direct exactly when every simple cycle is induced. An induced cycle of length \(\ell\) yields premises of size \(\ell-1\); the absence of induced cycles of length at least four is the graph-theoretic definition of chordality.

**6. Enumerations.** In \(K_n\), induced cycles are precisely the triangles, yielding three rooted paths each, and simple cycles of length \(\ell\) number \(\binom n\ell(\ell-1)!/2\); each has \(\ell\) roots. Consequently \(b_{\mathrm{dir}}=\frac12\sum_{\ell=3}^n\binom n\ell\ell!=\frac{n!}2\sum_{j=0}^{n-3}1/j!\). In a wheel of rim length at least four the only induced cycles are the rim and the \(r\) hub triangles; the count is \(r+3r=4r\).

## Verification
Execute the standalone file `verify_graphic_horn.py` using standard Python 3. No third-party packages are required. The program constructs graphic closure independently using union-find; it enumerates induced cycles by vertex-degree and connectivity, simple cycle rooted paths by depth-first search, and pseudo-intents directly from their recursive definition. It exhaustively checks all simple graphs on three, four and five vertices, 24 additional seeded six-vertex cases, complete graphs through six vertices, and wheels with rim lengths three through seven. Successful output ends with:

`VERIFY_OK small_graphs 1120 subsets_checked 77117 pseudo_intent_subset_candidates 77117 wheel=3..7 complete=3..6`

This finite verification checks a sizable domain but is not used as an infinite proof. The proof above covers every finite simple graph.

## Relationship to prior work
Kashiwabara and Nakamura (2013) establish the crucial prior statement that for a graphic matroid \(C\setminus\{e\}\) is a **prime stem if and only if** \(C\) is a chordless cycle (p. 3 of the published PDF), and prove that prime stems are pseudo-closed. They also give general conditions under which prime stems furnish optimal canonical bases. Those facts are fully credited and not new. The additional steps here are (i) the exhaustive converse identifying **all** graphic pseudo-intents, (ii) compulsory implication premises and exact uniqueness in the graphic subclass, and (iii) the precise one-pass/direct criterion with its factorial-vs-cubic complete-graph separation. Their displayed theorem does not give these graph-specific conclusions directly. Baixeries and Napoli (2024) compare minimal and direct implication bases in general closure systems, without the graph-cycle characterization or this asymptotic gap. Kahn and Bazin (2018) study basis sizes generally, not this graphic-matroid cycle family. The possibility of an earlier equivalent consequence under different terminology is a residual originality risk.

## Limitations
The theorem concerns graphic-matroid **edge** closure, not ordinary graph geodesic **vertex** convexity, incidence contexts of design blocks, or general matroids. The uniqueness statement is for minimum **number of implications** after standard omission of trivial conclusion elements; it makes no claim about other cost criteria such as total antecedent literals, algorithmic time, or minimum *direct* nonunit rules. The complete-graph example quantifies one-step direct-unit bases, not every conceivable incremental implementation. The mathematical review is not an independent external audit or publication-priority certification.

## References
1. K. Kashiwabara and M. Nakamura, *The prime stems of rooted circuits of closure spaces and minimum implicational bases*, Electronic Journal of Combinatorics 20(1), P22 (2013). DOI: 10.37236/3068. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i1p22/pdf/
2. J. Baixeries and A. Napoli, *A minimal base or a direct base? That is the question!*, arXiv:2404.12229v1 (first public 2024-04-18). https://arxiv.org/abs/2404.12229
3. A. Kahn and A. Bazin, *Average Size of Implicational Bases*, arXiv:1802.04032 (2018). https://arxiv.org/abs/1802.04032
