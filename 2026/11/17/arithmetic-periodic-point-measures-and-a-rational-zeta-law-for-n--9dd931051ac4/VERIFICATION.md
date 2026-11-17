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

The mathematical proof in `RESULT.md` is the basis for the infinite-parameter and infinite-length statements. A standalone Python 3 script `checker.py` independently constructs cyclic admissibility and junction-subset representations for finite lengths. Running `python checker.py` prints `PASS 67 finite parameter/length census and marker checks` and exits successfully on the reviewed package.

The finite program checks \(k=1,2,3,4\), all \(1\le n\le14\) for the fixed-point counts, and extra finite bijection and \([01]\) checks. It does not certify completeness at arbitrary lengths, the infinite weak-* limit, or publication priority; those require mathematical reasoning and separate review. Independent audit has not been performed.
