---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A two-step return gives L(f_0+f_1)=0. Connectivity makes f_0+f_1 constant, and the values zero and two give fixed points, so f_1=1-f_0 for every primitive orbit. For a proposed cut each firing vertex loses k_v cut chips and each waiting vertex gains k_v; complementary threshold inequalities give exactly k_v choices per vertex, all in the stated height box. Conversely every such independent choice returns after two steps and has distinct firing sets, hence minimal period two. Counting once at the hub-wait phase, the hub contributes k, and the run-local cut degree gives the asserted four-state transition weights and labelled closed-walk trace, without a spatial quotient or extra factor of two. Expanding det(I-tT(z)) and logarithmically differentiating at z=1 gives t(1+5t+2t²)/((1+t)(1-3t-t²)); its denominator expands to 1-2t-4t²-t³. The coefficient at the 1/(1+t) term is obtained by evaluating t(1+5t+2t²)/(1-3t-t²) at -1 and equals 2/3. The other two terms give the claimed conjugate coefficients, and |λ_-|<1<λ_+ gives the stated scale separation. Independent replay: python3 /workspace/branches/review_checks.py 2, direct hub-wait states versus exact marked transfer coefficients for n=3–6 (totals 60,276,1125,4476). The frozen symbolic checker compares its polynomials at z=1 and prints examples; the new replay checks all marked coefficients at the tested sizes. Frozen checkers were inspected, not run.

## originality

FAIL

The earlier indexed fan-versus-wheel result 4649ebc87d0f already evaluates precisely this wheel census in Step 4, with the same marked T(z), periodic trace and hub-count differentiation. Its normalized rational series is identical, with the same dominant coefficient and explicit -1 pole. The bound marked polynomial, recurrence, radical formula and alternating coefficient are direct readouts of that exact prior calculation, not merely analogous results or possible inaccessible overlap.

## value

FAIL

Counting actual chip configurations on a natural graph family is worthwhile, but this particular calculation adds no independent invariant to the prior identical marked wheel transfer. Extracting the -1 coefficient by a one-point evaluation, or rewriting the rational series as a recurrence or radical expression, is routine. A stronger point such as mass-conditioned asymptotics is not proved in this frozen record. No surviving substantive repair is identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
