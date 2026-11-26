---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The Euclidean digit recursion gives the last-digit parity plus the bit at q(n)=floor(an/b). As n runs from 0 to M−1, q(n) stays still or rises by one, with its rising edges covering exactly the q(M) input edges. The last-digit difference is a−b[q(n+1)−q(n)]. For even a, a stationary edge contributes zero and a rising edge contributes the complement of its input change. For even b, a stationary edge contributes one and a rising edge contributes the complement. This directly proves C(M)+C(q(M))=q(M) for even a, or =M for even b, a check also valid off the block grid and at M=0. At M=bN this gives the claimed identity. With β=t/(a+b), the all-prefix relation gives E(M)=−E(q(M))+O(1), and q contracts geometrically to zero, yielding the claimed logarithmic discrepancy. The difference between counts of 01 and 10 telescopes to the endpoint bit difference. For odd a,b, induction through the same recursion proves x(n)=n mod 2. No separate mixed-parity equal-pair frequencies follow from this argument.

## originality

PASS

The supported distinct claim is the all-coprime-radix identity and its parity-controlled discrepancy and densities, not a new numerical observation or a new isolated 3/2 theorem. Cassaigne et al.'s published sliding-pair substitution already implies the exact standard 3/2 instance. The closest separate Resultary record treats a genuinely different 3/2 sequence under a different digit normalization.

## value

PASS

Exact transition statistics are natural in rational-base parity words, for which full pattern-frequency questions are nontrivial. The identity determines every radix's leading transition frequency with an effective sublinear error without relying on separate single-bit or equal-pair frequencies, and classifies the radically different both-odd case. The useful new benchmark is universal, not its already implied isolated 3/2 value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
