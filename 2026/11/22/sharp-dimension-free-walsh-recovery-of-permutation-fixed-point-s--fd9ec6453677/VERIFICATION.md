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

XOR convolution is diagonal on the characters χ_A with probability-normalized multipliers. In the product of fixed-position signs, choosing j out of k labels contributes (−2)^j(n−j)! for each chosen set. This gives L_(n,k)=n! p̂_n(A), and subtracting adjacent binomial expansions gives L_(n,k)−L_(n,k+1)=2L_(n−1,k). The first four unnormalized rows are (1,−1), (2,0,2), (6,2,2,−2), (24,12,8,4,8); the binomial multiplicities give nullity two at n=2 and just one negative eigenvalue at n=1,3. The last entry is n! times the truncated exp(−2) sum. Odd truncations increase strictly from S_5=1/15; even truncations lie above exp(−2) and decrease to it. The positive fourth row then starts the induction: each later row is strictly decreasing in k with positive last term. This gives the n=4 minimum at k=3 and the unique n=5 full-weight uniform equality, and the maximum eigenvalue 1 gives the stated inverse norm and condition numbers. Inspected the supplied integer checker; a separate permutation enumeration through n=7 checked all 254 frequencies. The exact recurrence and alternating-sum argument, not that finite run, prove the all-order assertions.

## originality

PASS

Pass for the all-weight Boolean convolution inertia and sharp uniform spectral/conditioning theorem. The count polynomial, exchangeable labelled law, and full-character scalar are known or directly implied by known work. The closest indexed operators either change the group, embedding, or statistic, and none of the inspected comparators gives the minimum over all Walsh weights or its sharp uniform bound for this law.

## value

PASS

Exact inversion of convolution by a natural nonproduct Boolean law can be obstructed by zero or small Fourier multipliers. The proof isolates the only singular order and shows uniformly well-conditioned recovery in all positive orders, with a sharp amplification constant and its unique worst dimension and character. This solves an operator question left open by knowing the scalar fixed-point count alone, rather than just computing a short finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
