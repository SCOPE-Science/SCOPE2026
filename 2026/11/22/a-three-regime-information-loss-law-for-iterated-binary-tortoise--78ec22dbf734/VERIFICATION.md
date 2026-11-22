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

# Verification evidence

Run `python3 verify_exact.py` in the extracted directory: the recursive implementation of the tortoise map reproduces all output fibers for every binary word of length up to 12 at every iteration depth from 0 through the input length. It checks 98,305 word/depth instances, including empty-word and fully sorted endpoints.

Run `python3 verify_probabilities.py` in the same directory: an independently coded composition-count spectrum verifies class multiplicities, total source mass, image counts, and maximum fiber size for every one of 5,050 parameter pairs with length 1 through 100, as well as entropy-rate trajectories at lengths 100, 200, 400 and 800.

The supplied `verify_exact.out` and `verify_probabilities.out` are the recorded standard output from the two exact programs. They can be regenerated without installing external packages.

These computations check finite identities only. Infinite-size concentration, normal-limit, critical positive-part-normal limit, and supercritical chi-square limit are established analytically in RESULT.md using the coupled binomial and negative-binomial variables and Stirling expansions. They have not been independently audited.
