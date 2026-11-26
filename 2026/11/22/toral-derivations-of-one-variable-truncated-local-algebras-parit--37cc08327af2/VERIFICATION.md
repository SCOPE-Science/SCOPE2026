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

Every derivation is determined by f=D(t), with N t^(N−1)f=0. Outside characteristic two, the second Leibniz identity and idempotence force 2f²=0, so any nonzero f has valuation at least 2, in contradiction with ff'=f. In characteristic two, D² is a derivation; the same valuation estimate excludes f of valuation at least 2. A unit f forces f'=1, and for valuation 1 the annihilator is (t^(N−1)), which forces f'=1 because the derivative has degree at most N−2. This yields exactly the stated coefficient affine space in each parity. The same argument over residue fields of primes of the coefficient ring identifies the reduced locus, not only its k-points. The h images of the odd powers are independent by their distinct lowest degrees. With a=f(0) the coordinate s=f−a has linear coefficient 1 and D(s)=s+a; rescaling when a≠0 gives the second normal form. This second class can occur only at even length and is distinguished by failure to preserve the maximal ideal. Counting parameters gives the enumerator and orbit sizes. Independently enumerating all coordinate substitutions over F2 and F4 at N=3,4,5,6 confirmed the nonzero orbit sizes (for example, 16 and 48 over F4 at N=6).

## originality

PASS

The inspected sources contain close toral normal forms and related enumerators, but do not establish the arbitrary-length, ordinary composition-idempotent classification with its parity-dependent automorphism orbits. Search evidence does not establish priority.

## value

PASS

The composition-idempotent condition distinguishes the characteristic-two ordinary toral case from all other characteristics. The result classifies these operators as derivations of the algebra rather than just as projections on its underlying vector space. In particular the two even-length nonzero classes have the same rank but differ by how they act on the maximal ideal, a distinction invisible to the rank enumerator alone. This is a complete classification for the natural arbitrary-length family; no value is claimed for coefficient counting by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
