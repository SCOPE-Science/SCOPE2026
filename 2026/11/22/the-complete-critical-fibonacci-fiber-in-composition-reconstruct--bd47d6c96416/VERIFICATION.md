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

# Verification

Run `python3 check.py` in this directory. The Python standard-library program enumerates every composition of source weight \(3k\) for \(1\le k\le5\), computes exact distinct deletion sets and verifies the claimed inverse fiber. It separately tests shortest-unembeddable weights for the displayed family through \(k=13\) and explicit two-zero-gap witnesses through \(k=8\). Expected final line: `VERIFY_OK`. These are finite corroborations only; the all-parameter proof appears in RESULT.md. Independent external checks have not been performed.
