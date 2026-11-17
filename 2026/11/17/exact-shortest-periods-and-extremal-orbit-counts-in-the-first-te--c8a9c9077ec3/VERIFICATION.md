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

Run `python3 verify_periodic_systole.py` from the same directory. No additional dependencies are required. The program uses only exact integers and rational arithmetic. It reproduces the base cutoff, counts and primitive orbit histograms, directly differentiates all depth-ten extremal periodic orbits ten times, and independently brute-forces the low-depth minimum periods. On success it prints `CERTIFICATE_OK`.

The exact finite enumeration becomes a proof only together with the mathematical fact that inverse-run expansion has no missing primitive branches and increases a primitive periodic length by at least a factor of \(4/3\), so every depth-ten primitive period no greater than \(269\) descends to a depth-one period at most \(20\). It does not address higher-depth least periods or independent source-priority verification.
