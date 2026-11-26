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

Every unital coefficient-field-fixing map preserves the nilpotent maximal ideal. On that ideal the commuting linear idempotents have mutually orthogonal simultaneous Boolean projectors given by products of E_i or 1−E_i. Applying the matching projectors to an arbitrary section of each cotangent weight space produces an equivariant section of the cotangent quotient; no multiplicativity of 1−E_i is needed. Send each linear generator to its value under this section. The full ideal-power truncation makes this an algebra map, and its invertible degree-one part implies invertibility on the finite associated graded and hence on the algebra. It intertwines the original tuple with the linear extensions. Ordered tuples therefore have precisely the simultaneous cotangent multiplicities as conjugacy data. The automorphism group has |GL_n(q)| q^(nH) elements. The stabilizer has block general linear group at degree one, and each generator's higher coefficients must lie in its own Boolean weight, since the homogeneous retractions evaluate each monomial by the bitwise meet of its input colors. The number of such coefficients is the stated symmetric monomial count (including the empty-color conventions); multiplying by the number of generators of each weight gives exactly the displayed exponent by orbit–stabilizer. Products retain r_I variables and have linear image dimension binom(r_I+d,d), including the unit when r_I=0. For n=t=2 there are four singleton orbits; the six two-color cases have a common linear factor q(q+1). Only the incomparable pair loses all mixed terms from the stabilizer's permitted coefficients, adding sum_{j=2}^d(j−1)=binom(d,2) to the orbit exponent. Independent substitution enumeration at n=2,d=3,q=2 reproduced 770 maps and 9,988 ordered commuting pairs, and extended the check to 69,896 ordered commuting triples with all 36 joint cotangent-rank profiles matching for the seven nonempty products. Replay: /workspace/review-evidence/5/check_binary_triples.py. That bounded test uses actual map commutation and compares cotangent ranks (equivalent to the asserted image-rank exponents here by the proved rank formula); it is not an all-field proof. The frozen verifier was inspected, not executed.

## originality

PASS

The overlapping Boolean-weight method and all-arity orbit classification in the earlier associative setting, and the prior commutative single-map work, are credited. The independently supported distinct claim is the ordered commuting-tuple orbit size and joint product image-rank census in the symmetric jet algebra, with its commutative mixed-monomial enhancement. The closest associative theorem counts ordered tensor words and does not state or directly imply these orbit sizes on the commutative quotient. No historical priority beyond the checked statements is asserted.

## value

PASS

Full maximal-ideal-power jets are canonical finite local algebras. Exact counts of the compatible substitutions and their product images answer a natural question left open by marginal retraction counts: homogeneous tangent data alone do not tell how much larger a nonlinear orbit is. The computed stabilizer shows a specific symmetric mixed-monomial effect, producing the incomparable-color enhancement at every truncation depth and giving a joint-rank enumeration for arbitrary arity. This is more than a change of variables in the tensor-word formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
