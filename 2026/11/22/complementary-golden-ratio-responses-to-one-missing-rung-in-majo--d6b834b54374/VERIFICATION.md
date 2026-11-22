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

For every labelled prism \(C_n\square K_2\) with \(n\ge3\), delete the vertical rung at column zero and apply synchronous open-neighbor binary majority, retaining the incumbent bit at a two-neighbor tie. The theorem concerns states fixed after one or two updates and their arithmetic and asymptotic counts, not attraction basins.

`python3 verification/transfer_certificate.py` reconstructs the sixteen- and 256-state temporal-column graphs and checks their entire rational identities with integer arithmetic through the full Cayley–Hamilton bounds. It also verifies the displayed leading coefficients algebraically using degree-two polynomial reductions; expected marker: `EXACT_TRANSFER_CERTIFICATE_OK`. `python3 verification/direct_check.py` is a separately coded direct-state update enumerator through nine columns for both graph families; expected marker: `DIRECT_ENUMERATION_OK`.

Both source programs were actually executed from these package paths and the accompanying `.out` files record their results. Infinite-family conclusions rely on the finite adjacency-matrix and Cayley–Hamilton identities, not on extrapolation from small graphs. Independent external audit has not been performed.
