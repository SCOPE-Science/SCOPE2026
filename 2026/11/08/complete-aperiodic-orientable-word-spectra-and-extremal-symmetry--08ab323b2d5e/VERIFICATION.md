---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

A legal linear word corresponds bijectively to a path of de Bruijn length-n windows with no palindromes or repeated reversal-pair labels. The recursion over suffix and used-pair bitset enumerates every extension once, and complement pairs all first-bit-zero rooted paths. Independent from-scratch exhaustive enumeration found n=6: 11 normalized,22 labeled,6 R/C orbits,2 RC fixed; n=7:1647 normalized,3294 labeled,829 R/C orbits,22 RC fixed; no admissible length 27 or 49, each maximizer balanced. Source verify_bitmask.py and verify_direct.py implement complete independent representations. Recursion is a finite exhaustive proof for n=6,7 only; not an infinite-n extrapolation.

## originality

PASS

Originality survives only for the nontrivial REMAINDER: exact full intermediate-length populations at spans 6 and 7, all-order-seven maximal symmetry-orbit count 829, 22 reverse-complement-fixed and all-extremal balance/forced endpoints. Previously published results already establish optimal lengths 26/48, the complete order-six maximum 22 and six orbits, and apparently Mitchell 2026 also enumerates maximum-length aperiodic order-seven words. These known components must NOT be claimed as original; the submitted combined theorem still has independent length-refined and symmetry classifications not implied by those maximum-size statements. There is a material residual risk from inaccessible full Mitchell paper, explicitly recorded.

## value

PASS

The first nontrivial aperiodic orientable binary spans are natural finite benchmarks for position-sensing/sequence-design questions. Exact order-seven distribution N_7(L) at all feasible lengths and symmetry-resolved 829-orbit, 22 RC-fixed census plus universal boundary/balance constraints are independently useful unknown finite structural invariants, not just a duplicated maximum-length calculation. The complete finite search and certificates are substantial but do not, alone, prove value; the natural design/classification problem motivates them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
