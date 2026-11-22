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

The analytic proof is contained in `RESULT.md`. The standalone `CHECK.py` program requires Python, NumPy, and SymPy and can be run with `python CHECK.py` from the same extracted folder. The expected output is `PASS: 5910 symbolic and independent numerical assertions`.

The checker separately rederives exact stationary Fourier relations symbolically and through a numerical complex three-state generator solve; it evaluates spectral roots, stationary densities and radial tails over parameter grids; verifies the single crossing, strict ratio derivative signs, inverse Laplace design, and positive-moment identities. The numerical grids are finite diagnostic samples, not exhaustive coverage; all universal statements are proved analytically in `RESULT.md`.

No independent audit or third-party certification was performed. Published pure-protocol spatial formulas and the special spatial-aliasing balance are acknowledged as inputs. The new conclusion is restricted to the off-balance mixed-reset stationary spatial family and the precisely stated hypotheses.
