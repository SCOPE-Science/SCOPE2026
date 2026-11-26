# Independent mathematical audit

## correctness

PASS

The concept family is the distinct translates of one fixed subset of a finite abelian group, not the union of all coset families. For a pair with difference d, traces 11 and 00 require d in A-A and in B-B, respectively; both mixed traces occur exactly when translation by d fails to stabilize A, because the two directed set differences have equal size. There are |G| ordered pairs per qualifying nonzero d; divide by two even when d has order two, since each unordered pair still corresponds to two distinct ordered pairs. Quotienting by the stabilizer preserves traces across distinct fibers while a pair within a fiber cannot be shattered. In the quotient every nonzero d has both mixed traces; the larger of the two parts has the entire difference set if its size is greater than half, and at equality the two overlap counts agree for every d. Thus if the other part has two distinct points there is a shattered pair. A singleton part pulls back to a coset or its complement, and coset partitions and their Boolean complements realize no shattered pair. Each coset determines its subgroup, and a coset can equal another subgroup's coset complement only in the index-two case, with the same subgroup; exactly two subsets are then counted twice. This proves the census and the cyclic divisor specialization. Least positive period n means trivial stabilizer; singleton and co-singleton sets give 2n distinct words for n>=3, coincide as classes at n=2 (two words), and both constant words count at n=1. Counting indexed words, not necklaces, is essential. Separate direct trace and census checks passed for all 8190 cyclic subsets through order twelve and the three abelian groups of order eight (counts 28, 48, 88). Replay: /workspace/branches/9b848638-bf6e-421b-8e58-27713b32bf36/audit_vc_translate_new.py and audit_full.log. These are bounded checks, not the general proof. Frozen verification artifacts were inspected, not executed; no formal or external attestation is asserted.

## originality

PASS

Credit only the supported distinct contribution: the exact zero-error classification and subgroup census uniformly over finite abelian groups, together with the pair-count statistic for arbitrary seeds. The cyclic classification and the derived cyclic word counts are mechanically recoverable from the periodic specialization of Johnson's low-VC analysis and elementary counting; they are not relied on as separate new theorems. No inspected source states or implies the general result or the arbitrary-seed statistic at the same level of specificity. The general classification is elementary and may occur under an unrecognized matrix or group-theoretic formulation.

## value

PASS

VC dimension one is the first nonconstant level, and giving its exact group-theoretic structure rather than approximate regularity is a natural complete classification. The general subgroup census distinguishes groups of the same order (e.g., 28, 48, and 88 qualifying subsets in the three abelian groups of order eight), and the exact pair statistic quantifies departures from the classification for every seed using differences and periods. This value does not rely on treating the cyclic specialization or divisor-sum inversion as a separate discovery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
