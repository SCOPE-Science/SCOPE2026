---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PASS: The actual N_4(F_q) coordinate calculation gives u=aB-bA, v=bC-cB and central t=aE+dC-Ae-Dc. Conditioning on (b,B), the projected fiber is q^2(q^2-1)+q^4 1_{(u,v)=0}. The top equation has q^5 extensions per t except q^2 exceptional outer sextuples, where only t=0 admits q^6 extensions. This proves all three claimed fiber sizes for every finite field, including characteristic 2; the weighted sum is q^12. Fresh independent direct enumeration of all 4,096 pairs at q=2 and all 531,441 at q=3 reproduced every target count. The finite tests corroborate but do not establish the field-uniform theorem.

## originality

FAIL

FAIL: A published 2026-10-12 full theorem explicitly gives exactly the same additive associative commutator on the same 4-by-4 strictly upper-triangular algebra over every prime-power field, with the identical zero, nonzero central, and noncentral target fiber formulas. All claimed features, including image, twice-central effect, and commuting probability, are already proved. The later group-word theorem is a separate related map, not the decisive proof of coverage.

## value

FAIL

FAIL as an independent research contribution: the exact natural invariant is already established, and the current submission adds no distinct theorem, new parameter, stronger coverage, or mathematically meaningful precision beyond the earlier full three-fiber theorem. Correctness and a different projected-count proof do not rescue a covered claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
