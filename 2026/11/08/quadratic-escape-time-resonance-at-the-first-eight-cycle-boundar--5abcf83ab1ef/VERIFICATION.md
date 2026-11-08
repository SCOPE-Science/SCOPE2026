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

Proof-critical steps: the two hole endpoints generate a prime eight-orbit; the eight safe cells have lengths proportional to \((3,2,1,1,1,1,2,3)\). Every image endpoint belongs to the same finite orbit, so the eight-cell source-to-target transition matrix is exact. The formal identity \(G(z)=\mathbf1^\mathsf T(I-zB)^{-1}\ell\) counts all initial safe itineraries with the factor \(2^{-(n-1)}\). The eight explicitly displayed vector components solve the linear system; coefficient extraction gives the exact all-integer formula.

Run with `python verify_escape17.py` (Python 3 and SymPy required). Observed output: `VERIFY_OK exact_markov_cells=8 symbolic_generating_identity=1 independent_inverse_horizons=15 four_cycle_comparison=1`. The inverse-image implementation is algorithmically independent of the matrix recurrence. Its first fifteen cases are consistency evidence only; the generating-function proof is the exhaustive certificate for all horizons.

Scope limits: the hole is open, endpoints have zero Lebesgue mass, the discontinuity belongs to the hole, the initial distribution is Lebesgue, and no other hole parameters are covered. This verification is not an independent audit or a claim of historical priority.
