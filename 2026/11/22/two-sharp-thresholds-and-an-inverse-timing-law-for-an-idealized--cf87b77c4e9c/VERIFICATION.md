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

Normalize by B and set z=e^(−ht). The derivative divided by Bhz is 1−a g_r(z) with g_r(z)=z^(r−1)(r−(r+1)z). For r<1 this g decreases from infinity to −1; the unique stationary point is a maximum and H−B>0 near z=0. For r=1, g=1−2z, so the boundary a=1 is still strictly increasing at all finite times. For r>1, g has its only positive maximum at z_*=(r−1)/(r+1); 1/g_r(z_*) is exactly a_c. At equality the derivative has only an isolated zero, and above it the chronological sign pattern is +,−,+. Separately, at finite times H−B has the sign of a z^(r−1)(1−z)−1, and this latter shape reaches its maximum at z_g=(r−1)/r. Its reciprocal maximum is a_g. Since z_g>z_* and g_r(z_g)=z_g^(r−1)(1−z_g), a_g>a_c, and equality at B is attained once at a=a_g. This proves the finite maximum and unattained supremum cases. At rate ratio 2, the two phases satisfy sum 2/3 and product 1/(3a). The sum of exponentials is continuous and strictly decreases from 2 to 0 as h varies, and the distinct phases force a>3. Any one positive-time value recovers B by dividing by the positive normalized shape; times alone identify a, not A. Exact independent rational checks at a=3,4,25/3 reproduced the coalescence, plateau equality, and the 8/5 and 392/405 values. The supplied checker was read, not run; its finite comparisons do not establish global shape or statistical stability.

## originality

PASS

For the specified hypothetical index, the two inequivalent sharp thresholds and exact event-time identification are a distinct combined mathematical result in the inspected evidence. Fuel moisture and fuel load as wildfire predictors are not new. The closest exact indexed threshold result treats simultaneous dry exposure under periodic forcing, and the inspected primary fuel model computes fuel and moisture fields, not this product as a transient index. The calculus and Vieta methods are standard; no priority claim for the methods or for wildfire predictability is supported.

## value

PASS

The two thresholds answer different questions prompted by a two-factor hazard proxy: whether a rebound exists and whether the early peak was ever above the baseline. There is a whole region with a rebound but no baseline overshoot, rather than a single numerical illustration. The rate-two case is motivated by the particularly simple exact phase relation and gives an event-time identification diagnostic without a full curve; any distinct positive time pair can be fitted under the imposed ratio, so an independently measured rate or level is needed for a test beyond timing alone. Value is as a bounded shape and identifiability result, not a field calibration, fire probability or causal conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
