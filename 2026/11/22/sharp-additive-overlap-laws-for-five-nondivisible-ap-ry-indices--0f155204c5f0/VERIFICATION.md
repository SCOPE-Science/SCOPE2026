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

The standalone Python 3 file `verify.py` uses only standard-library arithmetic. It independently enumerates the two carry transitions for all five shift digits, generates the first 301 classical Apéry numbers from the integer three-term recurrence, and checks their nondivisibility by five against the base-five digit criterion. It compares finite pair counts and the exact formula for shifts in a bounded range through depth five, then verifies the strict first/second overlap family classification for every positive shift less than \(5^7\).

Run `python3 verify.py` in the directory containing this file and `verify.py`. These are finite consistency checks; the proof of the all-shift theorem and exact extremizers is the carry enumeration and product argument in `RESULT.md`. This verification does not constitute independent audit, a computer-assisted exhaustive proof for unbounded shifts, or a check of higher five-adic powers.
