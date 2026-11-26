---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independent bounded reproduction: run python3 /workspace/branches/reproduce-4.py. Enumerate all 2^10 spoke subsets; after their endpoints are removed, the remaining graph consists of unbroken cycles or paths cut from the outer decagon and two inner pentagons. An odd path or odd cycle has no perfect matching, an even path has one, and an even unbroken cycle has two. This exhausts and separates the 36 full matchings. For every deletion subset of each size 0–5, the bitwise union of edge incidence masks marks exactly the matchings destroyed; a one-bit complement gives the unique survivor. Examined respectively 1, 30, 435, 4060, 27405, 142506 subsets, with unique-survivor counts 0, 0, 0, 0, 240, 7272. The first size and its multiplicity, stratified by complement cycle lengths, are ((20),4,8):30 and ((5,5,10),5,22):6. Each minimum set is assigned to only one matching by uniqueness, so the class totals are 240 and 132. An adjacency-preserving permutation enumeration also gives 120 automorphisms and exactly those classes as the two orbits. The frozen scripts and their recorded outputs were inspected as separate evidence, not executed.

## originality

FAIL

Earlier distinct Resultary record 1922f6e21101 explicitly gives the same ordinary polynomial and the same 30/6 matching-orbit counts and 8/22 ordinary minimum-witness multiplicities on the same labelled graph. Its extra edge-disjoint results do not remove this ordinary overlap. The complementary-cycle labels are a descriptive refinement of the two already-known orbits, not a new polynomial or new witness counts. No equivalent historical-priority claim is made for any external paper not inspected.

## value

FAIL

This is a natural graph and invariant, but the main exact census is already available. The genuinely additional complement labels translate the two known orbit classes by an elementary invariant, checkable on representatives. The record does not use the labels to derive the witness counts structurally or solve a different open problem. The independent reproduction is useful confirmation, not a surviving new valuable mathematical finding; no repair is warranted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
