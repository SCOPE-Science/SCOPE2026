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

## Reproducibility

Run `python3 verification/verify.py` using Python 3 with no nonstandard packages. The expected standard output, reproduced by executing the delivered code, is stored at `verification/verify_output.txt`.

The checker builds actual adjacency masks for all parameter pairs with \(3\le a\le12\) and \(2\le b\le12\). It verifies six successive adjacency-power ranks for all 110 pairs; for the 36 cases of at most twelve vertices it also constructs the full trajectory graph and checks the period census, entry-time census, and individual attraction basin sizes. Six further baseline bicliques are enumerated. The output records 918 checks, not an exhaustive argument over all sizes.

The theorem follows from the rank reduction and Jordan-block argument in RESULT.md, independently of these experiments. No external expert assessment or independent audit was conducted.
