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

# Verification record

Run `python3 checker.py` (Python standard library only). It implements the cyclic run/gap coefficient formula with exact `Fraction` arithmetic and independently enumerates all proper nonempty vertex subsets. These full profile dictionaries agree at all even sizes four through twelve. Separately, every involutive bijection of each induced subposet is constructed and tested against every ordered comparison at even sizes four, six and eight; the complete fixed-point/two-cycle census matches the formula. The expected success message is `EVEN_CROWN_INVOLUTION_CENSUS_VERIFIED 4,6,8 brute; 4,6,8,10,12 transfer/profile checks`.

The exact rank totals at sizes four, six, eight, ten and twelve are `25,103,507,2629,14373`. The corank-two counts at those sizes are `8,24,56,90,144`. Exhaustive finite checks do not establish the infinite theorem; the structural component decomposition and factorial bounds in `RESULT.md` do. Independent scientific validation has not been performed.
