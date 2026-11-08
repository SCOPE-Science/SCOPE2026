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
# Verification evidence

Run `python3 verification/check.py`. The checker is standalone standard-library Python. It constructs rigorous rational enclosures for \(\pi\) using Machin's formula and an alternating arctangent series, and rigorous rational sine/cosine enclosures using Taylor-Lagrange error bounds. It certifies every strict integer-power form of the weak logarithmic inequality for the two residual small positive orders, all three high-order residue representatives, and strict exceptional ordering. It does not attempt to certify an infinite set by sampling; the proof's analytic residue-class monotonicity and strict convexity handle the infinite part.

Observed result after running from the final package: `RATIONAL_INTERVAL_CERTIFICATE_PASSED`, followed by finite-comparison counts \(18\) and \(30\), three large-order checks, and three exceptional comparisons.

There is no externally performed independent audit. Transcendental signs in the proof are bracketed rationally, not inferred from printed decimal approximations. The historical comparison is limited to the inspected published literature and relevant searches; absence of search hits is not proof of absolute first publication.
