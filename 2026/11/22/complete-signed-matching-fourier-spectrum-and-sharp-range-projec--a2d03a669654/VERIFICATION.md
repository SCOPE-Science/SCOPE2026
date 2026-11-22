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

# Reproduction of the exact finite calculation

Execute `python3 mcgee_verify.py` with Python 3.10 or newer and no third-party packages. The program reads no external data and constructs its own McGee graph from the LCF shifts \((-12,7,-7)^8\). It checks the \(36\) edges, degree three at every vertex, connectedness and girth seven. The least-uncovered-vertex recursion generates exactly \(60\) perfect matchings; a separately memoized signed matching recurrence checks all \(8192\) cotree signings against a direct integer Walsh transform of the enumerated incidence profiles.

The verifier then compares all nine absolute multiplier multiplicities, computes the exact full rank and nullity using the \(2^{23}\) cut-space multiplicity, checks the sharp nonzero gap, and verifies that the second Walsh transform of the nonzero-frequency indicator has absolute coefficient sum \(120192\), giving the exact projection norm \(939/64\). It checks the support size \(2412\) and all \(630\) two-edge frequencies, recovering exactly \(128\) zeros and none at weight one.

The logical completeness argument is contained in the matching recursion and the spanning-tree gauge normalization, not in a randomized sample. The unrestricted projection optimum follows separately from translation averaging. The verification uses exact Python integers and rational arithmetic. It does not certify publication priority or constitute independent mathematical review.
