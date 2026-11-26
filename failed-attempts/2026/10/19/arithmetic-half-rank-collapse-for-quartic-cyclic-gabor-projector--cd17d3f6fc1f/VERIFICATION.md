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

With the stated shift convention the projector Gram is the convolution kernel |A(h,w)|² at h=a−c,w=b−d. For the character (a,b)↦ζ_N^(ua+vb), expanding the ambiguity square and summing over w sets the two sample indices a lag v apart; the h-transform factors as a modulus square. This gives N|A(−v,u)|² at the stated label, not only as an unordered spectrum. Fourier-character kernel directions of the projector Gram correspond to zero weights, while Weyl operator directions describe the intensity-lifting kernel. Centering s=t+h/2 gives 4hs³+(h³−w)s+wh/2. Modulo p, cyclotomic irreducibility makes exact cancellation equivalent to the cubic being a permutation. For nonzero linear coefficient b in ax³+bx, the off-diagonal collision conic u²+3v²=−4b/a has p−χ(−3) solutions (count the quadratic character by a split difference of squares), at most two with u=0; for p≥5 this forces a collision. For b=0, cyclicity gives the p≡2 mod 3 condition. Modulo p², the two-digit split leaves exactly the stationary residue contributions, without a simple-root restriction. For unit h there are zero, one or two such residues; two p²-th roots cannot cancel at odd p. For h=pH≠0 only w=pW can survive and the residue sum is exactly the already classified cubic 4Hx³−Wx. The h=0 row is orthogonality. Counting 1, then (p−1)(p−δ_p), then (p²−p)p(p+1)/2 gives the square-order rank, and the h=0 and nonzero-shift zeros give the prime-order rank. The frozen checker’s floating comparisons sort spectra and do not by themselves test labels. Independent replay /workspace/branches/frozen-review-replay.py checks unsorted character-by-character values from the first Gram row and checks exact exponent-histogram cancellations for p=5,7 at both orders; ranks 17,43,317,1219 and worst labeled error below 1.5e−14. The analytic classification, not finite evidence, proves all p≥5.

## originality

FAIL

Two distinct inspected Resultary records give exact coverage of the quartic cyclic support and lifting ranks, one at each order. Their catalogue path dates are later than the frozen path date, which does not establish who obtained the results first; the decision is about demonstrable known equivalent content and lack of distinct remainder, not provenance. The normalized, character-labeled Gram identity is the standard Weyl/ambiguity diagonalization, and combining the two exact rank cases adds only elementary counts and limits.

## value

FAIL

Half-rank collapse is a meaningful invariant for this window, but the precise support and rank are already covered in both orders. The joint presentation and permutation of Fourier labels add no comparably useful unknown fact. No experiment or motivation change can rescue originality of this same claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
