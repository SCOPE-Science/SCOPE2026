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

# Reproduction and boundaries

Run `python3 verify_k33.py` with an ordinary standard-library Python 3 interpreter. The exact expected output is in `verification_output.txt`.

The checker directly enumerates the 512 edge subsets and selects all 327 nonempty forests, constructs the full 72-element or shore-preserving 36-element permutation groups, enumerates barycentric flag **orbits** without identifying different flags that have the same rankwise orbit vertices, and independently computes Burnside fixed-flag counts. It explicitly verifies all compositions of consecutive integer boundary operators vanish. All cancellations have coefficient exactly +1 or -1 and use the exact Schur complement, so they preserve integral homology (including potential torsion). They leave chain ranks (1,0,0,0,1), with no differential, for both groups.

The code proves only finite arithmetic facts. The general topological lemmas and the premises for applying them are supplied in RESULT.md: graphic-matroid shellability for connectivity, Armstrong for the orbit fundamental group, then Hurewicz and Whitehead to upgrade integral homology to homotopy equivalence. It does not certify manifold status, a general biclique family, or priority against every possible unpublished or unindexed work.
