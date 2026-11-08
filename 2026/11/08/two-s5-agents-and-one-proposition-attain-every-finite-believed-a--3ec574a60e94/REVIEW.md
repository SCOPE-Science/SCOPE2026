# Review: two-agent S5 stabilization resources

## Correctness

**PASS.** The belief-update semantics filters every agent's relation by the same truth set of targets. Because the initial S5 relations are reflexive, the retained target set obeys \(T_{k+1}=T_k\cap\llbracket\varphi\rrbracket_{M^k}\), and each updated relation is exactly its original relation restricted to those targets. In the alternating two-element equivalence blocks, the fixed depth-one formula tests the immediate right neighbor's continued target status. Induction yields \(T_k=\{0,\ldots,n-k-1\}\) and exactly \(n\) changes. All n are covered by the proof; the script's sizes through 100 are only checks. The one-agent upper follows from simultaneous within-block valuation-type deletion (as in earlier work); a uniform-equivalence construction realizes \(\min\{n,2^r\}\), including the zero-atom case.

## Originality

**PASS relative to inspected primary and indexed sources, with historical-priority risk.** The closest earlier published finite-state theorem already proves the general \(n\)-round upper bound and has a sharp directed-cycle witness. That witness is not S5. Yamada's single-agent K45 argument already proves the valuation-type upper mechanism; we expressly credit it. His multi-agent peeling examples use non-S5 accessibility, while the S5 sigma-validity existence examples use more proposition names and formulas dependent on length. The new finding is the two-agent *initial S5* extremizer with a formula independent of n, one proposition, modal depth one and equivalence classes of size at most two. A general upper bound does not imply subclass sharpness; the one-agent one-letter upper bound of two gives a concrete non-implication comparison. No equivalent indexed statement was found, though sources outside the inspected corpus remain a risk.

## Value

**PASS.** The exact attainable stabilization lifetime under a sharply restricted epistemic frame and vocabulary is a natural complexity/resource invariant. A second agent changes the one-letter lifetime from at most two rounds to as many rounds as there are worlds; independently the per-agent indistinguishability classes never exceed size two. This identifies a structural agent-arity boundary relevant to iterated belief updates rather than an incidental finite count.

## Literature and limits

Source: E. Yamada, *Eventual and Strong Eventual Notions in Public Announcements*, arXiv:2609.24006v1 (first posted 2026-09-21), Definition 5 and Lemma 6; E. Yamada, *Classification of σ-validity in iterated announcements*, arXiv:2607.04685, Sections 3-4; published result *Sharp state-count stabilization bound for finite believed announcements*, identifier `2026/10/4/SCOPE-sharp-state-count-stabilization-bound-for-finite-believed-announ--65b4b662c65e`. The construction requires S5 **only initially**, not after deleting arrows. It does not prove uniqueness of extremizers. Earlier equivalent observations outside inspected records are possible. Independent scrutiny of proof and historical priority remains outstanding.

Self-review: passed. Independent audit: not yet performed.
