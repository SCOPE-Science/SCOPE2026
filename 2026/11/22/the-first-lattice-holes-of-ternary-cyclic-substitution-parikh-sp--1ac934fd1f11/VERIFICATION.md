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

The finite certificate `verify_parikh_hole.py` contains exact integer enumeration and geometric computations, requiring only Python 3 standard library. It reconstructs all nine possible adjacent pairs of substitution blocks at ranks zero through three, scans every offset, determines the exact Parikh sets, and computes the integer convex hull and lattice holes. It also independently scans directly generated long prefixes, comparing complete factor-Parikh sets at each rank.

Run `python3 verify_parikh_hole.py`; compare with `verification_output.txt`. For ranks \(m=0,1,2,3\), the assertions check factor counts \(3,10,37,115\), hull lattice counts \(3,10,37,136\), and the exact 21-hole classification at rank three. The proof's nine-pair covering lemma establishes that the finite enumeration is exhaustive for these ranks. The checker does not prove an infinite-rank statement or novelty.
