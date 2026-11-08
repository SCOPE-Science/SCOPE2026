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
# Verification

Run `python verify.py` using NumPy and SymPy; it requires no network access or other data files.

The script builds the kernel from its stated edge conductances, checks its row sums, nonnegativity and detailed balance; compares eigenvalues with the Fourier expressions; checks threshold-case classifications; verifies exact-rational identities for smaller cycles; and tests deterministic samples of nonuniform edge conductances against the claimed SLEM bound. Expected output is a single `PASS` line with counts, including 48 Fourier checks, 32 exact-rational matrix checks and 1344 nonuniform-edge comparisons.

The included tests check only finite samples and algebraic identities. General optimality is established by the convex group-averaging argument and analytic two-branch spectrum in `RESULT.md`; neither the tests nor a finite grid certify a continuum of parameters. Source comparisons are recorded in `REVIEW.md` and `AUDIT.json`, with unindexed literature identified as a risk. Independent audit has not been performed.
