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
# Verification instructions and boundaries

Run `python3 verify.py` with Python 3.9+ in a directory containing that script. This is a standalone standard-library checker; no downloaded data, network calls, external packages, or generated certificates are needed. Expected terminal marker: `NO_MONOCHROMATIC_TRIPLE_SHATTERING_PASS`.

The checker constructs admissible words directly from their forbidden length-three factors, enumerates every coordinate support of lengths \(0\) through \(15\), and independently checks the full labeling trace size, the proposed structural criterion, and the recurrence-derived coefficient sequence. It also checks the two-hole bridge boundary cases and the fixed-background packing bound through length ten. The computational test is finite. The published mathematical proof in `RESULT.md` is what establishes the all-length assertions; the checker does not certify an infinite theorem by finite enumeration.

No external audit has been performed.
