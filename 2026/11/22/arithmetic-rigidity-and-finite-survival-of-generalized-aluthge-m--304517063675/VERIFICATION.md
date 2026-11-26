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

The polar formula gives the binomial average of logarithmic weights; telescoping gives (1). An m-isometric shift gives a polynomial of degree at most m−1 by forward differences, and conversely all starting-vector moments are translates divided by a positive constant. The candidate has degree deg P by its asymptotic at positive infinity. After setting x=1/z and removing z^(−deg P), each real power is a holomorphic germ chosen at a nonzero leading coefficient. The integer samples accumulate at z=0 and yield (2). In each root orbit the first moment of a_h−r_h is kλ times the positive integer orbit mass, forcing rational λ. With λ=u/v, reduction mod v^k at the last root and induction downward force every root multiplicity to be divisible by v^k because (v−u)^k is a unit. Conjugate pairs and normalization give a real root Q. For even v, the product of translates of Q with integer exponents is proportional to R with positive proportionality, as seen at large positive x. Its sign at the last exceptional integer would be negative because the exponent of Q(n) is odd. For odd v there is no sign ambiguity. This checks necessity as well as the explicit converse, the constant exception and strict order. The degree bound is attainable by powers of x+1. The frozen check_examples.py was inspected as supplementary finite evidence, not executed; the proof supplies all iterates and does not assume positivity between integers.

## originality

PASS

The complete all-iterate classification, including the integer-sign condition, is distinct to the best of current evidence. The best verified previous scalar examples and the simultaneous ordinary 2-isometry restriction overlap with consequences but do not give the iff, rational denominator power, or survival depth. This is not a priority certification.

## value

PASS

This resolves the scalar positive weighted-shift version of the higher-order/generalized preservation problem with a sharp lifetime, not just a counterexample. Irrational obstruction, denominator depth, and the independently necessary sign test separate exact preservation from formal perfect powers. These distinctions classify a natural transform across all finite orders and all interior parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
