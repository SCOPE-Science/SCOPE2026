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

## Reproducibility
Run `python3 verify_character.py` with a standard Python 3 interpreter. The program constructs the exact graph, six distance-four triples, all \(4095\) simplices, all \(216\) graph automorphisms, the full degree-five character by two independent methods, and the primitive fixed integral class. It uses no external files and no third-party modules.

The executed run produced the output embedded as `verification_output.txt`. The computation of the group is exhaustive over all distance-compatible partial injections; it is not a sampling estimate. Signed Lefschetz traces agree with the separate join-tensor formula for every element. The integer orbit-sum calculation gives exactly forty-two unit coefficients after dividing by twelve, and each enumerated automorphism fixes the resulting primitive vector.

## Proof responsibilities and limits
The abstract join decomposition and tensor sign follow from the six exact distance-four classes and the integral join homology formula. The certificate validates finite data and character calculations, while the theoretical group-averaging and rational quotient arguments are standard mathematical deductions. This result does not calculate torsion in the quotient or verify publication priority exhaustively. Independent validation has not been performed.
