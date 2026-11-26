---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Folding at the origin gives the reflecting condition for the inactive component and the absorbing value for the active component; the reset destination remains x0 in the folded process. The gate-stationary average and state difference solve decoupled constant-coefficient equations with masses r and r+alpha+beta. Matching the two conditions reproduces both numerators and L, with L(1)=h(alpha+beta). Eventual detection follows from a positive per-cycle chance from either gate state. The discriminant decomposes into the stated square plus 4*T²*eta*q³*h*k. Positive sum and product, mean below one and L(1)>0 put both distinct modes in (0,1). For noncancellation, normalize L and the numerators by T and put u=1-q²z: L/T minus the active numerator is (1-z)u[1-h+eta*q*(1-k)], and the active numerator vanishes at neither possible common root. At a zero of the inactive numerator, d=h-q*k yields the stated resultant test R=(1-q²-d)+eta*q*(1-q²-q*d)>0, since d≤1-q by differentiation in x0. A constant inactive numerator is nonzero. At z=exp(-s*beta/r) the leading inactive numerator and denominator are h(1+eta)beta and h(1+eta)(1+s)beta, respectively. For fixed z<1 the slow-active and fast-gate specializations reduce to h/[1-(1-h)z] as stated. These are conditional particle-only reset counts. The finite-difference verifier was inspected, not executed; none of these quantitative checks requires it.

## originality

FAIL

The frozen finding credits first-passage time transforms as a different observable, but the exact conditional PGFs and the slow-inactive scaling are mechanically covered by the earlier same-model transforms, not just derivable from a previously known model. On a path stopped at absorption time H, changing the Poisson reset rate from r to rz multiplies the path density by z^K exp(r(1-z)H). Thus F_j(z;r)=E_{rz,j}[exp(-r(1-z)H)]; the already explicit conditional transforms in Żbik et al. give these exact PGFs by substitution (extend to z=0 by continuity). The slow count limit follows by the same substitution into their inactive transform and a first-order limit. The explicit no-pole-cancellation check for both initial states is additional exposition relative to those inspected equations, not a basis to pass the frozen novelty claim for the count laws and scaling. The later-dated stationary count theorem provides material exact overlap on its subcase, but is not evidence of earlier priority. No replacement is submitted: after removing the transform and scaling coverage, the isolated denominator check is routine two-state spectral algebra rather than a separately motivated surviving claim.

## value

PASS

Reset counts are a natural cost observable for search protocols, distinct in interpretation from elapsed time. The exact two-mode description and singular scaling make the retained gate memory interpretable, unlike a mere table of counts. This value of the scientific question does not establish novelty for its solution, and a fresh proof of just the two-state algebra without the covered laws would not justify replacement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
