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
# Reproducibility and scope

Run `python check_spieker.py` after installing `requirements.txt`. Expected marker: `SPIEKER_WEBER_COINCIDENCE_OK`. The program derives \(G'(h)\) by exact symbolic differentiation, checks all one hundred adjacent rational subintervals of \([7/10,4/5]\) using directed outward-rounded 50-digit interval arithmetic, verifies endpoint signs, and independently integrates the boundary-distance derivative on three sides at four heights. The interval proof is finite but covers a continuum because each interval enclosure bounds every input in the interval. Numerical root approximations are descriptive. The checker does not inspect or certify results beyond the displayed interval; no independent expert or formal proof assessment has been performed.
