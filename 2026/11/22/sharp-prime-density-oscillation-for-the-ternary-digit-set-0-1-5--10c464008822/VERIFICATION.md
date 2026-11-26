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

Reading ordinary trits low-to-high, the carry after each step is the difference between the read input and its forced output digits divided by the corresponding power of three. Since D is a complete residue system and its digits are nonnegative, inputs below 3^N are representable iff the carry after N trits is zero. The independently reconstructed maps on (-3,-2,-1,0) are (-1,-1,-2,0), (-1,-2,0,0), (-2,0,0,-1). The word 021 resets every state, and the stationary weights scaled by eight are (0,1,2,5). For a fixed most-significant prefix, the unconditioned low-trit block approaches this law; the prefix imposes successive Boolean pullbacks of the terminal zero test. This proves the stated cylinder-mass recursion, with H_e=8F; each depth-m cylinder has mass at most 8*3^(-m), giving continuity. Independent integer enumeration regenerated 14 states and all 42 transitions; the minimum slack of each of the two families of 42 barrier inequalities was 0, and each of the four restricted-root inequalities had zero slack. Induction on ternary endpoints and continuity yield the barriers for all t in [1/3,1]. The root first-level weights are 5,7,3, so F(1/3)=5/24 and F(2/3)=1/2. Dividing by t gives 5/8 and 3/4; a full log-period lies in this interval, with the claimed attaining phases (no uniqueness needed). Zhou's Theorem 1.1 gives the continuous profile and O(1) count error in the complete-residue case. Theorem 1.4 applies since gcd(0,1,5)=1 and gives the same prime-proportion profile up to O(1/log X). Taking sequences X=3^(m+u) proves both sharp prime limits.

## originality

PASS

The periodicity, prime-transfer theorem, and exact digit-system example are due to Zhou. The added result is the sharp image of the profile and particular attaining phases, hence sharp prime-density liminf and limsup. The inspected prior statements and the related catalogue summary do not derive those all-phase inequalities.

## value

PASS

For the primary nonstandard ternary example in the motivating paper, qualitative oscillation leaves its entire attainable numerical range unknown. The exact two endpoints and explicit attaining subsequences answer that natural question for both the integer profile and the primes; the finite certificate supplies bounds valid at every real phase.

The dated certificate retains the supplied scientific assessment, sources and limitations.
