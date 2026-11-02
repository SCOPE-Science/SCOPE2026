---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Grossi–Moretti Theorem A establishes c2(X)=12, a Lagrangian Albanese immersion, one self-intersection pair. Their Lemma 6.1 itself explicitly gives [Z]^2=14 and the pulled-back class [W]=3([A x 0]+[0 x A])-[Delta]+H1H2 with W^2=126. Independently expanded the (1,6) NS intersection quartic 864(ab-c^2)^2: its fourth-degree monomial coefficients imply every integral product of two divisor classes on A x A squares to a multiple of 144. As 9[Z]^2=126 is not divisible by 144, a single integral Cartier divisor product on the quotient is impossible; no conclusion for rational combinations. This proves the statement but critically its inputs already come from the full published class calculation.

## originality

FAIL

Grossi–Moretti, arXiv:2502.13087v2, Lemma 6.1, already states the exact self-intersection 14 and more strongly supplies the *entire cohomology cycle class* [W] and computes W^2=126, with the displayed 144 term. The claimed integral-product obstruction is a direct one-step necessary-condition calculation from this stronger explicit class plus the textbook polarization intersection lattice; no new independent geometric classification or unprovided structural lemma survives. The original full class is stronger information than the binary obstruction even though that phrase is not printed.

## value

FAIL

The integral-product obstruction asks a motivated question about algebraic cycles, but here the full class and self-intersection were already determined in Lemma 6.1 of the primary source; checking 126 not a multiple of 144 is a short standard intersection-lattice deduction. It neither settles rational span nor the canonical complete-intersection question. As presented it is a mechanically implied consequence, not an independently valuable new invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
