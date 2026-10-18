# Under multiple choice, Galois-type bases already characterize choice without Foundation
## Finding
Define \(\mathsf{GAB}_{\mathrm{wo},0}\) to mean: whenever \(L/F\) is a normal separable algebraic field extension, the base field \(F\) is well-orderable, and \(\operatorname{char}(F)=0\), the \(F\)-vector space \(L\) has a basis. Then, over \(\mathsf{ZF}^{-}\),
\[
\mathsf{AC}\quad\Longleftrightarrow\quad \mathsf{MC}+\mathsf{GAB}_{\mathrm{wo},0}.
\]
Thus, once multiple choice is available, the basis hypothesis needed to recover full choice can be restricted from all vector spaces over well-orderable characteristic-zero fields to the natural class of normal separable algebraic extensions.

## Assumptions and scope
The ambient theory is \(\mathsf{ZF}^{-}\), Zermelo--Fraenkel set theory without Foundation. Here \(\mathsf{MC}\) is the axiom of multiple choice. A field is well-orderable when its underlying set admits a well-ordering. No claim is made that \(\mathsf{GAB}_{\mathrm{wo},0}\) alone implies \(\mathsf{MC}\) or \(\mathsf{AC}\).

## Proof
The forward implication is immediate: \(\mathsf{AC}\) implies \(\mathsf{MC}\) and gives a basis to every vector space, hence in particular to each extension covered by \(\mathsf{GAB}_{\mathrm{wo},0}\).

For the converse, assume \(\mathsf{MC}+\mathsf{GAB}_{\mathrm{wo},0}\), and let \(X\) be an arbitrary set. Fernandes, Mezabarba, and Rodrigues prove, under \(\mathsf{MC}\), that there are a well-orderable characteristic-zero field \(K\), a normal separable algebraic extension \(L/K\), and an injection \(X\to L\) (their Theorem B, proved in Section 7).

Their Theorem A says that such an \(L/K\) is well-orderable provided that for every well-orderable intermediate field \(F\) with \(K\subseteq F\subseteq L\), the \(F\)-vector space \(L\) has a basis. Fix such an \(F\). Because \(K\) has characteristic \(0\), so does \(F\). Since \(L/K\) is algebraic, normal, and separable, the extension \(L/F\) is again algebraic, normal, and separable; this inheritance is also used explicitly in the proof of their Theorem A. Hence \(\mathsf{GAB}_{\mathrm{wo},0}\) supplies the required \(F\)-basis of \(L\).

Theorem A therefore well-orders \(L\). Pulling that well-ordering back along \(X\to L\) well-orders \(X\). Since \(X\) was arbitrary, the well-ordering theorem holds and therefore \(\mathsf{AC}\) holds.

## Verification
The proof was checked against the full text of arXiv:2609.20140v2. Theorem B constructs the well-orderable characteristic-zero base and normal separable algebraic extension containing an arbitrary set; Theorem A states exactly the intermediate-field basis criterion needed to well-order the extension. Its proof explicitly notes that \(L/F\) stays normal, separable, and algebraic at every intermediate stage. Corollary 7.1 in the source assumes bases for every vector space over every well-orderable characteristic-zero field; the argument above verifies that only the Galois-type extensions appearing in Theorem A are needed.

## Relationship to prior work
The source paper proves that, in \(\mathsf{ZF}^{-}\), existence of bases for all characteristic-zero vector spaces implies \(\mathsf{AC}\), and records the equivalence of \(\mathsf{AC}\) with \(\mathsf{MC}\) plus bases for every vector space over every well-orderable characteristic-zero field. The present observation narrows the latter basis principle to normal separable algebraic extensions. Targeted semantic-database and web searches found no statement of this restricted equivalence. Historical papers on bases over fixed or specific fields use broader all-vector-space hypotheses in the accessible statements; a thematically close 2013 paper was available only at abstract level and remains a stated originality risk.

## Limitations
The result retains \(\mathsf{MC}\) as a separate hypothesis. It does not show that the restricted Galois-type basis principle by itself implies multiple choice, nor does it determine the relative strength of that restricted principle in models where \(\mathsf{MC}\) fails. The originality conclusion is based on targeted searches rather than an exhaustive classification of historical weak-choice principles.

## References
Gabriel Fernandes, Renan Maneli Mezabarba, and Vinicius de Oliveira Rodrigues, “Existence of bases implies the axiom of choice, a foundation-free proof,” arXiv:2609.20140v2 (first public version 17 September 2026). Relevant points: Theorem A, Theorem B, the proof of Theorem 1.2, Corollary 7.1, and Section 7.
