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

# Verification of the spectral fiber theorem

Run `python3 verify_isospectral.py` from a directory containing that standalone file, using a standard Python installation. The script uses only the standard library. The companion output `verify_output.txt` is the observed standard output of a successful execution.

Direct determinant enumeration verifies equality of two independently implemented counting paths: all rank-one vector updates versus a Krylov-dimension sum. It covers every base matrix of size two over fields of orders two and three, every base matrix of size three over the field of order two, and fixed deterministic samples of larger cases.

A further test compares the primary-partition target-count formula against a fresh literal determinant histogram **for every monic target** associated with ten explicit rational-canonical types, including irreducible polynomials of degrees two and three, mixed primary decomposition, and a repeated irreducible degree-two block. All 92 comparisons pass.

The strict Jordan-dominance implication is checked independently for 696 ordered pairs of small partitions at field orders two, three and five. The final output line is exactly `ALL_RANK_ONE_SPECTRAL_FIBER_CHECKS_PASS`.

The Python program operates over prime fields, not arbitrary prime-power extension fields, and tests only finite dimensions. Its coverage is explicitly limited; the proof in RESULT.md establishes the unrestricted theorem using elementary divisors and polynomial identities. No external, independent scientific audit has been performed.
