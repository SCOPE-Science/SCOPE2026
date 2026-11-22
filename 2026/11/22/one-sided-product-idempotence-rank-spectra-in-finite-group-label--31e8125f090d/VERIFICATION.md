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

Run `python3 verification/verify.py` with Python 3 (standard library only) from the folder containing `RESULT.md`. The included `verification/check_output.txt` is a captured successful run from the delivered checker.

The checker independently enumerates every ordinary underlying transformation idempotent on one through four positions and every ordered pair whose directed product is idempotent. It compares every rank-triple coefficient against the formula for group orders \(1,2,3,6\). A separate test enumerates and multiplies *actual* labelled idempotents: cyclic group \(C_2\) on up to four orbit positions, \(C_6\) up to three, and the nonabelian symmetric group \(S_3\) up to three, comparing the exact joint-rank distribution. The two order-six groups yield the same rank distribution independently of their multiplication laws, as predicted. Finally, for \(1\le n\le10\), direct coefficient arithmetic checks the \(q\)-degree leading term \(nq^{2n-2}\). Terminal marker: `VERIFY_OK_GROUP_WREATH_SKEW_IDEMPOTENCE`.

These are finite checks. The proof for all finite groups and all sizes is the reversible orbit-partition count and independent-label equation analysis in `RESULT.md`; the asymptotic follows from the leading coefficient. Checks are not a substitute for this proof. The literature comparisons are not independent or comprehensive priority certification. Independent mathematical audit has not been performed.
