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

Run `python3 check_direct.py` and `python3 check_binary.py` from the directory containing these files. The first checker enumerates all direct standardized single-deletion composition minors up to weight eleven, compares the entire pair edge set with the local-move family, constructs connected components and verifies predicted Fibonacci sizes. The second constructs independent terminal-bit-one binary encodings, tests admissible bit deletions against the composition channel, and verifies exact graph counts with two rational generating functions.

Each program completed successfully through \(n=11\) on the reviewed files. The generated output was checked against the reported first coefficients. Exhaustive checks stop at \(n=11\), and do not independently establish the infinite claims: the mathematical proof in `RESULT.md` establishes those claims using the standard binary deletion intersection lemma. No external independent mathematical audit has been performed.
