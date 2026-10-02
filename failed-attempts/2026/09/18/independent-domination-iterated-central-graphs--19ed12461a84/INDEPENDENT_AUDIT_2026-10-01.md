# Independent audit — Independent domination stabilizes on iterated central graphs

**Disposition: FAILED.**

## Correctness

**PASS** — The lemma \(\alpha(C(G))=|E(G)|\) is correct for connected graphs of order at least three: subdivision vertices give the lower bound, while the original vertices of an independent set form a clique and incident-edge counting gives the upper bound. Substitution into Cabrera-Martínez et al. Theorem 2.12 simplifies exactly to \(i(C^k(G))=2|E(C^{k-2}(G))|\). An independent brute-force check verified the independence lemma for all connected graph-atlas graphs of orders three and four.

## Originality

**FAIL** — A published SCOPE record dated 2026-09-17, “Independent domination of higher iterated central graphs” (Resultary path 2026/9/17/SCOPE-iterated-central-graph-independent-domination--7dc2104ad847), was inspected in full and states the same all-iterate theorem, the same \(\alpha(C(H))=|E(H)|\) lemma, the same use of Theorem 2.12, and the same order/size consequences. The audited 2026-09-18 claim is therefore exactly covered by an earlier published record.

## Scientific value

**FAIL** — The theorem is mathematically clean, but this package does not fill a remaining research gap because the identical theorem and proof mechanism had already been published by SCOPE on 2026-09-17. Re-presenting that exact result one day later adds no independent mathematical contribution.

## Source inspections

- **Independent domination in central graphs** (arXiv:2609.16357v1): complete primary full text including Theorem 2.12. Assessment: PRIOR INPUT, stops at second iterate.
- **Independent domination of higher iterated central graphs** (Resultary 2026/9/17/SCOPE-iterated-central-graph-independent-domination--7dc2104ad847): complete published RESULT.md. Assessment: COVERING: exact same theorem and proof mechanism.

## Originality checks

### Equivalent Formulations

Notation differences between \(C\) and \(\mathtt C\) do not change the statement.

Searches: Resultary independent domination higher iterates central graph third iterate kth iterate.

Evidence: 2026-09-17 SCOPE record gives verbatim-equivalent theorem and consequences.

### Broader Coverage

The decisive coverage is not the primary source but the earlier 2026-09-17 published SCOPE theorem.

Searches: Cabrera-Martínez et al arXiv:2609.16357 full text.

Evidence: The primary paper stops at the second iterate.

### Exact Database Or Table

This is an exact duplicate theorem rather than a database-table issue.

Searches: Resultary exact iterated central independent domination query.

Evidence: Exact earlier record: 2026/9/17/SCOPE-iterated-central-graph-independent-domination--7dc2104ad847.

### Claim Vs Prior Implication

The earlier record directly implies every scientific statement being claimed here.

Searches: full RESULT.md of the 2026-09-17 SCOPE record.

Evidence: It states \(i(C^k(G))=2|E(C^{k-2}(G))|\), proves \(\alpha(C(H))=|E(H)|\), and derives the same order/size dependence.

## Residual risks

- None material to the coverage decision; the earlier published record is decisive.

## Limitations

The theorem is correct, but the research finding is rejected because an earlier published SCOPE record dated 2026-09-17 states the same all-iterate theorem and proof mechanism.

This assessment preserves the historical same-model review as prior evidence but does not treat it as independent support for this audit.
