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

# Reproduction and evidential limits

Run `python3 CHECK.py` in a Python 3 environment; only the standard library is used. This verifies the sharp tangent resonance, the rational cofactor identity on exact test grids, the exact two-sided heteroclinic formula on rational parameter examples, and positive-orbit accumulated logarithmic defects. The expected final line is `LESLIE_HETEROCLINIC_CHECK_OK`.

The critical identities are fully expanded in `RESULT.md`, not inferred from the tests. The proof of whole-quadrant convergence quotes the previously established Theorem 6(b) in the publicly archived 2017 McArdle dissertation, later published by Kulenović–McArdle (2019); its strict hypotheses are checked explicitly. The rate proof invokes local spectral contraction at the sink and summable errors in two positive products. Computational checks sample finitely many parameters and iterations; they do not certify the infinite quantified theorem. No independent audit was performed.
