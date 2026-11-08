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
# Reproducibility of the three-period census

Run `python verify_source.py` and `python verify_dynamics.py` with Python 3. No third-party packages, external files, network access, or other dependencies are required. The two files are included alongside their captured exact stdout files.

The first program constructs the bivariate path-source coefficients, then independently enumerates admissible vertex colorings and records source multiplicities on 110 generalized-theta instances, covering 3,325,212 colorings. It also tests the equilateral closed formula for 49 parameter pairs. The second performs three actual synchronous Greenberg--Hastings updates on 1,025,946 initial states across 44 cores, checks that the only fixed state is zero, and enumerates four examples with attached trees. These reproducibility checks support, but do not replace, the unrestricted combinatorial proof.

The published general activity criteria do not by themselves certify novelty of this source-refined initial-state count. Priority beyond inspected literature remains qualified; independent audit has not been performed.
