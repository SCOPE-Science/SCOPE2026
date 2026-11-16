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

# Reproducibility of the signed Aztec-diamond theorem

Run `python3 verify.py` with Python 3.10 or newer. The checker uses no third-party libraries and is fully deterministic.

The checker validates, with exact binary Gaussian elimination, the full binary rank and complementary-minor nonsingularity for every order from one through twelve. It enumerates perfect matchings exactly for orders one through five and computes the complete \(2^n\)-entry table of signed sums obtained by flipping the distinguished diagonal edges. The resulting gcds are \(2,4,8,16,32\), and the numbers of exactly sharp signings are \(1,3,3,5,5\). A separate integer Bareiss determinant calculation verifies the Kasteleyn equality in absolute value for all such signings in orders one through four.

Expected terminal marker: `AZTEC_SIGNED_WALSH_GCD_PASS ranks_n=1..12 direct_sums_n=1..5 determinants_n=1..4`.

The all-order theorem is established by the proof's rank, complementary-minor, finite-difference and Walsh-inversion steps. The finite calculations alone do not certify the infinite quantifiers. All calculations use exact integers and no floating-point tolerances. Independent mathematical audit has not been performed.
