# Review of the squarefree four-prime 3-near-perfect classification

## Correctness — PASS
Odd squarefree four-prime integers have divisor-sum ratio below two. For even integers the positivity and omitted-divisor inequalities reduce the prime supports to twelve pairs. Every one of the 15 proper divisors of a candidate is affine in the largest prime; all 455 triples per pair have strictly smaller constant term than the target, giving at most one exact rational prime candidate each. The supplied standard-library checker tests all 5,460 cases, confirms all actual identities and produces 51 integers and 60 unordered witness triples. A separate direct integer-and-divisor enumeration through 13,000 agrees exactly. The global exhaustiveness is proved by the rational-template reduction, not by the bounded scan.

## Originality — PASS within inspected evidence
The closest 2023 original paper on 2-near-perfect numbers (arXiv:2310.01305) concerns two deleted divisors, with principal two-prime-support classifications. The 2025 follow-up (arXiv:2508.06651) has its main results on two deleted divisors and two distinct primes, and Section 6.3 only lists eight initial three-omission examples. The accessible squarefree 2-near-perfect four-prime census likewise has two rather than three omissions, while a published three-deficient-perfect result concerns the opposite sign. A sequence search uncovered OEIS A341475, again with two omitted divisors. Neither the inspected full primary texts nor targeted equivalence searches presented a stronger theorem covering the 51-value and 60-triple result. Some indexed literature and older records were available only in partial form; an unindexed equivalent theorem remains possible.

## Mathematical value — PASS
The classification resolves a natural first finite-prime-support layer of the three-deleted-divisor generalization and provides all exact witnesses. The necessary upper bounds on the smaller primes and the complete 5,460-template reduction establish why the computation covers the infinite class. The result goes beyond isolated examples or a known-table recomputation. It does not classify non-squarefree integers or other prime-factor counts.

Self-review: passed. Independent audit: not yet performed.
