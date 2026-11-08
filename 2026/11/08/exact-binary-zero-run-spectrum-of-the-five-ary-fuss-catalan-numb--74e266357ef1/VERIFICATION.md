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
# Verification notes

Run `python3 verify.py` using Python 3 standard library only. The supplied script performs exact-integer binomial calculations, binary carry tests, exhaustive admissible-index enumeration, predecessor checks, a Fibonacci-product census, and an observed-versus-predicted strict-record comparison.

Observed exact output:

```text
INTEGER_PARITY_OK 0..1199
LOCAL_PREDECESSOR_GAPS_OK j=0..32
FINITE_SPECTRUM_OK m= 6 odd_count= 25 distinct_positive_gaps= 6 largest_gap= 9
FINITE_SPECTRUM_OK m= 12 odd_count= 441 distinct_positive_gaps= 18 largest_gap= 614
FINITE_SPECTRUM_OK m= 18 odd_count= 7921 distinct_positive_gaps= 30 largest_gap= 39321
RECORD_VALUES_OK [1, 2, 3, 4, 6, 9, 12, 19, 25, 38, 51, 76, 102, 153, 204, 307, 409, 614, 819, 1228, 1638, 2457, 3276, 4915, 6553, 9830, 13107, 19660, 26214, 39321]
VERIFY_OK exact_finite_checks=yes infinite_proof_is_structural=yes
```

The binomial check is independent of the binary-carry implementation. The enumeration exhausts only the stated finite ranges; it is not an infinite proof or an independent audit. The unrestricted theorem follows from the structural lemmas in RESULT.md. No Lean or external certification is claimed.
