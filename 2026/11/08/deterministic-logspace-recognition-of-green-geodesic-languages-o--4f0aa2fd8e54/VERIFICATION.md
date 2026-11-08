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

# Reproducibility of finite experiments

Run `python3 verify.py` with Python 3.9 or later. No third-party modules are required. The command enumerates all words of lengths zero through seven over the two-generator symmetric alphabet and builds exact Munn-tree equivalence-class keys. A direct exhaustive search for shortest representatives is compared with the four independently computed tree-metric expressions. The second stage enumerates words of length at most five, checking modular-matrix equality of prefixes against actual free reductions and verifying the parity-of-repeated-edges method for all prefix pairs.

The complete recorded output is `verification_output.txt`. The expected leading line is `VERIFY_OK alphabet=4 max_length=7 words= 21845 class_checks= 87380`, and the second stage ends with `LOGSPACE_KERNEL_OK words= 1365 vertex_and_distance_pairs= 26093`.

The modular test's fixed modulus cutoff of 32 is used **only for this finite experiment**. The mathematical proof instead uses all integer moduli up to a sufficiently large fixed constant times the input length; this distinction is essential. The finite enumerations cannot establish correctness for arbitrary words, non-context-freeness, novelty, or any external validation. The infinite theorem follows from the proof in `RESULT.md`.
