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

The characters of the full binary group diagonalize unnormalized counting convolution; the eigenvalue is exactly the signed sum over all ideals, with the empty ideal contributing 1. An ideal containing the root is specified independently by its restriction to each child, so W=1+ε∏W_i. The total ideal count alternates even/odd starting with 2, and the signed sums have that same parity. At odd heights a product of d≥2 even integers is zero or divisible by four, so +1 is the only unit coefficient and occurs exactly when some child sum is zero. At even positive heights a zero requires all child sums at the preceding odd height to be +1 and exactly one root sign. Under uniform independent frequencies this gives the asserted recurrence with the root factor 1/2, starting at 1/2 for the single vertex. I independently regenerated all five positive rational Bernstein minima for d=2,…,6, so g_d(z)<z for 0<z≤1/2 there. For d≥7, 7(3/5)^7=15309/78125<1/5 and d(3/5)^d decreases, giving g_d(2/5)>2/5. The sign of the log-ratio derivative comes from d²/[sum_{j=0}^{d−1}(1−z)^(-j)]−1, which strictly decreases in z; together with g_d(z)/z→0 at zero and g_d(1/2)<1/2 this proves exactly two positive fixed points on the stated intervals. There are none above 1/2 since the map on [0,1] is at most 1/2. The increasing map's descending orbit from 1/2 stays above the larger fixed point and therefore converges to it.

## originality

PASS

The comparison supports a bounded claim about the rooted-poset Walsh zero distribution and its branching transition, not a claim to new convolution diagonalization or new general tree recursion. The nearest inspected exact Walsh comparators change the support or ambient coordinates. The scalar recurrence has an equivalent alternating Bernoulli-gate interpretation, but a recurrence in another model would not by itself identify the Fourier zeros of these order ideals; possible priority for the scalar threshold itself remains a separate risk.

## value

PASS

The full-group nullity measures recoverability from convolution with an ancestor-closed configuration family, not merely the number of such configurations. It gives exact lost-mode counts at all heights, complete invertibility for one parity, and a sharp switch from asymptotically negligible to positive lost-mode density in the other parity at branching seven. The threshold is a meaningful feature of a canonical tree family, not a selected frequency slice or a table of small cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
