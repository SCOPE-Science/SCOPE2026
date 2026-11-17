---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For odd p^k, the quadratic equations X^2-sX±1 have invertible 2 and roots of unit constant term, so their root existence is equivalent to squarehood of L=s^2-4 and R=s^2+4. The L and R roots do not intersect modulo p; away from their two or four exceptional classes the indicator is (1+χ(L))(1+χ(R))/4. The mixed character sum χ(s^4-16) equals -1-a_p by substitution u=s^2 and u=4v, where a_p is the Frobenius trace of y^2=x^3-x. Omitting the exceptional classes gives integer G_p=(p-5-2δ-2(1+δ)ε-a_p)/4. All ordinary qualifying residues have p^(k-1) lifts. At each exceptional root the vanishing discriminant has a unit derivative, so Hensel identifies its lifts with multiples of p; Q_(p,k) counts exactly those multiples which are squares, yielding factor (1+δ)(1+ε)Q_(p,k). CRT gives the multiplicative intersection for all odd m. For p=3 every local factor is zero; for p>=5 an ordinary or exceptional witness exists according to p mod 8, establishing emptiness iff 3|m. Independent direct unit/inversion enumeration confirmed the exact formula and criterion for every odd 3<=m<=529, including prime powers; this supports, but does not prove, unrestricted result.

## originality

PASS

The exact claim survives bounded search at best current knowledge, subject to explicit source inspections and residual risks. Neither theorem implies local intersection G_p plus singular lifting Q_(p,k) or empty iff 3|m; checked 2012 full text defines and counts marginal sets only. Inaccessible 2009 paper remains residual risk.

## value

PASS

The intersection of two natural one-coordinate images of a modular inverse hyperbola is not determined by their separate cardinalities. The exact trace of a fixed CM elliptic curve together with all singular p-adic lift factors gives a usable full arithmetic invariant over every odd modulus and the unexpectedly sharp 3-divisibility disjointness test. It connects natural quadratic-image overlap to a nontrivial genus-one correlation rather than an arbitrary chosen number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
