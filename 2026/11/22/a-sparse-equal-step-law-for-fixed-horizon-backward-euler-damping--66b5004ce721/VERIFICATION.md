---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For the normal damped rotation, the backward-Euler resolvent is complex multiplication with squared modulus 1/q(h), so the worst-state ratio is independent of the state. On the compact nonnegative simplex maximize product q. Holding z=x+y fixed makes q(x)q(y) a quadratic of xy with strictly positive leading coefficient (a^2+b^2)^2. Every unequal positive pair is interior in the xy interval and can be strictly improved by going to one of its endpoints. Thus every optimum is an equal-positive-support schedule, not merely some optimum. For b<=a, log q is strictly concave (its second derivative is strictly negative for t>0 even at b=a), proving unique uniformity. For b>a, log q changes curvature once; t(log q)'−log q starts at zero, increases and then decreases to minus infinity. Consequently log q(t)/t is uniquely maximized at ell>0 and the only integer candidates are the clamped floor/ceiling bracketing H/ell. The derivative of D_k=(k+1)log q(H/(k+1))−k log q(H/k) has sign of a^2−b^2+a(a^2+b^2)(x+y)+(a^2+b^2)^2xy with x=H/(k+1), y=H/k. This strictly increases through zero with H. D_k starts at zero, decreases then increases, and takes opposite strict signs at k ell and (k+1) ell. The disjoint open brackets give distinct ordered transitions, each with exactly the adjacent tie. If requiring positive lengths instead, attainment holds exactly when all-N support is among the minimizers, including its boundary tie; otherwise approximation by positive schedules gives the unattained infimum. The large-H conclusion follows by bracketing and clamping if liminf N/H>=1/ell. Independently computed all four exact support candidates in the stated four-solve example: 4/25, 256/1681, 46656/274625, 16777216/88529281; independent bisection gives the stated two transition values to the shown precision. Inspected supplied check.py, VERIFICATION.md and saved output, without executing the uploaded script.

## originality

PASS

Pass for the arbitrary-N deterministic oscillatory backward-Euler allocation, including rigid optimal supports and the ordered staircase. The b=0 result is covered, and Jensen applies to the concave portion of the present parameter range. Neither the scalar case nor same-day analogues are credited as novelty; no same-day publication order is inferred.

## value

PASS

A finite solve budget and a fixed endpoint time are natural constraints when deliberately optimizing numerical damping rather than fidelity. The classification rules out all unequal optimal steps, finds when unused opportunities are optimal, and reduces arbitrary-N design to a staircase or two scalar candidate evaluations. The four-solve comparison shows a substantial damping difference, not a claim about solution accuracy, physical dissipation or speedup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
