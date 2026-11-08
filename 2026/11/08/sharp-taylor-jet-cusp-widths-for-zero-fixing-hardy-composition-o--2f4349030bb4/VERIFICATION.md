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
# Verification of the Berezin cusp-width formula

The primary mathematical verification is the written argument in `RESULT.md`: it derives the exact normalized kernel expression, proves isolation of the Berezin value \(1\), computes the uniform Taylor expansion, and uses fixed-angle radial intermediate-value arguments to realize the two sharp section extrema. The Schwarz–Pick bound supplies the needed compactness of near-tip level sets. No finite sampling is substituted for those infinite-dimensional and asymptotic arguments.

The standalone standard-library checker `check_berezin_cusp.py` was executed with Python 3 and returned exactly:

`BEREZIN_JET_CUSP_FINITE_OK 29037`

The 29,037 assertions cover linear-symbol identities, numeric section widths of sample polynomial symbols with first nonlinear orders two, three and four, sample disk-selfmap inequalities, and section-radius scaling. These are finite consistency checks; in particular, they are not an exhaustive proof or an independent mathematical audit.

The 2026 primary source (arXiv:2610.17634v1) and the Cowen–Felder comparison manuscript were inspected as open full text. The main source already proves a qualitative cusp and a linear-symbol convexity classification; the exact all-orders transverse coefficient is the asserted extension. The statement does not claim a result for an arbitrary complex derivative.
