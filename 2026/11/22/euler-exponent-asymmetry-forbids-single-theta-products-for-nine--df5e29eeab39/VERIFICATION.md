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

## Reproduction

Run `python3 VERIFY.py` in the same directory. It requires only Python's standard library and should report three PASS lines, the 18-row table, and the exceptional exponent pair. There are no external input files.

The test computes all nine-colored partition coefficients needed through \(q^{379}\) by a finite, exact, nine-color unbounded-coin recurrence in \(\mathbb F_{19}\); constructs \(B_r\) independently from the two-term dissection formula; checks all nineteen truncated components through \(y^{19}\); extracts the unique Euler exponent vectors through degree \(18\) by the logarithmic derivative; and reconstructs each unit from its Euler factors. For each \(r\ne17\), it verifies either \(\epsilon_1\ne\epsilon_{18}\) or, for \(r=3\), \(\epsilon_2\ne\epsilon_{17}\). It also tests all 715 four-factor products as a redundant corroboration.

## Proof boundary

The formal uniqueness of Euler exponents in degrees below \(19\) and the paired-exponent necessity for theta products give the infinite identity obstruction; the finite computation is exhaustive for that obstruction, not a sample of indefinitely many cases. No independence or external certification is asserted. It does not address factor alphabets beyond the ten stated products or any additive rewrite.
