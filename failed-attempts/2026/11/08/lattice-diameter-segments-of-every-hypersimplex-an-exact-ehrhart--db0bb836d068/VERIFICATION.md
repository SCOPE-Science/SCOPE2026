---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The coordinate box bounds primitive-segment length by t, and adjacent 0/1 hypersimplex vertices attain t. Every maximal endpoint difference is t times a balanced {-1,0,1} direction, with p positive and p negative coordinates and residual common tuple summing to (k−p)t; reversing orientations gives exactly the displayed factorial/2 count. The bounded-composition coefficient equals an Ehrhart polynomial, with unique highest-degree p=1 term and Eulerian leading coefficient. Cases k=1,n−1 and the empty residual tuple are handled. Independent full pairwise enumeration for n=4,k=2,t=2 found 21 maximal segments, agreeing with 6t+9.

## originality

FAIL

The published 2026-10-25 RESULT on binary polytope diameter segments contains precisely the same hypersimplex full formula, degree n−3, Eulerian leading coefficient, endpoint ranks, and the same proof by balanced signed supports plus free-coordinate bounded compositions. Algebraic identity: 1/2 C(n,p)C(n−p,p) E_{n−2p,k−p}(t) equals the candidate n!/[2(p!)²(n−2p)!] [z^{(k−p)t}](1+...+z^t)^{n−2p}. This is exact earlier coverage, not simply a possible source.

## value

FAIL

The exact segment count of a natural hypersimplex is mathematically motivated and correct, but the entire all-parameter calculation was already published October 25. The candidate does not extend, sharpen or repair it; rank-two and leading-degree statements are immediate specializations of the known expression. Its independent mathematical contribution is absent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
