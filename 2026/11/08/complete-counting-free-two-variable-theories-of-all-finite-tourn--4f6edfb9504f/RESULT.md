# Complete counting-free two-variable theories of all finite tournaments

## Finding
Let \(E(u,v)\) mean that \(u\) beats \(v\) in a nonempty finite loopless tournament \(T\). Work in first-order logic with equality and this single directed-edge predicate, at most two reusable variable names and no counting quantifiers, with *no restriction on quantifier depth*. There is an exact classification of \(\mathrm{FO}^{2}\)-equivalence across **all** finite tournaments.

Repeatedly delete a vertex that beats every other remaining vertex (a **source**), until no source remains; let \(h(T)\) be the number deleted. If the tournament becomes empty, then \(T\) is transitive and we assign it the invariant \((\mathrm{transitive},|T|)\). Otherwise, repeatedly delete from the residue a vertex beaten by all other remaining vertices (a **sink**), until no sink remains; let \(t(T)\) be the number deleted. The final nonempty **core** has neither a source nor a sink. Assign \(T\) the invariant \((\mathrm{nontransitive},h(T),t(T))\). These deletions and their counts are unambiguous.

**Classification.** For any two nonempty finite tournaments \(T,U\),
\[
T\equiv_{\mathrm{FO}^{2}}U\quad\Longleftrightarrow\quad \operatorname{inv}(T)=\operatorname{inv}(U).
\]
In particular, any two source-free, sink-free finite tournaments of order at least three have the same \(\mathrm{FO}^{2}\) theory; no information about the interior core, including its size or strongly connected decomposition, survives.

**Exact spectrum at fixed order.** For every \(n\ge1\), the number of distinct \(\mathrm{FO}^{2}\) theories realized by tournaments with exactly \(n\) vertices is
\[
1+\binom{n-1}{2},
\]
where the binomial coefficient is zero when \(n<3\). A transitive tournament is the unique canonical minimal representative for its theory. The unique smallest representative of the nontransitive theory \((h,t)\), up to isomorphism, is an ordered sum of a transitive tournament on \(h\) vertices, a directed triangle, and a transitive tournament on \(t\) vertices, all arcs pointing from earlier to later summands; its order is \(h+t+3\).

## Assumptions and scope
A tournament is a finite nonempty set with an irreflexive directed relation \(E\) such that for distinct vertices exactly one of \(E(u,v)\) and \(E(v,u)\) holds. Its source is a vertex with an outgoing arc to every other vertex, and its sink has incoming arcs from every other vertex. There is at most one source and at most one sink in any nonempty tournament. The two-variable fragment permits arbitrary nesting and reuse of two variable names \(x,y\), but no additional variables, constants, counting quantifiers, or parameters. Logical equivalence means agreement on every *sentence* in this fragment, not just a fixed quantifier-rank prefix. The core and the numbers \(h,t\) are the full invariant only for nontransitive tournaments.

## Proof
**1. Canonical peeling.** A source, when present, is unique; removing successive sources therefore gives a uniquely defined initial chain \(s_1,\ldots,s_h\), where each earlier vertex beats every later one. The remainder has no source. If it is empty, the original tournament is transitive. Conversely, every finite transitive tournament is successively exhausted by source deletion. If a source-free tournament contains a sink, deleting that sink cannot create a source: every other vertex beat the sink already, so removing the sink eliminates none of their incoming arcs. After successive sink deletions, therefore, the residue remains source-free. It cannot be empty, because a nonempty source-free tournament has at least three vertices, and removing sinks cannot create a source. The final residue \(K\) has no source and no sink, and at least three vertices. The sink sequence is also uniquely determined, in the reverse order; a source never contributes an outgoing arc from another vertex, so deleting sources does not change which sinks can be successively removed. Thus the nontransitive decomposition is canonical:
\[
T\cong L_h\ \longrightarrow\ K\ \longrightarrow\ L_t,
\]
where \(L_r\) is the transitive tournament on \(r\) vertices (possibly empty), every vertex in one displayed term beats every vertex in a later term, and \(K\) has neither source nor sink. In particular, every \(v\in K\) has both an incoming and an outgoing neighbor *within* \(K\).

**2. The source and sink positions are definable with two variables.** Set
\[
\sigma_1(x):=\forall y\bigl(y=x\lor E(x,y)\bigr)
\]
and recursively, for \(r\ge1\),
\[
\sigma_{r+1}(x):=\neg\bigvee_{i=1}^{r}\sigma_i(x)\ \land\
\forall y\left(y=x\lor\bigvee_{i=1}^{r}\sigma_i(y)\lor E(x,y)\right).
\]
Each displayed formula uses only the two names \(x,y\): within the substituted subformulas \(\sigma_i(y)\), the auxiliary quantified name is \(x\), with ordinary lexical scope. Inductively, \(\sigma_r\) holds at exactly the \(r\)-th vertex removed by source peeling if one exists, and nowhere otherwise. The analogous formulas \(\theta_r\), obtained by reversing every directed edge in the recursion, identify the successive sink positions. Consequently, nontransitive tournaments with different source-peeling counts are distinguished by \(\exists x\,\sigma_j(x)\), and those with the same source count but different sink counts by \(\exists x\,\theta_j(x)\), for the first index where existence differs.

