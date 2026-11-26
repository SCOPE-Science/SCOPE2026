---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For an operator-rank-one map f(·)B, substitution in the bilinear identity and evaluation at f(X)=f(Y)=1 give B²=tB. Pairing a vector in ker f with one of f-value 1 forces f(B·)=αf and f(·B)=βf, with α+β=t and α²=tα, β²=tβ. In a field, t=0 gives both zero; t≠0 forces exactly one of α,β to be t, also in characteristic two. Normalizing B/t gives the unique idempotent on its line; P=I is excluded since its left and right actions both equal the identity. The annihilation condition gives f(B)=0 and hence R²=0 in both families. Over F_q a square-zero B is a flag im B⊂ker B plus an isomorphism V/ker B→im B. Under trace duality the allowable functional matrices C satisfy CB=BC=0 and are exactly maps V/im B→ker B, giving dimension (n−r)². Divide by q−1 for the nonzero scalar redundancy. An idempotent is its image plus a complementary kernel; the two functional spaces are the two off-diagonal block duals of dimension r(n−r). This verifies both sums, T₂(q), and T₃(3)=4160+3744=7904. The summand degrees n²−r²−1 and 3r(n−r) give the unique top square-zero rank-one term for n≥3 and the idempotent lead for n=2. A separate canonical-map basis-pair enumeration reproduced 15, 56 and 651 (split 315+336 for M₃(F₂)); from review-evidence/5 run python3 rankone_direct.py with argument pairs 2 2, 2 3, and 3 2. The run summary is rankone_direct_results.txt. The supplied check.py was not executed. These small prime-field counts do not establish the theorem for other fields.

## originality

FAIL

A distinct indexed full-matrix census states the same rank-one operator classification, count of actual nonzero maps and dominating asymptotic; the low-dimensional computations and leading-family switch are immediate evaluations of that count. This is a finding of equivalent coverage, not a claim about priority or derivation from catalogue path dates. Different-algebra, decomposable-tensor and complex orbit classifications are not substitutes for that exact match.

## value

PASS

The theorem has intrinsic structural value: it treats actual maps across all sizes and characteristics on a natural algebra, distinguishes two genuinely different image types, and identifies which one dominates and where that dominance changes. The value is in the uniform classification and census, not in recomputing the small numbers. Exact coverage of the result is a separate reason to reject it as a distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
