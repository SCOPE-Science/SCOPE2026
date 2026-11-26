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

A zero leaf would require its sole neighbor to be simultaneously zero for restraint and two for domination. With all leaves positive, the core zero set must induce no isolates. At a positive core, both it and its leaf can take either positive label, independently. At a zero core, the leaf can take either positive label if the core borders a positive core, and must take two otherwise. These factors give the full polynomial, with a unique least-weight term per zero set. For a path with r nonempty zero-core runs and h occupied-complement end runs, b=2r-2+h and n>=3r-1+h. Saturation gives precisely the stated choices: (k,1) at n=3k, (k,2) at 3k+1, and (k+1,0) or (k,2) at 3k+2, the last with one free extra site. Directly, P_1 has one optimizer and P_2 has two. On a proper cyclic zero set, b=2r and n>=3r; distributing n-3k extra sites over 2k alternating runs and marking a start gives the factor n/k and all three residues. The claimed extremal equality requires the complement to consist of a single universal vertex and the induced deletion to have no isolates, and both example families check. The frozen verifier and verification notes were inspected, not executed; the decision rests on the general proof.

## originality

FAIL

A distinct indexed record explicitly states the same universal labeled weight enumerator and optimizer identities, plus the same sunlet optimum census in binomial form. This is demonstrable overlap of the frozen central finding, not an inference of publication priority from dates. The comb residue formula is not printed there, but evaluates the already-established optimizer statistic by a short endpoint run count; it does not save the frozen broad novelty claim.

## value

FAIL

The universal labeled-function enumerator is useful mathematics, but it is already in the indexed record. The distinct comb expression is an elementary endpoint case split of that optimizer formula: at maximum there is at most one surplus position to place, and the two short exceptional paths are immediate. The record supplies no further substantive comb invariant that would make this narrow remainder a worthwhile standalone repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
