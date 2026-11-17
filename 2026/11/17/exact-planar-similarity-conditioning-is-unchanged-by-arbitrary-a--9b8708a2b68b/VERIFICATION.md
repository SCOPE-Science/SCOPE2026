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

# Verification guide

Run `python verify.py` with Python 3; no third-party packages are needed. The script checks 400 rational parameter pairs, three exact assertions for each (1,200 total), and 256 independently sampled complex unitary conjugations with seven assertions per sample (1,792 total). Expected output: `PASS: 2992 exact and numerical assertions; universal theorem is analytic.`

The actual run produced that exact output. These checks verify canonical intertwining identities, inverse identities, norm identities, and the sharp condition number under phase changes. They do not enumerate arbitrary matrices or infinite-dimensional amplifications.

The proof itself supplies the universal certificate: polynomials in an intertwined matrix remain intertwined; tensoring with a nonzero Hilbert identity preserves the operator norm; unit eigenvectors yield the stated involution normal forms; nontrivial square-zero matrices yield the stated Jordan forms; and the diagonal similarity attains the invariant lower bound. The \(q\)-independent witness explicitly attains the envelope for every real \(t\geq1\).

Independent audit has not been performed.
