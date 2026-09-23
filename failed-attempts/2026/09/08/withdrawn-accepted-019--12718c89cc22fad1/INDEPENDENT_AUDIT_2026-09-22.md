# Independent audit — 2026-09-22

**Disposition: FAILED ATTEMPT.** Recovery verification performed 2026-09-23 UTC against public `main` head `dcdc9e9b990eef6d712e3a1e18d83b7f50e21bfb`. The assigned source directory still has exact tree SHA `6df859d2ca51016e709d00b9c82a636d41b79ca9`, matching the assignment guard. RESULT.md blob: `15e96f593f0375f03a5253b9947f0ae9ce008429`.

## Claim reviewed
The commutator-square quotient of T(3,4,5). This audit preserves reproducible finite computations where supported while evaluating correctness, originality, and scientific value separately.

## Correctness
PASS WITH CERTIFICATE CAVEAT. The explicit A6 generators give a valid surjection satisfying orders 3,4,5 and commutator order 2. The stored closed Todd–Coxeter table was independently replayed in the prior audit and supported the matching 360 upper bound, yielding the claimed finite identification within the certificate model. The source tree is unchanged.

## Originality
FAIL / NOT ESTABLISHED. The earlier independent audit found pre-existing public triangle-group/A6 data covering the same (3,4,5) quotient/generators-index phenomenon, so the record cannot claim priority from targeted exact-presentation searches alone. Even setting that overlap aside, the record supplies a single isolated quotient rather than a new family or criterion.

## Scientific value
FAIL. The surviving result is one small-group identification of an isolated extra-relator quotient, with no general collapse criterion, classification, algorithmic improvement, or downstream theorem. Once the A6 quotient is known, the additional structural census is routine finite-group data.

## Literature checked
- Caprace–Conder–Kaluba–Witzel, Hyperbolic generalized triangle groups, property (T) and finite simple quotients: https://arxiv.org/abs/2011.09276
- Larsen–Lubotzky–Marion, Deformation theory and finite simple quotients of triangle groups I: https://arxiv.org/abs/1301.2949

The decisive disposition does not rely on an inaccessible source; the cited open/DOI literature was sufficient to assess the relevant coverage and value.

## Bounded repair assessment
A bounded wording repair can remove priority language and present the calculation as a reproducible example, but that does not create a new general theorem. A meaningful repair would require a new collapse criterion, family classification, or demonstrably new structural consequence.

## Final disposition
The record fails the independent three-axis gate because at least one of originality/scientific value does not pass after established results and the record's finite scope are accounted for. The complete package should be preserved and archived as a failed attempt rather than represented as a validated finding. This does not erase reproducible finite computations.

## Reproducibility / provenance
Inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`; current checked head `dcdc9e9b990eef6d712e3a1e18d83b7f50e21bfb`; source tree `6df859d2ca51016e709d00b9c82a636d41b79ca9`. Existing historical AUDIT/REVIEW evidence is preserved. Lean verification and expert attestation are not changed by this audit.
