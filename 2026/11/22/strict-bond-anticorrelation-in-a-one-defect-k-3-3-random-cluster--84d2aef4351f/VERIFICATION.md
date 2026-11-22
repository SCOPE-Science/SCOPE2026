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
# Verification record

The complete symbolic evidence consists of `CERTIFICATE.json` and the independent replay instructions in `verify.py`. Run `python verify.py CERTIFICATE.json` from the same directory. Exact subset enumeration covers each of the \(2^9=512\) edge configurations and every unordered pair of nine edges; polynomial comparisons take place in \(\mathbb Z[q,v,w]\). Every one of the eight orbit quotients has strictly positive integer coefficients, as listed in the attached certificate. The program also recomputes exact rational moment identities for 108 test instances. These tests supplement, not replace, the coefficientwise polynomial identity and analytic sign argument. The verification does not establish the unrestricted all-weights property, all graph sizes, historical priority, or independent validation.
