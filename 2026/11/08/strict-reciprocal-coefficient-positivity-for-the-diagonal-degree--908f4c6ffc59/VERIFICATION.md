---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

Verified the normalized diagonal [7/7] denominator term-by-term from the factorial formula, with constant coefficient 1. Independently reimplemented exact-Fraction Gaussian complex polynomial evaluation for four rational centers and their conjugates. The seven discs radius 10^-6 are pairwise disjoint, inside |z|<14, and each strict Rouché inequality holds with min positive rational margin about 5.08818e-9; the global bound sup |q''| <= 14.83776224 <15 is checked by rational coefficient majorization. Therefore all seven simple roots are isolated, including the unique positive real R near 9.9435737 with q'(R)<0. Independently verified 0<R<9.944, -q'(R)<0.0052, and the complex root modulus/derivative lower pairs (10.132,0.0071),(10.758,0.0202),(12.098,0.157). Hence positive real partial-fraction residue B>19 and conjugate coefficients have moduli below 15,5,1. At index n=32 the exact rational combined other-pole majorant 17.2853783363 is <19, and each modulus ratio is <1, proving c_n>0 for every n>=32, not only sampled n. The exact recurrence from q(z)c(z)=1 verifies c_0,...,c_31>0, with c_31 about 1.0287072e-30. All n>=0 are covered. Added checks n=32..99 are illustrations only. The source verifier and RESULT proof were read; an independent implementation performed the critical rational checks, not just a source VERIFY_OK log.

## originality

PASS

Best-of-knowledge original, exact all-index strict positivity for the normalized exponential diagonal [7/7] denominator. The 2019 Fasi–Higham paper formulates the sign statement as Conjecture 3.2, not a proof. Scardino arXiv:2610.39051v1 (2026) proves conditional eventual positivity if the real pole uniquely minimizes modulus and states that its large-k fixed-m theorem and nondiagonal counterexamples do not resolve diagonal k=m. Scardino does not provide the exact (7,7) root separation nor positivity of the finite prefix. The published degree 9 and 13 certificates, m=3 all-k theorem, and m=5 finite k spectrum concern different denominator degrees and do not logically cover m=7. Dunster et al. compute reverse Bessel zeros, and Wolfram 2024 inverse connection coefficients are change-of-basis coefficients, not inverse Taylor coefficients. Literature priority remains qualified because an uncatalogued equivalent finite-degree computation may exist; negative searches alone do not prove novelty.

## value

PASS

The scalar coefficient positivity property is a motivated exact mathematical boundary in the widely used diagonal Padé family for matrix exponentials. Degree seven is one of the standard practical diagonal orders and follows the already investigated odd degrees three and five, so its numerator/denominator orders are not arbitrary slicing. The result gives strict positivity for an infinite sequence of rational coefficients, supported by an independently reconstructed exact Rouché/residue inequality and a finite-prefix certificate. Earlier conditional pole theorems do not mechanically imply the seven-root separation or the 32 required finite signs, so this new exact order-seven fact is independently reusable for the positivity-dependent step of matrix exponential forward-error estimates. It has no claimed all-order generalization, new runtime bound, or paper-sized result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
