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

# Verification and boundaries

The two standalone programs `verify_dp.py` and `verify_direct.py` run under Python 3 with no third-party dependencies. Run each from the directory holding all eight packaged files.

`verify_dp.py` performs complete enumeration of all \(8192\) length-thirteen and all \(16384\) length-fourteen binary words, calculates all sixteen scattered four-factor multiplicities by an exact integer dynamic program, and groups every word by its complete deck. It checks respectively \(8176\) and \(16328\) different decks, no mixed run-status fiber at length thirteen, and exactly the two listed witnesses in the unique length-fourteen mixed fiber. Observed output terminates `DP_EXHAUSTIVE_OK`.

`verify_direct.py` independently computes each length-thirteen deck through the \(715\) index quadruples, checks the same zero-mixed-fiber conclusion and \(8176\) class count, and computes both witness decks through all \(1001\) quadruples. Observed output terminates `DIRECT_EXHAUSTIVE_N13_OK`.

The padding and deck-marginalization identities are symbolic, and do not depend on the finite checker. The general upper bound is taken with its stated scope from Angal et al., Theorem 1.3, arXiv:2610.41110v1. These checks were performed in the same scientific assessment; independent audit and external validation have not occurred. Exhaustive finite verification does not assert a count of all longer-length collision classes.
