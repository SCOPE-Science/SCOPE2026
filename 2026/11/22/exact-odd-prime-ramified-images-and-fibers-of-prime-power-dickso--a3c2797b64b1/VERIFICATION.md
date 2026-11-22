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
# Verification and reproducibility

Execute `python3 check_dickson.py` using standard Python 3 without third-party packages. It computes Dickson integer polynomial coefficients directly, evaluates each iterate modulo \(p^k\), then compares exact full residue-frequency histograms against the predicted disjoint branch balls and multiplicities. Tested primes are \(5,7,11,13\), with the highest precisions respectively \(5^6,7^5,11^4,13^3\) and two or three iterate depths. It verifies the integer counts and additional least-period instances.

Actual output ends `PASS: exact tested input values 170481 ; metric assertions 4680`. All enumerations are finite diagnostics, not proofs for all \(p,r,k\). The rigorous unlimited quantifiers rest on the derivative/Taylor isometry argument in `RESULT.md`. The checker does not use an external theorem prover or provide independent audit. The applicability limits are \(p\ge5\), \(r,k\ge1\), first-kind Dickson parameter one; the exceptions \(p=2,3\), mixed degree, and general parameter values are not established.
