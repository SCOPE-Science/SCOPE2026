---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Integer compositions by block sums reduce L_a(q) to weights binom(r+a-1,a-1) under pairwise sum constraints. Splitting z^{r1+r2+r3-min r}/(1-z) yields the exact minimum-layer generating identity F_a=1/(1-z)^{3a+1}+sum_{t>=1}z^{2t}A_{a,t}(z)^3. The top t-degree 3a-3 coefficient is ((a-1)!)^-3(1-z)^-3 and yields a strictly nonzero pole at z=-1 of order 3a-2 with principal coefficient (3a-3)!/(2^{3a+1}((a-1)!)³), excluding period collapse. A full-dimensional Ehrhart pole at z=1 has order 3a+1. Independent height enumeration and constituent interpolation at a=2,3 recover the claimed leading alternating coefficients 1/128 and 1/8192. This is a valid unrestricted analytic proof, not an inference from finite checks.

## originality

FAIL

An October 25 stronger all-odd-cycle theorem already proves exact period two and the leading parity constituent difference. Specializing m=3 and dividing constituent difference by two yields the submitted Q coefficient and hence the same negative-pole order.

## value

FAIL

The exact leading parity term and minimum period are a routine m=3 specialization of an older, stronger full odd-cycle theorem; the reduced generating denominator follows from its nonzero parity degree. Repackaging this as a pole calculation adds no distinct motivatably unknown fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
