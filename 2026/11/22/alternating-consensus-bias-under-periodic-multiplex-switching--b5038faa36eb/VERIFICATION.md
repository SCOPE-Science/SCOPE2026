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

# Reproduction and limitations

The standalone `check.py` uses only Python's standard-library exact rational fractions. Run `python check.py` from the directory containing this document and the script. Its assertions independently construct the two weighted adjacency matrices, normalize every row, and for each integer \(1\le k\le31\) check \(BA^k=U+r_k(B-U)\), the claimed stationary probabilities, their normalization and parity comparison. It also verifies the isolated-layer stationary laws.

The infinite family is proved analytically in `RESULT.md` by a resolvent identity and a geometric remainder bound. Exhaustive finite arithmetic is not claimed to prove the infinite claim. The only numerical demonstration is the known exact three-vertex network. Generic second layers require the stated connectedness, positivity, nonbipartiteness and degree heterogeneity; arbitrary multiplex models and human populations are not covered. Historical novelty has a documented literature-access risk. Independent scientific audit has not been performed.
