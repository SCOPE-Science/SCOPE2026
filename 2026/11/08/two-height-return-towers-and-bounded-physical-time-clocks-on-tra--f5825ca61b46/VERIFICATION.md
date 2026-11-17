---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The four explicit translations map the long corridor through exactly 4n exterior indices: the nonzero index permutation is j->j+(2n-1) mod 4n and gcd(2n-1,4n)=1. The short corridor returns after 2 steps. Total tower lengths 2L+(4n+1)eta fill the original interval, so no omitted excursion. The induced rotation has wrap count floor((x+kL)/(L+eta)); consequently the long count is k minus that wrap count and t_k=2k+(4n-1)H_k, giving a bounded coboundary. A direct independently implemented exact-Fraction four-piece IET verified the return and roof across 1200 representative base states, n=1..4; the unrestricted proof is the permutation arithmetic. Uniform x has two possible wrap counts, giving the advertised mean/variance; rational u/v rotation has u+v returns with v long and u short excursions, so least original period exactly 2u+(4n+1)v. The original half-open map handles endpoints; geometric statement excludes ambiguous planar branch endpoints.

## originality

PASS

PASS, limited to the explicit physical-time return roof, two-point clock law and realization of least original-map periods. The original geometric construction and induced circle rotation are already published and not novel. Mechanical/Sturmian balanced coding follows from classical rotation arithmetic; the model-specific return height and global integer original-time law are substantive additional facts, not simply restatements of an induced map.

## value

PASS

Original physical time and induced-return time differ by long excursions 4n+1, so the two-tower roof and uniformly bounded clock variance answer a mathematically meaningful dynamical question ignored by a bare circle-rotation classification. The exact least-period spectrum in the original nonuniform-time map is useful for classifying actual cap orbits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
