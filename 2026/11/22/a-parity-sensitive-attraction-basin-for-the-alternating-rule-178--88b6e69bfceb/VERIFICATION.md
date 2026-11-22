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

Run `python3 verify_rule178_basin.py` from the directory containing the checker. The program independently constructs the full functional graph for every path length from three through eighteen, identifies which states flow into the fully alternating two-cycle, and compares those basins with the claimed explicit run criterion for every one of 524,280 finite labelled states. The program separately uses an integer recurrence for the rational generating function and checks its Lucas/Fibonacci parity formulas through length 100. The supplied `verification_output.txt` records the outputs from the actual execution and concludes `ALL_RUN_BASIN_CHECKS_PASSED`.

The unrestricted-length correctness rests on the written wall-persistence, run-erosion and symbolic enumeration proof; exhaustive checks do not establish infinitely many cases. The primary literature establishes the total primitive-attractor count and the worst transient, but no full historical-priority or independent audit is asserted. The proof does not address basins of the other two-cycles or boundaries other than zero.
