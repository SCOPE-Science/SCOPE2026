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

# Verification of the prime-field structure-graph six-cycle theorem

Execute `python3 prime_structure_cycle_checker.py`. The script uses the Python standard library only and prints `PRIME_STRUCTURE_GRAPH_DENSITY_CERTIFICATE_OK` on completion. It checks the exact degree-eight iterative identity, the resultant, the integer discriminant, irreducibility modulo five, the distinct linear-plus-irreducible-cubic factorization modulo eleven, the orbit lengths at four sample primes, and the finite wreath-product element distribution.

The infinite-prime density follows by Chebotarev after the proven Galois and cyclotomic intersection calculations; no finite computation independently validates Chebotarev or all primes. The checked theorem counts only cycles canonically supplied by the stated sextic, not every primitive six-cycle of the structure digraph.
