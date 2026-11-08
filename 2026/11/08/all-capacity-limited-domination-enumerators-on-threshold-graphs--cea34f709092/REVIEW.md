# Self-review

## Correctness — PASS

The two disjoint apex-status cases give a bijective recurrence, and an isolated vertex is forced into every dominating set. In a clique bouquet, an omitted apex adds exactly one outside neighbor to each selected blade vertex; consequently each blade contributes an independently bounded omission count. Minimizing the two disjoint branch exponents gives both the exact optimum and the correct sum of multiplicities at the equality boundary. Substitution in the equal-blade case proves the phase transition. The extracted exact-integer verifier checks 1,991 complete heterogeneous bouquet/capacity enumerations, 5,405 universal-apex cases, 693 uniform parameter cases, and 4,608 threshold creation-string cases. Boundary cases \(k=1\), \(k=M-1\), unit blade size, and tied minima are covered. The finite tests are corroboration; the bijections prove arbitrary order.

## Originality — PASS, historically provisional

The motivating 2026 source defines the invariant and supplies a universal-vertex result for the scalar \(k=1\) minimum, which is explicitly not new here. The second 2026 paper proves hardness and Cartesian-product results, not the stated creation-string enumeration. Relevant indexed findings on complete multipartite limited domination, threshold-graph \(k\)-tuple total domination, and generalized windmill dissociation concern different adjacency classes or different invariants, so none implies the exact all-set polynomial or the phase-count formulas. Related \((0,k)\)-pitchfork terminology was included in searches. No identical or stronger covering result was found in the inspected material. Unindexed or inaccessible historical literature may alter priority.

## Mathematical value — PASS

Exact enumeration across every capacity is a strengthening beyond one optimum and yields a polynomial-time exact counting algorithm for the full threshold-graph class, against the motivating paper's general computational difficulty. The heterogeneous common-apex family produces an explicit coefficientwise polynomial and a meaningful classification of optimizer types. In uniform generalized windmills, optimizer multiplicities change from binomial-power growth to a constant-size plateau and then a global apex family, with a genuine mixed equality case. These distinctions are not implied by the published scalar universal-vertex bound.

## Scientific limitations and closest work

The structural recurrence is specific to isolate/universal graph construction, and the explicit minimum formulas apply only to common-apex clique unions. Božović et al.'s universal-vertex \(k=1\) scalar theorem is prior work. The nearest other work addresses Cartesian products or a distinct domination constraint. No external independent verification has been performed.

Self-review: passed. Independent audit: not yet performed.
