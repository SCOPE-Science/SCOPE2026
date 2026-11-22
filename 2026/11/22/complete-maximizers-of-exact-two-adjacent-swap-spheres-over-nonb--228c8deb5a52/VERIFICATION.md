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

Run the self-contained Python 3 program `verify.py` with `python3 verify.py`. It needs no third-party packages, no input data, and no network access. Its saved standard output appears verbatim in `verification_output.txt`.

The standalone implementation constructs the set of all tuples resulting from every ordered pair of adjacent swap positions. It compares this direct finite construction with the claimed local formula, tests the exact maximizing-words characterization for alphabets of size at least three, checks the recurrence and convolution counts for these words, and checks the binary local formula as an auxiliary control. Domains are \(q=2\) with \(2\le n\le12\), \(q=3\) with \(2\le n\le9\), \(q=4\) with \(2\le n\le7\), and \(q=5\) with \(2\le n\le6\), together totaling 79,073 source words. All assertions complete successfully.

The program does not establish an all-length theorem merely by enumeration. The general formula, the two extremal constructions, their equality conditions, and the recurrence are instead proved by the local support and run arguments in `RESULT.md`. Exact-two-operation spheres are distinct from at-most-two metric balls and from disjoint-swap spheres. Independent mathematical auditing or external formal validation has not been performed.
