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

# Verification scope
The symbolic proof counts every prescribed output in the cube ideal for every finite field. Matrix-coordinate multiplication is the only nontrivial computational identity, and the degenerate-functional and output-zero quadruple counts are explicitly reconstructed in RESULT.md. The five finite fields in CHECKER_OUTPUT.txt test an independent implementation and all target triples in each field. The runner invokes `python CHECKER.py` with no external package dependencies. The characteristic-three group conclusion follows from the ordinary binomial expansion of the single element `I+X`; it is not asserted for other characteristics. Historical-priority uncertainty and the absence of independent validation remain.
