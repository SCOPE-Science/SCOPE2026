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

The transform numerator telescopes by the binomial theorem to (b+1)^5−32. Exact division by b−1 gives the two displayed monic quartics F,G. An independent support certificate is multiplication by G in Z[X]/(F): in order 1,X,X²,X³ the four columns are (30,25,15,5), (−5,25,20,10), (−10,−15,15,10), (−10,−20,−25,5); the determinant is 378125=5^5·11². If p divides both F(b),G(b), evaluation modulo p gives a nonzero functional annihilating this multiplication map, so p must divide its determinant. Checking complete residue systems gives common roots {1} modulo 5, {5,9} modulo 11, and no common roots modulo 25 or 121 (in particular, the lifts in each row of the frozen table cannot coincide). Hence the valuations are exactly the indicators, not merely upper bounds on support. The CRT gives 36,9,8,2 and minimal base period 55 since both nonconstant indicators have prime moduli. For b=2^k the two orders are 4 and 10 and the 11 classes correspond to k=4,6 mod 10. No nontrivial translation modulo 10 can fix these two classes: a swap would require their difference to be 5. Thus each period is a multiple of 4 and 10, and counting their joint residues gives 13,3,2,2. All arguments apply on the stated positive domains.

## originality

PASS

The inspected sources give the underlying sequence and transform, and treat nearby common-divisor families, but no distinct inspected statement gives the simultaneous value gcd of this pair at index five or a stronger theorem directly implying its residues and valuations. This is a bounded priority assessment.

## value

PASS

The repunit and its ordinary binomial transform provide a natural pair for studying their shared arithmetic, beyond closed forms for each sequence. Fifth index is structurally meaningful: at prime index two the difference of the two polynomials is 2, and at index three it is 3(b+2), while the repunit at b=−2 equals 3. Thus neither smaller prime index permits a common prime away from its index, whereas at five the prime 11 appears and has two distinct residue classes with no simultaneous square lift. Exact shared factors, not just resultant support, are needed to determine the periodic correlations of these sequences and their higher-order Mersenne specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
