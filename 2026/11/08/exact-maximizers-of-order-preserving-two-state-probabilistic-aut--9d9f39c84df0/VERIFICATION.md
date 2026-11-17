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

Writing the probability in the first state as x converts any 2x2 row-stochastic letter matrix to f_a(x)=q_a+(p_a-q_a)x; nonnegative determinant makes the update monotone. For acceptance in the first/second state, upper/lower envelopes optimize at each step. Their iterates form a monotone orbit, and active distinct affine functions must have strictly ordered slopes along that orbit, forbidding any return to a letter after a different active letter. A unique word forces strict action at each prefix. Conversely the explicit rational f_(a_i)(x)=(r+(i-1)eps)x+c−eps*sum_{h<i}T_h have ordered crossing thresholds T_i between baseline orbit points. The orbit error is <=1/(5000 n^2), strictly below the half-spacing 3/(64n); all f maps send [0,1] strictly inside (0,1) with positive slopes. The prescribed runs are the only greedy itinerary. Counting ordered distinct run labels and compositions gives the formula. Independently enumerated all run-distinct words q=2,3,4 through length 6 and matched the expression; this is corroboration, not proof.

## originality

PASS

Gill’s 2024 theorem classifies unrestricted *binary* two-state PFAs and includes alternating motifs requiring orientation-reversing letters; it does not determine the all-alphabet orientation-preserving model. Kjos-Hanssen’s 2026 three-state upper bound supplies existence for unrestricted words, not a minimal-two-state constrained if-and-only-if theorem. Resultary adjacent decreasing-two-state parity-run obstruction concerns the opposite sign of determinant. The monotone-affine envelope formulation was explicitly compared. Best-of-knowledge passes; an older affine control/greedy-envelope theorem could contain a close equivalent.

## value

PASS

The order-preserving determinant restriction is an intrinsic stochastic dynamics condition, not a mere arbitrary word subset, and admits a complete finite-alphabet structural classification with rational positive witnesses. Exact enumeration separates polynomially growing accepted families for fixed q from all q^n words, and also explains the new role of orientation reversal in unrestricted binary witnesses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
