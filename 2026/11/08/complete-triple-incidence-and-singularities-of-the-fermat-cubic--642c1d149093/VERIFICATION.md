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
# Reproducibility and limits

Install Python 3 and SymPy; in the directory containing this file, run `python3 verify_fermat_conic_incidence.py`.

Expected last line: `FERMAT_27_CONICS_COMPLETE_PASS 2925 65 5 4 2 9 18 36 1242`.

The implementation constructs all polynomial coefficient vectors, the full group action of order \(54\), all \(65\) orbits of unordered conic triples, and three affine Gröbner bases for each orbit representative in both characteristics \(109\) and \(127\). It also verifies the two characteristic-zero positive representatives, complete combinatorial list of concurrent triples, and uniqueness of each unordered conic pair among them. The two prime specializations are legitimate because \(\alpha,\omega\) are algebraic integers; a characteristic-zero common projective zero must specialize to a nonzero common projective zero at every finite place.

The pairwise intersection types and the local analytic classification of the three common-tangent branches are published premises, not silently re-established by the script. There is no independent audit or external validation certificate.
