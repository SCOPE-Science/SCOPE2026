# Two and three variables completely classify finite marked Cayley digraphs

## Finding
Fix an integer \(d\ge1\). A finite \(d\)-marked group is a finite group \(G\) with an ordered generating tuple \((g_1,\ldots,g_d)\). Repetitions, inverse coincidences and identity entries are allowed. Its directed, edge-coloured relational Cayley structure \(\mathcal C(G)\) has domain \(G\) and binary predicates \(R_i(x,y)\) interpreted by \(y=xg_i\). The language has equality but no constants, functions or counting quantifiers.

Form the ordered list of signed marked elements \(E_G=(1,g_1,\ldots,g_d,g_1^{-1},\ldots,g_d^{-1})\). Let \(\pi_G\) be its equality partition (retaining the positions in the list), and let \(\eta_G\) be true precisely when some group element is absent from the list. For any two finite \(d\)-marked groups \(G,H\):

\[
\mathcal C(G)\equiv_{\mathrm{FO}^{2}}\mathcal C(H)
\quad\Longleftrightarrow\quad (\pi_G,\eta_G)=(\pi_H,\eta_H).
\]

At the next variable width there is complete rigidity:
\[
\mathcal C(G)\equiv_{\mathrm{FO}^{3}}\mathcal C(H)
\quad\Longleftrightarrow\quad
(G;g_1,\ldots,g_d)\cong(H;h_1,\ldots,h_d).
\]
Both equivalences allow **unrestricted quantifier depth**. Moreover, if the marked groups are not isomorphic and \(m=\min(|G|,|H|)\), a distinguishing \(\mathrm{FO}^{3}\) sentence exists with quantifier rank at most
\[
1+\lceil\log_2(2D+1)\rceil\le1+\lceil\log_2(2m-1)\rceil,
\]
where \(D\) is the undirected signed-generator Cayley diameter of whichever group has order \(m\). Conversely, the logarithmic rank order cannot be improved uniformly: for every integer \(r\ge0\), the one-generator cyclic Cayley structures of orders \(2^{r+1}\) and \(2^{r+1}+1\) (for \(r\ge1\)) satisfy the same \(\mathrm{FO}^{3}\) sentences of quantifier rank at most \(r\), but their full \(\mathrm{FO}^{3}\) theories differ. The lower-bound assertion also holds whenever both cyclic orders are at least \(2^{r+1}\).

The width jump is already present at the same cardinality: \(S_3\) marked by a transposition and a three-cycle, and \(C_6\) marked by elements of respective orders two and three, have identical \(\mathrm{FO}^{2}\) theories but different \(\mathrm{FO}^{3}\) theories.

## Assumptions and scope
A signed word may use each generator or its formal inverse. The marked tuple is required to generate its group, making each Cayley structure connected when edges may be traversed backwards. Relations are **labelled by position**: an isomorphism must preserve each predicate \(R_i\), even if distinct labels happen to define identical relations. Every group considered is finite and nonempty. The logic is ordinary first-order logic with at most two or three reusable variable names, equality and the binary predicates \(R_i\); quantification is unrestricted in depth unless an explicit rank is stated.

For a signed word \(w\) of length \(L\ge1\), let \(P_w(x,y)\) express that following the prescribed signed-colour walk from \(x\) arrives at \(y\). Its atomic clauses are \(R_i(x,y)\) for a positive letter and \(R_i(y,x)\) for a negative letter. For a decomposition \(w=uv\) into two nearly equal nonempty pieces, use
\[
P_w(x,y):=\exists z\bigl(P_u(x,z)\land P_v(z,y)\bigr).
\]
At every recursive stage reuse one of exactly three variable names, alpha-renaming locally so that the two free endpoint names and their temporary third name are correctly scoped. The resulting relation has quantifier rank at most \(\lceil\log_2 L\rceil\). For the empty word the path predicate is \(x=y\).

## Proof
**1. Two-variable classification.** For any fixed vertex \(a\), the complete atomic two-variable type of \((a,b)\) is determined solely by whether \(a=b\), \(b=ag_i\), or \(b=ag_i^{-1}\), for the various labels \(i\). Different labels can coincide, which is recorded in \(\pi_G\). Every signed-list equality class is realized by one \(b\); in addition the otherwise unconstrained generic type occurs exactly when \(\eta_G\) is true. Left multiplication makes these type lists the same at every \(a\). When the pairs of invariants agree, Duplicator permanently matches every two-pebble move by choosing a vertex of the corresponding type over the one stationary pebble. This preserves all atomic formulas, including loops, reversals and equality, at every round.

Conversely, the one- or two-variable sentences \(\exists x R_i(x,x)\), \(\exists x\exists y(R_i(x,y)\land R_j(x,y))\), \(\exists x\exists y(R_i(x,y)\land R_j(y,x))\), together with the analogous diagonal tests and equality, detect every coincidence among signed positions and the identity. The sentence
\[
\exists x\exists y\left(x\ne y\land\bigwedge_{i=1}^{d}\neg R_i(x,y)\land\neg R_i(y,x)\right)
\]
detects \(\eta_G\). Thus unequal invariant pairs are distinguishable with two variables.

**2. Three-variable rigidity.** The balanced path formula above gives a three-variable sentence \(\exists x\,P_w(x,x)\) of rank at most \(1+\lceil\log_2 |w|\rceil\). It is true in a marked Cayley structure exactly when \(w\) evaluates to the group identity (evaluation is independent of the chosen starting vertex). If two structures have the same three-variable theory, every signed word is a relation in the first marked group if and only if it is a relation in the second. Their common free-group kernel therefore yields the same quotient of the free group on \(d\) generators, hence a marked isomorphism. Conversely a marked isomorphism induces an isomorphism preserving every binary relation, and hence every first-order sentence.

