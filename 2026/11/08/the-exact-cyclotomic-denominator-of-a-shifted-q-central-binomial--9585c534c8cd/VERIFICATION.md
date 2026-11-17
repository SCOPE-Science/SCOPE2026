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

For each d>=2 count cyclotomic exponent e_d from all original 1−q^h factors. If g=gcd(d,k)>=2, first numerator progression A=floor(n/(d/g))>=2floor(n/d), and the shifted progression includes the endpoint whenever d|kn+j, so e_d>=0. If g=1, unique shifted residue r mod d gives e_d=1_{r<=n mod d}−1_{r=n mod d}, which is -1 precisely when d divides both n and j, else >=0. d=1 exponent is zero. Therefore all negative orders are exactly nontrivial divisors of u, once each, yielding [u]_q and the radical iff. Independently enumerated 968 triples with all d<=kn+j and verified complete negative spectrum; finite test does not prove universal classification.

## originality

PASS

Straub–Moll–Amdeberhan 2008 Section 5 introduces precisely this q-product as a polynomiality problem and proposes gcd(n,j)|k as an iff; Straub 2012 dissertation repeats it without the corrected denominator. Earlier 2026 two-step Resultary theorem handles j=2k only and cannot imply the all-parameter denominator. Thus the full all-n,k,j radical criterion and exact rational denominator survive, while original family and elementary cyclotomic factorization are credited.

## value

PASS

It resolves a published natural all-parameter integrality problem and identifies a subtle repeated-prime obstruction missed by the proposed condition, with explicit exact denominators when nonpolynomial. An infinite counterfamily and a necessary/sufficient criterion are substantially more informative than a small counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
