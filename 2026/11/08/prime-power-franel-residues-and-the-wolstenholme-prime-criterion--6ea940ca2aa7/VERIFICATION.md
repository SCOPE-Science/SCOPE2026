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

For 0<k<p^a, the remaining binomial coefficient in C(p^a,k)=(p^a/k)C(p^a-1,k-1) is a unit by Lucas, so the valuation is a-v_p(k). Only k=jp^(a-1) can contribute modulo p^4 after cubing, and at these indices C(p^a,k)/p reduces to (-1)^(j-1)/j. The endpoints sum to 2. For p≥5 the full reciprocal-cube sum is zero modulo p, leaving -1/4 times the half sum. Setting m=p-3, that half sum is (B_m((p+1)/2)-B_m(0))/m by Faulhaber's formula. The coefficients are p-integral since all Bernoulli indices are below p-1. The half-argument formula B_m(1/2)=(2^(1-m)-1)B_m and 2^(1-m)=8 mod p give the half sum -2B_m, hence the frozen coefficient B_m/2. Glaisher's classical binomial congruence detects the same Bernoulli zero modulo p. At p=2 the surviving unit sum is 1, and at p=3 it is 2 modulo 3, giving exact valuation 3 at every height. Divisibility by the cube of p^a for a≥2 requires valuation at least six, so only the stated nonexceptional cases are excluded by the frozen modulus.

## originality

PASS

The supported distinct result is the explicit Bernoulli coefficient for the Franel residue, its identification with the Wolstenholme exception and the small-prime valuations. The prime-power stability itself is covered by Straub's stronger theorem for p≥5, and the binomial/Bernoulli Wolstenholme criterion is classical. No independent matching statement for the remaining Franel coefficient was established in the strongest available comparisons; this is a bounded judgment, not a claim of historical priority.

## value

PASS

At canonical input indices for a known primality-test conjecture, this is an exact obstruction, not generic height stability: it explains why essentially the entire prime-power problem falls at valuation three and isolates the precise classical irregularity that can make that obstruction vanish. The small-prime valuations cover the boundary not covered by the cited general odd-prime height-stability theorem. This is useful even though the exceptional case requires finer digits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
