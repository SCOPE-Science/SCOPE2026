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

# Reproducibility and limits

The standalone `verify.cpp` performs two complete finite integer enumerations for binary five-mers. Build with `c++ -std=c++17 -O2 verify.cpp -o verify` and execute `./verify`; compare its output with `verify_output.txt`.

The literal-word route visits all 1,048,576 binary words of length twenty and records exactly 512 covering words, all with equal four-symbol prefix and suffix, giving thirty-two rotation classes and eight symmetry classes. The independently parameterized edge-selection route visits all 65,536 orientation masks, finds 52 balanced and eighteen connected choices, and counts 32 rooted-edge Euler tours using a precise path-subset recurrence. Counts are integer exact with no statistical sampling, timeouts or optimization oracle.

The lower bound is the sixteen distinct reverse-complement classes requiring at least sixteen five-symbol windows. The closure lemma for arbitrary odd binary order is justified by vertex-imbalance parity in `RESULT.md`, not by experimental induction. No general optimizer count at larger orders follows from the finite certificate. The previous odd-order minimum-length result is cited rather than reclaimed; external independent validation is unperformed.
