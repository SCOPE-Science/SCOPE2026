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

The edge ODE tested is \(\dot w_{ij}=(w_{ij}+n^{-1}(W^2)_{ij})(1-w_{ij})\), with \(w_{ii}=1\). The packaged `verify.py` builds the Taylor coefficient recurrence directly from this polynomial vector field using `fractions.Fraction`, and separately computes shortest-distance data and matrix powers from the initial weighted graph. These independent constructions compare the first nonzero coefficient and preceding zeros for every reachable ordered vertex pair; disconnected ordered pairs are checked to the available expansion order.

Run `python verify.py` using Python 3.9 or later. Observed output: `VERIFY_OK 4832 exact coefficient/vanishing/positivity identities`.

The universal conclusion additionally needs the analytical induction, the exact \(d-1\) geodesic-split count, component invariance, scalar comparison, and invertibility of a positive-leading-term function, as established in `RESULT.md`. The verifier is finite corroboration and does not establish every graph size or the publication novelty of the theorem. Independent external validation has not been performed.