**3. Explicit logarithmic upper rank.** Let \(A\) be the smaller of two nonisomorphic marked groups and \(B\) the other, so \(|A|\le|B|\). Fix for each \(a\in A\) a signed word \(p_a\) of length at most \(D\) representing \(a\), with \(p_1\) empty. For each \(a\) and each signed generator letter \(s\), the word
\[
w_{a,s}=p_as\,p_{as}^{-1}
\]
is an identity relation in \(A\) of length at most \(2D+1\). Suppose every such relation held in \(B\). Then the assignment \(f(a)=p_a(B)\) preserves each signed-generator transition \(f(as)=f(a)s(B)\), beginning at the identity. By following any signed word, \(f\) is a surjective marked homomorphism \(A\to B\); because \(|A|\le|B|\), it must be an isomorphism, a contradiction. Thus one of these words distinguishes, and its balanced path sentence has the advertised rank. A connected graph on \(m\) vertices has diameter at most \(m-1\), proving the second inequality.

**4. Logarithmic lower-rank obstruction.** Write \(C_N\) for the relational structure with one directed successor cycle of length \(N\). In the \(r\)-round three-pebble game on \(C_N,C_M\), with \(N,M\ge2^{r+1}\), Duplicator maintains the circular order of distinct occupied positions and, for every directed gap between successive occupied positions, the following invariant at \(t\) rounds remaining: if the gap length is less than \(T_t=2^{t+1}\), its exact length is the same on both cycles; otherwise both gap lengths are at least \(T_t\). With fewer than two occupied positions, regard the unique cyclic gap as the whole circumference. Equality is preserved separately. This holds initially. Removing a moved pebble merges two gaps, preserving the invariant because the sum of two exactly matched small lengths stays equal, while a sum with a long term stays long. There are at most two stationary points after a move; they split the circle into at most two arcs. If a new pebble is placed in a short arc, copy its exact offset. In a long arc, a split with one new short part can be copied exactly while leaving the other part long, and when both parts are long choose the new point so that both are at least \(T_{t-1}\), possible because each original long arc has length at least \(2T_{t-1}\). At \(t=0\), gap lengths one (adjacent successors) are exactly matched and equality is preserved, so atomic diagrams agree. Induction proves Duplicator's win. Nonisomorphic cycles have different word identities, and are distinguished at some larger rank by part 2. This proves the logarithmic-order lower bound.

**5. Equal-size separation.** In \(S_3\), take a transposition \(s\) and a three-cycle \(t\). In \(C_6\), take the unique involution and any element of order three. In each case the signed list contains identity, a self-inverse nonidentity element, two distinct nonidentity mutually inverse order-three elements; the remaining two group elements form a generic class. Thus \((\pi,\eta)\) agrees. But the word \(sts^{-1}t^{-1}\) is nontrivial in \(S_3\) and trivial in \(C_6\). Parts 1–2 give the claimed sharp width distinction.

## Verification
Run \(\texttt{python3 verify.py}\) from a directory containing the supplied standalone checker. It uses only the Python standard library and finishes with \(\texttt{VERIFY_OK}\). It checks signed-list profiles for cyclic groups of orders 1–15, the equal-order \(S_3/C_6\) example, 253 unequal cyclic-group pairs against the short-relation bound, and exact counting-free pebble refinement for eight pairs at widths two and three. These are finite consistency checks only; the indefinite game and arbitrary-group claims are proved above rather than inferred from the experiment.

## Relationship to prior work
Kuske and Lohrey studied decidability of first-order theories of Cayley graphs and the relationship with group word problems (STACS 2003, DOI 10.1007/3-540-36494-3_41; APAL 2005, DOI 10.1016/j.apal.2004.06.002). Their accessible abstracts assert decidability equivalences, not the exact two-variable signed-type classification, the three-variable rigidity threshold, or the diameter-sensitive logarithmic rank bound. The complete texts of their most directly related works were not available for comparison; priority therefore remains provisional. Grohe and Otto's open 2012 paper develops the finite-variable pebble-game framework, including counting-free games, but not this marked-Cayley specialization. Published findings on prime cyclic groups in relational *multiplication* languages and one-generator permutation structures have different signatures or narrower scopes and do not by themselves imply the general marked multi-generator result.

## Limitations
The conclusions depend on every directed generator edge having its own named binary predicate and on the generators spanning the group. They are not assertions about uncoloured, undirected, unlabeled or possibly disconnected Cayley graphs, nor about group multiplication written as a ternary relation. No optimal constant for the rank bound is asserted; only its logarithmic growth order is shown sharp. The complete 2002 Kuske–Lohrey technical report and its 2005 expanded article were not inspected in full, so unrecognized historical coverage remains a substantial originality risk. Independent review has not been performed.

## References
1. D. Kuske and M. Lohrey, *Decidable Theories of Cayley-Graphs*, STACS 2003, LNCS 2607, pp. 463–474, DOI 10.1007/3-540-36494-3_41, https://link.springer.com/chapter/10.1007/3-540-36494-3_41 (publisher records first online 2003-01-01; cites an earlier 2002 technical report without day-level date evidence).
2. D. Kuske and M. Lohrey, *Logical aspects of Cayley-graphs: the group case*, Annals of Pure and Applied Logic 131 (2005), pp. 263–286, DOI 10.1016/j.apal.2004.06.002, https://doi.org/10.1016/j.apal.2004.06.002.
3. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, CSL 2012, LIPIcs 16, pp. 289–316, DOI 10.4230/LIPIcs.CSL.2012.289, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2012.289.
