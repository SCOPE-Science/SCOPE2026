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

Reproduce finite checks by running `python3 verify.py` using Python 3 with no third-party dependencies.

Observed: `PASS 134418 finite exact/combinatorial and floating-point assertions`.

The finite test enumerates all simple labelled graphs with at most six vertices, checks the extremal inequality for every target length not exceeding the order, verifies sharp path constructions for lengths three through seventeen, and compares finite survival products with their asymptotic approximations. The analytic proof in RESULT.md is needed for arbitrarily large graphs and all fixed target lengths; finite checks alone cannot establish it. Independent audit has not been performed.
