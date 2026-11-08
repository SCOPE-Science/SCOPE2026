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

# Reproducibility checks

From the directory containing these files, execute `python3 verify_ring.py` with an ordinary Python 3 interpreter. No external packages, internet services or downloaded data are required. The verifier enumerates every A/R/L configuration for all ring sizes 3 through 8. For each configuration it independently constructs the set of type-dependent cohesive subsets by testing the exact local neighbor conditions and searches for two disjoint cohesive subsets; this is compared with the cyclic R-to-L transition statement. It compares exact rational probabilities for two different type probability triples with the closed formula. It separately enumerates all A/T configurations of sizes 3 through 9 and tests the four-median boundary by the same subset enumeration. It prints `ALL CHECKS PASSED 10844 exact network-type configurations` on success.

These are finite corroborating checks. The analytic steps giving validity for every cycle size are in `RESULT.md`. The cited Cheng–Mei consensus theorem is used as a known theorem; its original proof is not replicated by this local verifier. Asymptotics are justified analytically by exponential and binomial limits. This package does not contain any independent scientific audit or externally certified validation.

The exact distribution of all R-to-L switch counts is checked against full independent weighted type enumeration for two rational parameter triples at every tested strict-ring size. Closed communicating classes are computed by graph reachability, without using the count formula.
