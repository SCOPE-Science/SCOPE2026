---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For q prime power and m>=3, original proof expands rank^t in kernel-subspace count functions and derives exact nonconstant rank-frequency Fourier multipliers. The rank-two multiplier Phi=(Q-a)+(qQ-q^3)*3^t-((q+1)Q-qa)*2^t is strictly increasing with unique beta in (0,1), and the other Fourier sectors stay negative up to beta. Endpoint nullity is rank-two frequency count a*(Q-1)*(Q-q), giving minimal Hilbert squared-distance dimension q^(3m)-1-nullity. Asymptotics follow derivative expansion. Independently checked q=2,m=3 critical root 0.34862420028772034, nullity 294 and endpoint dimension 217, plus algebraic identity of entire Phi with other published theorem.

## originality

FAIL

FAIL. Full published Resultary theorem Sharp generalized roundness of all three-column finite-field rank metrics establishes the same metric on M_{m,3}(F_q), identical root equation and rank-two endpoint nullity and Hilbert rank for all q,m. Explicitly published coefficient qt-(q-1)h-1 equals qQ-q^3 because (q-1)(q²+q+1)+1=q³. Its fixed-q asymptotic q ln(3/2)-ln2 equals q ln3-(q+1)ln2. The submitted additional fixed-m large-q expansion is an immediate derivative consequence of this prior exact all-parameter equation. Publication dates of both records are 2026-11-08, so no within-day chronological precedence is inferred; exact coverage is decisive for this publication audit.

## value

FAIL

FAIL for independent scientific contribution. The exact all-parameter classification, critical eigenspace and embedding rank already have an explicit full published theorem. A mechanical limit extracted from its identical root has not been motivated as a separate new exact invariant; repeated derivation and verification do not confer independent value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
