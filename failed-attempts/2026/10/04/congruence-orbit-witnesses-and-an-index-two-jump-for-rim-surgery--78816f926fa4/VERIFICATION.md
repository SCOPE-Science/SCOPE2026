---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Niu's exact formula immediately identifies the two stabilizer cases. The sign map on the unoriented stabilizer has kernel the oriented stabilizer; a hyperelliptic involution acts as \(-I\) on integral first homology, hence trivially mod two and so preserves the Rokhlin quadratic form, giving an order-two splitting element. For odd \(p\), squared Dehn twists lie in \(H\) and realize arbitrary symplectic transvection coefficients mod \(p\); these transvections act transitively on nonzero vectors, yielding the stated orbit sizes and orbit-stabilizer lower bounds.

## originality

FAIL

The result is implication-level covered by Niu's exact stabilizer theorem together with standard mapping-class/symplectic facts. Niu already uses even Dehn twists to produce an infinite orbit; the two longitude-sign cases, split sign extension, and odd-prime orbit-stabilizer bounds require no new nonstandard lemma beyond reducing those same twists modulo \(p\) and using standard transitivity. Under the audit rule, such corollaries are covered even when the displayed finite numbers were not printed.

## value

PASS

Finite congruence witnesses and the exact sign-extension description are useful quantitative packaging of the extendability obstruction, even though they do not survive originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
