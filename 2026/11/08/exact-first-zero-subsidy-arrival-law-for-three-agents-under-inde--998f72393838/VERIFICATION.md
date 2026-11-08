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

# Reproducibility and mathematical verification

Run `python3 check.py` with Python 3's standard library. It exhaustively enumerates strict rankings of three agents among three through six houses, up to a common permutation of house labels, and checks both direct triple-subset feasibility and collision elimination, together with the exact distribution of deletion depth.

For \(m=6\), this checks \((6!)^2=518400\) reduced preference triples, which represents all \((6!)^3\) labeled triples modulo house-label relabeling. The analytic proof establishes all \(m\ge3\); the checker tests only finite cases and does not independently prove the infinite product, the gamma limit, or novelty.

Inputs: none. Network and third-party packages: none. Expected exact infeasibility fractions at \(m=3,4,5,6\): \(7/9,35/72,91/360,91/810\).

Scientific integrity: full appendix-level access to the 2026 motivating preprint was not obtained and exact publication priority is not independently established. Independent scientific audit has not been performed.
