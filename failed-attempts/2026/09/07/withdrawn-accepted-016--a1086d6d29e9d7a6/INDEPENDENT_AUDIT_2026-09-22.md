# Independent audit — 2026-09-22 campaign

**Record:** SCOPE-20260907-016  
**Original source path:** `2026/09/07/016`  
**Audited repository state:** `1182b71328a408a740c274616869ab885009b620`  
**RESULT.md blob:** `78a82f644a6d733953498c21e94d16ada8217462`  
**Review date:** 2026-09-23 UTC  
**Reviewer:** separate AI independent audit; no Lean or expert attestation is claimed.

## Claim audited

The record enumerates multiplicity-free rank-5 fusion rings, obtaining 16 isomorphism types in total and seven with Frobenius–Perron dimension at most 12, all commutative, with exact dimension certificates.

## Correctness — PASS

The headline total of 16 multiplicity-one rank-5 fusion rings is consistent with the independent classification literature, and the record's Frobenius-reciprocity reduction, associativity identities and isomorphism quotient are mathematically standard and correctly stated. The seven displayed low-FP-dimension representatives have internally consistent exact dimensions and characteristic polynomials: pointed `C5` has dimension 5; the two Tambara–Yamagami examples have dimension 8; the two quadratic examples have `(17+sqrt(17))/2`; and the final pair has dimension 12. I found no mathematical contradiction in the stated subset or exclusion mechanism. The rejection does not rely on a correctness defect.

## Originality — FAIL

The underlying rank-5 multiplicity-one fusion-ring classification was already available before this record. Vercleyen and Slingerland, *On Low Rank Fusion Rings* (arXiv:2205.15637), explicitly describe an exhaustive generation method for fusion rings of fixed rank and multiplicity and publish low-rank lists. Liu, Palcoux and Ren, *Classification of Grothendieck rings of complex fusion categories of multiplicity one up to rank six* (arXiv:2010.10264; Lett. Math. Phys. 2022), classify multiplicity-one Grothendieck rings through rank six. Published low-rank count tables give 16 rank-5 multiplicity-one fusion-ring types, the same total obtained here.

Searches included `rank 5 multiplicity one fusion rings 16`, `multiplicity-free fusion rings rank 5 classification`, `Grothendieck rings multiplicity one rank five`, and the cited Vercleyen/Slingerland and Liu/Palcoux/Ren classifications. After this prior classification is subtracted, the `D<=12` filter is an elementary invariant-based selection from a known finite list rather than a new classification theorem.

## Scientific value — FAIL

A second integer-arithmetic enumerator is a useful software cross-check, but the scientific residual is a re-enumeration of a known 16-object classification plus a simple FP-dimension threshold. It does not add new categorifiability results, new fusion-ring families, a sharper classification range, or a method that changes the known frontier. That is insufficient for the validated-finding threshold.

## Repair assessment

No bounded correction yields a distinct new theorem without changing the record's identity. A genuinely new result would need, for example, a new rank/multiplicity regime, categorifiability classification, or structural theorem beyond the existing lists.

## Final disposition

**FAILED.** Correct-looking computation, but originality and value fail because the rank-5 multiplicity-one classification is already known.