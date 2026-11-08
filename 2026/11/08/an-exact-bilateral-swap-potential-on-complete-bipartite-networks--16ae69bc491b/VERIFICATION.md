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

# Reproducibility

Run \(\texttt{python3 verify.py}\) from the directory containing the extracted code; it requires the Python standard library only. Expected output starts with `PASS: 212500 exact swap identities over 1519 graph/type profiles; 21 witness placements, 12 improving, PoS=17/15.` The program independently computes individual average neighbor distances, internal pairwise distances and social cross sums using exact fractions. It checks the exact potential-difference identity for each cross-part exchange and completely enumerates the seven-agent instance.

The potential identity is established analytically in \(\texttt{RESULT.md}\); finite examples are independent consistency checks. The normalized seven-agent witness is exhaustive because every two-vertex-side placement has one of the seven listed type multisets (zeros are indistinguishable for costs), and every cross-part exchange is enumerated. No reliance on untracked datasets, remote services, external numerical libraries, or precomputed logs is required. No independent audit or external certification has been carried out.
