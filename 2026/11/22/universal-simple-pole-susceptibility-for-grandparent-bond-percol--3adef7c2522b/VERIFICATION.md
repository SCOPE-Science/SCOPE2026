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

# Reproduction and scope

Run `python3 CHECK.py` using the Python standard library. The checker runs 247 deterministic assertions (including exact rational enumeration of all short/long edge configurations on binary grandparent graphs through depth two), compares the analytic derivative formula with symmetric finite differences, and verifies numerical convergence to the claimed residue in seven finite-support examples. The numerical binary reference is \(p_c\approx 0.15865632604477647\), with residue \(0.08260628557486904\). These are independent finite consistency checks, not infinite certificates.

The proof in `RESULT.md` uses the cited decomposition and boundary identity from the original full-text article and derives the previously unstated first-block expectation. Strict positive derivative and finiteness under infinite offspring variance follow from evaluation of the pgf at an argument strictly below one. No external expert validation has been performed.
