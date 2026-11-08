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
# Exact computational checks

From the directory containing the extracted files, run `python3 verify.py` (Python 3 standard library). The program builds the 16-state transition matrices from the explicit five-neighbor Boolean rule, recomputes their integer characteristic polynomials using Newton identities, and checks the claimed factorizations exactly. It compares 384 integer trace powers against the closed formulas. It also brute-forces 8,190 cyclic input states across lengths 1–12 and 65,536 length-16 inputs against the alternating target; all eight length-16 preimages are checked for primitive period 16.

The checked output is `VERIFY_OK exact_charpolys=3 trace_powers=384 bruteforce_ring_states=8190 alternating_N16_preimages=8`. Finite brute force is a supporting regression check, not an infinite proof; the all-length argument uses the exactly reconstructed finite characteristic polynomials and closed-walk bijections. No external review or independent verification has been performed.
