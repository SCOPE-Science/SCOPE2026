---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The exact K_n family is fibred as an L-space knot; its hyperbolic complement gives pseudo-Anosov monodromy. Published Δ_{K_n}(t)=((t^{4n+5}+1)(t^{4n+2}+1))/((t+1)(t²+1)) equals the characteristic polynomial of A=(φ_n)_* on H1 for genus g=4n+2 (monic degree 2g). With a=4n+5 odd and b=4n+2≡2 mod4, P=(t^a+1)/(t+1) and Q=(t^b+1)/(t²+1) are polynomials with simple roots, and cannot share a root since z^a=z^b=-1 would imply z³=1 and z^b=-1. Thus A is diagonalizable over C. P retains primitive ζ_{2a}, Q retains primitive ζ_{2b}; all roots have orders dividing 2a or 2b. Hence ord(A)=lcm(2a,2b). Because gcd(a,b)=gcd(3,4n+2) is 3 iff n≡1 mod3, the displayed piecewise formula and minimal Torelli power follow exactly. No assertion is made about finite geometric order.

## originality

FAIL

The entire exact-period assertion is an elementary, logically forced corollary of the specific factorized Alexander polynomial published by Baker–Kegel (2024), together with classical monodromy/Alexander identification. For a=4n+5 odd, b=4n+2=2 mod4, the two quotient factors are squarefree and have no shared root (common root would obey z³=1 and z^b=-1). Each retains a primitive 2a- or 2b-th root, so the already published characteristic polynomial forces exact order lcm(2a,2b), exactly the claimed formula. The 2026 unique-strong-inversion theorem contributes an unrelated descriptive property, not new H1 period information. This is mathematical implication coverage, not merely a missing title or an unsuccessful novelty search.

## value

FAIL

The homological period and first Torelli power are indeed natural invariants for a fibered knot, but this specific computation is no more than a standard cyclotomic-root-order extraction from Baker–Kegel’s fully factored all-n Alexander polynomial. The only added checks are separability, gcd of the exponents (differing by three), and an lcm. The mod-three variation is the elementary gcd(4n+5,4n+2), not a new structural knot phenomenon. The 2026 uniqueness of the strong inversion has no stated mathematical interaction with the homological action. Thus the submitted theorem does not fill an independently unknown or non-implied mathematical gap; it is a routine consequence of published formulae rather than a motivated new classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
