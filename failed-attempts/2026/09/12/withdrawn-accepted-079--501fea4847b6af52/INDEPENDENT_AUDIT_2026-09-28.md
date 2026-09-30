# Independent Audit — 2026/09/12/079

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `c4757f2dfd802af00fbf77d731486024fb6bab92`
- Disposition: **FAILED**

## Correctness

**PASS** — The stated wreath decomposition, finite-cycle cyclic-product invariant, and label-vanishing on bi-infinite cycles are standard and correct. The compact profinite group H=Aut(B) indeed has smooth conjugacy. The conditional countable-versus-continuum implication is also sound. However the record's claim that it is unknown which cardinality side H occupies is unnecessarily weak: H has continuum many conjugacy classes by an elementary explicit family. For A⊆N, swap the two child subtrees at each pairwise prefix-free vertex v_k=1^k0 for k∈A. At level n the number of fixed vertices is 2^n-sum_{k∈A,k≤n-2}2^(n-k-1), and this sequence recovers A. Distinct A therefore give nonconjugate automorphisms. This strengthens the record to the continuum side but does not falsify its conditional propositions.

## Originality

**FAIL** — Beserra-Coskey explicitly prove smooth conjugacy for every finitely branching rooted tree by compactness and point to the earlier labeled-orbit-tree conjugacy classification. Thus the H-smoothness core is prior. The remaining wreath-cycle statements are standard conjugacy theory for wreath products, and the supposedly open cardinality branch is settled by the elementary fixed-level construction above. The package does not isolate a substantial new classification theorem.

## Scientific value

**FAIL** — The record deliberately stops short of the motivating requested smoothness/non-smoothness certificate and leaves its own conditional dichotomy unresolved despite a direct continuum-class construction. As deposited, the result is mostly a synthesis of standard compact-tree and wreath-product facts and does not materially advance the target classification.

## Sources

- On the classification of automorphisms of trees (Kyle Beserra; Samuel Coskey): https://arxiv.org/abs/1709.02467 — Theorem 2.1 proves smooth conjugacy for finitely branching rooted trees by compactness; the paper also recalls earlier orbit-tree classifications.
- Conjugacy classes and centralisers in wreath products (David Bernhardt; Alice C. Niemeyer; Friedrich Rober; Lutz Wollenhaupt): https://arxiv.org/abs/2107.04645 — General wreath-product conjugacy and cyclic-product/territory framework.

## Limitations

- The explicit continuum family establishes only cardinality of H-conjugacy classes; the record's own reduction is still needed to pass from that fact to its =^+-hardness conclusion for G.
- This audit does not claim to provide the target's stronger requested generic-E0-ergodicity certificate.

GitHub was read only as evidence. No GitHub mutation, dispatcher completion call, or separate publication/report action was performed by this audit chat.
