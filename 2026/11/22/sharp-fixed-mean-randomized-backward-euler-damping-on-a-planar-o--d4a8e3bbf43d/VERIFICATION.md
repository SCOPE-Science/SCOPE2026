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

Backward Euler is a scaled orthogonal map, with squared gain f(t)=1/(1+2at+r²t²). Independently, the slope magnitude of the chord from (0,1) is (1−f(t))/t=(2a+r²t)/(1+2at+r²t²); the derivative has the sign of r²−(2a+r²t)². For r>2a its unique peak at s=(r−2a)/r² gives a global supporting line touching only at 0 and s, and f is strictly convex from s onward by the displayed second derivative. At an interior mean of the affine face, equality in the line bound fixes the two masses. For h>s the tangent of the convex minorant has a unique contact at h on the whole half-line; at h=s the first supporting line restricts the support to {0,s} and the mean forces the point mass. For r≤2a strict convexity holds even at the r=2a boundary (f''>0 for t>0). The lower bounds apply to arbitrary finite-mean laws by the affine supporting-line inequalities. Replacing the zero atom by ε and reweighting gives the positive-only nonattainment result; i.i.d. stages multiply the expected gains. The rational example and positive approximants were independently spot-checked.

## originality

PASS

Qualified pass for the complete integrator-specific partition of regimes and optimizing laws, not for convex envelopes, random time stepping, or the deterministic backward-Euler transfer function. The strongest available indexed statements either change the one-stage gain or change the constraint and objective. No covering result was established after the stated comparisons.

## value

PASS

A complete boundary classification for a standard integrator answers when variance can actually improve a natural mean-square damping metric and whether any strictly positive law attains it. The exact split is more useful than a local failure of Jensen: it specifies the optimizer for every mean and reveals the skipped-stage obstruction. Its value is as a benchmark, not as a speed or accuracy claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
