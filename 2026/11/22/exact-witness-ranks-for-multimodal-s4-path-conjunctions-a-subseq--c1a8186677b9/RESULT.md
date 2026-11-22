# Exact witness ranks for multimodal \(\mathsf{S4}\) path conjunctions: a subsequence-antichain law

## Finding

Let \(\Sigma\) be an alphabet of \(q\geq1\) distinct modal indices and let \(L\subseteq\Sigma^*\) be a finite nonempty set of words, with empty word \(\varepsilon\) permitted. For any word \(w\), let \(\rho(w)\) delete all but one symbol from every maximal run of identical symbols. Write \(u\preceq v\) if \(u\) is a scattered subsequence of \(v\), and put
\[
A(L)=\min_{\preceq}\{\rho(w):w\in L\}.
\]
The minimum denotes the set of distinct minimal words. In the class of all Kripke structures in which each indexed accessibility relation is reflexive and transitive, consider
\[
\Phi_L(p)=\bigwedge_{w\in L}\langle w\rangle p,
\]
where \(\langle w\rangle\) is the nested sequence of indexed diamonds indicated by \(w\), and \(\langle\varepsilon\rangle p=p\).

**Exact witness-rank theorem.** The least nonnegative integer \(k\) such that, on *every* such pointed Kripke structure \((M,s)\) with \(M,s\models\Phi_L(p)\), there is a set \(X\subseteq V(p)\) with \(|X|\leq k\) and \(M[p\mapsto X],s\models\Phi_L(p)\), is precisely
\[
\boxed{\operatorname{wr}(\Phi_L)=|A(L)|.}
\]
The lower bound always has a finite rooted, acyclic-off-the-diagonal witness model.

For all nonempty conjunctions of modal word length at most \(d\geq1\), the sharp greatest witness rank is
\[
\boxed{B(q,d)=\begin{cases}1,&q=1,\\q(q-1)^{d-1},&q\geq2.\end{cases}}
\]
It is attained by conjoining the path formulas for *all* length-\(d\) words with no two successive indices equal. In particular, the maximum rank is exactly two for two modalities at *every* depth, while it grows exponentially as \(3\cdot2^{d-1}\) for three modalities. With an empty conjunction, excluded here, the rank would be zero.

## Assumptions and scope

The carrier is nonempty but may be finite or infinite. Each of the \(q\) binary relations \(R_a\) is individually reflexive and transitive; there is no assumption that two different relations commute, confluence, or coincide. Valuations of \(p\) are arbitrary subsets of the carrier, and all other atoms, if any, are irrelevant. A point satisfies \(\langle a_1\cdots a_t\rangle p\) if a corresponding \(R_{a_i}\)-walk ends in \(V(p)\). Witness rank measures the **uniform number of retained \(p\)-points**, not the size of a whole model, and is quantified over all models and all starting states. The theorem is limited to a finite conjunction of existential paths to one positive atom; it is not asserted for formulas containing universal modalities, negation, further Boolean nesting, or fixed-point operators.

## Proof

**1. The word relation.** Reflexivity and transitivity give \(R_a\circ R_a=R_a\), hence \(R_w=R_{\rho(w)}\). Reflexivity also gives \(R_u\subseteq R_v\) whenever \(u\preceq v\): insert diagonal steps at the deleted indices of \(v\). Therefore \(\Phi_L(p)\) is equivalent on every frame of the specified class to \(\bigwedge_{u\in A(L)}\langle u\rangle p\). If this holds at the starting state, choose one terminal \(p\)-point witnessing each conjunct. The union has at most \(|A(L)|\) points, and retaining those points still satisfies the conjunction. This proves the upper bound.

