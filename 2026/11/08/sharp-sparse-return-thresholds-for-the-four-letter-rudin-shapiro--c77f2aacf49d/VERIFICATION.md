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

# Reproducibility and verification

Run `python3 verify.py` with Python 3.9 or later. No packages, downloads, external tables, or special theorem provers are needed. The verifier constructs the fixed-point substitution directly and tests precisely the claim in `RESULT.md`.

The complete length-67 factor language consists of 528 words, with equality between the factor sets at substitution powers 11 and 12 and stability under the factor-substitution operator. That equality plus the elementary finite-language lemma in `RESULT.md` is the reason the finite computations are logically exhaustive for all positions of the infinite word.

For each of the 66 candidate delays, the verifier constructs an integer column whose 528 bits encode whether the first and delayed letters of each factor agree. It checks that every shift of odd length has no matches, that every required even shift through 10 has a forcing length-11 factor, and that the five-shift set covers all 528 factors. It enumerates all 1,024 subsets of delays 1 through 10, all 40,920 four-combinations of even delays through 66, and all 35,960 four-combinations through 64. It verifies that the complete list of four-shift solutions through 66 is exactly the two sets stated in the result.

It separately tests actual positions in a substitution prefix of length 8192 and compares the binary image of that prefix with the parity of adjacent 11 occurrences in the base-two digit expansion. These additional checks are supporting evidence; the infinite-position guarantee comes from factor-language closure. The published binary three-shift impossibility in Meleshko–Ochem–Shallit–Shan, Theorem 28, is a cited premise and is not re-certified here.

Expected successful output:

```
VERIFY_OK factors67=528 factors11=80 four_shift_sets_checked=40920 max64_checked=35960 optimum_sets=2 horizon10_minimum=5
```

Independent scientific audit has not been performed. No claim is made about optimizers with four shifts and maximum shift greater than 66.
