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
# Finite verification and reproducibility

Run `python3 verify.py` using Python 3 without third-party dependencies. The code enumerates all Dyck words through semilength 10, recomputes the alternating-interval edges, and checks the theorem's edge total and maximum degree. At semilengths 1–8 it also builds complete sets of one-deletion descendants, accumulates overlap counts and verifies equality of the resulting graphs rather than merely equal counts. All positive-height marked vertices are separately enumerated through semilength 10. Expected stdout begins with `VERIFY_OK`.

The generated edge totals for semilengths 1–10 are 0, 1, 6, 27, 111, 441, 1728, 6733, 26181, and 101763. The exact number sequence is already available as OEIS A371965 in a different enumerative interpretation; matching the table is a cross-check rather than novel evidence. The proof of the universal statements is mathematical and invokes the previously published Type-A intersection theorem. An independent mathematical audit has not been performed.