**2. A sharp finite countermodel to smaller supports.** The set \(A=A(L)\) consists of reduced words and is an antichain for \(\preceq\), hence is prefix-free. Form the finite set \(T\) of all prefixes of words in \(A\), including \(\varepsilon\), as worlds. Include the directed edge \(t\to ta\) labeled \(a\) whenever \(ta\in T\); define \(R_a\) as the reflexive transitive closure of the \(a\)-labeled edges. Mark \(p\) at precisely the leaf worlds in \(A\). These \(R_a\) are reflexive and transitive by construction. Because every branch word in \(A\) is reduced, a directed branch never contains two consecutive edges with the same label. Consequently any \(R_v\)-walk starting at the root and ending at a leaf \(u\in A\) follows the unique root-to-leaf path and requires \(u\preceq v\). The converse is realized by inserting diagonal steps for deleted indices. Thus
\[
\varepsilon R_v u\quad\Longleftrightarrow\quad u\preceq v\qquad(u\in A).
\]
For \(u,v\in A\), antichainness makes the right side true exactly if \(u=v\). Every conjunct has its *own unique* marked witness. Removing that mark makes its conjunct false, even if every other marked point is retained. Hence no valuation with fewer than \(|A|\) marked points satisfies the formula at the root of this model. This proves the lower bound and the exact theorem. The case \(A=\{\varepsilon\}\) is the one-world model; all cases are covered.

**3. Depth bound.** An antichain of reduced words is prefix-free. For \(q\geq2\), there are \(q(q-1)^{d-1}\) reduced words of length exactly \(d\). Each reduced word \(u\) with \(1\leq|u|\leq d\) has exactly \((q-1)^{d-|u|}\geq1\) length-\(d\) continuations. The continuation sets of distinct prefix-free words are disjoint. Hence a nonempty antichain not containing \(\varepsilon\) has at most \(q(q-1)^{d-1}\) members. If it contains \(\varepsilon\), it has one member. The full length-\(d\) layer is a subsequence antichain of that cardinality and attains the bound by part 2. For \(q=1\), the only distinct reduced words are \(\varepsilon\) and the single letter; they are comparable, giving the bound one. This completes all quantifiers and boundary cases.

## Verification

A standalone standard-library script, `verify.py`, creates each finite prefix-trie model, closes every indexed relation under reflexivity and transitivity, and tests the exact path-reachability/subsequence condition and indispensability of each marked leaf. It exhausts all nonempty sets of reduced words for \((q,d)=(1,4),(2,3),(3,2)\), checks additional seeded three-letter cases through depth three, and checks complete depth layers for up to four modalities and four levels. Its actual run reports `VERIFY_OK cases=1469 max_q2=2 q3_d3=12 trie_worlds=22`. The computational checks are finite corroboration; the preceding proof covers all depths and infinite frames. Run `python3 verify.py` beside this document.

## Relationship to prior work

Van Benthem, ten Cate and Yang (2026, Section 2.4, especially Proposition 2.9 and Proposition 2.10) define strong continuity via an unspecified uniform finite support bound and study its transfer to finite models. The present statement determines the *least* bound for the special, explicit class of existential word conjunctions over separate reflexive-transitive relations and also computes its maximum as a function of alphabet size and depth. Their general finiteness theorem does not supply the numerical subsequence-antichain formula. The familiar \(\mathsf{S4}\) axioms give the repeated-index cancellation, which is used here but does not by itself prove the indispensable-witness lower bound or the two-versus-three alphabet threshold. Gouveia and Santocanale (2019) study infinite-cardinal continuity and the modal \(\mu\)-calculus, distinct from this sharp natural-number witness budget. Literature and specialized database searches found related word conditions and modal generator counts, but no inspected statement covering this exact claim; this is a qualified priority assessment, not a claim of exhaustive novelty.

## Limitations

No independent mathematical validation or exhaustive historical priority audit has been performed. A previously unindexed result on word embeddings or support-width of positive multimodal formulas could imply the result. The bound is syntactically specialized and does not imply a similar bound for conjunctions with \(\Box\), negative occurrences of \(p\), or additional modal frame interactions. The executable check does not independently certify the unrestricted theorem.

## References

1. J. van Benthem, B. ten Cate and X. Yang, *When do modal definability and preservation theorems transfer to the finite?*, arXiv:2603.12171v1 (first public posting March 12, 2026), Section 2.4 and Propositions 2.9–2.10. https://arxiv.org/pdf/2603.12171
2. M. J. Gouveia and L. Santocanale, *Aleph1 and the modal mu-calculus*, Logical Methods in Computer Science **15** (2019), arXiv:1704.03772, Introduction, pp. 1–3. https://arxiv.org/pdf/1704.03772
3. *Modal Logic*, Stanford Encyclopedia of Philosophy, section on \(\mathsf{S4}\), reflexivity and transitivity. https://plato.stanford.edu/entries/logic-modal/
