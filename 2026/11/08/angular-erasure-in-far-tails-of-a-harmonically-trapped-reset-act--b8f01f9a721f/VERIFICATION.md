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

# Verification and limits

The analytical proof in `RESULT.md` derives the stationary exponential-age mixture, the universal Gaussian upper bound, an angular Brownian tube-event lower bound, and the separate frozen-heading exact tilted integral. The two resulting estimates establish the logarithmic survival expansion through an \(o(x)\) error at each fixed parameter set. Uniformity in the angular direction uses a strictly positive heat kernel on the circle and compactness of the direction set.

Run `python checker.py` with a standard Python installation in the folder containing the seven package files. The checker evaluates exact integral identities, mean formulas, OU variance, Gaussian saturation and the deterministic lower bounds on finite grids; it does not prove infinite limits. The run's observed output was `PASS 186 finite independent diagnostic assertions`.

Limitations: fixed \(D,\beta,v,r>0\), \(d\ge0\), two spatial dimensions; no uniform \(d\downarrow0\) statement, density prefactor, or vanishing-thermal-noise theorem. No independent scientific audit has been conducted.
