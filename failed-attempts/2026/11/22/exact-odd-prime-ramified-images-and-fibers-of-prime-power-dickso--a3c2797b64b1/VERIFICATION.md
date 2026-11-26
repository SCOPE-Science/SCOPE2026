---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The Laurent substitution X=z+z⁻¹ gives D_n(X)=z^n+z⁻n, composition, the Frobenius reduction, and D_p′(X)/p≡(X²−4)^((p−1)/2) modulo p. In the coordinate x=a+pu away from ±2 the linear term has exact factor p²; higher terms are divisible by p³ since all inner coefficients in the shifted Taylor expansion are multiples of p and the top term has p^p. At ±2 the derivative is p² and the degree-two coefficient is ±p²(p²−1)/12, as follows by expanding the Laurent identity at z=±1. The quadratic term in u thus has factor p⁴ for p≥5, as do the higher terms including the top term. The resulting unit-linear polynomial plus p times an integral polynomial is a surjective isometry after normalization, giving valuation gains 1 and 2 on the respective branches. D_p(x)≡x mod p makes the gains additive under iteration and the isometry maps smaller balls onto the balls of exactly the corresponding depths. At finite k, branch size p^(k−1) divided by p^max(k−1−rh,0) gives the constant fiber size, and disjointness modulo p permits summing the sizes and their second moments; the measures are those of the full balls. A translation period must be divisible by p and testing in a nonexceptional branch forces v_p(T)+r≥k. The same inequality suffices on both kinds of branch, proving the stated minimum including k=1.

## originality

FAIL

A distinct indexed result on prime-index Dickson polynomials already gives the normalized polynomial models that determine exact distances on every one-step branch for parameter one. The frozen family uses no new input to pass from those models to r steps: classes are preserved and the known one-step isometries compose on all subballs. The image and finite counts, collision moment and least additive translation period then follow directly. This is demonstrated mathematical coverage, not a chronology claim about two records with the same catalogue date. The uncertain scope of the 1991 paper is not the basis for failure.

## value

FAIL

The whole-ring fiber profile would be useful if it required a new local classification. Here the ordinary and exceptional normalized one-step maps, including their full p-adic domains, are already available. The different exponent merely iterates those same contractions; counting, collisions and the least translation period are immediate arithmetic of the already determined branches. The exact restatement is a useful corollary but does not have a substantive remaining scientific gain as an independent finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