A transitive tournament of order \(n\) satisfies the two-variable sentence
\[
\left(\exists x\,\sigma_n(x)\right)\ \land\
\forall x\left(\bigvee_{i=1}^{n}\sigma_i(x)\right).
\]
No other tournament satisfies it: the first conjunct forces at least \(n\) successive sources, and the second forces every vertex to be among those first \(n\) sources. Thus different transitive orders and every transitive/nontransitive pair are distinguished.

**3. Permanent two-pebble strategy.** Consider two nontransitive tournaments with identical \(h,t\). In a two-pebble Ehrenfeucht game, Duplicator always responds to any source-chain vertex with the corresponding vertex at the same source position, and analogously for a sink-chain vertex. She responds to every core vertex with a core vertex. These choices preserve all arcs involving head or tail vertices, since their arcs to each other and to the core are fixed by the ordered-sum construction. When the other pebble is already in the core, and Spoiler moves to a core vertex, Duplicator copies equality if Spoiler reused that vertex; otherwise, she chooses within her core an in-neighbor or out-neighbor of the stationary core pebble according to the required arc direction. Both sorts of neighbor exist because her core has neither a source nor a sink. If no stationary pebble lies in the core, she may choose any core vertex. This maintains equality and both directions of the edge predicate after every move, from either structure, indefinitely. Hence Duplicator wins at every finite game length and the two tournaments satisfy exactly the same \(\mathrm{FO}^{2}\) sentences. Transitive tournaments of the same order are isomorphic. Combining this with step 2 proves the equivalence classification.

**4. Spectrum and minimum representatives.** At order \(n\), one theory comes from the transitive tournament. For a nontransitive tournament the core has at least three vertices, so \(h,t\ge0\) and \(h+t\le n-3\). Every such pair actually occurs: for any \(r\ge3\), take a directed three-cycle and substitute transitive tournaments of sizes \(r-2,1,1\) for its vertices. The resulting \(r\)-vertex core has neither source nor sink; attach transitive head and tail chains of sizes \(h,t\). Thus the number of nontransitive theories at order \(n\) is \(\sum_{j=0}^{n-3}(j+1)=\binom{n-1}{2}\). Every representative of \((h,t)\) needs at least \(h+t+3\) vertices, and equality forces the core to be a directed triangle, unique up to isomorphism. For transitive theories the order is already a complete invariant, so their minimum representatives are unique as well. \(\square\)

## Verification
Two independent standalone Python 3 scripts accompany this text. `verify_tournament_fo2.py` implements simultaneous finite two-variable unary-type refinement with no counting; it compares 1,699 tournaments (all labelled tournaments of orders at most five and 600 sampled labelled tournaments of order six). It finds, respectively for orders 1 through 6, \(1,1,2,4,7,11\) distinct theories and verifies global agreement between the logical-refinement signatures and the peeling invariant; output is in `verify_tournament_fo2.out`. `verify_tournament_pebbles.py` independently constructs the complete finite safety-game fixed point for the genuine two-pebble game on 157 selected pairs, including distinct cores, transitive cases and mixed orders. It finds no discrepancies; output is in `verify_tournament_pebbles.out`. Execute each with `python3` in a directory containing its source file; both use only the Python standard library. These finite calculations are checks, **not** proofs of the unrestricted quantifier-depth statement; that statement follows from the explicit permanent strategy and distinguishing formulas above.

## Relationship to prior work
Finite-variable logic and its Ehrenfeucht/pebble-game characterizations are standard (Pikhurko–Verbitsky, arXiv:1003.4865, especially their game preliminaries). The ordered decomposition of arbitrary tournaments into irreducible components is classical; Thörnblad (arXiv:1604.04271, Section 3, citing Moon) develops and proves its classical finite/countable form while studying tournament limits. Neither statement alone gives the two-variable equivalence classes. Geniet–Thomassé (arXiv:2207.07683) studies general first-order model-checking complexity and twin-width in tournament classes, not the equivalence quotient for the two-variable fragment. A narrower result for transitive-block substitutions into a directed triangle gives the \(h=t=0\) corner but does not classify tournaments with source/sink chains or arbitrary interior components. The present theorem combines logically definable head/tail peeling with the complete loss of information in source-free, sink-free cores.

## Limitations
The theorem is **relative to finite nonempty tournaments** in the pure directed-edge language with equality, no counting quantifiers, and two reusable variables. It does not classify arbitrary oriented graphs, richer signatures with named vertices or auxiliary relations, higher variable widths, infinite tournaments, or quantifier-rank-bounded spectra. An equivalence classification does not certify that the theorem is historically first: existing stronger general bisimulation or composition results may entail it; independent literature priority and external proof validation remain open.

## References
1. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865, first posted 2010-03-25; especially Sections 1 and 3 on finite-variable logic and games. https://arxiv.org/abs/1003.4865
2. E. Thörnblad, *Decomposition of tournament limits*, arXiv:1604.04271, first posted 2016-04-14, especially Section 3 for finite tournament structural decomposition. https://arxiv.org/abs/1604.04271
3. C. Geniet and S. Thomassé, *First Order Logic and Twin-Width in Tournaments and Dense Oriented Graphs*, arXiv:2207.07683, first posted 2022-07-15; comparison of subject and scope. https://arxiv.org/abs/2207.07683
