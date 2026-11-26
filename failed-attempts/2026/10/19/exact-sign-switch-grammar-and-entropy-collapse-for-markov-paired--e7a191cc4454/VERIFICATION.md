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

FAIL

The gap rule, entropy and asymptotics are correct for the closure of the coded itineraries, but the stated ambient-open-interval realization on the stipulated all-future coding domain is false. The backward orbit of 0 contains both turns: they map to ∓κ and those points reach 0 after n more steps. If a nonempty open interval U avoided the full backward orbit, then for every j its image T^j(U) would be an interval avoiding 0 and both turns, by induction on the affine branches. Its length would be λ^j times that of U, contradicting the length bound 2. Thus the deleted set is dense, not merely countable, and the residual domain contains no ambient open interval. The branch proof produces ambient intervals for finite-time cylinders, whose intersections with the residual domain still have full measure in those intervals and are relatively open. Also, either initial half can be chosen for a switch word; a sign word itself already fixes that half. On this corrected interpretation each switch lands in J of the new sign, T^j(J) stays on that side through j=n, and T^n(J) is the full open half. The two onto return blocks 0 and 10^n prove all admissible finite words occur after deletion of the exceptional countable set. The marker-word recurrence gives ρ^n(ρ−1)=1; with u=n(ρ−1), taking logs gives u≤O(log n) and u exp(u)=n(1+o(1)), and κ∼2^(−n) gives the leakage expression. Independent numerical corroboration compared all 12,276 finite sign words for n=1–6, lengths 1–10, by propagating intervals split at the turns and zero and clipping each successive image to the required half. That calculation tests finite cylinders, not ambient openness on the residual domain.

## originality

FAIL

The correct finite language and entropy are direct deductions from the previously displayed branches and critical-orbit calculation for this very parameter sequence. Neither an independent new dynamical estimate nor a new Markov partition is needed. The inspected earlier text addresses the full operator and need not explicitly name the sign factor for this implication to hold.

## value

FAIL

A comparison between observation entropy and microscopic expansion is well motivated. Here, after correcting the domain wording, the proposed exact difference is just the two-block count from already published critical-orbit and branch geometry, followed by a standard scalar-root asymptotic. There is no distinct structural claim left to support a repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
