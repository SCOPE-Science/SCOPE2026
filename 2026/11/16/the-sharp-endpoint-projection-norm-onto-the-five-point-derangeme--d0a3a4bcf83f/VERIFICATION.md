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

Run `python3 check_derangement_walsh.py` (Python 3 standard library only). For each of 2048 normalized signings, an exact derangement sum was independently matched to a Ryser permanent. The program then constructed the nonzero signed-permanent frequency indicator and independently computed its entire 2048-coefficient Walsh transform by butterfly recursion and direct character summation. It verified the nine-value absolute support-transform histogram, whose absolute sum is exactly 27996, hence the claimed new sharp endpoint projection constant 6999/512. It also verified the previously known signed-permanent histogram and rank as consistency checks, not as newly claimed results. Success marker: `DERANGEMENT5_WALSH_PROJECTOR_PASS cases=2048 rank=28016640 projection=6999/512`.

The exhaustive finite checker supports the evaluated integer identity. The proof separately establishes why translation averaging gives the global minimum among all linear projections. Independent mathematical audit is not performed.
