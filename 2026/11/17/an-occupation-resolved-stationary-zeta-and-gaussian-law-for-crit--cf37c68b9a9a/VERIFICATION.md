---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Every original even 2×2 block is one 4-bit state a∈0..15. In the inspected original Critters rule each f(a) complements occupation and permutes block patterns. A fixed full even+odd step is exactly a cyclic word satisfying 16-state local conditions f(X(a,b))=Y(a,b) for adjacent original block labels, so Fm(u)=tr[diag(u^{|a|})M]^m, with no missing phase or quotient. The source SymPy program constructs all 256 edge possibilities and derives exact determinant (1−u²z)^5 [1−(1+u²+u⁴)z+(u⁴−u²−u⁶)z²−u⁶z³]. Independently rebuilt the 16-state graph (30 edges), checked 8-state primitive SCC and its (1−u²z)Q determinant, four other singleton loops, traces at m=2..5 (16,44,136,448), and reciprocal polynomial symmetry. PF analytic simple dominant root λ from X³−3X²−X−1 yields exact entropy and Gaussian quasi-powers, ψ'(0)=2, ψ''(0)=2.6898249; variance linear. Independent exhaustive C++ original-update source supports m=2..5; it is not an all-length proof.

## originality

PASS

Margolus’s original Crystalline Computation describes the precise complementing block rule, conservation across full steps and gliders but no width-two weighted fixed-point determinant or Gaussian stationary-occupation law in inspected relevant primary chapter. Marotta studies oscillators and dynamics in the distinct nonstrobing phase convention, explicitly identified in his text, not the same fixed-point ensemble. Resultary returned related parity/majority/cyclic-rule stationary findings with distinct local rules and the present record, not a dominating Critters stationary law. The archival 1987 Toffoli–Margolus book was not fully inspected, leaving a named priority risk; inaccessible literature alone is not O failure.

## value

PASS

Critters is a canonical nontrivial reversible partitioning automaton. Its exact fixed-configuration occupation distribution, spatial zeta, entropy and central-limit variance for an infinite strip family provide natural, independently useful spectral/statistical invariants. Width two is the first nondegenerate periodic geometry where the staggered block interactions are nontrivial; this is not merely recomputing a known tiny table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
