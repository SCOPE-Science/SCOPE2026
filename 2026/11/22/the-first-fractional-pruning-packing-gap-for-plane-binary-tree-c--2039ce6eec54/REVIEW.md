# Scientific review

## Correctness — PASS

The specified channel removes a terminal leaf together with its parent and promotes its sibling in an ordered full binary tree. Its recursive shadow identity is proved by cases at the root. Every source shape, output shape and incidence for sizes one through six is enumerated in the attached data. Both verification programs independently reconstruct the source and output shapes and exact pruning shadows; their rational arithmetic checks the primal inequalities, dual inequalities, and matching objective for every length. Explicit codeword index sets have disjoint shadows, and integer feasibility combined with a fractional upper bound below the next integer proves all exact maxima. The observed six-node gap is \(205/13-15=10/13\). The proof concerns exactly this finite domain and channel. No floating-point result or sampling assertion is used as a proof.

## Originality — PASS, with residual historical risk

The closest source-specific tree-edit literature [1] studies leaf-labelled phylogenetic distances; it cannot imply the cardinality of deletion-correcting sets on unlabelled ordered tree shapes. Hypergraph fractional optimization for strings in [2] supplies the abstract technique but not this shape incidence matrix or its sharp values. Binary-tree grammar compression in [3] does not correct an unknown pruning. Related results for matched-parenthesis-pair erasure or single-character deletion of Dyck words concern different channels; arbitrary matched-pair deletion can remove an internal node whose children are both nonleaf, while this channel can only remove a node incident to a leaf. Thus exact code sizes in those problems do not imply the claim. The primary papers and their relevant model/result sections were inspected and no corresponding exact table or \(205/13\) certificate was identified. Search coverage is finite: alternate terminology, older dissertations, and unindexed examples remain priority risks, so no absolute novelty guarantee is made.

## Mathematical value — PASS

Rooted ordered binary trees are the elementary shapes underlying full binary expression trees and abstract syntax structures. Recovering an unlabelled tree after one unknown elementary leaf pruning is a natural combinatorial zero-error problem. Exact optima through the first fractional-relaxation failure give a complete finite benchmark and show that a standard and useful optimization relaxation is not always tight even though rounding still gives the correct answer. The specific six-node boundary is motivated by the earliest observed breakdown of all smaller exact equalities rather than an arbitrary isolated slice. It does not purport to settle asymptotic capacity or practical parsing-channel performance.

## Verification, sources, and limits

Run `python3 verify.py` and `python3 alternate_verify.py` next to `certificates.json`. All three artifacts are complete and included. The first verification reconstructs prefix encodings; the second uses independent bottom-up shape decomposition. Both compare their own deletion incidences to the complete data and check the exact rational inequalities and exhibited codebooks. Bibliographic comparisons include Koperwas–Walczak (2011), Kulkarni–Kiyavash (2012), and Zhang–Yang–Kieffer (2013). These establish context, not a claim of scientific priority. Independent mathematical audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
