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

# Verification and reproducibility

The finite checker `sus_three_verifier.py` uses Python 3 standard-library `Counter`, combinations, and seeded pseudorandom sampling. It constructs every weight-three word of lengths 3–21 and determines the global shortest uniquely occurring **contiguous** substring by explicit factor-frequency dictionaries. Separately, it calculates the same quantity using a bounded number of zero-gap candidate patterns with zero, one, two, or three ones. The two procedures agree on all 7,315 tested words.

It also verifies the theorem's maximum and exact equality set exhaustively at lengths 5–21. For each length 22–300, all theoretically prescribed maximizing gap vectors are checked against the separate candidate computation, as well as 30 fixed-seed random gap vectors, a total of 8,370 samples. The stored output `sus_three_verification_output.txt` was captured by running `python3 sus_three_verifier.py`.

The certificate is diagnostic finite evidence. Infinite correctness rests on the self-contained case proof in `RESULT.md`. A finite sample does not establish all-length extremality, and no computer-algebra, external theorem-prover, or independent human validation is claimed.
