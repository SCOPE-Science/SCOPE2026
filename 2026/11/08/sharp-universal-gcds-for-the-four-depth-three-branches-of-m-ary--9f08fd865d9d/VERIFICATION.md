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

Pinned RESULT.md proves coefficient-ideal equivalence using F(q)=(1-q)^(-1)F(q^m), three U_m selections and T(q) with an integral power-series inverse and constant 1. The explicit K_3(n)=m^6*C(n+2,3)+B*C(n+1,2)+Cn is an integer-valued cubic with binomial-basis coefficient gcd determined by n=1,2,3. For p>=5, v_p(C)=3v_p(m); for p=2 the relevant exponent is 3v_2(m)-2; for p=3 the exact modulo-9 branch criterion caps the possible extra factor at one 3. Every m>=2 and (a,b) in {0,1}² is handled; the arguments m^4n-m-am²-bm³ are nonnegative. Independently regenerated both full coin-change and four-power truncated counts for m=2..12 (44 base-branch cases); verified individual truncated polynomial values and first-three actual full-sequence gcds. The full partition values need NOT equal K_3 coefficients termwise: their gcd ideals agree via convolution with T.

## originality

PASS

Best-of-knowledge: the earlier Rødseth–Sellers congruence provides m³/D_m as a divisor, whereas this theorem proves the exact universal gcd and its extra branch-specific factor 3 with three-term attainment. Żmija supplies high-order divisibility bounds, not the four shifted-branch exact ideal. No prior exact coincident table found; the search cannot prove total novelty.

## value

PASS

The exact all-n ideal of the four canonical shifted m-ary partition progressions, including its exceptional residue classes, resolves a natural gap between a known lower congruence modulus and actual sharp divisibility. Three-term certification is an independently useful finite reduction, not a routine restatement of the lower modulus; it has substantive p-adic content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
