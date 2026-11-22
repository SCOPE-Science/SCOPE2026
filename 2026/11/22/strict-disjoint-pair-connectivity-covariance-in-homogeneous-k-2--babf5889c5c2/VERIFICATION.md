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

The all-size proof is algebraic and self-contained in `RESULT.md`. Its critical steps are: a disjoint partition into disconnected-hub and connected-hub sectors; exact one- and two-event marked partition sums; a covariance numerator factorization; and a strict positivity inequality for \(0<q<1\). The factorization is checked independently against brute-force edge-subset enumeration.

Run `python3 verify.py` in a directory containing the extracted standalone files. Using only the Python standard library, it enumerates all occupied-edge configurations of the graph at each of four leaf counts \(n=4,5,6,7\), five rational cluster weights and three rational bond activities. All 60 complete finite-state comparisons agree exactly with the partition function, both marked moments and the factored covariance expression; all checked covariances are positive. The two smaller graph orders are used only as supplementary identities and are not included in the new theorem's asserted novelty.

Limits of verification: a finite enumeration cannot establish the theorem for unbounded \(n\), untested real \(q,v\), or nonhomogeneous weights. Those conclusions rest on the proof in `RESULT.md`; no claim of independent scientific audit or computer formalization is made.
