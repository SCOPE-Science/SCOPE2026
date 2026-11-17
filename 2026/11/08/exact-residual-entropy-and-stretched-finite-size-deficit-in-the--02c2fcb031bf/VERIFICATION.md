---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Reconstructed the complete 27-boundary-triple minimum-plus-count recursion, color-orbit AAA/AAB/ABC reduction and induction on consecutive minima x,x+1,x+2; root-edge costs show E_t/J=(3^(t-1)+1)/2, D_t=18b_t+6c_t. Independent exact recurrence at t=0..6 gave (energy,degeneracy) (0,6),(1,36),(2,72),(5,216),(14,6480),(41,468163800),(122,5643087076554259583661696). The recurrences for r_t=a_t/b_t imply s_(t+1)=2s_t+eps_t and u_(t+1)=3u_t+Delta_t; superexponential growth and summable tails yield log D_t = c 3^t - k 2^t +log18+o(1). Finite check supports, not replaces, induction/asymptotic convergence.

## originality

PASS

Best-of-knowledge original surviving core as compared against named prior and mathematical implications. Finite exact counts implicitly covered by older Tutte partition; explicit stretched deficit not established there.

## value

PASS

The remaining genuinely new precise invariant is the two-scale thermodynamic asymptotic of an explicitly motivated frustrated planar hierarchical spin system: a positive entropy density with negative stretched 2^t finite-size deficit. It answers how the zero-temperature ground-manifold count approaches its extensive entropy; exact finite counts alone are already implicitly known through Tutte and are not used as standalone value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
