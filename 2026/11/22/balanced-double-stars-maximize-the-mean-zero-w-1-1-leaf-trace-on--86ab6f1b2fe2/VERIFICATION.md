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

The proof of the exact cut expression uses the identification of mean-zero tree functions modulo constants with their \(L^1\) edge derivatives. A cut derivative contributes a vector with precisely two coordinate levels. Its squared norm is a strictly convex quadratic along each edge, reducing the supremum to endpoint cuts.

For any side with \(s\ge1\) complete edges, at most \(s\) original leaves are carried on that side when its cut endpoint is not itself an original leaf. Applying that fact to both nonempty sides gives the finite quadratic \(\Phi_N(s)\), whose integer maximum and double-star equality condition were checked algebraically. Cases with one isolated leaf give norm at most one and are handled separately.

Run `python check_leaf_trace.py` using the Python standard library. This executes complete labeled-tree enumeration for one through seven edges, integer-bound calculations through three hundred edges, and exact short-ramp diagnostics. The executed output ended with `ALL_EXACT_TREE_TRACE_TESTS_PASSED 325330`. These checks do not substitute for proof for arbitrary tree size or for external priority verification. Independent audit: not performed.
