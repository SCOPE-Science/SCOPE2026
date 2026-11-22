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

# Reproduction and limits

Run `python VERIFY.py` with a standard Python 3 interpreter. The program enumerates every nilpotent zero-preserving nondecreasing map of \(\{0,\dots,n\}\) and tests the bound for all ordered pairs through \(n=8\) (2,044,900 ordered pairs), triples through \(n=5\) (74,088 triples), and quadruples for \(n=4\) (38,416 quadruples). It separately enumerates every exact-index stratum at the minimal bound \(n=N\), verifies its multinomial cardinality, and reconstructs every color-word extremizer. The final line must read `JOIN_NILPOTENCY_AND_MULTINOMIAL_CHECKS_PASSED`.

A finite test cannot certify a theorem over all positive \(n\) and \(k\). The mathematical proof is the height-potential argument, the characterization of equality, and the explicit inverse-coloring construction in `RESULT.md`. All results concern zero-preserving monotone transformations; no general arbitrary-semiring sum or nonmonotone-map claim is made. Independent mathematical audit: not performed.
