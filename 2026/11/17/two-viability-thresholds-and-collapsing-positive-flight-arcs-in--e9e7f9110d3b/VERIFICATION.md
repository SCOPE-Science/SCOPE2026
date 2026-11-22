---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

On X,Y>0, principal square roots u=√X, v=√Y obey u′=(v−1)/2 and v′=(r−u)/2; therefore (u−r,v−1) is a circle with angular speed −1/2. The forbidden u≤0 and v≤0 closed phase intervals have half widths α and β and centers a quarter turn apart. The number of connected positive arcs changes at m=min(r,1), M=max(r,1) and at their overlap radius R=√(r²+1). A complete period exists only below m; one positive arc for m≤ρ<M, two for M≤ρ<R and one for ρ≥R. Multiplying angular lengths by 2 derives the stated durations, while differentiating α+β at R gives short-flight decay 2R(R−ρ)/r+O((R−ρ)^2). At X=0, the axis path and a delayed outgoing square-root harmonic arc share the same C1 derivative, establishing nonunique local nonnegative continuation. For r=1 the middle one-arc regime is empty. Numeric phase sampling cannot replace this exact proof.

## originality

PASS

The harmonic oscillator and squared explicit trajectories are established prior work; the narrowly claimed additions are a full maximal strictly positive component classification, exact collapse rate, and explicit non-Lipschitz boundary branching. The earlier original model discusses extinction/stopping, but not these complete topology and lifetime statements in read sections.

## value

PASS

Strict positivity and collision with extinction axes matter mathematically and biologically: an exact oscillator circle does not supply a physical phase portrait once principal roots change sign. The full natural positive-orbit classification, two component changes and exact lifetime collapse give useful, testable boundaries, even though the construction is elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
