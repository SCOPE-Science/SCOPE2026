---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

With u_j=R(ix_j)-1, direct expansion gives q_j=|u_j|^2>0 and g_j=-2Re(u_j)/q_j>0 on the excited interval. The unique nonzero root gamma is the E_j q_j weighted mean of g_j; the squared modal multiplier is 1+q_j gamma(gamma-g_j). Summing proves conservation; multiplying by g_j before summing gives the negative weighted variance. Energy of the initial minimizing set increases by at least g_* min_M(q_j) E_M(0)(gamma-g_*). Bounded monotonicity therefore forces gamma->g_*, and the mean formula with bounded denominator forces each loser to zero. The limiting squared multiplier yields the claimed ratio on surviving losers. Exactly, g(rt)-g(t)=48(r-1)t^2 P_r(t)/(D(t)D(rt)); the proof's removal wording omits one harmless positive factor t. Endpoint signs +96(r+1), -48r and positive leading coefficient give the unique admissible root. At r=4, P_4(197/100)=-931/500 and Q(197/100)>Q(197/25), with 197/25<8, so the two corrections really select opposite winners within RK4 stability. Recorded VERIFY_OK 127 was inspected, not freshly run; independent bounded rational replay is /workspace/branches/957ea9b8-9f45-40d6-a345-3836be29f3a9/independent-check.py. The infinite-time conclusion is analytic; no assertion on allocation within tied winners or on rounding.

## originality

PASS

The known relaxation and the existence of modal transfer are not new. The finite-mode winner law, its explicit Lyapunov identity and exact increment-relaxation switch are distinct on the located evidence.

## value

PASS

Exact global energy conservation masks the loss of all nonwinning independent physical actions. The finite-mode law and sharp frequency-step diagnostic distinguish two widely relevant correction geometries at an identical stable base step; this is stronger than one observed transient or one isolated numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
