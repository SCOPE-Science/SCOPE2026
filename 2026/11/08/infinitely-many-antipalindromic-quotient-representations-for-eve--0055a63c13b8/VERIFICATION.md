---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For r>=2 and t>=1 set Q=2^(2r), b=Q-3*2^(r-1), c=b-Q/2+1, x=c-1, y=b+1. Direct blockwise reverse-complement identities show both explicit B=[b,x^t,c,y^t,b]_Q and A=[b-1,Q/2,0^(t-1),1,Q/2-1,(Q-1)^(t-1),Q-2,Q-b]_Q are canonical binary antipalindromes. Base-Q borrowing establishes A=(Q-1)B, with denominator length exactly 2r(2t+3), strictly increasing in t. The base cases t=1 and r=2 have no empty-block ambiguity. Independently evaluated 56 cases with a separate exact-integer construction. The unbounded claim rests on symbolic identities, not finite experiments.

## originality

PASS

Bai–Meleshko–Riasat–Shallit prove infinite quotient multiplicity for a different even integer family and exact finite multiplicity for the neighboring odd plus family 4^i+1. Their numerical table includes 15 and 63 but no all-r minus-family theorem. Their algorithm for individual quotients does not itself supply uniform infinite multiplicity for every 4^r-1. Current indexed searches did not find stronger coverage; residual priority uncertainty retained.

## value

PASS

Infinite representation multiplicity is a primary mathematical question for binary-antipalindromic quotients. The natural odd Mersenne family is separated by a genuine multiplicity transition from the neighboring 4^r+1 family. A single infinite construction uniform in r, not a table lookup or trivial arithmetic substitution, has independent mathematical use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
