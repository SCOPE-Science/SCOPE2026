---
audit_date: 2026-10-01
status: failed
---

# Independent scientific audit

## Final claim

For Cintioli's locally Join-Property extension inside \(\mathrm{GL}_1\), every ordinary jump-degree fibre above \(\mathbf0'\) is countable, dense, and has no isolated points, hence is homeomorphic to \(\mathbb Q\); the extension is partitioned into continuum many pairwise disjoint dense such fibres.

## Correctness — PASS

Cintioli's theorem gives the Join Property on every nonempty relative cylinder of the extension, while the appendix gives countably infinitely many jump-inversion degrees above every target for any Join-Property class. Because the extension is contained in \(\mathrm{GL}_1\), generalized-low and ordinary jump fibres coincide. Applying the appendix to each relative cylinder gives local infinitude and hence density and no isolated points. Every fibre is countable because each member is computable from a fixed representative of its jump degree. Sierpiński's classical theorem then gives the homeomorphism with \(\mathbb Q\); disjointness, coverage, and continuum-many indices are immediate.

**Checked sources.** assigned RESULT.md at tree 33e84c478e2949d0264ae244998434171bcfdea2; Cintioli, arXiv:2609.37480, primary abstract and theorem-level source material; Sierpiński 1920 countable dense-in-itself metrizable-space theorem

**Residual risks.** No correctness defect was found.

## Originality — FAIL

The final topological statement is a direct corollary of the same primary paper's two advertised theorems plus Sierpiński's classical characterization. The source explicitly states both local Join Property on every nonempty relatively basic subclass and countably infinite jump-inversion fibres for every Join-Property class. Applying the second statement locally and invoking Sierpiński requires no new nonstandard lemma, so lack of identical wording does not establish originality.

### Equivalent formulations

The dense/no-isolated formulation is equivalent to applying the published fibre theorem to every published local Join subclass.

### Broader coverage

The broader source theorem covers all targets and all local cylinders, dominating the degree-theoretic content needed here.

### Exact database or table

A database/table comparison is inapplicable; theorem-level implication is decisive.

### Claim versus prior implication

Under the required implication standard, this is covered even if Cintioli does not spell out the topological corollary.

**Checked sources.** https://arxiv.org/abs/2609.37480; Sierpiński 1920; Resultary semantic search

**Residual risks.** The source is extremely recent, but the rejection rests on direct implication from it, not a novelty search gap.

## Value — FAIL

Dense rational fibres are an attractive reformulation, but the mathematical work after the published local theorem and appendix is a standard countability/no-isolated-points observation followed by Sierpiński's theorem. Under the shared value bar, this is too routine to constitute a separate motivated gap.

**Checked sources.** Cintioli 2026; Sierpiński 1920

**Residual risks.** The corollary remains useful expository structure.

## Limitations

- The conclusion is restricted to extensions with the local Join Property.
- No effective or uniform homeomorphism with \(\mathbb Q\) is claimed.
- The rejection is implication-level coverage, not a correctness defect.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
