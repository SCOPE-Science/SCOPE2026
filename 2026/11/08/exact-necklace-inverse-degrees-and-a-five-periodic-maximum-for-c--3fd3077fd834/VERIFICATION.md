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

Rule 12 outputs exactly the cyclic 01 transitions in the input. Nonzero feasible outputs have gaps d_i>=2; between consecutive output markers a predecessor has exactly one 10 transition and d_i−1 choices, independent between gaps. Repeated primitive gap pattern with repetition h has A choices per block; quotienting by the stabilizer cyclic group order h gives δ=(1/h)Σ_j A^gcd(h,j). For nonuniform gap multisets consecutive grouping yields primitive gap words, so the unquotiented product is attained. Integer-break local replacements force sizes 4 or 5; normalized ratios ρ_d=(d−1)/4^(d/5) bound any defect. A uniform all-5 output pays a strict necklace symmetry penalty, hence n multiple 5 improves by five 4-gaps for large n. Finite n<=20 checked in package, and independent brute-force ring enumeration n=5,8 returned maximal degrees 4 and 8. General proof not inferred from finite enumeration.

## originality

PASS

Jen (1989) explicitly calculates finite-linear Rule 12 preimage factorization; the result credits this known precursor. Fukś (2003) studies iterated preimages. The new object is one-step preimage orbits modulo cyclic spatial rotation, stabilizer-dependent degrees and sharp global maximum with period-five exceptions, which the examined linear-block treatment does not state. Resultary nearest matches for Rules 90, 110, 150 and other local rules are different maps.

## value

PASS

Maximum inverse ambiguity of finite cyclic Rule 12 is a natural dynamic invariant, and quotienting rotations creates genuine symmetry-driven changes to an otherwise classical integer-break optimization. The exact all-output Burnside formula and sharp period-five maximum are useful outside a small finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
