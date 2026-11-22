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

# Reproducibility and scope

The complete proof is in `RESULT.md`. `verify_direct.py` computes suffix-power exponents by comparing trailing blocks for each possible period, with no use of the closed-form formula inside the observed computation. It then checks the explicit formula, the complete inverse classes, the image counts, and the maximum fiber size for every length \(2\le n\le40\). The execution counted 10,660 distinct sources and 73 nontrivial fibers across those lengths.

`verify_inverse.py` implements the explicit three-gap formula separately and groups all sources at every length \(2\le n\le100\), comparing its outputs to all predicted exception families. The captured stdout files `direct_output.txt` and `inverse_output.txt` give the passing results and sample collision classes.

To replay: `python verify_direct.py` and `python verify_inverse.py` (Python 3 standard library only), using the files from this package. These finite checks verify implementation agreement and stated small inputs; they do not prove the quantified infinite result. The suffix-power lemma and inverse-case analysis supply the all-length argument. No independent external validation is asserted.
