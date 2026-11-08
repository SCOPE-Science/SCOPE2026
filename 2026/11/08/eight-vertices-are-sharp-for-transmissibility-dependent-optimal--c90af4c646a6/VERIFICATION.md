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

# Mathematical verification

Run `python3 verify.py` using Python 3.8 or newer. No external software is needed. The script computes all path-distance polynomial coefficients by direct graph traversals for each of the \(n^{n-2}\) Prüfer-labelled trees at orders \(n=2,\ldots,7\). It selects an edge at \(p=1/2\), and calculates Bernstein coefficients exactly with `fractions.Fraction`; every signed difference is verified to be nonnegative for the entire unit interval. This is a finite exhaustive certificate with a standard Prüfer-bijection completeness argument.

For the eight-vertex witness it prints each edge's distance-count coefficients and checks the proposed signed differences coefficient-by-coefficient. Independently of the distance formula, it enumerates each possible open/closed status of the six remaining edges for three exact probabilities, computes the resulting graph components, and checks the expected uniform-seed outbreak by summing squared component sizes. All checks are exact integer or rational calculations; the probabilities used for this independent corroboration are \(1/4\), \(1/2\), and \(3/4\). This independent finite test does not replace the all-parameter Bernstein certificate.

The mathematical conclusions are confined to trees of order at most seven and to the stated eight-vertex counterexample. They do not assert general trees always have a probability-invariant optimal edge, or extend to other seed laws, transmission dependence or arbitrary networks. Historical-priority review and independent mathematical audit remain unperformed.
