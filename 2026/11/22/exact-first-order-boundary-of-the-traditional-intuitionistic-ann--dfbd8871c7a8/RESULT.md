# Exact first-order boundary of the traditional intuitionistic announcement-necessity reduction

## Finding

Let \(F=(W,\leq,R)\) be a nonempty birelational frame, where \(\leq\) is a preorder and \(R\) is an arbitrary binary relation. Interpret intuitionistic public announcements by restriction to the upward-closed truth set of the announced formula, and interpret necessity by quantifying over modal successors of all future worlds, as specified below.

**Theorem (exact frame correspondence).** The following statements are equivalent, without any finiteness or confluence assumption:

1. Every persistent valuation on \(F\) validates every instance of the traditional necessity-reduction schema
   \[
   [A]\Box B\ \leftrightarrow\ (A\to\Box[A]B).
   \]
2. Every persistent valuation on \(F\) validates its single two-atom instance
   \[
   [p]\Box q\ \leftrightarrow\ (p\to\Box[p]q).
   \]
3. The frame satisfies the following first-order condition \(\mathsf{AR}\):
   \[
   \begin{aligned}
   \forall v,u,w\;\bigl(vRu\land u\le w\ \Longrightarrow\
   \exists v',u'\;(&v\le v'\land v'Ru'\land u'\le w\\
   &\land(v\le u'\lor w\le u'))\bigr).
   \end{aligned}
   \]

The customary forward-confluence condition
\[
 vRu\land u\le w\ \Longrightarrow\ \exists v'\ge v\ (v'Rw)
\]
implies \(\mathsf{AR}\), but not conversely. The separation already occurs on a two-element chain, and two elements are minimal for an invalid instance. Thus the traditional reduction axiom remains valid on a strictly larger class than the conventionally sufficient forward-confluent frames.

## Assumptions and scope

A valuation sends each atom to an upward-closed subset of \(W\). Every formula's truth set is upward-closed under the following forcing clauses:

- \(s\Vdash C\to D\) iff every \(t\ge s\) forcing \(C\) also forces \(D\).
- \(s\Vdash\Box C\) iff for all \(t\ge s\), every \(R\)-successor of \(t\) forces \(C\).
- \(s\Vdash[A]C\) iff for all \(t\ge s\) forcing \(A\), \(C\) holds at \(t\) in the model restricted to \(P=\llbracket A\rrbracket\).

The preorder and the relation are both restricted to \(P\); the valuation is restricted too. The unrestricted binary modality of relativized necessity and further announcement operators may occur in \(A\) and \(B\). The proof only needs persistence of their truth sets, which follows by structural induction for the language of Balbiani, van Ditmarsch, Gencer and Lerouvillois (2026). The correspondence is a frame-validity statement: **all** persistent valuations and **all** worlds are quantified.

Here \(\uparrow S=\{z:\exists y\in S,\ y\le z\}\) and \(R[S]=\{u:\exists v\in S,\ vRu\}\). These definitions also cover nonantisymmetric preorders.

## Proof

Fix formulas \(A,B\) and a persistent valuation. Let \(P=\llbracket A\rrbracket\), and let \(Q\subseteq P\) be the truth set of \(B\) in the restricted model on \(P\). Both \(P\) and \(Q\) are upward-closed in \(W\). Indeed, \(Q\) is upward-closed in the induced preorder on \(P\), and \(P\) itself is an upset.

By expanding the forcing clauses and using transitivity of \(\le\), at any world \(s\), the left side of the reduction is equivalent to
\[
 L_s:\quad \forall v\ge s\ \forall u\;((v\in P\land vRu\land u\in P)\Rightarrow u\in Q),
\]
whereas the right side is equivalent to
\[
 H_s:\quad \forall v\ge s\ \forall u,w\;((v\in P\land vRu\land u\le w\land w\in P)\Rightarrow w\in Q).
\]
The intermediate future-world quantifiers collapse because \(\le\) is transitive and \(P\) is upward-closed. Since \(\le\) is reflexive, \(H_s\) always entails \(L_s\), without any frame condition.

