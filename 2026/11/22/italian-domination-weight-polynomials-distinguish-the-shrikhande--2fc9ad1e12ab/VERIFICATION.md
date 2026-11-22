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
# Reproduction

From this directory run `python3 verify_support.py`; it must print `SUPPORT_ENUMERATION_OK`. Compile the independent direct-labelling verifier with `c++ -O3 -std=c++17 verify_ternary.cpp -o verify_ternary` and run `./verify_ternary`; it must print `TERNARY_EXHAUSTION_OK`. Both codes use the standard library only.

The support method checks every one of 65,536 possible positive supports on each graph, counts compatible weight-labelled functions with binomial coefficients, separately classifies all four-cocliques, and compares the entire difference vector. The direct method independently checks all 43,046,721 three-label assignments for each graph. Their complete coefficient tables match. The analytic proof of the minimum and the exact sixteen-versus-twenty-four optimum classification is in RESULT.md.

These exact finite checks do not certify any infinite family or exhaust the entire historical literature. No independent mathematical audit has been carried out.
