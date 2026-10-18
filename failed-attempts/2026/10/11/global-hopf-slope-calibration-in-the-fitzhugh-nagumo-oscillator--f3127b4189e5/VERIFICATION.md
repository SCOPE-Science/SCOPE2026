---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Reconstructed the exact autonomous FHN Liénard reduction and state-energy derivative L E=(1−εb−v²)(v′)². Invariance of compactly supported μ annihilates L E; a zero speed-square measure lies on equilibria. Equality εb=1 also excludes non-equilibrium recurrence. Conditional nullcline regressions follow from invariant antiderivative tests and their variance decompositions. Verified exact polynomial identities in actual verify.py; no simulation used as universal proof.

## originality

FAIL

Already implied by the classical model-specific Liénard energy balance used in Kostova–Ravindran–Schonbek (2004): their transformed energy derivative is minus damping times squared speed. Taking the invariant-measure expectation and inserting f′(v)=1−v² gives the precise boxed identity and threshold; it is a specialization plus stationarity, not an independent uncovered theorem. The coordinate conditional laws are standard generator identities. Lack of wording in indexes is not novelty.

## value

FAIL

Although weighted trace and εb<1 are interpretable for model dynamics, under the originality bar this is a direct energy-identity integral already available from standard Liénard analysis, with no independently motivated non-implied invariant, classification or new structural gap. The basic Bendixson divergence also supplies the global negative-divergence obstruction in the regime εb≥1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
