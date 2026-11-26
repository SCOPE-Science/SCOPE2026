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

Reconstructed the fixed-force proof directly in calendar time, avoiding any inverse-hazard ambiguity on zero-force intervals. If v_I and v_R are the expected future repeat counts, their backward difference w=v_R−v_I solves w′=(1+φλ)w−φλ with terminal value zero, and v_I(t)=∫_t^∞w(s)ds. The kernel for w is positive wherever future exposure is positive, and ∫w is bounded by φH. Tonelli gives F(q)=∫[1−exp(−q x(s))]w(s)ds, with x(s) the accumulated common hazard. A nonzero integrable force has positive w on a positive-measure set with 0<x(s)<H. This proves the strict alternating derivative signs and the strict concavity bound; the normalized factor [1−exp(−q x)]/[1−exp(−qH)] strictly increases in q for 0<x<H by the truncated exponential likelihood-ratio comparison. This proves the strict upper bound and the per-primary comparison. The share formula is an increasing rational function of the per-capita ratio. Independently, in hazard time aggregate recovered mass solves dR/dx=1/R₀−φR, giving the stated aggregate Q from φ∫R dx. The unseeded positive orbit has I(x)=1−(1−c)e^(−x)−c exp(−θx)−R(x); e^(φx) I′(x) strictly decreases from a positive value to a negative limit. Thus I is positive until its unique positive simple root H. Finite seeds converge to that orbit in the interior in hazard time; conditional post-primary recovered probabilities solve the linear transition equation there, converge on compact interior subintervals, and are bounded by one. Dominated integration in hazard time therefore gives the limiting subgroup burdens, with initial infectives contributing at most seed mass times φH. Strictness follows on the limiting positive orbit itself (up to calendar-time translation), rather than by taking a limit of strict inequalities. For all-or-none vaccine action only a fraction θ enters the identical susceptible process; the quoted per-capita and per-primary identities follow.

## originality

PASS

Best-of-knowledge pass for the strict leaky subgroup ordering, resulting disaggregation bounds, and its fixed-force representation in this setting. The aggregate final-size and all-or-none relations are prior premises, not new. The general theorem about alternating derivatives of a Bernstein integral is standard; the contribution is identifying a positive time-to-go kernel for repeat burden and using it for the groupwise comparison.

## value

PASS

The two endpoints turn a known aggregate number into an interpretable interval for an otherwise unallocated subgroup burden. The strict comparison of repeats per primary distinguishes two mechanisms even though post-primary susceptibility is shared; the fixed-force theorem explains the role of primary-infection timing without claiming different total outcomes when the epidemic feedback changes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
