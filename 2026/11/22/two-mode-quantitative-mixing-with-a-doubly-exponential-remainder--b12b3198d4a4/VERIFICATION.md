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

# Reproducible checks

Run `python3 verify.py`. It uses only Python standard-library `fractions.Fraction` and enumerates 340 elementary dyadic cylinders at depths two, four, six and eight. It checks the exact cylinder-transfer mass, resolution halving, preservation of constants and the \(1/2\) bit eigenmode. For \(\varphi(x)=x\), it computes the first four rational approximants to the asymptotic coefficient, through depth 16, obtaining \(c_4=38745189/134217728\) and the rigorous analytic enclosure \(38483045/134217728<\Lambda(x)<39007333/134217728\).

The checker does not inspect an infinite set of cylinders, certify the source's full measure-theoretic construction, or prove the asymptotic theorem by brute force. The full proof relies on the published exact-cylinder identity, dyadic cell approximation, \(L^1\) contraction and a proved summable tail bound, as written in `RESULT.md`.
