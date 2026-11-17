---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

On the nonnegative competitive LV orthant, a hyperbolic sink must have positive supported abundance, positive-definite symmetric supported interaction matrix, and strictly negative invasion exponents. For alpha<1 an occupied peripheral pair must contain both leaves (otherwise missing sibling invades); for alpha>1 both cannot coexist by the negative eigenvalue 1-alpha. Without hub, every pair must be occupied; hub invasion threshold is beta=(1+alpha)/(2k) or beta=1/k. With hub, beta>1 forbids all leaves by indefinite principal minor, and beta<1 forces each pair occupied, giving explicit arrowhead-supported abundances h=(1-k beta)/(1-k beta^2), y=(1-beta)/(1-k beta^2), or all-leaf symmetric formula with 1+alpha replacing pair degree. Positivity and definiteness coincide with the stated open chambers; no unlisted supports. Independently solved rational support tests for k=2,3 at alpha=1/2,3/2 and beta=.1,.4,.5,1.3, yielding stable counts 1,1,2,8,8,9 as appropriate. The infinite classification rests on support argument, not finite tests.

## originality

PASS

PASS for complete two-parameter phase diagram with explicit hub-present abundances, threshold switching, and exact all-k sink counts for a natural graph family. Earlier Hong–Pego exclusion/multistability framework and Fried clique results already explain the 2^k mutually exclusive peripheral choices in strong competition; not original in isolation. The inspected primary material did not give both hub competition thresholds or classify every open chamber at finite strengths. Potential parameter-specialization of a more general network theorem remains residual risk.

## value

PASS

A friendship graph is an elementary but natural motif for multistable competitive communities: one shared species interacting with k otherwise separated rival pairs. The classification locates real bifurcation boundaries between coexistence, exclusion, hub-only and bistability, and gives exact abundances and sink multiplicities for every k. More than generic clique counting; usable exact case study with experimentally meaningful finite competition strengths, without claiming basins or transition curve dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
