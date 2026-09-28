# Independent audit — SCOPE-20260910-016

## Scope
Independent review of `2026/09/10/016` at Git tree `53a2c8e8f58d2f62ba18f9bda5831f56228837fe` for task `20cb4fb0f42f361f7a14d25d084c5c02`. The current `main` tree matched the assigned source snapshot, so the scientific assessment used the assigned package without a stale-tree substitution.

## Correctness
**EXACT_DATUM_PASS_ASYMPTOTIC_INTERPRETATION_UNPROVED**

Independent parsing of baselines.json verifies G has 574 distinct triples, H has 621, both are linear, their intersection has size 9, their symmetric difference is 1177, and their defects from 651 are 77 and 30.

An independent Pasch census gives zero for both families; since every Fano plane contains a Pasch configuration, this certifies Fano-freeness of the archived pair.

The finite pair is therefore correct. It does not, however, refute an asymptotic o(n^2)-stability statement by itself; RESULT.md appropriately admits that no infinite-sequence theorem is proved, while some slogan/title language still invites an overly strong 'non-stability' reading.

The committed reproduction commands use output/artifacts/... although the repository stores these files under artifacts/....

## Originality
**FAIL**

Grannell et al. proved anti-Pasch STS(v) exist for every admissible v except 7 and 13, so a full anti-Pasch STS(63) with all 651 triples is already known to exist.

Given any such STS(63), a uniformly relabeled copy has expected intersection 651^2/C(63,3)=651/61≈10.672 with the original. Hence some relabeling has intersection at most 10, producing two co-located full anti-Pasch (therefore Fano-free) STS(63) with symmetric difference at least 2*651-20=1282 and zero defect—strictly stronger than the archived 1177-distance, positive-defect pair.

Classical STS intersection literature goes further and explicitly studies systems with tiny prescribed intersections. The record's finite separation is therefore subsumed by older design theory.

## Scientific value
**FAIL**

The exact archived pair is weaker than an elementary consequence of known anti-Pasch existence plus random relabeling, and one fixed order cannot establish the asymptotic non-stability target that would be scientifically substantive.

The Bose-retention and flag statistics are descriptive properties of one construction; they do not overcome the stronger pre-existing existence result or supply an infinite family theorem.

## Reproducibility
Status: **reproduced_independently_with_committed_path_defect**.
- baselines.json independently checked: 574/621 unique triples, linearity, intersection 9, symmetric difference 1177, defects 77/30.
- Independent Pasch census returns 0 for both archived families.
- Known-existence comparison quantified exactly: C(63,3)=39711 and expected relabeled intersection=651/61.
- Limitation: Repository reproduction commands in RESULT.md and paths in METADATA.json use output/artifacts although the committed files are under artifacts/.

## Literature checked
- [The resolution of the anti-Pasch conjecture](https://onlinelibrary.wiley.com/doi/10.1002/1520-6610(2000)8:4%3C300::AID-JCD7%3E3.0.CO;2-R): Proves anti-Pasch STS(v) exists for every v≡1 or 3 mod 6 except v=7,13; in particular a full anti-Pasch STS(63) exists.
- [Construction of Steiner Triple Systems Having Exactly One Triple in Common](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/construction-of-steiner-triple-systems-having-exactly-one-triple-in-common/3FD7C8A74086DABC9761A959A6215FB8): Classical literature directly studies co-located Steiner triple systems with very small intersections, showing that large symmetric differences are not a new design-theoretic phenomenon.
- [The 3-way flower intersection problem for Steiner triple systems](https://arxiv.org/abs/1908.06679): Modern intersection-spectrum work further demonstrates that prescribed intersections among STSs are a developed classical topic.

## Limitations
- The archived finite pair remains a valid reproducible construction; relocation is because its claimed research contribution is subsumed and does not prove the asymptotic target.

## Conclusion
The package is scientifically **failed** under the three-axis audit because at least one required axis fails. Relocate the complete original package atomically to the assigned failed path, preserving all original evidence. The relocation is a publication-status decision, not a claim that every underlying computation is false.
