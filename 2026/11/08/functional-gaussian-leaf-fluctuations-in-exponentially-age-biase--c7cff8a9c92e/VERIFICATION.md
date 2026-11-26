---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The corrected RESULT.md preserves the claim and repairs its variance proof. In the frozen conditioning at multiples of three only B_t is exposed; if B_t=0 a longer lag can still hit t-1 from a future selected time, so the frozen measurability assertion does not follow. The corrected proof additionally exposes H_t when B_t=0. The remaining choices are independent Bernoulli switches on disjoint pairs; future switches cannot hit t-1, so the event E_t is now measurable. When H_{t-1}=1 and no future edge hits t-1, one pair contributes conditional variance r/(1+r)^2. Independence across times gives P(E_t)=(1-r^2)(1-r)*mu_r/r and density 1/3 of switch sites gives exactly the claimed lower bound. Independently, the one- and two-point products follow by avoiding respectively one and two possible parents at each independent arrival; the product defect is bounded by r^{-2} sum_h p_h p_{h+d}, summably in d. Deleting long crossings from future times gives exponential strong mixing and the bounded strongly mixing invariance principle applies. The exact finite-tree coupling changes only a summable number of parents and has a uniform exponential-moment bound on the number of future edges across each cut; it gives O(log(n+2)) almost-sure maximal error and bounded single-time L^2 error. These transfer the functional law, almost-sure density, bounded mean error and normalized variance. For r approaching one, the aggregate denominator and product-linearization errors are O(1-r), using sum_{h,d>=1}p_hp_{h+d}=r/(1+r) and max_d sum_h p_hp_{h+d}=O(1-r). Uniform attachment has the usual one-leaf Bernoulli recursion giving density 1/2 and normalized variance 1/12; at fixed finite n its moments are continuous up to r=1. For r approaching zero, 0< v_r<=mu_r(1-mu_r) and mu_r<=r. Independent finite-product diagnostics, not the frozen checker, give at r=1/2 mu about 0.2887881, R_1 about 0.6270959 and v about 0.0892541, above the lower bound about 0.0160438. This is corroboration rather than an asymptotic proof.

## originality

PASS

The correction changes the proof, not the claim. The exponential birth-label model and general mixing tools are prior work; the distinct result is their use to identify the full leaf-count trajectory limit with a signed, explicit nondegenerate variance and noncommuting ordered boundary. The closest inspected primary statements and distinct catalogue records do not imply that combination for these weights.

## value

PASS

For a natural weighted recursive tree, the result gives a usable functional variance, a rigorous positive lower bound despite strictly negative spatial correlations, and a concrete discontinuity between weak label preference and exact uniform attachment. This explains a fluctuation feature invisible to single-vertex degrees. The repair retains these conclusions and supplies the conditioning needed to establish the variance lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