**Sufficiency of \(\mathsf{AR}\).** Assume \(L_s\). Fix \(v\ge s\) in \(P\), an edge \(vRu\) and \(w\ge u\) in \(P\). The frame condition supplies \(v'\ge v\) and \(u'\le w\) with \(v'Ru'\) and either \(v\le u'\) or \(w\le u'\). As \(P\) is an upset containing both \(v\) and \(w\), it contains \(u'\) in either case. It also contains \(v'\). Therefore \(L_s\) yields \(u'\in Q\), and upward closure of \(Q\) yields \(w\in Q\). Thus \(H_s\) holds. Together with the unconditional reverse implication, this proves the full reduction schema.

**Necessity from the atomic instance.** Suppose \(\mathsf{AR}\) fails. Choose \(v,u,w\) such that \(vRu\) and \(u\le w\), but no \(v',u'\) satisfy its consequent. Define the upsets
\[
 P=\uparrow\{v\}\cup\uparrow\{w\},\qquad
 Q=\uparrow\bigl(R[\uparrow\{v\}]\cap P\bigr).
\]
One has \(Q\subseteq P\). Furthermore \(w\notin Q\): otherwise some \(v'\ge v\) and \(u'\in P\) would satisfy \(v'Ru'\) and \(u'\le w\); membership of \(u'\) in \(P\) would mean \(v\le u'\) or \(w\le u'\), contradicting the failure of \(\mathsf{AR}\).

Set the atomic valuations \(V(p)=P\), \(V(q)=Q\). At \(v\), the formula \([p]\Box q\) holds: every surviving successor in \(P\) of every world above \(v\) belongs to \(R[\uparrow\{v\}]\cap P\subseteq Q\). But \(p\to\Box[p]q\) fails at \(v\). Indeed, \(v\in P\), \(vRu\), and \(u\le w\) with \(w\in P\setminus Q\), so \([p]q\) is false at \(u\) and consequently \(\Box[p]q\) is false at \(v\). Thus the two-atom instance detects every failure of the frame condition. The full schema entails the atomic instance trivially; all three statements are equivalent.

**Sharpness relative to standard confluence.** Forward confluence supplies \(v'\ge v\) with \(v'Rw\), so \(\mathsf{AR}\) holds by choosing \(u'=w\). On the chain \(0<1\), take \(R=\{(0,0)\}\). The condition \(\mathsf{AR}\) holds: for the only edge, \(v=u=0\); when \(w=1\), choose \(v'=u'=0\), which satisfies the alternative \(v\le u'\). But forward confluence fails for \(0R0\) and \(0\le1\), since no arrow ends at \(1\).

On the same chain, \(R=\{(1,0)\}\) fails \(\mathsf{AR}\) at \((v,u,w)=(1,0,1)\). In particular, \(V(p)=\{1\}\) and \(V(q)=\varnothing\) falsify the atomic reduction at world \(1\). No one-world preorder frame can fail \(\mathsf{AR}\): if its only arrow exists, its endpoints and the target are equal and themselves witness the existential. Thus two worlds are the sharp smallest counterframe size.

## Verification

The standalone file `verify.py`, with no external dependencies, computes \(\mathsf{AR}\) directly from the relational quantifiers and independently checks the two atomic announcement formulas from their forcing clauses for **every** preorder and binary relation on \(1\), \(2\) or \(3\) labelled worlds. It also enumerates all binary relations on fixed chains of orders \(2\), \(3\) and \(4\), checking their \(\mathsf{AR}\) status and strict separation from ordinary forward confluence.

The exhaustive preorder counts are respectively \((1,2,2)\), \((4,64,56)\) and \((29,14848,9571)\), in the order (number of preorders, number of frames, number validating the reduction). On fixed chains of orders \(2\), \(3\), \(4\), the valid relation counts are \(12\), \(224\), \(14592\), of which respectively \(1\), \(26\), \(1215\) fail ordinary forward confluence. The program separately checks both two-world examples. The checker output is `VERIFY_OK` with these values. Enumeration is only a finite cross-check; it is not used to infer the all-cardinalities theorem.

## Relationship to prior work

Balbiani, van Ditmarsch, Gencer and Lerouvillois (2026, arXiv:2611.14408), Introduction and Sections 3–4, explicitly observe that the traditional reduction \([A]\Box B\leftrightarrow(A\to\Box[A]B)\) fails without standard confluence, and replace it by a reduction employing binary relativized necessity. Their setting and forcing clauses are exactly those used here. They establish the soundness of their replacement over arbitrary birelational frames, but do not state the necessary-and-sufficient condition \(\mathsf{AR}\) for retaining the traditional axiom or its two-atom completeness.

Ma, Palmigiano and Sadrzadeh (2014), particularly the algebraic modal reduction Lemma 35, establish the traditional reduction in the stricter intuitionistic public announcement setting. This supports the sufficient direction but does not establish the precise validity class for arbitrary preorders and relations.

The published frame-correspondence results *Exact frame correspondence for Box Excluded Middle* (2026-10-12) and *Exact frame correspondence and finite-chain census for box excluded middle* (2026-10-18) analyze the distinct **static** schema \(\Box\varphi\vee\neg\Box\varphi\) under an extra basic modal persistence condition and a different box forcing clause. Their exact correspondence is about the upward closure of successor rows of comparable worlds. Neither result establishes a dynamic announcement reduction with an arbitrary modal relation. Both complete accessible reports were compared at the level of hypotheses and implications. Other related records concerned asynchronous updates, confluence enumeration, and modal-relation observational quotients; none of the retrieved statements subsumes \(\mathsf{AR}\).

## Limitations

The theorem is not a completeness theorem or an elimination theorem for arbitrary intuitionistic public-announcement formulas, and it does not replace the valid relativized-necessity reduction of the 2026 paper. It characterizes when one specific **traditional** reduction schema is frame-valid, including arbitrary infinite preorders. It assumes the explicit future-world forcing clause for necessity; changing to a different modal clause may change the correspondence.

The finite census fixes the labels and the preorder; it is not an enumeration of isomorphism classes. The all-cardinalities conclusion follows from the symbolic proof, not the small cases. The literature inspection establishes noncoverage by the sources examined, not a universal guarantee of historical priority; an equivalent result under different dynamic-algebraic terminology may exist.

## References

1. P. Balbiani, H. van Ditmarsch, C. Gencer and C. Lerouvillois, *A minimal intuitionistic public announcement logic*, arXiv:2611.14408, first public 2026-11-10, https://arxiv.org/abs/2611.14408. Introduction, Sections 3 and 4.
2. M. Ma, A. Palmigiano and M. Sadrzadeh, *Algebraic semantics and model completeness for Intuitionistic Public Announcement Logic* (2014), https://www.academia.edu/109184799/Algebraic_semantics_and_model_completeness_for_Intuitionistic_Public_Announcement_Logic. Section 6.3, Lemma 35.
3. *Exact frame correspondence for Box Excluded Middle* (2026-10-12), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-exact-frame-correspondence-for-box-excluded-middle--1ecb5d699ac7. `RESULT.md`.
4. *Exact frame correspondence and finite-chain census for box excluded middle* (2026-10-18), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-frame-correspondence-and-finite-chain-census-for-box-exclu--64522d36a52e. `RESULT.md`.
