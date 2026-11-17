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
# Reproduction and limits

Run `python3 verification/check_windmill.py` with standard Python 3. The script uses only the Python standard library, directly enumerates acyclic orientations as independent total orders, forms each centered vertex by summing oriented half-edge generators, and compares its exact integer \(4Q\) values against the independent rank/multinomial formula. It checks the number of distinct vertices, exact finite moments, all shell multiplicities, the outermost squared radius, and the number of outer contacts for seven input pairs. The observed marker is `CLIQUE_WINDMILL_RADII_PASS cases=7 enumerated=548748`.

Checked cases: \((k,m)=(3,2),(3,3),(3,4),(4,2),(4,3),(5,2),(6,2)\). This totals 548,748 enumerated vertices. The computational check is finite and does not establish the all-parameter claim by itself. The proof uses the acyclic-orientation bijection, the exact hub-score identity, and independent rank moments. The weak limit uses the central limit theorem and strong law with fixed clique size; no finite simulation is offered as its proof.

Independent mathematical audit: not performed.
