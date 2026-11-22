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

# Reproduction and limits

Run `python3 verify_moving_max_plateaus.py` from the extracted package directory using Python 3 standard library only. The program exhaustively enumerates relative ranks of all needed observations for window lengths 1 through 4. On the reviewed run, it passed 368,046 complete rank permutations and 56 exact rational identities. No package download or external service is needed. The arbitrary-width and weak convergence parts follow from the mathematical proof, not from these finite computations. The checker does not independently verify historical novelty or statistical practical performance.
