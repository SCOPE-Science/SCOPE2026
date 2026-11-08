# Ten knowing-whether types versus twenty-two necessity types on complete multipartite frames

## Finding
For the class \(\mathcal K\) of all **nonempty finite, irreflexive, symmetric complete multipartite Kripke frames having at least two nonempty parts**, with one propositional variable \(p\) and unrestricted Boolean connectives, consider the two separate languages with sole modal operators \(\Delta\) (noncontingency, or knowing whether) and \(\Box\) (necessity). Their numbers of distinct pointed semantic types at maximum modal depth \(d\) are exactly
\[
\begin{array}{c|rrrrr}
 d&0&1&2&3&\ge4\\\hline
 \Delta&2&4&10&10&10\\
 \Box&2&6&16&22&22
\end{array}.
\]
The number of formula-equivalence classes under agreement at every pointed model on \(\mathcal K\) is the number of subsets of the respective pointed types. Thus the respective exact profiles are \(4,16,1024,1024,\ldots\) and \(4,64,65536,4194304,4194304,\ldots\). Both depth cutoffs are sharp. Every one-letter formula in the first language is equivalent over \(\mathcal K\) to one of depth at most two, whereas ordinary necessity requires depth three for full expressivity. At stabilization necessity has precisely \(4096\) times as many formula meanings as noncontingency.

## Assumptions and scope
A frame has vertex set partitioned into \(k\ge2\) nonempty independent parts \(P_1,\ldots,P_k\), and a vertex accesses precisely all vertices in all *other* parts, not its own part. A pointed model is a valuation \(v:W\to\{0,1\}\) and designated world \(w\). Interpret \(\Box\varphi\) as universal truth of \(\varphi\) among successors (vacuously true on an empty successor set, although none occurs here). Define \(\Delta\varphi:=\Box\varphi\lor\Box\neg\varphi\). Modal depth counts nested occurrences of the one designated operator, with depth zero for Boolean formulas. Equivalence is quantified over **every** finite such graph, all binary valuations, and all designated vertices; the two languages are compared separately, not by combining their operators.

## Proof
**1. Canonical finite universe.** A part is of category \(Z\) when every vertex has \(p=0\), category \(O\) when every vertex has \(p=1\), and category \(M\) when both truth values occur. Record the number of parts of each category, **truncated at two**, by a triple \(c=(c_Z,c_O,c_M)\in\{0,1,2\}^3\). For the current part record its category \(s\in\{Z,O,M\}\), and record the designated world's truth bit \(b\in B(s)\), where \(B(Z)=\{0\}\), \(B(O)=\{1\}\), and \(B(M)=\{0,1\}\). The canonical state space consists exactly of those \((c,s,b)\) with \(c_Z+c_O+c_M\ge2\) and \(c_s>0\). It has exactly \(68\) states. Each state occurs in an actual finite pointed model: take exactly \(c_j\) parts of each category, assigning one vertex to a pure part and two differently valued vertices to a mixed part. Since counts are truncated, every original model has one canonical state and every canonical state is realizable.

