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

# Verification and limitations

The self-contained `verify.py` uses exact bitwise addition for \(\mathbb F_2^r\). It checks every one of the \(12{,}870\) size-eight subsets at \(r=4\), independently reconstructs all restricted four-sums, determines whether an affine-hyperplane condition holds, and separately identifies full-fiber exceptional lifts. The verified classes are \(12{,}000\) fully covering sets, \(840\) sets with exactly one missing nonzero target, and \(30\) hyperplanes with eight missing targets. It checks each of the \(62\) affine hyperplanes for \(r=5\) and a fixed-seed collection of \(2000\) further half-sized subsets.

Run `python verify.py` with Python 3.10+. Expected terminal marker is `VERIFY_OK` after the preceding `R4_OK` and `R5_OK` lines. The checks are finite corroboration; the unrestricted theorem is proved by exact quotient-fiber reasoning. Independent mathematical audit has not been performed. Historical priority, especially equivalent inverse-sumset terminology, remains subject to specialist review.
