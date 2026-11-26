---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For odd N at most one cyclic gap exceeds N/2, so the endpoints can be cyclically labeled with opposite paired gaps a,c<N/2. Their pair sums have positive lengths 2cos(πa/N), 2cos(πc/N) and direction difference π+π(b-d)/N. The squared norm therefore equals four times the sum of the squared cosine difference and the nonnegative direction-error term. If a≠c, successive cosine drops grow strictly on the relevant interval, and equality needs paired gaps 1 and 2, with b=d. If a=c, odd parity gives b≠d and N-2a≥3. The norm is 4cos(πa/N)|sin(π(b-d)/(2N))|, bounded below by 4sin(3π/(2N))sin(π/(2N)), the same minimum. Equality needs a=c=(N-3)/2 and opposite gaps 1 and 2. Both cases give the cyclic word (1,m,2,m); its reversal is a rotation and it has no proper period, even at N=5. For even N a zero sum pairs antipodes: a prescribed nonzero sum of two unit vectors determines the unordered pair, so the pair summing to its negative is the negated pair; when the pair sum is zero both pairs are already antipodal. This includes N=4. The stated normalization, Taylor constant and equality reindexing at a unit k all follow.

## originality

FAIL

Full equivalent coverage is established in the distinct same-day Resultary finding 2026/11/22/SCOPE-sharp-four-sample-two-mode-cyclic-fourier-designs-and-their-pari--3754c9ae0870. Its design objective is a strictly decreasing function of the identical distinct-site four-root modulus, and it gives the same constants, equality sets and odd asymptotic for all N≥4. The primitive-frequency corollary is a bijective reindexing, not a remaining case. This is scientific coverage in the frozen record comparison, not evidence about within-day priority; neither chronological precedence nor copying is inferred.

## value

FAIL

The four-distinct-site optimum is a natural and useful invariant in isolation, but the exact quantity and optimizer family are already supplied by the demonstrably equivalent design theorem. The primitive relabeling, cyclic-gap notation and Taylor expansion give no independent mathematical increment. The alternate gap proof verifies the theorem but supplies no separate valuable exact result beyond the covered claim. There is no distinct surviving claim to repair within the frozen scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
