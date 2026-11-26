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

Modulo u coprime to 6, A and B are finite permutations, inverses are forward powers, and (AB)(BA)^{-1} translates by 2, covering u. Modulo 3N for odd N, C, AB and B hit each of the three families given full projection at N, so every odd modulus is full. Applying A reaches all even classes at m=2·3^b·u. Every odd word must end in a last C followed only by j copies of B, giving x+1=2·3^j(3s+2); for j<b the normalized ternary unit is 1 modulo 3, for j>=b it is in the terminal residue. Conversely an allowed j<b class fixes s modulo the odd 3^(b−j−1)u, which is attained. For the terminal class j=b gives all u lifts because 3 is invertible modulo u. Shells are disjoint, sizes sum to u(3^(b+1)+1)/2, and the inverse-limit odd slice has mass sum of 3^(−j−1)=1/2 (the limit point has mass zero). Together with the full even slice the Haar mass is 3/4; it is not integer density. Independent fixed-point set checks for m=6,18,378,4050,16038 confirmed the full predicted images (sizes 5,14,287,3050,12034), via python3 /workspace/branches/independent-reproduction/arithmetic_review.py. Frozen checker inspected, not run.

## originality

FAIL

The distinct indexed six-profile record explicitly covers the entire u=1 parity–ternary classification, its limiting mass, and the identical terminal-word formula. The only apparent enlargement is the coprime cofactor, and it follows directly on combining that proof identity with the indexed locality theorem's odd-modulus surjectivity. For j<b the condition on x= B^j C(s) divided by 2·3^j gives one class of s modulo 3^(b−j−1)u, an odd modulus. For the terminal residue take j=b and solve for s modulo u because 3 is a unit there. Even branches are A applied to every class modulo 3^b u. Thus every base-image class simply has all u lifts. The same-day records establish material statement/proof coverage, not chronological ordering.

## value

FAIL

The parity–ternary local image is a natural and useful invariant, but the precise base classification and Haar mass are already covered. Multiplying the modulus by a coprime cofactor yields exactly the mechanically determined full product lifts, not a new local obstruction or a separately valuable exact invariant in this submission.

The dated certificate retains the supplied scientific assessment, sources and limitations.
