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
Run `python3 verify.py` with Python 3.10 or newer. Compare standard output with `expected_output.txt`. The program reconstructs all relative faces and checks that a sequential vertex-toggle matching leaves exactly the expected critical four-faces for all \(3\le n\le12\) and all diagonal positions. The infinite proof, including the integral connecting map, is in `RESULT.md`; bounded enumeration is not an infinite certification. Independent mathematical audit is not performed.