**2. Exact transition relation.** For \((c,s,b)\), its set of successor canonical states is exactly
\[
 E(c,s,b)=\bigl\{(c,t,b'):t\in\{Z,O,M\},\ c_t-\mathbf 1_{t=s}>0,\ b'\in B(t)\bigr\}.
\]
Here \(\mathbf 1_{t=s}\) is one if the current part has category \(t\), zero otherwise. The requirement \(c_t-\mathbf 1_{t=s}>0\) is exactly the condition for there to be another part of category \(t\). Truncation at two loses no such existence information. Every state listed on the right is realized by some successor because a mixed part has both \(p\)-values; none outside the set is. For a given Boolean-valued formula, only this support set of successor types matters, not the number of successors. Structural induction on formulas therefore shows that the 68-state graph, equipped with its initial bit \(b\), computes the truth of every one-variable formula in either language on every model in \(\mathcal K\), without any bound on actual number or sizes of parts.

**3. Partition refinement yields *all* formulas.** For each \(d\), partition the 68 states according to agreement on all formulas of modal depth at most \(d\). At depth zero, the two classes are the truth values of \(p\). Suppose the partition at depth \(d\) is known. Every union of its classes is definable by a depth-\(d\) Boolean formula: for each class, use a finite conjunction of separating depth-\(d\) formulas (and possibly their negations), then take disjunctions. Thus every possible Boolean labelling of those classes is available as a subformula.

For \(\Box\), the truth values of \(\Box\psi\) for all such subformulas distinguish the *entire set* \(S\) of depth-\(d\) classes present among successors: \(\Box\neg\chi_C\) is false precisely when \(C\in S\), where \(\chi_C\) names class \(C\). The exact depth-\(d+1\) refinement is therefore the pair (old class, successor-class support set).

For \(\Delta\), if \(|S|\le1\), every \(\Delta\psi\) is true. If \(|S|\ge2\), the predicate \(\Delta\chi_C\) is false exactly when \(C\in S\); hence the entire support set is recovered. The exact refinement is the pair (old class, successor-class support set when it has at least two elements, and a single common symbol otherwise). These descriptions apply to all Boolean combinations and to all formulas, not merely to a selected list of test formulas.

**4. Finite exact certificate and termination.** The accompanying `abstract_checker.py` constructs all 68 states and their exact successor supports from the formulas of steps 1–2. It starts at the depth-zero partition and computes precisely the two refinements proved in step 3. Its complete 68-state calculations return class counts \(2,4,10,10\) for \(\Delta\) and \(2,6,16,22,22\) for \(\Box\). The script also verifies the last partition is a fixed point under the corresponding refinement. At a fixed point, induction gives the same partition at all higher depths. Every one of the distinct classes at each stage is definable, by step 3, so there are exactly \(2^r\) formula-equivalence classes when there are \(r\) types. Since the class counts increase strictly at each depth before the fixed point, the asserted thresholds are sharp. The argument is a finite computation embedded inside an exhaustive, proved abstraction covering arbitrarily large finite graphs, not an extrapolation from a finite sample of graphs.

## Verification
Execute `python3 abstract_checker.py` using standard Python 3. The complete abstract calculation outputs the asserted type and formula-equivalence profiles and checks stability after the claimed depth. Execute `python3 finite_models_checker.py` to independently enumerate every valuation and pointed vertex on six fixed complete bipartite graphs and independently evaluate Boolean-subformula closure for \(\Delta\). The finite-model checker is a corroboration of the reduction; the exact 68-state argument is what covers the infinite frame family. Both programs are embedded with their complete source. A supplementary direct necessity checker `finite_box_checker.py` evaluates the usual \(\Box\) on the same small examples.

## Relationship to prior work
Wang and Zenger's *Proof Theory for Non-Contingency Logic* (first public September 30, 2026) treats general labelled proof systems and frame conditions; the inspected exposition and theorems do not furnish the present exact modal-depth profile or the 68-state canonical quotient for complete multipartite frames. Humberstone's work on agreement/noncontingency establishes general semantic and logical foundations, not the specific quantitative classification. Fan, Wang and van Ditmarsch study knowing whether and expressive comparison with ordinary modalities; those general expressivity comparisons do not directly yield the sharp finite-algebra counts above. The contribution here is specifically the universal complete-multipartite one-letter algebra, compared quantitatively with necessity, including both sharp depth cutoffs. Standard Boolean partition refinement is a proof technique, not asserted to be new.

## Limitations
The classification concerns one propositional atom, complete multipartite finite frames with at least two parts, classical Boolean connectives, and the **irreflexive** cross-part relation. It does not assert the same counts for reflexive frames, arbitrary symmetric frames, several atoms, or a language containing both modalities simultaneously. The 68-state script checks a finite reduction whose completeness is proved above; its numerical assertions remain dependent on correct execution and transcription, and independent audits have not been performed. An equivalent exact census could exist in unindexed work, so bibliographic priority is not independently certified.

## References
1. Y. Wang and L. Zenger, *Proof Theory for Non-Contingency Logic*, arXiv:2609.38975, initially public 2026-09-30; https://arxiv.org/abs/2609.38975.
2. L. Humberstone, *The Modal Logic of Agreement and Noncontingency*, Notre Dame Journal of Formal Logic, 2002, DOI:10.1305/ndjfl/1071509431.
3. J. Fan, Y. Wang and H. van Ditmarsch, *Contingency and Knowing Whether*, Review of Symbolic Logic, DOI:10.1017/S1755020314000343.
