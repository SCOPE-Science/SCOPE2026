# Independent audit — SCOPE-20260910-014

## Scope
Independent review of `2026/09/10/014` at Git tree `370ddef3fbeb415bd4a14111534bbb2533d59d26` for task `20cb4fb0f42f361f7a14d25d084c5c02`. The current `main` tree matched the assigned source snapshot, so the scientific assessment used the assigned package without a stale-tree substitution.

## Correctness
**PASS_WITH_REPRODUCIBILITY_PATH_DEFECT**

Independent enumeration of all 29,183 eleven-colored partitions of 6 exactly reproduces S(r;6)=[1894,5873,2728,949,253,49,6,1,11,78,426].

The hand proof is exhaustive: residue 6 can have positive s-weight only from c1-c2=6, forcing pi^(1)=[1^6] and contribution 6; residue 7 can have positive s-weight only from c1-c2=-4 with (c1,c2)=(1,5), forcing contribution 1.

Thus the stated non-equidistribution at the first progression term is correct. However RESULT.md tells readers to run output/artifacts/verify_target.py while the committed record contains artifacts/verify_target.py.

## Originality
**PASS_NARROW**

The closest located colored-partition statistic NB_k counts all parts of the first component by crank class, whereas this record weights only the multiplicity of the smallest part of the first component. The ordinary spt-crank literature uses different objects. No located source states the exact S(6;6)=6, S(7;6)=1 datum for this bespoke hybrid statistic.

This narrow originality finding is limited to the exact defined statistic; it is not evidence of a new modular-form phenomenon.

## Scientific value
**FAIL**

The headline is a first-index counterexample obtained directly from a newly assembled hybrid statistic. It does not produce an 11-dissection, modular identity, structural congruence theorem, or reusable result about an established spt-crank.

Because the statistic is not shown to have independent mathematical significance and the obstruction is forced at N=6 by two elementary cells, the result is better characterized as a target-definition diagnostic than a validated research contribution.

## Reproducibility
Status: **reproduced_independently_with_committed_path_defect**.
- Independent full N=6 enumeration reproduced 29,183 objects and the exact 11-entry row.
- Hand cell-budget proof independently checked.
- Limitation: The committed replay command in RESULT.md uses output/artifacts although the repository stores the verifier at artifacts/verify_target.py.

## Literature checked
- [Some identities on Lin-Peng-Toh's partition statistic of k-colored partitions](https://arxiv.org/abs/2308.05931): NB_k counts total parts of pi^(1) by k-colored crank class; it is related motivation but a different statistic from first-component smallest-part multiplicity.
- [Deviation of the rank and crank modulo 11](https://arxiv.org/abs/2305.08751): Develops 11-dissections for ordinary-partition rank/crank deviations and applications to spt; it does not supply the record's 11-colored hybrid statistic.
- [The spt-Crank for Ordinary Partitions](https://arxiv.org/abs/1308.3012): Defines/realizes the ordinary-partition spt-crank and explains mod 5 and 7 congruences; it is not this k-colored first-component statistic.
- [Cranks for Ramanujan-type congruences of k-colored partitions](https://arxiv.org/abs/2006.16195): Provides a general theta-block framework for colored-partition cranks; no located theorem turns the record's bespoke smallest-part slice into an established modular object.

## Limitations
- The exact N=6 computation is correct. Failure is on scientific value, not on the arithmetic identity.

## Conclusion
The package is scientifically **failed** under the three-axis audit because at least one required axis fails. Relocate the complete original package atomically to the assigned failed path, preserving all original evidence. The relocation is a publication-status decision, not a claim that every underlying computation is false.
