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

For x=(a,b,c,d)=|w|², distinct powers of the shift occupy distinct diagonals; the squared resolvent norm is 5+E+Q with Q=ab+cd+bc(1+a)(1+d). Reflection flips both differences p=a−d and q=b−c; a strict improvement is possible if pq<0. At fixed A=a+d and B=b+c the exact difference multiplied by 16 is −(B²−q²)p²−(A+2)²q²+8pq. If A,B>0 and q=0, p=0 is necessary. If q=B>0 then p=A is necessary. At 0<q<B a maximum with p<A uses p=4q/(B²−q²)>0; after eliminating p, the objective difference in z=q² is 16z/(B²−z)−(A+2)²z, with strictly positive second derivative. An unsaturated point has an open feasible z-neighborhood and cannot maximize. A=0 is already outer-zero; B=0 yields Q=0 and is suboptimal. Thus the equality reduction is exhaustive, not just a symmetrization inequality for values. On d=0, fixing b>0 forces a=c via their product; the resulting cubic has derivative 2E+(2E−8)y−6y², positive at 0 and negative at E/2, with just one positive root. Reflection handles a=0, and b=0 cannot win on d=0. The palindrome derivative is 2F(u,s−u). For u>0 the positive root v*(u) of F(u,v) has F_v>0 and lies below u+2, so F_u=v²−(2u+2)v−1<0 there. Consequently u+v*(u) increases continuously from zero to infinity, giving one interior maximum, with the derivative positive at the left endpoint and negative at the right. The phase and tie cases follow. For E≤1, dropping v² to its upper bound E²/4 and completing the square yields P≤E²/4+E⁴/12, below the broken trial E²/4+E³/32 when E<3/8. For E≥10, the equal-four trial minus the broken bound is at least E²(−1/16−5E/864+E²/256)>0, since the bracket is positive at 10 and increasing thereafter. Continuity gives a tie, not uniqueness. This independently reconstructs the all-real-budget proof; CHECK.py and VERIFICATION.md were inspected as finite corroboration, not executed or used to prove the reduction.

## originality

PASS

On inspected evidence, the exact fixed-energy value and all optimizers for the length-four edge path survive as a distinct claim. The finite path resolvent expansion itself is routine and is not the originality basis. The strongest inspected neighboring results fix the weight multiset, fix the numerical shadow, or bound an operator norm under a contraction hypothesis; none determines the fixed-budget sparse-versus-palindromic classification.

## value

PASS

Fixed squared gain is a natural allocation constraint, and the squared Hilbert–Schmidt inverse norm measures aggregate response in all basis directions. On the first path where the outer-zero and positive palindromic allocations compete, the proof gives a global design reduction and the complete extremal profiles, and demonstrates that an edge must be inactive at sufficiently small budget but active at large budget. The structural support change and equality classification, rather than evaluating a single finite polynomial, are the contribution. No operator-norm, larger-chain, or unique-transition claim is credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
