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

# Verification evidence and limits

Execute `python3 verify.py` in the same directory as `RESULT.md`; only the Python 3 standard library is used. The source constructs all 729 six-column states and all admissible seven-column transitions from the definition, identifies the unique cyclic component (117 states, 241 arcs), finds and checks integer potentials, and computes the complete degree-117 determinant modulo \(t^5\) by exact integer Newton identities. It asserts the exact nonzero determinant coefficient support at all characteristic degrees, providing a finite proof certificate for the unrestricted residue result.

The verifier also independently builds the graph-neighborhood ESI predicate and enumerates all 3-state column assignments directly for \(3\le n\le11\), comparing every maximum and its multiplicity, with additional transfer counts for lengths seven through eleven. Terminal output `VERIFY_OK` means all checks passed. These numerical cases supplement, rather than replace, the local-equivalence proof and exact finite characteristic certificate. Historical priority and mathematical judgement have not undergone independent audit.
