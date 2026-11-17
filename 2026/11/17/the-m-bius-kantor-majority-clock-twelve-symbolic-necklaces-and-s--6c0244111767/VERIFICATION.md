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

# Verification record

Run `python3 verify_shores.py` and `python3 verify_full.py` with Python 3 and its standard library. The programs are standalone, present in the same package, and contain the complete definitions they check.

`verify_shores.py` evaluates all \(256\) eight-bit words using the Boolean majority polynomial, verifies the full-power identities and the \(72\) stable symbols, derives the \(12\) rotational classes and all retraction fiber weights, and checks the resulting exact orbit, basin, and entrance-time counts. The recorded successful stdout is `verify_shores_output.txt`.

`verify_full.py` independently constructs the sixteen-node LCF graph from edges and updates all \(65{,}536\) complete labelled configurations. It checks the universal three-step bound, an explicit sharpness witness, both eventual-period populations, the full first-entry-time table, and the attraction-basin distribution without using the shore-map formulas. The recorded successful stdout is `verify_full_output.txt`.

These exhaustive finite tests support the exact claim for the defined finite graph; they do not establish any statement on graph families or an independent audit. The original Goles–Olivos full text was not available for full historical-priority comparison.
