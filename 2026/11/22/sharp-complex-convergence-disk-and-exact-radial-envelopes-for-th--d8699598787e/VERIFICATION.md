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

The tangent series converges on |z|<π/2 and its coefficients are all positive by the recurrence from T′=1+T². Removing the linear term bounds |N(z)| by A(|z|). Equality at positive radius requires the cubic and quintic terms to have the same argument, hence z²>0. A(t)/t increases strictly from 0 to infinity, so the unique R solves A(R)=R and A contracts radii below R. Monotonicity and closure of [0,R] under A give the iterated upper bound without hitting a pole; oddness and N(r)=−A(r) show both real extremizers attain it. For n≥1 and r>0 these are the only maximizers; at n=0 all boundary points attain the same maximum. Since A(t)/t³ increases, iteration of the cubic bound on [0,r] gives the claimed exponent (3ⁿ−1)/2 for r<R. The open disk is connected and attracts to zero. Each nonreal point of its critical circle maps into the disk and belongs to the immediate component by its radial segment to zero. The two real points alternate and obstruct any larger centered disk; |N′(±R)|=A′(R)>A(R)/R=1, giving repulsion under the return map. π-periodicity of tangent translates the statement. An independent bounded calculation gave R≈1.165561185207211 and passed 135 sampled root, orbit and modulus checks; the supplied check.py was inspected, not rerun. Neither numerical check establishes the universal claims.

## originality

PASS

Credit the published real cycle, real-axis boundary, and numerical proposal for the centered disk. The supported distinct claim is the analytic complex inclusion and precise circle contact, together with exact all-iterate radial maxima. Bounded searches and comparison support this distinction, not absolute priority.

## value

PASS

This gives an exact geometric boundary for a natural Newton iteration and resolves a published numerical centered-disk claim. It distinguishes points on the first-contact circle that enter the basin from the only two obstructions, and gives sharp worst-case errors at every finite iteration, not just an asymptotic local convergence order. The known real number alone is not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
