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

# Verification and limits

The universal proof is in `RESULT.md`. The following two files independently compute complete profiles and periodic witnesses using only the Python standard library:

- `verify_spectrum.py` compares the full list of every non-singleton fiber against the formula for \(n=5,\ldots,56\) and every integer \(k>(n+1)/2\), for 780 parameter pairs, and checks the smallest injective read length for \(n=5,\ldots,34\).
- `verify_witness.py` checks every admissible periodic witness in each of 4,601 length/read pairs with \(n=5,\ldots,120\) and \(3\le k\le\lfloor(2n+1)/3\rfloor\).

Both programs were executed on the included source files. The exact captured standard outputs are in `verify_spectrum.out` and `verify_witness.out`. Their finite scope cannot independently prove an infinite theorem; that requires the five-step interval/period argument. No independent external audit or formal proof assistant was used.
