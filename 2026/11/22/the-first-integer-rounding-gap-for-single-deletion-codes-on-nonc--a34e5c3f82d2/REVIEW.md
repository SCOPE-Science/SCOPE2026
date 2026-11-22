# Scientific review

## Correctness — PASS

The represented object is the class of canonical restricted-growth words with no alternating two-block quadruple, equivalent to noncrossing partitions. Every source and every single-position deletion is enumerated; deduplication of coincident outputs is explicit. The integer optimum is proved by an exhaustive branch-and-bound over the exact compatibility graph, with valid proper-color pruning and explicit attaining codes. The fractional optima follow from positive-integer-scaled primal and dual vectors satisfying every incidence inequality, with equal exact rational totals. `python3 verify.py` reads `certificate.json` and returns `VERIFY_OK`. The generalization to larger lengths is **not** proved.

## Originality — PASS, with residual priority risk

Jelínek–Mansour (arXiv:math/0703898) classifies partition patterns and Catalan classes, but its relevant full-text sections and finite tables do not give this deletion-packing invariant. Kulkarni–Kiyavash (arXiv:1211.3128) treats generic string deletion and fractional matching bounds, not this noncrossing set-partition observation channel. Gabrys et al. (2014) treats rank-relative permutation deletion. The geometric query-shattering criterion for noncrossing partitions tests independence of pair-equality queries, a different family of objects and constraints. An exact six-point capacity and fractional value for unrestricted set partitions neither gives a noncrossing optimum nor the restricted LP value; a Catalan-equinumerous permutation family uses a different deletion map. No scrutinized primary source or close indexed record implies the exact profile \((M_n,P_n)\) stated here. Historical priority remains qualified because equivalent unindexed tables may exist.

## Mathematical value — PASS

Noncrossing partitions are an intrinsic Catalan combinatorial class, closed under point deletion, making one-point erasure and exact recovery natural. The result identifies both the first fractional integrality gap at order five and the first strict **integer-rounded** capacity gap at order six. It differentiates the combinatorial deletion geometry of a Catalan source from that of arbitrary set partitions and pattern-avoiding permutations and supplies a reproducible exact benchmark for constrained deletion-channel LP relaxations. A finite precise cutoff, rather than a speculative asymptotic claim, is the warranted contribution.

## Boundaries and access risks

The proof is certificate-assisted finite enumeration through order six, not a general theorem for larger orders. Originality is assessed against indexed literature and technically comparable full-text primary sources, not the entire historical literature; independent review has not occurred. No unpublished additional claim is accepted.

Self-review: passed. Independent audit: not yet performed.
