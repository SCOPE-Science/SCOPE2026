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

Two standalone programs provide reproducible finite checks of the exact labelled-configuration dynamics and of an independent weighted block reduction. Run `python3 verify_direct.py` and `python3 verify_signature.py` from the directory containing these files. No dependencies outside Python's standard library are required. Recorded stdout is in `verify_direct.out` and `verify_signature.out`.

`verify_direct.py` builds the adjacency lists explicitly and enumerates all possible binary configurations for 53 graphs, totaling 1,024,064 configurations. It classifies precisely those for which two updates return the original labelled word, rather than inferring periodicity from a simulation cutoff.

`verify_signature.py` enumerates 1,681 parameter pairs (all integers 3 through 43 for both shore sizes) and weights each block signature by exact binomial coefficients. Signature-level periodicity is equivalent to labelled periodicity because a nonuniform block can return to the same exact size after two steps only if it was retained bitwise throughout; any strict-majority reset makes a uniform block that cannot restore a nonuniform word in a single further update.

These finite computations corroborate, but do not replace, the all-parameter proof from the explicit block-update equations and mixed/uniform-block dichotomy. The historical-priority check is not a mathematical certificate; independent scientific audit has not been performed.
