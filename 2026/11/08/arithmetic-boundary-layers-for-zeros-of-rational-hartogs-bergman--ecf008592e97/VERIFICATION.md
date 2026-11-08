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

The theorem uses the Edholm–Mathew normalization \(Q_{m,n}(s)=s^{1-2n}P_{m,n}(s,s)\), with \(m=n+k\), \(k\) fixed, and \(\gcd(m,k)=1\). The exact finite coefficient representation and the original source formula agree on tested coprime grids. The general proof supplies a uniform \(O_k(m^{-2})\) coefficient error, an exact Fejér root-of-unity evaluation, and a local simple-root perturbation argument. This is what proves the all-sufficiently-large-parameter assertion; finite tests are not an exhaustive proof.

Run `python CHECK.py` after installing the dependency in `requirements.txt`. The saved script completed 1,544 finite assertions, including exact-integer coefficient identities, high-precision root-of-unity evaluations, and numerical root comparisons for several gaps. The bounds in the theorem depend on a fixed gap; the checker does not establish the implicit constants or settle variable-gap asymptotics. No independent audit was performed.
