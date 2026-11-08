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

`verify.py` uses only Python's standard library and exact integer arithmetic. Run `python verify.py`.

The theorem reduces every possible input to one of 19 truncated triples for each ordered nonzero-symbol pair, a total of 57 templates for the two representative symbol types. Every fiber size is obtained by stars and bars, a polynomial in length of degree at most two. The program compares all 57 complete nonzero-three-mer vectors and checks the proposed fiber-size patterns at three consecutive lengths, enough to establish the polynomial identities for all lengths in scope. It also verifies these identities for additional lengths and directly enumerates 15,120 actual words over alphabet sizes two through five at lengths eight through fifteen.

Expected output: `VERIFY_OK templates=57 direct_words=15120 alphabet_sizes=4 n=8..15`.

The finite comparison is exhaustive only because of the proved truncation reduction. The direct input enumeration by itself would not justify a universal statement. Neither independent review nor tests of noisy or cyclic read models are claimed.
