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

Run `python3 CHECK.py` in the directory containing this file, with Python 3 and no third-party packages. This program constructs the original recurrence modulo \(2^k\) independently of the binomial-series proof for all sixteen even values \(0\le v\le30\) and all eleven moduli \(2^1\) through \(2^{11}\). It verifies every odd input/output fiber (32,752 fibers overall), bijectivity onto even target residues, the complete even-index congruence modulo eight, unique zero-target index classes and all attainable low-shell three-square congruences. A separate exact-integer loop checks the asserted valuation of differences between odd-index generalized derangements. The previously studied parameters \(v=0,2\) serve only as controls.

The infinite theorem follows from the uniformly convergent \(2\)-adic interpolation, its integer-coefficient divided-difference parity, finite eight-state congruence induction, and Legendre's theorem; no finite search can replace those arguments. The computed root digits depend on the parameter and are supplied by an algorithm, not as an unsupported closed form. The published prior comparison has residual priority risks. Independent mathematical audit has not been performed.
