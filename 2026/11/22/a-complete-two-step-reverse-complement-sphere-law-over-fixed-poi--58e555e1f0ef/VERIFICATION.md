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

# Verification and reproducibility

Run `python3 verify_direct.py` to enumerate exact two-step output sets and independently compute the run penalty for all words over alphabet sizes 2, 4, and 6 through the configured lengths. Run `python3 verify_transfer.py` to compare a transfer dynamic program and full source enumerations for the complete statistic distribution, including endpoint populations.

The tests are finite cross-checks. The symbolic proof in `RESULT.md` establishes all positive lengths, every fixed-point-free involutive finite alphabet, and the exact rational generating function. The code uses the canonical complement pairing \(a\mapsto a\mathbin{\mathrm{xor}}1\); every fixed-point-free involution is equivalent under relabeling.

Independent audit: not performed. No third-party verification is asserted.
