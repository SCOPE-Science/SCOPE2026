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

The package contains `checker.py`; run `python3 checker.py` from any directory with Python 3. The checker uses rational arithmetic for the exact adjacent-swap identity and exhaustive finite-permutation extremum comparisons, plus floating-point cross-checks for explicitly proved infinite-product asymptotics. A successful run prints four `PASS` lines, with respectively 144, 36522, 144 and 54 checks.

**What was checked.** Adjacent exchanges were checked at rational weights and multiple intrinsic dependence rates; every distinct permutation was checked for several weight families of orders 2 through 7. Closed-form geometric products were checked in 144 exact parameter/order instances. Positive limiting constants and the descending exponential scale were checked numerically for representative values.

**What was proved mathematically, not computationally.** The proof in `RESULT.md` establishes the adjacent-exchange sign for arbitrary positive weights, any finite number of partners and \(0<r<1\); it also establishes positivity of the infinite products and the stated relative asymptotic error. Finite checks do not prove these infinite or arbitrary-parameter claims. The theorem does not address fully coupled coextinction cascades, ecological measurement noise or control of primary extinction times.

Independent audit: not performed. No external certification is claimed.
