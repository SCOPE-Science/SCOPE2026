# Scientific review

**Correctness — PASS.** This result concerns binary length-eight and length-nine words under exactly two deletions and list size two. The complete 199-node branching certificate has 100 disjoint leaves, with each leaf either directly infeasible or equipped with rational nonnegative dual multipliers. All inequalities and parent-incidence constraints are reconstructed and checked exactly by a standard-library verifier. The two explicit codes are checked on all possible received subsequences; common-prefix extension proves the minimum-length assertion. No finite experiment is offered as a substitute for the complete certificate.

**Originality — PASS against accessible literature, with priority risk.** Lin (2026) analyzes the full deletion-list hypergraph and proves asymptotic lower bounds, but the inspected full text gives no exact length-eight bound. Guruswami and Håstad (2020) describe an asymptotic two-list construction; the primary arXiv PDF was accessed, with Section 4 and the main theorems inspected. The closest indexed exact record addresses length six, not length eight, and does not imply the exact value here. Equivalence, broader coverage and exact numerical value queries found no direct stronger statement. An unindexed independent finite table remains a priority risk.

**Value — PASS.** The least binary length permitting sixteen messages with worst-case two deletions and at most two candidate parents is a natural coding threshold. Establishing that eight bits fail while nine suffice is an exact, nontrivial finite cutoff with a portable, independent-of-solver rational certificate and explicit witnesses. This is not a universal code family or an efficient decoding algorithm.

Self-review: passed. Independent audit: not yet performed.
