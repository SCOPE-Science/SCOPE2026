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

# Verification of the two-crossover tree classification

Run `python3 check.py` with Python 3.8 or later (standard library only). On a successful run the last line is `ALL_CHECKS_PASS`. The script enumerates all labeled Prüfer encodings up to seven vertices, deduplicates them by canonical unrooted-tree codes, and computes every pair of exact source-variance polynomials from the unique-path moment identity. It asserts the counts of tree shapes, sign-variation bounds, exceptional pair configurations, and their two marked-tree isomorphism types.

The proof of the all-parameter crossover counts uses the Mobius substitution mapping the unit interval to the positive half-line, followed by Descartes' sign rule and exact endpoint/intermediate evaluations. It is not inferred from a finite grid of transmission parameters. For the displayed witness, an independent computational route sums the complete distribution over all 64 edge-open masks and confirms the two moment polynomials obtained by path-distance sums.

This verifies the exact finite classification and symbolic witness under the specified independent-edge model. It does not validate the statement for other epidemic processes, larger-tree classifications, or unpublished historical literature. Independent scientific audit has not been performed.
