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

For each divisor d of n, the shift-fixed space V_d consists of d-periodic repetitions and is the cyclic module F_q[z]/(z^d−1). Because p does not divide d, the operator kills exactly the eigencomponents at roots of z^d−1 whose orders divide a or b. Inclusion–exclusion gives the stated gcd dimension, and inversion of counts by exact period gives the primitive indexed count. For A=gcd(n,a), B=gcd(n,b), the kernel is V_A+V_B. It is contained in V_lcm(A,B), and contains a vector of that exact period: when A≠B, sum nonzero vectors in the distinct order-A and order-B cyclotomic primary summands, which exist over F_q since the cyclic module includes each reduced cyclotomic factor. If A=B, use just one such summand. If neither stride is divisible by n, evaluation at a root of exact order n gives a nonzero operator; if one stride is divisible by n it is the zero operator. Proper divisors of a prime power form a chain, whereas two coprime nontrivial blocks of the prime-power factorization of a non-prime-power length realize lcm n. In the coprime case V_a∩V_b consists of the constants, so the sum map has q preimages and a primitive output of that sum map exactly when both components have full respective period. Equivalently, the divisor sum factors because each d splits uniquely as e·f with e|a, f|b and the exponent is e+f−1. The six-cell numbers are (25−5)(125−5)/5=480 and 5⁶−5³−5²+5=15480. The argument covers nonsplit cyclotomic factors, finite field extensions and zero operators under the stated hypotheses. The checker is a finite corroboration over three prime fields and gcd-class stride representatives; it was inspected, not executed. The stated 58,939 configurations and 110 stride-class comparisons agree with the loop ranges.

## originality

PASS

The supported distinction is the sharp mixed-stride primitive-to-zero boundary for a nonzero update, together with its exact census and product law. Cyclic polynomial gcd methods, cyclotomic splitting, primitive-word Möbius inversion and monotonicity of translation stabilizers are established ingredients and not new claims. The closest inspected statements treat all spatial stabilizers, only one noninvertible difference factor, a resonant temporal extinction clock, or a different primitive-word observable; none covers this mixed-stride classification on prime-to-characteristic rings.

## value

PASS

This asks when a nonzero local, shift-equivariant map can erase all information in a maximally translation-asymmetric input in one step even outside the resonant characteristic regime. The answer separates prime powers from mixed-prime lengths, identifies the specific stride criterion across all inputs, and gives an exact conditional probability in the coprime case. These are reusable structural and quantitative baselines for additive symmetry acquisition, not priority claims for the classical counting tools or a single numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
