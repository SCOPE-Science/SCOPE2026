---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and mathematical limits

Run `python3 verify.py` in the directory containing this file and the program. The program constructs the oriented tournament through forbidden cyclic triples, enumerates all simplices, calculates reduced mod-two Betti ranks by independent bitset elimination, and calculates the signed simplicial Lefschetz number under vertex-label reflection. It checks the twelve pairs of center size 1–3 and nested-pair count 1–4. Expected line: `PASS: 12 independent face/enumeration, reduced homology, and signed reflection Lefschetz checks`.

Those checks are finite only and do not prove the formula for arbitrary parameters or the exact integral action. Those conclusions are supported by the exhaustive structural simplicial decomposition, integral suspension recurrence, and orientation-sign proof in `RESULT.md`. The rational quotient calculation uses finite-group averaging; no full integral quotient computation was performed. No independent audit was performed.
