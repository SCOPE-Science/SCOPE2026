# Scientific audit — 2026-10-01

## Final claim

Genus-0 degree-7 fully general quasi-triple Hurwitz census H=24 with verified cut-join step

## Correctness — PASS

A fresh S7 reconstruction independently reproduced class sizes 630,280,105,21; with a fixed (4,2,1) representative it found 244 relation tuples, 192 transitive and 52 disconnected, split 28 of orbit type 1+6 and 24 of type 3+4. Thus N_all=153720, N_conn=120960 and H=24. The fused types and connected/disconnected counts reproduce 136=96+40 for (4,2,1), 36=24+12 for (2,2,1,1,1), and 72=72+0 for (3,2,2). Fresh enumeration verified class-constant cut numbers 2,3,3 and triple totals 42840,7560,15120, hence the cut-join identity. Finally, an independent BFS under the six pure-braid generators pure-braid square and inverse-square moves reached exactly all 120960 transitive tuples, validating the single pure-braid-orbit claim.

## Originality — PASS

Resultary returned this record as the only exact match. Chen's primary paper says the general three-nonsimple regime lacks explicit formulas and develops detailed explicit formulas for one-part quasi-triple cases; all three deterministic profiles here have at least three parts. No prior exact H=24 census, braid-orbit certificate, or fused cut-join table for these profiles was located. This is best-knowledge originality with residual risk from unindexed computational data.

## Scientific value — FAIL

Although the computation is richer than a bare count, the record still studies one hand-selected small passport with no proof that it is the first by degree, minimal, extremal, a complete classification boundary, or otherwise naturally distinguished. The H=24 value, one braid orbit, and one-step cut-join table are finite outputs of standard symmetric-group operations. Without a motivated reason that future work needs this particular passport or a complete finite cutoff that it settles, the instance remains an arbitrary slice under the stated value standard.

## Sources inspected

- **R. X.-F. Chen, Towards studying the structure of triple Hurwitz numbers** (https://arxiv.org/abs/2308.08455): BROADER_NOT_EXACT_COVERAGE. The paper gives a general symmetric-function description and detailed one-part formulas, not this exact three-multipart degree-7 census or braid orbit.

## Residual risks

- Absolute novelty cannot exclude unpublished computational tables.
- The value rejection is about motivation of the chosen finite instance, not correctness or reproducibility.

## Disposition

**failed** — at least one required scientific axis does not pass. The original scientific files are preserved unchanged as evidence.
