# Independent audit — 2026-09-22

**Disposition: FAILED ATTEMPT.** Recovery verification performed 2026-09-23 UTC against public `main` head `dcdc9e9b990eef6d712e3a1e18d83b7f50e21bfb`. The assigned source directory still has exact tree SHA `7efe6d8a5e7ed7028a62c4f809f28daab1bb9391`, matching the assignment guard. RESULT.md blob: `8bbd0ad4a2ee9a3faf51c505f8fc5bf2841c0feb`.

## Claim reviewed
Gap-frequency spectrum modulo 30030. This audit preserves reproducible finite computations where supported while evaluating correctness, originality, and scientific value separately.

## Correctness
PASS. Independent gcd and sieve enumeration reproduced the 5760 totatives, the full cyclic gap histogram, both moment identities, the missing gap 20, maximum gap 22, and the two maximum-gap starting positions. The current source tree is unchanged.

## Originality
NARROW/FAIL AS A RESEARCH CLAIM. Prior public sources already record the occurring-gap set, the maximal gap 22 and extremal witness information at this primorial. The only residual distinction is the exact multiplicity histogram for one 5760-element period, which follows routinely from enumerating the reduced residue system.

## Scientific value
FAIL. A single small primorial histogram is a routine finite enumeration and yields no new theorem on Jacobsthal gaps, frequency recurrences, asymptotics, or primorial-to-primorial structure. The exact tally is reproducible reference data, but it does not have enough transferable consequence to pass the value axis.

## Literature checked
- Mario Ziller, On differences between consecutive numbers coprime to primorials: https://arxiv.org/abs/2007.01808
- Mario Ziller and John F. Morack, Algorithmic concepts for the computation of Jacobsthal's function: https://arxiv.org/abs/1611.03310

The decisive disposition does not rely on an inaccessible source; the cited open/DOI literature was sufficient to assess the relevant coverage and value.

## Bounded repair assessment
A bounded repair can explicitly call the result a one-period reference histogram and remove novelty over known maxima/witnesses. That leaves the same value deficit; a scientific repair would need a nontrivial recurrence, theorem, or general frequency law.

## Final disposition
The record fails the independent three-axis gate because at least one of originality/scientific value does not pass after established results and the record's finite scope are accounted for. The complete package should be preserved and archived as a failed attempt rather than represented as a validated finding. This does not erase reproducible finite computations.

## Reproducibility / provenance
Inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`; current checked head `dcdc9e9b990eef6d712e3a1e18d83b7f50e21bfb`; source tree `7efe6d8a5e7ed7028a62c4f809f28daab1bb9391`. Existing historical AUDIT/REVIEW evidence is preserved. Lean verification and expert attestation are not changed by this audit.
