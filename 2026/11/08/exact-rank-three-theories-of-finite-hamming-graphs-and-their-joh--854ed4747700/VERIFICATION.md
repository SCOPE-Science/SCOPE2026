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

# Verification and limitations

The accompanying `checker.py` uses only the Python standard library. Run `python3 checker.py` from a directory containing the script. In the present execution the output began:

`RANK_THREE_HAMMING_CHECKS_OK direct_graph_checks= 116 classes= 8`

The checker constructs actual adjacency graphs for Hamming and Johnson parameters within its size cutoff, computes ordered-pair four-bit extension masks and compares them against independently coded counting formulas. It tests distinctness of all eight analytic Hamming profiles and both Johnson comparison families on selected parameters. No randomness or external datasets are used.

Finite program execution does not prove statements for all positive integer parameters, or prove historical originality. Uniform correctness instead relies on the explicit three-round game lemma, exact common-neighbor identities, strict positivity inequalities, and binomial estimates given in `RESULT.md`. No proof-assistant formalization, expert validation, or independent mathematical audit has been undertaken.
