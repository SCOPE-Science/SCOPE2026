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

# Reproduction and verification limits

Run `python3 check_involution_shattering.py` with Python 3 and the standard library. No external software dependencies are required. The script enumerates **every** involution and every subset of the full ordered \(n\times n\) query board of cardinality at most \(n\), for \(1\le n\le5\), testing realized Boolean traces directly. It independently calculates the proposed face polynomial coefficients, then checks that maximal shattered supports have the predicted size distribution. The genuine output from this run is embedded in `CHECK_OUTPUT.txt`.

Expected coefficients (powers in ascending order):

- \(n=1\): \((1,0)\)
- \(n=2\): \((1,4,0)\)
- \(n=3\): \((1,9,3,0)\)
- \(n=4\): \((1,16,42,4,0)\)
- \(n=5\): \((1,25,130,70,5,0)\)

The all-order proof is independent of the checker: disjoint two-cycles/fixed points provide both the obstruction and the explicit trace construction. Facet and homology claims use the face classification and a standard integer simplex-boundary matrix. The probability threshold uses a closed sequential product with a uniformly bounded diagonal-sampling error, not simulation. The finite enumerator is *not* a proof beyond order five; no separate homology computation or independent mathematical validation is asserted. Historical uniqueness remains subject to broader literature review.
