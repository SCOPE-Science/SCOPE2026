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

# Verification scope

Run `python3 verify_pairs.py`. The program checks the exact coprime parametrization against direct testing of every unordered integer pair in five intervals for each parameter \(m=1,\ldots,8\). It also evaluates exact larger finite counts and confirms the predicted rational local factors. The leading asymptotic and \(O_m(X)\) remainder follow from the proof in `RESULT.md`, not from extrapolating the finite counts. No independent mathematical audit has been performed.

Selected actual output: for \(m=1,2,3,4,6\) at \(X=100000\), the exact edge counts were respectively 203931, 278380, 341416, 366033, 458604. For \(m=2\) and \(X=300\), the exact count was 348, agreeing with the OEIS A362931 entry \(300+2(348)=996\).
