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

The theorem is established analytically in RESULT.md. The finite diagnostic script `run_spectrum_verifier.py` checks digit recurrence values, predicted change positions and the exact supports for each \(d=2,3,4,5,6,7,8\) on the first \(2^{18}\) positions. It computes all rational density formulas with exact `fractions.Fraction` arithmetic and checks the predicted moment and total run-start density. Each finite count differs from its asymptotic prediction by no more than two counts in the tested dyadic prefix.

Use: `python3 run_spectrum_verifier.py`. This is an ordinary standalone Python diagnostic without dependencies outside the standard library. It is not a proof of infinitely many cases and not an independent audit. The actual infinite proof is the derived carry identity, exact boundary classification, and 2-adic density calculation.

Caution: a *constant-letter run* is a maximal block of identical bits, distinct from a maximal repetition with arbitrary period. The preexisting upper bound on the longest run is credited rather than claimed as independently novel. The origin and citation data are scientific rather than claims of external certification.
