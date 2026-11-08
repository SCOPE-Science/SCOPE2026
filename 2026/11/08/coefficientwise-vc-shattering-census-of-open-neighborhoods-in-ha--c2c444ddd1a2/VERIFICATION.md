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

The standalone Python program `verify_hamming_open.py` constructs all Hamming words, evaluates every graph open neighborhood by literal coordinate distance one, and tests every Boolean trace on every support of sizes one through three for fourteen finite parameter choices. It also checks all four-point supports when the ground set has at most 27 vertices. The program independently compares each degree count and each of the three triple categories against the claimed formulas.

Command: `python3 verify_hamming_open.py`

Observed terminal line: `ALL_QARY_OPEN_HAMMING_SHATTERING_CHECKS_PASS`.

Selected exhaustive outputs: the open-neighborhood polynomial for \(H(2,4)\) has coefficient vector \((1,16,120,320)\), split as \((32,288,0)\) triple types; for \(H(3,3)\), the vector is \((1,27,243,216)\), with all \(216\) triples of type C; for \(H(4,2)\), the vector is \((1,16,48,64)\). No four-point support was shattered in any tested graph with at most 27 vertices.

The infinite-domain parameter claims are supported by the finite-coordinate structural proof in `RESULT.md`; finite checking alone would not establish them. No external or independent audit is asserted.
