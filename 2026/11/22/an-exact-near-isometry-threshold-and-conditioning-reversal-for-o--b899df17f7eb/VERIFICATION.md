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

## Executed verification
`python verify.py` completed, using Python standard-library rational arithmetic only. The observed output was:

`PASS: 1260 exact rational characteristic-polynomial checks; 216-case triangle and 1296-case pendant-triangle enumerations`

The checks compare full characteristic polynomials of the compressed Gram operator to the two-root formulas, rather than comparing floating point eigenvalues. Independent exhaustive hash-and-sign enumeration checked two smallest relevant examples and their exact probabilities.

## Limits
These finite checks support the algebra and the counted examples, but the all-size statement depends on the circulation-hyperplane, rank-two compression and kernel dimension proofs. They are not a substitute for those arguments, nor an independent scientific audit. Prior literature may contain equivalent, unindexed special-purpose formulas.
