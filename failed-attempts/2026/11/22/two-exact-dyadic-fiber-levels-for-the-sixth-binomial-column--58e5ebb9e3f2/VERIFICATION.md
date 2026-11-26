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

With w=(n−2)(n−3)/2, each input parity gives a polynomial in the half-index whose difference quotient is odd; hence each permutes every finite quotient and w has two preimages at the stated levels. Exactly F=P(w)=w(w−1)(w−3)/90. When w=2u the resulting polynomial u(2u−1)(2u−3)/45 is an isometric permutation. For w=2u+1 it is 4B(u), with B(u)=(2u+1)u(u−1)/90. Each parity of u gives another odd-linear, even-higher-coefficient polynomial in the remaining index, hence an isometric permutation. At k≥2, for y divisible by four, each parity gives two lifts modulo 2^(k−1) from a unique residue modulo 2^(k−2), otherwise no lifts. At k=1 both odd w modulo four contribute to zero. The counts and Haar mixture follow including the factor two. The 2^(k+2) shift preserves w modulo 2^(k+1); the half-shift at n=2 produces valuation k−1 in P, ruling out all proper divisors of the proposed period. Independently using the numerator product modulo 720·2^k before exact division by 720, I enumerated all fibers and verified the shift over one full block and the half-shift witness for k=1,…,12.

## originality

FAIL

There is demonstrable equivalent coverage by two stronger indexed results, not merely a same-day thematic match. In the universal dyadic doubling theorem take m=3, L=2, and sum its exact class counts over r modulo four: each parity of the sixth column in a block of 2^(k+2) contributes exactly the third-column count in a block of 2^(k+1). In the Mersenne theorem take s=2, so the third-column count is 1+4·1_(4|y) for k≥2, and (3,1) at k=1. Doubling it gives the entire frozen law, including k=1 and the pushforward. Both catalogue records have the same displayed day as the assigned record; the coverage comparison does not establish who was first. The least period itself is also directly covered by an older external theorem.

## value

FAIL

The exact law is a natural output measure, and the direct proof is sound. But as a standalone new exact invariant of column six it is a mechanical specialization of two available stronger laws; the frozen finding establishes no distinct structural result beyond the covered census, period and measure. A shorter derivation of this exact instance does not change what is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
