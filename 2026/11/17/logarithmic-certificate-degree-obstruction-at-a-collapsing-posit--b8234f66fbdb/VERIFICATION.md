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

# Verification notes

The theorem is proved analytically in `RESULT.md`. Exact rational checks in `CHECKER.py` test the source polynomial identities and derivative data at several positive rational parameters. Those tests do not establish an infinite asymptotic theorem; the proof's core is the Bernstein–Walsh estimate combined with the globally positive matrix jet inequality and the source polynomial's boundary values.

The lower bound requires the weighted-degree SOS model specified in `RESULT.md`; replacing the cone, the moving generators, or the degree convention changes the problem. The proof gives \(\liminf\), not an upper bound or an exact certificate degree. The source paper proves existence of certificates and qualitative degree divergence. Unrestricted mathematical-priority claims and independent validation are not made.

To replay the finite arithmetic diagnostics, run `python3 CHECKER.py` from the extracted package directory. It uses only the Python standard library. The checks use exact fractions for polynomial coefficients and a finite geometric numerical illustration. The analytically proved positivity-jet lemma and extrapolation inequality are not inferred from samples.
