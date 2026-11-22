# Scientific review

## Correctness — PASS

The hypothesis is a hereditary class of finite strict chains with exactly one of \(q\) named unary colours on each point, not a class requiring each colour to occur in every substructure. The one-point-extension game has precisely one type for every named colour and gap. Its recursive semantics gives a min-across-gaps rank and a per-colour max-over-pivots recurrence, with correct empty-gap and missing-colour boundary cases. In the inductive basis proof the extreme leftmost/rightmost of the \(q\) pivot positions supply the two recursive witnesses; their order supplies the central colour permutation. Conversely each central colour position has both necessary flanking witnesses. This gives the exact threshold and unique fixed-length decomposition for the minimum word census. Proof covers every \(q\ge1\), \(t\ge0\), and finite host size. Finite checks reproduce the abstract game on 2,127 host words, compare embeddings on 69,029 cases, and enumerate extremizers. The main unbounded claim is proved mathematically rather than inferred from those checks.

## Originality — PASS within inspected evidence

The full text of López-Callejas–Navarro-Castillo (arXiv:2604.14461) defines precisely this rank but computes finite orders with no colours; its \(\lfloor\log_2(n+1)\rfloor\) theorem is the \(q=1\) case only. Mwesigye–Truss (2018), inspected in the lawful open full PDF, asks about shortest representatives of a **two-structure** Ehrenfeucht–Fraïssé equivalence class. Its two- and three-move results do not imply the single-host, one-sided recursion, particularly the complete rank-at-least-\(t\) scattered-subword basis and count \((q!)^{2^t-1}\). Related published searchable results on one-red orders, three-move coloured orders and one-joker subsequence covers involve different properties and different implication directions. Other previously reported mathematical claims were compared by their statements and implications. Residual risk: literature search is finite and does not certify historical global priority.

## Value — PASS

The classification solves an intrinsic finite-rank invariant on the natural class of coloured finite orders: exact thresholds, all minimum hosts, their named-colour counts, and relative ranks for arbitrary marked suborders. It records how a finite palette multiplies adversarial insertion requirements, yielding many genuinely distinct extremizers, rather than simply rescaling an uncoloured formula. It is a complete basis theorem with a dynamic-programming test, not an arbitrary finite census or unsupported downstream application.

## Limitations and provenance

The theorem is finite, uses a fixed nonempty named palette, and does not classify countable orders. Its computable enumeration is corroboration, not an infinite proof. The named references were read to the extent specified in the accompanying structured scientific comparison; no unindexed literature is asserted absent. Independent mathematical and historical-priority audits have not been performed.

Self-review: passed. Independent audit: not yet performed.
