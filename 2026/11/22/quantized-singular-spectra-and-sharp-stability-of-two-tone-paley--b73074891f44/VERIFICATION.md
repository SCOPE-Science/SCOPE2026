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

# Mathematical and computational verification

The exact assertion is proved in `RESULT.md` by Plancherel, the truncated-step Fourier Gram identity, unitary disintegration of the frequency interval into residue chains, and sine diagonalization of the finite path. Those steps cover every \(\sigma,\eta,r>0\); no finite cutoff is used in the proof.

Reproducing the finite consistency checks: run `python3 two_tone_check.py` with the Python 3 standard library. The observed result is `TWO_TONE_PALEY_WIENER_CHECK_OK 40704` (40,704 assertions). The program independently calculates finite rectangular synthesis matrices with exact rational coefficients, checks the Gram entries, tests all sine eigenvectors numerically and enumerates fiber cardinalities at 48 parameter pairs.

Limit: these finite checks support the algebraic formulas but do not certify the infinite-dimensional spectral decomposition. No independent audit was performed; no independent validation is claimed. The source-comparison assessment is qualified because an implicit general theorem may exist outside the inspected literature.
